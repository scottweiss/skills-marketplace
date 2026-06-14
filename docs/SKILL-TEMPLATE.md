# Skill Template

Use this template to create a new marketplace skill.

## Suggested Structure

```
skills/[skill-id]/
├── skill.yaml
├── README.md
├── [skill-name].md
└── examples/
    ├── codex-usage.md
    └── claude-usage.md
```

## skill.yaml

```yaml
id: example-skill
name: Example Skill
version: 1.0.0
author: Your Name
license: MIT
description: |
  A short description of the skill.

tags:
  - example
  - reusable

harness_compatibility:
  codex:
    supported: true
    format: "markdown"
  claude:
    supported: true
    format: "markdown"
```

## README.md

Document:
- What the skill is
- When to use it
- Quick start
- Integration links
- Limitations

## Core markdown file

Include the actual portable skill content here.

## Examples

Add one example for Codex and one for Claude.
