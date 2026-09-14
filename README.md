# Skills

My collection of agent skills, grouped by how I use them. Each link opens the skill’s instructions.

## Workflow and repository setup

| Skill | Description |
| --- | --- |
| [dev-cycle](skills/dev-cycle/SKILL.md) | Route development tasks through the right skills and verification steps. |
| [dev-cycle-setup](skills/dev-cycle-setup/SKILL.md) | Configure project instructions, issue tracking, labels, and domain docs. |
| [menu](skills/menu/SKILL.md) | Find skills by name, category, or intended outcome. |

## Planning and requirements

| Skill | Description |
| --- | --- |
| [capture-issue](skills/capture-issue/SKILL.md) | Record an idea as an issue without expanding its scope. |
| [grilling](skills/grilling/SKILL.md) | Resolve open decisions through evidence and focused questions. |
| [grill-with-docs](skills/grill-with-docs/SKILL.md) | Clarify a design while recording its glossary and architectural decisions. |
| [to-spec](skills/to-spec/SKILL.md) | Turn an agreed discussion into a specification in the issue tracker. |
| [to-tickets](skills/to-tickets/SKILL.md) | Split an approved specification into implementation tickets with dependencies. |
| [wayfinder](skills/wayfinder/SKILL.md) | Map large, uncertain projects into decisions that can be resolved incrementally. |

## Architecture and exploration

| Skill | Description |
| --- | --- |
| [architect](skills/architect/SKILL.md) | Design module boundaries, ownership, and interfaces before implementation. |
| [domain-modeling](skills/domain-modeling/SKILL.md) | Define domain terminology, sharpen models, and record architectural decisions. |
| [arena](skills/arena/SKILL.md) | Compare independent candidate solutions and combine their strongest ideas. |
| [prototype](skills/prototype/SKILL.md) | Build disposable experiments to resolve technical or behavioral choices. |

## Implementation, testing, and review

| Skill | Description |
| --- | --- |
| [implement](skills/implement/SKILL.md) | Implement an agreed change against its specification and acceptance criteria. |
| [coding-standards](skills/coding-standards/SKILL.md) | Apply coding conventions, type-driven design, and dependency guidance. |
| [testing](skills/testing/SKILL.md) | Choose test boundaries, structure, and expected behavior. |
| [code-review](skills/code-review/SKILL.md) | Review changes for coding standards, specification compliance, and hidden risks. |
| [interrogate](skills/interrogate/SKILL.md) | Challenge designs and diffs through adversarial review. |
| [blast-radius](skills/blast-radius/SKILL.md) | Trace affected callers and contracts beyond the immediate diff. |
| [eval](skills/eval/SKILL.md) | Evaluate skill routing and agent behavior against fixed scenarios. |

## Git and delivery

| Skill | Description |
| --- | --- |
| [commit](skills/commit/SKILL.md) | Create Conventional Commits, with an optional push. |

## Investigation and performance

| Skill | Description |
| --- | --- |
| [how](skills/how/SKILL.md) | Explain a subsystem by tracing its flow, ownership, and boundaries. |
| [why](skills/why/SKILL.md) | Recover the evidence behind past code and architecture decisions. |
| [investigation](skills/investigation/SKILL.md) | Answer observable questions before proposing changes. |
| [runtime-forensics](skills/runtime-forensics/SKILL.md) | Diagnose live symptoms using captured signals and source mapping. |
| [trace-forensics](skills/trace-forensics/SKILL.md) | Analyze existing profiles, traces, heap snapshots, and spindumps. |
| [perf-issue](skills/perf-issue/SKILL.md) | Diagnose and improve a specific, measured performance problem. |
| [hillclimb](skills/hillclimb/SKILL.md) | Improve a metric through repeated, measured keep-or-revert experiments. |

## Session continuity and progress tracking

