# Closing pass

Each unit gets one full review and, if fixes change the reviewed artifact, one closing pass. The pass checks the full review's blocking findings and the fix diff. A unit reviewed inline closes inline. Fixes stay in the same unit; newly requested behavior starts a new unit.

## Assign

Record the unit, the reviewed revision and any uncommitted changes, and when each pass starts and is verified. Carry that record into handoffs so a later session resumes rather than restarts a pass.

Give the closing reviewer the original blocking findings, the diff from the reviewed snapshot to the fixed snapshot, and this reference and the [result contract](result-contract.md).

## Verify

Decide each listed finding closed or open:

- **Spec and Adversarial:** closed when the recorded case or trigger no longer produces the recorded consequence.
- **Standards:** closed when the cited rule holds on the cited hunk.

A different trigger or case is a new finding. Moving the affected code does not close the original finding. Admit a new finding only on lines the fix changed and only if it meets the [blocking threshold](result-contract.md#blocking-threshold). Note a new issue in unchanged, already reviewed code as a nonblocking limit for the user.

Run the [risk gate](risk-gate.md) only for conditions the fixes introduce. Resolve its [pending claims](risk-gate.md#resolve-pending-claims) within this pass. Report any invalidated prior coverage as a gap.

Return `review/1` for the axes checked. Report open findings with current evidence and omit closed findings. Merge the gate's disposition under the [result contract](result-contract.md#consumer).

## After the pass

Once the closing pass ends, another review of the unit needs a direct user request. Prove any later fix with a check that fails before it and passes after. If that evidence cannot close a finding, show the user what remains and recommend one action: fix further, accept the limit, or revert the change.

For delivery, retain the review record, any checks run after the pass, and user decisions. Match that evidence to the final diff and flag gaps before claiming readiness.

## Repeated counterexample

At any stage, stop fixing individual cases when a second blocking counterexample to the same property is confirmed. State the property and use [verification selection](../../formal-verification/references/selection.md) to choose evidence for a design that enforces it or a generated or exhaustive check on the real code. If you add the check, retain confirmed counterexamples as named regressions. If neither approach is adequate, ask the user to accept the limit or revert.

Completion: each blocker is closed by verified evidence or decided by the user, and the task record identifies the passes that ran and the final revision they and any later checks cover.
