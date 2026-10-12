## Dev cycle

### Issue tracker

Issues, specs, and tickets live in GitHub Issues. See `docs/agents/issue-tracker.md`.

### Issue labels

Use category, readiness, and activity labels, with one label per state dimension. See `docs/agents/triage-labels.md`.

### Delivery

Deliver directly to `origin/main`. Before implementation or delivery, read `docs/agents/delivery.md` for route and target defaults.

### Domain docs

Use the single-context layout. See `docs/agents/domain.md`.

## Test a skill change blind

A skill edit affects every future session, and so does adopting someone else's skill. Treat either as an experiment: check that it makes the agent better on real work before keeping it. `eval` owns the procedure.

```text
/eval this skill change. Same task for both variants, candidates stay blind.
```

When a skill keeps missing and the intended behavior is known, change and test it in one task:

```text
/eval update the review skill so it flags missing migrations, then test the change.
```

Asking for the eval up front keeps the edit honest. A fix written from one bad session tends to overfit that session, and over many edits the skill drifts. The eval catches the drift before it ships.

The procedure is built around one failure mode, the observer effect: an agent that knows it is being evaluated behaves differently. Candidates get an organic-looking task in sanitized directories, one judge scores every output under neutral labels, and chain-following is graded from the files each candidate actually read rather than from its claims.

Read every output yourself before accepting the verdict. On disagreement with the judge, suspect the rubric before your own judgment.
