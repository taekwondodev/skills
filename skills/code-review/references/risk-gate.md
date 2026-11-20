# Residual-risk gate

The semantic reviewer decides whether independent Adversarial review is needed after inspecting the diff, contract, consumers, and current check evidence. Each decision rests on the signals below: how a failure is reached, what it would cause, and what current evidence covers. Read the contrasting decisions when a signal alone does not settle it. A direct request for adversarial review requires that review.

## Decide

1. List the failures the change could cause, including in consumers of what changed. Each listed failure names a changed line and a trigger: the input or sequence, starting from a real entry point, that produces it. For each, read the signals:
   - **Trigger:** whether normal use reaches the failure, or only a constructed input, a crash or interruption at one precise moment, or an attacker.
   - **Reach:** who observes the wrong result: only the changed unit, other code in the repository, or users, stored data, and systems outside it.
   - **Persistence:** whether the wrong result outlives the run that produced it.
   - **Reversibility:** whether correcting the code undoes the effect, or the effect itself needs repair.
   - **Detection:** whether current checks or normal use would expose the failure before it causes harm.
2. Sort each failure:
   - **Significant:** normal use reaches it, and its effect reaches stored data or systems outside the repository, outlives the run, or needs repair beyond correcting the code. A security breach or irreversible data loss is significant under any trigger.
   - **Local:** every other failure, whatever its detection, including a wrong result that a person only sees and that ends with the run. It needs no Adversarial review; the unit's ordinary tests are its cover.
3. Match each significant failure to evidence, including maintained verification listed in `docs/agents/delivery.md` whose covered code the change touches. Evidence counts only when it exercises the condition the change introduces: the inputs, ordering, failures or interruptions, environment, or consumers it affects. Record the relevant inputs, assumptions, bounds, and consumers. A check that passes without exercising that condition covers nothing about it. A maintained check counts only while it corresponds to the current code; [formal-verification](../../formal-verification/SKILL.md#maintain-correspondence) owns that judgment.
4. Choose the cheapest means that closes each significant failure:
   - **Current evidence covers it.** Cite the evidence and its boundaries.
   - **A runnable probe would settle it.** Name the probe and the outcome that permits a skip. The coordinator runs it.
   - **It is a property over a domain, not a named case:** every input a parser or matcher accepts, every state of a state machine, every ordering of events. Name the property and require a generated or exhaustive check on the real code, chosen through [verification selection](../../formal-verification/references/selection.md). Reading for further counterexamples does not establish such a property.
   - **Otherwise,** require independent Adversarial review. Name each claim to challenge and the evidence that would close it.

Permit a skip when no failure is significant, or when current evidence covers each significant one. A skip saves a worker, not the assessment. Keep Standards and Spec review.

## Contrasting decisions

- **Changed output with no consumer beyond its display, and a check on the new output.** Signal: nothing persisted, immediately visible. Skip with the consumer search and check as evidence.
- **A failure that needs a hand-built input or a crash at one instant, with an effect confined to the run.** Signal: constructed trigger, local effect. Skip.
- **A defect normal use reaches, that correcting the code undoes, with no check on it.** Signal: local, whatever its detection. Skip. A missing test for approved behavior belongs to Standards.
- **A significant failure whose passing checks never reach the condition the change introduces.** Signal: the evidence does not exercise the new condition, however small the diff. Name a probe that reaches it, or dispatch.
- **A result other systems or stored data depend on, with no evidence about those consumers.** Signal: reach outside the repository, effect outlives the run. Dispatch unless consumer evidence covers it.
- **A permission check that only a crafted request bypasses.** Signal: security, significant under any trigger. Dispatch unless evidence exercises the crafted request.
- **A matcher that must reject everything outside its grammar, after review produced one counterexample.** Signal: a property over a domain. Require the generated or exhaustive check.
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
- **Pending:** `coverage: partial`, empty findings, and one limit per significant failure that current evidence leaves open: its trigger and consequence, the claim to challenge, and the probe, property check, or independent investigation that closes it. If missing or inaccessible evidence prevents a decision about a significant failure, use this disposition and name the gap; that uncertainty never permits a skip. Keep semantic findings on their own axes.

Completion: the coordinator can justify the skip from retrievable evidence, or can run each named probe, route each named property check, and dispatch a bounded assignment whose claims each name their closing evidence.
