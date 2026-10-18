# Hackathon Observer Skill — Universal Edition

A planning-only Agent Skill for hackathons and time-boxed innovation work across software, AI/data, hardware, research, design, business, games, social impact, and hybrid projects. It adapts to the actual event, project modality, deliverables, rules, time budget, and user's execution model. It does not assume SIH or any other specific organizer.

## Default operating model

- The user is the project owner, prompt orchestrator, and primary builder unless they say otherwise.
- Observer researches, evaluates, plans, drafts bounded task prompts, tracks uncertainty, and audits evidence; it does not implement by default.
- Teammates primarily prepare to explain and present the real project unless the user explicitly assigns other responsibilities.

## Version 1.4 design change: evidence-led skill ecosystem integration

- Added a source-backed landscape of high-signal open-source skill, harness, evaluator, security, and UI-design repositories.
- Added a third-party skill supply-chain review protocol and a reusable skill-audit report template.
- Expanded the manual evaluation suite to cover ecosystem research, deprecated sources, unsafe skills, selective installation, evaluation claims, and God Harness maturity.
- Kept external repositories as references rather than vendoring their skill contents; licenses and installation behavior must be checked before reuse.

## Version 1.3 design change: progressive disclosure

`SKILL.md` is intentionally a compact router. It points the agent to conditional references instead of loading every procedure for every request. This reduces irrelevant context and makes modules easier to revise. Do not delete a reference because its content is not used by every project; load it only when needed.

### Reference modules

- `references/discovery-and-feasibility.md` — event classification, source hierarchy, problem discovery, prior art, scope, and experiments.
- `references/solution-design-and-domain-modules.md` — design decisions and conditional AI/data, security, hardware, research, and domain risk checks.
- `references/professional-ui.md` — product-specific UI design and visual QA; only for projects with a real digital interface.
- `references/execution-and-presentation.md` — primary-builder task planning, bounded prompts, validation, demo, delivery, and presenter handoff.
- `references/project-state-and-template-routing.md` — state continuity, template choice, and evidence/decision/risk registers.
- `references/audit-and-blueprint-output.md` — adversarial review, full-blueprint format, and completion criteria.
- `references/skill-ecosystem-and-evaluation.md` — curated open-source skill/harness landscape, selection criteria, evaluation strategy, and supply-chain cautions; read only when auditing or improving skills/harnesses.

## Installation

Copy the complete `hackathon-observer` folder into the project's `.agents/skills/hackathon-observer/` directory. Keep `references/`, `templates/`, `tests/`, and `scripts/` alongside `SKILL.md`; do not install only the main file.

### OpenCode CLI

OpenCode documents `.agents/skills/<name>/SKILL.md` as a compatible project-level location, along with native OpenCode directories. It supports slash invocation when configured/recognized. If discovery differs, check the documentation for your installed version and verify that the skill is not denied by permissions.

### Google Antigravity CLI (`agy`)

Antigravity documents workspace skills under `.agents/skills/<name>/SKILL.md`. Global paths and behavior can vary by surface/version; check the current documentation if using a global installation.

Official documentation:
- https://opencode.ai/docs/skills/
- https://www.antigravity.google/docs/skills?tab=ide

## First use

> Use `hackathon-observer` in Intake/Discovery mode. Classify the event format and project modality from the supplied evidence. Read only the relevant reference modules. Inspect the official challenge materials and available project files, distinguish facts from assumptions, identify the highest-impact unknowns, and produce a discovery report. Do not implement or mutate project files.

After reviewing discovery, use the skill for feasibility, planning, bounded execution prompts, adversarial audit, or presenter preparation. Do not ask for the full blueprint if the current task is narrow.

## Templates

- `templates/intake-brief.md` — new project/event intake.
- `templates/project-blueprint.md` — detailed plan after enough discovery.
- `templates/risk-register.csv` — risks, blockers, mitigations, and fallbacks.
- `templates/plan-audit.md` — adversarial review.
- `templates/presenter-brief.md` — teammate explanation/demo prep.
- `templates/project-state.md` — resumable, evidence-grounded status snapshot.
- `templates/ui-design-brief.md` — professional product-specific design and rendered UI QA, when applicable.

Templates are optional support materials, not mandatory paperwork. Only use those that improve the requested result.

## Structural validation

After extraction, run:

```bash
python3 scripts/validate_skill.py
```

The validator is read-only and dependency-free. It checks required files/frontmatter, the skill name and description, internal module/template paths, and the manual evaluation-case inventory. It does **not** test the LLM's behavior or prove compatibility in a live CLI session.

## Behavioral evaluation and release

Run the scenarios in `tests/evaluation-cases.md` in every target CLI/model combination that matters. Record results in `tests/evaluation-results-template.csv`. Use `Pass`, `Partial`, or `Fail`; capture the exact prompt, CLI/version, model, evidence, and remediation. Re-run failed and regression-prone cases after changing the skill. Do not label the skill behaviorally validated until critical cases are executed.
