# Decision results

Use for agent-facing candidate designs, synthesis, and resolved decision handoffs. Return JSON only unless the caller supplies a compatible contract. Human questions and approval checkpoints remain interactive.

## Shape: decision/1

Required root fields: `format` (literal `decision/1`), `status` (`complete`, `partial`, or `blocked`), `decisions` (array), and `limits` (string array). Optional `artifacts` lists objects with nonempty `role` and `ref` strings. Optional `next` contains nonempty `action` and `done_when` strings. No other fields are defined.

Each decision contains nonempty `choice` and `reason` strings and an `evidence` string array. Evidence must identify the inspected source or observation, or include the necessary context when no retrievable source exists. Optional `alternatives` lists objects with `option` and `reason` strings; include it whenever alternatives were compared. Retain the constraint or principle that actually changed the choice in the reason or its evidence.

- `complete`: the assigned decision or candidate deliverable meets its completion criterion. A completed candidate is a proposal, not approval to adopt it.
- `partial`: a required decision, approval, comparison, or artifact remains outstanding. `blocked`: prerequisites prevented useful work. Both require limits explaining what remains and how to resolve it.
- Empty decisions mean none were settled; they do not resolve open questions. Human-owned choices require actual confirmation before they are reported as settled.

Keep native sketches, signatures, module maps, and rationale files intact. Design results require locators for those deliverables in `artifacts`; they do not replace them with a summary. Record the selected base, justified grafts, and reasons for rejected candidates in the synthesis. Keep speculative options out of settled decisions.

Give each candidate worker this contract and its artifact requirements. The caller reads the artifacts, verifies evidence and independence, then consumes the decisions without requesting a second report. An unverified candidate or missing independent attempt remains a limit. `next` describes the next action and completion criterion, not permission to cross a checkpoint.

Examples use fictional sources.

```json
{"format":"decision/1","status":"complete","decisions":[{"choice":"Candidate A with B's cache isolation","reason":"Preserves the public API without shared mutable cache state.","evidence":["design/rationale.md#comparison: A preserves the call sites; B isolates cache ownership."],"alternatives":[{"option":"Candidate B unchanged","reason":"Changes the required public API."}]}],"artifacts":[{"role":"sketch","ref":"design/types.ts"},{"role":"rationale","ref":"design/rationale.md"}],"limits":[]}
```

```json
{"format":"decision/1","status":"partial","decisions":[],"limits":["Retention duration needs the user's decision."],"next":{"action":"Ask the user for the retention requirement.","done_when":"The requirement is confirmed and recorded."}}
```
