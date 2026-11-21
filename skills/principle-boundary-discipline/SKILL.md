---
name: principle-boundary-discipline
description: "Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions."
---

# Boundary Discipline

Validate, narrow types, and handle errors where data crosses a system boundary (CLI args, config files, external APIs, network). Parse raw data into domain types there, and keep transport and framework types out of the public surface. Inside, trust intrinsic invariants established at the boundary while they remain valid: no repeated validation and no redundant nil checks. A rule that depends on stored or mutable state is not an input invariant; evaluate it in the operation that owns that state. Business logic lives in pure functions with no framework dependencies. The shell that calls them is thin.

- Reject missing required configuration at startup rather than failing later in business logic.
- Use secure defaults and least privilege; insecure behavior requires explicit opt-in.
- Keep secrets out of code, logs, errors, traces, and comments.

Two tests. Is this an intrinsic input invariant or a rule that depends on current state? Can this be a pure function the shell just calls?
