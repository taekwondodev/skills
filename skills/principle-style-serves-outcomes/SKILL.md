---
name: principle-style-serves-outcomes
description: "Apply when a style, idiom, readability, or abstraction choice could change runtime cost."
---

# Style Serves Outcomes

Style reduces development effort and reader load. Preserve correctness, security, and required behavior.

- **Zero-cost abstractions.** Prefer abstractions whose overhead the compiler or runtime erases.
- **Modern idioms.** Use the language's current idioms when they are at least as fast as the older form.
- **Ground the cost.** Ground runtime-cost comparisons in the executed code, accounting for compiler and runtime optimization, or in representative measurements. When uncertainty could change the decision, measure through [benchmark-checklist](../benchmark-checklist/SKILL.md).
- **Weigh by frequency.** Establish execution frequency from the workload. On frequent paths, any proven runtime cost overrides readability, however small. Startup, error, and one-shot paths take the clearer form unless a measurement shows otherwise.
- **Keep the fast form readable.** When performance wins, recover readability through names, types, and structure rather than reverting to the slower form.

Resolve the tradeoff from the evidence; on its own it is not a user-owned decision.

**The test:** Is the selected form justified by workload frequency and runtime-cost evidence?
