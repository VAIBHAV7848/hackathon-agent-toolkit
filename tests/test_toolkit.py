from __future__ import annotations
import contextlib
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
import hashlib
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import install as installer  # noqa: E402


class InstallerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "project"
        self.project.mkdir()

    def call_cli(self, *args: str) -> int:
        # Source structure is checked once in a dedicated test and in CI. These
        # tests focus on installer behavior and avoid repeated subprocess scans.
        argv = ["install.py", "--no-validate", "--project", str(self.project), *args]
        with mock.patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return installer.main()

    def test_successful_install(self) -> None:
        self.assertEqual(self.call_cli(), 0)
        for name in installer.SKILL_NAMES:
            self.assertTrue((self.project / ".agents/skills" / name / "SKILL.md").is_file())

    def test_default_refuses_to_overwrite(self) -> None:
        target = self.project / ".agents/skills/hackathon-observer"
        target.mkdir(parents=True)
        (target / "custom.txt").write_text("keep", encoding="utf-8")
        self.assertEqual(self.call_cli(), 2)
        self.assertEqual((target / "custom.txt").read_text(encoding="utf-8"), "keep")
        self.assertFalse((self.project / ".agents/skills/hackathon-builder").exists())

    def test_dry_run_does_not_create_agents_directory(self) -> None:
        self.assertEqual(self.call_cli("--dry-run"), 0)
        self.assertFalse((self.project / ".agents").exists())

    def test_check_passes_then_detects_drift(self) -> None:
        self.assertEqual(self.call_cli(), 0)
        self.assertEqual(self.call_cli("--check"), 0)
        target_file = self.project / ".agents/skills/hackathon-observer/SKILL.md"
        target_file.write_text(target_file.read_text(encoding="utf-8") + "\nlocal edit\n", encoding="utf-8")
        self.assertEqual(self.call_cli("--check"), 1)

    def test_upgrade_backs_up_existing_skill(self) -> None:
        target = self.project / ".agents/skills/hackathon-observer"
        target.mkdir(parents=True)
        (target / "custom.txt").write_text("user content", encoding="utf-8")
        self.assertEqual(self.call_cli("--upgrade"), 0)
        backups = list((self.project / ".agents/.hackathon-ai-toolkit-backups").rglob("custom.txt"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(encoding="utf-8"), "user content")
        self.assertTrue((self.project / ".agents/skills/hackathon-builder/SKILL.md").is_file())

    def test_failed_staged_copy_leaves_no_partial_install(self) -> None:
        original_copytree = shutil.copytree
        def fail_during_copy(src, dst, *args, **kwargs):
            dst_path = Path(dst)
            if Path(src).name == "hackathon-builder":
                dst_path.mkdir(parents=True, exist_ok=True)
                (dst_path / "partial.txt").write_text("partial", encoding="utf-8")
                raise OSError("simulated partial copy failure")
            return original_copytree(src, dst, *args, **kwargs)
        with mock.patch("install.shutil.copytree", side_effect=fail_during_copy):
            self.assertEqual(self.call_cli(), 1)
        self.assertFalse((self.project / ".agents/skills/hackathon-observer").exists())
        self.assertFalse((self.project / ".agents/skills/hackathon-builder").exists())
        self.assertEqual(list((self.project / ".agents").glob(".hackathon-ai-toolkit-stage-*")), [])

    def test_upgrade_failure_restores_original_skills(self) -> None:
        target_root = self.project / ".agents/skills"
        for name in installer.SKILL_NAMES:
            target = target_root / name
            target.mkdir(parents=True)
            (target / "original.txt").write_text(f"original-{name}", encoding="utf-8")
        real_replace = os.replace
        failed = False
        def flaky_replace(src, dst):
            nonlocal failed
            src_path, dst_path = Path(src), Path(dst)
            is_staged_builder = (
                src_path.name == "hackathon-builder" and src_path.parent.name == "skills"
                and ".hackathon-ai-toolkit-stage-" in str(src_path)
                and dst_path == target_root / "hackathon-builder"
            )
            if is_staged_builder and not failed:
                failed = True
                raise OSError("simulated second-skill replacement failure")
            return real_replace(src, dst)
        with mock.patch("install.os.replace", side_effect=flaky_replace):
            self.assertEqual(self.call_cli("--upgrade"), 1)
        for name in installer.SKILL_NAMES:
            target = target_root / name
            self.assertEqual((target / "original.txt").read_text(encoding="utf-8"), f"original-{name}")
        self.assertEqual(list((self.project / ".agents").glob(".hackathon-ai-toolkit-stage-*")), [])

    def test_symlinked_agents_root_is_rejected(self) -> None:
        external = Path(self.temp.name) / "external"
        external.mkdir()
        try:
            (self.project / ".agents").symlink_to(external, target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symlink creation is unavailable on this platform")
        self.assertEqual(self.call_cli(), 2)
        self.assertFalse((external / "skills").exists())

    def test_nonexistent_project_fails_without_creating_it(self) -> None:
        other = Path(self.temp.name) / "missing"
        argv = ["install.py", "--project", str(other)]
        with mock.patch.object(sys, "argv", argv), contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(installer.main(), 2)
        self.assertFalse(other.exists())


class ToolkitSanityTests(unittest.TestCase):
    def test_source_validation_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "validate_toolkit.py")],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_version_and_required_skills_present(self) -> None:
        self.assertEqual((ROOT / "VERSION").read_text(encoding="utf-8").strip(), "1.1.0")
        for name in installer.SKILL_NAMES:
            self.assertTrue((ROOT / "skills" / name / "SKILL.md").is_file())


    def test_release_build_is_valid_and_reproducible(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            release_root = Path(temp_dir)
            first, second = release_root / "release-a", release_root / "release-b"
            for output in (first, second):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "scripts/build_release.py"), "--output-dir", str(output)],
                    cwd=ROOT, capture_output=True, text=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            zip_a = first / "hackathon-ai-toolkit-universal-v1.1.0.zip"
            zip_b = second / "hackathon-ai-toolkit-universal-v1.1.0.zip"
            self.assertEqual(hashlib.sha256(zip_a.read_bytes()).hexdigest(), hashlib.sha256(zip_b.read_bytes()).hexdigest())
            with zipfile.ZipFile(zip_a) as archive:
                self.assertIsNone(archive.testzip())
                self.assertIn("hackathon-ai-toolkit-universal-v1.1.0/README.md", archive.namelist())
                self.assertIn("hackathon-ai-toolkit-universal-v1.1.0/LICENSE", archive.namelist())

    def test_license_and_public_project_docs_present(self) -> None:
        for name in ("LICENSE", "LICENSES.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "SUPPORT.md", "CHANGELOG.md"):
            self.assertTrue((ROOT / name).is_file(), name)


if __name__ == "__main__":
    unittest.main(verbosity=2)
