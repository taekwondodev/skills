# Verification selection

Read when the evidence needed for a claim is unclear or several verification methods could fit. Compare methods against the claim, not against the subject of the change. These are comparison points, not automatic routes.

## Establish the required evidence

State the property, its source in the approved contract, and the consequence of being wrong. Trace it to the owning code and every operation or external assumption that can affect it; for a design without code, keep implementation correspondence explicitly open. Identify what current checks establish and what remains uncertain. Define whether the required claim concerns named cases, a bounded set, or an unbounded domain, and which assumptions it depends on.

Reuse an adequate existing check. When stronger evidence is needed, compare its expected coverage with the cost of constructing, running, and maintaining it. Use [proportional proof](../../principle-prove-it-works/SKILL.md) when the investment is unclear.

## Compare methods

| Method | Evidence it can provide | Limit to account for |
| --- | --- | --- |
| Existing static or structural check | An enforced rule over the code it analyzes | Its rule may not express the required behavior |
| Focused executable check | The required result for specific cases on the implementation | Unexercised cases remain open |
| Generated inputs or paths | Broader exploration of the implementation against a stated property | Sampling is not exhaustive proof |
| Exhaustive bounded exploration | The property holds throughout the explored finite scope, if exploration completes | Bounds and abstractions limit the conclusion; a separate model needs code correspondence |
| Code-level verification or deductive proof | The stated obligations hold under the verifier's semantics and assumptions | Unchecked obligations, unsupported features, and abstraction gaps remain outside the proof |

Compare the cheapest plausible method with the next stronger option. Name the additional claim the stronger option would establish and whether the task needs it. A formal method may be appropriate for an ordinary-looking change; a consequential topic may already have adequate executable evidence.

## Contrasting decisions

- **One known failure, broader behavior already covered.** A regression that fails on the broken implementation can close the gap. A new model does not automatically add useful evidence.
- **Every case in a declared finite domain must satisfy a property.** Sampling does not establish that claim. Compare exhaustive execution on the implementation with bounded verification; prefer the implementation when both are practical and adequate.
- **The claim applies beyond every tested bound.** Increasing sample counts or model bounds does not establish it. Compare a proof under explicit assumptions with the cost of leaving the claim unproven. Narrowing an approved claim requires a user decision.
- **A passing model describes an older implementation.** First establish correspondence or replace the stale result with adequate evidence. More exploration of the old model does not resolve the gap.

## Decision

If a verifier cannot analyze the implementation, say so. Prefer checks on the real code to a hand model of directly executable logic when those checks provide the required evidence; otherwise keep the proof gap explicit.

Record the property, chosen method, coverage gained, assumptions and exclusions, and why a cheaper check is insufficient or already enough. State any approval needed for new tooling or maintained verification. If no available method supplies the required evidence, keep the claim unproven rather than silently narrowing it.

Return the decision through the calling procedure's existing result contract. When a formal method is selected and construction or upkeep is authorized, read [formal-verification](../SKILL.md) to produce the check and its correspondence evidence.

Completion: the caller can explain why this method supplies the required evidence without relying on the topic's name, and can distinguish its verified scope from the claims still open.
