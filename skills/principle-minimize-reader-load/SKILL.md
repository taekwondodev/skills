---
name: principle-minimize-reader-load
description: "Apply when shaping or reviewing code for readability, comments, or unnecessary complexity."
---

# Minimize Reader Load

Reader load is the work a reader must do to understand code. It has two independent axes: layers to trace between the question and the answer, and hidden or mutable state to hold in their head. Guard both. Decompose by domain responsibility, not merely to satisfy a complexity threshold.

- Write comment-free code: express intent through names, types, and structure. Keep decision rationale in documentation. Required tool directives and legal notices are exempt.
- Collapse layers that only forward: wrappers with one caller, adapters with no second implementation, pass-through methods. Inline them.
- Shrink state scope: returns over mutations, locals over fields, fields over module state, module state over globals. Derive instead of sync.
- Name an invariant once at the boundary, not in every consumer.

The test: can a new reader answer "where does X come from?" and "what can change X?" in under 30 seconds? If not, cut layers or cut state.
