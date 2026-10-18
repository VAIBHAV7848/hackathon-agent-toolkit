# Adversarial Audit, Blueprint Output, and Completion Criteria

## Phase 12 — Adversarial plan audit

Audit the draft as a skeptical reviewer. Look for:

- unmet official requirements or missing deliverables;
- unsupported problem/novelty/impact claims;
- weak or stale sources and conflicting evidence;
- feature bloat and an MVP that is too large;
- infeasible estimates for one primary builder;
- hidden prerequisites, integration bottlenecks, or unavailable services/data;
- unclear requirements, interfaces (where relevant), or acceptance criteria;
- for digital interfaces: generic AI-template aesthetics, unmotivated dark/purple/gradient/glow styling, excessive repetitive cards, fake metrics/testimonials, inconsistent design tokens, missing empty/error/loading states, weak responsiveness/accessibility, or claims of visual polish without rendered evidence;
- missing relevant edge cases, safety/security/privacy issues, or appropriate evaluation methods;
- brittle demonstrations or deliverables, untested dependencies where applicable, and missing fallbacks;
- discrepancies between planned, implemented, tested, and demonstrated features;
- legal/license/access constraints;
- presentation claims that go beyond evidence.

For each finding, state severity, evidence/affected section, consequence, and recommended resolution. Separate blockers from high-value improvements and subjective preferences. Then reconcile valid findings; list unresolved disagreements for the human developer.

## Required output for a full project blueprint (adapt to the event and modality)

Tailor depth to event format, deliverables, project modality, risk, and remaining time. Cover relevant headings; omit inapplicable sections or mark them `N/A` with a reason. Do not assume every project has software, AI, a database, an API, hosting, a repository, or a live demo:

1. Executive summary and current status.
2. Official challenge requirements and traceability matrix.
3. Problem definition, users, workflow, and evidence.
4. Prior art and defensible differentiation hypothesis.
5. Assumptions, unresolved questions, and decision requests.
6. Minimum credible outcome/prototype (MVP where appropriate), priorities, non-goals, and acceptance criteria.
7. Feasibility experiments/validations and results/status.
8. Solution/design options and recommended approach with trade-offs (software/system architecture where relevant).
9. Professional UI design brief and visual QA plan when a digital interface is in scope; omit when no interface is required.
10. Data/AI plan, evaluation metrics, and limitations, if applicable.
11. Security, privacy, safety, and domain-specific risks.
12. Primary-builder task plan, dependencies, estimates, and cut line.
13. Validation plan and definition of done.
14. Delivery, operations/deployment where applicable, documentation, and submission checklist.
15. Demonstration/pitch storyline, fallback plan, and teammate presentation packet.
16. Risk register, contingency decisions, and open blockers.
17. Next 3–5 actions, ordered by importance and dependency.

Every material claim must be traceable to evidence or labeled as an assumption. Do not fill sections with generic boilerplate simply to make the report longer.

## Completion criteria

A plan is ready for human approval when:

- official requirements and deliverables are understood or explicitly flagged;
- the problem and differentiator are supported by evidence or labeled hypotheses;
- the minimum credible outcome is feasible for one primary builder and the available time;
- critical technical, domain, or delivery risks have validation plans or evidence;
- relevant solution/design decisions and unresolved trade-offs are visible;
- essential requirements map to tasks and acceptance checks;
- appropriate validation, safety/security/privacy considerations, demonstration, delivery, and fallbacks are covered;
- if a digital UI is in scope, its visual direction is product-specific, the generic AI-aesthetic anti-patterns are explicitly checked, and rendered visual QA is evidenced or clearly marked unverified;
- estimates state their assumptions;
- the presentation plan matches real capability;
- the adversarial audit has been addressed or its remaining blockers disclosed.

For full planning/audit responses, end with **Recommended next action**, **Why now**, and **Evidence or decision needed**. Keep narrow task responses proportionate; do not produce the full blueprint when the user only asks a focused question.
