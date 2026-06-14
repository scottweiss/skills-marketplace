# Integrating Skills with Codex and Claude

This document explains how to use marketplace skills with AI coding harnesses.

## Codex

### Option 1: Reference the repository

```yaml
skills:
  - source: "github://scottweiss/skills-marketplace"
    skill: "disciplined-implementation"
```

### Option 2: Paste the skill content

Copy the core markdown file for the skill and include it in your Codex prompt or harness instructions.

## Claude

### Option 1: Custom instructions

Paste the skill content into Claude custom instructions.

### Option 2: System prompt

Include the skill markdown inside the system prompt for your Claude API call.

## Best Practices

- Start with one skill at a time
- Prefer the full source markdown for the initial integration
- Verify the harness is actually following the skill
- Keep the registry entry and examples in sync
