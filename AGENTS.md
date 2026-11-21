## Dev cycle

### Issue tracker

Issues, specs, and tickets live in GitHub Issues. See `docs/agents/issue-tracker.md`.

### Issue labels

Use category, readiness, and activity labels, with one label per state dimension. See `docs/agents/triage-labels.md`.

### Delivery

Deliver directly to `origin/main`. Before implementation or delivery, read `docs/agents/delivery.md` for route and target defaults.

### Domain docs

Use the single-context layout. See `docs/agents/domain.md`.

## Install skills with stow

`skills/` is a stow package linked into `~/.agents/skills/`. Run from the repository root and never link skills by hand.

- **First use:** `mkdir -p ~/.agents/skills && stow -d . -t ~/.agents/skills skills`.
- **New or deleted skill:** add or remove `skills/<name>/`, then `stow -R -d . -t ~/.agents/skills skills`.

## Test a skill change blind

A skill edit affects every future session, and so does adopting someone else's skill. Treat either as an experiment: check that it makes the agent better on real work before keeping it. `eval` owns the procedure.

```text
/eval this skill change. Same task for both variants, candidates stay blind.
```

When a skill keeps missing and the intended behavior is known, change and test it in one task:

```text
/eval update the review skill so it flags missing migrations, then test the change.
```

