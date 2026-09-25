---
name: show-me-your-work
description: Record decisions, evidence, and results for long or unattended work.
---

# Show Me Your Work

Keep a reviewable decision trail when work is long-running, autonomous, or likely to be reviewed later. Use a local TSV unless the user asks for a durable repository or issue artifact.

## Record

One row per decision or attempt:

```text
id\twhat\twhy\tevidence\tresult
```

For measurement work, include hypothesis, change, before, after, tests, and verdict.

## Procedure

1. Create the smallest decision log that makes the run auditable.
2. Append a row when a meaningful choice, hypothesis, or attempt is made.
3. Link evidence by path, command, issue, or URL. Do not paste large artifacts into the log.
4. Read the log before making the next dependent decision.
5. Keep it local by default. Commit it only when the work outlives the session or needs an auditable record.

## Agent result

At an agent-facing handoff, load [delivery/1](../implement/references/result-contract.md). Return the log locator and verification, not a replay of its rows.

## Verification

Every row has a reason, evidence, and result. The log distinguishes decisions from observations. It contains no secrets or unsupported self-reports.
