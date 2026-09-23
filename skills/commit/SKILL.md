---
name: commit
description: Create requested commits and handle issue delivery.
argument-hint: "[issue] [push]"
---

# Commit

Start when the user requests a commit, directly or by approving that transition after implementation. Read `writing-for-agents` before drafting messages or tracker comments.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Return verified commit and issue references, distinguish a local commit from a verified push, and preserve any pending user decision.

## Steps

### 1. Gather

Run in parallel:
- `git status --porcelain`
- `git diff HEAD`

For an associated issue, read `docs/agents/issue-tracker.md` and fetch its body, comments, and state. Resolve the target from the user's request or the implementation being committed; ask if ambiguous.

### 2. Stage

```
git add $(git ls-files --modified --others --exclude-standard)
```
Respects .gitignore. Never stages ignored files.

### 3. Generate Message

Conventional Commits format:
- `<type>(<scope>): <summary>`; scope is optional
- Types: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `chore`, `build`, `ci`, `style`, `revert`
- Imperative mood: "add", "fix", "remove"
- Subject ≤50 chars, hard cap 72
- No trailing period
- Never add a body. Subject line only, always.

For an associated issue, append its identifier as a non-closing reference in the subject.

Never include: "This commit does X", emoji.

### 4. Commit

```
git commit -m "<message>"
```
Verify the created revision and committed diff.

### 5. Deliver

Select delivery from the resolved issue state:

- **Open issue:** report the local commit and checks, then ask whether the user is satisfied and approves closure and push. Wait for approval. Once approved and the issue's acceptance criteria are verified, close it with a completion comment and push. Otherwise keep the issue open and the commit local.
- **Already closed issue:** add a follow-up comment to that same issue and push, leaving it closed.
- **No issue:** push only when requested.

Tracker comments state the change, commit reference, and verification. Read back comments and state changes. Push with `git push` and verify the destination branch contains the commit.

Completion: the commit and authorized delivery actions are verified; pending user decisions remain explicit.
