# ADR Format

An ADR preserves a decision's non-obvious rationale for future changes.

## Before creating a record

Choose the content's home before its format:

- Keep concise repository-wide rules in `AGENTS.md` and task-specific rationale behind conditional pointers.
- Reuse an existing document, issue, spec, or ADR when it already records the decision and rationale. Link the exact section or comment that a future reader needs.
- Keep enduring decisions in the ADR, implementation details in code or operational documentation, and execution evidence in task records.

Offer a new ADR only when a separate record is still needed and all three are true:

1. **Hard to reverse**: changing the decision has meaningful cost.
2. **Surprising without context**: a future maintainer could reasonably undo it without knowing why it exists.
3. **A real trade-off**: viable alternatives existed and were rejected for specific reasons.

Name the future change that needs this rationale. If the gate fails, retain any needed content in its appropriate existing owner.

## Write the smallest sufficient decision

```md
# {Short title of the decision}

{1-3 sentences: the decision, the non-obvious reason for it, and any essential constraint or accepted consequence.}
```

Start with that paragraph. Expand only for an alternative, constraint, or consequence that would change a future modification. Preserve essential boundaries regardless of length. Add headings, status, or supersession information only where needed to interpret the decision.

Link the exact retrievable source when acceptance or rationale depends on it. Update the ADR when the decision, rationale, or enduring constraints change.

## Placement

Follow the repository's existing convention. Otherwise use `docs/adr/` and sequential names such as `0001-slug.md`; create the directory only when the first record passes the gate. Scan existing numbers before choosing the next one.

Add a conditional pointer from the relevant project context naming the change that requires reading this decision.

## Completion

The current decision, its non-obvious reason, and its reading trigger are explicit. Every paragraph informs a future modification or preserves an essential boundary. An existing sufficient record or a concise project rule completes the task without a new ADR.
