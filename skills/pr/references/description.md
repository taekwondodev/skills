# PR description

Give the reviewer the outcome, the changed behavior, the risks, and the evidence at a glance. One primary visual carries the explanation; prose captions it. A repository template wins over the skeleton below: fit the slots into its sections. Omit empty optional sections.

## Skeleton

Fill the slots and delete every angle-bracket hint.

```markdown
## Why the change

<One or two sentences: the problem, then what someone can now do or what no longer goes wrong.>

## Change outline

<Primary visual from the capture table.>

<One-sentence caption naming the review question the visual answers.>

Start at `<file>`: <why first>. Then `<file>`: <what to check>.

## Reviewer attention

| Risk | Consequence | Guard | Where |
| --- | --- | --- | --- |
| <migration, compatibility limit, accepted limitation, or verification gap> | <what happens> | <what prevents or bounds it> | <file or link> |

## Verification

| Check | Result | Evidence |
| --- | --- | --- |
| <command or suite> | ✅ passed / ❌ failed / ⏳ pending / ➖ not run | <log, link, or reason> |
| Remote CI | <status> | <run link or "not checked"> |

<details><summary>Decisions and extended evidence</summary>

<ADR, issue discussion, review outcomes, long logs.>

</details>

<Refs #N or Closes #N, as resolved in the skill.>
```

## Capture before drafting

Capture the real artifact first; the capture is the visual. Draft the caption from it.

| Change surface | Capture |
| --- | --- |
| Command or log output | Run the command on base and on head; paste both verbatim in fenced blocks, or one unified diff of the two |
| Full-screen terminal UI | Drive the repository's terminal test harness and paste the final frame as a fenced text block |
| Graphical UI | Before/after screenshots with the same state and framing, with descriptive alt text |
| Interaction or timing | A short recording with a caption |
| Flow, ownership, or state transitions | A Mermaid diagram rendered natively by GitHub |
| Actions and outcomes, or a compact before/after | A short table |
| Small, straightforward fix | Text-only explanation or focused diff, stating why no visual |

Media hosting: the GitHub API cannot attach uploaded images to a PR body. Use the repository's documented media location when one exists; otherwise commit the image under the documentation tree on the head branch and link it, which enters commit scope and needs that authorization. Without a host reachable by every intended reviewer, the fenced text capture is the visual, and the missing image is a verification gap in Reviewer attention. Check rendering and reviewer access before publication.

## Mermaid rules

- One review question per diagram.
- At most 8 nodes.
- Node labels of at most 4 words; detail goes in the caption or a link.
- Labels are domain terms from the diff; edges are the actual relationships.
- Label a conceptual sketch as such; captured runtime evidence comes from an actual run.

## Reader check

Count:

- Words outside tables, diagrams, code blocks, and `<details>`: at most 150.
- Primary visual: present, or a stated text-only reason.
- Longest bullet list: at most 5 items.
- Every table: a header row and at most 5 columns.

Fix a failed count by moving detail into a table or `<details>` and deleting repeated text.
