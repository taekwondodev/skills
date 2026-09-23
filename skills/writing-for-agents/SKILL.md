---
name: writing-for-agents
description: Writing agent-facing documents. Use when creating or editing skills, project context, ADRs, specs, tickets, comments, or agent briefs.
---

Use this contract for agent-facing writing, from titles and comments through specs, ADRs, and handoffs. Artifact-specific writers may add format or domain constraints, but must not contradict these shared rules.

## Operating rules

- Write prose and explanatory string values in plain English. Structured results use their contract's keys and enum values. Never use em-dashes; rewrite naturally rather than swapping punctuation mechanically. Keep prose harness-neutral unless the document explicitly describes an integration. A project context file may name a deliberate integration, but the no-em-dash rule remains unless the user explicitly changes it.
- Match the consumer: return contracted data to another skill or agent; render concise prose only at the human-facing boundary. A structured result is a deliverable, not an outline for a second report.
- Ground external context: name a retrievable source or include the context needed to understand each claim. Never rely on an unavailable conversation.
- Keep one source of truth per meaning. Link to authoritative material instead of repeating it. Document unwritten conventions, reasons, and gotchas; leave cheap lookups to the environment.
- Keep scope tight. Include requirements and guardrails the artifact needs, and make branch-specific instructions conditional. Keep run-specific constraints and verification outcomes in task records, not reusable instructions.
- Define completion for each step or deliverable in observable, checkable terms, with enough demand to establish that the work is actually done.

## Further guidance

When defining or changing a skill-to-skill or subagent response, load [agent-results.md](references/agent-results.md) for the shared result contract. The producing skill owns its domain-specific shape.

Load [authoring.md](references/authoring.md) when designing or restructuring an agent-facing document or skill, including decisions about information hierarchy, pointers, splitting, and pruning. Routine title or comment work needs only this contract.

When authoring a skill, read [SKILL-MECHANICS.md](SKILL-MECHANICS.md) for frontmatter, invocation choice, and router skills.
