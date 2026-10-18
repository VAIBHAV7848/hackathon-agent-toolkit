# Security, Privacy, and Reliability Checks

Use the relevant portions for authentication, roles/permissions, personal or regulated data, uploads, payments, external inputs, network calls, secrets, agent tools, or other sensitive operations. Keep security proportional to the project's context, but never omit obvious high-impact risks.

## Trust boundaries

Map untrusted inputs, privileged actions, sensitive data, external systems, and trust boundaries. Validate inputs on the authoritative server or device boundary—not only in the UI. Use allowlists where possible and encode output for its destination context.

## Authentication and authorization

- Authenticate where needed and authorize each sensitive operation at the resource/action level.
- Never trust user-supplied role IDs, ownership IDs, prices, status, or permission claims.
- Avoid IDOR/BOLA by checking resource ownership and permissions server-side.
- Protect sessions, cookies, CSRF-sensitive flows, redirects, and account recovery according to the framework's documented safe defaults.
- Use least privilege for filesystem, network, agent tools, tokens, cloud accounts, and service credentials.

## Secrets and data

- Never hard-code secrets or print them to logs.
- Keep secrets in authorized environment/configuration mechanisms; provide `.env.example` with placeholders, not real values.
- Minimize collected data; redact sensitive data from logs and errors; define retention/deletion when relevant.
- Do not use production personal data for demonstrations without appropriate permission and controls.
- Protect uploads and downloads with size/type validation, safe names, storage boundaries, and authorization as appropriate.

## External dependencies and APIs

Set sensible timeouts and bounded retries; validate responses; handle errors and rate limits. Avoid logging sensitive request/response bodies. Check package provenance, license, maintenance, compatibility, and transitive risk before additions. Pin or lock dependencies according to project conventions.

## State changes and transactions

Use transactions or compensating actions when partial state would violate invariants. Make retryable operations idempotent where appropriate. Avoid unsafe read-modify-write flows. Validate migrations on a safe environment; never run production migrations or destructive data commands without explicit authorization.

## AI/ML or agent-specific risks

When applicable, guard against prompt injection, untrusted tool output, data leakage, unjustified tool permissions, unsafe generated actions, hallucinated facts, and hidden state. Keep secrets out of model context when possible. Require human approval for high-impact or irreversible actions. Verify outputs with code/tests/independent sources rather than treating model confidence as proof.

## Release blockers

Do not declare the task complete with an unresolved critical issue such as exposed credentials, unauthorized data access, an obvious privilege escalation, unsafe destructive action, or a sensitive endpoint lacking required authorization. Explain the issue and propose a safe fix; do not hide it to achieve a green report.
