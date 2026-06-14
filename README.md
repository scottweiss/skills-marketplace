# Skills Marketplace

A curated, machine-discoverable marketplace of reusable skills for AI coding agents and teams.

## Why this repository

This repository packages practical engineering skills so they can be:
- discovered via `registry.json`
- integrated across harnesses (Codex, Claude, and others)
- reused consistently across projects

## Marketplace structure

- `registry.json` — canonical index of published skills
- `skills/<skill-id>/` — one directory per skill
- `docs/` — contributor and integration guidance

## Available skills

| Skill | Summary | Version |
| --- | --- | --- |
| [Disciplined Implementation](skills/disciplined-implementation/) | Structured implementation loop for reliable delivery, verification, and review | 1.0.0 |

## Quick start

### Discover skills

Inspect `registry.json` and read each skill entry's:
- `slug`
- `entry`
- `readme`
- `metadata`

### Use with Codex

```yaml
skills:
  - source: "github://scottweiss/skills-marketplace"
    skill: "disciplined-implementation"
```

### Use with Claude

Open `skills/disciplined-implementation/disciplined-implementation.md` and include it in your system/custom instructions.

## Publishing and contribution

- Contribution guide: [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)
- Skill authoring template: [`docs/SKILL-TEMPLATE.md`](docs/SKILL-TEMPLATE.md)
- Integration details: [`docs/INTEGRATION.md`](docs/INTEGRATION.md)

## Stability and compatibility

- Skill contracts are declared in `skill.yaml`
- Marketplace discovery contracts are declared in `registry.json`
- Validation checks run in `.github/workflows/validate.yml`

## License

MIT — see [`LICENSE`](LICENSE).
