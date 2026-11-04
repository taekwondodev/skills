# Review results

Load before dispatching, returning, or consuming `code-review` or `interrogate` results. Return compact JSON only, without fences, narration, counts, or a duplicate report.

## Shape: review/1

Root fields: `format` (literal `review/1`) and `axes` (object). Axis keys are `standards`, `spec`, and `adversarial`. Workers return assigned axes only; full code-review includes all three; standalone interrogate includes only `adversarial`. The semantic reviewer also returns the risk gate's `adversarial` disposition as defined below.

Every axis contains:

- `coverage`: `complete`, `partial`, `unavailable`, or `skipped`.
- `findings`: array of findings; empty means none supported, not necessarily reviewed.
- `limits`: string array of coverage gaps, their consequences, and what resolves them; for permitted skips, the permission, rationale, evidence, and boundaries. Empty means none known.

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

`act_on` means "act on". The implementer resolves each smell without the user: apply its action within the reviewed scope, or dismiss it when [Style Serves Outcomes](../../principle-style-serves-outcomes/SKILL.md) rejects the action. Record dismissals through [Implement's agent result](../../implement/SKILL.md#agent-result). A smell whose action would change scope, a public contract, or security goes to the user. An action that encodes a rule in an already-configured tool is within the reviewed scope: add the rule, show that it fails on the violating hunk and passes after the fix, and fix the existing violations it reports, using the tool's autofix where available. Installing a new tool or dependency, and existing violations outside the reviewed scope that the tool cannot autofix, go to the user. `consider` requires human judgment, not automatic scope expansion. Retain `noted` or `dismissed` only to answer an assigned concern or prevent repeating a decision; put the reason in `evidence`.

## Coverage and gates

`complete` means assigned scope and required method were covered. Gaps require `partial`; no review performed means `unavailable`. An inline review is complete only when independence was not required. Every non-complete state requires nonempty limits.

`skipped` requires permission from the owning procedure: code-review permits skipping Spec when no approved contract exists after prerequisite handling, and Adversarial when its [risk gate](risk-gate.md) finds no significant uncovered or uncertain risk. Inaccessible existing contracts are unavailable, not skipped. Unavailable and skipped axes have empty findings.

For the risk gate, the semantic reviewer returns `adversarial` with empty findings and either `skipped` with the decision's evidence and boundaries in `limits`, or `partial` with the risks requiring independent review in `limits`. A skip identifies its assessor and checked revision, includes a diff or content identity for uncommitted changes, and explicitly says self-assessed when inline. This `partial` disposition, including an undecidable gate caused by missing evidence, is a pending assignment, not completed Adversarial review. Distinguish it by the caller's retained assignment role. The coordinator verifies the rationale and replaces it with the required worker's result. If that worker cannot run, report `unavailable`. Only a reviewer assigned the Adversarial review itself can return `complete`.

Blocking classes block the caller's gate. Partial or unavailable coverage requires resolution or an explicit user decision before proceeding. Permitted skips remain visible, never labeled passed. Malformed payloads, unknown versions, missing assigned axes, or unsupported evidence are incomplete results, never clean reviews.

## Consumer

1. Pin scope and revision; give workers their axes and this reference. Retain assignment metadata at the caller.
2. Check shape and inspect evidence before accepting findings. Keep unverified claims as limits. Merge by axis, deduplicating within an axis without collapsing different obligations. Preserve every decision-relevant finding.
3. Recheck a risk-gate skip when the diff, contract, or supporting evidence changes. A previous skip does not cover new risks.
4. Consume or return the merged payload directly. Route blocking actions and smells to the implementer, and remaining judgment calls to the user. Rerun affected axes after fixes; retain other results only while their evidence remains valid. Render concise prose only at a human-facing boundary unless structured output was requested.

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

Risk-gate skip (fictional evidence):

```json
{"format":"review/1","axes":{"adversarial":{"coverage":"skipped","findings":[],"limits":["Self-assessed inline gate; independent review not required. Checked HEAD head456 plus ui/title.ts:8 replacement of Workspace with Project, the entire dirty diff from head456. Inspected callers use a separate stable identifier; render check confirms the new text. This covers the label, not unrelated UI behavior."]}}}
```

Pending independent assignment (fictional evidence):

```json
{"format":"review/1","axes":{"adversarial":{"coverage":"partial","findings":[],"limits":["lease.ts:42 adds a writer absent from Lease.tla. The recorded model pass does not cover current ownership. Independently inspect overlapping acquisition and replay any violating sequence against the implementation."]}}}
```

Permitted omission:

```json
{"format":"review/1","axes":{"spec":{"coverage":"skipped","findings":[],"limits":["No approved contract exists after prerequisite handling; code-review permits skipping Spec. Supply a contract to review it."]}}}
```
