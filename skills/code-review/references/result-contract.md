# Review results

Load before dispatching, returning, or consuming `code-review` or `interrogate` results. Return compact JSON only, without fences, narration, counts, or a duplicate report.

## Shape: review/1

Root fields: `format` (literal `review/1`) and `axes` (object). Axis keys are `standards`, `spec`, and `adversarial`. Workers return assigned axes only; full code-review includes all three; standalone interrogate includes only `adversarial`. The semantic reviewer also returns the risk gate's `adversarial` disposition as defined below.

Every axis contains:

- `coverage`: `complete`, `partial`, `unavailable`, or `skipped`.
- `findings`: array of findings; empty means none supported, not necessarily reviewed.
- `limits`: string array. Record coverage gaps, their consequences, and what resolves them. Record the rationale, evidence, and boundaries for skips. A closing pass can also record a nonblocking note here. An empty array means there are no known limits.

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

The implementer resolves each smell without the user: apply its action within the reviewed scope, or dismiss it when [Style Serves Outcomes](../../principle-style-serves-outcomes/SKILL.md) rejects the action. Record dismissals through [Implement's agent result](../../implement/SKILL.md#agent-result). A smell whose action would change scope, a public contract, or security goes to the user. An action that encodes a rule in an already-configured tool is within the reviewed scope: add the rule, show that it fails on the violating hunk and passes after the fix, and fix the existing violations it reports, using the tool's autofix where available. Installing a new tool or dependency, and existing violations outside the reviewed scope that the tool cannot autofix, go to the user. `consider` requires human judgment, not automatic scope expansion. Use `dismissed` only to answer an assigned concern or prevent repeating a decision; put the reason in `evidence`.

## Blocking threshold

A finding takes a blocking class only when it meets its axis threshold.

- **Adversarial:** `act_on` states the trigger, an input or sequence starting from a real entry point, and a consequence the [risk gate](risk-gate.md#decide) sorts as significant, and shows the failure through a run (a failing test, repro script, or command output) or a cited source location that contains the defect. A significant failure supported only by reasoning is at most `consider`. Record a concrete failure below that threshold as `noted`, with each field one sentence and no action.
- **Spec:** cite a written requirement or scope limit in the approved contract and show how the change violates it. Use a case the contract names or that normal use reaches. Send constructed cases outside the contract to the risk gate as candidate failures. Apply general quality rules under Standards.

## Coverage and gates

`complete` means assigned scope and required method were covered. `partial` means assigned scope was left unread or an assigned claim was left open; a probe outside the assignment that was not run is not a gap. No review performed means `unavailable`. An inline review is complete only when independence was not required. Every non-complete state requires nonempty limits.

`skipped` requires permission from [code-review](../SKILL.md#1-pin-the-inputs) for Spec or the [risk gate](risk-gate.md#decide) for Adversarial. An inaccessible existing contract is `unavailable`, not `skipped`. Unavailable and skipped axes have empty findings.

A [pending risk-gate disposition](risk-gate.md#return) uses `partial` to record work still needed, not completed Adversarial review. Distinguish it from a review result by the retained assignment role and follow the gate's [resolution procedure](risk-gate.md#resolve-pending-claims).

Blocking classes block the caller's gate. Partial or unavailable coverage requires resolution or an explicit user decision before proceeding. Permitted skips remain visible, never labeled passed. Malformed payloads, unknown versions, missing assigned axes, or unsupported evidence are incomplete results, never clean reviews.

## Consumer

1. Pin scope and revision; give workers their axes and this reference. Retain assignment metadata at the caller.
2. Check shape and inspect evidence before accepting findings. Merge by axis and deduplicate without collapsing different obligations. Keep open claims as limits alongside supported findings. When combining scopes on one axis, a scoped skip does not replace other coverage or findings. If a required part was not reviewed but another part was, report `partial` and name the gap.
3. Retain results only while the contract and supporting evidence still apply. For review fixes, follow the [closing procedure](closing-pass.md).
4. Consume or return the merged payload directly. Route blocking actions and smells to the implementer, and remaining judgment calls to the user. Render concise prose only at a human-facing boundary unless structured output was requested.

Completion: every assigned axis is represented, accepted findings are grounded, and fixes, user decisions, and coverage gaps remain distinguishable.

## Examples

Clean worker:

```json
{"format":"review/1","axes":{"standards":{"coverage":"complete","findings":[],"limits":[]}}}
```

Blocker (fictional evidence):

```json
{"format":"review/1","axes":{"spec":{"coverage":"complete","findings":[{"class":"incorrect","at":"src/parse.ts:18","claim":"Zero is accepted.","evidence":"spec.md#inputs requires > 0; the guard rejects only < 0.","action":"Reject zero and test the boundary."}],"limits":[]}}}
```

Missing coverage:

```json
{"format":"review/1","axes":{"adversarial":{"coverage":"unavailable","findings":[],"limits":["Independent worker unavailable; scope unreviewed. Obtain review or an explicit user decision."]}}}
```

Risk-gate skip (fictional evidence):

```json
{"format":"review/1","axes":{"adversarial":{"coverage":"skipped","findings":[],"limits":["Self-assessed inline gate; independent review not required. Checked HEAD head456 plus ui/title.ts:8 replacement of Workspace with Project, the entire dirty diff from head456. Inspected callers use a separate stable identifier; render check confirms the new text. This covers the label, not unrelated UI behavior."]}}}
```

Pending independent assignment (fictional evidence):

```json
{"format":"review/1","axes":{"adversarial":{"coverage":"partial","findings":[],"limits":["export.ts:42 reorders the fields of the file every export writes; the file persists and tools outside the repository import it. No current check reads an exported file through an importer. Claim to challenge: each importer listed in docs/consumers.md reads fields by name, not position. Closed by reading each importer's parser."]}}}
```

Permitted omission:

```json
{"format":"review/1","axes":{"spec":{"coverage":"skipped","findings":[],"limits":["No approved contract exists after prerequisite handling; code-review permits skipping Spec. Supply a contract to review it."]}}}
```
