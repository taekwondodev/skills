# Closing pass

Load after the implementer has fixed the blocking findings of a unit's full review. A unit gets one full review and one closing pass. The closing pass verifies those fixes against a closed list; it is not a second review. A small change reviewed inline closes inline by the same rules.

## Assign

Give one worker:

- the closed list: every blocking finding from the full review, as returned;
- the fix diff, from the reviewed revision to the current one;
- this reference and the [result contract](result-contract.md).

Write each pass in the task record when it starts and again when its result is verified, and carry that into any handoff, so a later session continues the count instead of restarting it. Fixes for findings stay in this unit. Newly requested behavior is a new unit with its own review.

## Verify

Decide each listed finding closed or open:

- **Spec and Adversarial:** closed when the recorded case or trigger no longer produces the recorded consequence.
- **Standards:** closed when the cited rule holds on the cited hunk.

A different trigger or case is a new finding, not evidence that a listed one is open. A listed finding whose code only moved keeps its identity. Admit a new finding only on lines the fix diff changed, and only when it meets the [blocking threshold](result-contract.md#blocking-threshold). Code the full review covered and the fix left unchanged stays closed; report a problem noticed there in one limit for the user to judge.

The full review's Adversarial result stands. Apply the [risk gate](risk-gate.md) only to a condition the fix diff introduces, and return a pending disposition only when that condition is significant. An Adversarial worker dispatched for it settles that condition alone.

Return `review/1` with the axes of the listed findings. `findings` holds each listed finding still open, restated with the observation that shows its trigger still producing its consequence, and each admitted new finding. Empty findings with `complete` coverage means every listed finding is closed.

## After the pass

The closing pass, with any Adversarial worker its pending disposition required, ends the unit's review; another review needs a direct user request. The implementer fixes each finding still open and proves the fix with a check that fails before it and passes after. Take a finding that such a check cannot close to the user with one recommendation: fix further, accept it as a recorded limit, or revert the change that introduced it.

## Repeated counterexample

When a second counterexample to the property a fix is meant to establish is confirmed, whether while fixing, in the pass, or after it, stop patching cases. A counterexample below the blocking threshold is `noted` and does not count. State the property, then choose between a design that makes it hold by construction and a generated or exhaustive check on the real code, through [verification selection](../../formal-verification/references/selection.md). When neither fits, the user decides between a recorded limit and a revert.

Completion: every listed finding is closed by the pass, closed by a failing-then-passing check, or decided by the user, and the task record shows both passes verified.
