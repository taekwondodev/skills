---
name: principle-fix-root-causes
description: "Apply when debugging. Trace each symptom to its root cause and fix it there; reproduce first, ask why until you reach it, resist nil-check guards that silence crashes."
---

# Fix Root Causes

Fix the fault, not the place where it surfaced. The root cause is the first place the system did something it should not do, or failed to handle a state it should handle.

- Reproduce first. Ask "why" until the answer is a wrong decision in the code. When stuck, instrument and read the actual state.
- Ask whether the state that triggered the symptom is legitimate. If it is, handle it where the code broke. If it should never exist, a check there hides the bug, so find what produced it. Guards, retries, swallowed errors, clamped values, and discarded state are the usual ways to hide a bug.
- Fix the pattern, not the instance. Find every place with the same fault.
- If the deciding fact took a deep dig, propose the cheap, always-on signal that would have shown it at first look.

## Recheck the premise after repeated failures

When two or more fixes assume the same premise and fail the same check, test the premise before attempting another fix.

1. Write the shared premise and the failed check explicitly.
2. Identify an observation that would distinguish that premise from an alternative explanation. Use the smallest probe that can make the distinction. Compare actors or workloads only when the hypothesis concerns a difference between them.
3. Run the probe and record whether the result supports, contradicts, or leaves the premise unresolved. An inconclusive result does not rule out the premise.
4. Revise the hypothesis or the probe before the next fix. Keep product and scope changes subject to the user's decision.

Completion criterion: the premise, observation, result, and reason for the next attempt are recorded. Another implementation based on the same untested premise is not progress.
