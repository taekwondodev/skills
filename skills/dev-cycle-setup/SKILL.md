---
name: dev-cycle-setup
description: Configure portable project context, tracking, delivery, and domain documentation for dev-cycle.
disable-model-invocation: true
---

# Dev Cycle Setup

Scaffold the per-repo configuration that `/capture-issue`, `/to-spec`, `/to-tickets`, `/implement`, and `/wayfinder` assume:

- **Issue tracker**: where issues and tickets live
- **Issue labels**: the strings used for the canonical category, state, and workflow-marker roles
- **Delivery**: the default direct or PR route and its target refs
- **Domain docs**: where `CONTEXT.md` and ADRs live, and the consumer rules for reading them
- **Project context**: one portable `AGENTS.md` at the repo root, produced from whatever agent-rule sources already exist

Read `writing-for-agents` before drafting the generated project context, domain, and tracker documents. Its general writing rules govern those documents; this skill adds only setup-specific structure.

This is a prompt-driven skill, not a deterministic script. Explore, present what you found, confirm with the user, then write.

## Agent result

For an agent-facing return, load [delivery/1](../implement/references/result-contract.md). Reference the configuration and domain artifacts actually written and their verification.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- `git remote -v`: is this a GitHub repo? Which one?
- Current branch, remote default branch, contribution rules, branch protection, PR templates, and any existing `docs/agents/delivery.md`: which delivery choices are already explicit? Inspect accessible configuration; report unavailable rules rather than infer permission from missing evidence.
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repo root
- `docs/adr/` and any `src/*/docs/adr/` directories
- `docs/agents/`: does this skill's prior output already exist?
- Monorepo signals: a workspace manifest, or a populated `packages/*`/`crates/*` with its own `src/`. Present only in a genuinely large multi-package repo; their absence means single-context, which is almost every repo.
- **Existing agent-rule sources**, searched across Git-tracked files at the repo root and at the conventional per-agent config directories, plus an explicit existence check for each known conventional path even when Git ignores it: `AGENTS.md` and `CLAUDE.md` at the repo root; `CLAUDE.md` in `.claude/`; `GEMINI.md` in `.gemini/`; `.hermes.md` and `HERMES.md` in `.hermes/`; `.cursorrules` and rules under `.cursor/rules/` only when they carry no path-scoped frontmatter; `.github/copilot-instructions.md`. Record each hit's path and read its full content. Treat a hit as repo-global only when its location gives it repository-wide scope. A rule file nested inside a package, subproject, or other subdirectory whose scope is that subtree only is directory-scoped: report it in the findings but exclude it from the merge, because broadening it to root would change its meaning. Never treat `AGENTS.override.md` as a merge source, and exclude every path-specific instruction file (any rules file whose frontmatter, name, or declared scope applies to selected paths rather than the whole repository). For each repo-global source found, check whether it already carries a `## Dev cycle` section; if it carries domain terms or architectural decisions beyond operational rules and pointers, flag it as a migration candidate for Section D.

For the known conventional paths above, check the filesystem directly even when the path is ignored by Git. Use tracked-file search only for additional recursive discovery, so dependencies, build output, and vendored copies are never treated as project rules.

### 2. Present findings and ask

Summarise what's present and what's missing. Then take the sections in order, one section and one answer at a time.

Lead each section with the recommended answer so the user can accept it in a word. Give a one-line explainer only when the choice genuinely branches; skip the section entirely when exploration already settled it.

**Section A0: Existing agent rules.** Only runs when Explore found at least one source.

> Explainer: the dev-cycle expects one portable `AGENTS.md` at the repo root. Whatever agent wrote the existing rule files, they are merged into it; the originals remain untouched.

Take these steps before the other sections, because their output feeds Sections B through D:

1. Classify each repo-global source's content using Section D's placement rules: repository-wide rules, domain terms, and decision rationale.
2. Merge the operational content: deduplicate instructions that say the same thing in equivalent words, keep genuinely distinct rules side by side, and normalize Claude-specific references (`CLAUDE.md`, "Claude") to harness-neutral wording naming `AGENTS.md` or "the agent".
3. Surface every contradiction, whether it sits between two sources or inside one source (an old rule contradicting a newer one in the same file). Never pick by filename precedence or position. Show both excerpts and ask one focused question per conflict; retain the resolution in the content's selected authoritative home.
4. Apply Section D's placement rules before moving content. Keep concise repository-wide rules in `AGENTS.md`; route glossary entries to `CONTEXT.md` and only qualifying decisions to ADRs. Use conditional pointers for content moved or already recorded elsewhere.
5. Draft `AGENTS.md` with concise repository-wide rules and a `## Dev cycle` block per the template below. Add conditional pointers only to existing or justified new targets.
6. Carry the draft into Confirm and edit below; resolve its targets before writing it.

