---
name: eval
description: Test a skill change blind with organic tasks, parallel candidates, and one judge.
disable-model-invocation: true
---

# Eval

Own the experiment design: plan, blind, run, synthesize. The variant under test is a skill edit in the working tree or a skill adopted from elsewhere. The baseline is the committed version, or no skill at all for an adoption. An agent that knows it is being observed behaves differently, so each candidate receives an organic task and the rubric stays with the judge.

When the request bundles a skill edit with its test, make the edit first, then run this procedure with the working tree as the variant and the last committed version as the baseline.

## Blinding

Hold these for every candidate:

- Keep `eval`, `test`, `judge`, `experiment`, `rubric`, `score`, `compare`, `benchmark`, `candidate`, and `arena` out of every directory, file, and prompt the candidate sees. This skill is hidden from model invocation, so a candidate's skill list does not advertise it.
- Write the candidate prompt as an organic user request: state the goal, not the meta.
- Ask for design notes in general terms. A request to list the skills, principles, or files applied elicits a self-report; grade chain-following from the transcript and the shape of the code instead.
- Name directories and slugs the way a user would name a project.
- Give each candidate no sign that other candidates exist.
- The judge may know it is judging. It sees outputs under sanitized labels, never a model name.
- When comparing two variants, one judge scores both sets in a single pass on one scale, blind to which set each output came from.

## Procedure

1. **Frame.** State the variant under test and the behavior that counts as success. Write a rubric of three to six concrete criteria for the judge only. Completion: a reader can tell a pass from a fail for each criterion before seeing any output.
2. **Set up sanitized environments.** Give each candidate its own working directory: a separate checkout with a project-shaped name, holding exactly one version of the skill under test, the variant or the baseline. Plant the context an organic task would have: a project skeleton and the skills the candidate would naturally read. Completion: each directory resolves the skill name to one version, and the blinding list holds for every path and file in it.
3. **Author one organic prompt.** Write what a user would type, with nothing that reveals what is measured. Every candidate receives the same prompt.
4. **Launch candidates in parallel** through the available delegation capability, each in its own sanitized directory, on distinct models when the capability lets you choose. Record the model behind each sanitized label where no candidate can see it. If independence or model choice is unavailable, record that limit rather than treating same-context attempts as candidates.
5. **Launch one blinded judge** on a different model family from the candidates. Give it the rubric and the outputs under sanitized labels. It returns a verdict per label and a ranking on one scale.
6. **Verify the chain from transcripts.** Read each candidate's transcript through the delegation capability's inspection record, the complete record rather than the returned answer. Stay within the children this run launched. Note which files each candidate actually opened. Grade chain-following from those reads and the shape of the code; the candidate's own claims carry no weight.
7. **Read every candidate output yourself**, end to end, before accepting the verdict. A disagreement with the judge means a biased model or an ambiguous rubric. Settle which before synthesizing.

## Reply

Report the variant under test, the rubric, notes per candidate, the judge's verdict, your synthesis, and a recommendation on promoting the variant. Keep the sanitized labels and reveal the model mapping beside them. Carry unresolved limits forward: a shared model, missing independence, or an unread transcript stays in the reply as a gap, not a pass.
