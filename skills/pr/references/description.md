# PR description

Help the reviewer understand the outcome, changed behavior, material risks, and evidence. Follow the required repository template and retain human-authored content and required checklists. Use the shape below where the template leaves room; omit empty optional sections.

## First read

### Why the change

Lead with the problem and the observable result. Explain what someone can now do, or what no longer goes wrong, before naming implementation machinery.

### Change outline

Use the most useful visual below to explain the changed behavior, adding the context needed to interpret it. Include implementation decisions that help the reviewer navigate the diff.

### Reviewer attention

Keep merge-relevant risks, compatibility constraints, migrations, accepted limitations, and verification gaps outside collapsed sections. Link supporting detail while keeping the warning visible.

### Verification

State what was exercised and its result, with commands or retrievable evidence. Separate local tests from remote CI. Name required checks that failed, remain pending, or were not run, including the reason. Keep the result visible; disclose extended logs on demand.

## Choose a useful visual

| Change to explain | Prefer |
| --- | --- |
| Visible UI or terminal output | Real before/after screenshots with comparable state and framing |
| Interaction or timing | A short recording of the relevant action and outcome |
| Flow, ownership, or state transitions | A focused Mermaid diagram rendered natively by GitHub |
| A small, straightforward fix | A text-only explanation or focused diff when that is clearer |

Choose a visual that answers a specific review question and replaces redundant prose. Ground diagrams in the actual diff, using domain labels and accurate relationships. Label conceptual sketches; captured runtime evidence must come from an actual run. Report unavailable captures as verification gaps where they matter.

Give images descriptive alt text and recordings a caption. Host media at destinations accessible to the intended reviewers and consistent with repository privacy. Preview rendering and check access before publication; report anything that could not be verified.

## Details on demand

Link to the relevant ADR, issue discussion, source location, or verification artifact. Put secondary explanations and extended evidence in labeled `<details>` sections when they belong in the PR itself. Retain outcomes and unresolved decisions that affect this review; keep material warnings in the first read.

## Reader check

Read the draft as someone unfamiliar with the work, before expanding details:

- Can they explain why the change matters and what behaves differently?
- Does each visual answer a useful question, with enough context to interpret it?
- Can they identify material risks and distinguish verified behavior from pending or missing evidence?
- Do links and expandable details help investigate those questions?

Resolve unclear answers by supplying missing context and removing competing detail.
