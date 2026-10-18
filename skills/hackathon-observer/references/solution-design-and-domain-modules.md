# Solution Design and Conditional Domain Modules

## Phase 6 — Solution design and technical decisions

Compare plausible solution approaches before recommending one. Evaluate fit to requirements, existing skills, time, materials/equipment, compatibility, resource use, reliability, safety, security, licensing, cost, documentation, reproducibility, debugging/repair burden, and delivery constraints.

Choose artifacts according to modality. The plan may include, as appropriate:

- software/system context and component diagrams;
- hardware block diagrams, interfaces, power, physical constraints, and safety considerations;
- data-flow and trust-boundary diagrams;
- database entities/relationships and integrity constraints, when a database is needed;
- API/interface contracts, input/output/error behavior, and authentication, when interfaces exist;
- research design, variables, controls, baseline, and reproducibility protocol;
- user journey, service blueprint, wireframes, accessibility checks, or prototype flow;
- a professional UI design brief and visual QA plan for digital interfaces, when applicable;
- business model, stakeholder/customer validation, impact model, or go-to-market assumptions where the event requires them;
- model/service integration, asynchronous work, and failure handling where applicable;
- deployment/runtime architecture and configuration requirements where applicable;
- decision records with alternatives, rationale, trade-offs, and assumptions.

Do not force unnecessary diagrams, microservices, agents, models, databases, or infrastructure into a small project. Identify single points of failure and the simplest acceptable design. Treat architecture as provisional until critical feasibility tests have passed.

## Phase 7 — Data, AI, security, and domain risks

### If data or AI/ML is involved

Investigate provenance, permission, licensing, quality, coverage, labels, privacy, data leakage, representative evaluation, baselines, metric choice, compute, latency, cost, reproducibility, and failure handling. Compare AI with a simpler non-AI approach where useful. Define what happens when confidence is low or output is unreliable. Do not assert model accuracy without a defined evaluation set, metric, and measured results.

### Security and privacy

Consider only threats relevant to the actual system, including authentication/authorization, secrets, input validation, sensitive logs, dependency risk, access boundaries, data retention, malicious input, and abuse cases. Recommend authorized tests and do not propose testing systems outside the user's permission.

### Sensitive or regulated domains

For healthcare, finance, legal, public services, biometrics, or other sensitive contexts, identify relevant official sources and domain-expert validation needs. Do not invent clinical, legal, or regulatory rules. Minimize sensitive data and distinguish administrative assistance from consequential decision support.
