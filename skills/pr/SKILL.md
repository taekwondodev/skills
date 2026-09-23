---
name: pr
description: Create or update PRs with concise visual explanations.
argument-hint: "[issue or PR] [base] [draft]"
---

# Pull Request

Create or update a GitHub PR when requested. Read `writing-for-agents` before drafting its title or body.

## 1. Resolve the task and PR

Load [delivery mode and branch preparation](../implement/references/delivery.md) to resolve missing route or branch context. Consume existing task evidence and prepare or reuse the source branch when needed; preserve the review starting revision.

Inspect remotes and authenticated GitHub access. Read the associated issue through `docs/agents/issue-tracker.md`, repository PR templates, and any supplied PR. Resolve the target repository, head repository and branch, and base branch explicitly.

Query PRs for that source, including open, closed, and merged states, using `gh pr list` or `gh pr view` with JSON metadata. Match the repository identities as well as head and base branches. Reuse the same open PR on repeated requests. If multiple matches exist, or the relevant PR is closed or merged, ask before choosing a different PR or lifecycle. A lookup failure is not evidence that no PR exists.

For a description-only request, inspect the named PR's published base and head without switching branches, committing, or pushing. Substitute that head for local HEAD below. Stop at the saved draft unless publication was requested.

Completion: the task, intended PR identity, and authorized operations are unambiguous.

## 2. Verify the complete change

Inspect `git status --short`, staged and unstaged changes, untracked files, `git log base..HEAD`, and `git diff base...HEAD`, substituting the resolved base ref. Read the complete diff and enough surrounding code to understand behavior and ownership. Account for every commit and file that would enter the PR. Stop on unrelated scope or an empty task diff.

Consume the task's verification and review evidence. If that evidence does not cover the complete publication scope, return the gap for verification or review before claiming readiness. If uncommitted task changes remain and committing is authorized, load `commit` with the reviewed scope and **local-only** mode, then consume its verified commit result. Otherwise ask for the missing commit authorization. If no commit is needed, reuse the existing revision. Changes after review require affected checks and review again.

Completion: the head revision and complete PR diff are reviewed and verified, or draft publication is approved with its unresolved scope and checks. A description-only update reports the existing verification state without triggering implementation.

## 3. Prepare the description

Load [description guidance](references/description.md) and draft from the verified complete diff, issue, and actual checks. Preserve repository-required sections and human-authored content. Save the proposed body in the task's artifact directory or an available local workspace, outside the commit scope unless the user requests otherwise. Record the destination path for readback and retry.

Use a concise title describing the whole PR. Preserve an existing title and draft state unless changing them is requested. For a new PR, use the requested draft state; otherwise publish ready for review only when the preceding gate is satisfied. Ask when unresolved work makes the intended state unclear.

For fully resolved issue scope and approved closure on merge, use `Closes #N` only when the base is the repository's default branch. Use a non-closing reference for partial work, unapproved closure, or a non-default base. GitHub ignores closing keywords on non-default-base PRs. Leave the issue open while the PR is open; publishing a PR does not complete integration.

Completion: the saved body accurately explains the whole change, preserves required content, and carries only supported check and issue claims.

## 4. Publish or update

When publication and any needed source push are authorized, push the intended revision to the explicit source remote and branch without force. Verify that remote ref with `git ls-remote`; reconcile an unexpected remote advance before publishing. Re-query the intended PR after pushing, including after any ambiguous command failure, to avoid duplicate creation.

For a new PR, use `gh pr create --repo <target> --head <qualified-head> --base <base> --title <title> --body-file <path>`, with `--draft` only for the resolved draft state. Qualify a fork's head using the supported CLI/API identity; do not silently fork or guess a destination if the CLI cannot express it. Explicit head selection avoids the CLI's implicit push/fork path. Add reviewers, labels, or other metadata only when requested or required by the repository.

For an update, compare the current body with the last-published draft when available and preserve human edits. Ask when edits conflict or ownership is unclear. Re-read immediately before `gh pr edit <number> --repo <target> --body-file <path>` to reconcile intervening changes, and preserve unrelated metadata. On partial failure, report the pushed ref or created PR that exists and resume only missing authorized operations.

Read back the exact PR with `gh pr view` JSON, including `url`, `state`, `isDraft`, `baseRefName`, `headRefName`, `headRefOid`, head repository identity, title, and body. Verify the intended repository/ref pair, published revision, and description. Save the published body for the next update's comparison. An unexpected head change invalidates the old verification claim.

Query required checks for that head with `gh pr checks` and the repository's other required gates. Distinguish passing, failing, pending, unavailable, and no configured checks. Keep local test evidence separate from remote CI.

Completion: the intended PR and body are read back, the head revision matches, and actual check states and remaining gates are recorded. This skill never merges, enables auto-merge, or closes an issue directly.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Reference the PR, head revision, and saved description, with publication checks and remaining limits. For a human-facing return, give the PR URL, concise change summary, and outstanding checks or decisions.
