# Vibe CPA Skills — Project Memory

## Mission
Build a publicly-distributed 28-skill Claude Skills pack for CPAs that
replicates Holistiplan, Blue J Tax, TaxPlanIQ, CPA Pilot, and TaxGPT
capabilities, with state coverage spanning all 50 states + DC.
Author: Kurt — CPA, founder of Kisaes LLC, builder of the Vibe family
of self-hosted CPA software (sibling repo: Vibe-Trial-Balance).

## Source of truth
Execution is governed by **BUILD_PLAN.md**. Read it first every session.
Phase tracking lives in BUILD_PLAN.md as `- [ ]` checkboxes. Tick boxes
ONLY after end-to-end verification (validation command exits 0).

Companion files you must read before substantive work:
@BUILD_PLAN.md
@shared/citation-discipline.md
@shared/authority-hierarchy.md
@shared/confidence-bands.md
@shared/compliance.md
@shared/legislation-tracking.md
@shared/output-schema.json
@shared/state-template.md
@docs/skill-template.md

## Identity & authority
You are operating under Kurt's authorization to build out a public CPA
tool. You may run any necessary CLI tooling (gh, git, mkdir, jq, yq,
curl, node, python). You may push to the `build` branch and open PRs
against `main`. You may NOT push directly to `main`, force-push, delete
branches/repos, set/delete secrets, run `npm publish`, or create
GitHub Releases. Use `gh pr create` and stop.

## Autonomous execution rules

### Non-blocking question protocol (CRITICAL)
You must NEVER stop to ask a clarifying question. The session is
autonomous. When you encounter ambiguity:
1. Append a numbered entry to QUESTIONS.md using the template there.
2. Pick the most defensible interpretation and label it as your
   working assumption with a one-line justification.
3. Note the file(s) affected and a revert path (commit SHA or undo
   command).
4. Proceed.

Categories: BLOCKING (work cannot continue safely — extremely rare;
proceed with safest available behavior and continue other phases),
MINOR (proceeding is fine), FUTURE (deferrable), INTERPRETIVE (a
matter of style or scope).

### Phase-gate protocol
- Read BUILD_PLAN.md at session start; resume at the first unchecked
  box in the lowest unfinished phase.
- Tick `[x]` only after the validation command for that item exits 0.
- Append a session-log line to BUILD_PLAN.md (bottom of file) before
  any `/compact` or session end: timestamp, items completed, items
  open, last commit SHA.
- Run `git add -A && git commit -m "<conventional message>"` after
  every checkbox tick. Push to `build` at least every 5 ticks.

### Commit conventions
Conventional Commits. Allowed types: `feat`, `fix`, `docs`, `chore`,
`refactor`, `test`, `ci`. Scope = phase number or skill family. Examples:
- `feat(p1): add tax-research-federal flagship skill`
- `feat(p2): add 11 prediction skills`
- `feat(p3): add 51 state stubs for income skill`
- `docs(p5): expand README install + usage`
- `chore(p7): tag v1.0.0-beta`

## SKILL.md authoring rules

Every SKILL.md MUST:

1. **YAML frontmatter** — `name` ≤ 64 chars (kebab-case, no reserved
   words `anthropic`/`claude`); `description` ≤ 1024 chars, third
   person, declarative, includes "Use when…" with concrete trigger
   phrases users actually say.
2. **Body ≤ 500 lines.** Push longer reference content into
   `references/<topic>.md` one level deep, not nested.
3. Begin with a "Read before output" list pointing to the relevant
   shared/ files (citation-discipline, authority-hierarchy,
   confidence-bands, compliance, legislation-tracking when applicable)
   and any local references.
4. Numbered workflow with Intake → Analysis → Conclusion →
   Authorities → JSON sidecar (matches shared/output-schema.json).
5. Hard rules section explicitly forbidding fabricated citations and
   reciting the [CITATION NEEDED — search: <query>] sentinel pattern.
6. Verification checklist appendix: SSTS §1.1/§2.3 + Circular 230
   §10.22/§10.37 items the practitioner must confirm.

For the two state research skills (`tax-research-state-income` and
`tax-research-state-salesuse`), the SKILL.md must additionally include
a state-router section that lists all 51 jurisdiction codes and
documents the routing protocol: when the user mentions a state by
name, abbreviation, or distinctive feature, load the corresponding
`references/states/<XX>.md` before drafting analysis.

