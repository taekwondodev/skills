---
name: implement
description: "Implement a piece of work based on a spec, ticket, or agreed small change, writing tests against its Testing Decisions or acceptance criteria."
disable-model-invocation: true
---

# Implement

Implement the approved spec, ticket, or small change. Start only when the user requests implementation, directly or by approving that transition from `dev-cycle`.

## Establish the contract

Read the approved behavior, acceptance criteria, selected architecture or sketch, and applicable security and compatibility constraints. Use the project's actual components and ownership. Reuse current grounding; a settled design is an input, not a reason to run `architect` again.

For a small change without a spec, record the **expected line**: observed behavior from the reproduction and required behavior after the change. An explicit, unambiguous user request already confirms the required behavior; ask only about a missing or conflicting expectation. Preserve the line in the issue or another durable task artifact before implementation.

Record the starting commit and the review unit. One independent ticket is one unit; a dependent ticket chain shares its starting commit and one final review. Resolve the task's delivery route and prepare its branch before editing through [delivery mode and branch preparation](references/delivery.md).

## Build and verify

1. Write tests at the agreed seams using `testing` when adding or changing tests. Expected values come from the approved contract, not the implementation. For a bug fix, use `principle-fix-root-causes` to guide reproduction and the causal check. Run the regression test red before fixing the owning cause when following the small-change path without a spec or ticket.
2. Implement within the selected boundaries. Preserve required authorization, validation, secure defaults, and secrets handling while coding; these are not deferred to review.
3. Load a specialist only for an unresolved need in this step: `investigation` for an unknown cause, `blast-radius` for uncertain consumer impact, `architect` for an unsettled shape or boundary, or `coding-standards` for a dependency or API decision. Consume each specialist's declared result contract and inspect its evidence without requesting a second report. Return scope, contract, and security changes to the user before choosing them.
4. Reuse the active procedure's workload, pinned behavior, and evidence rather than restarting its router. For a direct performance task without that context, use `perf-issue` or `hillclimb` to establish the realistic workload and measured verdict. For a refactoring, pin behavior and migrate every affected caller against the selected target shape. Run focused tests and typechecking during the change, then the relevant suite and build at the unit boundary.
5. Exercise the changed behavior against the real artifact using `principle-prove-it-works` when selecting the proof. Report what was exercised, unavailable, or unproven.

Extended coding-conformance checks belong to the Standards reviewer. Supply its source paths at review time instead of preloading the standards corpus into the implementation context.

## Agent result

For an agent-facing return, load [delivery/1](references/result-contract.md). Locate the changed artifact or commit and retain the actual checks, review disposition, and unresolved limits. Keep review evidence accessible instead of repeating every finding.

## Complete the unit

Use `code-review` once at the completed unit boundary, against its recorded starting commit and approved contract. Load its [result contract](../code-review/references/result-contract.md) when consuming the review. Use the returned axes, finding actions, and coverage limits directly; apply its gates without expanding the payload into another report. Intermediate dependent slices retain their checks and defer the full review to the unit boundary. Fix blocking findings and rerun only affected review axes.

Stop with the reviewed changes uncommitted. When the user requests a commit, load `commit` with the reviewed scope, verification evidence, issue reference, resolved delivery context, and approved actions. If the user requests PR publication, load `pr` with the same evidence. Ask before dispatching another unit.

Completion: the approved behavior is implemented, the relevant checks passed on the real artifact, the review gate is satisfied, and every changed file is accounted for.
