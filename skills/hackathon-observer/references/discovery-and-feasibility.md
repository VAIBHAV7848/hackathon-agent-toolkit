# Discovery, Evidence, and Feasibility Reference

## Universal adaptation protocol — mandatory before planning

This skill is universal because its **decision process adapts**, not because every project receives the same checklist. At intake, classify the event and project using available evidence. If a classification is uncertain, label it provisional instead of guessing.

### A. Identify the event format

Record the event's actual format and constraints where relevant: build hackathon, ideathon, datathon, game jam, research/science challenge, design sprint, startup/business challenge, hardware/robotics event, cybersecurity competition, civic/social-impact challenge, sponsor challenge, open-theme event, or a hybrid. These are examples, not a closed list.

Determine the required submission: functioning product, prototype, proof of concept, dataset/model, experiment, research artifact, design, business case, pitch, report, physical demonstration, or another event-defined deliverable. Never assume that a live software demo, source-code repository, public deployment, AI model, or published scoring rubric is mandatory.

### B. Identify project modality

Choose all that apply; hybrid projects can combine multiple modalities:

- software / web / mobile / developer tools;
- AI / ML / data science / analytics;
- cybersecurity / privacy;
- hardware / embedded / IoT / robotics;
- research / science / experiment;
- product / UX / service design / accessibility;
- business / startup / market validation;
- education / healthcare / finance / climate / agriculture / civic technology / social impact;
- media / games / creative technology;
- another or hybrid modality.

Select only the relevant specialist checks. For example, apply model-evaluation requirements to AI systems, physical safety and hardware validation to hardware projects, usability testing to design projects, reproducibility to research, and customer or stakeholder validation to business/service concepts. For any project that includes a user-facing digital interface (web, mobile, desktop, game UI, dashboard, control panel, or prototype), also activate the Professional UI Quality module below. Do not force a digital-UI module onto projects with no such interface. These checks supplement—not replace—the event's official requirements.

### C. Apply the context profile

Capture the actual:

- event rules, deadline and timezone, judging criteria, submission and IP/licensing rules;
- time remaining, working environment, and resource constraints;
- primary builder's skills and available hours;
- available equipment, data, tools, collaborators, APIs, internet, budget, and permissions;
- state of the project: idea only, research underway, prototype exists, or implementation in progress;
- agent capabilities and whether it has read-only access, browser/search access, or repository access.

Do not infer geography-specific rules, organizer preferences, technology requirements, judging weights, or legal obligations without supporting evidence.

### D. Use the universal core and conditional modules

The universal core is: **rules → problem/opportunity → evidence and prior art → proposed outcome → feasibility → scoped plan → verification → presentation/submission → independent audit**.

Use conditional modules only when applicable: software architecture; hardware/system design; data and AI evaluation; research methodology; business/customer validation; product/UX/accessibility; security/privacy; safety/regulatory context; deployment/operations; pitch/presentation. If a section does not apply, omit it or mark it `N/A` with a brief reason. Never fill a report with boilerplate merely to satisfy a template.

Translate “acceptance criteria” into observable evidence suitable to the project: tests passing, a physical device behaving as specified, a repeatable experiment, a usability task, a dataset/model evaluation, a validated workflow, a design critique, stakeholder evidence, or another relevant proof. Do not pretend that every type of proof is interchangeable.

### E. Choose planning depth based on time and risk

- **Rapid mode:** when time is severely constrained, focus on disqualifying rules, critical unknowns, the smallest credible demonstrable outcome, one or two high-risk validations, test/demo readiness, and submission compliance.
- **Standard mode:** use the full relevant workflow with evidence, feasibility, scoped execution plan, validation, risk controls, and presentation preparation.
- **Deep mode:** when the schedule permits or stakes/complexity are high, broaden prior-art research, alternatives analysis, experiments, security/safety review, documentation, and adversarial evaluation.

Choose based on the actual remaining time and risk; do not use a fixed mode just because a competition has a familiar name. Even in Rapid mode, do not skip eligibility/disqualification checks, critical safety concerns, truthfulness, or the final submission requirements.

### F. Preserve the user's execution model

By default, assume one primary builder/implementer (the user) and teammates primarily responsible for presentation/explanation, because that is the user's stated workflow. Estimate effort for the actual work modality, including learning, research, prototyping, fabrication, integration, tests, rehearsal, and submission—not only coding time. Do not create parallel developer workstreams unless the user updates the model.

## Operating modes

Infer the current mode from the request and context. State the selected mode briefly when useful.

1. **Intake:** collect and normalize available project materials, constraints, deadlines, and tool capabilities.
2. **Discovery:** research the challenge, problem, users, prior art, and unresolved questions. Do not lock architecture prematurely.
3. **Feasibility:** identify critical assumptions and specify experiments that could verify them. Record results only after the developer supplies actual evidence or tools return verified results.
4. **Solution planning:** define the minimum credible outcome, relevant requirements, design options, project-specific execution plan, validation, risks, milestones, and required demonstration/submission. Use technical architecture and software tests only when appropriate.
5. **Task-prompt drafting:** turn an approved plan into a narrowly scoped prompt for one execution task—implementation, research, design, experiment, fabrication, analysis, or another relevant activity—with context, constraints, acceptance criteria, validation steps, and stop conditions.
6. **Plan audit:** independently search for omissions, unsupported claims, dependencies, unrealistic estimates, security issues, overengineering, and failure modes.
7. **Reconciliation:** address valid audit findings, record disagreements, and provide a corrected plan with remaining blockers.

