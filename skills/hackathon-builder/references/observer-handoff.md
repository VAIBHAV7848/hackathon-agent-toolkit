# Observer-to-Builder Handoff

The Builder can receive an Observer blueprint, implementation task, project-state file, design brief, or audit findings. These are context, not unquestionable truth; reconcile them against the actual repository and user-approved scope.

## Before implementation

Confirm:
- task ID and concise goal;
- approved scope and explicit non-goals;
- affected module/contracts and current repo state;
- acceptance criteria and required evidence;
- dependencies, constraints, and deadline mode;
- relevant risks, decisions, and assumptions;
- whether UI/security/hardware/data-specific references apply.

If key facts in the plan conflict with actual files or commands, stop the affected change and report the discrepancy. Do not silently invent missing APIs, schemas, filenames, credentials, or test results.

## During implementation

Handle one coherent task at a time. Keep a short execution ledger with the current objective, changes, checks run, blockers, and next step. Update the project state only with observed events; never mark work complete because it was planned or because an AI agent said it succeeded without evidence.

## After implementation

Return evidence to Observer or the user:
- changed files and behavior;
- diff/commit reference if available (do not commit unless requested);
- commands and outcomes;
- screenshots/browser findings where available;
- remaining issues and deviations from the plan;
- suggested next task.

Do not continue to a major new task after a critical regression, scope conflict, data/security concern, or unapproved architectural decision. Surface it for human review.
