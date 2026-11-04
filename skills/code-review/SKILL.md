---
name: code-review
description: Review design, contract fidelity, and adversarial risks without repeating verified mechanical checks.
---

# Code Review

Review one completed unit against a fixed point. Keep three reporting axes:

- **Standards**: uncovered project obligations, the selected design, maintainability, and test quality.
- **Spec**: fidelity to the approved behavior, scope, and acceptance criteria.
- **Adversarial**: unsafe assumptions, missed consumers, and unproven safety or runtime claims.

Tools supply mechanical evidence; reviewers evaluate what that evidence cannot establish. `implement` requests this gate before committing a completed unit. Direct requests may review a branch, ticket, PR, or working tree.

## Result contract

Before dispatching or returning results, load [result-contract.md](references/result-contract.md). Reviewers return `review/1` JSON for their assigned axes; the coordinator verifies and merges it. Human-facing requests receive a concise rendering unless structured output was requested.

## Scope

- **Small change**: review inline. The risk gate can still require independent Adversarial review. Escalate unresolved hard findings that need an independent judgment.
- **Medium or large change**: run an independent semantic reviewer for Standards and Spec after the unit's checks pass. That reviewer also owns the risk gate; dispatch a separate Adversarial worker only when it requires one. Split the semantic assignment only when scope or expertise warrants another worker. A dependent ticket chain earns one full review at its boundary.
- **Re-review**: rerun only affected axes, checking fixes and regressions. Apply the result contract's skip-invalidation rule before retaining an earlier risk-gate decision. After two full rounds without convergence, show the remaining findings to the user.
- Review shipped code, tests, and contracts. Review disposable scripts and evidence artifacts when requested or when they are themselves the deliverable.

## 1. Pin the inputs

Use the supplied fixed point, or the implementation unit's recorded starting commit. Ask when neither exists. Verify it with `git rev-parse`, resolve `git merge-base <fixed-point> HEAD`, and capture `git diff <merge-base>`, `git status --short`, and `git log <fixed-point>..HEAD --oneline`.

Include committed, staged, unstaged, and untracked changes. Stop on an invalid base or genuinely empty scope.

Find the approved contract from the supplied spec, ticket, agreed-change artifact, or originating issue. Retrieve tracker material through `docs/agents/issue-tracker.md`. If no contract is discoverable, ask; if none exists, skip Spec and report that limitation.

Inspect supplied check commands, outcomes, scope, and retrievable logs. Treat a mechanical rule as covered only while its evidence matches the reviewed code, inputs, configuration, and toolchain. Do not repeat covered checks. For missing, stale, or failed evidence, obtain the relevant check or retain the gap under the result contract's coverage gates. The presence of a tool alone proves nothing. Review relevant check-configuration changes and the claims the tools do not establish.

## 2. Assign judgments, not checklists

Give each reviewer the resolved base, diff command, untracked paths, commit list, assigned axes, approved contract, check evidence, accessible source paths, and result-contract reference. Require reviewers to read their own sources and inspect the actual changes. The parent does not preload or paste the full standards corpus; provide necessary excerpts only when a source is inaccessible.

Reuse current `blast-radius` evidence. Assign unsettled consumer impact to the relevant reviewer and share confirmed cross-axis findings when needed. If independent delegation is unavailable, report the limitation; an inline pass is not an independent review.

### Standards

Provide project conventions and the approved architecture sketch or ADRs. When tests change, include `testing`. For a concrete type, boundary, migration, readability, or runtime-cost concern, select its canonical owner through [the principle index](../dev-cycle/references/principles.md) and read that body, not the entire corpus. Use [the smell baseline](references/standards-review.md) only for a relevant design concern.

Judge components, ownership, abstractions, and comprehensibility against the actual project. An unresolved architecture contract is a finding, not permission to execute `architect` inside review. Inspect whether tests prove the approved behavior rather than the implementation's own assumptions. A hard violation requires an applicable binding rule and a concrete file/hunk. Report other principle and smell-baseline violations in the changed code as smells. Give each smell an action that [Style Serves Outcomes](../principle-style-serves-outcomes/SKILL.md) accepts. When a hard or smell finding is mechanically decidable, extend its action to encode the rule in a tool the project already runs, choosing the mechanism through [Encode Lessons in Structure](../principle-encode-lessons-in-structure/SKILL.md) and naming the tool, rule, and configuration file.

### Spec

Report missing or partial requirements, unrequested behavior, and incorrect implementations. For a refactoring, check pinned behavior and the selected target-shape contract. Cite the requirement and the relevant change or omission.

### Risk gate

The semantic reviewer reads [risk-gate.md](references/risk-gate.md) and returns the Adversarial disposition alongside Standards and Spec. The implementer supplies evidence, not the decision.

When the disposition requires independent review, give the Adversarial worker `interrogate`, the named risks, the contract, and available impact and verification evidence. It challenges those claims without spawning another review tree. Keep stylistic conformity with Standards.

### Reusable verification

When a finding warrants a reusable check, name the property and the evidence missing from existing checks. If the method is unsettled, read [verification selection](../formal-verification/references/selection.md) and use its comparison to choose the cheapest adequate check. Read [formal-verification](../formal-verification/SKILL.md) only when a formal method is selected or an existing formal check needs upkeep.

Return the proposed check in the finding's action, not as an extra report. Review identifies the obligation; implementation adds the check within approved scope. An optional improvement is not a blocker by itself; an unproven safety claim remains a coverage gap until adequate evidence or an explicit user decision resolves it.

## 3. Resolve and report

Inspect cited evidence before accepting findings. Keep **Standards**, **Spec**, and **Adversarial** separate even when one worker covers multiple axes, and apply the result contract's coverage and gate rules. Return the payload directly to the caller without a second prose report. Do not merge or rerank the axes into one score.

Return blocking actions to the implementer, then rerun affected axes. Route smells under the result contract. Preserve unresolved coverage and user-owned judgment calls rather than treating them as a pass.

Completion: every required axis covered the unit, unavailable coverage is explicit, and blocking findings are resolved before the caller commits.
