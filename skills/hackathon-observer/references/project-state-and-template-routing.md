# Project Continuity, Template Routing, and Registers

## Project continuity and state protocol

For work spanning multiple sessions, use `templates/project-state.md` as the compact source-of-truth snapshot. At the beginning of a resumed session, inspect the latest available state file and project evidence before asking the user to repeat information. If no state file exists, propose an initial snapshot instead of pretending one exists.

Track at least: event/project profile; current phase; approved scope; decisions and rationale; tasks marked planned/in progress/verified/blocked; evidence links; completed validation and actual results; unresolved assumptions; active risks; next action; and last-updated date. Distinguish planned from completed work. Update a proposed snapshot in the response after a meaningful milestone; do not write or mutate files unless the user explicitly authorizes that action, because this skill is planning-only by default. If new evidence conflicts with the state snapshot, flag the conflict and reconcile it rather than silently preserving stale assumptions.

## Template routing protocol

Use supporting templates as tools, not mandatory paperwork. Read and populate the template most relevant to the current task:

- `templates/intake-brief.md` — new event/project or missing intake context;
- `templates/project-blueprint.md` — comprehensive plan after enough discovery;
- `templates/risk-register.csv` — ongoing risks, blockers, mitigations, and fallbacks;
- `templates/plan-audit.md` — skeptical review before approval;
- `templates/presenter-brief.md` — preparation for teammates who explain or demo the real project;
- `templates/project-state.md` — resumable project state across sessions;
- `templates/ui-design-brief.md` — product-specific visual direction, design tokens, interface states, accessibility, and rendered visual QA, only when a digital UI is in scope;
- `tests/evaluation-cases.md` — evaluate the skill's behavior, not a project deliverable.

Do not fill all templates for a narrow question. Only use files that improve the current outcome and are accessible.

## Phase 11 — Evidence, assumption, decision, and risk registers

Maintain these lightweight registers in the response or proposed project documents:

- **Evidence ledger:** claim, source, date, what the source supports, confidence, limitation.
- **Assumptions/questions:** assumption or unknown, impact if wrong, verification method, decision deadline.
- **Decision log:** decision, alternatives, rationale, evidence, trade-offs, owner, revisit condition.
- **Risk/blocker register:** probability, impact, trigger, mitigation, fallback, owner, decision deadline.

Keep status labels consistent: `verified`, `inferred`, `assumed`, `unresolved`, `proposed`, `tested`, `passed`, `failed`. Do not use `passed` without results.
