#!/usr/bin/env python3
"""Dependency-free structural validator for Hackathon Builder skill package."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors: list[str] = []
warnings: list[str] = []

required = [
    "SKILL.md", "README.md", "CHANGELOG.md", "LICENSE",
    "references/engineering-workflow.md",
    "references/testing-and-debugging.md",
    "references/ui-quality.md",
    "references/security-reliability.md",
    "references/observer-handoff.md",
    "references/open-source-practices.md",
    "templates/implementation-task.md",
    "templates/completion-report.md",
    "templates/code-review-checklist.md",
    "tests/evaluation-cases.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        errors.append(f"Missing required file: {rel}")

skill_path = ROOT / "SKILL.md"
if skill_path.is_file():
    content = skill_path.read_text(encoding="utf-8")
    if not content.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        end = content.find("\n---\n", 4)
        if end < 0:
            errors.append("Could not find closing YAML frontmatter delimiter")
        else:
            frontmatter = content[4:end]
            for key in ("name:", "description:"):
                if not re.search(rf"(?m)^{re.escape(key)}\s*\S", frontmatter):
                    errors.append(f"Missing or empty required frontmatter field: {key[:-1]}")
            name_match = re.search(r"(?m)^name:\s*([a-z0-9-]+)\s*$", frontmatter)
            if not name_match:
                errors.append("Skill name must be lowercase kebab-case")
            elif name_match.group(1) != ROOT.name:
                errors.append(f"Skill name '{name_match.group(1)}' does not match directory '{ROOT.name}'")
            desc_match = re.search(r"(?m)^description:\s*(.+)$", frontmatter)
            if desc_match and len(desc_match.group(1).strip().strip('"\'')) > 1024:
                errors.append("Skill description exceeds 1024 characters")

    # Verify local markdown links and inline references to expected file paths.
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target_path = (ROOT / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            warnings.append(f"Markdown link target not found: {target}")
    for target in re.findall(r"`((?:references|templates|tests|scripts)/[^`]+)`", content):
        if not (ROOT / target).exists():
            warnings.append(f"Referenced path not found: {target}")

cases = ROOT / "tests/evaluation-cases.md"
case_count = 0
if cases.is_file():
    case_text = cases.read_text(encoding="utf-8")
    case_count = len(re.findall(r"(?m)^\d+\. \*\*", case_text))
    if case_count < 20:
        errors.append(f"Expected at least 20 numbered evaluation cases; found {case_count}")

print(f"Skill: {ROOT.name}")
print(f"Required files checked: {len(required)}")
print(f"Behavioral evaluation cases: {case_count}")
print(f"Errors: {len(errors)}")
for item in errors:
    print(f"ERROR: {item}")
print(f"Warnings: {len(warnings)}")
for item in warnings:
    print(f"WARNING: {item}")
print("NOTE: structural validation does not prove that an LLM follows the skill or that a target CLI discovers it.")
sys.exit(1 if errors else 0)
