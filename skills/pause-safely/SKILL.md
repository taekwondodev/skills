---
name: pause-safely
description: Suspend development work with enough evidence to resume safely.
---

# Pause Safely

Suspend an active task without losing its decisions, evidence, repository state, or next criterion. Use before leaving, restarting the agent, or reaching a context boundary.

## Procedure

1. Record running processes and generated artifacts the next session must find or stop.
2. Save a checkpoint with `handoff`, passing that state as input.
3. Leave external systems unchanged unless the user explicitly requested a durable update.

Completion: the handoff receipt exists and names the next action and its completion criterion.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md) and forward the verified handoff receipt with its next action and completion criterion.
