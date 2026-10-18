#!/usr/bin/env python3
"""Safely install, check, or upgrade the Hackathon AI Toolkit skills.

Uses only the Python standard library. By default, existing skills are never
modified. --upgrade keeps a timestamped backup and rolls back on failure.
"""
from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SKILL_NAMES = ("hackathon-observer", "hackathon-builder")


def tree_digest(root: Path) -> str:
    """Hash relative paths and file bytes, ignoring runtime cache files."""
    digest = hashlib.sha256()
    for path in sorted(root.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts or path.suffix == ".pyc":
            continue
        rel = path.relative_to(root).as_posix()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        digest.update(b"\0")
    return digest.hexdigest()


def validate_sources(package_root: Path) -> bool:
    validator = package_root / "validate_toolkit.py"
    if not validator.is_file():
        print(f"ERROR: missing package validator: {validator}", file=sys.stderr)
        return False
    completed = subprocess.run([sys.executable, str(validator)], cwd=package_root, check=False)
    return completed.returncode == 0


def contains_symlink(root: Path) -> Path | None:
    """Return the first symlink in a source tree, if any."""
    if root.is_symlink():
        return root
    if not root.exists():
        return None
    for path in root.rglob("*"):
        if path.is_symlink():
            return path
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Target project directory (default: current directory)")
    parser.add_argument("--dry-run", action="store_true", help="Check the plan without modifying files")
    parser.add_argument("--check", action="store_true", help="Compare installed skills against this package")
    parser.add_argument("--upgrade", action="store_true", help="Replace installed toolkit skills after backing them up")
    parser.add_argument("--no-validate", action="store_true", help="Skip source validators (not recommended)")
    args = parser.parse_args()

    if args.check and (args.dry_run or args.upgrade):
        parser.error("--check cannot be combined with --dry-run or --upgrade")
    if args.dry_run and args.upgrade:
        parser.error("--dry-run cannot be combined with --upgrade")

    package_root = Path(__file__).resolve().parent
    source_root = package_root / "skills"
    project_root = Path(args.project).expanduser().resolve()

    if not project_root.exists() or not project_root.is_dir():
        print(f"ERROR: project directory does not exist or is not a directory: {project_root}", file=sys.stderr)
        return 2

    missing = [name for name in SKILL_NAMES if not (source_root / name / "SKILL.md").is_file()]
    if missing:
        print("ERROR: package is incomplete; missing SKILL.md for: " + ", ".join(missing), file=sys.stderr)
        return 2
    for name in SKILL_NAMES:
        link = contains_symlink(source_root / name)
        if link is not None:
            print(f"ERROR: refusing to install a skill tree containing a symlink: {link}", file=sys.stderr)
            return 2

    if not args.no_validate and not validate_sources(package_root):
        print("ERROR: source validation failed; nothing was installed.", file=sys.stderr)
        return 2

    agent_root = project_root / ".agents"
    target_root = agent_root / "skills"
    if agent_root.is_symlink() or target_root.is_symlink():
        print("ERROR: refusing to follow a symlink at .agents or .agents/skills; inspect the target and resolve it manually.", file=sys.stderr)
        return 2
    targets = {name: target_root / name for name in SKILL_NAMES}
    existing = [name for name, path in targets.items() if path.exists() or path.is_symlink()]
    target_symlinks = [name for name, path in targets.items() if path.is_symlink()]
    if target_symlinks:
        print("ERROR: refusing to replace symlinked skill directories:", file=sys.stderr)
        for name in target_symlinks:
            print(f"  {targets[name]}", file=sys.stderr)
        return 2

    if args.check:
        differences = []
        for name in SKILL_NAMES:
            source, target = source_root / name, targets[name]
            if not target.is_dir():
                differences.append(f"missing installed skill: {name}")
            elif tree_digest(source) != tree_digest(target):
                differences.append(f"installed skill differs from package: {name}")
        if differences:
            print("CHECK FAILED:")
            for difference in differences:
                print(f"- {difference}")
            return 1
        print(f"CHECK PASSED: installed skills match package at {target_root}")
        return 0

    if existing and not args.upgrade:
        print("ERROR: refusing to overwrite existing skill directory/directories:", file=sys.stderr)
        for name in existing:
            print(f"  {targets[name]}", file=sys.stderr)
        print("Back up and move/remove the existing directory yourself, or rerun with --upgrade to create a backup first.", file=sys.stderr)
        return 2

    if args.dry_run:
        action = "upgrade" if existing else "install"
        print(f"DRY RUN: would {action} these skills into {target_root}")
        for name in SKILL_NAMES:
            print(f"  - {name}" + (" (existing; would back up and replace)" if name in existing else ""))
        return 0

    # Stage every source tree before touching the existing installation.
    agent_root.mkdir(parents=True, exist_ok=True)
    staging_parent: Path | None = None
    backup_root: Path | None = None
    moved_to_backup: list[tuple[Path, Path]] = []
    installed_targets: list[Path] = []

    try:
        staging_parent = Path(tempfile.mkdtemp(prefix=".hackathon-ai-toolkit-stage-", dir=agent_root))
        staged_root = staging_parent / "skills"
        staged_root.mkdir()
        for name in SKILL_NAMES:
            shutil.copytree(source_root / name, staged_root / name)

        # Validate staged copies too, then compare staged/source content.
        for name in SKILL_NAMES:
            if tree_digest(source_root / name) != tree_digest(staged_root / name):
                raise RuntimeError(f"staging verification failed for {name}")

        if existing:
            stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            backup_parent = agent_root / ".hackathon-ai-toolkit-backups"
            backup_parent.mkdir(parents=True, exist_ok=True)
            backup_run = Path(tempfile.mkdtemp(prefix=f"{stamp}-{os.getpid()}-", dir=backup_parent))
            backup_root = backup_run / "skills"
            backup_root.mkdir()
            for name in existing:
                source, backup = targets[name], backup_root / name
                os.replace(source, backup)
                moved_to_backup.append((source, backup))

        target_root.mkdir(parents=True, exist_ok=True)
        for name in SKILL_NAMES:
            target = targets[name]
            os.replace(staged_root / name, target)
            installed_targets.append(target)

        print(f"Installed {len(SKILL_NAMES)} skills into: {target_root}")
        for name in SKILL_NAMES:
            print(f"  - {name}")
        if backup_root is not None:
            print(f"Backup of replaced skills: {backup_root}")
        print("Next: restart/refresh your CLI if needed, then run install.py --check --project PATH.")
        return 0

    except Exception as exc:
        # Remove only targets created during this invocation, then restore moved originals.
        for target in reversed(installed_targets):
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target, ignore_errors=True)
            else:
                target.unlink(missing_ok=True)
        rollback_errors: list[str] = []
        for original, backup in reversed(moved_to_backup):
            try:
                original.parent.mkdir(parents=True, exist_ok=True)
                if original.exists():
                    if original.is_dir() and not original.is_symlink():
                        shutil.rmtree(original)
                    else:
                        original.unlink()
                os.replace(backup, original)
            except Exception as rollback_exc:
                rollback_errors.append(f"{original}: {rollback_exc}")
        print(f"ERROR: installation failed: {exc}", file=sys.stderr)
        if rollback_errors:
            print("CRITICAL: rollback had failures:", file=sys.stderr)
            for error in rollback_errors:
                print(f"  - {error}", file=sys.stderr)
            print("Recover originals from the backup directory before retrying.", file=sys.stderr)
        else:
            print("Rollback completed; prior installed skills were preserved/restored.", file=sys.stderr)
        return 1
    finally:
        if staging_parent is not None:
            shutil.rmtree(staging_parent, ignore_errors=True)


if __name__ == "__main__":
    raise SystemExit(main())
