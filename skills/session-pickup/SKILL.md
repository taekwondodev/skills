---
name: session-pickup
description: Resume prior development work from its artifacts and live repository state.
disable-model-invocation: true
---

# Session Pickup

Resume work from a prior session, agent, transcript, branch, issue, or handoff. Trust current artifacts and repository state over a stale summary.

## Procedure

1. Locate the handoff, issue, plan, transcript, branch, and current task. When given a structured receipt, resolve its artifact references and read the source material instead of treating the receipt as the handoff.
2. Inspect git status, diff, recent commits, tests, and generated artifacts.
3. Reconcile the prior summary with the current repository. Surface contradictions.
4. Recover settled decisions, open questions, applicable principles, and the next completion criterion.
5. Confirm the task identity before continuing. Use `new task` when the requested work is different.
6. Resume the owning skill or route through `dev-cycle`.

## Agent result

For an agent-facing context-recovery return, load [delivery/1](../implement/references/result-contract.md). Reference the reconciled sources, retain stale or missing evidence as limits, and give the next action and completion criterion. If the requested work continues into another phase, return that phase's result instead of an intermediate report.

## Verification

The current repository state, prior artifacts, and next action agree. Stale or missing context is explicit. No work is claimed complete from a handoff alone.
