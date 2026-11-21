---
name: principle-build-the-lever
description: "For non-trivial mechanical work, reuse or build a tool that performs or verifies it; reserve agent effort for judgment."
---

# Build the Lever

Move mechanical work from agents to tools; reserve review for decisions that require judgment. For non-trivial work, reuse a suitable executable tool (a codemod, script, generator, or rerunnable check) before building one instead of repeating the work by hand.

Use the project's existing commands and configuration when they cover the work. Build the smallest missing lever only within the approved scope. Trivial edits may need no new tool; a judgment call is not made mechanical by putting it in a script. The bar is triviality, not repetition.

- When building a missing tool, do the first unit by hand, then build the tool and prove it by rerunning it on that unit. Make it safe to rerun.
- A deterministic tool beats fan-out. When you do fan out, write the recipe, the verification contract, and the fences as one skill the delegates read and cannot edit.
- Show the executable artifact used and its observed result. Reusing an existing tool needs no new file. Its result covers only the rules and inputs it actually checked, not semantic correctness. Commit the lever when the work outlives the session.
- Build the smallest script that does or proves the job, never a framework. A lever is bounded by the work it serves: when the lever's own code or tests outgrow the change it performs, the lever has become the project. Stop, and ask the user whether they want that project.
