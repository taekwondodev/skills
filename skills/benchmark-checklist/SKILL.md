---
name: benchmark-checklist
description: "Apply when running a benchmark or reporting a measured speedup or regression, including performance comparisons between libraries or configurations."
---

# Benchmark Checklist

Vet a performance measurement before reporting or acting on it. Answer the checks with evidence from runs, not guesses from source. Reuse current evidence for unchanged conditions; recheck what an experiment invalidates.

For a quick ballpark the user requested, one run is enough. Check output correctness and that the work happened (checks 4 and 7), label it a single-run estimate, and name the unchecked conditions. Run the remaining checks if the result looks wrong. Choosing between options is not a ballpark.

## Prepare the measurement

- Write the claim you expect to make, including the metric and workload: "export latency is 30% lower at p50 on the 60k-row dataset."
- Read the measurement script. Identify what it times, counts, and ignores.
- Check CPU capacity and system load with tools available on the platform. Identify contention without disturbing unrelated workloads. If it remains, interleave the alternatives and disclose the conditions.

Completion: the claim, timed region, workload, and relevant execution conditions are recorded.

## Check the number

1. **Why not double?** Identify the limiting resource or code path from a profile or system counters, then map it to source. Keep instrumented diagnostic runs separate from reported timings because instrumentation adds overhead. Check the load generator too: if it saturates first, that is what the result measures. Find the limiter before treating an unchanged number as evidence that a change is useless.
2. **Was it tuned?** Run each alternative in a production-equivalent configuration: release builds, flags, batching, transactions, connection pools, and realistic warm or cold caches. Pin versions and use the same data. A debug build, missing index, or transaction per row may measure configuration rather than implementation. Tune that side and rerun before selecting a winner. If tuning is unavailable, keep the comparison inconclusive; narrowing the claim to today's defaults does not justify an adoption decision.
3. **Did it break limits?** Compare throughput with resource capacity and time saved with the cost of the changed component. With other work unchanged, removing a component that takes 10% of elapsed time saves at most 10% of that time, about an 11% speedup. A result beyond the bound may measure a cache, no-op, or bug instead of the claimed work.
4. **Did it error?** Count failures and non-success responses. Check output correctness, not just presence. Rejections can be fast; retries and timeouts can be slow. Add error counts when the measurement script omits them.
5. **Does it reproduce?** Run each alternative at least five times, alternating them so warmup, initialization, caches, and drift favor neither. Report the median and range. A gap not distinguishable from run-to-run variation is no measurable difference. For a close comparison, use the harness's statistical analysis or an appropriate rank-sum test.
6. **Does it matter?** Alongside a microbenchmark, measure the end-to-end path with realistic data and concurrency. Report the component's share of the total. Removing work that takes 1% of elapsed time saves at most 1% of that time when other work is unchanged.
7. **Did it happen?** Verify that the intended work ran inside the timed region and its result was consumed: requests reached the server, rows were written, or bytes were read. Unconsumed generators, unawaited promises, discarded results, and timeouts can produce numbers for work that never happened.

Completion: every applicable check has run evidence or an explicit gap. Required correctness and work-execution checks cannot be replaced by a timing result.

## Record the verdict

- For a comparison, lead with faster, slower, no measurable difference, or inconclusive. For a standalone measurement, state what it establishes and its limits.
- Retain the value and unit, workload, run count, spread, measured limiter, and evidence locator. A requested ballpark retains its single-run label and unchecked conditions instead of implying this full coverage.
- A comparison is inconclusive if the limiter is unknown, an alternative is untuned, or a required check fails or is incomplete. State what observation would resolve it.
- Keep bulky run evidence in a linked artifact or notes file. The active delivery procedure owns how that evidence appears in a PR or other publication.

Completion: the verdict follows from the recorded checks; unchecked conditions are not presented as verified.

## Agent result

For an agent-facing measurement audit, load [evidence/1](../investigation/references/result-contract.md). Return the verdict and supporting measurements as findings, with unresolved checks in limits. If the caller supplies a compatible phase result contract, preserve this evidence there rather than producing a second report.
