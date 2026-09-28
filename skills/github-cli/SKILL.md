---
name: github-cli
description: Use when reading or changing GitHub resources.
---

# GitHub CLI

Use [gh-axi](https://github.com/kunchenguid/gh-axi) for GitHub reads and writes.

## Command selection

- Consult the relevant command's help for supported flags.
- Use `git` for Git operations and `gh auth` for authentication setup or checks.
- Use `gh-axi api` when a subcommand cannot express the operation.
- If gh-axi cannot perform the operation, report the limitation and ask before using another GitHub client.

Completion: the command supports the required operation, or an alternative client is approved.

## Execution

Use the target and authorized action established by the active workflow. Read the relevant context before a write, request complete output, and paginate when needed. Read back the exact target after a mutation. After an ambiguous failure, inspect its state before retrying.

Completion: report the target's observed state and any pending effects or unavailable verification.
