---
name: principle-foundational-thinking
description: "Apply before writing logic: choosing core types and data structures, sequencing scaffold-vs-feature work, asking what concurrent actors share. Get the data structures right so downstream code becomes obvious."
---

# Foundational Thinking

Get the data shape right before writing logic. Define core types early, trace every access pattern, and choose structures that match the dominant paths. DRY the structure, not every line.

State shared between concurrent actors follows the **separate-before-serializing-shared-state** principle skill.

Scaffold first. Whatever helps every later phase (CI, tests, shared types) goes first, after removing dead weight. Keep commits small and single-purpose.
