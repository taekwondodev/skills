# Domain Docs

How the dev-cycle skills should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`CONTEXT.md`** at the repo root, or
- **`CONTEXT-MAP.md`** at the repo root if it exists: it points at one `CONTEXT.md` per context. Read each one relevant to the topic.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in. In multi-context repos, also check `src/<context>/docs/adr/` for context-scoped decisions.

If any of these files don't exist, **proceed silently**. Don't flag their absence or suggest creating them upfront. The `/domain-modeling` skill creates them lazily when terms or decisions actually get resolved.

## File structure

This repo uses a single-context layout: `CONTEXT.md` at the root and ADRs in `docs/adr/`. Create those files only when domain terms or decisions actually need recording.

For comparison, a multi-context repo uses a root `CONTEXT-MAP.md` pointing to one `CONTEXT.md` per context, with system-wide ADRs in `docs/adr/` and context-specific ADRs in each context's `docs/adr/`.

## Use the glossary's vocabulary

When output names a domain concept (for example in an issue title, ticket, spec, or test name), use the term as defined in `CONTEXT.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary, reconsider whether you're inventing project language. If the term represents a real gap, note it for `/domain-modeling`.

## Flag ADR conflicts

If output contradicts an existing ADR, surface it explicitly rather than silently overriding it. For example:

> _Contradicts ADR-0007 (event-sourced orders). It may be worth reopening because…_
