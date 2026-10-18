# Release checklist

## Engineering gates

- [ ] `python3 validate_toolkit.py` passes.
- [ ] `python3 -m unittest discover -s tests -v` passes.
- [ ] Both skill-level structural validators pass.
- [ ] Failure-path install and upgrade tests pass.
- [ ] Deterministic archive builds and passes ZIP integrity validation.
- [ ] SHA-256 manifest is created and matches the release archive.
- [ ] No secrets, user data, unlicensed copied content, or local cache files are included.
- [ ] Version, changelog, root README, skill metadata, and release notes agree.

## Behavioral gates

- [ ] Run Observer on representative discovery and planning tasks.
- [ ] Run Builder on real repository tasks with tests and failure cases.
- [ ] Compare with and without skills under controlled, documented conditions.
- [ ] Record model, version, host CLI, permissions, repetitions, cost/time, failures, and limitations.
- [ ] Inspect actual rendered screenshots for UI tasks when the environment supports it.
- [ ] Mark unsupported/unavailable target CLIs as untested rather than claiming universal compatibility.

## Public release gates

- [ ] License and provenance reviewed.
- [ ] CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, and SUPPORT files are present.
- [ ] Issue and PR templates are usable.
- [ ] CI has passed on the release commit.
- [ ] Release ZIP and SHA-256 digest are attached to the tag.
- [ ] Fresh-user install documented and attempted.
- [ ] Known limitations and compatibility status are published.

A release is not blocked by lack of evidence for every possible model, but unsupported claims must be removed and untested environments clearly labeled.
