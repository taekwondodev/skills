# Mechanical checks

Read project guidance and configuration to identify applicable checks and what they enforce.

- Run checks relevant to the changed unit before review. Reuse results only while the checked code, inputs, configuration, and toolchain remain unchanged.
- Pass commands, outcomes, and coverage gaps to reviewers. Keep full logs retrievable rather than copying them into review context.
- Standards reviewers skip only mechanical rules covered by current evidence, then inspect uncovered rules and relevant check-configuration changes. Static checks complement behavior tests and semantic review.

For recurring mechanical review findings, use [encode lessons in structure](../../principle-encode-lessons-in-structure/SKILL.md) to decide whether a project check should enforce the rule. Keep tooling changes within the approved scope.
