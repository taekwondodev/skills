---
name: retro
description: Conduct a retrospective on a coding session.
disable-model-invocation: true
---

# Retro

Run a **retrospective** on one coding session. The result is a ranked list of candidate improvements to the agent's **environment**: the project context, checks, docs, skills, and tools that future runs inherit.

## Steps

1. Read the [authoring reference](../writing-for-agents/references/authoring.md) of `writing-for-agents` for the terms used below: context pointer, information hierarchy, no-op.

2. Read the primary sources for the session the user names, defaulting to the current one. For an earlier session, retrieve the transcript through the available session-history capability or the harness's session logs on this machine. If it cannot be retrieved, state the gap and ask the user for its location. Completion: the complete session was read, including its tool calls, failures, and the user's corrections.

3. Hunt candidates in every category below. Tie each candidate to the session moment that exposed it and name where its change lands. Check it against the current environment: a pointer, check, or rule that already exists but sits unwired, silently broken, or ignored is the finding, not a reinvention. Completion: every category has a candidate with session evidence or an explicit "nothing found".

4. Present the candidates in order of severity, each with its category, session evidence, and proposed change. Stop there: an accepted candidate becomes its own task.

## Categories

- **Navigation**: how easily did the agent find the right files? Are there hidden dependencies between files? Would a **context pointer** make them easier to find? _Use when_ the session took a long time to find a piece of information.
- **Automated checks**: could an automated check have caught an error the agent made? Linting, typing, tests, filesystem linters? Read the repository's own check commands first: its build-tool or task-runner scripts, its hook configuration, its CI workflow, and the verification gates in `docs/agents/delivery.md` when that file exists. A repository with no **guardrail** (no pre-commit hook and no CI job running its lint, typecheck, or test command) is itself a finding: an unlinted repository is a standing missed opportunity, not a neutral default. _Use when_ the agent made a mistake an automated check could have caught, or the repository has no guardrail at all.
- **Coding standards**: should review enforce a new rule? Should an existing rule be removed or clarified? Classify the violation first. A **mechanical** one (a fixed syntactic pattern, a banned API, an import shape, a file-location rule) gets a deterministic check: choose its mechanism through [Encode Lessons in Structure](../principle-encode-lessons-in-structure/SKILL.md) and name the tool, rule, and configuration file. A genuine **judgement call** (cross-file consistency, "matches the surrounding style", anything no guardrail could ever substitute for) gets a rule in the review-time conventions. _Use when_ review failed to catch a mistake.
- **Project context**: are there steering instructions that belong in a deterministic check or in the review-time conventions instead? _Use when_ a project context file is particularly large, in the repository or in the user's global agent instructions.
- **Tool economy**: did the agent make expensive tool calls that could be streamlined? Is any custom tooling (CLIs, MCP servers) particularly token-inefficient? _Use when_ the agent made an expensive tool call.
- **No-ops**: look for instructions in project context files and skills that fail the authoring reference's no-op test. _Use when_ those files are large and unwieldy.
- **Information access**: look for opportunities to increase the agent's access to information: teeing dev server logs to a file, read-only access to third-party services. _Use when_ a crucial piece of information was not available to the agent.

## Where instructions land

**Review-time conventions** are the project conventions that review reads. Implementation works under the most context pressure: it explores, writes code, and debugs failures. Review works under the least: it receives a diff. Review therefore enforces coding conventions, and they stay out of the implementing agent's always-loaded context. When a project keeps no such conventions, the candidate proposes where to start them.

Any other instruction lands in a project context file, a doc behind a context pointer, or a skill. The authoring reference's information hierarchy selects among them. Extend an existing document before creating a new one.

## Agent result

For an agent-facing return, load [evidence/1](../investigation/references/result-contract.md). Order the findings by severity. Each claim names the candidate's category and proposed change, and its evidence locates the session moment.
