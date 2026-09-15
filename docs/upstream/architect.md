# Architect upstream record

Source: https://github.com/cursor/plugins/tree/d7cde2b84eadbcd6fd890302c876f4436ccb6d82/pstack/skills/architect

Imported files: SKILL.md, references/runner-prompt.md, references/rationale-template.md, and references/design-red-flags.md.

Local adaptations:

- Use available task tracking and configured runners instead of named models.
- Resolve principle skill names with the local principle- prefix.
- Keep candidate runners scoped to their own design; the orchestrator owns dispatch and synthesis.
- Retain optional pointers to local hexagonal, layered, and modular-monolith references.

Preserve the upstream phases, mandatory arena comparison, at least two structurally distinct candidates, usage-derived sketches, and opt-in checkpoint when updating. Compare changes against the pinned source before adapting further.

Upstream license: MIT, Copyright (c) 2026 Lauren Tan (`pstack/LICENSE`). Preserved in the repository root `LICENSE` and `NOTICE.md`.
