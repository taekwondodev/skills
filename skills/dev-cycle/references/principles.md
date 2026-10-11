# Principle Selection

Consult this index when choosing the principle that governs a current decision. Read its canonical body before relying on it; a route through this index does not activate every principle or future phase. Each bold entry names the `principle-<title>` skill: lowercase the title and replace spaces with hyphens.

### Core

- **Laziness Protocol**. Bias toward deletion and the smallest change that solves the problem.
- **Foundational Thinking**. Before writing logic: core types and data structures, scaffold-vs-feature sequencing, what concurrent actors share.
- **Redesign from First Principles**. Redesign as if the requirement had been foundational from day one.
- **Subtract Before You Add**. Remove dead weight, redundant validators, and stub references first, then build on the simpler base.
- **Minimize Reader Load**. Count layers between question and answer, and hidden state in the reader's head; collapse one-caller wrappers and shrink mutable scope.
- **Outcome-Oriented Execution**. Planned rewrites and migrations converge on the target architecture instead of preserving throwaway compatibility states.
- **Experience First**. Choose user delight over implementation convenience; ship fewer polished features over more rough ones.
- **Exhaust the Design Space**. A novel interaction or architectural decision gets 2-3 competing prototypes before commitment.
- **Build the Lever**. For non-trivial work, build the tool that does or proves it instead of working by hand.

### Architecture

- **Model the Domain**. Encode the domain in a structure instead of scattered conditionals.
- **Boundary Discipline**. Concentrate guards at system boundaries; trust internal types and keep business logic pure.
- **Type System Discipline**. Make illegal states unrepresentable, brand semantic primitives, and parse external data at boundaries.
- **Make Operations Idempotent**. Converge to the same end state regardless of partial prior runs.
- **Migrate Callers Then Delete Legacy APIs**. Migrate callers and delete the old API in the same wave.
- **Separate Before Serializing Shared State**. Eliminate sharing first; serialize only when one shared writer is a real invariant.

### Verification

- **Prove It Works**. Verify against the real artifact, not a proxy, self-report, or “it compiles.”
- **Explain the Number**. Before trusting or reporting a measured result, identify what bounds it and rule out misleading measurements.
- **Fix Root Causes**. Trace each symptom to its root cause and fix it there; reproduce first.
- **Sequence Verifiable Units**. Break multi-step work into small units that each end in a checkable state.

### Delegation

- **Guard the Context Window**. Route bulk to subagents and keep summaries in the main thread.
- **Never Block on the Human**. Proceed on observable facts and reversible preparation; stop for product, scope, architecture, contract, security, and other human-owned decisions.

### Meta

- **Encode Lessons in Structure**. Encode recurring corrections as lint, metadata, runtime checks, scripts, or skills instead of repeating prose.

When a principle influences a choice, record the principle and the changed choice. A principle name without a decision is not evidence of application.
