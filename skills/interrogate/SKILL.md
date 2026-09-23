---
name: interrogate
description: Challenge a design or diff with independent adversarial review.
disable-model-invocation: true
---

# Interrogate

Challenge a design or diff for unsafe assumptions, missed consumers, failure modes, and checks that do not prove the claim. Review against the approved contract, not a new preferred architecture.

Before dispatching or returning results, load the [review result contract](../code-review/references/result-contract.md). Give each worker that reference and require its `adversarial` payload; merge verified results through the same contract.

1. Read the source material, selected design, and relevant impact or runtime evidence. Load a principle or policy only when it governs the risk under investigation; stylistic conformity belongs to the Standards axis.
2. For a direct request that warrants independent perspectives, assign bounded risk areas to separate subagents. When already acting as a delegated Adversarial reviewer, inspect the assigned area yourself without spawning another review tree. Report unavailable independence instead of simulating it.
3. Check findings against actual sources or a discriminating probe. Reuse current `blast-radius` evidence; investigate missing consumer impact when needed.
4. Categorize findings as act on, consider, noted, or dismissed, with evidence and reasons. Distinguish hard constraints from judgment calls and keep proposed scope expansion separate.
5. Return the contracted `adversarial` axis as `review/1` JSON. A delegated worker returns only that payload; a direct human-facing request receives a concise rendering unless structured output was requested.

Completion: every finding cites a file, hunk, requirement, consumer, or observation; unresolved claims remain explicitly unproven.
