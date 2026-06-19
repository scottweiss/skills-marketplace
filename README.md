# Skills Marketplace

A public, author-curated marketplace of reusable skills for AI coding agents and teams. The collection reflects Scott Weiss's preferred engineering practices while remaining portable enough to share and integrate across projects. The skills are deliberately opinionated; portability means reusable across environments, not neutral or lowest-common-denominator guidance.

## Why this repository

This repository packages practical engineering skills so they can be:

- discovered through `registry.json`
- integrated across harnesses such as Codex and Claude
- versioned and reused consistently across projects
- validated against explicit metadata and documentation contracts

## Marketplace structure

- `registry.json` — canonical discovery index
- `skills/<skill-id>/skill.yaml` — canonical per-skill metadata contract
- `skills/<skill-id>/<skill-id>.md` — executable skill instructions
- `skills/<skill-id>/README.md` — human-facing overview
- `skills/<skill-id>/examples/` — harness-specific usage
- `scripts/validate_marketplace.py` — local and CI contract validation
- `docs/` — contribution, authoring, and integration guidance

## Available skills

| Skill | Summary | Version |
| --- | --- | --- |
| [Disciplined Implementation](skills/disciplined-implementation/) | Strict test-first implementation loop with full-gate verification, real-artifact checks, independent review, and auditable reporting | 1.1.0 |

## Quick start

### Discover skills

Inspect `registry.json` and read each skill entry's:

- `slug`
- `summary`
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

Open the skill's declared entry file and include it in system or custom instructions alongside the target repository's own guidance.

## Validate the marketplace

```bash
python -m pip install -r requirements-validation.txt
python scripts/validate_marketplace.py
```

Validation checks registration, file layout, semantic versions, metadata synchronization, frontmatter, required documentation sections, examples, and text hygiene.

## Publishing and contribution

- Contribution guide: [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)
- Skill authoring template: [`docs/SKILL-TEMPLATE.md`](docs/SKILL-TEMPLATE.md)
- Integration details: [`docs/INTEGRATION.md`](docs/INTEGRATION.md)

## Stability and compatibility

- `skill.yaml` is the canonical contract for an individual skill.
- `registry.json` is the canonical marketplace discovery index.
- Mirrored fields must agree; CI rejects drift.
- Skill and marketplace versions use semantic versioning.

## License

MIT — see [`LICENSE`](LICENSE).
