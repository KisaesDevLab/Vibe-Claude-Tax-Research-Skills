---
description: Pre-compaction checkpoint — persist progress, commit, push
allowed-tools: Bash(git:*) Edit Read
---
1. Append a session-log entry at the bottom of BUILD_PLAN.md:
   `YYYY-MM-DDTHH:MM | phase X | items: ... | last commit: <sha>`
2. `git add -A && git commit -m "chore: checkpoint" || true`
3. `git push -u origin claude/build-vibe-cpa-skills-3bct8`
4. Suggest `/compact` if context is over 70% full.
