---
name: to-tickets
description: Break a complete approved spec into tracer-bullet tickets when multiple implementation slices are needed, each declaring blocking edges and affected components, published to the configured tracker.
disable-model-invocation: true
---

# To Tickets

Decompose a complete, approved spec into the smallest useful set of **tickets**: implementable slices with real blocking edges and the selected components they touch.

**Scope conservation:** completing the tickets delivers the approved spec, neither less nor more. Every ticket obligation must trace to a requirement, constraint, or testing decision in the spec or an explicitly approved input it references. Clarify acceptance without inventing product behavior, architecture, or verification requirements. Present newly discovered necessary prerequisites separately for approval; leave optional improvements outside the breakdown.

Use the architecture, ownership, and security decisions referenced by the approved spec as inputs.

**This step is user-invoked**: start when the user requests decomposition, directly or by approving that transition from `dev-cycle`. The breakdown still requires approval before publication.

The issue tracker and issue-label vocabulary should have been provided to you. Tell the user to run `/dev-cycle-setup` if not; it's user-invoked, so you can't call it yourself.

Read `writing-for-agents` before drafting ticket bodies. Its general writing rules govern this document; the ticket template below adds only ticket-specific structure. Resolve the configured `ready-for-agent` state label through `docs/agents/triage-labels.md` rather than assuming the canonical name is the tracker label.

## Process

### 1. Gather context

Work from the complete approved spec. If the user passes a reference (a spec path, an issue number or URL) as an argument, fetch it and read its full body and comments. If the available material is only a plan, conversation, or incomplete issue, stop and hand off to `to-spec` rather than drafting tickets.

### 2. Explore the codebase (optional)

If you have not already explored the codebase, do so to understand the current state of the code. Ticket titles and descriptions should use `docs/agents/domain.md`'s glossary vocabulary, and respect ADRs in the area you're touching.

Use exploration to verify feasibility and dependencies of the approved work. Distinguish a prerequisite without which that work cannot proceed from a refactor or automation that would merely make it easier.

### 3. Draft vertical slices

Break the work into **tracer bullet** tickets.

First decide whether the approved spec describes one independently implementable slice or multiple slices. If it is one slice, report that `to-tickets` would add no value and stop. Do not publish a redundant ticket.

Start with the fewest tickets that preserve independently verifiable outcomes. Justify each additional split with a distinct deliverable, an evidenced size limit, or a necessary technical boundary. Different files, tools, or adapters alone do not justify separate tickets.

Judge the breakdown by scope coverage, justified boundaries, and real dependencies, not by ticket count. Merge tickets when combining them preserves a coherent, verifiable outcome and no evidenced size or dependency constraint requires separation.

Write concise acceptance criteria, each describing an observable behavior. Their count does not determine ticket boundaries; express independent checks as separate criteria within the same ticket.

<vertical-slice-rules>

- Each slice delivers a complete path through the components it needs, using the architecture already selected in the spec
- A completed slice is demoable or verifiable on its own. Allocate the spec's Testing Decisions to the relevant slices; load `/testing` when translating them into acceptance criteria and preserve their scope.
- Split for size only when inspected work shows that a slice cannot be completed coherently in one implementation session; a generic context-window concern is not evidence
- Sequence approved prerequisites before the work they genuinely block

</vertical-slice-rules>

Give each ticket its **blocking edges**, meaning the other tickets that must complete before it can start, and the affected components or layers using the project's vocabulary. Explain dependencies through the concrete output needed from the blocker. A preferred implementation order alone is not a blocking edge.

For an approved migration that cannot land as independent vertical slices, preserve its specified sequencing and verification boundaries. If those decisions are missing, return the gap for approval instead of choosing a migration strategy during decomposition.

### 4. Quiz the user

Present the proposed breakdown as a numbered list. For each ticket, show:

- **Title**: short descriptive name
- **Affected components**: the existing architecture areas this touches
- **Blocked by**: which other tickets (if any) must complete first
- **What it delivers**: the end-to-end behaviour this ticket makes work
- **Why separate**: the concrete reason this is a ticket rather than part of another

Ask the user in the available interaction channel:

- Does the granularity feel right? (too coarse / too fine)
- Are the blocking edges correct? Does each ticket only depend on tickets that genuinely gate it?
- Should any tickets be merged or split further?

Iterate until the user approves the breakdown.

### 5. Verify scope and publish

Before publication, check both directions: every requirement and testing decision in the spec is allocated, and every ticket obligation has an approved source. Use the spec's sections or requirement descriptions to check traceability; add a source pointer where the connection is not obvious. Resolve gaps or additions before publishing. Keep shared constraints authoritative in the parent and carry the relevant ones into each ticket without copying unrelated policy.

Publish the approved tickets in dependency order (blockers first) so each ticket's blocking edges can reference real identifiers. Use the tracker's native blocking / sub-issue relationship. See `docs/agents/issue-tracker.md`'s "Tracer-bullet ticket operations" section. Apply the configured `ready-for-agent` state label unless instructed otherwise: the tickets are agent-grabbable by construction.

Read back the published bodies, labels, and native relationships. Report which tickets have no open blockers, then stop; implementation is a separate step.

Preserve the parent issue's body, labels, and open/closed state. Adding the required native child relationships is permitted.

<issue-template>

## Parent

A reference to the parent issue on the tracker (if the source was an existing issue or a `/wayfinder` map, otherwise omit this section).

## Affected components

The components or layers named by the approved architecture that this ticket touches.

## What to build

The end-to-end behaviour this ticket makes work, from the user's perspective, not layer-by-layer implementation.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to each blocking ticket, or "None: can start immediately".

</issue-template>

Avoid specific file paths or code snippets. They go stale fast. Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it and note briefly that it came from a prototype. Trim to the decision-rich parts rather than a working demo; include just the important bits.
