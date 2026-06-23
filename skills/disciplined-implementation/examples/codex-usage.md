# Using Disciplined Implementation in Codex

## Reference the marketplace

```yaml
skills:
  - source: "github://scottweiss/skills-marketplace"
    skill: "disciplined-implementation"
```

Alternatively, load `skills/disciplined-implementation/disciplined-implementation.md` directly into the instruction context alongside the repository's own instructions.

## Prompt example

```text
Apply the Disciplined Implementation skill to this substantial coding task.
The skill is intentionally strict; do not reduce its requirements based on
perceived task risk, cost, or convenience.

Before editing:
- read repository instructions and inspect status and diffs
- define acceptance criteria, non-goals, and required evidence
- map real signatures, contracts, call sites, schemas, and existing patterns
- reproduce current behavior or establish a baseline

During implementation:
- write and run a failing test before each behavior change
- confirm the test fails for the intended reason
- implement the minimum passing change, then refactor
- search before introducing a duplicate responsibility
- preserve unrelated work and keep an audit log

Before every commit:
- run the complete repository-prescribed gate against the final tree
- report exact commands, results, and counts
- stage explicit paths or patches and inspect the staged diff

Before handoff:
- exercise the real artifact
- obtain an independent or clean-context review verdict
- verify the remote commit and pull-request diff when published
- return the skill's evidence report

A step may be waived only when impossible or genuinely inapplicable. Record the
rule, evidence, substitute verification, approving operator, and residual risk.
```

## Expected output

The response should distinguish verified facts from inference, show RED→GREEN and per-commit gate evidence, name every waiver, and never claim completion from tests alone.
