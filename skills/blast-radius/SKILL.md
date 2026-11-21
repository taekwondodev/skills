---
name: blast-radius
description: Find what a change could break beyond the immediate diff.
---

# Blast Radius

Find dependencies and behavior outside the obvious diff before a change ships. Prove safety with repository searches and real checks rather than assertions.

## Procedure

1. Identify the changed symbol, contract, data shape, or behavior.
2. Search all callers, implementers, serializers, migrations, fixtures, docs, and external boundaries.
3. Classify each affected consumer and likely failure mode.
4. Load [principle-prove-it-works](../principle-prove-it-works/SKILL.md) when the important safety assumption depends on public runtime behavior. Use its proportional-proof guidance to select a check against the real artifact.
5. Run the smallest check that proves the important safety assumption.
6. Return the findings to `to-spec`, `implement`, or `code-review`.

Completion: every claimed consumer comes from an actual search, important assumptions have a check or are marked unproven, and confirmed impact is distinguished from plausible risk.

## Agent result

For an agent-facing return, load [evidence/1](../investigation/references/result-contract.md). Identify each affected consumer in its claim and distinguish confirmed impact from plausible risk.
