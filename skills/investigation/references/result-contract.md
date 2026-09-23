# Evidence results

Use for agent-facing investigation, explanation, research, impact analysis, and prototype returns. Return JSON only. An explicit compatible caller contract takes precedence. Human-facing answers remain concise prose.

## Shape: evidence/1

Required root fields: `format` (literal `evidence/1`), `status` (`complete`, `partial`, or `blocked`), `findings` (array), and `limits` (string array).

Each finding has `kind` (`fact`, `inference`, `hypothesis`, or `rejected`), `claim` (nonempty string), and `evidence` (string array of source locators with the decisive observations). Optional `next` is a focused follow-up check. No other fields are defined.

- `fact` records an inspected source or observation; `inference` states the reasoning connecting its sources. Both require evidence.
- `hypothesis` is unproven. Evidence may be empty; state the missing observation in `next` or `limits`.
- `rejected` requires refuting evidence. Include rejected hypotheses only when their disposition affects the decision or avoids repeated work.
- `complete` means the assigned scope was examined, not that every hypothesis became fact. `partial` means required coverage is missing; `blocked` means meaningful investigation could not proceed. Non-complete results require limits explaining the gap and how to resolve it. Empty findings alone never establish safety or absence.

Keep observations and uncertainty with their evidence. Link large sources through accessible locators; include necessary excerpts when the receiver lacks access.

Before delegation, give workers this contract and their bounded questions. The caller verifies sources, merges distinct findings, and updates its decision or risk record directly. Preserve unresolved claims and coverage gaps; a result neither authorizes changes nor resolves user-owned choices.

Examples use fictional sources.

```json
{"format":"evidence/1","status":"complete","findings":[{"kind":"fact","claim":"The caller retries once.","evidence":["src/client.py:42-48: the retry loop has two total attempts."]}],"limits":[]}
```

```json
{"format":"evidence/1","status":"partial","findings":[{"kind":"hypothesis","claim":"A retained subscription may explain the leak.","evidence":[],"next":"Capture the retaining path."}],"limits":["Heap capture unavailable; the retaining mechanism remains unproven."]}
```
