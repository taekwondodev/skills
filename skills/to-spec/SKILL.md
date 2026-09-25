---
name: to-spec
description: Turn the current conversation into a spec and publish it to the project issue tracker (no interview, just synthesis of what you've already discussed).
---

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user. Just synthesize what you already know. If real gaps remain, read the `grilling` skill (and `domain-modeling` too if the gap is a domain term) for just those gaps, not a full re-interview.

**This step is user-invoked**: start when the user requests the spec, directly or by approving that transition from `dev-cycle`. A completed investigation alone is not authorization to publish.

The issue tracker and issue-label vocabulary should have been provided to you. Tell the user to run `/dev-cycle-setup` if not; it's user-invoked, so you can't call it yourself.

Read `writing-for-agents` before drafting the spec. Its general writing rules govern this document; the spec template below adds only spec-specific structure and the budget per section.

When invoked with an issue reference, first read `docs/agents/issue-tracker.md` and fetch the issue's full body, comments, and labels through the configured tracker. Use that issue as the source material, update the same issue with the completed spec and its label transition, and do not create a duplicate issue for the same request. Resolve the configured label strings through `docs/agents/triage-labels.md`; do not assume canonical state names are the tracker labels.

When an upstream skill supplies a structured result, load its declared result contract, resolve its artifact references, and read the decision evidence.

When invoked with a `wayfinder` map whose frontier is empty, read the map's Decisions-so-far and the full body of each closed ticket. That is the source material, not the conversation.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Read back the published spec and labels, then return the verified reference and publication checks. Keep the full spec in the tracker rather than duplicating it in the response.

## Budget

A spec is a decision record, not a manual. Aim for 800 words excluding headings, using the section budgets below as review thresholds. When a section grows, remove repetition and link existing rationale or procedures rather than copying them. Keep detail necessary to make requirements, boundaries, and expected behavior unambiguous.

Exceeding a budget is a signal to review the structure, not proof that the work is oversized. Explain necessary excess rather than deleting an acceptance criterion or creating extra tickets solely to meet a word count.

## Evidence and principles

Carry forward the selected `/architect` sketch and any `how`, `why`, `investigation`, or `prototype` evidence that changed a decision. Load `blast-radius` when a contract, data shape, migration, or shared symbol may affect consumers beyond the obvious scope; the confirmed consumers and unproven risks must shape Architecture, Implementation Decisions, Testing Decisions, and Out of Scope.

Load the canonical principle when its trigger fires:

- `principle-experience-first` changes Solution and Out of Scope toward the user outcome rather than implementation convenience.
- `principle-outcome-oriented-execution` describes the intended end state and keeps temporary migration states from becoming accidental requirements.

Record a principle only where the spec can name the decision it changed. Evidence supports a decision; it does not silently expand product scope.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use `docs/agents/domain.md`'s glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. For code-shaped work with an unsettled structure, use `/architect` to derive types and responsibilities from concrete caller usage and compare viable shapes. Carry its selected sketch and rationale into the spec. Describe the project's actual components; a function or module may be sufficient. Confirm unresolved user-owned architecture decisions before recording them as settled.

3. Sketch out where this will be tested, per `/testing`'s scope. Use the highest existing seam possible; new seams are a real decision, not a default.

4. Write the spec using the template below, check every section against its budget, then publish it to the project issue tracker. Apply the configured `ready-for-agent` state label; no additional triage step is needed. When completing an issue, replace the configured `needs-grilling` state with `ready-for-agent`.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective. Guideline: one paragraph, at most 80 words.

## Solution

The solution to the problem, from the user's perspective. Guideline: one paragraph, at most 120 words.

## User Stories

A numbered list of user stories, each in the format:

1. As an <actor>, I want a <feature>, so that <benefit>

Guideline: at most 6 stories. One story per distinct user-visible outcome; stories that restate the same outcome under different conditions collapse into one. Constraints and failure behavior go in Implementation Decisions, not in stories.

## Architecture

Describe the selected structure using its actual components and responsibilities:

- The caller-facing operations, inputs, and results
- Which existing components change and which new responsibilities are justified
- The important dependencies, ownership, and error or security boundaries
- The concrete reason for the selected shape over viable alternatives, when a choice was needed

Guideline: at most 6 bullets. Include only decisions relevant to this change. Ports, layers, and bounded contexts belong here only when they are part of the selected architecture.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Schema changes
- API contracts
- Specific interactions
- Dependency additions, if any, with the `/coding-standards` justification for each

Guideline: at most 8 bullets, one decision each. Keep the rationale here or link its existing authoritative record. Before creating a separate ADR, read [ADR-FORMAT.md](../domain-modeling/ADR-FORMAT.md) and apply its necessity gate.

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts. This is not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made, scoped by `/testing`'s rules. Include:

- Which behavior-owning functions, modules, or types get test coverage, and the expected behavior/values each asserts. `/implement` writes tests against this, not values invented during implementation
- Prior art for the tests (i.e. similar types of tests in the codebase)
- Any OWASP-relevant security test called for by `/testing`'s coverage rule

Guideline: at most 6 bullets. Name the behaviors to prove and the seam; list neither test case names nor an apparatus. A verification apparatus larger than the change is a separate decision the user makes, not a Testing Decision.

## Out of Scope

The things that are out of scope for this spec. Guideline: at most 5 bullets.

## Further Notes

Anything that does not fit above. Guideline: at most 80 words; usually empty.

</spec-template>
