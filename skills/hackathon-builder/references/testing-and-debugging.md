# Testing, Debugging, and Verification

## General principle

Verification must produce evidence, not reassuring language. Choose checks proportional to risk and the actual project. Tests supplement code review; neither replaces the other.

## Before changing code

1. Identify expected and actual behavior.
2. Reproduce the failure if possible.
3. inspect logs, stack traces, recent diffs, call paths, and relevant state.
4. Form a root-cause hypothesis and a way to falsify it.
5. Add a regression test or define a minimal diagnostic experiment.

Do not apply speculative fixes in sequence without understanding what changed.

## Feature and bug-fix cycle

Where feasible:
1. Write or update a test for the intended behavior.
2. Run it and confirm it fails for the expected reason, not due to a broken test harness.
3. Implement the smallest correct change.
4. Run the focused test and confirm it passes.
5. Run related regression tests, then appropriate lint/type/build checks.
6. Refactor only while preserving passing behavior; rerun relevant tests.

Do not force strict TDD for every non-behavioral change (for example, some docs or generated assets), but still perform a suitable verification. If the existing project has no test harness, do not silently install one; propose a proportionate approach and obtain authorization if setup has material impact.

## Test design

Prioritize:
- normal successful path;
- boundary values and empty/missing inputs;
- invalid and malicious inputs at trust boundaries;
- permission failures and unauthenticated access;
- external dependency timeout, rejection, and malformed response;
- persistence failure and partial state change;
- duplicate calls, retries, cancellation, races, and idempotency where relevant;
- regression scenario that previously failed;
- user-visible empty/loading/error/success states for UI.

Tests should fail when the behavior is wrong. Avoid tautological assertions, heavy mocking that bypasses the code under test, snapshot-only confidence for logic, and tests coupled to implementation details without reason.

## Run commands safely

Discover commands from package scripts, Makefile, pyproject, tox, Cargo.toml, go.mod, project docs, or existing CI. Prefer targeted checks first. Avoid destructive setup, production endpoints, network-dependent commands, or broad operations without authorization. Record command, exit status, and relevant output. If not run, say “not run” and why.

## Interpreting failures

Classify each failure:
- product defect;
- regression;
- flaky/environment-dependent test;
- test harness/configuration failure;
- unrelated pre-existing failure;
- insufficient evidence.

Do not dismiss a failing test as flaky without evidence. If it appears pre-existing, show the baseline evidence where possible and don't modify unrelated behavior to make it green.

## Browser and visual QA

When a web UI is affected and browser tooling exists, test the actual running app. Inspect console errors, failed network requests, interactive behavior, responsive layout, keyboard navigation/focus, and relevant loading/empty/error/success states. Use screenshots at representative viewports when possible. A build passing does not prove the UI looks or behaves correctly.

## Completion claims

Use exact states:
- **Executed and passed:** the command actually ran with success evidence.
- **Executed and failed:** it ran but did not pass.
- **Not run:** not executed; explain why.
- **Blocked:** could not run due to an identified dependency or environment problem.
- **Not applicable:** explain briefly if the reason is not obvious.

Never infer a successful run from source inspection, and never claim physical hardware behavior without actual hardware or a valid simulator test.
