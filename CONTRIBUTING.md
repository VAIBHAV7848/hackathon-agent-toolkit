# Contributing

Thanks for considering a contribution. The goal is to make this toolkit more
reliable and more useful across hackathons, project modalities, and coding
agents—not merely larger.

## Before opening an issue

- Search existing issues and discussions for the same problem.
- Include the toolkit version, operating system, CLI/agent and model versions,
  exact command, minimal reproduction, and relevant output.
- Remove secrets, personal data, private challenge information, and proprietary
  repository content from logs and examples.

## Before opening a pull request

1. Explain the user problem and the evidence that it exists.
2. Keep changes focused. Do not copy another project's skill or code without
   confirming its license and preserving required notices.
3. Update the relevant skill, reference, template, tests, README, and changelog
   when behavior or public usage changes.
4. Run `python3 validate_toolkit.py` and `python3 -m unittest discover -s tests -v`.
5. If changing installation behavior, add a regression test. If changing agent
   instructions, add or update a behavioral scenario and describe how it should
   be evaluated in a real supported CLI.
6. Do not claim behavioral improvement without a reproducible with-skill versus
   no-skill comparison or clearly described evidence.

## Design principles

- Evidence over claims; tests over assurances.
- Minimal complete scope, not minimal code at any cost.
- Security, accessibility, data integrity, and user approval are not optional.
- Keep Observer planning-only and Builder implementation-oriented.
- Adapt to the project and competition; never assume every hackathon is SIH or
  that every project is a web application.
- Favor small, inspectable changes and preserve user modifications.

By submitting a contribution, you agree to the terms in `LICENSES.md`.
