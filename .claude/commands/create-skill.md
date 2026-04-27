---
description: Scaffold a new SKILL.md following the project template
argument-hint: [skill-name] [family]
allowed-tools: Read Edit Write Bash(mkdir:*) Bash(ls:*) Glob
---
Scaffold a new skill: $1 (family: $2).

1. Create directory `skills/$1/` and `skills/$1/references/`.
2. Copy `docs/skill-template.md` body into `skills/$1/SKILL.md`,
   replacing `<skill-name>` with $1 and `<topic>` with $2.
3. Match the style and rigor of the three flagship exemplars:
   - skills/tax-research-federal/SKILL.md
   - skills/predict-worker-classification/SKILL.md
   - skills/return-summary-1040/SKILL.md
4. Tailor description to family $2 with three concrete trigger phrases
   in the words a CPA actually uses. Description ≤ 1024 chars.
5. Add at least one `references/<topic>.md` stub.
6. If this is a state research skill, also create the
   `references/states/` directory and populate it with 51 stub files
   per shared/state-template.md (one per jurisdiction in
   shared/sources.json state_dors).
7. If this skill touches recent Public Laws (irc-section-lookup,
   tax-research-federal, planning-multi-year), reference
   shared/legislation-tracking.md from the SKILL.md "Read before
   output" block.
8. Run `./scripts/validate.sh skill $1`. Iterate until exit 0.
