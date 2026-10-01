# Test audit

Procedure for a sweep of existing tests with no change driving it. The anti-patterns and the expected-value rules in [SKILL.md](../SKILL.md) decide what is junk; this reference decides how a candidate becomes a deletion. Optimize for confidence, not deletion count.

## Discovery

Read-only, before any edit. Partition the test surface into lanes by production ownership, not by directory, and run broad lanes in parallel workers that report evidence without editing. Read the root and scoped project instructions first. For each candidate, read the complete test, its production owner, callers, sibling implementations, overlapping tests, every runner or driver that consumes the test's output, and the commit that introduced it. Prefer a few high-confidence candidates over a large speculative inventory.

## Candidate evidence

Record every field before editing; a missing field means the candidate is not ready:

- exact test name and location;
- the failure it can detect today;
- non-test consumers of the covered production or support seam, including a runner, driver, or expectation file that reads the test's output or exit code;
- the stronger owner proof that remains, by name and location, or why none is needed;
- the commit and the reason the test or seam exists;
- the production or test-support deletion it unlocks;
- risk and the focused validation command.

## Retention bar

Keep a test that independently enforces a public API, protocol, config, storage, security, platform, default, release, or architecture contract. Also keep call ordering when order is observable behavior, a regression with a credible failure mode, and source inspection when it is the cheapest independent guard of a user-facing key, byte, or path. Static or slow is not a deletion reason. A retained test that fails on the baseline is a possible product bug: reproduce it and repair the owner. A test that resembles implementation may still be the independent contract; prove otherwise before removing it.

## Edit shape

One coherent batch per owner boundary. Delete the test-only seams and dead production paths the batch unlocks instead of preserving aliases, move a retained regression to its canonical owner, and consolidate repeated assertions into one contract. Add no replacement test that restates the implementation. Leave an uncertain candidate in the report rather than converting it into cleanup.

## Proof

Run the owner and sibling suites and every runner that consumes their output. For each deleted test, make one deliberate mutation of the production owner, confirm the keeper goes red, and revert the mutation. Report production and test line counts separately, the retained false positives with their reason, and the candidates left for a later batch.
