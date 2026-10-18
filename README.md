# Hackathon AI Toolkit

**Research carefully. Build deliberately. Verify with evidence.**

A universal, open-source toolkit for directing AI agents through hackathon discovery, planning, approved implementation, and verification.

> One package. Two roles. One developer-controlled workflow.

## Why this exists

AI coding tools can produce a plausible plan or a lot of code without establishing that either solves the real problem. This toolkit separates the decisions from implementation, gives each phase a bounded responsibility, and asks for evidence before work is called complete.

It is not a guarantee of perfect code, a substitute for engineering judgment, or an automatic project builder. It is a repeatable workflow that can be evaluated and improved.

## The two skills

| Skill | Responsibility | Must not do |
|---|---|---|
| **Hackathon Observer** | Challenge research, evidence and assumptions, feasibility, solution definition, architecture planning, task prompts, risk tracking, and audit | Implement product code or claim that planned work was executed |
| **Hackathon Builder** | Implement explicitly approved tasks, inspect existing code, test, debug, review diffs, and report actual verification evidence | Silently expand scope, bypass safety checks, or claim an unrun check passed |

You remain the project owner, primary developer, prompt orchestrator, and final decision-maker. Teammates are treated as presenters by default unless you explicitly assign engineering tasks.

## Universal by design

Observer classifies the event and project from supplied evidence instead of assuming a single organizer or project type. It can adapt its workflow to software, AI/data, hardware/IoT, research, design, game, business/social-impact, and hybrid projects. Only relevant specialized checks should be activated.

For every project, it should distinguish verified facts, inferences, assumptions, and unresolved questions. It should use the competition's actual rules and rubric when available, rather than hard-code SIH or any other organizer's process.

## Workflow

```text
Official materials + existing project context
                    |
                    v
          OBSERVER: discover and plan
                    |
           Human approves a task
                    |
                    v
          BUILDER: implement and test
                    |
          Actual diff + command output
          + screenshots or other evidence
                    |
                    v
          OBSERVER: review and re-plan
```

The workflow intentionally uses small, verifiable implementation tasks. A skill instructs an agent; it does not grant repository access, shell permissions, browser access, model credentials, hardware access, or deployment capabilities.

## Install

Requirements: Python 3.10+ and an existing local project directory. The installer and structural checks use the Python standard library; individual coding-agent capabilities depend on your host environment.

1. Download and extract the release ZIP.
2. From the extracted `hackathon-ai-toolkit-universal-v1.1.0` directory, run:

   ```bash
   python3 validate_toolkit.py
   python3 -m unittest discover -s tests -v
   python3 install.py --dry-run --project /path/to/your/project
   python3 install.py --project /path/to/your/project
   python3 install.py --check --project /path/to/your/project
   ```

3. Restart or refresh the target CLI if required, and verify that it actually discovers both skills.

To install into your current project, use `--project .`. The installer refuses to overwrite existing skills by default. Use `--upgrade` only when you intend to replace the toolkit-managed directories; it creates a timestamped backup and attempts rollback on failure.

### Installer commands

| Command | Behavior |
|---|---|
| `python3 install.py --project PATH` | Install without overwriting existing skill directories |
| `python3 install.py --dry-run --project PATH` | Show planned action without copying files |
| `python3 install.py --check --project PATH` | Compare installed skills byte-for-byte by relative file content (excluding Python cache files) |
| `python3 install.py --upgrade --project PATH` | Back up existing skill directories, then replace them |
| `python3 validate_toolkit.py` | Validate required files, Markdown links, and both skills' structures |
| `python3 -m unittest discover -s tests -v` | Run installer and package regression tests without network access |

## First-use prompts

### 1. Start with Observer

> Use `hackathon-observer` in Intake/Discovery mode. Classify the event and project modality from supplied evidence. Inspect official challenge materials and accessible repository context, separate facts from assumptions, research relevant existing solutions, and identify high-impact unknowns and feasibility risks. Do not implement or mutate project files.

### 2. Approve a bounded task

Review the plan, choose one task, and confirm its scope and acceptance criteria before asking Builder to implement it.

