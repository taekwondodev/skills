---
name: formal-verification
description: Build or maintain a formal check after selecting the required proof.
---

# Formal Verification

Build a rerunnable check for the selected property and proof scope. A review request selects the property and proposes the check; it does not authorize implementation. Building new tooling, creating a maintained model, or expanding verification coverage requires explicit approval. Rerunning and restoring correspondence of existing approved checks is within the implementation's scope, including modeling new readers or writers of state they already guard. Expansion means a new property, newly guarded state, or a new tool, not merely an updated file list.

## Select the proof

Consume the selected property, method, scope, and assumptions. When any is unsettled, read [verification selection](references/selection.md) and return its comparison before proceeding. A comparison that selects an ordinary check ends this procedure with that recommendation.

For a selected formal method, prefer tools the project can run and maintain. Verify current commands and supported language features from official documentation before adding an integration.

Completion: property, code scope, tool, bounds, assumptions, and uncovered risks are explicit. If construction is not authorized, return the recommendation and approval needed without creating the apparatus.

## Build a reusable check

1. Map each model action or proof obligation to retrievable code. Treat a step as atomic only when the implementation guarantees it. Include the transitions and environmental behavior that can affect the property. For a design without code, label the result design-only and defer implementation claims until correspondence is checked.
2. State safety and progress properties separately, including fairness assumptions where needed. Record finite domains, exploration bounds, excluded behavior, and tool version. An incomplete exploration, timeout, or unchecked property is inconclusive, not a pass.
3. Run the check. Keep failures as findings; change a property only when the approved contract changes, with the authorization recorded. Replay model counterexamples against real code as a reproduction or regression test. If replay fails, investigate model error first; until resolved, report a model violation rather than a proven product bug.
4. Show each property failing on a scratch broken variant of the code it protects. For a separate model, follow the same code-to-model update procedure a future change will use, then confirm the corresponding violation. Merely breaking the model does not demonstrate protection of code changes. Drop the scratch break and rerun the original check, preserving any genuine existing failure.
5. Leave one reproducible command and a project-local verification entry point using the project's existing conventions. Read [writing-for-agents](../writing-for-agents/SKILL.md) if writing a skill or agent instructions.
6. Record the property, covered files and functions, mapping, tool version, bounds, assumptions, failure demonstration, and last revision confirmed to match the code. Include a diff or content identity for uncommitted covered changes; a HEAD identifier alone does not describe a dirty tree.

If a statechart helps explain a counterexample, generate it from the checked model and disclose hidden transitions; the diagram does not establish code correspondence.

Completion: the project-local entry point runs end to end, catches the intended broken variant, identifies its covered code, and lets the next agent distinguish a pass from incomplete checking or stale correspondence. An unrun entry point is a draft.

## Maintain correspondence

Load the project-local verification instructions and compare all covered code against the recorded revision and any recorded dirty diff. Follow moved functions and new readers or writers that affect the guarded property, not just the old file list.

1. Run the existing check and record the result before editing. A pass on an old description is not evidence about changed code.
2. Classify changes as no effect, model or harness drift, an explicitly approved contract change, or a possible product bug. Update from the code, not from what makes the checker pass. Change a property only with an explicitly approved contract change. A reduced bound, omitted transition, or changed assumption that weakens coverage leaves the affected claim inconclusive until adequate replacement evidence or explicit user approval resolves it; disclosure alone is insufficient.
3. For changed verification, repeat the failure demonstration and original rerun. Replay counterexamples against the implementation. Keep product fixes separate unless implementation was authorized.
4. Update the coverage mapping and sync revision, including the diff or content identity of uncommitted covered changes, only after confirming correspondence and resolving any reduction in coverage. Leave blocked checks at their prior sync point with the unresolved changes recorded.

Completion: each check is in sync, updated, a confirmed bug, or blocked, with commands and evidence. An updated check may expose a bug. Report stale-model passes explicitly.

## Return

For a review recommendation, use the caller's `review/1` finding action or coverage limit. For artifact creation or upkeep, load and return [delivery/1](../implement/references/result-contract.md), locating the project-local instructions and checks. Include observed outcomes, bounds, assumptions, correspondence evidence, failure demonstrations, and remaining risks through its artifacts, checks, and limits. Human-facing returns explain the property, result, rerun command, and exclusions plainly.
