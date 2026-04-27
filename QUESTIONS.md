# Questions log

This file is the **non-blocking** question log. Claude Code never
stops to ask Kurt; it appends here and proceeds with a labeled
assumption. Kurt reviews periodically and replies inline under each
question. Claude Code re-reads this file at the start of every
session.

Categories:
- BLOCKING — work cannot continue safely. Extremely rare. Claude
  Code still proceeds with the safest default and continues other
  phases; the BLOCKING tag tells Kurt to act first.
- MINOR — a small choice was made; revert is trivial.
- FUTURE — surfaces something to revisit later; not on critical path.
- INTERPRETIVE — a stylistic or scoping judgment.

Entry format:

## Q### — YYYY-MM-DD HH:MM — [CATEGORY] — short title
**Phase:** N
**Question:** ...
**Assumption proceeded with:** ...
**Files affected:** ...
**Revert path:** `git revert <sha>` or `<command>`
**Kurt review:** [ ] needed / [x] resolved
**Kurt's response:** _(filled in by Kurt)_

---
(append new questions below this line)

## Q001 — 2026-04-27 21:40 — [INTERPRETIVE] — Build branch name divergence

**Phase:** 0
**Question:** The handoff prompt says "you are working on the `build`
branch", but the harness pre-created `claude/build-vibe-cpa-skills-3bct8`
as the working branch. Should I rename to `build` or stay on the harness
branch?
**Assumption proceeded with:** Stay on `claude/build-vibe-cpa-skills-3bct8`
because (a) the system instruction explicitly names that as the develop
branch and forbids pushing to other branches without permission, and
(b) renaming a remote branch in a one-shot autonomous run risks
breaking GitHub PR linkage. CLAUDE.md and BUILD_PLAN.md and the slash
commands have been updated to reference the actual branch name where
applicable; Kurt can rename to `build` later by:
`git branch -m claude/build-vibe-cpa-skills-3bct8 build && git push -u origin build && git push origin --delete claude/build-vibe-cpa-skills-3bct8`
**Files affected:** CLAUDE.md, BUILD_PLAN.md, .claude/commands/commit-phase.md,
.claude/commands/checkpoint.md, .claude/commands/open-phase-pr.md
**Revert path:** rename via git as shown above; commit history is preserved.
**Kurt review:** [ ] needed
**Kurt's response:** _(awaiting)_

## Q002 — 2026-04-27 21:40 — [INTERPRETIVE] — Repository name divergence

**Phase:** 0
**Question:** Build plan recommends `vibe-cpa-skills` but the actual
repo is `KisaesDevLab/vibe-claude-tax-research-skills`. Should I fight
the repo rename or align documentation to the existing name?
**Assumption proceeded with:** Align documentation. The repo name is a
fait accompli; renaming a public-facing identifier mid-build would
break any existing clone/fork references. CLAUDE.md / BUILD_PLAN.md /
README / install docs all say "Vibe CPA Skills" as the product name
(the marketplace identifier `kisaes-cpa-skills` and plugin identifier
`vibe-cpa-pack` remain as planned). The repository slug is
`vibe-claude-tax-research-skills` everywhere a slug is required.
**Files affected:** README.md, .claude-plugin/marketplace.json,
docs/install-claude-code.md, CLAUDE.md
**Revert path:** rename the repo on GitHub via the UI or
`gh repo rename`, then re-run the install-doc generator section.
**Kurt review:** [ ] needed
**Kurt's response:** _(awaiting)_
