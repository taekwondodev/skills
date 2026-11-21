---
name: arena
description: Compare independent candidate solutions and synthesize the strongest shape.
---

# Arena

Use this for genuinely contested design, architecture, or implementation choices. Do not use it for deterministic mechanical edits.

## Procedure

1. Define the decision, constraints, caller usage, data shape, verification contract, and write fences.
2. Decide the number of candidates. Use at least two for a novel or contested architecture. Keep candidates structurally distinct.
3. Launch one subagent per candidate in parallel, each in a separate context, through the available delegation capability. Give every worker the same grounded context, the decision result contract below, and explicit artifact requirements.
4. Keep parallel writes isolated with explicit git worktrees. Read candidate artifacts directly after completion.
5. Compare candidates on behavior, domain fit, public surface, ownership, dependency direction, reader load, invalid states, security, observability, complexity, migration risk, and verification cost.
6. Select a base and graft only justified parts of other candidates. Do not average incompatible designs.
7. Record the synthesis as a [decision/1](references/result-contract.md) decision.

## Delegation

If delegation is unavailable, report that the independence requirement is unmet rather than presenting same-context alternatives as independent. The parent owns synthesis and verification. Subagent self-reports are not proof.

Completion: the selected shape and each rejected alternative have concrete reasons, a run with fewer candidates records why, and no external or repository state changed without explicit scope.

## Agent result

Load [decision/1](references/result-contract.md) before dispatching candidates or returning to another skill. Consume candidate payloads and inspect their artifacts; return the synthesis through the same contract, preserving the selected base, grafts, rejected alternatives, and limits.
