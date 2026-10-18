# Hackathon Builder Skill

Version 0.1.0 — a universal, implementation-capable companion to `hackathon-observer`.

## Purpose

Observer researches, plans, and audits. Builder executes user-approved implementation tasks, runs available checks, and reports evidence. The user remains the project owner and final decision-maker. The skill is designed for one primary developer and must not assume teammates will implement code.

It supports diverse software and digital components within hackathon projects. For tasks requiring physical fabrication or hardware access, it can edit firmware/design files and plan checks only to the extent the installed environment allows; it cannot claim physical validation without actual evidence.

## What “professional code” means here

No skill can guarantee that code is bug-free or make code not AI-generated in origin. This skill targets professional engineering outcomes: repository fit, clear contracts, narrow changes, maintainability, tests, security checks, accessible/product-specific UI, reviewed diffs, and truthful reports. Quality must be demonstrated by evidence, not claimed by prompt.

## Install

Extract the ZIP, then copy the whole `hackathon-builder` folder (not just `SKILL.md`) into your project:

```text
.agents/skills/hackathon-builder/
  SKILL.md
  README.md
  references/
  templates/
  tests/
  scripts/
```

This Agent Skills-style path is documented by OpenCode and Antigravity. Confirm discovery for your installed CLI/version; a correctly structured file is not proof of live discovery.

## Use with Observer

1. Ask Observer to produce/approve a specific implementation task and acceptance criteria.
2. Invoke Builder with that task and relevant project-state/design brief.
3. Builder inspects repository and user changes, implements one coherent scope, runs suitable checks, and reports results.
4. Return Builder's actual diff/test evidence to Observer for review and the next task.
5. Do not declare success where a required test, browser check, or physical/hardware verification remains unperformed.

Example:

> Use `hackathon-builder` in BUILD mode for task HACK-012 from the approved Observer blueprint. Inspect the actual repository and its current working-tree changes first. Implement only that task, add/update meaningful tests, run the relevant checks available in this environment, inspect the final diff, and report exact commands and outcomes. Do not broaden scope or claim unrun checks passed.

For professional UI:

> Use Builder in UI mode. Read `references/ui-quality.md` before editing. Follow the approved UI design brief, the existing app architecture, and the light-first/product-specific direction specified there. Avoid generic AI SaaS aesthetics. Run the app and inspect screenshots and interactions if supported; otherwise clearly state that visual QA is unverified.

## Target CLI paths

- OpenCode: `.agents/skills/hackathon-builder/SKILL.md` is a supported compatibility location in the documented Agent Skills search paths. Also see https://opencode.ai/docs/skills/.
- Antigravity CLI: use `.agents/skills/hackathon-builder/SKILL.md` in the project skill directory according to the currently documented skill convention. See https://www.antigravity.google/docs/skills?tab=ide.

Check current CLI docs if discovery behavior or invocation differs.

## Validation

Run the dependency-free structural validator:

```bash
python3 scripts/validate_skill.py
```

The validator checks frontmatter, required references/templates, and test case inventory. It does not execute the behavioral evaluation cases, code the product, or prove CLI compatibility.

Run the cases in `tests/evaluation-cases.md` in the actual CLI/model environment. Record the prompt, model/version, commands/evidence, status, and remediation. Don't describe it as behaviorally validated until those cases are executed.

## Scope boundary

Builder is implementation-capable when invoked in a coding agent with repository/terminal tools and allowed permissions. The skill itself does not grant filesystem access, shell access, browser automation, deployment permission, API credentials, or any other capability. It does not auto-install packages or deploy/publish without explicit authorization.
