---
description: Open a phase PR build → main with full body
argument-hint: [phase-number]
allowed-tools: Bash(gh:*) Read
---
Open a PR from the working build branch (`claude/build-vibe-cpa-skills-3bct8`)
to `main` titled `Phase $1`. Body must include:
- Checklist of items completed in BUILD_PLAN.md Phase $1
- Eval pass-rate summary (paste from scripts/run-evals.sh output)
- Validation output from scripts/validate.sh
- "Awaiting Kurt's review" footer
Do NOT merge. Stop after PR creation.
