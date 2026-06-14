# Skills Marketplace

A curated collection of portable engineering skills for AI coding harnesses (Codex, Claude, and others). Each skill is language-agnostic, harness-neutral, and battle-tested.

## Available Skills

| Skill | Description | Harnesses |
|-------|-------------|-----------|
| [Disciplined Implementation](skills/disciplined-implementation/) | A rigorous, portable engineering method for substantial coding tasks | Codex, Claude |

## Quick Start

### Use in Claude

1. Open [disciplined-implementation.md](skills/disciplined-implementation/disciplined-implementation.md)
2. Copy the content
3. Paste into your Claude system prompt or custom instructions

### Use in Codex

Add to your harness config:
```yaml
skills:
  - source: "github://scottweiss/skills-marketplace"
    skill: "disciplined-implementation"
```

## About This Marketplace

This marketplace contains portable, reusable engineering methodologies designed for AI coding agents and developers. Each skill:
- ✅ Is language- and tool-neutral
- ✅ Has been refined through real-world usage
- ✅ Works across multiple harnesses (Codex, Claude, etc.)
- ✅ Includes integration examples

## Adding New Skills

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on creating and submitting new skills.

## Integration Guide

Learn how to integrate these skills into your harness:
- [Codex Integration](docs/INTEGRATION.md#codex)
- [Claude Integration](docs/INTEGRATION.md#claude)

## License

MIT - See [LICENSE](LICENSE) for details.

---

**Maintained by:** Scott Weiss  
**Repository:** https://github.com/scottweiss/skills-marketplace
