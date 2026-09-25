---
name: handoff
description: >
  Use when saving unfinished work for a new session or approaching a context limit.
  Write an agent-to-agent checkpoint with the next authorized action, evidence, and remaining obligations.
argument-hint: "What will the next session focus on?"
---

# Handoff

Read `writing-for-agents` before authoring an execution checkpoint for a fresh agent. The artifact must be usable without the previous conversation.

When called by `pause-safely`, use its captured state as input.

## 1. Recover the continuation boundary

Identify the task, current phase, approved scope, authorization limits, next action, and final acceptance source. A requested focus selects the next action without dropping the task's remaining obligations.

Recover decisions from available conversation and artifacts. If required context is missing, retrieve the relevant prior conversation through the available session-history capability. If retrieval is unavailable, record the gap and the action it blocks.

Completion: the next authorized action and its completion criterion are known, or the exact missing decision or evidence is identified as a stop condition.

## 2. Inspect relevant state

Read an existing handoff before replacing it. Reconcile its claims with current sources and retain only information relevant to continuation.

For a Git repository, start with `git status --short --branch`, `git rev-parse HEAD`, and `git diff --stat HEAD`. Inspect relevant diffs, untracked contents, and recent commits as needed to explain unfinished work.

Collect existing verification results and inspect other task state only when the next action depends on it. Record what was observed and what remains unknown.

Completion: evidence distinguishes current observations, earlier results, and unresolved state. The next agent can locate the work and identify what must be refreshed.

## 3. Write the checkpoint

Use the agreed artifact path, otherwise `HANDOFF.md` at the repository root. Use compact Markdown with the headings below in this order and explicit `field: value` bullets. `Resume`, `Evidence and gaps`, and `Remaining work` are required. Omit optional sections without useful content; mark unknown required values explicitly.

### Resume

Put the continuation contract first:

- `task`: stable task reference when available and a concise goal.
- `workspace`: working location.
- `snapshot`: observation time with timezone and relevant state identifiers; for Git, include branch, HEAD, and uncommitted state.
- `phase`: current procedure and its owning skill.
- `authorization`: recorded permissions, limits, and unresolved approval gates, with their source. Mark unknown permissions explicitly.
- `next_action`: one concrete action after reconciliation, or the resolution required to unblock it.
- `required_inputs`: retrievable skill bodies and sources needed for reconciliation and that action. Include `session-pickup` with its source; skill names alone do not supply their instructions.
- `done_when`: observable completion of that action, distinct from completion of the whole task.
- `stop_when`: task-specific approval, safety, or missing-evidence conditions that prevent continuation; state explicitly when none are known.

### Retained context

Keep information whose loss could change the next agent's decisions: non-obvious rationale, relevant failed approaches, blockers, and unfinished work that current sources do not explain. Record progress only when it changes what remains to do.

### Evidence and gaps

For each relevant check or finding, record the command or source, result, state covered, and limits. Distinguish observed results, reported results, and required checks not run. Preserve reproduction details for unresolved findings. State explicitly when no relevant verification is available.

### Remaining work

List subsequent obligations in dependency order, with their acceptance sources. Include the final task completion criterion and any pending task checkpoints, distinct from `done_when` for the next action.

### Sources

List later inputs with the condition that requires reading them; keep immediate inputs in `required_inputs`. When an existing `show-me-your-work` log contains needed evidence, reference it. If a required source may be unavailable to the next agent, retain its essential context in the checkpoint.

Redact secrets, API keys, and PII. `Resume` is the single continuation instruction; the return carries the artifact's locator.

## 4. Check the consumer boundary

Check the written artifact and resolve the references needed for the first action. Without the previous conversation, the consumer must be able to identify the workspace, next action and its authorization, required inputs, completion criteria, stop conditions, and unresolved evidence. Mark inaccessible dependencies explicitly.

Completion: the checkpoint exists and supplies a usable continuation contract or identifies what blocks it. Handoff completion describes context preservation, not completion of the underlying task.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Return the artifact locator, checkpoint checks, unresolved limits, and next action with its completion criterion. At the human-facing boundary, confirm the path briefly.
