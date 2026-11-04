# Residual-risk gate

The semantic reviewer decides whether independent Adversarial review is needed after inspecting the diff, contract, consumers, and current check evidence. Each decision rests on the signals below: what a failure would cause and what current evidence covers. Read the contrasting decisions when a signal alone does not settle it. A direct request for adversarial review requires that review.

## Decide

1. List the plausible failures the changed behavior could cause, including in consumers of what changed. For each, read the consequence signals:
   - **Reach:** who observes the wrong result: only the changed unit, other code in the repository, or users, stored data, and systems outside it.
   - **Persistence:** whether the wrong result outlives the run that produced it.
   - **Reversibility:** whether correcting the code undoes the effect, or the effect itself needs repair.
   - **Detection:** whether current checks or normal use would expose the failure before it causes harm.
2. Match each failure to evidence, including maintained verification listed in `docs/agents/delivery.md` whose covered code the change touches. Evidence counts only when it exercises the condition the change introduces: the inputs, ordering, failures or interruptions, environment, or consumers it affects. Record the relevant inputs, assumptions, bounds, and consumers. A check that passes without exercising that condition covers nothing about it. A maintained check counts only while it corresponds to the current code; [formal-verification](../../formal-verification/SKILL.md#maintain-correspondence) owns that judgment.
3. A failure is significant unless its reach is limited, it is reversible, and it is detectable. Require independent Adversarial review for a significant failure without adequate evidence, or whose consequences cannot be established. Name the claims and missing evidence in the pending disposition. Permit a skip only when each significant failure has adequate current evidence. Cite the concrete evidence and its boundaries.

A skip saves a worker, not the assessment. Keep Standards and Spec review.

## Contrasting decisions

- **Changed output with no consumer beyond its display, and a check on the new output.** Signal: limited reach, nothing persisted, immediately visible. Skip with the consumer search and check as evidence.
- **Changed behavior whose passing checks never reach the condition the change introduces.** Signal: the evidence does not exercise the new condition, however small the diff. Dispatch, naming the unexercised condition.
- **A result other systems or stored data depend on, with no evidence about those consumers.** Signal: reach outside the repository, effect outlives the run. Dispatch unless consumer evidence covers it.
- **A large change with pinned-behavior evidence across its consumers.** Signal: wide diff, but equivalence shown on the affected inputs. Skip can be justified.
- **A passing proof that describes an earlier version of the code.** Signal: evidence exists but no longer corresponds. Treat as uncertain until correspondence or replacement evidence is established.

## Signals that do not decide

- The size of the diff, in either direction.
- The subject area of the change, or how important it feels.
- A check, tool, or model existing, without evidence that it exercises the changed condition.
- Reviewer confidence that cites no inspected evidence.

## Return

Return the `review/1` Adversarial axis alongside the semantic axes:

- **Skip:** `coverage: skipped`, empty findings, and limits stating who assessed the gate, why no independent pass is required, the checked revision plus a diff or content identity for any uncommitted changes, supporting evidence, and what remains outside it. An inline skip explicitly says it is self-assessed, not independent.
- **Dispatch:** `coverage: partial`, empty findings, and limits naming the residual risks and required independent investigation. If missing or inaccessible evidence prevents a decision, use this disposition and name the evidence gap; uncertainty never permits a skip. Keep semantic findings on their own axes.

Completion: the coordinator can either justify the skip from retrievable evidence or dispatch a bounded independent assignment.
