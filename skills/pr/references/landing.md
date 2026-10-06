# Landing

Load this reference when the user chooses to land a published PR: squash and merge it, update the local base, and clean up the task's local branch and worktrees. Use the expected closing-issue set recorded at publication for issue verification.

## 1. Read the PR state

Re-read the PR with `gh-axi api /repos/<owner>/<repo>/pulls/<number> --full` and its checks with `gh-axi pr checks`.

- Already merged: record `merge_commit_sha` and continue from step 3 with the steps still missing.
- Open, not a draft, mergeable, head SHA equal to the locally verified revision, required checks passing or none configured: continue with step 2.
- Any other state: report it and stop; nothing was merged.

Completion: the PR lifecycle, head SHA, base ref, merge commit when present, and check state are recorded.

## 2. Squash and merge

Send the merge through the API with the verified head pinned:

```text
gh-axi api PUT /repos/<owner>/<repo>/pulls/<number>/merge --input <body.json>
```

with body `{"merge_method":"squash","sha":"<verified head>","commit_title":"<PR title> (#N)","commit_message":""}`.

Read the PR back and record `merged`, `merge_commit_sha`, and the merged head. Perform no local change before this readback.

Completion: the readback shows `merged: true` with the merge commit SHA recorded.

## 3. Update the base checkout

In the primary checkout, inspect `git status --short --branch`. If there are uncommitted changes, report their paths and stop without changing the checkout. With a clean checkout, switch to the base branch, fetch the base remote, and merge fast-forward only. A diverged base stops here with its state reported.

Completion: the base branch tip equals the remote base tip and the merge commit is reachable from it.

## 4. Remove task worktrees and the local branch

Read the worktrees recorded for this task in the task record, as written during [branch preparation](../../implement/references/delivery.md#prepare-pr-work), and the current `git worktree list`. If no worktrees are recorded, skip removal.

For each recorded worktree, confirm that its path is listed by `git worktree list` with the recorded branch checked out, then run `git worktree remove --force -- <path>` even if it has uncommitted changes. A recorded path that is absent from the list, or that holds a different branch, is reported as stale and left untouched.

Any other worktree holding the task branch stays untouched: report its path, mark the branch `held`, and skip branch deletion.

When no worktree holds the branch, run `git branch -D <task-branch>`.

Completion: every recorded worktree is removed or reported as stale, every other worktree holding the branch is reported, and the branch is `deleted` or `held`.

## 5. Verify issue closure

For each issue in the expected closing set recorded at publication, read its state and report `closed`, `open`, or `unverified`. Close an expected issue that remains open without adding a comment, then read its state back. Issues outside the expected set stay as they are.

Completion: every expected issue has one of the three states recorded.

## Agent result

For an agent-facing return, load [delivery/1](../../implement/references/result-contract.md). Reference the PR, merge commit SHA, base tip, removed and stale worktrees, branch state (`deleted` or `held` with the holding path), and each issue state. A stopped step keeps the merge that exists and lists the local steps still pending.
