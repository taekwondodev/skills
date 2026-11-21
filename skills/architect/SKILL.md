---
name: architect
description: "Design types, signatures, and module boundaries before code. Use for /architect, 'architect this', 'design this', or work where coding first would lock in the wrong shape."
---

# Architect

Before writing code, trace every system the change touches, then sketch two different shapes for it (types, signatures, module boundaries) and pick the one where each piece of state has one owner, each task has one way to do it, and callers need to know least. Redesign instead of patching if workarounds repeat.

For a large or contested design, run the **arena** skill instead of sketching alone and adopt its `decision/1` synthesis as the selected shape.

Completion: the selected sketch exists as types and signatures a caller can read, and the losing shape has a concrete reason.

## Agent result

When returning to another skill or agent, load [decision/1](../arena/references/result-contract.md). Return one decision with the selected shape as `choice`, the criterion that separated it as `reason`, the traced sources as `evidence`, and the losing shape in `alternatives`. Reference the sketch in `artifacts` with role `sketch`. Forward an arena synthesis as is.
