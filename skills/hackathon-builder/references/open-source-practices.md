# Open-Source Engineering Practice Notes

This is a curated reading list, not a claim that every open-source coding agent or skill has been exhaustively audited. Projects change; check current repository state, license, supported versions, maintenance, and security posture before depending on them. The Builder uses the ideas below as engineering patterns, not as authority over the user's repository or project scope.

## Useful projects and transferable ideas

- **obra/superpowers** — https://github.com/obra/superpowers : explicit design/specification, small plans, TDD, root-cause debugging, code review, and verification-before-completion. Adopt workflow principles; keep this Builder authorized to implement only the user-approved task.
- **anthropics/skills** — https://github.com/anthropics/skills : examples of focused `SKILL.md` workflows and a frontend-design skill emphasizing specific visual identity, design critique, accessibility, and screenshots. Do not copy their skill text; inspect the repository's license and terms before any reuse.
- **addyosmani/agent-skills** — https://github.com/addyosmani/agent-skills : production UI, API/interface design, browser verification, debugging, and code-review patterns.
- **Aider** — https://github.com/Aider-AI/aider : automatic lint/test feedback and benchmark thinking around whether code edits pass executable tests. Its benchmark documentation explicitly notes that executing model-generated code is safer in an isolated container.
- **mini-swe-agent** — https://github.com/SWE-agent/mini-swe-agent : small tool loop and simple, hackable engineering-agent architecture. The SWE-agent repository now recommends mini-swe-agent for current development direction; do not assume older SWE-agent recipes are current.
- **Cline** — https://github.com/cline/cline : user-visible tool use, project rules/skills, large agent codebase, and a visible evaluation/test ecosystem. Study patterns rather than copying implementation wholesale.
- **OpenCode skills docs** — https://opencode.ai/docs/skills/ : supported skill path and metadata. Verify discovery in the installed version.
- **Agent Skills specification** — https://github.com/agentskills/agentskills : interoperable skill-folder conventions; use current spec and target-CLI documentation.

## Engineering principles derived for this skill

1. Inspect current repository state before editing.
2. Reproduce and investigate before fixing.
3. Prefer a narrow, testable patch over broad rewrites.
4. Test behavior and inspect final diffs.
5. Separate a passing build from complete verification.
6. For UI, design intentionally from product/audience/content and inspect actual rendering; don't rely on aesthetic adjectives alone.
7. Use isolation when executing untrusted generated code.
8. Keep user control over irreversible changes, external services, and scope expansion.

## What not to do

- Do not clone an entire popular skill collection into the user's skill directory.
- Do not assume stars prove correctness or that a clean scanner proves safety.
- Do not mix incompatible assumptions or licences from different projects into one bundle.
- Do not claim any practices guarantee bug-free or non-AI-looking code. Use measurable checks and honest limitations.
