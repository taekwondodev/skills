# Document audit

Procedure for checking the documents a change adds or modifies. The parent [contract](../SKILL.md) decides what conforms; this reference decides the scope, what to hunt, the fix shape, and the proof.

## Scope

Every Markdown file the diff adds or modifies. Read each one complete at the head revision and locate its changed hunks. For a skill file, the [isolation rules](../SKILL-MECHANICS.md#isolation) bind as well; for a new or restructured document, so does the [authoring reference](authoring.md). Unchanged text enters scope only where a changed hunk restates or contradicts it.

## Hunt

Apply every operating rule of the contract to each changed hunk, then hunt two defects by name:

- **Contamination**: text that entered from the run that wrote it rather than from what the document's reader needs. Test each sentence against that reader, who holds this document without the conversation, the task, or its results. For a reusable document such as a skill, that reader also works in a different project.
- **Duplication**: search the repository's documents and the environment for each rule, definition, and procedure the hunk introduces before treating it as new.

## Fix shape

Delete contamination, keeping only a fact the reader needs. Resolve duplication to one owner, the site where the meaning's procedure or contract lives: merge the better wording into it, then link to it from the other site or delete that copy. Report unchanged text that fails the contract instead of editing it.

## Proof

Re-read each edited file complete, resolve every link the audit added or moved, and search the changed files for em-dashes. Give each file one verdict: conforming, fixed with the rule applied, or left with its reason.

Completion: every Markdown file in the diff has a verdict, and each meaning the change introduced has exactly one owner.
