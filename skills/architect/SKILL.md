---
name: architect
description: "Sketch types, signatures, and module structure before code, then stay in the loop while implementation fills in. Use for /architect, 'architect this', 'design this', or non-trivial work where jumping to code would lock in the wrong shape."
disable-model-invocation: true
---

# Architect

Design an unsettled shape before implementing. Sketch types, function signatures, class shapes, and module boundaries with `not implemented` bodies and pseudocode. Synthesize independent alternatives, then fill in code against the chosen sketch. When another phase requests only a design artifact, return that artifact within its scope instead of starting implementation. Use an approved sketch directly as the input to the requested phase.

## Start

Track one entry per phase using the available task-tracking capability before starting.

1. Ground
2. Sketch
3. Agree
4. Implement
5. Scrap

## Phase A: Ground the problem

Reuse current grounding for the relevant subsystems. Where it is missing or invalidated, run the **how** skill to trace the systems the new code touches.

Naming a file is not grounding. Consume the traced model `how` prescribes. If the design redefines ownership or layering and its rationale is unknown, run **why** on the existing shape.

Skip Phase A only when the work is genuinely greenfield with no surrounding system to integrate.

## Phase B: Sketch

Run the **arena** skill with the design-sketch task and the Phase A grounding artifacts. Pass `references/runner-prompt.md` as each runner's prompt. Each candidate produces a design package shaped per `references/rationale-template.md`.

Use the configured architect runners through the available delegation capability. Preserve independent candidate contexts; report unavailable capabilities rather than simulating independent runs.

Design it twice. Require at least two structurally distinct candidates before synthesis, even when the first looks sufficient. This is the **principle-exhaust-the-design-space** principle skill made concrete. Whole-shape alternatives, not point fixes inside one shape.

Screen every candidate against [`references/design-red-flags.md`](references/design-red-flags.md) before synthesis. Reject or revise shallow modules, information leakage, temporal decomposition, and pass-through methods.

Compare viable candidates on interface depth. Prefer the design that hides more complexity behind a smaller, simpler public surface. A rich interface can keep call chains short by concentrating capability instead of scattering it across layers.

Arena returns one synthesized design package. The synthesis decision populates the rationale's "Synthesis decision" section.

## Phase C: Agree (opt-in)

Default: proceed directly to implementation with the synthesized design. No human checkpoint.

Opt in to a checkpoint when the invoker explicitly asks: "/architect with checkpoint," "stop and show me before implementing," or similar. Then surface the synthesized design and pause for sign-off.

The synthesis can ship as its own commit either way, as the "scaffold first" mode of the **principle-foundational-thinking** principle skill. Planned and scoped breakage during fill-in is fine, per the **principle-outcome-oriented-execution** principle skill. For adversarial pressure on the design before implementing, run the **interrogate** skill on the synthesized sketch. Consume its `adversarial` result through the [review result contract](../code-review/references/result-contract.md); resolve blockers and coverage gaps before filling in the design, and keep judgment calls with the user.

If the human pushes back on the shape (in a checkpoint or after the fact), treat that as Phase A evidence. Re-ground and re-run Phase B before writing more code.

## Phase D: Implement against the sketch

Replace `not implemented` bodies with code, pseudocode with logic. The synthesized sketch is the contract.

Deviations from the sketch are signal worth surfacing, not friction to absorb silently. If a function needs a parameter the sketch didn't anticipate, ask whether the sketch was wrong, the requirement was missed, or the implementation is overreaching.

## Phase E: Scrap when the architecture is wrong

If implementation keeps producing friction the sketch can't absorb, throw the sketch out. Don't bolt fixes onto a wrong design, per the **principle-redesign-from-first-principles** and **principle-fix-root-causes** principle skills.

The signal is a *pattern*, not single instances. Tells:

- The same shape of workaround appearing repeatedly across unrelated code.
- Multiple unrelated edge cases that all need special-case branches.
- Types that need escape hatches (`any`, casts, optional fields always set in practice) to compile.
- The "we need a lock" reflex when the sketch said the state wasn't shared.
- Callers having to know the abstraction's internal rules to use it.
- Two or more independent Phase D deviations of the same shape across the implementation.

Use judgment. A few edge cases don't condemn an architecture. Some problems are legitimately complex. Complexity in the data is not complexity in the design.

When you scrap:

1. Refresh **how** evidence for the parts invalidated by what was built.
2. Redesign as if the new constraints had been day-one assumptions, per principle-redesign-from-first-principles.
3. Subtract before adding, per the **principle-subtract-before-you-add** principle skill. The new sketch should be smaller than the old one before it grows.
4. Return to Phase B and re-run arena.

## Outputs

The caller's usage is written first and the type sketch derived from it. One file with new types and signatures for small changes. Module map plus type definitions for larger work. The rationale ships alongside, shaped per `references/rationale-template.md`, including the usage sketch and the synthesis decision.


## Optional architecture references

When evaluating ports and adapters, read `references/hexagonal.md` for its applicability and costs. For a layered candidate, read `references/layered.md`; for module boundaries within one deployment, read `references/modular-monolith.md`. Use these references to compare the relevant candidate against concrete usage, not to select a pattern in advance.
