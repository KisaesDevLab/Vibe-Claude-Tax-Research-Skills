# Installing Vibe CPA Skills in claude.ai

Vibe CPA Skills is distributed as a Claude Skills pack. For
`claude.ai` (the web app), each skill is installed individually via
ZIP upload.

## Prerequisites

- Anthropic claude.ai Pro / Team / Enterprise account.
- Skills feature enabled (currently in rollout; verify in your
  account settings).

## Installation steps

### 1. Download the skill ZIP

Each skill ships as a folder under `skills/`. To install a single
skill in claude.ai:

```bash
# Clone the repo
git clone https://github.com/KisaesDevLab/vibe-claude-tax-research-skills.git
cd vibe-claude-tax-research-skills

# Create a ZIP of the skill of interest (example: tax-research-federal)
cd skills/tax-research-federal
zip -r ../../tax-research-federal.zip .
cd ../..
```

This produces `tax-research-federal.zip` containing:
- `SKILL.md` (the skill instruction file).
- `references/*.md` (supporting reference content).

### 2. Upload to claude.ai

1. Navigate to claude.ai Settings → Capabilities → Skills.
2. Click "Add Skill" → "Upload ZIP".
3. Select the ZIP file you created.
4. Confirm the skill appears in your list.

### 3. Repeat for additional skills

The Vibe CPA pack contains 33+ skills. You can install all of them
individually, or just the subset you need for your engagement.

Recommended starter set:
- `tax-research-federal` (the federal research flagship).
- `predict-worker-classification` (one prediction example).
- `return-summary-1040` (return summary).
- `irc-section-lookup` (IRC + Public Law lookup).
- `compliance-ssts-circular230` (SSTS / Circular 230 checklist).

You can add more skills to the same project as your needs grow.

## Recommended approach: download a project ZIP

Alternatively, you can download a release ZIP from GitHub:

1. Navigate to
   https://github.com/KisaesDevLab/vibe-claude-tax-research-skills/releases.
2. Download the latest release `.zip` artifact.
3. Extract.
4. Per-skill ZIP each subfolder of `skills/` and upload as
   above.

We provide a script (`scripts/zip-each-skill.sh`) to automate
per-skill ZIP creation. (Add this script in Phase 5+ as a
convenience.)

## Verifying installation

After upload, test the skill by invoking it in a conversation:

```
Use the tax-research-federal skill to research IRC §199A QBI
qualification for a sole-proprietor consultant.
```

Claude should:
1. Recognize the skill trigger (description matches).
2. Read `shared/citation-discipline.md`, `authority-hierarchy.md`,
   `confidence-bands.md`, `compliance.md` (if available in the
   uploaded skill bundle).
3. Walk the SKILL.md workflow.
4. Return a memorandum-style answer with JSON sidecar.

## Limitations of claude.ai distribution

- claude.ai skills are uploaded individually; no marketplace
  installer.
- Cross-skill references (e.g., a research skill routing to a
  state-research skill) work only if both skills are uploaded.
- The `shared/` directory must be uploaded as part of each skill's
  ZIP (or maintained as a reference file in each skill's bundle).

## Maintenance

Skill packs are versioned in the repository. To update:

1. Pull latest from GitHub.
2. Re-create per-skill ZIPs.
3. Re-upload to claude.ai (replace existing skill or upload new
   version).

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Skill not invoked when expected | Description mismatch | Review SKILL.md description trigger phrases |
| Skill produces fabricated citations | shared/citation-discipline.md not loaded | Ensure shared/ files are bundled with each skill |
| State research caps at LOW confidence | Per-state file is `status: stub` | Promote per-state file to `draft` or higher (see `docs/state-stub-promotion.md`) |

## See also

- [docs/install-claude-code.md](install-claude-code.md) — Claude
  Code (CLI / IDE) installation.
- [docs/authoring-guide.md](authoring-guide.md) — authoring new
  skills.
