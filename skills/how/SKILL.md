---
name: how
description: Explain how a subsystem works, including flow, ownership, and boundaries.
disable-model-invocation: true
---

# How

Explain how a subsystem works well enough for a senior engineer to change it safely. Trace the real path from trigger to effect. Do not guess from filenames or produce an annotated source dump.

## When to Use

Use for:

- `how does X work?`;
- code walkthroughs before a change;
- ownership and placement questions;
- layering and dependency questions;
- runtime flow questions.

Use `why` for motivation and historical rationale. Use `architect` when the question becomes a new structural decision.

## Procedure

1. Define the scope and state the interpretation if the request is ambiguous. Do not ask when repository inspection can resolve the ambiguity.
2. Use the available repository-search and file-reading tools to find the entry point, callers, callees, types, persistence or external effects, and tests. Follow pagination or additional result pages until the relevant source is retrieved.
3. Trace the flow from input or trigger to output or effect. Follow symbols across module boundaries.
4. Record ownership, dependency direction, validation, error conversion, observability, and security boundaries.
5. When the subsystem is broad, launch independent read-only subagents in separate contexts through the available delegation capability. Keep each worker on a distinct angle and give it the evidence result contract below. Verify and merge returned findings in flow order. If delegation is unavailable, state that limitation and continue sequentially only when independent runs are not required by the request.
6. For a human-facing answer, present a concise overview, key concepts, flow, ownership, and gotchas. For an agent-facing return, use the result contract below.

## Agent result

Load [evidence/1](../investigation/references/result-contract.md) for workers and agent-facing returns. Keep the traced flow ordered and retain ownership, boundaries, and source symbols in the findings.

## Verification

Before presenting the result:

- every claimed flow step has a source file and symbol;
- callers and callees were followed across each relevant boundary;
- surprising behavior is marked as observed rather than inferred;
- open uncertainty is explicit;
- no code or project state was modified.
