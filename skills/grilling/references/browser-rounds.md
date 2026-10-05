# Browser rounds

`lavagna` shows a grilling round as a page in the user's browser and blocks until the user sends one feedback batch. It serves only the grilling phase; other questions stay in the terminal.

## Opt-in

`lavagna check` passes when the environment binds a conversation identity. A harness that binds none opts in when its configuration exports `LAVAGNA_SESSION`, one stable value per conversation. Leave the variable to that configuration rather than setting it to pass the check.

`lavagna round` waits for feedback until interrupted, so run every round with no timeout. Where the shell tool applies a timeout by default, turn it off explicitly. If the tool cannot run the call without a timeout, use terminal questions instead.

## Rounds

Before the first round of a conversation, run `lavagna round --help` for the `round.md` grammar and bounds; write every round to it.

- Text-only round: pipe `round.md` into `lavagna round` through one heredoc in a single shell call.
- Richer round (SVG, images, `.js` or `.css` files): write `DIR/round.md` and its files in a fresh directory under `$TMPDIR`, never inside the checkout, then run `lavagna round DIR`.

Each round carries every independent frontier decision under `# Decidere`. A decision that depends on another waits for a later round. Option order and phrasing follow User questions in `SKILL.md`. Explain before asking: `# Capire` comes first, `# Confrontare` follows when alternatives must be weighed.

The last stdout line is one JSON object; its `lavagna` field names the outcome.

- `feedback`: record `choices` in the design tree, read every path in `images`, investigate facts the comments raise, and treat a comment that corrects an assumption as a frontier change. Recompute the frontier, then present the next round.
- `invalid` for content or bounds: fix the round from the line-numbered errors and rerun it. For usage or identity errors, report them in the terminal as for `error`.
- `error` or `busy`: report it in the terminal and start no new round on your own initiative.
- No outcome line: stop and report the interruption without assuming its cause. Respond to any available user message; otherwise wait for the user to resume. The next round returns to the browser unless the user asks to stay in the terminal.

## Completion

When the frontier is empty, present a confirmation round: `# Capire` lists the decisions with their decisive evidence, the rejected alternatives, and the unresolved risks; `# Decidere` holds one confirm-or-correct question.

The confirmation is clean when the user confirms and no comment reopens or changes a decision. Only then run `lavagna close`; it ends the browser phase and the page sends the user back to the terminal. Otherwise handle the batch as `feedback` and continue the loop.

Completion criterion: `lavagna close` returned `closed` after a clean confirmation. Then follow [Checkpoint and handoff](../SKILL.md#checkpoint-and-handoff) for the caller's handoff.

## Choosing the representation

State the open question in one sentence, then pick the smallest representation that answers it. Use one primary representation per question; add a second only when it reveals a different unresolved property. Put a short `why` block beside it saying what to look at or try and why that helps decide.

| Question to resolve | Use | Choose something else when |
| --- | --- | --- |
| What is the subject, and why does it matter? | Prose and `info` blocks in `# Capire` | The uncertainty is spatial, relational, or interactive: add that module after the explanation. |
| Which alternative meets the same criteria better? | A table with identical row meanings for each alternative, plus a `proposal` block for the recommendation | The question is order, causality, or ownership. |
| What happens next, who owns it, what depends on what? | `steps` for a linear sequence; an SVG diagram for branching, state, or boundaries | A sentence answers it, or the user must try an interaction. |
| Can the user discover and complete this interaction? | A UI prototype in raw HTML with round `.js` and `.css` files | The decision is an implementation detail or a factual comparison. A mockup proves no runtime behavior. |
| What exactly changes in code or behavior? | `excerpt` blocks citing inspected source; show a proposed change beside a `proposal` block | The reader needs the system model first. |
| What does a measurement show? | An SVG chart, or a small table, of observed values with source, units, and uncertainty | No measurements exist. Never invent metrics. |
| None of these fits | Bounded custom HTML or SVG covering only the missing property | An existing module answers the question. |

Keep categories visibly separate: sourced observations as `info` or `evidence` items marked observed; proposals in `proposal` blocks, unapproved until the design tree records the decision; unverified assumptions as `evidence` items marked unverified; scope limits in `boundary` blocks.

### Prototype boundary

Use the real application's source and visual vocabulary when available. Label hypothetical examples and data as demonstrative, in the page and in the design tree. Build the smallest path and states the question needs, with one concrete exploration prompt. Prototype controls stay inside the prototype: no real account, repository, filesystem, or runtime action.