Do not silently jump from Intake or Discovery to a final architecture. Use approval gates when decisions are consequential. In a very short event, compress the process rather than omitting critical checks.

## Phase 1 — Intake and source-of-truth setup

Inspect what is actually available before asking the user for material they have already supplied. Relevant inputs include:

- exact challenge statement, challenge ID, official problem PDF/website, FAQs, addenda, judging rubric, submission requirements, event schedule, and deadline/timezone;
- current project idea, existing prototype/repository/docs, constraints, and previous decisions;
- developer skills and available hours, hardware, OS, internet, budget, APIs, accounts, datasets, and deployment options;
- authorized tools available to this agent (browser/search, file reading, repository access). Do not assume a tool exists because another agent or environment has it.

Create an intake summary with:

- **Verified facts** — backed by an accessible source or supplied official material;
- **Assumptions** — provisional choices being made for progress;
- **Unknowns/blockers** — information that could materially change the plan;
- **User decisions required** — choices that must remain with the developer.

Prefer original, current, authoritative competition sources. Record source title, URL, publisher/owner, date when available, accessed date when relevant, and the claim it supports. Distinguish official requirements from promotional statements, old editions, third-party advice, and agent inference. If browsing is unavailable, disclose the limitation and provide a research checklist rather than pretending to have searched.

## Phase 2 — Challenge and problem intelligence

Analyze:

1. What outcome the challenge explicitly asks for.
2. Mandatory rules, constraints, eligibility, deliverables, scoring criteria, and deadlines.
3. The target user/stakeholder and their current workflow.
4. The root problem, consequences, existing workaround, and evidence that the problem exists.
5. Domain-specific conditions (for example, connectivity, language, accessibility, hardware, privacy, or regulated workflows).
6. What is verified, inferred, hypothesized, or still unknown.

Map every official requirement to a proposed response and evidence of compliance. Never infer judging weights that are not published. If a rubric is missing, say so and use a clearly labeled provisional evaluation framework instead of claiming to predict judges.

## Phase 3 — Prior art and differentiation

Research relevant products, repositories, papers, standards, datasets, APIs, and non-AI alternatives. Prefer primary sources, maintained repositories, official docs, and original research over SEO summaries. Verify recency where it can affect the conclusion.

For each meaningful alternative, assess:

- capability and intended users;
- workflow and technical approach;
- documented limitations (do not invent shortcomings);
- license and reuse restrictions, if reuse is proposed;
- potential to reuse rather than rebuild;
- the measurable gap the proposed project might address.

State differentiation as a **testable hypothesis**, such as a specific workflow improvement, supported offline use, lower cost in a defined setup, better performance on a stated task, accessibility, or a useful integration. “Uses AI,” “has a dashboard,” or “all-in-one” alone is not meaningful differentiation. Do not claim uniqueness without sufficiently broad research; explain the limits of the search.

## Phase 4 — Solution, outcome, and scope definition

Define the intended solution or project outcome before detailed design. Select only the artifacts that fit the event and modality:

- concise problem/opportunity statement and intended value;
- target users/stakeholders/audience and current workflow, where relevant;
- requirements or evaluation criteria appropriate to the deliverable;
- the smallest credible demonstrable outcome (MVP where appropriate) and explicit non-goals;
- priorities (for example, essential / important / optional / out of scope);
- acceptance criteria or observable proof for essential requirements;
- representative test, experiment, review, or validation scenarios;
- demonstration/submission scope, known limitations, and claims that must not be made.

For software, this may become a vertical slice. For research, it may be a reproducible experiment; for hardware, a safe working proof of concept; for design, a testable prototype; for a business or social-impact concept, a validated workflow or stakeholder hypothesis. State what can be demonstrated with available resources and what remains a stretch goal.

## Phase 5 — Feasibility and critical experiments

Assume there is **one primary builder/implementer** unless the user explicitly states otherwise. In the default workflow, teammates are presentation/explanation support, not parallel engineering capacity. Estimate the work for the project's actual modality—software, research, design, data analysis, hardware, experimentation, or a combination—based on demonstrated skills and explicit uncertainty. Include setup, learning, sourcing, fabrication, integration, validation, testing, rehearsal, and submission time as applicable.

Identify high-impact unknowns across technical feasibility and the actual project domain. Examples include data/API/hardware access, model performance, deployment, device limits, materials lead time, experimental reproducibility, user/stakeholder acceptance, research validity, license/IP permissions, costs, venue/network dependence, integration burden, and learning curve.

For each high-impact unknown, define:

- hypothesis to test;
- smallest practical experiment or prototype;
- inputs, tools, access, and estimated effort required;
- observable success/failure threshold and its rationale;
- owner (normally the developer);
- fallback or scope change if it fails.

Mark an experiment as **proposed**, **in progress**, **passed**, or **failed** only when supported by evidence. Never treat a suggested experiment as completed. Do not delay useful planning because non-blocking details are missing; use labeled provisional assumptions.
