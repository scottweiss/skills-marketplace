# Disciplined Implementation

A reusable implementation discipline for substantial coding tasks.

## Summary

Disciplined Implementation defines a repeatable loop for planning, execution, validation, review, and auditable reporting.

## When to use

Use this skill for:
- multi-file feature work
- bug fixes with regression risk
- refactors that require verification
- investigations that need explicit evidence

## Quick start

1. Read `disciplined-implementation.md`
2. Apply the core loop to your task
3. Use examples for harness-specific prompt structure

## Skill files

- `disciplined-implementation.md` — core skill entry document
- `examples/codex-usage.md` — Codex usage pattern
- `examples/claude-usage.md` — Claude usage pattern
- `skill.yaml` — machine-readable metadata contract

## Integration notes

- Registry discovery fields point to this skill's `entry` and `readme`
- Examples are declared in `skill.yaml` and `registry.json` for machine loading

## Limitations

- Assumes a workflow that supports iterative validation and review
- Requires adapting command-level checks to each target repository
