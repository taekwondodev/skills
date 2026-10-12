---
name: principle-encode-lessons-in-structure
description: "Apply when writing the same instruction a second time or noticing a recurring correction."
---

# Encode Lessons in Structure

Encode recurring fixes in mechanisms rather than repeated instructions.

1. Check whether a tool, type, lint rule, metadata flag, runtime check, or script can enforce the lesson.
2. If it can, implement the mechanism and remove the redundant instruction.
3. If it requires judgment, make the instruction more prominent and add an example of the failure mode.

**Pick the strongest mechanism.** When more than one mechanism would work, choose the strongest the situation allows (an unrepresentable state that cannot compile, then a lint or banned API that fails CI, then a canonical helper, then a runtime check), because agents copy whatever the surrounding code already does and a weaker guard becomes the next template.

**Feedback loop:** When the human intervenes or tests fail, classify and route the correction: one-off -> brain note, recurring fix -> skill or lint rule, systemic issue -> principle. Address the recurring pattern, not only the observed instance. Close the loop: apply now or create a concrete todo.