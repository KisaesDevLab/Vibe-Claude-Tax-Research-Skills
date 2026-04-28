# Installing Vibe CPA Skills in Claude Code

Claude Code (CLI / IDE extensions) supports the Skills marketplace,
so you can install the entire Vibe CPA pack with a single command.

## Prerequisites

- Claude Code CLI ≥ 1.0 (`claude --version`).
- Internet access to GitHub.

## Installation

### Add the marketplace

```bash
claude /plugin marketplace add KisaesDevLab/vibe-claude-tax-research-skills
```

This registers the marketplace at
`.claude-plugin/marketplace.json` of the repo.

### Install the plugin

```bash
claude /plugin install vibe-cpa-pack@kisaes-cpa-skills
```

This installs all skills under `~/.claude/plugins/`.

### Verify installation

```bash
claude /plugin list
```

You should see `vibe-cpa-pack` listed with its version.

## Usage

Once installed, the skills auto-load when the user's input matches
a trigger description. Example invocation:

```
> Research §199A QBI deduction eligibility for a CPA solo practitioner.

[Claude Code uses tax-research-federal skill]
```

The dispatcher (`cpa-pack-index`) routes to the appropriate
specialist skill based on user input phrasing.

## Updating

```bash
claude /plugin update vibe-cpa-pack
```

## Uninstalling

```bash
claude /plugin uninstall vibe-cpa-pack
```

## Configuration

Skills follow the AICPA SSTS / Circular 230 compliance scaffolding.
Practitioners may customize `shared/` files for firm-specific
policies; commit changes locally if you want them to persist
across `/plugin update` operations.

## See also

- [docs/install-claude-ai.md](install-claude-ai.md) — claude.ai
  web-app installation.
- [docs/authoring-guide.md](authoring-guide.md) — authoring new
  skills.
