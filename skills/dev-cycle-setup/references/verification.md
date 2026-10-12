# Verification baseline

Use during project setup to select and configure reusable checks for the project's stack.

## Discover

Inspect contributor guidance, build manifests, tool configuration, and CI. Identify existing commands, their coverage, and required gates. Preserve established tooling and report gaps rather than replacing it on first use of the workflow. Defer tool choices while the stack is undecided.

## Select

For a new project, propose the smallest useful baseline: the stack's formatter, compiler or type checker where applicable, and reliable correctness lint rules. Use established ecosystem tools; add custom rules only for demonstrated gaps. For rule selection or dependency choices, use [coding-standards](../../coding-standards/SKILL.md).

Separate required checks from advisory preferences. Choose rules that fit project conventions and keep feedback costs proportionate. On existing projects, propose additions only where the current coverage warrants them.

Include proposed dependencies, configuration changes, commands, and coverage gaps in the setup draft. Apply only the choices confirmed through the setup's existing approval step.

## Apply and verify

Expose reproducible commands through the project's native build or task configuration. Point the delivery policy's verification gates to that source rather than maintaining another command inventory.

Run the selected checks on the project and resolve failures within the approved scope. Report unrun checks and remaining gaps explicitly; an unavailable or failing check is not a verified baseline. For newly configured checks, use a disposable invalid example to confirm that the intended violation is detected and affects the gate as configured, then confirm the corrected example passes.

Completion: the confirmed baseline is configured, its commands and failure behavior have been exercised, and coverage limits are recorded. Routine implementation and review then consume [mechanical-check evidence](../../implement/references/mechanical-checks.md).
