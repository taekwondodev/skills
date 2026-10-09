---
name: perf-issue
description: Diagnose and improve one measured performance problem.
---

# Performance Issue

Handle one measured performance problem with a realistic workload and a before-and-after comparison. A sustained search against a target belongs to `hillclimb`.

## Procedure

1. Use `how` to ground the affected path and workload dimensions. Consume its evidence result directly and retain the sources needed for measurement.
2. Establish a reproducible baseline and a regression gate.
3. Profile or measure the matching surface.
4. Form one mechanism-based hypothesis from the measurement using the [performance mantras](#performance-mantras).
5. If the fix crosses a function boundary or changes a data shape, use `architect` before implementation and consume its design sketch.
6. Apply the smallest change that tests the hypothesis.
7. Measure before and after with the same harness.
8. Keep the change only when the improvement clears measurement noise and the regression gate stays green. Verify each attempt before trying the next mantra; stop when an earlier mantra meets the target and passes this gate.

## Performance mantras

Try applicable categories in order, cheapest first:

1. Don't do it. Stop work whose result nothing uses rather than cheapening it.
2. Do it, but don't do it again.
3. Do it less.
4. Do it later.
5. Do it when they're not looking.
6. Do it concurrently.
7. Do it cheaper.

## Agent result

For an agent-facing return, load [measurement/1](references/result-contract.md). Preserve the workload, retained-state measurements, regression evidence, and keep/revert verdict.

## Verification

The baseline, workload, metric, measurement command, before value, after value, and regression result are recorded. No claim rests on code inspection alone.
