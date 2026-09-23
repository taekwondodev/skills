# PR description

Use the repository template as the required structure and these sections where it leaves room. Retain human-authored content and required checklists; omit optional links or views that do not help the review.

## Why the change

One sentence explaining the problem and what the change enables.

## Special things to note

One to three bullets for migrations, compatibility constraints, deliberate omissions, surprising decisions, or reviewer warnings. Write `None.` when there are none.

## Change outline

Choose the smallest structural view that explains the implementation: changed types or contracts, shallow responsibility tree, component tree, call or data flow, or behavior pseudocode. A small straightforward fix may need only a short explanation. Do not turn this into a file-by-file changelog.

Use a focused `diff` block when an existing shape changes. Show the complete target shape when it is mostly new or omissions would obscure ownership.

Keep sketches grounded in the actual diff; label pseudocode as a sketch rather than executable code. Place each view beside the brief text it supports, and include only relevant views.

## Verification

State what was exercised and its result, with commands or retrievable evidence. Separate local tests from remote CI. Name required checks that failed, remain pending, or were not run, including the reason.
