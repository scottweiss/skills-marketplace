# Integration Guide

This guide explains how to discover and integrate skills from this marketplace.

## Discovery flow

1. Read `registry.json`
2. Select a skill by `slug` and `summary`
3. Resolve `entry` and `readme` paths
4. Load examples listed in `metadata.examples`

## Codex

### Repository reference

```yaml
skills:
  - source: "github://scottweiss/skills-marketplace"
    skill: "disciplined-implementation"
```

### Direct content inclusion

Load the file declared by the skill entry (for example: `skills/disciplined-implementation/disciplined-implementation.md`) and include it in your instruction context.

## Claude

Use the same skill entry markdown in either:
- custom instructions
- a system prompt

## Recommended integration behavior

- Always resolve from `registry.json` instead of hardcoding paths
- Keep skill entry and examples in sync
- Prefer loading skill README plus entry for onboarding and execution context
- Pin to repository revision when deterministic behavior is required

## Verification

After integration:
- validate the selected skill files exist
- verify your harness follows the expected workflow from the skill
- review examples if behavior diverges
