---
name: coding-standards
description: Choose project coding policy, dependencies, or external APIs when a decision is unresolved.
---

# Coding Decisions

Resolve an explicit coding-policy, dependency, or API choice. Start from the project's existing conventions, toolchain, approved behavior, and security and compatibility constraints. Reuse settled decisions.

## Coding policy

Identify the concrete problem the proposed rule solves. Distinguish a binding project requirement from a design heuristic or preference. A convention must reduce development or reader effort without silently trading away required behavior, security, or runtime performance.

Use the canonical owner only for the question being decided:

- Types and public signatures: [Type System Discipline](../principle-type-system-discipline/SKILL.md).
- Validation and security boundaries: [Boundary Discipline](../principle-boundary-discipline/SKILL.md).
- Readability, comments, and complexity: [Minimize Reader Load](../principle-minimize-reader-load/SKILL.md).
- Replacing an internal API: [Migrate Callers Then Delete Legacy APIs](../principle-migrate-callers-then-delete-legacy-apis/SKILL.md).

For a mechanically decidable rule, use [Build the Lever](../principle-build-the-lever/SKILL.md) to select existing enforcement before proposing new tooling. Record the rule in its authoritative configuration or policy, not a second checklist. Tooling changes require approved scope; an uncovered rule does not authorize installation.

## Dependencies and APIs

Prefer the standard library or an existing dependency. An addition needs a substantial capability, performance, or complexity benefit that the existing stack cannot provide reasonably.

For version, API, maintenance, security, or license facts, use [investigation](../investigation/SKILL.md) and consume its verified sources and limits. Reuse current evidence; never select versions or assert API behavior from memory. Choose widely used, actively maintained dependencies that fit the project. Check security advisories, prefer a disclosure policy, and run applicable audits. Verify license compatibility with the distribution model; flag copyleft implications and unavailable evidence.

Compare viable options against the approved constraints, including migration and runtime costs. Recommend one option with its rationale and unresolved risks. Return scope, public compatibility, and security-policy changes to the caller for the user's decision before adopting them.

## Result

For an agent-facing return, use [evidence/1](../investigation/references/result-contract.md). Distinguish verified facts from the recommendation and retain unresolved approval or evidence gaps. A recommendation is not authorization to change project policy or dependencies.

Completion: the caller can identify the proposed choice, its evidence and tradeoffs, the authoritative owner, and any decision that still requires approval.
