---
name: eval
description: Evaluate skill routing and behavior against a fixed scenario matrix.
disable-model-invocation: true
---

# Eval

Test whether a skill, router, or workflow change produces the intended agent behavior. Compare against a fixed scenario matrix rather than relying on one successful transcript.

## Procedure

1. Define scenarios, expected route, applicable principles, required gates, and completion criteria.
2. Run the same scenarios against the baseline and the candidate behavior where possible.
3. Record selected skills, questions, decisions, tool actions, verification, and failures.
4. Check source-of-truth boundaries and unwanted scope or ceremony.
5. Report regressions, improvements, and unresolved cases. Do not silently promote a candidate based on one example.

## Script idempotency

Verification scripts must be resumable and idempotent. Save completed observations and reuse them by default when the scenario, policy, runner, execution configuration, and repetition match. Across invocations, execute only missing work and reconcile partial state without duplicating observations. Publish a final gate result only when all required observations are complete.

Provide an explicit fresh-start option to begin a separate evaluation without reusing saved observations.

## Select the gate

Run the existing structural checks and relevant runner tests for changed skill contracts. Read [the evaluation contracts](references/contracts.md) when choosing or running a model-backed gate; load only the selected scenario inputs into each worker.

| Question | Gate |
|---|---|
| Do workflow text, skill names, and references satisfy the approved contract? | `scripts/validate_dev_cycle.py` |
| Does the model select the current-phase procedure and preserve the next user-owned gate? | `scripts/run_dev_cycle_behavior.py` |
| Do bounded reviewers and investigators classify supported claims correctly? | `scripts/run_subagent_behavior.py` |
| Do coding-policy decisions match the approved cases? | `scripts/run_coding_standards_behavior.py` |
| Do workers actually execute the required tools and produce artifacts? | `scripts/run_tool_use_behavior.py` |

For the structural gate, run `python3 skills/eval/scripts/validate_dev_cycle.py --baseline-ref HEAD` from the repository root. A routing prediction is not evidence of tool execution or context placement. For a load-distribution change, inspect returned bodies, dedup stubs, reload boundaries, and parent versus worker contexts in representative traces.

Keep verification proportional to the changed behavior and agreed risk. Use model-backed gates when the changed behavior is materially uncertain or the user requests that confidence level.

## Verification

Report the contract and policy versions, executed checks, actual observations, and unresolved failures. Distinguish structural, routing, and execution evidence. A skipped model gate is unrun, not passed; an unchanged-policy alias is not a second independent observation. Promote only on evidence appropriate to the agreed risk.
