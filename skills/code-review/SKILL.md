---
name: code-review
description: Review a diff on Standards, Spec, and Adversarial axes.
---

# Code Review

Review one completed unit against a fixed point on three separate axes:

- **Standards**: conformity to project conventions, the selected architecture contract, and test quality.
- **Spec**: fidelity to the approved behavior, scope, and acceptance criteria.
- **Adversarial**: unsafe assumptions, missed consumers, and unproven safety or runtime claims.

`implement` requests this gate before committing a completed unit. Direct requests may review a branch, ticket, PR, or working tree. This skill owns review scope and re-review; it does not restart implementation or architecture workflows.

## Result contract

Before dispatching or returning results, load [result-contract.md](references/result-contract.md). Reviewers return `review/1` JSON for their assigned axes; the coordinator verifies and merges it for the caller. Human-facing requests receive a concise rendering unless structured output was requested.

## Scope

- **Small change**: review inline in the same three groups. Read the applicable standards for this review. Escalate when an unresolved hard finding requires independent review.
- **Medium or large change**: run available axes as **parallel sub-agents** with isolated contexts, once after the unit's checks pass. A dependent ticket chain earns one full review at its boundary, not one per intermediate slice.
- **Re-review**: rerun only affected axes, checking the listed fixes and regressions they introduce. After two full rounds without convergence, show the remaining findings to the user.
- Review shipped code, tests, and contracts. Note disposable scripts and evidence artifacts; review them when requested or when they are themselves the deliverable.

## 1. Pin the inputs

Use the supplied fixed point, or the implementation unit's recorded starting commit. Ask when neither exists. Verify it with `git rev-parse`, resolve `git merge-base <fixed-point> HEAD`, and capture `git diff <merge-base>`, `git status --short`, and `git log <fixed-point>..HEAD --oneline`.

This diff includes committed, staged, and unstaged changes. Include untracked paths separately; an empty tracked diff with new files is still reviewable. Stop on an invalid base or genuinely empty review scope.

Find the approved contract from the supplied spec, ticket, agreed-change artifact, or originating issue. Retrieve issue material through `docs/agents/issue-tracker.md` when using the tracker. If no contract is discoverable, ask; if none exists, skip Spec and report that limitation.

## 2. Dispatch only what each reviewer needs

Give each reviewer the resolved base, diff command, untracked paths, commit list, scope, accessible source paths, assigned axis, and result-contract reference. Each worker loads the result contract in its own context. Require reviewers to read their own sources and inspect the actual changes. When a worker cannot access a source, supply its necessary contents or report the missing capability. The parent does not preload or paste the full standards corpus merely to delegate it.

Reuse current `blast-radius` evidence. If consumer impact is unsettled, assign that investigation to the relevant reviewer; send confirmed cross-axis findings to other reviewers when needed.

### Standards

Provide paths to `coding-standards`, the project's conventions, the approved architecture sketch or ADRs, and [the smell baseline](references/standards-review.md). When tests change, include `testing`. The reviewer reads applicable principle bodies only where they affect a concrete decision in the diff.

Review the selected components and ownership, not a universal layer taxonomy. An unresolved architecture contract is a finding, not permission to execute `architect` inside review. Skip rules already enforced by tooling. Separate hard violations from smell heuristics and cite the rule plus file/hunk. Check implementation-coupled, tautological, and self-graded tests against their approved expected behavior.

### Spec

Provide the approved contract. Report missing or partial requirements, unrequested behavior, and incorrect implementations. For a refactoring, check the pinned behavior and selected target-shape contract. Cite the requirement and the relevant change or omission.

### Adversarial

Provide the `interrogate` path, contract, and available impact evidence. The reviewer acts as the bounded adversarial worker, without spawning another review tree. Challenge consumers, migrations, security, runtime effects, and whether checks prove the claims. Categorize findings as act on, consider, noted, or dismissed. Keep stylistic conformity with Standards.

Each reviewer returns only its contracted JSON with evidenced findings and coverage limits. If independent delegation is unavailable, report the limitation; an inline pass is not an independent review.

## 3. Resolve and report

Inspect the cited evidence before accepting findings. Keep **Standards**, **Spec**, and **Adversarial** separate in the merged result and apply the result contract's coverage and gate rules. Return the payload directly to the caller without a second prose report. Do not merge or rerank the axes into one score.

Return blocking actions to the implementer, then rerun affected axes. Preserve unresolved coverage and user-owned judgment calls rather than treating them as a pass or automatic scope expansion.

Completion: every available axis covered the unit, unavailable coverage is explicit, and blocking findings are resolved before the caller commits.
