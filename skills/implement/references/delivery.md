# Delivery mode and branch preparation

Load this reference before implementation or delivery when the task's route, branch, or issue mapping is unresolved.

## Resolve the route

Read `docs/agents/delivery.md` when present. Use an explicit task choice of `direct` or `pr` over the repository default. A request to open a PR chooses `pr`; a request to commit alone does not choose a route. If neither a task choice nor a repository default exists, ask the user rather than infer solo or team intent. Keep task overrides in the task record, not in repository policy.

Resolve the integration repository and branch, PR base, and source remote from the policy, task context, existing task PR, and inspected remotes. Verify branch identities; use the remote's discovered default only when no different target is specified. Ask when multiple targets remain plausible. A task override cannot bypass branch protection or repository contribution requirements.

Record the route, qualified source and target refs, qualified implementation issue references (or none), starting revision, and approved actions in the task record. A route is not authorization for delivery actions. Carry forward the user's requested scope, including any approvals or limits already given.

Use the implementation ticket, not its parent spec, as the issue identity. For a multi-ticket unit, map each ticket to its covered scope. Carry this mapping into commit and PR handoffs, adding their verified references as they exist.

Completion: the route, refs, and issue mapping are unambiguous, and requested actions are distinct from pending decisions.

## Inspect before changing branches

Inspect `git status --short --branch`, staged and unstaged diffs, untracked paths, `git branch --show-current`, `git remote -v`, and the relevant commit range. Refresh the relevant remote refs before relying on their integration state. Preserve the recorded review starting revision across any branch change.

For **direct** delivery, use the intended integration branch only when it contains the task's intended history and changing to it will preserve other work. A feature-branch push is not direct integration. If the current branch cannot safely support the selected route, resolve that mismatch before edits or delivery.

For **PR** delivery, identify both repositories and branches. The source and base must be different refs; matching branch names in different fork repositories are not the same ref. Compare the complete `git log base..HEAD` and `git diff base...HEAD` scope using the resolved base ref, including pre-existing commits. Resolve unrelated commits before selecting a source branch.

Completion: every change that would enter the commit or PR is attributable, and the branch operation preserves unrelated work.

## Prepare PR work

Name new issue-backed branches using repository conventions, or `<type>/<issue-number>-<slug>` by default. For multiple tickets, use one covered ticket's number and retain the full mapping. Preserve existing branch names.

For issue-backed PR work, establish native branch associations through `docs/agents/issue-tracker.md` within authorized remote and tracker writes. Associations that propagate closing links require full-ticket delivery intent and approved closure on merge. Record deferred or unavailable associations as pending.

- **Reuse** a current task branch with the intended base and task-only scope. Do not create another branch merely because a PR is requested.
- **New task:** create a named task branch before edits from the verified base, for example `git switch -c <task-branch> <base-ref>` in a clean worktree. Check the name and existing refs before creation. Use an isolated worktree for concurrent writers or when the current worktree belongs to another task.
- **A late PR request:** task-only uncommitted changes or local commits may be preserved by creating a branch at the current HEAD with `git switch -c <task-branch>`. First verify the full base-to-head scope and worktree ownership. This retains commits and changes without moving the old branch. Explain any local integration branch still pointing at those commits; do not reset it automatically. Mixed work, detached HEAD, or a different intended base requires a safe scope decision before changing refs.
- **Work already integrated** into the target cannot become a meaningful new PR for that same change. Report the actual integration state and ask about any distinct follow-up; do not manufacture a diff by reverting or rewriting history.

Never reset, force-push, discard changes, or automatically stash another task's work to prepare a branch. After a branch operation, verify the current ref, HEAD, worktree/index preservation, and complete PR scope. Branch preparation ends with a usable source ref, not a commit or a publication.
