# Residual-risk gate

The semantic reviewer decides whether independent Adversarial review is needed after inspecting the diff, contract, consumers, and current check evidence. Size does not determine this decision. For small changes this assessment may be inline; for medium or large changes the semantic reviewer is independent. A direct request for adversarial review requires that review.

## Decide

1. Identify plausible failures and their consequences. Inspect security boundaries, persisted data and migrations, external compatibility, irreversible effects, shared ownership, concurrency, retries, cancellation, and recovery when touched. A small diff can change a critical protocol; a large mechanical diff can be well covered.
2. Match each significant risk to evidence that actually covers it. Record the checked revision, a diff or content identity for uncommitted changes, and relevant inputs, assumptions, bounds, and consumers. A suite passing, a tool being installed, or a model passing alone is insufficient. For a separate model, confirm correspondence with the current code, including atomic steps and all readers or writers that affect the modeled property. Code or model drift invalidates affected proof until reconciled.
3. Require independent Adversarial review for significant uncovered or uncertain risks. Name the claims and missing evidence in the pending disposition. Uncertain impact is not low risk. Permit a skip only when each identified significant risk has adequate current evidence and any remaining risks have low and reversible consequences. Cite the concrete evidence and its boundaries.

A skip saves a worker, not the assessment. Keep Standards and Spec review. New findings can reopen the gate. A passing formal check can discharge its modeled property, not unrelated security, integration, or contract obligations. A stale model does not make model repair mandatory: adequate cheaper evidence may resolve the risk while the stale result remains explicitly unused. Require repair only when the approved contract requires that maintained check.

## Return

Use the existing `review/1` Adversarial axis alongside the semantic axes. The coordinator retains the assignment role to distinguish a semantic gate disposition from an Adversarial worker's review:

- **Skip:** `coverage: skipped`, empty findings, and limits stating who assessed the gate, why no independent pass is required, the checked revision plus a diff or content identity for any uncommitted changes, supporting evidence, and what remains outside it. An inline skip explicitly says it is self-assessed, not independent.
- **Dispatch:** `coverage: partial`, empty findings, and limits naming the residual risks and required independent investigation. If missing or inaccessible evidence prevents a decision, use this disposition and name the evidence gap; uncertainty never permits a skip. Keep semantic findings on their own axes. The coordinator replaces this pending disposition with the worker's result before delivery.

For example, a local label change can skip with evidence that only display text changed and no stored or external identifier uses it. A lease change with only sequential checks needs independent investigation of overlapping acquisition and expiry. A passing lease model with an unmodeled new writer remains uncertain.

Completion: the coordinator can either justify the skip from retrievable evidence or dispatch a bounded independent assignment. Missing evidence is never reported as a clean review.
