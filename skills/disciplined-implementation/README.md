# Disciplined Implementation

A reusable, risk-calibrated implementation discipline for substantial engineering work.

## Summary

Disciplined Implementation defines a repeatable loop for scoping, orientation, baseline capture, proof selection, implementation, verification, review, publication, and auditable reporting. It is deliberately opinionated while remaining language-, framework-, repository-, and harness-neutral.

## When to use

Use this skill for:

- multi-file feature work
- bug fixes with regression risk
- refactors that require behavioral proof
- public contract, schema, migration, permission, concurrency, or security changes
- investigations that need explicit evidence and a reconstructable conclusion

For low-risk documentation or metadata edits, use the same evidence discipline with lighter ceremony. The skill explicitly permits alternatives to RED→GREEN when an automated failing test is not the strongest available proof.

## Quick start

1. Load `disciplined-implementation.md` into the agent's instruction context.
2. Classify the task as low, medium, or high risk.
3. Define acceptance criteria and required evidence before editing.
4. Follow the core loop and finish with the evidence report.
5. Run the target repository's own verification commands; do not substitute a generic checklist.

## Skill files

- `disciplined-implementation.md` — core skill entry document
- `examples/codex-usage.md` — Codex usage pattern
- `examples/claude-usage.md` — Claude usage pattern
- `skill.yaml` — machine-readable metadata contract

## Integration notes

- `registry.json` is the marketplace discovery index.
- `skill.yaml` is the canonical per-skill contract; duplicated registry fields must remain synchronized.
- Harness examples demonstrate prompt shape, not repository-specific commands.
- Pin a repository revision when deterministic skill behavior matters.

## Limitations

- The skill cannot identify a repository's real verification gate without reading that repository's instructions and configuration.
- Real-artifact verification may require credentials, services, devices, or environments unavailable to the agent; the gap must be reported as residual risk.
- Independent review is strongest with a separate reviewer or clean context, but the skill provides an adversarial self-review fallback.
- The method improves evidence and process discipline; it does not make an unsafe environment safe or replace domain expertise.
