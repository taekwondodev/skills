---
name: principle-explain-the-number
description: "Apply before measuring, and before trusting, reporting, or acting on measured results such as speedups, regressions, throughput, latency, or evaluation scores."
---

# Explain the Number

- **Write the decision before you run.** Name the result that would change a decision and the noise floor. Stop when run-to-run spread is larger than the effect.
- **Rule out alternative explanations.** List what else the number could be measuring and rule out each one with evidence. An unexplained number is not a basis for a decision.
- **Keep evidence with the number.** Retain the run count, spread, and relevant controls in the notes or a retrievable artifact.

For a performance measurement, load [benchmark-checklist](../benchmark-checklist/SKILL.md) and consume its verdict and evidence. It owns the performance checks, including the limiter, and the bounded exception for a user-requested ballpark.

For other empirical results, verify that each trial performed the intended task, that the result holds across repeated trials, and that the scenario matters. Identify experimental limits and use controls appropriate to the claim's scope.

Completion: the conclusion is supported by the measurement evidence, or the unexplained result and the observation needed to resolve it are explicit. A run started without the result that would change a decision, a missing run count, or unreported variation warrants rechecking the measurement rather than promoting the claim.
