#!/usr/bin/env python3
"""Run bundled skill validators and toolkit-level integrity checks."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ("hackathon-observer", "hackathon-builder")
REQUIRED_ROOT_FILES = (
    "README.md", "LICENSE", "LICENSES.md", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "SUPPORT.md", "CHANGELOG.md", "CITATION.cff", "VERSION", "install.py",
    "tests/test_toolkit.py", "docs/agent-handoff-contract.md", "docs/benchmarking.md",
    ".github/workflows/ci.yml", ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml", ".github/PULL_REQUEST_TEMPLATE.md",
)
ERRORS: list[str] = []


def check_local_links() -> None:
    for file in ROOT.rglob("*.md"):
        if any(part in {".git", "__pycache__", "dist"} for part in file.parts):
            continue
        try:
            content = file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            ERRORS.append(f"Unreadable UTF-8 Markdown file: {file.relative_to(ROOT)}")
            continue
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = target.strip()
            if not target or re.match(r"^(?:https?://|mailto:|tel:|data:|#)", target, re.I):
                continue
            target_path = target.split("#", 1)[0].split("?", 1)[0]
            if not target_path:
                continue
            if not (file.parent / target_path).resolve().exists():
                ERRORS.append(f"Broken local Markdown link: {file.relative_to(ROOT)} -> {target}")


def main() -> int:
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip() if (ROOT / "VERSION").is_file() else "MISSING"
    for rel in REQUIRED_ROOT_FILES:
        if not (ROOT / rel).is_file():
            ERRORS.append(f"Missing toolkit file: {rel}")
    for name in SKILLS:
        root = ROOT / "skills" / name
        validator = root / "scripts" / "validate_skill.py"
        if not (root / "SKILL.md").is_file():
            ERRORS.append(f"Missing skills/{name}/SKILL.md")
            continue
        if not validator.is_file():
            ERRORS.append(f"Missing skills/{name}/scripts/validate_skill.py")
            continue
        print(f"\n=== {name} ===")
        result = subprocess.run([sys.executable, str(validator)], cwd=root, check=False)
        if result.returncode:
            ERRORS.append(f"Validator failed for {name} (exit {result.returncode})")
    check_local_links()
    print(f"\nToolkit version: {version}")
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} error(s)")
        for item in ERRORS:
            print(f"- {item}")
        return 1
    print("PASS: required files, local Markdown links, and both skill validators passed.")
    print("NOTE: structural checks do not prove live CLI discovery or behavioral improvement.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
