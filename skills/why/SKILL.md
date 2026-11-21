---
name: why
description: Recover the rationale behind code, architecture, and past decisions.
---

# Why

Recover why a system works the way it does from the record. Read the commits and PR or issue discussions that introduced the target and each later change, plus ADRs, `GLOSSARY.md`, and README documents. Cite what the authors wrote, mark your own inferences as inferences, check whether later changes invalidated the original reason, and say what the record does not answer. Write rationale back to an ADR or spec only when the user's workflow asks for it.

Completion: every rationale claim cites an inspected source or is labelled as inference, and competing explanations and open questions are explicit.

## Agent result

For an agent-facing return, load [evidence/1](../investigation/references/result-contract.md). Distinguish recorded rationale from inferred explanations and retain evidence for competing or rejected explanations.
