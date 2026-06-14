# Contributing

Thank you for helping expand the marketplace.

## Contribution scope

Contributions may include:
- new skills
- updates to existing skills
- documentation and validation improvements

## Required skill layout

Each skill lives in `skills/<skill-id>/` and should include:

- `skill.yaml`
- `README.md`
- `<skill-id>.md` (main entry document)
- `examples/` with at least one harness example

## Required metadata

### `skill.yaml`

A skill definition should include at minimum:
- `id`, `name`, `version`
- `summary`, `description`
- `entry`, `readme`
- `examples`
- harness compatibility details

### `registry.json`

Every skill listed in `registry.json` must include discovery fields:
- `slug`
- `entry`
- `readme`
- `metadata`
- `summary`

## Submission checklist

1. Add or update files under `skills/<skill-id>/`
2. Add or update skill entry in `registry.json`
3. Verify all referenced files exist
4. Run repository validation checks
5. Open a pull request with a clear summary

## Naming conventions

- Skill IDs and slugs: lowercase kebab-case
- Directory name: must match `id`
- Entry document: should match the skill identifier when possible

## Quality expectations

A marketplace skill should be:
- portable across environments
- concrete and actionable
- easy to discover and integrate
- auditable through examples and metadata

## License

Unless explicitly stated otherwise, contributions are MIT licensed.
