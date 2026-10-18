# Optional Ponytail integration

Official repository: https://github.com/DietrichGebert/ponytail

Ponytail is not part of this toolkit and is not installed by the toolkit installer.

## What is already covered

Builder already directs the coding agent to:
- inspect existing code and conventions before changing them;
- prefer the smallest maintainable solution that satisfies requirements;
- reuse suitable project components and platform features;
- avoid unnecessary dependencies and speculative abstractions;
- trace bugs to their root cause;
- preserve security, boundary validation, error handling, accessibility, and data integrity;
- test meaningful behavior and review the final diff.

## Whether to install it separately

Do not install it solely because it is popular. First inspect the latest official release, installation steps, license, hooks, permissions, and supported host-agent behavior. Consider possible overlap with Builder's instructions and any project-specific rules. Do not grant broader permissions than needed.

If you want to compare it with Builder, use the same representative tasks and same model/CLI configuration with and without the additional skill. Evaluate correctness, security, edge cases, unnecessary code, tests, latency/cost if available, and instruction conflicts. Keep it only if the measured benefits outweigh extra context, cost, complexity, and conflicts.

Its published numbers are upstream author-reported benchmarks for their own task set and environment, not a guarantee of gains on your projects. Reproduce results where practical and account for your own project mix.
