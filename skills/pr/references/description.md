# PR description

Help the reviewer understand the outcome, changed behavior, material risks, and evidence at a glance. Follow the required repository template and retain human-authored content and required checklists. Treat the sections below as guidance, not mandatory headings; omit empty optional sections.

## First read

### Why the change

Lead with a brief summary of the problem and the observable result. Explain what someone can now do, or what no longer goes wrong, before naming implementation machinery.

### Change outline

Summarize the changed behavior. Use a visual when it explains the behavior more clearly than prose. For broad changes, provide a short linked review path so the reviewer knows where to start.

### Reviewer attention

Group merge-relevant risks, compatibility constraints, migrations, accepted limitations, and verification gaps outside collapsed sections. State their consequences; link supporting detail while keeping the warning visible.

### Verification

State what was exercised and its result, with commands or retrievable evidence. Separate local tests from remote CI. Name required checks that failed, remain pending, or were not run, including the reason. Keep the result visible; disclose extended logs on demand.

## Choose a useful visual

| Change to explain | Prefer |
| --- | --- |
| Visible UI or terminal output | Real before/after screenshots with comparable state and framing |
| Interaction or timing | A short recording of the relevant action and outcome |
| Actions and their outcomes, or a compact before/after comparison | A short table |
| Flow, ownership, or state transitions | A focused Mermaid diagram rendered natively by GitHub |
| A small, straightforward fix | A text-only explanation or focused diff when that is clearer |

Choose a visual that answers a specific review question and replaces redundant prose. Keep its level of detail consistent. Ground diagrams in the actual diff, using concise domain labels and accurate relationships. Label conceptual sketches; captured runtime evidence must come from an actual run. Report unavailable captures as verification gaps where they matter.

Give images descriptive alt text and recordings a caption. Host media at destinations accessible to the intended reviewers and consistent with repository privacy. Preview rendering and check access before publication; report anything that could not be verified.

## Details on demand

Link to the relevant ADR, issue discussion, source location, or verification artifact. Put secondary explanations and extended evidence in labeled `<details>` sections when they belong in the PR itself. Retain outcomes and unresolved decisions that affect this review; keep material warnings in the first read.

## Reader check

Read the draft as someone unfamiliar with the work, before expanding details:

- Can they explain why the change matters and what behaves differently by skimming the opening and outline?
- Is each visual easy to read, with a clear purpose and enough context to interpret it?
- Can they find material risks and distinguish verified behavior from pending or missing evidence without expanding details?
- For a broad change, is it clear where to start reviewing and where to find the supporting rationale and evidence?

Resolve unclear answers by supplying missing context and removing competing or repeated detail.
