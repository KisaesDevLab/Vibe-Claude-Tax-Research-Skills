---
description: Validate phase, commit with conventional message, update CHANGELOG
argument-hint: [phase-number] [short-summary]
allowed-tools: Bash(./scripts/validate.sh:*) Bash(./scripts/run-evals.sh:*) Bash(git:*) Edit Read
---
1. Run `./scripts/validate.sh phase $1`. If non-zero, stop.
2. If $1 in {1,2,3,4,6}, run `./scripts/run-evals.sh phase $1`.
3. Append a line to CHANGELOG.md `[Unreleased]` section:
   `- Phase $1: $2`
4. `git add -A`
5. `git commit -m "feat(p$1): $2"`
6. `git push -u origin claude/build-vibe-cpa-skills-3bct8`
7. Print last commit SHA.
