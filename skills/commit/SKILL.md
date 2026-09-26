---
name: commit
description: Create scoped commits and authorized direct delivery.
argument-hint: "[issue] [local-only] [push]"
---

# Commit

Start when the user requests a commit, directly or by approving that transition after implementation. Read `writing-for-agents` before drafting messages or tracker comments. A caller may require `local-only`; in that case create local history without push, tracker writes, or PR publication.

## 1. Resolve scope and delivery

Consume the reviewed scope, verification evidence, issue reference, and approved actions from the task. For a standalone invocation, inspect the changes and establish that scope before staging. Load [delivery mode and branch preparation](../implement/references/delivery.md) to resolve any missing route, branch, or issue mapping. Reuse a current resolution rather than asking again.

Inspect `git status --porcelain`, `git diff HEAD`, `git diff --cached`, unstaged changes, and untracked files. Stop on conflicts or an in-progress Git operation. For associated issues, read `docs/agents/issue-tracker.md` and fetch each issue's body, comments, and state; ask only when the intended mapping is ambiguous.

Completion: the commit boundary is explicit, its verification evidence is available, and local versus publication authority is recorded.

## 2. Stage the reviewed scope

Inspect the entire index, including content staged before this task. If unrelated staged changes exist, stop and ask for their separation; leave them untouched. Scope mixed files by reviewed hunks or ask when the intended split is uncertain.

Stage explicit, quoted task paths with `git add -- <task-paths>`, including deletions. Preserve path boundaries for spaces and other special characters; do not expand a whitespace-separated file list in the shell. Review `git diff --cached` and its path list after staging. Leave unrelated unstaged and untracked work alone.

Completion: the complete staged diff, not merely the paths just added, matches the reviewed scope. If there is no task diff, report that no commit is needed rather than create an empty commit.

## 3. Write the message and commit

Use a Conventional Commits subject: `<type>(<scope>): <summary>`, with optional scope. Types are `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `build`, `ci`, `style`, and `revert`. Use imperative mood, aim for 50 characters, and enforce a 72-character cap. Use no trailing period or emoji. The message is always subject-only, with no body.

Append each implementation issue covered by the commit as a non-closing reference in the subject; use repository-qualified identifiers for other repositories. Keep identifiers intact; resolve message-length conflicts before committing. Run `git commit -m "<message>"`. Verify the issue references against the recorded mapping, the created revision, complete committed diff, and remaining worktree/index against the approved scope. If hooks changed the artifact, inspect and reverify affected behavior before delivery.

Completion: the verified commit contains the task changes and no unrelated work; otherwise report the mismatch without rewriting history automatically.

## 4. Deliver only as authorized

- **Local-only or no publication approval:** report the local commit and checks, preserving any pending push or closure decision. An open issue stays open.
- **PR route:** return the local commit. Outside local-only mode, when PR publication is requested, load `pr` with the commit, reviewed scope, checks, issue, resolved refs, and approved actions.
- **Direct route with push approval:** verify that the entire outgoing range belongs to the authorized delivery and targets the configured integration ref. Push explicitly with `git push <remote> HEAD:refs/heads/<integration-branch>`, without force. Use `git ls-remote` and, if the ref has advanced, fetch the observed target and verify that it contains the delivered commit. A source-branch push alone is not integration.

For direct delivery, verify the integration and required checks for the delivered revision before closing an issue. If push fails, integration is unverified, checks are pending or failing, or acceptance criteria remain incomplete, keep the issue open and report the actual state. Once those gates pass, obtain closure approval if not already given, post the completion comment, and close the issue. For an already closed issue, keep it closed and add a follow-up comment only when that tracker update is authorized; its state grants no push permission. With no issue, perform only the requested delivery.

Read back exact tracker comments and state changes. On retry, inspect the existing commit, remote ref, comments, and issue state; resume only missing authorized actions rather than duplicate the commit or completion comment.

Completion: the local commit and each authorized external action have verification evidence; unresolved actions remain explicit.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Reference the verified commit, any delivered remote ref and issue, and the checks performed. Distinguish local commit, verified integration, and pending decisions.
