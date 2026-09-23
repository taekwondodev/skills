# Delivery results

Use for agent-facing artifact, publication, implementation, and continuity returns. Return JSON only unless the caller supplies a compatible contract. Keep specs, tickets, code, diagrams, handoffs, logs, and reports in their native format. Human-facing completion messages remain concise prose.

## Shape: delivery/1

Required root fields: `format` (literal `delivery/1`), `status` (`complete`, `partial`, or `blocked`), `artifacts` (array), `checks` (array), and `limits` (string array). Optional `outcome` explains a meaningful no-op or disposition not conveyed by the artifacts; it is required for a complete result with no artifacts. Optional `next` contains nonempty `action` and `done_when` strings; require it at a continuity boundary. No other fields are defined.

Each artifact has nonempty `role` and `ref` strings. The reference is a retrievable path, URL, or revision with enough repository/worktree context to locate it. For ticket readiness, include optional `blocked_by`: an array of verified unresolved blocker references. Empty means none observed; omitted means not queried or not applicable. Readiness does not authorize dispatch or implementation.

Each check has a nonempty `check` name, `outcome` (`pass`, `fail`, `unrun`, or `skipped`), and an `evidence` string array. Passed or failed checks require an observed result and retrievable source or command. Skips require the applicable permission and reason. Required unrun checks must be represented explicitly, not hidden in an empty array.

`status` describes the assigned work under the owning skill's completion criterion, not approval of everything delivered. A completed evaluation may report failing gates. Missing required work makes the result partial; inability to proceed makes it blocked. Both require limits explaining the gap and what resolves it. Empty checks mean no checks are reported, never that all gates passed.

Verify written artifacts and read back exact external targets before reporting them. List partial outputs even when the operation did not finish. An artifact receipt is not proof of its contents: the caller retrieves what the next step depends on, checks evidence, and preserves failures, missing coverage, and human decisions. Consume or forward the receipt without copying the artifact or producing a second report. A result or `next` action never grants permission to publish, execute, or cross a phase checkpoint.

Examples use fictional artifacts and observations.

```json
{"format":"delivery/1","status":"complete","artifacts":[{"role":"handoff","ref":"HANDOFF.md"}],"checks":[{"check":"handoff contents","outcome":"pass","evidence":["HANDOFF.md: pending work and the verified repository state are recorded."]}],"limits":[],"next":{"action":"Resume the recorded parser fix.","done_when":"The pending regression passes on the corrected parser."}}
```

```json
{"format":"delivery/1","status":"partial","artifacts":[{"role":"patch","ref":"src/parser.py"}],"checks":[{"check":"regression suite","outcome":"unrun","evidence":[]}],"limits":["Required test dependency unavailable; restore it and run the suite before claiming completion."]}
```

```json
{"format":"delivery/1","status":"complete","artifacts":[],"checks":[],"limits":[],"outcome":"The approved spec contains one independent slice; no decomposition was needed."}
```
