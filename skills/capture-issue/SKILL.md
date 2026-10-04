---
name: capture-issue
description: Capture a new issue quickly when the idea should be recorded now and explored later.
disable-model-invocation: true
---

# Capture Issue

Create a new issue from the user's current request when they want to record an idea without grilling or repository exploration. This is a parked capture, not a specification or an implementation ticket.

Read `writing-for-agents` before writing the issue title or body. Keep the result minimal: synthesize a concise title and minimally clean the user's text without adding requirements, acceptance criteria, architecture, testing decisions, or scope claims.

Read `docs/agents/issue-tracker.md` for issue-creation operations and `docs/agents/triage-labels.md` for label rules. If either document is missing, tell the user to run `dev-cycle-setup` and stop without publishing.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Return the created issue reference after reading back its body and labels. The receipt records capture only, not readiness for implementation.

## Process

1. Read the user's request as the only source material. Do not explore the repository or ask design questions.
2. Classify the request as exactly one category: `bug` or `enhancement`.
3. If the category is ambiguous, ask one focused classification question before publishing. Do not ask any other question in this skill.
4. Create a new issue in the configured tracker with the concise title and minimally cleaned body.
5. Apply the category label, the `needs-grilling` readiness label, and the `parked` activity label.
6. Return the created issue through the agent result contract, or report it concisely to the human, and stop.
