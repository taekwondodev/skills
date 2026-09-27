# PR history

Inspect the complete commit range and the repository's merge policy. Base the recommendation on the logical structure of the change and the usefulness of its intermediate commits.

## Choose a recommendation

- **Squash and merge:** recommend when the PR represents one logical change developed through incremental fixups and repository policy permits it. This creates one commit on the base branch; the source branch and the PR's Commits tab retain their history.
- **Preserve meaningful commits:** retain independently meaningful steps that help review and later investigation, using a merge method allowed by repository policy.
- **Branch cleanup:** distinguish a branch rewrite from squash at merge when the user needs the source history reorganized before review. Account for collaborators and dependent branches when explaining its consequences.

Merging, rewriting history, and changing repository settings require separate authorization and are outside this skill's execution scope.

## Final message

Check the repository's squash-message defaults and recommend a summary of the delivered change, preserving necessary issue references and attribution. Review a generated message before accepting it as the final commit description.

Completion: return the recommendation, its rationale, and any pending authorization with the PR result.
