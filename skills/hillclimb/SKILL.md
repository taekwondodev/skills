---
name: hillclimb
description: Improve one metric through measured keep-or-revert iterations.
---

# Hillclimb

Improve one measurable result against an explicit target through repeated experiments. One change and one measurement make each iteration. Use a decision log for sustained work.

## Procedure

1. Define the realistic workload, metric, direction of improvement, target, and stop predicate.
2. Build and freeze a sensitive measurement harness.
3. Record the baseline and green regression gate.
4. For each iteration, record one hypothesis, implement one change, measure before and after, run the gate, and keep or revert the change.
5. Push past the first plateau by changing hypothesis category or revisiting the grounded architecture.
6. Stop only when the predicate is met, cheap hypotheses are exhausted, or the remaining cost is explicitly accepted.

## Agent result

For an agent-facing return, load [measurement/1](../perf-issue/references/result-contract.md). Link the complete trial log and return the retained result, actual stopping reason, and remaining hypotheses without replaying every iteration.

## Verification

Every attempt has a recorded result and verdict. Accepted changes clear noise and preserve correctness. Rejected changes are fully reverted. The result includes baseline, final metric, and remaining ideas; derive the delta from those measurements when rendering a human-facing report.