### 3. Use Builder

> Use `hackathon-builder` in BUILD mode for the approved task below. Inspect repository instructions, working-tree changes, relevant implementation, and existing tests before editing. Keep changes within approved scope, implement the smallest maintainable solution that satisfies the acceptance criteria, add appropriate tests, run relevant available checks, inspect the final diff, and report exact commands and actual outcomes. Do not claim a check passed unless it ran and passed.

### 4. Return evidence to Observer

> Review Builder's completion report and the actual diff, test output, and UI evidence provided. Compare the implementation with the approved acceptance criteria, update only project-state facts supported by evidence, identify remaining gaps, and recommend the highest-value next task. Do not implement changes.

## Compatibility status

The package uses the Agent Skills-style `SKILL.md` folder layout and installs to `<project>/.agents/skills/`. That is an intended portable layout, not a claim that every CLI automatically discovers or executes every part of it.

| Environment | Package status |
|---|---|
| Python structural validator and installer tests | Locally testable using bundled commands |
| OpenCode CLI | Requires live discovery and workflow test in the installed version |
| Antigravity CLI (`agy`) | Requires live discovery and workflow test in the installed version |
| Other Agent Skills-compatible agents | Review each host's skill path, frontmatter, permissions, and tool behavior |

Do not report a CLI as tested until a clean session has discovered and used both skills successfully. Track agent/model/version and test results when evaluating compatibility.

## Quality philosophy

- Correctness and completeness before code-size optimization.
- Inspect the real project before prescribing changes.
- Prefer the smallest complete solution, not the fewest possible lines.
- Keep security, data integrity, accessibility, and required error handling.
- Verify behavior with tests and inspect diffs; test results must be observed, not invented.
- For UI changes, use product-specific art direction and inspect rendered screens when tooling allows. The default aesthetic preference is professional and light-first—not generic dark/purple gradients, neon glow, or glassmorphism.
- Adapt to hardware, research, and non-software projects instead of forcing a web-app workflow.
- Keep the human in control of scope, destructive actions, publication, paid resources, and consequential decisions.

## Measuring whether it helps

Read [`docs/benchmarking.md`](docs/benchmarking.md) before making performance or quality claims. Compare the same agent and model with and without the toolkit on representative tasks, use fresh isolated workspaces, repeat runs, and evaluate correctness, completeness, security, maintainability, visual quality where applicable, cost, and latency. Report failed tests and limitations. A smaller diff is not a win if it omits requirements.

The included behavioral cases are evaluation specifications, not pre-completed proof. This release does not claim cross-agent behavioral success until those runs have been executed and recorded.

## Open-source project files

- [`CONTRIBUTING.md`](CONTRIBUTING.md): development and pull-request expectations.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md): community expectations.
- [`SECURITY.md`](SECURITY.md): vulnerability-reporting guidance and scope.
- [`SUPPORT.md`](SUPPORT.md): reproducible support requests.
- [`LICENSE`](LICENSE) and [`LICENSES.md`](LICENSES.md): license and provenance.
- [`CHANGELOG.md`](CHANGELOG.md): release changes.

## Optional Ponytail integration

[Ponytail](https://github.com/DietrichGebert/ponytail) is not bundled. Builder already follows overlapping principles: inspect existing code, avoid unnecessary abstractions, debug root causes, preserve safety, and verify changes. Read [`docs/optional-ponytail-integration.md`](docs/optional-ponytail-integration.md) before installing another always-on instruction set. Only keep additional rules if a same-task, same-model comparison shows a useful net benefit.

## Current limitations

- Structural checks cannot prove an LLM follows instructions.
- Cross-agent discovery and visual/browser verification depend on the host tools actually available.
- Hardware calibration and physical behavior require real hardware evidence.
- Security scans and tests reduce risk but do not prove that a system is secure.
- Popularity is not guaranteed. The goal is useful, reproducible work that the community can inspect, test, and improve.

## License

Original toolkit materials are licensed under MIT; see [`LICENSES.md`](LICENSES.md) for attribution and third-party provenance details.
