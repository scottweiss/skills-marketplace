# Disciplined Implementation

An intentionally strict implementation discipline for substantial engineering work.

## Summary

Disciplined Implementation codifies a rigorous delivery loop derived from observed Fable 5 behavior: orient before editing, ground plans in real code, prove behavior through RED→GREEN, run the complete repository gate before every commit, inspect the actual artifact, review independently, and leave exact evidence.

The strictness is intentional. This is an opinionated execution policy, not a menu of optional best practices. A required step may be waived only when it is impossible or genuinely inapplicable, with explicit substitute proof, authorization, and residual-risk reporting.

## When to use

Use this skill for:

- multi-file feature work
- bug fixes with regression risk
- refactors that require behavioral proof
- public contract, schema, migration, permission, concurrency, or security changes
- investigations that require reconstructable evidence

Trivial prose-only or mechanical metadata work may explicitly opt out before implementation. Once the skill is invoked for an in-scope task, do not scale it down based on perceived risk, cost, or convenience.

## Quick start

1. Load `disciplined-implementation.md` into the agent's instruction context alongside the target repository's own instructions.
2. Define acceptance criteria, non-goals, and required evidence.
3. Orient in the real code and establish a baseline.
4. Follow RED→GREEN for every behavior change.
5. Run the complete repository-prescribed gate before every commit.
6. Verify the real artifact and obtain an independent or clean-context review verdict.
7. Finish with the evidence report, including every waiver and residual risk.

## Skill files

- `disciplined-implementation.md` — core skill entry document
- `examples/codex-usage.md` — Codex usage pattern
- `examples/claude-usage.md` — Claude usage pattern
- `skill.yaml` — machine-readable metadata contract

## Integration notes

- `registry.json` is the marketplace discovery index.
- `skill.yaml` is the canonical per-skill contract; duplicated registry fields must remain synchronized.
- Repository and task instructions take precedence when they conflict with the portable skill.
- Harness examples demonstrate the required evidence and workflow, not repository-specific commands.
- Pin a repository revision when deterministic skill behavior matters.

## Limitations

- The skill cannot identify a repository's real verification gate without reading that repository's code, instructions, and configuration.
- Some environments cannot provide required services, credentials, devices, production-like data, or destructive test targets; these constraints require explicit waivers.
- Independent review is strongest with a separate reviewer; clean-context adversarial self-review is a weaker fallback.
- Strict process reduces avoidable implementation risk but does not replace security, legal, operational, accessibility, or other domain-specific expertise.
