# Review results

Load before dispatching, returning, or consuming `code-review` or `interrogate` results. Return compact JSON only, without fences, narration, counts, or a duplicate report. When changing this contract, load [agent-result authoring](../../writing-for-agents/references/agent-results.md); runtime workers need only this file.

## Shape: review/1

Root fields: `format` (literal `review/1`) and `axes` (object). Axis keys are `standards`, `spec`, and `adversarial`. Workers return assigned axes only; full code-review includes all three; standalone interrogate includes only `adversarial`.

Every axis contains:

- `coverage`: `complete`, `partial`, `unavailable`, or `skipped`.
- `findings`: array of findings; empty means none supported, not necessarily reviewed.
- `limits`: string array of coverage gaps, their consequences, and what resolves them; empty means none known.

Every finding contains nonempty strings `class`, `at`, `claim`, `evidence`, and optional `action`. No other fields are defined.

- `at`: affected file and line/hunk, requirement, consumer, or artifact locator.
- `claim`: specific finding and consequence.
- `evidence`: decisive observation with retrievable anchors, including the rule for Standards or requirement for Spec. A path alone is insufficient. Inline necessary excerpts when the caller cannot retrieve them.
- `action`: required correction or verification for blockers; proposed option for judgment calls. Required for blocking classes; otherwise omit when unnecessary.

| Axis | Allowed classes | Blocking classes |
| --- | --- | --- |
| `standards` | `hard`, `smell` | `hard` |
| `spec` | `missing`, `partial`, `unrequested`, `incorrect` | all |
| `adversarial` | `act_on`, `consider`, `noted`, `dismissed` | `act_on` |

`act_on` means "act on". Smells and `consider` require human judgment, not automatic scope expansion. Retain `noted` or `dismissed` only to answer an assigned concern or prevent repeating a decision; put the reason in `evidence`.

## Coverage and gates

`complete` means assigned scope and required method were covered. Gaps require `partial`; no review performed means `unavailable`. An inline review is complete only when independence was not required. Every non-complete state requires nonempty limits.

`skipped` requires permission from the owning procedure: code-review permits skipping Spec when no approved contract exists after prerequisite handling. Inaccessible existing contracts are unavailable, not skipped. Unavailable and skipped axes have empty findings.

Blocking classes block the caller's gate. Partial or unavailable coverage requires resolution or an explicit user decision before proceeding. Permitted skips remain visible, never labeled passed. Malformed payloads, unknown versions, missing assigned axes, or unsupported evidence are incomplete results, never clean reviews. Request correction only when another model call is authorized; otherwise expose the gap.

## Consumer

1. Pin scope and revision; give workers their axes and this reference. Retain assignment metadata at the caller.
2. Check shape and inspect evidence before accepting findings. Keep unverified claims as limits. Merge by axis, deduplicating within an axis without collapsing different obligations. Preserve every decision-relevant finding.
3. Consume or return the merged payload directly. Route blocking actions to the implementer and judgment calls to the user. Rerun affected axes after fixes; retain other results only while their evidence remains valid. Render concise prose only at a human-facing boundary unless structured output was requested.

Completion: every assigned axis is represented, accepted findings are grounded, and fixes, user decisions, and coverage gaps remain distinguishable.

## Examples

Clean worker:

```json
{"format":"review/1","axes":{"standards":{"coverage":"complete","findings":[],"limits":[]}}}
```

Blocker (fictional evidence):

```json
{"format":"review/1","axes":{"spec":{"coverage":"complete","findings":[{"class":"missing","at":"src/parse.ts:18","claim":"Zero is accepted.","evidence":"spec.md#inputs requires > 0; the guard rejects only < 0.","action":"Reject zero and test the boundary."}],"limits":[]}}}
```

Missing coverage:

```json
{"format":"review/1","axes":{"adversarial":{"coverage":"unavailable","findings":[],"limits":["Independent worker unavailable; scope unreviewed. Obtain review or an explicit user decision."]}}}
```

Permitted omission:

```json
{"format":"review/1","axes":{"spec":{"coverage":"skipped","findings":[],"limits":["No approved contract exists after prerequisite handling; code-review permits skipping Spec. Supply a contract to review it."]}}}
```
