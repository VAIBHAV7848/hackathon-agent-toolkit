# Third-Party Skill / Harness Audit Report

## 1. Candidate identity
- Name:
- Canonical repository URL:
- Owner/maintainer:
- Exact commit/tag or version reviewed:
- Review date:
- License and attribution obligations:
- Intended use in Observer:
- Decision owner:

## 2. Fit and maturity
- Problem this candidate solves:
- Evidence of maintenance (recent commits, releases, issue handling):
- Relevant supported agents/versions:
- Required dependencies, credentials, services, and estimated cost:
- Why existing Observer files are insufficient:
- Proposed minimal adoption (specific skill/module only):
- Lower-risk alternative:

## 3. Source and license review
- [ ] Canonical source verified.
- [ ] License file and per-skill licensing checked.
- [ ] Copied content, upstream dependencies, attribution, and notices identified.
- [ ] References resolve and point to the expected project.
- [ ] Version or commit is pinned for reproducible review.

## 4. Capability and side-effect review
- Instructions/tools requested:
- Scripts/hooks/package install behavior:
- File-system access and writes:
- Process/subprocess execution:
- Network endpoints/downloads:
- Environment/credential access:
- External services and telemetry:
- Hidden/obfuscated files or instructions:
- Prompt injection / policy override / secrecy / persistence signals:
- Potential conflict with Observer's planning-only default:

## 5. Validation evidence
| Check | Tool/version | Scope | Result | Limitations |
|---|---|---|---|---|
| Structural/spec | | | Not run / Pass / Partial / Fail | |
| Link/reference validation | | | Not run / Pass / Partial / Fail | |
| License/provenance | Manual/source | | Not run / Pass / Partial / Fail | |
| Static/security scan | | | Not run / Pass / Partial / Fail | |
| Target CLI discovery | | | Not run / Pass / Partial / Fail | |
| Representative behavior test | | | Not run / Pass / Partial / Fail | |
| With/without-skill evaluation (if warranted) | | | Not run / Pass / Partial / Fail | |

## 6. Evaluation design (if tested)
- Task and expected behavior:
- Negative/adversarial test:
- Model + CLI + version:
- Conditions held constant:
- Number of runs / judge method:
- Baseline score/results:
- Candidate score/results:
- Quality lift and uncertainty:
- Token/time/cost overhead:
- Regressions or critical violations:

## 7. Findings
| Severity | Evidence/line or file | Risk/consequence | Recommended treatment |
|---|---|---|---|

## 8. Decision
Choose one: `adopt` / `adopt-with-changes` / `reference-only` / `quarantine` / `reject`.

- Rationale:
- Exact files/content to reuse (if allowed):
- Required adaptations:
- Follow-up tests:
- Review-by date or revalidation trigger:

> A clean scan or a successful single run does not prove a skill is safe, effective, or cross-agent compatible. Clearly state untested areas.
