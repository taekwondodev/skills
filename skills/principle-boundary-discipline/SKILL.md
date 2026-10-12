---
name: principle-boundary-discipline
description: "Apply when wiring validation, error handling, or framework adapters. Concentrate guards at system boundaries (CLI, config, network, external APIs); trust internal types and keep business logic in pure functions."
---

# Boundary Discipline

Place validation, type narrowing, and error handling at system boundaries. Trust established intrinsic invariants internally; keep context-dependent rules with the operation that owns their state. Business logic lives in pure functions; the shell is thin and mechanical.

**Why:** Scattered validation is noisy, redundant, and gives a false sense of safety. Keep logic out of framework wiring so it can be tested without the framework.

**The pattern:**
- **At boundaries** (CLI args, config files, external APIs, network protocols): validate, return errors, handle defensively.
- **Inside the system:** typed data, error propagation, no repeated intrinsic validation. Reuse established facts while they remain valid. Rules needing stored or mutable context remain with the operation that owns the decision.
- **Across the boundary.** Expose domain concepts, not the boundary's private representation. Keep general-purpose mechanism inside and special-purpose policy at the edge.

**Applications:**

Validation and error handling:
- Validate config at parse time (the boundary), not inside business logic
- Parse raw data into domain types at the boundary
- Do not re-export transport, storage, framework, or wire types through the public surface
- No redundant nil checks deep in call chains if the boundary already validated
- Reject missing required configuration at startup rather than failing later in business logic
- Use secure defaults and least privilege; insecure behavior requires explicit opt-in
- Keep secrets out of code, logs, errors, traces, and comments

Code organization:
- Business logic in pure functions with no framework dependencies
- Parse functions: pure transforms from raw bytes to typed state
- Prompt construction: structured state in, string out
- Scoring and assessment: pure transforms from state to results

**The tests:**
- "Is this an intrinsic input invariant or a rule depending on current state?" Parse the former at entry; evaluate the latter at its state-owning operation.
- "Can this be a pure function that the shell just calls?" If yes, extract it.