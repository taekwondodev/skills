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
   - **Not significant:** every other failure, even without a check that detects it. It does not require Adversarial review.
3. Match each significant failure to evidence, including maintained verification listed in `docs/agents/delivery.md` whose covered code the change touches. Evidence counts only when it covers the condition the change introduces, such as affected inputs, ordering, interruptions, environment, or consumers. Record the relevant inputs, assumptions, bounds, and consumers. A passing check does not count if its scope misses the changed condition. A maintained check counts only while it corresponds to the current code; [formal-verification](../../formal-verification/SKILL.md#maintain-correspondence) owns that judgment.
4. Choose the cheapest means that closes each significant failure:
   - **Current evidence covers it.** Cite the evidence and its boundaries.
   - **An open property over a domain**, such as parser inputs, reachable states, or event orderings. Require a generated or exhaustive check on the real code.
   - **A runnable probe would settle the claim.** Name the probe and the result that would close it.
   - **Otherwise,** require independent Adversarial review. Name each claim to challenge and the evidence that would close it.

Skip independent Adversarial review when no failure is significant or current evidence covers every significant failure. Keep Standards and Spec review.

## Contrasting decisions

- **A wrong label that only affects the display and clears when the run ends.** Skip Adversarial review. Cite the consumer search; a missing test for approved behavior belongs to Standards.
- **A failure that needs a hand-built input or a crash at one instant, with an effect confined to the run.** Signal: constructed trigger, local effect. Skip.
- **A field changes position in a file that external tools import.** If the claim is that the named importers read by field name, run a probe with them if available. Otherwise ask an independent reviewer to inspect their parsers.
- **A permissions failure that requires a crafted request.** Treat it as significant despite the trigger. Count only evidence that covers that condition.
- **An import parser can corrupt stored records, and the claim concerns every input the parser accepts.** Require a property check, not a search for another example.
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

## Resolve pending claims

The coordinator checks the rationale, then uses the method named for each claim:

- Run the probe and record its result. If it does not settle the claim, reassess what evidence would.
- Use [verification selection](../../formal-verification/references/selection.md) to choose an adequate property check and give the implementer the property and missing evidence. If the check cannot be run or cannot establish the claim, keep the limit open.
- Give `interrogate` only the claims that require independent judgment, the evidence that would close each, the contract, and current impact and check evidence.

Keep each claim open until evidence or a user decision settles it. If a required worker cannot run, record that scope as unavailable under the [result contract](result-contract.md#coverage-and-gates). Merge independent results only for assigned claims. For the scope of this gate, record a skip with check results if checks settle every claim without an independent review.

Completion: the disposition is backed by retrievable evidence, and each remaining gap names the claim and the decision or evidence needed to close it.
