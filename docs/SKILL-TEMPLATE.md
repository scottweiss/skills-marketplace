# Skill Template

Use this template when adding a new skill.

## Directory template

```text
skills/<skill-id>/
├── skill.yaml
├── README.md
├── <skill-id>.md
└── examples/
    ├── codex-usage.md
    └── claude-usage.md
```

## `skill.yaml` template

```yaml
id: example-skill
name: Example Skill
version: 1.0.0
summary: One-line summary for discovery.
description: |
  A short explanation of what the skill does and when to use it.

entry: skills/example-skill/example-skill.md
readme: skills/example-skill/README.md
examples:
  - skills/example-skill/examples/codex-usage.md
  - skills/example-skill/examples/claude-usage.md

tags:
  - example
  - reusable

harness_compatibility:
  codex:
    supported: true
    format: markdown
  claude:
    supported: true
    format: markdown

metadata:
  maturity: experimental
  license: MIT
  author: Your Name
```

## `README.md` expectations

Document:
- purpose and outcomes
- when to use the skill
- quick start by harness
- skill file map
- known limitations

## `registry.json` entry template

```json
{
  "id": "example-skill",
  "slug": "example-skill",
  "name": "Example Skill",
  "version": "1.0.0",
  "summary": "One-line summary for discovery.",
  "description": "Expanded description.",
  "path": "skills/example-skill/",
  "entry": "skills/example-skill/example-skill.md",
  "readme": "skills/example-skill/README.md",
  "metadata": {
    "examples": [
      "skills/example-skill/examples/codex-usage.md",
      "skills/example-skill/examples/claude-usage.md"
    ]
  }
}
```
