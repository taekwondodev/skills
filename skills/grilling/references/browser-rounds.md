# Browser rounds

`lavagna` shows a grilling round as a page in the user's browser and blocks until the user sends one feedback batch. It serves only the grilling phase; other questions stay in the terminal.

## Opt-in

`lavagna check` passes when the environment binds a conversation identity. A harness that binds none opts in when its configuration exports `LAVAGNA_SESSION`, one stable value per conversation. Leave the variable to that configuration rather than setting it to pass the check.

`lavagna round` waits for feedback until interrupted, so run every round with no timeout. Where the shell tool applies a timeout by default, turn it off explicitly. If the tool cannot run the call without a timeout, use terminal questions instead.

## Rounds

Before the first round of a conversation, run `lavagna round --help` for the minimal authoring contract. Load `lavagna round --help grammar` only when the round needs syntax beyond it.

- Text-only round: pipe `round.md` into `lavagna round` through one heredoc in a single shell call.
- Richer round (SVG, images, `.js` or `.css` files): write `DIR/round.md` and its files in a fresh directory under `$TMPDIR`, never inside the checkout, then run `lavagna round DIR`.
- Unchanged content, new decisions: use `lavagna round --reuse rN` with decisions-only stdin. It reuses the earlier content snapshot, not its questions or choices. When content changes, submit a new complete round.

Each round carries every independent frontier decision under `# Decidere`. A decision that depends on another waits for a later round. Option order and phrasing follow User questions in `SKILL.md`. Explain before asking: `# Capire` comes first, `# Confrontare` follows when alternatives must be weighed.

Stdout is one JSON outcome; its `lavagna` field names the outcome. Operational URL/status goes to stderr.

For `feedback` with `deferred:true`, fetch `lavagna feedback SUBMISSION --all` using the returned `submission` before updating the design tree or closing. Read the complete batch so no objection is missed; counts are not decisions. Retrieval errors stop advancement, never imply empty feedback. For both inline and retrieved batches, omitted choices are not approval.

- `feedback`: read all comments and every path in `images`, then record `choices` in the design tree, investigate facts the comments raise, and treat a comment that corrects an assumption as a frontier change. Recompute the frontier, then present the next browser round without waiting for another user request to continue. Put answers to comments and explanation-only followups in the next browser round alongside any remaining decisions. When no decisions remain, proceed directly to the confirmation round.
- `invalid` for content or bounds: fix the round from the line-numbered errors and rerun it. For usage or identity errors, report them in the terminal as for `error`.
- `error` or `busy`: report it in the terminal and start no new round on your own initiative.
- No outcome object: stop and report the interruption without assuming its cause. Respond to any available user message; otherwise wait for the user to resume. The next round returns to the browser unless the user asks to stay in the terminal.

## Completion

When the frontier is empty, present a confirmation round: `# Capire` lists the decisions with their decisive evidence, the rejected alternatives, and the unresolved risks; `# Decidere` holds one confirm-or-correct question.

The confirmation is clean when the user confirms and no comment reopens or changes a decision. Otherwise handle the batch as `feedback` and continue the loop. After a clean confirmation and reading all retained feedback and images, run `lavagna close`; it ends the browser phase and directs a connected page back to the terminal. Until then, keep the interaction in the browser unless an error or interruption requires the recovery described above, or the user explicitly asks to leave it.

`close` deletes retained phase content, feedback and images, not source round directories. Conversation data is swept after one day of inactivity, skipping live calls. The close result's `page` is `cleaned` only when a connected page acknowledges cleanup, `unconfirmed` when the close event was delivered without acknowledgment, or `not-connected` when no page connected. Local deletion still occurs without acknowledgment; none of these statuses proves other offline copies were erased.

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