| Skill | Description |
| --- | --- |
| [handoff](skills/handoff/SKILL.md) | Save task context and a resume prompt for the next session. |
| [pause-safely](skills/pause-safely/SKILL.md) | Suspend work with enough evidence to resume safely. |
| [session-pickup](skills/session-pickup/SKILL.md) | Resume prior work after reconciling its handoff with live repository state. |
| [show-me-your-work](skills/show-me-your-work/SKILL.md) | Record decisions, evidence, and results during long-running work. |

## Documentation and learning

| Skill | Description |
| --- | --- |
| [writing-for-agents](skills/writing-for-agents/SKILL.md) | Write clear skills, project instructions, specifications, and agent briefs. |
| [reflect](skills/reflect/SKILL.md) | Turn lessons from completed work into proposed skill improvements. |

## Engineering principles

| Skill | Description |
| --- | --- |
| [principle-boundary-discipline](skills/principle-boundary-discipline/SKILL.md) | Validate at system boundaries and keep business logic independent of adapters. |
| [principle-build-the-lever](skills/principle-build-the-lever/SKILL.md) | Build reusable tools that perform or verify non-trivial work. |
| [principle-encode-lessons-in-structure](skills/principle-encode-lessons-in-structure/SKILL.md) | Turn recurring corrections into checks, metadata, or scripts. |
| [principle-exhaust-the-design-space](skills/principle-exhaust-the-design-space/SKILL.md) | Compare distinct prototypes before committing to a novel design. |
| [principle-experience-first](skills/principle-experience-first/SKILL.md) | Favor a polished user experience over implementation convenience. |
| [principle-fix-root-causes](skills/principle-fix-root-causes/SKILL.md) | Reproduce problems and fix their causes rather than masking symptoms. |
| [principle-foundational-thinking](skills/principle-foundational-thinking/SKILL.md) | Choose core types and data structures before writing logic. |
| [principle-guard-the-context-window](skills/principle-guard-the-context-window/SKILL.md) | Keep context focused and isolate large intermediate outputs. |
| [principle-laziness-protocol](skills/principle-laziness-protocol/SKILL.md) | Prefer deletion and the smallest change that solves the problem. |
| [principle-make-operations-idempotent](skills/principle-make-operations-idempotent/SKILL.md) | Make operations converge safely across retries and partial failures. |
| [principle-migrate-callers-then-delete-legacy-apis](skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | Migrate internal callers and remove obsolete APIs in the same change. |
| [principle-minimize-reader-load](skills/principle-minimize-reader-load/SKILL.md) | Reduce indirection and the hidden state readers must keep in mind. |
| [principle-model-the-domain](skills/principle-model-the-domain/SKILL.md) | Represent domain rules with explicit structures instead of scattered conditions. |
| [principle-never-block-on-the-human](skills/principle-never-block-on-the-human/SKILL.md) | Proceed on observable facts while preserving human-owned decisions. |
| [principle-outcome-oriented-execution](skills/principle-outcome-oriented-execution/SKILL.md) | Optimize migrations for a verified end state, not temporary compatibility code. |
| [principle-prove-it-works](skills/principle-prove-it-works/SKILL.md) | Verify real artifacts and behavior before declaring success. |
| [principle-redesign-from-first-principles](skills/principle-redesign-from-first-principles/SKILL.md) | Integrate new requirements as foundational parts of the design. |
| [principle-separate-before-serializing-shared-state](skills/principle-separate-before-serializing-shared-state/SKILL.md) | Eliminate shared mutable state before adding synchronization. |
| [principle-sequence-verifiable-units](skills/principle-sequence-verifiable-units/SKILL.md) | Break work into small units that each end in a verified state. |
| [principle-subtract-before-you-add](skills/principle-subtract-before-you-add/SKILL.md) | Remove unnecessary complexity before building on top of it. |
| [principle-type-system-discipline](skills/principle-type-system-discipline/SKILL.md) | Use types to rule out invalid states and enforce domain contracts. |
