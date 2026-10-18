# Release and sustainable growth

No repository can guarantee a target number of stars. The actionable objective is to make the toolkit easy to understand, safe to try, demonstrably useful, and maintainable by more than its original author.

## Before publishing

- [ ] Choose the repository name and one-sentence value proposition.
- [ ] Confirm root license and third-party provenance; do not publish unclear licensing.
- [ ] Run `python3 validate_toolkit.py` and `python3 -m unittest discover -s tests -v`.
- [ ] Run representative live tests in each CLI/model environment you claim to support.
- [ ] Run paired behavior evaluations and publish methodology, raw scores, limitations, and failed cases.
- [ ] Build the archive with `python3 scripts/build_release.py`; validate ZIP and verify the SHA-256 manifest.
- [ ] Review docs on a fresh machine using only the README; record any missing prerequisites.
- [ ] Ensure badges reflect real workflows and current status. Do not add invented adoption, benchmark, or compatibility badges.
- [ ] Confirm no API keys, private data, local machine paths, generated cache, or proprietary files are included.
- [ ] Add a tagged release and attach the ZIP plus SHA-256 digest.

## Make the first 60 seconds useful

A new visitor should quickly understand:

1. What problem this toolkit solves better than a generic prompt.
2. How Observer and Builder divide responsibility.
3. The exact quick-start command and a small example.
4. What has been tested versus what remains unverified.
5. How to report a bug or contribute a focused improvement.

Provide a small demo using a representative fixture project. Show the task, prompt, actual diff, tests, and remaining limitations. A reproducible before/after is more persuasive than large claims about being "god tier".

## Grow through usefulness

- Start with a specific user segment: developers coordinating AI agents on time-constrained hackathon projects.
- Ask a small number of developers to use it on real projects and report where instructions fail.
- Turn recurring failures into tests before changing the skill.
- Accept focused contributions with a clear problem and reproducible evidence.
- Publish changelogs and compatibility status honestly.
- Write tutorials around real outcomes, including unsuccessful cases and when the toolkit is not useful.
- Participate in relevant communities transparently; follow their rules and do not spam links.
- Never buy stars, use fake accounts, or imply endorsements or benchmark results that do not exist.

Stars are a lagging signal of reach and perceived utility, not a controllable deliverable. Retention, successful installations, repeat use, issue quality, reproducibility, and independent contributors are better early indicators of whether the project deserves to grow.
