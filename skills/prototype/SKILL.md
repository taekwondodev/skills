---
name: prototype
description: Build disposable alternatives to settle a technical or behavioral fork.
---

# Prototype

Use a small disposable experiment when observation can resolve a technical or behavioral fork faster than discussion. A prototype informs a decision. It does not decide product scope or user preference.

## Procedure

1. State the question and the observation that would distinguish the candidates.
2. Define the smallest useful input, output, and verification check.
3. Build structurally distinct alternatives when the choice is architectural.
4. Run the same comparison against every candidate.
5. Record behavior, complexity, failure modes, and measurements.
6. Return the evidence to the invoking skill without silently retaining prototype code.

Completion: the result states what was learned, what remains undecided, and any retained prototype scope.

## Agent result

For an agent-facing return, load [evidence/1](../investigation/references/result-contract.md). Include each candidate's outcome against the shared check, evidence locators, retained artifact scope, and the unresolved decision.
