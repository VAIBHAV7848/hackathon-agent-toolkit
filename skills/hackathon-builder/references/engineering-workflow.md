# Engineering Workflow and Code Quality

Read this reference for implementation tasks, non-trivial refactors, and repository-level decisions.

## Repository reconnaissance

Inspect only enough of the codebase to understand the affected path, its callers, data contracts, tests, and conventions. Use project-provided guidance and manifests as primary context. Avoid dumping the entire repository into context.

Record the relevant starting state:
- branch/working tree status when Git is available;
- affected modules and their callers;
- existing conventions and adjacent implementations;
- available test, lint, type-check, build, and formatting commands;
- unknowns that could change the implementation.

## Design rules

- Optimize for understandable, correct, maintainable behavior—not maximum abstraction or minimum line count.
- Prefer simple designs with clear ownership, cohesive modules, explicit contracts, and low coupling.
- Preserve public APIs and existing data formats unless a change is authorized.
- Avoid speculative generalization, premature microservices, unnecessary state-management frameworks, custom utility frameworks, and dependencies for trivial functionality.
- Add an abstraction when it meaningfully reduces duplication or isolates a real volatile/complex concern, not simply because an AI can generate one.
- Keep side effects near boundaries. Isolate I/O, clock/randomness, external services, and persistence where doing so improves testing and reasoning.
- Validate untrusted inputs at boundaries. Do not rely only on client-side validation for server-enforced rules.
- Use errors that preserve useful context without leaking secrets or sensitive data.
- Respect project-specific accessibility, localization, performance, and compatibility requirements.
- Consider data migrations, backwards compatibility, cancellation/timeouts, idempotency, and retry safety when the code path requires them.

## Anti-patterns to reject

- Rewriting a working codebase to match a preferred stack without justification.
- Huge components/modules that combine unrelated concerns.
- Over-engineered factories/providers/registries for one simple use case.
- Duplicated validation logic or multiple competing sources of truth.
- Broad `catch` blocks that hide errors or return fabricated success.
- Empty `try/catch`, swallowed promise rejections, console-debug residue, TODO-only implementations, and dead controls.
- Hard-coded credentials, environment values, fake API success, mock data shown as real data, or tests that only assert that a value exists.
- Suppressing compiler/linter warnings instead of understanding them.
- Adding a dependency without assessing whether it is maintained, compatible, licensed, and necessary.
- Formatting or editing unrelated files to make a diff look uniform.

## Dependency protocol

Before adding a dependency, establish that the project does not already provide the capability. Check compatibility with the runtime/framework/package manager, maintenance/activity signals, license, security posture, size/performance implications, transitive dependencies, and offline/demo constraints. Do not perform package installation if the environment or user has not authorized it; propose the command and rationale where required.

## Interfaces and contracts

For a public function, API, event, component, or shared schema, define inputs, outputs, invariants, error semantics, and compatibility expectations. Validate at trust boundaries. Avoid changing a shared contract without updating its consumers and tests.

## Readability and ownership

Use names that explain the domain. Keep functions and modules focused. Comments should capture why a non-obvious choice exists, not restate what the code does. Organize files according to the existing project's conventions rather than inventing new structure unnecessarily.

## Diff discipline

After changes, inspect the diff and check:
- only intended files changed;
- no unrelated formatting churn;
- no secrets, tokens, local database dumps, logs, build artifacts, or user data entered version control;
- no package/lockfile drift;
- no accidental removal of TODOs or existing work unrelated to task;
- behavior changes are covered with tests or explained limitations.
