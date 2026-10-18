# Code Review Checklist

Review the actual diff and relevant callers/tests. Do not approve based on the author's summary alone.

## Correctness
- [ ] Acceptance criteria and edge cases are met.
- [ ] Existing behavior and public contracts remain compatible or changes are deliberate.
- [ ] Invalid input, errors, and asynchronous paths are handled.
- [ ] No race, ordering, idempotency, or partial-state issue is apparent where relevant.

## Design and maintainability
- [ ] Changes are narrowly scoped and fit repository conventions.
- [ ] Functions/modules have clear responsibilities and useful names.
- [ ] No speculative abstraction, duplicated source of truth, or avoidable dependency.
- [ ] Comments explain non-obvious rationale rather than narrating code.

## Security and privacy
- [ ] Trust boundaries and permissions are handled appropriately.
- [ ] No secrets, unsafe logs, injection surfaces, or sensitive data leaks were introduced.
- [ ] Dependencies, file operations, external requests, and state changes are safe for the scope.

## Tests and delivery
- [ ] Tests meaningfully exercise behavior and regression risks.
- [ ] Required test/lint/type/build checks were actually run or limitations disclosed.
- [ ] No dead controls, fake success, placeholder business logic, or debug residue.
- [ ] User changes and unrelated files remain untouched.
- [ ] Documentation/configuration updated when behavior or setup changed.

## UI, if relevant
- [ ] Design fits the actual product and does not default to generic AI aesthetics.
- [ ] Primary flows and loading/empty/error/success states work.
- [ ] Responsive layouts, keyboard focus, labels, contrast, and reduced motion are considered.
- [ ] Rendered UI was inspected, or visual QA is explicitly marked unverified.
