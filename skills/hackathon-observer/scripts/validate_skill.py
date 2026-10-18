#!/usr/bin/env python3
"""Read-only structural validator for the Hackathon Observer skill bundle."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def main() -> int:
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        error("Missing SKILL.md")
        return finish()
    text = skill_path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        error("SKILL.md must begin with YAML frontmatter")
        return finish()
    end = text.find("\n---\n", 4)
    if end < 0:
        error("YAML frontmatter closing delimiter not found")
        return finish()
    fm = text[4:end]
    name_match = re.search(r"^name:\s*[\"']?([^\"'\n]+)[\"']?\s*$", fm, re.M)
    desc_match = re.search(r"^description:\s*(.+)$", fm, re.M)
    if not name_match:
        error("Frontmatter missing name")
    else:
        name = name_match.group(1).strip()
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            error(f"Invalid skill name format: {name!r}")
        if name != ROOT.name:
            error(f"Skill name {name!r} does not match package directory {ROOT.name!r}")
    if not desc_match:
        error("Frontmatter missing description")
    else:
        desc = desc_match.group(1).strip().strip("\"'")
        if not desc:
            error("Description cannot be empty")
        if len(desc) > 1024:
            error(f"Description exceeds 1024 characters ({len(desc)})")
    if 'version: "1.4.0"' not in fm:
        WARNINGS.append("Version metadata is not explicitly set to quoted string 1.4.0")

    required_files = [
        "README.md",
        "references/discovery-and-feasibility.md",
        "references/solution-design-and-domain-modules.md",
        "references/professional-ui.md",
        "references/execution-and-presentation.md",
        "references/project-state-and-template-routing.md",
        "references/audit-and-blueprint-output.md",
        "references/skill-ecosystem-and-evaluation.md",
        "templates/intake-brief.md",
        "templates/project-blueprint.md",
        "templates/risk-register.csv",
        "templates/plan-audit.md",
        "templates/presenter-brief.md",
        "templates/project-state.md",
        "templates/ui-design-brief.md",
        "templates/skill-audit-report.md",
        "tests/evaluation-cases.md",
        "tests/evaluation-results-template.csv",
        "scripts/validate_skill.py",
    ]
    for rel in required_files:
        if not (ROOT / rel).is_file():
            error(f"Missing required file: {rel}")

    # Check local markdown link destinations and explicit paths in backticks.
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for file in md_files:
        content = file.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            target = target.strip().split("#", 1)[0]
            if not target or re.match(r"^(?:https?://|mailto:|tel:|data:)", target, re.I):
                continue
            dest = (file.parent / target).resolve()
            if not dest.exists():
                error(f"Broken local Markdown link in {file.relative_to(ROOT)}: {target}")
        for target in re.findall(r"`((?:references|templates|tests|scripts)/[^`]+)`", content):
            # Ignore shell globs or placeholder patterns; only validate likely file paths.
            if any(c in target for c in "*{}<>"):
                continue
            if not (ROOT / target).exists():
                error(f"Broken referenced path in {file.relative_to(ROOT)}: {target}")

    cases = ROOT / "tests/evaluation-cases.md"
    if cases.exists():
        case_ids = re.findall(r"^### (E\d{2}) —", cases.read_text(encoding="utf-8"), re.M)
        if len(case_ids) < 20:
            error(f"Expected at least 20 evaluation cases; found {len(case_ids)}")
        if len(case_ids) != len(set(case_ids)):
            error("Duplicate evaluation case IDs found")
        result_csv = ROOT / "tests/evaluation-results-template.csv"
        if result_csv.exists():
            csv_text = result_csv.read_text(encoding="utf-8")
            missing = [case_id for case_id in case_ids if case_id not in csv_text]
            if missing:
                error("Evaluation results template missing cases: " + ", ".join(missing))

    if len(text) > 15000:
        WARNINGS.append(f"SKILL.md is {len(text):,} characters; consider preserving progressive disclosure if it grows")
    print(f"Package: {ROOT}")
    print(f"Core skill: {len(text):,} characters")
    print(f"Markdown files scanned: {len(md_files)}")
    if 'cases' in locals():
        print(f"Evaluation cases: {len(case_ids)}")
    return finish()


def finish() -> int:
    for warning in WARNINGS:
        print(f"WARN: {warning}")
    for item in ERRORS:
        print(f"ERROR: {item}")
    if ERRORS:
        print(f"FAILED: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
        return 1
    print(f"PASS: no structural errors ({len(WARNINGS)} warning(s))")
    return 0

if __name__ == "__main__":
    sys.exit(main())
