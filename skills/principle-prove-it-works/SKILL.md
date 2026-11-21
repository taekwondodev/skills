---
name: principle-prove-it-works
description: "Apply after completing a task, before declaring done. Verify against the real artifact (run the feature, read the actual value, inspect the diff), not a proxy, self-report, or 'it compiles.'"
---

# Prove It Works

Verify every output by checking the real thing directly: run the feature, read the actual value, inspect the diff. Proxies (file mtimes, self-reports, cached output, "it compiles") do not count. When a check fails, suspect the observation method before the system.

## Proportional proof

The cost of the proof is bounded by the cost of being wrong. Before building any check, name the failure it would catch and what that failure would cost the user (a restart, a lost keypress, corrupted data, a security hole). Choose the cheapest check that catches it against the real artifact.

- A reversible change to a personal utility is proven by the existing suite, a build, and the user exercising the feature once. That is a complete proof, not a shortcut.
- A comparison between two implementations is proven by running both against the same check and letting the user try both. Two builds and one log line beat a campaign.
- Persisted data, security boundaries, and contracts consumed outside the repository earn scripted, rerunnable proof.

A verification apparatus larger than the change it verifies is a separate decision the user makes explicitly, never a default. When you notice the apparatus growing (protocols, receipts, signed manifests, evidence directories), stop and ask whether the risk justifies it.

## Script the check when you can

When the failure cost warrants it, script the check. A deterministic script that reruns the comparison beats a one-time look. Keep its output where the human can see it, and commit it only when the trail must be auditable later.
