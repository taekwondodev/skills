---
name: dev-cycle
description: Route development work through principles, capabilities, and verified delivery.
disable-model-invocation: true
---

# Dev Cycle

`dev-cycle` is the normal entrypoint for development work. Size the task, select the current mode, and activate only the procedure needed for the next result. A planned route is not a preload list.

## Task state and context

Stay active for the current task across turns. `continue` resumes it; `new task` resets classification. A direct skill invocation overrides the current step without silently changing the task's scope. For work spanning turns, keep the current mode, decisions, evidence, and next completion criterion in the todo or handoff.

- Reuse a skill body already available and unchanged in this context. Reload when it was lost through compression or pruning, its file changed, or a new worker needs it. Names in a handoff do not substitute for the bodies.
- Reuse grounded evidence and approved artifacts while they remain current. A dependency consumes their result; it does not restart completed work merely because another phase references it.
- Load a principle when it governs a concrete current decision. Use [the principle index](references/principles.md) when selecting its canonical owner; record the choice it changed, not an inventory of every principle.
- Keep safety, acceptance criteria, and selected contracts available to the implementer. Full coding-conformance criteria belong to the reviewer. A skill loaded inline shares the current context; isolation requires a separate worker or session.

## Size before routing

Default to **small** and move up only on evidence. Ceremony follows size. Read [sizing examples](references/sizing.md) when the boundary is unclear.

| Size | Signals | Route and proof |
|---|---|---|
| **Small** | one behavior, few files, reversible, no persisted format or shared contract change | reproduce, record the expected line, implement, check the real artifact, one inline review |
| **Medium** | one feature or fix across modules, or a repository-internal contract | `grilling` on open decisions, checkpoint, `to-spec`, `implement`, one `code-review` per completed unit |
| **Large** | new bounded context, persisted format, security boundary, or multi-session work | user's explicit agreement to the size, then `wayfinder` into the approved spec and implementation route |

For a small change, an explicit user request can already establish the expected behavior; ask only about missing or conflicting expectations. Add the smallest regression proof, run the relevant existing suite and build, and retain the user's manual check where required by the task.

`principle-prove-it-works` owns proportional proof. A verification apparatus larger than the change needs the user's explicit request. Do not add a test methodology the task does not require.

## Select the current mode

| Mode | Current procedure and output |
|---|---|
| **Investigation** | `how` for current behavior, `why` for rationale, or `investigation` for an unknown cause; return cited evidence, not an unsolicited change. Use `grilling` only for user-owned decisions left open by the evidence. |
| **Feature** | Follow the sized route. Use `to-tickets` only for multiple independently useful slices of an approved spec. |
| **Bug fix** | Reproduce, trace the root cause, add regression proof, fix, and review. An error-handling change stays a bug fix at small size unless it changes a persisted format, security boundary, or shared contract. |
| **Refactoring** | Pin behavior, identify affected consumers with `blast-radius` when uncertain, subtract dead weight, migrate callers, and verify equivalence. Promote when behavior changes. |
| **Performance issue** | `perf-issue`: realistic baseline, mechanism-based hypothesis, one change through `implement`, before/after measurement. |
| **Hillclimb** | `hillclimb`: frozen harness, hypotheses, keep/revert iterations through `implement`, explicit stop predicate or documented plateau. |
| **Architecture** | Activate `architect` for an unsettled shape, ownership model, dependency direction, or boundary. Consume an approved sketch directly when the design is settled. |
| **Large work** | `wayfinder` owns map and decision tickets. Use `handoff` and `session-pickup` at real context boundaries; `show-me-your-work` when an unattended run needs a decision trail. |

Use secondary capabilities only when the current mode needs their result. For a live symptom use `runtime-forensics`; for a supplied trace use `trace-forensics`. Neither automatically authorizes a fix.

## Decisions and promotion

Separate facts, hypotheses, and user-owned decisions. Investigate observable facts before asking questions. Present genuine choices through the available structured user-question capability.

Preserve the human checkpoint after grilling. Planning approval does not silently authorize implementation: the user requests the next phase, directly or by approving the proposed transition. The phase retains its own publication and execution gates.

`architect` has no automatic checkpoint; it proceeds unless the user explicitly requests one. This does not authorize new product scope, public contracts, or security policy.

Promote to the governed decision path when the work changes unapproved product behavior, scope, a public API consumed outside the repository, a schema or persisted format, a bounded context, a security boundary, or a major compatibility decision. Continue reversible investigation while the decision is pending.

A prototype, benchmark, or internal ownership change alone is not promotion. Before creating an ADR for an internal choice, apply the [ADR necessity gate](../domain-modeling/ADR-FORMAT.md). Do not create a spec solely for ceremony.

## Delegation and delivery

Keep one coordinator responsible for synthesis, external effects, and verification. Delegate independent research or artifacts in separate contexts, with explicit scope, accessible source paths, write boundaries, and completion criteria. Reviewers load their own standards. Supply source contents only when the worker cannot retrieve them. Use worktrees for concurrent repository writers.

`code-review` owns the review gate once per completed unit, including a dependent ticket chain, and reruns only affected axes after fixes. When consuming its result directly, load the [review result contract](../code-review/references/result-contract.md) and apply its gates to the payload without an intermediate prose report. Resolve delivery intent and branch preparation through [the shared delivery reference](../implement/references/delivery.md) before implementation. `commit` owns requested local commits and authorized direct delivery; `pr` owns requested PR publication. Report unavailable independence instead of simulating it, and verify artifacts rather than trusting a worker's self-report.

For an agent-facing return, consume and forward the active phase's declared result contract without wrapping it in another report. Preserve that procedure's pending decisions and next checkpoint. If no phase result exists yet, continue the current interaction rather than fabricating a completed payload.

Completion: the requested result exists, its relevant behavior or evidence was checked, user-owned decisions are settled, changed files are accounted for, and remaining risks are explicit. For a human-facing summary, report checks and principles that changed actual choices.

Direct invocation remains supported: each phase owns its prerequisites and consumes only the sources needed for that invocation.
