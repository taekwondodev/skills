# Agent results

Use this reference when designing a result consumed by another skill or agent. Runtime workers load only their selected result contract. It governs the response, not the format of the underlying deliverable: a requested spec, patch, or diagram stays in its native format.

## Consumer boundary

- Agent-facing calls return only the contracted payload. Human-facing calls render a concise answer unless the user requests structured output. A worker returning to a coordinator is agent-facing even when the original request came from a human.
- Inline skill loading shares context. Produce an intermediate payload only when another procedure needs a result to consume or retain, not as a running commentary.
- The producing skill's result reference defines the default shape. An explicit caller contract may replace the serialization, but must preserve required evidence, coverage, and decision gates. Report incompatible requirements rather than dropping mandatory information.

## Compactness

- Use JSON by default, with short meaningful keys, documented enums, and only the fields the consumer needs. Return one JSON value without fences or surrounding prose. Minification is optional; opaque encodings and positional shorthand need demonstrated benefit before adoption.
- Carry decisions, actionable findings, evidence anchors, unresolved limits, and required next actions. State each fact once. Derive counts and summaries at the consumer instead of returning them alongside the source data.
- Preserve every decision-relevant finding. Omit process narration, repeated task context, ceremonial sections, and empty optional fields. Keep required empty collections when they distinguish a checked absence from missing work.
- Link bulky evidence through a path or URL the receiving worker can access, with the necessary locator and concise observation inline. If access is unavailable, carry the necessary excerpt. A pointer alone is not evidence; a shorter answer is not permission to truncate blockers or hide uncertainty.

## Contract ownership

Keep the result shape in one reference beside its producing skill; dispatchers and consumers load that same reference. A worker must receive the reference path or its contents in its own context. Do not preload unrelated result families or create a universal envelope full of unused fields.

Each result reference defines:

1. Field types, allowed values, required versus optional fields, and a format version when several consumers share the shape.
2. Completion, incomplete or unavailable work, and the meaning of empty or omitted values.
3. How the caller validates, merges, and acts on the result, including user-owned decisions.
4. Minimal examples for a clean result and important failure or incomplete states.

Add a machine schema when a program consumes the response; keep field definitions there instead of maintaining a second prose schema. A template alone is insufficient when its omissions have no defined meaning.

## Acceptance

Before adoption, check that the caller can choose the next action from the payload, retrieve its evidence, and distinguish clean completion from unperformed work. Parse JSON examples and check links locally. Claim model adherence or token savings only when those properties were actually measured; include reference-loading costs when comparing token usage.
