---
name: how
description: Explain how a subsystem works, including flow, ownership, and boundaries.
---

# How

Explain how a subsystem works well enough for a senior engineer to change it safely. Trace the real path from trigger to effect through entry points, callers, callees, types, persistence or external effects, and tests, following symbols across module boundaries. Record ownership, dependency direction, validation, error conversion, observability, and security boundaries. If the scope is ambiguous, state your interpretation and proceed. For a broad subsystem, give independent read-only workers distinct angles and merge their verified findings in flow order.

For a human, present an overview, key concepts, the flow, ownership, and gotchas.

Completion: every flow step cites a file and symbol, and inferred behavior and open uncertainty are labelled.

## Agent result

Load [evidence/1](../investigation/references/result-contract.md) for workers and agent-facing returns. Keep the traced flow ordered and retain ownership, boundaries, and source symbols in the findings.
