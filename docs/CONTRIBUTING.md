# Contributing Skills to the Marketplace

Thank you for considering adding a skill to this marketplace! This guide will help you create and submit a well-structured, reusable skill.

## Skill Requirements

Before creating a skill, ensure it meets these criteria:

1. **Language-neutral or explicitly scoped** — Skills should be applicable across multiple programming languages, or clearly document their language constraints.
2. **Harness-agnostic** — Skills should work with any AI coding harness (Codex, Claude, or others), or explicitly document which harnesses they support.
3. **Battle-tested** — The skill should have been used and refined in real scenarios.
4. **Well-documented** — Clear, actionable instructions with examples.
5. **Reusable** — Designed for sharing and reproduction across projects.

## Creating a New Skill

### 1. Use the Skill Template

Start with [`docs/SKILL-TEMPLATE.md`](SKILL-TEMPLATE.md) to scaffold your skill structure.

### 2. Directory Structure

Create your skill under `skills/[skill-id]/`:

```
skills/[skill-id]/
├── skill.yaml
├── README.md
├── [skill-name].md
├── examples/
│   ├── codex-usage.md
│   └── claude-usage.md
└── tests/                     # optional
```

### 3. Update the Registry

Add your skill's metadata to `registry.json` so it can be discovered.

### 4. Document Harness Compatibility

Clearly specify:
- Supported harnesses
- Integration method
- Expected format
- Any limitations

## Submission Process

1. Add your skill files under `skills/[skill-id]/`
2. Update `registry.json`
3. Verify links and examples
4. Open a pull request

## Naming Conventions

- **Skill ID**: lowercase kebab-case, e.g. `disciplined-implementation`
- **Directory name**: must match the skill ID
- **Display name**: human-readable title case

## Quality Bar

A good skill should be:
- Concrete
- Actionable
- Reusable
- Portable
- Auditable

## License

Unless otherwise specified, marketplace contributions are MIT licensed.
