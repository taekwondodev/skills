---
name: principle-guard-the-context-window
description: "Apply when context is filling up: large outputs, long files, repeated reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread, not raw payloads."
---

# Guard the Context Window

- **Isolate large payloads.** Route verbose outputs, screenshots, and large documents to subagents; return summaries to the main context.
- **Load selectively.** Read only sources needed for the current task.
- **Inline shared needs.** Keep material needed on every invocation in the skill; disclose branch-specific material on demand.
- **Bound phases.** Limit files per phase, set turn budgets, and account for mechanism costs.