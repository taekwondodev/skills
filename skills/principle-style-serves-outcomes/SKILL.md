---
name: principle-style-serves-outcomes
description: "Apply when a style, idiom, readability, or abstraction choice could change runtime cost. On conflict, runtime performance wins."
---

# Style Serves Outcomes

Style exists to reduce development effort and reader load. It earns that without sacrificing runtime performance. Correctness, security, and required behavior stay fixed; runtime performance breaks ties between style and speed.

- **Zero-cost abstractions.** Prefer abstractions the compiler or runtime erases: generics with static dispatch, inlined helpers, newtypes, fused iterators, compile-time configuration. An abstraction that adds allocation, copying, dynamic dispatch, or indirection on a hot path keeps its place only with evidence that the cost is negligible.
- **Modern idioms.** Use the language's current idioms when they are at least as fast as the older form.
- **Ground the cost.** A cost claim in either direction names its mechanism (allocation, copy, dispatch, complexity class, syscall, lock contention) or a measurement. When the mechanism is uncertain and the path matters, measure through [benchmark-checklist](../benchmark-checklist/SKILL.md). An evidenced cost overrides readability; a speculative one does not.
- **Weigh by frequency.** Code that runs per request, per item, or inside a loop is where cost matters. Startup, error, and one-shot paths take the clearer form unless a measurement shows otherwise.
- **Keep the fast form readable.** When performance wins, recover readability through names, types, and structure rather than reverting to the slower form.

Resolve the tradeoff from the evidence; on its own it is not a user-owned decision.

**The test:** Does the style choice change what the machine does on a path that runs often? If not, take the clearer form. If it does, keep the faster form and make it readable.
