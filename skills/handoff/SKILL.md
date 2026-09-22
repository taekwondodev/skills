---
name: handoff
description: >
  Context bridge for session continuity. Synthesizes conversation state, git status, and pending
  work into a structured HANDOFF.md, then produces a copy-paste resume prompt for the next session.
  Invoke when user says "save context", "new session", "continue later", "save progress",
  "running out of context", "handoff", "context limit", or when context window is nearly full
  and the current task is incomplete.
argument-hint: "What will the next session focus on?"
---

## Steps

Read `writing-for-agents` before writing `HANDOFF.md` or its resume prompt. Its general writing rules govern the handoff; this skill adds only handoff-specific structure.

Use `pause-safely` as the suspension contract and this skill as the artifact writer. Use `session-pickup` in the next session to reconcile the handoff with live repository state. When conversation context is incomplete, retrieve the relevant prior conversation through the available session-history capability and reconcile it with live state. If required history access is unavailable, record the missing evidence instead of inventing it. When long or unattended work has a `show-me-your-work` log, point to it instead of copying it.

Apply the canonical principles where they change the artifact:

- `principle-guard-the-context-window` keeps the handoff context-lean and links large sources instead of embedding them.
- `principle-prove-it-works` requires current git, test, process, and artifact evidence before progress is called complete.
- `principle-sequence-verifiable-units` makes the next action singular and gives it an exact completion criterion.

### 1. Gather State

Run: `git status && git diff HEAD && git log --oneline -10`

### 2. Synthesize

Extract from conversation + git state:

- **Task:** goal in 1-3 sentences. If args given, weight toward that focus.
- **Mode:** current `dev-cycle` mode, phase, and active capabilities
- **Progress:** done items (file names, functions, decisions)
- **What Didn't Work:** failed approaches that the next agent should not repeat
- **Pending:** ordered, most critical first
- **Decisions & Context:** non-obvious choices, constraints, gotchas a fresh agent can't derive from code
- **Files Changed:** path: one-line description
- **Blockers:** stuck or unclear items
- **Verification:** tests, checks, measurements, and processes with their latest observed result
- **Next Completion Criterion:** the exact observable state the next session should reach
- **Current phase:** the procedure still needed and the artifacts it consumes
- **Next skills:** only skills needed for the next action, not every skill previously used

The handoff is a pointer, not a copy of another skill's procedure. Preserve the canonical owner of every rule and record which principles changed decisions.

Policies:
- Don't duplicate PRDs, plans, ADRs, issues, or commits. Reference them by path or URL
- Redact secrets, API keys, PII

### 3. Write & Output

Write to `HANDOFF.md` at the repository root.

Add `## Resume Prompt` at bottom. It must be self-contained and copy-paste ready.
Name the next procedure, its source, and its inputs. Include the skill bodies needed for the next action as explicit reads:
```
Read `HANDOFF.md`. We are working on <project>: <task goal>.
Load <next skill> from <retrievable source> and read <required inputs>.
Continue from the Pending section toward <next completion criterion>.
```

Then confirm the path, print the Resume Prompt in chat, and say "Open new session, paste prompt above."
