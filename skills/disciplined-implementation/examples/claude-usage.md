# Using Disciplined Implementation in Claude

## Custom instructions

Paste the contents of `disciplined-implementation.md` into Claude custom instructions or a system prompt alongside the target repository's own instructions. The skill is intentionally strict and should not be reframed as optional guidance.

## Prompt example

```text
Apply the Disciplined Implementation skill to this substantial coding task.

Show:
1. Acceptance criteria, non-goals, and the repository instructions consulted
2. Working-tree state, baseline behavior, real signatures, contracts, and data shapes
3. The failing test observed before each behavior implementation
4. The minimal passing change and subsequent refactor
5. The complete repository-prescribed gate before every commit, with exact commands and counts
6. Real-artifact verification
7. Independent or clean-context review findings and explicit verdict
8. Staged and published diff verification
9. The final evidence report, including every waiver and residual risk

Do not waive a required step because it is slow, expensive, inconvenient, or
likely to pass. A waiver is valid only when the step is impossible or genuinely
inapplicable and must identify substitute proof and the approving operator.
```

## Expected output

The final response should use the skill's evidence-report structure, distinguish verified facts from inference, and explicitly label anything that was not verified.
