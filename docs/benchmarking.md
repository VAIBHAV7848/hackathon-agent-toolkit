# Behavioral evaluation protocol

This toolkit should earn trust through observable outcomes, not by the number of instructions or the length of its README. This protocol adapts ideas used by public agent-skill evaluation projects, including NVIDIA SkillEvaluator and SkillsBench; it does not claim affiliation with those projects.

## Questions to answer

1. Does Observer improve challenge interpretation, evidence quality, risk discovery, feasibility, and task-plan completeness?
2. Does Builder improve correct implementation, test coverage, security, maintainability, and task completion without unnecessary code?
3. Does the combined workflow improve end-to-end task success without excessive latency or token/cost overhead?
4. Do results transfer across more than one model and CLI?
5. Does visual quality improve when UI tasks have explicit design briefs and screenshot-based review?

## Minimum fair comparison

- **Arms:** same agent/model/tool permissions with no toolkit; Observer only; Builder only; both skills. Add Ponytail as a fifth arm only when testing its interaction is the question.
- **Isolation:** fresh worktree or temporary repository for every run; no global rules or hidden project memory unless those are intentionally held constant across all arms.
- **Randomization:** alternate or randomize arm order to reduce time-of-day and service-drift bias.
- **Repeated runs:** start with at least 5 runs per task/arm for exploratory comparisons; use more runs when variance is high or the claim is consequential.
- **Task set:** include realistic tasks from multiple project modalities and varying difficulty. Do not tune only to the cases used in the skill file.
- **Pre-register:** write task definitions, expected outcomes, scoring rubric, exclusions, and primary metrics before reviewing the results.
- **Blinding:** where practical, have a reviewer score anonymized results without knowing which arm produced them.
- **Report all outcomes:** include incomplete runs, failures, timeouts, costs, variance, environment, and changes to the benchmark. Never cherry-pick a favorable subset.

## Example task matrix

Include, at minimum, one task from each relevant category. Not every project modality applies to every release; mark non-applicable tasks explicitly rather than inventing results.

| Category | Example task | Key evidence |
|---|---|---|
| Challenge analysis | Extract requirements from an official brief with a conflicting unofficial summary | Correct precedence, traceable citations, unresolved conflict identified |
| Discovery | Compare 3 existing approaches for a given problem | Accurate sources, limitations, differentiation, no invented claims |
| Planning | Plan a constrained MVP with a short deadline | Dependency-aware, feasible steps and contingency plan |
| Existing codebase | Add behavior to an existing module | Regression tests, scoped diff, old conventions respected |
| Security | Handle untrusted input or sensitive data | Adversarial test passes, threat and data risks addressed |
| Professional UI | Implement a product-specific light-first dashboard | Functional flow, screenshots at agreed viewports, accessibility checks |
| AI/data | Evaluate a model-assisted feature | Baseline, data provenance, representative metrics, failure analysis |
| Hardware/IoT | Plan a sensor-based prototype | Power/IO constraints, calibration, failure and physical test plan |
| Research project | Compare evidence for a hypothesis | Reproducible sources, method, limitations, falsifiable success criteria |
| Presentation | Explain a real implementation to judges | Claims match code and observed evidence; limitations acknowledged |

## Scoring rubric

Score each dimension 0–4 with written evidence. Define task-specific pass/fail gates for critical correctness and safety.

- **Correctness:** 0 = wrong or dangerous; 1 = mostly wrong; 2 = partial; 3 = correct on expected cases; 4 = expected and important adversarial/edge cases pass.
- **Completeness:** 0 = placeholder; 1 = core behavior missing; 2 = material requirements missing; 3 = acceptance criteria met; 4 = criteria met with relevant edge cases and documentation.
- **Security/data integrity:** 0 = critical unsafe behavior; 1 = major weakness; 2 = partial control; 3 = relevant controls and tests present; 4 = additional adversarial evidence supports the controls. A score is not a security certification.
- **Maintainability:** 0 = unintegrated or incoherent; 1 = poor fit; 2 = workable but awkward; 3 = clear and consistent with the repository; 4 = clear with unnecessary complexity removed without sacrificing safety or completeness.
- **Evidence quality:** 0 = fabricated/unsupported; 1 = vague claims; 2 = some sources/output; 3 = traceable evidence; 4 = reproducible, limitations-aware evidence.
- **Visual quality (UI tasks only):** evaluate hierarchy, consistency, content fit, accessibility, responsive behavior, interaction states, and real screenshots. Do not score aesthetics from source code alone.

Track cost, elapsed time, tokens/turns where available, test status, number of task-completion retries, and human interventions. Do not collapse all metrics into one number unless weighting is defined in advance.

## Reporting template

Publish the model and version, CLI and version, OS, permissions, skill commit/version, task set, run count, failure/timeout policy, raw scores, variance, cost/latency, and known limitations. Link artifacts or sanitized transcripts when legally and ethically permissible. State what was not tested.

A credible result may be neutral or negative. If skills do not improve outcomes, revise or remove the ineffective instructions.

## External references

- [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)
- [SkillsBench](https://github.com/benchflow-ai/skillsbench)
- [Agent Ecosystem skill-validator](https://github.com/agent-ecosystem/skill-validator)
- [Ponytail agentic benchmark](https://github.com/DietrichGebert/ponytail/tree/main/benchmarks/agentic)
