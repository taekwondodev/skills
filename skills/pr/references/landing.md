# Landing

Load this reference when the user chooses to land a published PR: audit its documents and tests, squash and merge it, update the local base, and clean up the task's local branch and worktrees. Use the expected closing-issue set recorded at publication for issue verification.

## 1. Read the PR state

Re-read the PR with `gh-axi pr view <number> --repo <owner>/<repo> --fields state,isDraft,mergeable,baseRefName,headRefOid,mergeCommit,title` and its checks with `gh-axi pr checks <number> --repo <owner>/<repo>`. A non-zero exit from `pr checks` reports check state (1: a check failed or none are reported; 8: a check is pending), not a command failure.

- Already merged (`state: MERGED`): record `mergeCommit.oid` and continue from step 4 with the steps still missing.
- Open, not a draft, `mergeable: MERGEABLE`, `headRefOid` equal to the locally verified revision, required checks passing or none configured: continue with step 2.
- Any other state: report it and stop; nothing was merged.

Completion: the PR lifecycle, head SHA, base ref, merge commit when present, and check state are recorded.

## 2. Audit documents and tests

Skip this step when the task record shows it complete for the verified head. Otherwise list the paths of the PR's complete diff with `git diff --name-only <base>...<verified head>` and run each audit whose condition holds:

- **A Markdown file changed:** load `writing-for-agents` and run its [document audit](../../writing-for-agents/references/audit.md) on that diff.
- **A test was added or modified:** load `testing` and run its [change audit](../../testing/references/audit.md#change-audit) on that diff.

The landing request authorizes the audit's fixes and their publication. With no fixes, record the audit against the verified head and continue with step 3. With fixes, rerun the checks they affect and load `commit` with the audited scope and **local-only** mode. Push the new head and update the PR through [publication](../SKILL.md#4-publish-or-update), revising the description only where a fix changes one of its claims. Record the audit against the new head, wait for its checks with `gh-axi pr checks <number> --repo <owner>/<repo> --watch`, and return to step 1.

Completion: each audit that applies has a verdict for every changed Markdown file or test, and the task record names the PR head the audit covers.

## 3. Squash and merge

Send the merge through the API with the verified head pinned:

```text
gh-axi api PUT /repos/<owner>/<repo>/pulls/<number>/merge --input <body.json>
```

with body `{"merge_method":"squash","sha":"<verified head>","commit_title":"<PR title> (#N)","commit_message":""}`.

Read the PR back with the same `pr view` command and record `state`, `mergeCommit.oid`, and `headRefOid`. Perform no local change before this readback.

Completion: the readback shows `state: MERGED` with the merge commit SHA recorded.

## 4. Update the base checkout

In the primary checkout, inspect `git status --short --branch`. If there are uncommitted changes, report their paths and stop without changing the checkout. With a clean checkout, switch to the base branch, fetch the base remote, and merge fast-forward only. A diverged base stops here with its state reported.

Completion: the base branch tip equals the remote base tip and the merge commit is reachable from it.

## 5. Remove task worktrees and the local branch

Read the worktrees recorded for this task in the task record, as written during [branch preparation](../../implement/references/delivery.md#prepare-pr-work), and the current `git worktree list`. If no worktrees are recorded, skip removal.

For each recorded worktree, confirm that its path is listed by `git worktree list` with the recorded branch checked out, then run `git worktree remove --force -- <path>` even if it has uncommitted changes. A recorded path that is absent from the list, or that holds a different branch, is reported as stale and left untouched.

Any other worktree holding the task branch stays untouched: report its path, mark the branch `held`, and skip branch deletion.

When no worktree holds the branch, run `git branch -D <task-branch>`.

Completion: every recorded worktree is removed or reported as stale, every other worktree holding the branch is reported, and the branch is `deleted` or `held`.

## 6. Verify issue closure

For each issue in the expected closing set recorded at publication, read its state and report `closed`, `open`, or `unverified`. Close an expected issue that remains open without adding a comment, then read its state back. Issues outside the expected set stay as they are.

Completion: every expected issue has one of the three states recorded.

## Agent result

For an agent-facing return, load [delivery/1](../../implement/references/result-contract.md). Reference the PR, the audit verdicts with any commit they produced, merge commit SHA, base tip, removed and stale worktrees, branch state (`deleted` or `held` with the holding path), and each issue state. A stopped step keeps the merge that exists and lists the local steps still pending.