**Section A: Issue tracker.**

> Explainer: this is where issues and tickets live for this repo. `/capture-issue`, `/to-tickets`, `/to-spec`, and `/wayfinder` read from and write to it.

Use GitHub Issues for every project. If the current directory is already a Git repository, proceed using its GitHub remote when available. Otherwise, create a private GitHub repository with `gh repo create --private`, clone or initialize it as needed, and then proceed with GitHub Issues.

Record the choice in `docs/agents/issue-tracker.md`, seeded from [issue-tracker-github.md](./issue-tracker-github.md).

**Section B: Issue-label vocabulary.**

> Do you want to keep the default issue labels? (recommended: **yes**)

The defaults are the two canonical issue-state labels, each label string equal to its name: `needs-grilling` and `ready-for-agent`. On **yes**, write them as-is from [triage-labels.md](./triage-labels.md). Only collect the overrides if the user says no. Usually this is because their tracker already uses other names.

`needs-grilling` is the initial issue state for quick issues intentionally created before a grilling session. It is replaced by `ready-for-agent` when the complete spec is published.

**Section C: Domain docs.** Default to the **single-context** layout: `CONTEXT.md` + `docs/adr/` at the repo root. Record this convention without asking; create content files only when a resolved term or a decision passing Section D's gate needs one.

Offer **multi-context** only when exploration found monorepo signals: a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files. Then confirm which layout they want.

**Section C1: Delivery.** Preserve an existing explicit delivery policy. Otherwise ask for the repository default: `direct` or `pr`. Present discovered integration and PR base refs and ask only about unresolved targets.

Draft `docs/agents/delivery.md` from [delivery.md](./delivery.md), replacing its placeholders with the chosen mode, integration target, PR base, source-remote policy, and required verification gates.

**Section D: Existing rule-file content.** Only runs if Explore flagged a migration candidate; skip entirely otherwise.

Section D runs when a flagged source contains a domain term or a possible decision record. Classify it before creating files. Reuse an existing authoritative target where sufficient, and create only missing qualifying content. Every pointer in the draft must resolve to an existing or newly written target.

> Explainer: keep concise rules needed across repository work in `AGENTS.md`. Put glossary definitions and task-specific rationale behind conditional pointers, reusing existing records rather than copying them.

Read each flagged source in full and sort each section into one of three buckets:

- **Repository-wide rule**: keep the concise instruction and necessary reason in `AGENTS.md`. Task-specific procedures and setup details belong behind conditional pointers.
- **Decision rationale**: read [ADR-FORMAT.md](../domain-modeling/ADR-FORMAT.md) and apply its placement, necessity, and completion checks to select an existing or new record.
- **Domain term**: a project-specific concept given a definition. Becomes a `CONTEXT.md` entry per CONTEXT-FORMAT.md.

For remaining content, apply `writing-for-agents`' information hierarchy to select its home and reading trigger.

### 3. Confirm and edit

Show the user a draft of:

- The generated `AGENTS.md`
- The contents of `docs/agents/issue-tracker.md`, `docs/agents/domain.md`, `docs/agents/triage-labels.md`, and `docs/agents/delivery.md`
- If Section D ran: each section's selected home, reused targets, and the content of any justified new records or glossary entries
- If any conflicts were found in Section A0: each conflict, both excerpts, and the user's recorded decision

Let them edit before writing.

### 4. Write

Write `AGENTS.md` at the repo root. If an `AGENTS.md` already existed there, preserve its operational content in the merge. Do not modify any other agent-rule source file; the originals remain byte-for-byte unchanged.

If Section D ran: resolve reused targets and write any justified new ADR files or `CONTEXT.md` entries before composing `AGENTS.md`. Keep concise repository-wide rules inline and use conditional pointers for disclosed content, per `writing-for-agents`. Verify every pointer's target and reading trigger.

The block contains pointers only, never the content itself:

```markdown
## Dev cycle

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Issue labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Delivery

[default direct or PR route]. Before implementation or delivery, read `docs/agents/delivery.md` for route and target defaults.

### Domain docs

[one-line summary of layout: "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

Then write the docs files using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md): GitHub issue tracker, including the operations `/wayfinder` needs
- [triage-labels.md](./triage-labels.md): label mapping
- [delivery.md](./delivery.md): delivery defaults and verification gates
- [domain.md](./domain.md): domain doc consumer rules + layout

For a human-facing return, tell the user the base setup is complete and which skills will now read from these files. Mention they can edit `docs/agents/*.md` and `AGENTS.md` directly later. For an agent-facing return, use the receipt instead. Re-running this skill is only necessary if they want to switch issue trackers, redo the context merge, or restart from scratch.
