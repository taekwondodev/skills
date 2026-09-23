# Measurement results

Use for agent-facing performance and hillclimb returns. Return JSON only unless the caller supplies a compatible contract. Human-facing results remain concise prose.

## Shape: measurement/1

Required fields:

- `format`: literal `measurement/1`.
- `status`: `complete`, `partial`, or `blocked`.
- `metric`: object with `name`, `unit` (strings), and `direction` (`minimize` or `maximize`).
- `workload`: reproducible workload and harness locator, or null when unavailable.
- `baseline`, `final`: observed numbers for the initial and retained states, respectively; null when unmeasured, never invented zeroes.
- `verdict`: `keep`, `revert`, or `inconclusive` for the scoped change or accumulated retained changes, not merely the last experiment.
- `regression`: `pass`, `fail`, or `unrun` for the retained state.
- `evidence`: string array locating commands, measurements, revision identities, noise analysis, and regression results with concise observations.
- `stop`: nonempty string naming the actual stopping condition and whether the target was met.
- `limits`: string array of uncertainty, missing checks, or obstacles and what resolves them.

Optional `trials` is an accessible log/report locator; required for multiple attempts or a reverted experiment. It records candidate measurements, hypotheses, checks, and keep/revert outcomes without repeating the log in the response. Optional `ideas` is a string array of remaining hypotheses. No other fields are defined.

`complete` means the scoped experiment or search ended at its declared stop criterion, not that performance improved. `partial` means required measurements or checks remain; `blocked` means the workload could not be exercised. Non-complete results require limits. `keep` requires comparable measurements, improvement beyond noise, and a passing regression gate. A failed or unrun required check cannot establish success.

The caller checks evidence and the retained revision, derives deltas from the recorded values, and consumes the verdict without another report. A reverted candidate's measurement is not the final retained result. Preserve unsuccessful attempts in the trial log. No verdict authorizes further iterations or scope changes beyond the owning procedure.

Examples use fictional measurements and sources.

```json
{"format":"measurement/1","status":"complete","metric":{"name":"request latency p95","unit":"ms","direction":"minimize"},"workload":"bench/request.json","baseline":100,"final":80,"verdict":"keep","regression":"pass","evidence":["bench/result.json: matching workload; retained revision measured beyond the reported noise interval; regression suite passed."],"stop":"The scoped optimization and regression check finished.","limits":[]}
```

```json
{"format":"measurement/1","status":"blocked","metric":{"name":"request latency p95","unit":"ms","direction":"minimize"},"workload":null,"baseline":null,"final":null,"verdict":"inconclusive","regression":"unrun","evidence":[],"stop":"Required workload unavailable; target not evaluated.","limits":["Obtain the representative workload before measuring."]}
```
