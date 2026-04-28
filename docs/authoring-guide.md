# Authoring guide — adding or editing skills

## Skill structure

Each skill lives at `skills/<skill-name>/`:

```
skills/<skill-name>/
├── SKILL.md
└── references/
    ├── <topic-1>.md
    ├── <topic-2>.md
    └── states/                  # for state research skills only
        ├── AL.md
        ├── ...
        └── WY.md
```

## SKILL.md frontmatter

Every SKILL.md MUST start with YAML frontmatter:

```yaml
---
name: <kebab-case-name>            # ≤ 64 chars, no "anthropic"/"claude"
description: |
  <Third-person, declarative paragraph, ≤ 1024 chars total. Front-
  load the use case. Include "Use when ..." with at least three
  example user phrasings. End with "Make sure to use this skill
  whenever the user mentions ..." trigger phrases.>
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---
```

Constraints:
- `name` ≤ 64 chars; no reserved words `anthropic` / `claude`.
- `description` ≤ 1024 chars (validate.sh enforces this).
- `version` semver-formatted.

## Skill body

Use the canonical structure (see `docs/skill-template.md`):

1. **Read before output** — list of `shared/` files + per-skill
   references the skill MUST read before producing output.
2. **Operative authority** — primary IRC sections, Treas. Regs.,
   case law.
3. **Workflow** — numbered steps (Intake → Analysis →
   Conclusion → Authorities → JSON sidecar).
4. **Hard rules** — explicit forbiddances and decay rules.
5. **Verification checklist (appendix)** — SSTS / Circular 230
   reference.

## Citation discipline

Per `shared/citation-discipline.md`:
- NEVER fabricate citations.
- Use the sentinel `[CITATION NEEDED — search: <query>]` when a
  primary source is unreachable.
- Every citation in JSON sidecar `authorities[]` must include:
  `authority_type`, `citation`, `url`, `retrieved_date`,
  `quoted_text` (≤75 words), `weight`.

## Reference files

Push longer content into `references/<topic>.md` files (one level
deep). Don't nest deeper than `references/<topic>/file.md`
unless absolutely necessary.

For state research skills, per-state files live at
`references/states/<XX>.md` (where `<XX>` is the state code).

## Adding a new skill

1. Pick a kebab-case slug (≤ 64 chars).
2. Create `skills/<slug>/SKILL.md` from the template.
3. Add `references/<topic>.md` files for substantive content.
4. Run `./scripts/validate.sh skill <slug>`.
5. Add eval JSON at `evals/<family>/<slug>.json` (≥ 3 cases by
   Phase 6).
6. Run `./scripts/run-evals.sh skill <slug>`.
7. Add the skill path to `.claude-plugin/plugin.json` `skills[]`.
8. Update `shared/strategy-list.md` if it's a planning strategy.
9. Submit PR for review.

## Editing an existing skill

1. Read the current SKILL.md.
2. Make minimal, targeted edits.
3. Increment `version` in frontmatter (e.g., 0.1.0 → 0.2.0 for
   substantive changes; 0.1.0 → 0.1.1 for fixes).
4. Run validation and eval harness.
5. Commit per Conventional Commits style:
   `feat(<scope>): <message>` for new features;
   `fix(<scope>): <message>` for bug fixes;
   `docs(<scope>): <message>` for documentation;
   `refactor(<scope>): <message>` for refactoring.
6. PR for review.

## State stub promotion

State stub files at `references/states/<XX>.md` are intentionally
placeholder. To promote:
1. Edit the file with substantive content.
2. Update the `status` field from `stub` to `draft`.
3. Update `last_reviewed` and `last_reviewed_by`.
4. Replace `<!-- TODO -->` markers with real citations or
   `[CITATION NEEDED — search: <query>]` sentinels for items
   still requiring research.
5. Submit PR for second-pair review.
6. After review, promote to `reviewed`.
7. After live citation walk against current statute and regulation,
   promote to `verified`.

See [docs/state-stub-promotion.md](state-stub-promotion.md) for
detailed promotion procedure.

## Public-Law-to-USC workflow

Skills that touch recent legislation (TCJA, IRA, OBBBA, SECURE 2.0,
etc.) must implement the workflow in
`shared/legislation-tracking.md`:

1. Resolve popular name → Public Law via Popular Name Tool.
2. Pull Classification Tables for affected USC sections.
3. Verify each affected section's current text via USLM.
4. Locate JCT Bluebook / committee reports / Greenbook / CBO.
5. Check Federal Register IRS feed for proposed regs / TDs.
6. Optional Cite Checker.

See [docs/legislation-tracking-howto.md](legislation-tracking-howto.md)
for detailed procedure.

## Compliance scaffolding

Every skill output MUST include the SSTS / Circular 230
verification checklist appendix referenced in
`shared/compliance.md`:
- AICPA SSTS § 1.1, § 2.3.
- Circular 230 §§ 10.22, 10.35, 10.37.
- Disclosure flagging (Form 8275 / 8275-R / 8886).
- Negative-treatment-review residual practitioner responsibility
  for high-stakes positions.

## Eval harness

Each skill should have an eval JSON at `evals/<family>/<slug>.json`:

```json
{
  "skill_name": "<slug>",
  "version": "<semver>",
  "evals": [
    {
      "id": "<case-id>",
      "prompt": "<user prompt>",
      "expected_output": "<narrative description of expected behavior>",
      "expectations": [
        "<bullet 1>",
        "<bullet 2>",
        ...
      ]
    },
    ...
  ]
}
```

Phase 6 requires ≥ 3 eval cases per skill. Add cases gradually as
you refine the skill.

## Validation commands

```bash
# Full validation:
./scripts/validate.sh full

# Phase-specific:
./scripts/validate.sh phase 1   # ... through 7

# Skill-specific:
./scripts/validate.sh skill <slug>

# Eval harness:
./scripts/run-evals.sh full
./scripts/run-evals.sh phase 1
./scripts/run-evals.sh skill <slug>
```

URL-liveness check is gated by `SKIP_URL_CHECK=1` for offline
development; CI runs without the flag.

## CI

GitHub Actions workflow at `.github/workflows/validate.yml` runs
on every PR:
- `validate.sh full`
- `run-evals.sh full`
- Frontmatter / JSON / sentinel / state-stub / authority-taxonomy
  checks.

PRs must be CI-green before merge.

## Versioning

- v0.x.y — pre-release.
- v1.0.0-beta — first beta release (Phase 7 target).
- v1.0.0 — first stable release.

Release tags created by Kurt manually after PR merge to `main`.

## Code style

- Markdown body ≤ 500 lines per SKILL.md.
- Reference files can be longer.
- Use third-person, declarative voice in frontmatter description.
- Use second-person ("the practitioner") in body where appropriate.
- ASCII / UTF-8 only; avoid smart quotes / em-dashes that break in
  some validators.

## Don't

- Don't fabricate citations.
- Don't push to `main` directly; use the `build` branch.
- Don't include client-confidential data, PII, or live API keys.
- Don't include §831(b) micro-captives or other Listed
  Transactions in the strategy library without explicit warning.
- Don't claim Chevron deference for Treasury Regs (post-Loper
  Bright; use Skidmore framework).
