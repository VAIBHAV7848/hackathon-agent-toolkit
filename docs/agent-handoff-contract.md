# Observer ↔ Builder handoff contract

This contract keeps a single developer workflow evidence-based and traceable.

## Observer task packet

Every non-trivial implementation prompt should specify:

1. Task ID and objective.
2. Why the task matters to the approved requirements or judging/demo objective.
3. Repository facts and files that were actually inspected (or explicitly marked unknown).
4. Approved scope and non-goals.
5. Acceptance criteria that can be observed or tested.
6. Relevant architecture/design decisions, assumptions, and dependencies.
7. Required checks and expected evidence.
8. Risks, compatibility constraints, and any needed user approval.
9. Time mode (rapid, standard, or deep) when useful.

Observer creates prompts and plans; it does not claim that implementation occurred.

## Builder completion packet

For each task, Builder reports:

1. Status: complete, partial, blocked, or not started.
2. Actual behavior changed and a file-by-file summary.
3. Commands run, exit outcomes, and test/build/lint results.
4. UI evidence and states/viewports inspected, or a clear statement that visual QA was not possible.
5. Deviations from the approved scope and why they occurred.
6. Remaining risks, untested paths, assumptions, and blockers.
7. Suggested next step, without automatically starting unrelated tasks.

Builder must not mark a task verified based only on generated code or an uncorroborated claim from another agent. It should cite observable command output, diff context, screenshots, or other available evidence.

## Reconciliation rules

- Actual repository state outranks stale plan assumptions.
- Official competition requirements outrank guesses or promotional summaries.
- User approval controls scope and consequential trade-offs.
- Tests that were not run remain unverified; failures are not silently omitted.
- If new evidence invalidates the plan, Builder reports the discrepancy and pauses the affected work rather than expanding scope on its own.
- Observer updates project state after receiving evidence, distinguishing confirmed results from claims awaiting independent verification.
