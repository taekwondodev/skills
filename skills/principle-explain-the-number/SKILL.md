---
name: principle-explain-the-number
description: "Apply before measuring, and before trusting, reporting, or acting on measured results such as speedups, regressions, throughput, latency, or evaluation scores."
---

# Explain the Number

A real output does not establish what a measurement means. Explain the result before using it to choose a change or claim an improvement.

- **Write the decision before you run.** Name the result that would change a decision and the noise floor. Stop when run-to-run spread is larger than the effect.
- **Ask "why not double?"** Identify the resource or code path bounding a performance result, such as a core, lock, disk, network, or load generator. Use a profile or system counters from a run, then map the limiter to source. Reading code alone does not establish it.
- **Rule out alternative explanations.** Check for errors, skipped or cached work, code that never ran, untuned alternatives, noise, and improvements too small to matter end to end. An unexplained number is not a basis for a decision.
- **Keep evidence with the number.** Retain the run count, spread, and relevant controls in the notes or a retrievable artifact. Include the measured limiter for performance results.

For performance measurements, load [benchmark-checklist](../benchmark-checklist/SKILL.md) and consume its vetted verdict and evidence. It owns the full procedure and the bounded exception for a user-requested ballpark.

For other empirical results, verify that each trial performed the intended task, that the result holds across repeated trials, and that the scenario matters. Identify experimental limits and use controls appropriate to the claim's scope.

Completion: the conclusion is supported by the measurement evidence, or the unexplained result and the observation needed to resolve it are explicit. A run started without the result that would change a decision, a missing run count, unreported variation, or time saved beyond the changed component's cost warrants rechecking the measurement rather than promoting the claim.