For the `irc-section-lookup` skill, the SKILL.md must implement the
Public-Law-to-USC workflow described in shared/legislation-tracking.md:
when the user references a Public Law by popular name (TCJA, IRA,
OBBBA, SECURE 2.0, etc.) or by Public Law number, the skill must use
the USC Popular Name Tool and Classification Tables to resolve all
affected USC sections.

Match the style and rigor of the three flagship exemplars:
@skills/tax-research-federal/SKILL.md
@skills/predict-worker-classification/SKILL.md
@skills/return-summary-1040/SKILL.md

If any of those three files do not yet exist, create them first using
the drafts referenced in BUILD_PLAN.md Phase 1 and the
docs/skill-template.md template.

## State scope
State coverage is ALL 50 states + DC (51 jurisdictions). Phase 3
includes creating 102 state stub files (51 each in
tax-research-state-income/references/states/ and
tax-research-state-salesuse/references/states/). Each is copied from
shared/state-template.md with the canonical agency URL pre-filled
from shared/sources.json. Stubs ship with `status: stub` and TODO
markers — they are intentionally incomplete and will be filled in
post-launch by Kurt and contributors. Do NOT block on substantive
state research; populate the frontmatter and primary agency URL,
flag the no-income-tax / no-sales-tax states in their bodies, and
move on.

## Citation discipline (immutable)

You MUST NOT fabricate citations. If you cannot point to a primary
source you have actually retrieved or that the user has provided:
- Emit `[CITATION NEEDED — search: <specific query>]` exactly.
- Add an entry to the JSON sidecar's `unresolved_citations` array
  with the search query, the proposition, and date.

When citing, every citation entry in the JSON sidecar must include:
`authority_type, citation, url, retrieved_date, quoted_text` (≤ 75
words excerpt). No paraphrase passes for `quoted_text`.

Authority hierarchy and weighting follow Treas. Reg. §1.6662-4(d)(3).
Loper Bright (2024) ended Chevron — flag any post-2024 reliance on
Treasury Regulations as Skidmore-deference review.

State stub files use `TODO:` markers (NOT `[CITATION NEEDED]`)
because their content is intentionally placeholder. The CI grep for
fabricated citations excludes `references/states/`.

The pack uses free primary sources only. There is no free equivalent
of a commercial citator (KeyCite, Shepards, BCite, Citator 2nd) for
detecting implicit overrules. Skill outputs that touch contested
positions should explicitly note this limitation in the
verification checklist appendix.

## Compliance posture

Every research, prediction, summary, and planning skill output MUST
include the verification checklist scaffolding referenced in
shared/compliance.md. The checklist enforces:
- AICPA SSTS §1.1 (realistic possibility) and §2.3 (estimates)
- Circular 230 §10.22 (diligence), §10.35 (competence), §10.37
  (written advice — reasonable practitioner standard)
- Disclosure flagging (Form 8275 / 8275-R when reasonable basis
  with disclosure is the chosen path)

## Build environment

- Repo: KisaesDevLab/vibe-claude-tax-research-skills
- Default branch: main (protected; do NOT push directly)
- Working branch: claude/build-vibe-cpa-skills-3bct8 (push freely)
- Open one PR per phase: `gh pr create --base main --head <build-branch> --fill`
- CI must be green before phase tick-off

## What NOT to do
- Don't fabricate IRC sections, case names, Reg cites, or PLR numbers.
- Don't push to main, force-push, or rewrite published history.
- Don't bake live API keys, client data, or PII into examples.
- Don't claim Chevron deference for Treasury Regs (post-Loper Bright).
- Don't include §831(b) micro-captives or syndicated conservation
  easements in the strategy library without the explicit
  Dirty-Dozen / Listed Transaction warning banner.
- Don't embed copyrighted treatise content; cite primary sources only.
- Don't exceed 1024 chars in any SKILL.md `description` field.
- Don't put plugin components inside `.claude-plugin/` — only
  plugin.json and marketplace.json belong there.
- Don't block Phase 3 on substantive state research; ship stubs.
- Don't let a blog or commentary site (TaxProf Blog, Procedurally
  Taxing, Tax Foundation, Tax Policy Center) drive a confidence band.
  These are tagged `not_authority` or `persuasive_non_authority` only.
