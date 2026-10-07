# Browser rounds

`lavagna` keeps a grilling phase on one browser page. Each `lavagna round` call applies changes to its questions and blocks until the user sends one feedback batch. Other questions stay in the terminal.

## 1. Opt-in

`lavagna check` passes when the environment binds a conversation identity. A harness that binds none opts in when its configuration exports `LAVAGNA_SESSION`, one stable value per conversation. Leave the variable to that configuration rather than setting it to pass the check.

Run every `lavagna round` with no timeout. Where the shell tool applies a timeout by default, turn it off explicitly. If the tool cannot run the call without a timeout, use terminal questions instead.

## 2. One call per turn

Make one blocking `lavagna round` call per agent turn. The first call carries `::: phase TITLE`, every independent frontier question, and every known dependent decision as a planned question: a bare title with an id and `after` naming its prerequisites. Close the phase element with `:::`. Planned questions get their bodies once their prerequisites are settled.

Later calls carry only changes: replies, settlements, replacement questions or new questions. Lavagna retains the questions and discussions; an unchanged question needs no input. Keep the design tree in step with this question ledger.

## 3. Writing a question

Before the first call, run `lavagna round --help` for the minimal authoring contract. Load `lavagna round --help grammar` only when the question needs syntax beyond it. The command's output owns the grammar.

- Start each question with `# Title {id="stable-id"}`; add `after="prerequisite-id"` for a dependent decision. Reuse the id when replacing that question.
- Explain before asking: `## Capire`, then `## Confrontare`, then `## Decidere`. Capire is 01, Confrontare is 02, and the page owns the decision controls in 03.
- Give a recommended option and explain why it fits. Write one indented `=>` effect line per option, so the preview explains what changes. Option order and phrasing follow [User questions](../SKILL.md#user-questions).
- For text-only input, pipe the call through one heredoc into `lavagna round` in a single shell call.
- For resources, write `DIR/round.md` and files under `DIR/<question-id>/` in a fresh directory under `$TMPDIR`, outside the checkout, then run `lavagna round DIR`. Reference resources as `<question-id>/file`; each question owns its scripts and styles.

Keep observations in `info` or observed `evidence`, proposals in `proposal`, unverified assumptions in unverified `evidence`, and scope limits in `boundary`. Before sending, every open question has enough explanation, concrete options and a recommendation to decide without reconstructing the agent's investigation.

## 4. Choosing the representation

State the open question in one sentence, then pick the smallest representation that answers it. Use one primary representation per question; add another only for a different unresolved property. Put a short `why` block beside it saying what to inspect or try and why it helps decide.

| Question to resolve | Use |
| --- | --- |
| What is the subject, and why does it matter? | Prose and `info` in Capire. |
| Which alternative is better? | One diagram in 01 with per-option variants that 02 redraws, plus each option's `=>` line. Never a comparison table. |
| Order, causality or ownership? | `sequence` or `flow`, with the fault marked `!n`; combine related diagrams into one. |
| What does a measurement show? | `bars` with observed values, source, units and uncertainty, not a table. |
| Can the user discover and complete an interaction? | A bare screen with no phone or computer frame, following `data-option`; lavagna fits wide screens and supplies Expand. |
| What exactly changes in code? | `excerpt` citing inspected source, with problem lines marked like `45!1`. |
| Settled decisions and recap | The confirmation's `::: recap`; author no tables elsewhere in the phase. |

For a UI prototype, use the application's source and visual vocabulary when available. Label hypothetical data and behavior as demonstrative, in the page and design tree. Build only the path and states needed, with one concrete exploration prompt. Controls act only inside the prototype, never on a real account, repository, filesystem or runtime. A mockup proves no runtime behavior.

## 5. Reading a batch

Read stdout as the JSON outcome, identified by its `lavagna` field, and stderr as operational status. For `feedback` with `deferred:true`, run `lavagna feedback SUBMISSION --all` using the returned `submission`. Read the complete batch before acting; stop on retrieval errors.

For each entry in `questions`, read its `choice` or free-text `answer`, all `messages`, and every path in `images`. Read the Overview's messages and images too. An omitted answer is unresolved, not approval.

Record answers in the design tree, investigate facts raised by messages, and recompute the frontier when feedback corrects an assumption. Respond with `::: reply ID` in that question's thread; use `::: reply` without an id for the Overview. Close each element with `:::`. An explanation needs only a reply; send a whole replacement question only when its proposal changes.

A message on a settled question may need only a reply. If it changes the proposal, replace the question with the same id to reopen it; for a plain change to an existing option, use `::: settled ID OTHER` with the new reason. Read all feedback before deciding which applies.

After processing the batch, make the next browser call without waiting for another user request. If discussion continues, send replies and any changed questions in the current round; if the frontier can advance, follow the next section. When it is empty, proceed to confirmation.

## 6. Advancing

Settle answered questions when opening the next round or the confirmation, not immediately after receiving the answer. This keeps choices editable while discussion continues and avoids a separate call.

In that same call, send `::: settled ID` with the reason in its body, then the complete new questions whose prerequisites are settled. For a free-text answer, put your interpretation in the settlement reason, which the Overview shows. If the answer is ambiguous, ask in its thread instead of settling it.

A new question with a body opens the next round; unsettled questions move there automatically. Fill planned questions using their existing ids. Never resend an unchanged question, including one still awaiting an answer. The call is ready when its settlements justify the new frontier and it contains only changes.

## 7. Confirmation

When the frontier is empty, send one confirm-or-correct question. Include `::: recap` (closed with `:::`) in its Capire and the open risks in `::: evidence`; lavagna renders the decisions table after applying the same call's settlements. Use settlement reasons for rationale and decisive evidence; the recap supplies the rejected alternatives.

The confirmation is clean only when the user confirms with no messages in the batch and no screenshot changes or reopens a decision. Otherwise process the feedback and continue in the browser, revising the confirmation when needed.

After a clean confirmation and reading all retained feedback and images, run `lavagna close`. It ends the browser phase and directs a connected page back to the terminal. Retained content, feedback and images are deleted by close or swept after one day of inactivity; source directories remain. The close result's `page` means connected-page cleanup acknowledged (`cleaned`), acknowledgment missing (`unconfirmed`), or no page connected (`not-connected`); none proves offline copies were erased.

Completion: `lavagna close` returned `closed` after a clean confirmation. Then follow [Checkpoint and handoff](../SKILL.md#checkpoint-and-handoff).

## 8. Recovery

- `invalid` for content or bounds: fix the line-numbered errors and retry. The rejected call changes no questions. For usage or identity errors, report them in the terminal as for `error`.
- `error` or `busy`: report it in the terminal and start no new call on your own initiative.
- No outcome object: report the interruption without assuming its cause. Respond to an available user message; otherwise wait for the user to resume.

After an interruption, an empty call, `lavagna round < /dev/null`, resumes waiting without resending questions. Inspect the page's delivery state; a returned batch is not automatically resent. Keep later interaction in the browser unless the user asks to leave it.

If close, expiry or an upgrade cleared the phase, the old ids are no longer in the ledger: author a fresh first call with complete frontier questions and planned dependents instead. Resume only when the phase state and the next expected feedback are understood.
