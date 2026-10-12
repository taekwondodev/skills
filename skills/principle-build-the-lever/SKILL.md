---
name: principle-build-the-lever
description: "For non-trivial mechanical work, reuse or build a tool that performs or verifies it; reserve agent effort for judgment."
---
# Build the Lever

Move mechanical work from agents to tools; reserve review for decisions that require judgment. For non-trivial work, reuse a suitable executable tool before building one instead of repeating the work by hand.

A codemod, generator, or script does the work the same way every time and reruns for free. The tool is one artifact a reviewer can read and rerun to check the work. Hand-done changes can only be re-verified by redoing them. A deterministic script turns "trust me" into "run this".

Use the project's existing commands and configuration when they cover the work. Build the smallest missing lever only within the approved scope. Trivial edits may need no new tool; a judgment call is not made mechanical by putting it in a script.

- When building a missing tool, do the first unit by hand to learn the recipe. Prove it by rerunning it on that unit and diffing against your hand-done version. Make the lever safe to rerun.
- Codemod or script for edits, generator for repetitive files, a dump-to-sqlite query for analysis, a rerunnable check for verification.
- A deterministic lever beats fan-out. If the tool can process every unit in one pass, run it yourself; don't fan out delegates to hand-apply what a script can do.
- When you fan work out to subagents, write the lever as a skill they all read: the recipe, the verification contract, and the do-not-touch fences in one artifact. Keep it outside the delegates' write scope so they can't quietly edit the contract.
- Show the executable artifact used and its observed result. Reusing an existing tool needs no new file. Its result covers only the rules and inputs it actually checked, not semantic correctness.
- Commit the lever when the work outlives the session.

The bar is triviality, not repetition. A one-off still earns a lever when the lever is what makes the work checkable. Per the [Laziness Protocol](../principle-laziness-protocol/SKILL.md), build the smallest script that does or proves the job, never a framework. A lever is bounded by the work it serves: when the lever's own code, tests, or evidence outgrow the change it does or proves, the lever has become the project. Stop, and ask the user whether they want that project.

Distinct from [Encode Lessons in Structure](../principle-encode-lessons-in-structure/SKILL.md), which makes a recurring instruction a durable guardrail. This is throughput and reviewability on the work in front of you. For scripting the verification itself, see [Prove It Works](../principle-prove-it-works/SKILL.md).