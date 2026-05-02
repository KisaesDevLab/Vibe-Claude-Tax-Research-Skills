# Kisaes CPA Skills Pack — Autonomous Build Plan for Claude Code

**Version 1.1** — folds in additions surfaced by review of seven law-library tax-research guides (Illinois, NYU, UIC, Vanderbilt, Harvard, uscode.house.gov, Cornell LII).

This is the complete executable plan Kurt hands to Claude Code. Every artifact is production-ready and copy-pasteable. Read top to bottom; the **Handoff Prompt in Section L** is the single message that kicks off the autonomous build.

---

## What's new in v1.1

These changes are folded throughout the document below; this section is a quick scannable summary of what changed from v1.0.

- **New shared file**: `shared/legislation-tracking.md` documenting the USC Classification Tables / Popular Name Tool / JCT Bluebook / Treasury Greenbook / CBO score workflow.
- **`shared/sources.json` extended** with nine new blocks: `irs_extended`, `tax_court_extended`, `doj_tax_division`, `uscode_tools`, `legislative_branch`, `policy_data`, `international_extended`, `free_case_databases_extended`, `current_awareness_non_authority`.
- **`shared/live-sources.md` extended** with corresponding sections.
- **`shared/citation-discipline.md`** authority_type list extended with `FSA`, `OfficeMemo`, `InfoLetter`, `TreasuryDecision`, `ATG`, `ISPPaper`, `IRSNewsRelease`, `Greenbook`, `CBOReport`, `StatutesAtLarge`.
- **`shared/citation-discipline.md`** explicitly notes the negative-treatment-detection limitation (no free citator equivalent of KeyCite/Shepards).
- **`shared/authority-hierarchy.md`** cites IRS "Understanding IRS Guidance — A Brief Primer" as the IRS's own published view of the guidance hierarchy.
- **`shared/state-template.md`** gains an optional "Secondary policy data" reference block (Tax Foundation Center for State Tax Policy + Tax Policy Center).
- **`irc-section-lookup`** gets `references/legislation-tracking.md` and `references/subtitle-map.md` and a Public-Law-to-USC workflow section.
- **`tax-research-federal`** picks up legislative-history workflow citations to JCT, House W&M, Senate Finance, Treasury Greenbooks, CBO.
- **`tax-research-procedure`** picks up Tax Court Rules, DOJ Tax Division, IRS Data Book, and DAWSON Today's Opinions/Orders feeds.
- **`tax-research-international`** picks up IRS Treaties A–Z and OECD Tax.
- **`predict-reasonable-cause`** picks up IRS Data Book penalty-abatement statistics as `persuasive_non_authority`.
- **State research skills** pick up Tax Foundation Center for State Tax Policy as `persuasive_non_authority` secondary supplement.
- **`.claude/settings.local.json`** WebFetch allowlist extended with: `justice.gov`, `jct.gov`, `waysandmeans.house.gov`, `finance.senate.gov`, `home.treasury.gov`, `cbo.gov`, `loc.gov`, `taxfoundation.org`, `taxpolicycenter.org`, `ustaxcourt.gov`, `apps.irs.gov`, `legalbitstream.com`, `taxprof.typepad.com`, `procedurallytaxing.com`, `appellatetax.com`, `oecd.org`.
- **CI workflow** validates the new shared file exists and the extended `authority_type` taxonomy is consistent.

---

## A. Pre-flight checklist

Run these on Kurt's workstation before pasting the handoff prompt. All must succeed.

```bash
# 1. GitHub CLI authenticated to KisaesDevLab org
gh auth status                                         # must show "Logged in"
gh api user --jq .login                                # confirm account
gh api orgs/KisaesDevLab --jq .login                   # confirm org access

# 2. Git identity set
git config --global user.name                          # not empty
git config --global user.email                         # matches GitHub

# 3. Claude Code installed + authenticated
claude --version                                       # >= 2.1.x
claude /status                                         # logged in, model visible

# 4. Required CLIs
which jq yq curl bash gh git node python3              # all present

# 5. Working directory clean and dedicated
mkdir -p ~/code/kisaes && cd ~/code/kisaes
test -z "$(ls -A .)" && echo "OK clean directory"     # empty

# 6. Optional: pull skill-creator locally as a reference (the path
#    /mnt/skills/example/skill-creator only exists inside Anthropic's
#    hosted Claude.ai sandbox — NOT on local Claude Code)
git clone --depth 1 https://github.com/anthropics/skills.git /tmp/anthropic-skills
ls /tmp/anthropic-skills/skills/skill-creator/SKILL.md # confirm exists

# 7. Confirm the model you intend to use is the default
#    As of April 2026: Pro/Team plans default to Sonnet 4.6.
#    Recommended for this build: Sonnet 4.6 (cost/throughput) with
#    `/model opus` switches for Phase 1 flagship and Phase 7 tagging.
```

If any check fails, fix it before continuing.

---

## B. Repository name recommendation

**`vibe-cpa-skills`** — recommended.

Rationale: places the pack inside Kurt's existing **Vibe** brand (Vibe Trial Balance is the sister repo), uses the public-facing product family ("Vibe CPA Skills"), is descriptive enough that a non-Anthropic engineer browsing KisaesDevLab understands what it is, and avoids overloading the word "skills" with the official `anthropic/skills` repo.

Plugin/marketplace identifiers inside the repo:
- marketplace `name`: `kisaes-cpa-skills`
- plugin `name`: `vibe-cpa-pack`

---

## C. Bootstrap bash script (one-shot, idempotent)

Save as `~/bootstrap-vibe-cpa-skills.sh` and run once. Idempotent: rerunning is safe.

```bash
#!/usr/bin/env bash
set -euo pipefail

ORG="KisaesDevLab"
REPO="vibe-cpa-skills"
ROOT="$HOME/code/kisaes/$REPO"
DEFAULT_BRANCH="main"
BUILD_BRANCH="build"

mkdir -p "$ROOT" && cd "$ROOT"

# 1. git init
if [ ! -d .git ]; then
  git init -b "$DEFAULT_BRANCH"
fi

# 2. Create the directory skeleton
mkdir -p \
  skills shared scripts evals examples docs \
  .claude-plugin .claude/commands .claude/hooks .github/workflows

# 3. .gitignore
cat > .gitignore <<'GITIGNORE'
# Claude Code local
.claude/settings.local.json
.claude/.session/
CLAUDE.local.md
.cache/
node_modules/
__pycache__/
*.pyc
.venv/
.DS_Store
.env
.env.*
!.env.example
dist/
build-artifacts/
evals/runs/
GITIGNORE

# 4. LICENSE (BSL 1.1 with 4-year change date)
TODAY="$(date -u +%Y-%m-%d)"
CHANGE_DATE="$(date -u -d '+4 years' +%Y-%m-%d 2>/dev/null || date -v+4y -u +%Y-%m-%d)"
cat > LICENSE <<LICENSE
Business Source License 1.1

Licensor: Kisaes LLC
Licensed Work: Vibe CPA Skills (vibe-cpa-skills)
                Copyright (c) ${TODAY%%-*} Kisaes LLC
Additional Use Grant: You may use the Licensed Work for non-production
  internal evaluation, education, and the personal practice of any
  licensed CPA, EA, or attorney advising fewer than 100 clients.
Change Date: ${CHANGE_DATE}
Change License: Apache License, Version 2.0

For full BSL 1.1 terms see https://mariadb.com/bsl11/
LICENSE

# 5. Skeleton DISCLAIMER, CONTRIBUTING, CHANGELOG
cat > DISCLAIMER.md <<'EOF'
# Disclaimer

Vibe CPA Skills is **professional reference tooling for licensed CPAs,
EAs, and tax attorneys**. It is NOT tax advice, NOT a substitute for
professional judgment, and does NOT establish a client relationship.

Outputs may be incomplete, out of date, or wrong. Every authority cited
must be independently verified against the primary source by a competent
practitioner before being relied on for a tax position. The pack
implements AICPA SSTS and Circular 230 §10.22/§10.37 verification
checklists; the human practitioner is responsible for completing them.

Free-source citation discipline cannot detect implicit overrules with
the same coverage as a commercial citator (KeyCite, Shepards, BCite,
Citator 2nd). Practitioners relying on outputs for high-stakes
positions should run a citator check independently.
EOF

cat > CONTRIBUTING.md <<'EOF'
# Contributing
Issues and PRs welcome. By submitting, you agree your contribution is
licensed under the project's BSL 1.1 license. All SKILL.md changes must
pass `./scripts/validate.sh` and include at least one eval case.
EOF

cat > CHANGELOG.md <<'EOF'
# Changelog
All notable changes documented here. Format follows Keep a Changelog;
versions follow SemVer.

## [Unreleased]
EOF

# 6. README skeleton (Claude Code expands during Phase 5)
cat > README.md <<'EOF'
# Vibe CPA Skills

A 28-skill Claude Skills pack for CPAs covering all 50 states + DC.
Replicates the core capabilities of Holistiplan, Blue J Tax, TaxPlanIQ,
CPA Pilot, and TaxGPT, packaged as installable Claude Skills with
strict citation discipline and AICPA SSTS / Circular 230 compliance
scaffolding.

(Full README expanded by build process — see BUILD_PLAN.md Phase 5.)
EOF

# 7. Create the GitHub repo (private first; flip to public after review)
if ! gh repo view "$ORG/$REPO" >/dev/null 2>&1; then
  gh repo create "$ORG/$REPO" \
    --private \
    --description "28-skill Claude Skills pack for CPAs (Vibe family) — all 50 states + DC" \
    --source . \
    --remote origin \
    --push=false
fi

# 8. First commit on main
git add -A
git commit -m "chore: bootstrap repo skeleton" || true
git push -u origin "$DEFAULT_BRANCH"

# 9. Build branch
git checkout -B "$BUILD_BRANCH"
git push -u origin "$BUILD_BRANCH"

# 10. Branch protection on main (best-effort; ignore if perms missing)
gh api -X PUT "repos/$ORG/$REPO/branches/$DEFAULT_BRANCH/protection" \
  -F required_pull_request_reviews.dismiss_stale_reviews=true \
  -F required_pull_request_reviews.required_approving_review_count=0 \
  -F enforce_admins=false \
  -F required_status_checks.strict=true \
  -F required_status_checks.contexts='["validate"]' \
  -F restrictions= 2>/dev/null || \
  echo "(branch protection skipped — set later via UI)"

echo "✅ Bootstrap complete. cd $ROOT && claude"
```

After running the script, the rest of the build is performed by Claude Code reading `CLAUDE.md` and `BUILD_PLAN.md`. **Sections D–K below are the file contents Claude Code expects to find. Drop them in before the first Claude Code session.**

---

## D. CLAUDE.md (production)

Path: `CLAUDE.md` (committed, repo root)

```markdown
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

- Repo: KisaesDevLab/vibe-cpa-skills
- Default branch: main (protected; do NOT push directly)
- Working branch: build (push freely)
- Open one PR per phase: `gh pr create --base main --head build --fill`
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
```

---

## E. BUILD_PLAN.md (production)

Path: `BUILD_PLAN.md` (committed)

```markdown
# Build Plan — Vibe CPA Skills

**Goal:** Ship `v1.0.0-beta` with 28 skills, 1 dispatcher, 8 shared
files, 102 state stub files, full eval harness, README, and a green CI.

Tick `[x]` only after the validation command for that line exits 0.

---

## Phase 0 — Bootstrap verification & shared/

Validation: `./scripts/validate.sh phase 0`

- [ ] Confirm directory tree matches: skills/ shared/ scripts/ evals/
      examples/ docs/ .claude-plugin/ .claude/ .github/
- [ ] Confirm files: CLAUDE.md, BUILD_PLAN.md, QUESTIONS.md,
      LICENSE (BSL 1.1), DISCLAIMER.md, CONTRIBUTING.md,
      CHANGELOG.md, README.md, .gitignore
- [ ] Write shared/citation-discipline.md
- [ ] Write shared/authority-hierarchy.md
- [ ] Write shared/confidence-bands.md
- [ ] Write shared/compliance.md
- [ ] Write shared/live-sources.md (incl. all 50 + DC table; incl.
      extended IRS, Tax Court, USC tools, legislative branch,
      policy data, international, current-awareness sections)
- [ ] Write shared/sources.json (incl. all 51 state_dors entries
      AND extended blocks: irs_extended, tax_court_extended,
      doj_tax_division, uscode_tools, legislative_branch,
      policy_data, international_extended, free_case_databases_extended,
      current_awareness_non_authority)
- [ ] Write shared/output-schema.json
- [ ] Write shared/state-template.md (incl. optional Secondary
      policy data section)
- [ ] Write shared/legislation-tracking.md (NEW in v1.1)
- [ ] Write docs/skill-template.md
- [ ] Write scripts/validate.sh (validates frontmatter, description
      length, JSON parse, URL liveness, state-stub completeness,
      authority_type taxonomy consistency)
- [ ] Write scripts/run-evals.sh (subagent-pair harness; reads
      evals/<family>/<skill>.json)
- [ ] Write .github/workflows/validate.yml
- [ ] Write .claude-plugin/plugin.json skeleton
- [ ] Write .claude-plugin/marketplace.json skeleton
- [ ] Commit: `chore(p0): bootstrap shared/ + scripts + CI skeleton`
- [ ] Push to build; open draft PR to main

## Phase 1 — Three flagship skills + dispatcher + eval harness

Validation: `./scripts/validate.sh phase 1 && ./scripts/run-evals.sh phase 1`

- [ ] skills/cpa-pack-index/SKILL.md (always-on dispatcher; routes
      Public-Law popular names like "OBBBA"/"TCJA" to irc-section-lookup)
- [ ] skills/tax-research-federal/SKILL.md (flagship)
- [ ] skills/tax-research-federal/references/{authority-weights.md, retrieval-checklist.md, legislative-history.md}
- [ ] skills/predict-worker-classification/SKILL.md (flagship)
- [ ] skills/predict-worker-classification/references/{factors-20.md,case-law.md}
- [ ] skills/return-summary-1040/SKILL.md (flagship)
- [ ] skills/return-summary-1040/references/{line-keys.md,red-flags.md}
- [ ] evals/research/tax-research-federal.json (≥ 3 cases; include 1
      legislative-history case exercising JCT/Greenbook/CBO citations)
- [ ] evals/prediction/predict-worker-classification.json (≥ 3 cases)
- [ ] evals/summary/return-summary-1040.json (≥ 3 cases)
- [ ] CI green
- [ ] Commit: `feat(p1): three flagships + dispatcher + eval harness`

## Phase 2 — Prediction (11) + research (4) + 1 summary + notice

Validation: `./scripts/validate.sh phase 2 && ./scripts/run-evals.sh phase 2`

Predictions (11 — worker-classification already in Phase 1):
- [ ] predict-hobby-loss
- [ ] predict-reasonable-comp
- [ ] predict-real-estate-pro
- [ ] predict-material-participation
- [ ] predict-qbi-eligibility
- [ ] predict-1031-qualification
- [ ] predict-economic-substance
- [ ] predict-debt-vs-equity
- [ ] predict-innocent-spouse
- [ ] predict-reasonable-cause
      (references include: irs-data-book-penalty-stats.md citing
      IRS Data Book penalty-abatement statistics as
      persuasive_non_authority)
- [ ] predict-r-and-d-credit

Research (4 — federal already in Phase 1):
- [ ] tax-research-entity
- [ ] tax-research-payroll
- [ ] tax-research-international
      (references include: treaties-a-to-z.md pointing to IRS
      Treaties A–Z; oecd-model-treaty.md pointing to OECD Tax)
- [ ] tax-research-procedure
      (references include: tax-court-rules.md, doj-tax-division.md,
      irs-data-book-audit-rates.md, dawson-freshness-feeds.md)

Summary + notice:
- [ ] return-summary-entity
- [ ] notice-response

For each: SKILL.md + references/ + 1 eval case minimum.
- [ ] Commit per family with conventional message; push frequently.

## Phase 3 — Planning (3) + remaining research (3) + utilities (5) + compliance (1) + 51 state stubs × 2 skills

Validation: `./scripts/validate.sh phase 3 && ./scripts/run-evals.sh phase 3`

### 3a. Planning skills
- [ ] planning-actions-1040
- [ ] planning-actions-entity
- [ ] planning-multi-year
      (references include: legislation-tracking-pointer.md
      cross-referencing shared/legislation-tracking.md for
      reconciliation-bill scoring context)

### 3b. Remaining research skills (state shells + estate/gift)
- [ ] tax-research-state-income (SKILL.md + references/ + state router logic)
- [ ] tax-research-state-salesuse (SKILL.md + references/ + state router logic)
- [ ] tax-research-estate-gift

### 3c. Utilities
- [ ] irc-section-lookup
      (references include: legislation-tracking.md implementing the
      Public-Law-to-USC workflow per shared/legislation-tracking.md;
      subtitle-map.md documenting IRC Subtitles A–K)
- [ ] treas-reg-lookup
      (references include: treasury-decisions.md distinguishing TDs
      from codified TreasReg)
- [ ] form-line-explainer
- [ ] due-date-calculator
- [ ] penalty-interest-calc

### 3d. Compliance
- [ ] compliance-ssts-circular230
      (references include: irs-guidance-primer.md citing the IRS
      "Understanding IRS Guidance — A Brief Primer" page)

### 3e. State stubs — tax-research-state-income (51 files)

For each jurisdiction, copy `shared/state-template.md` to
`skills/tax-research-state-income/references/states/<XX>.md`,
populate the YAML frontmatter, and pre-fill the primary agency URL
from `shared/sources.json`. Status remains `stub` until edited.

- [ ] AL — Alabama
- [ ] AK — Alaska *(no individual income tax — note in body)*
- [ ] AZ — Arizona
- [ ] AR — Arkansas
- [ ] CA — California *(FTB primary; note CDTFA/EDD splits)*
- [ ] CO — Colorado
- [ ] CT — Connecticut
- [ ] DE — Delaware
- [ ] DC — District of Columbia
- [ ] FL — Florida *(no individual income tax)*
- [ ] GA — Georgia
- [ ] HI — Hawaii
- [ ] ID — Idaho
- [ ] IL — Illinois
- [ ] IN — Indiana
- [ ] IA — Iowa
- [ ] KS — Kansas
- [ ] KY — Kentucky
- [ ] LA — Louisiana
- [ ] ME — Maine
- [ ] MD — Maryland
- [ ] MA — Massachusetts *(note 4% surtax over $1M)*
- [ ] MI — Michigan
- [ ] MN — Minnesota
- [ ] MS — Mississippi
- [ ] MO — Missouri
- [ ] MT — Montana
- [ ] NE — Nebraska
- [ ] NV — Nevada *(no individual income tax)*
- [ ] NH — New Hampshire *(I&D tax repealed 2025)*
- [ ] NJ — New Jersey
- [ ] NM — New Mexico
- [ ] NY — New York *(note convenience-of-employer rule)*
- [ ] NC — North Carolina
- [ ] ND — North Dakota
- [ ] OH — Ohio
- [ ] OK — Oklahoma
- [ ] OR — Oregon
- [ ] PA — Pennsylvania
- [ ] RI — Rhode Island
- [ ] SC — South Carolina
- [ ] SD — South Dakota *(no individual income tax)*
- [ ] TN — Tennessee *(Hall tax repealed)*
- [ ] TX — Texas *(no individual income tax)*
- [ ] UT — Utah
- [ ] VT — Vermont
- [ ] VA — Virginia
- [ ] WA — Washington *(capital gains tax in effect; no general income tax)*
- [ ] WV — West Virginia
- [ ] WI — Wisconsin
- [ ] WY — Wyoming *(no individual income tax)*

Validation: `test "$(ls skills/tax-research-state-income/references/states/*.md | wc -l)" -eq 51`

### 3f. State stubs — tax-research-state-salesuse (51 files)

Same procedure. Where a state has no sales tax (AK¹, DE, MT, NH, OR),
include a reference file noting the fact and pointing to local-option
authority where applicable.
¹ Alaska has no statewide sales tax but local sales taxes; flag clearly.

- [ ] AL [ ] AK [ ] AZ [ ] AR [ ] CA [ ] CO [ ] CT [ ] DE [ ] DC [ ] FL
- [ ] GA [ ] HI [ ] ID [ ] IL [ ] IN [ ] IA [ ] KS [ ] KY [ ] LA [ ] ME
- [ ] MD [ ] MA [ ] MI [ ] MN [ ] MS [ ] MO [ ] MT [ ] NE [ ] NV [ ] NH
- [ ] NJ [ ] NM [ ] NY [ ] NC [ ] ND [ ] OH [ ] OK [ ] OR [ ] PA [ ] RI
- [ ] SC [ ] SD [ ] TN [ ] TX [ ] UT [ ] VT [ ] VA [ ] WA [ ] WV [ ] WI [ ] WY

Validation: `test "$(ls skills/tax-research-state-salesuse/references/states/*.md | wc -l)" -eq 51`

### 3g. State router logic
Both state SKILL.md files must implement a routing pattern: when the
user mentions a state by name, abbreviation, or distinctive feature
(e.g., "FTB", "Comptroller", "convenience rule"), the skill loads the
corresponding `references/states/<XX>.md` before drafting analysis.

- [ ] tax-research-state-income SKILL.md includes state router section
- [ ] tax-research-state-salesuse SKILL.md includes state router section
- [ ] Both list all 51 jurisdiction codes in a "Supported jurisdictions"
      block at the top of the SKILL.md body.
- [ ] Both reference Tax Foundation Center for State Tax Policy as
      `persuasive_non_authority` secondary supplement (NOT authority)
      with explicit caveat language.

### 3h. Phase commit
- [ ] `/commit-phase 3 "planning + state shells + 51 state stubs × 2"`

## Phase 4 — Strategy library (30 entries)

Validation: `./scripts/validate.sh phase 4`

- [ ] skills/planning-strategy-library/SKILL.md
- [ ] skills/planning-strategy-library/references/strategies/<slug>.md
      for all 30 strategies (list in shared/strategy-list.md derived
      from this plan's appendix)
- [ ] Each strategy file: IRC §, eligibility, mechanics, citations,
      Dirty-Dozen / Listed-Transaction flag where applicable
- [ ] Strategies with state-specific eligibility (PTET, CA AB5, NY
      convenience rule, MA millionaire surtax, WA capital gains tax,
      OR transit tax) reference per-state files via:
      `> See state files for jurisdiction-specific eligibility: CA, NY, ...`
- [ ] Strategies materially affected by recent legislation (post-2024)
      reference shared/legislation-tracking.md and link to
      Classification Tables for the relevant Public Law.
- [ ] index.md cross-references all 30
- [ ] Commit: `feat(p4): 30-strategy planning library`

## Phase 5 — Examples, docs, README, marketplace

Validation: `./scripts/validate.sh phase 5`

- [ ] examples/research-federal/{prompt.md, expected-output.json}
- [ ] examples/predict-worker-classification/...
- [ ] examples/return-summary-1040/...
- [ ] examples/notice-response/...
- [ ] examples/state-research-CA/...
- [ ] examples/state-research-NY-convenience-rule/...
- [ ] examples/legislation-tracking-OBBBA/{prompt.md, expected-output.json}
      (NEW in v1.1: exercises Public-Law-to-USC workflow)
- [ ] docs/install-claude-ai.md (ZIP upload flow)
- [ ] docs/install-claude-code.md (`/plugin marketplace add` flow)
- [ ] docs/authoring-guide.md
- [ ] docs/state-stub-promotion.md (how to promote stub → draft → reviewed → verified)
- [ ] docs/legislation-tracking-howto.md (NEW in v1.1: practitioner-
      facing guide on how the pack tracks Public-Law impact)
- [ ] Expand README.md: install, usage, skills index table, state
      coverage table, compliance posture, license, contribution
- [ ] Finalize .claude-plugin/plugin.json (full skills array)
- [ ] Finalize .claude-plugin/marketplace.json
- [ ] CHANGELOG.md updated
- [ ] Commit: `docs(p5): examples, docs, README polish`

## Phase 6 — Eval expansion + final QA

Validation: `./scripts/run-evals.sh full`

- [ ] ≥ 3 eval cases per skill (28 × 3 = 84 minimum)
- [ ] State router eval: 1 case per state research skill exercising a
      non-priority state (suggested: AK sales-tax, NH I&D transition,
      TN Hall-repealed, WA cap gains)
- [ ] Legislation-tracking eval: 1 case in irc-section-lookup
      exercising a Public-Law popular name → USC sections workflow
- [ ] Eval pass rate ≥ 80% on each skill
- [ ] `claude plugin validate .` exits 0
- [ ] All URLs in shared/live-sources.md return non-error (allow ≤ 5
      flakes; retry once)
- [ ] All SKILL.md frontmatter validates (description ≤ 1024)
- [ ] All JSON in references/ parses
- [ ] All 51 state stubs exist and have matching state_code frontmatter
      in BOTH state research skills (102 files total)
- [ ] No fabricated-citation sentinels remain except in template files
- [ ] Every authority_type used in any references file appears in the
      enumeration in shared/citation-discipline.md
- [ ] Commit: `test(p6): full eval suite + QA`

## Phase 7 — Release

Validation: `gh release view v1.0.0-beta` (DO NOT auto-create the
release; open a PR and stop)

- [ ] Open PR build → main: `gh pr create --base main --head build --fill`
- [ ] Wait for CI green
- [ ] In PR body, request Kurt's review and tag-creation approval
- [ ] Add a final BUILD_PLAN.md session-log entry
- [ ] STOP. Kurt merges, tags v1.0.0-beta, and creates the release.

---

## Session log
(Claude Code appends entries here before each /compact or exit.
Format: `YYYY-MM-DD HH:MM | phase X | items: ... | last commit: <sha>`)
```

---

## F. shared/ files (production)

### F.1 `shared/citation-discipline.md`

```markdown
# Citation discipline

## Hard rule
Never fabricate a citation. If you cannot ground a proposition in a
primary source you have actually retrieved (or that has been provided
to you), you must:
1. Emit the sentinel `[CITATION NEEDED — search: <specific query>]`
   inline at the point of the proposition.
2. Add an entry to the JSON sidecar's `unresolved_citations` array.
3. Lower the confidence band by at least one step (see
   confidence-bands.md).

A "primary source" is the IRC section, the Treasury Regulation, the
court opinion, the Revenue Ruling/Procedure/Notice, the PLR/TAM, the
Form/Instructions, the state DOR pronouncement, or a comparable
authoritative document — accessed at its canonical URL listed in
live-sources.md.

## Stub vs. published files
State stub files at `references/states/<XX>.md` use `TODO:` markers
(NOT `[CITATION NEEDED]`) because their content is intentionally
placeholder pending practitioner edits. The CI grep for fabricated
citations excludes `references/states/`. When a state stub is
promoted to `status: reviewed` or `verified`, all `TODO:` markers
must be resolved or replaced with `[CITATION NEEDED]` sentinels for
items still requiring research.

## Required fields per citation
Every citation in the `authorities` array of the JSON sidecar MUST
include:
- `authority_type`: one of (extended in v1.1):
  - **Primary federal**: `IRC`, `TreasReg`, `TreasuryDecision`,
    `StatutesAtLarge`
  - **IRS published guidance (IRB)**: `RevRul`, `RevProc`, `Notice`,
    `Announcement`
  - **IRS written determinations**: `PLR`, `TAM`, `CCA`, `GCM`, `AOD`,
    `FSA`, `OfficeMemo`, `InfoLetter`
  - **IRS practice/published**: `IRSPub`, `IRM`, `ATG`, `ISPPaper`,
    `IRSNewsRelease`
  - **Legislative**: `JCT_BlueBook`, `LegHistory`, `Greenbook`,
    `CBOReport`
  - **Federal courts**: `SCOTUS`, `CtAppeals`, `TaxCt`, `DistCt`,
    `CtFedClaims`
  - **State**: `StateStatute`, `StateReg`, `StateAdmin`, `StateCt`
  - **Treaty**: `Treaty`
  - **Forms**: `Form`, `Instructions`
- `citation`: human-readable cite (e.g., "I.R.C. § 199A(a)(1)" or
  "Treas. Reg. § 1.199A-1(b)(14)" or "Watson v. United States, 668
  F.3d 1008 (8th Cir. 2012)")
- `url`: canonical URL from live-sources.md
- `retrieved_date`: ISO 8601 (YYYY-MM-DD)
- `quoted_text`: ≤ 75 words verbatim excerpt that supports the cited
  proposition. Paraphrase is not acceptable for this field.
- `pin_cite`: optional — paragraph, line, or footnote pointer
- `weight`: see authority-hierarchy.md (`primary_statute`,
  `binding_judicial`, `regulation`, `binding_circuit`, `judicial`,
  `irs_published`, `legislative_history`, `written_determinations`,
  `persuasive_non_authority`, `not_authority`)

## Authority-type-to-weight default mapping (v1.1)

| authority_type | default weight |
|---|---|
| `IRC`, `StatutesAtLarge`, `Treaty` | `primary_statute` |
| `SCOTUS` | `binding_judicial` |
| `TreasReg`, `TreasuryDecision` | `regulation` |
| `CtAppeals` | `binding_circuit` (in taxpayer's circuit) or `judicial` (other circuits) |
| `TaxCt`, `DistCt`, `CtFedClaims` | `judicial` |
| `RevRul`, `RevProc`, `Notice`, `Announcement` | `irs_published` |
| `JCT_BlueBook`, `LegHistory`, `Greenbook`, `CBOReport` | `legislative_history` |
| `PLR`, `TAM`, `CCA`, `GCM`, `AOD`, `FSA`, `OfficeMemo`, `InfoLetter` | `written_determinations` |
| `IRSPub`, `IRM`, `ATG`, `ISPPaper`, `IRSNewsRelease`, `Form`, `Instructions` | `persuasive_non_authority` |
| `StateStatute` | `primary_statute` (state-tier) |
| `StateReg` | `regulation` (state-tier) |
| `StateCt` | `judicial` (state-tier) |
| `StateAdmin` | `persuasive_non_authority` to `judicial` depending on body |

The mapping is a default. Skills may override with rationale recorded
in the citation entry's `weight_override_rationale` field.

## Sentinel format
Use exactly: `[CITATION NEEDED — search: <query>]`
Examples:
- `[CITATION NEEDED — search: §199A QBI deduction wage limitation 2024]`
- `[CITATION NEEDED — search: Watson reasonable comp 8th Circuit]`

## Graceful degradation ladder
When a primary source is unreachable mid-task, descend in order:
1. Same authority via mirror URL (e.g., Cornell LII for eCFR).
2. A higher authority that subsumes the proposition (Code section
   that directly states the rule).
3. A clearly-labeled IRS Publication or IRM citation, marked
   `weight: persuasive_non_authority`, with explicit caveat in the
   conclusion.
4. Sentinel + `unresolved_citations` entry + lowered confidence band.
Never silently substitute a treatise, blog, or AI summary.

## Out-of-date detection
If `retrieved_date` is older than 365 days for a proposition tied to
a regulation that may have been amended, emit a `staleness_warning`
in the sidecar with the recommended re-verification date.

## Loper Bright caveat (post-Chevron)
Treasury Regulations no longer command Chevron deference. When
relying on a Treasury Regulation's interpretation of an ambiguous
statute, flag `chevron_replaced: true` and note that a court would
review the regulation under Skidmore (Loper Bright Enterprises v.
Raimondo, 144 S. Ct. 2244 (2024)).

## Negative-treatment-detection limitation (v1.1)

The pack relies on free primary sources only. There is **no free
equivalent** of a commercial citator (KeyCite, Shepards, BCite,
Citator 2nd) capable of detecting implicit overrules with
comprehensive coverage.

Mitigations the skills implement:
- Authority-weight rules drop one band when retrieved_date > 365 days
  in fast-moving areas (state SALT/PTET, R&D §174 capitalization,
  OZ rules) — see confidence-bands.md.
- DAWSON Today's Opinions / Today's Orders feeds are consulted for
  freshness signals on Tax Court authorities.
- The Federal Register IRS feed is consulted for new TDs and proposed
  regs that may supersede current guidance.

Mitigations the skills do NOT implement (residual practitioner
responsibility):
- Comprehensive negative-treatment review of cited cases.
- Detection of implicit overrules outside the freshness window.

Every output's verification checklist appendix must explicitly call
out this residual practitioner responsibility.

## Current-awareness sources are NOT authority

TaxProf Blog, Procedurally Taxing, Tax Appellate Blog, Tax Foundation,
Tax Policy Center, and similar sources are listed in live-sources.md
as current-awareness signals. They are tagged `weight: not_authority`
or at most `persuasive_non_authority`. They MUST NOT drive a
confidence band assignment, and they MUST NOT appear as the closest
authority for any cited proposition.
```

### F.2 `shared/authority-hierarchy.md`

```markdown
# Authority hierarchy

Recognized "authority" follows Treas. Reg. § 1.6662-4(d)(3)(iii). Use
this table to assign `weight` to every citation in the JSON sidecar.

For the IRS's own published view of the guidance hierarchy, see
"Understanding IRS Guidance — A Brief Primer" at
https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer
(cite as `IRSNewsRelease`/`persuasive_non_authority` — note that the
IRS's own characterization of authority weight is itself not authority,
but is useful as a malpractice-defense scaffolding artifact).

## Weights

| Tier | Weight key | Authorities |
|---|---|---|
| 1 | `primary_statute` | Internal Revenue Code; tax treaties + Treasury explanations; state statutes |
| 2 | `binding_judicial` | U.S. Supreme Court decisions |
| 3 | `regulation` | Treasury Regulations: final > temporary > proposed (post-Loper Bright reviewed under Skidmore); state agency regulations |
| 4 | `binding_circuit` | U.S. Court of Appeals (controlling in taxpayer's circuit; Tax Court applies the *Golsen* rule) |
| 5 | `judicial` | U.S. Tax Court regular & memorandum, District Courts, Court of Federal Claims, state appellate courts |
| 6 | `irs_published` | Revenue Rulings, Revenue Procedures, Notices, Announcements (IRB-published) |
| 7 | `legislative_history` | JCT Blue Book; committee/conference reports; floor statements by bill managers; Treasury Greenbooks; CBO reports |
| 8 | `written_determinations` | PLRs, TAMs, CCAs, GCMs, AODs, FSAs, Office Memorandums, Information Letters (citable; **no precedential value** to other taxpayers per § 6110(k)(3)) |
| 9 | `persuasive_non_authority` | IRS Publications, IRM, Forms/Instructions, Audit Technique Guides, ISP Coordinated Issue Papers, IRS News Releases — NOT authority under § 1.6662-4(d)(3)(iii) but persuasive of IRS practice; state DOR publications; policy-data sources (Tax Foundation, Tax Policy Center) |
| 10 | `not_authority` | Treatises, articles, blogs, AI/LLM outputs, tax-professional opinions — **never authority** |

## Weighting rules (§ 1.6662-4(d)(3)(ii))
- Authority that cogently relates law to facts > authority that
  states a conclusion.
- Newer trumps older for written determinations; > 10 years old
  generally accorded "very little weight."
- Implicit/explicit overrule strips authority status.

## Loper Bright disclosure
For any proposition resting on a Treasury Regulation's interpretation
of an ambiguous statute, set `chevron_replaced: true` in the sidecar
authority entry and note Skidmore review framework: thoroughness,
reasoning validity, consistency, persuasiveness.

## IRM and ATG disclosure
IRM, ATG, and ISP Paper citations get `weight: persuasive_non_authority`
and must be accompanied by a higher-tier authority for the underlying
legal proposition, OR the conclusion must be limited to "describes IRS
practice" rather than "the law requires."

## Golsen rule reminder
Tax Court follows the law of the U.S. Court of Appeals to which the
taxpayer's case is appealable. Identify the taxpayer's circuit before
weighting Court of Appeals authority.

## State authority
For state tax questions, weight in the analogous order:
state statute > state agency regulations > state appellate court
decisions > state administrative tribunal decisions > letter rulings
or advisory opinions (often non-precedential) > state DOR
publications. Per-state nuances live in the per-state reference
files at `skills/tax-research-state-{income,salesuse}/references/states/`.

Tax Foundation Center for State Tax Policy and Tax Policy Center are
secondary policy data sources useful for context (state conformity
tables, rate tables, recent legislative tracking) but are
`persuasive_non_authority` at most. They MUST NOT serve as the
closest authority for a state tax conclusion.

## Treasury Greenbooks and CBO reports
Treasury "Greenbooks" (Administration's Fiscal Year Revenue Proposals)
and CBO scoring reports describe **proposed** legislation and
projected revenue effects. They are `legislative_history` weight ONLY
when the proposal becomes enacted law and the Greenbook/CBO report
becomes part of the authoritative legislative-history record.
Otherwise they describe what was proposed, not what is law — tag as
`persuasive_non_authority` for purely descriptive use.
```

### F.3 `shared/confidence-bands.md`

```markdown
# Confidence bands

Confidence bands map IRC § 6662 substantial-authority standards to
labels every prediction/research/planning output must include.

| Band | Approx. probability | Statutory label | Penalty implication |
|---|---|---|---|
| **HIGH** | ≥ 70% (informal "should") to ≥ 90% ("will") | More likely than not (> 50%) when at the floor; "should/will" above | Avoids accuracy-related penalty without disclosure; meets FIN 48/ASC 740 recognition |
| **MODERATE** | ~ 40–50% | Substantial authority (§ 6662(d)(2)(B)(i)) | Avoids substantial-understatement penalty without disclosure |
| **LOW** | ~ 20–35% | Reasonable basis (Reg. § 1.6662-3(b)(3)) | Avoids negligence penalty **only with adequate disclosure** (Form 8275 / 8275-R) |
| **SPECULATIVE** | < 20% | Below reasonable basis | Penalty risk; do not recommend |

## Required band assignment

Every prediction or research conclusion MUST carry a band. The
sidecar field `confidence_band` is one of `HIGH`, `MODERATE`, `LOW`,
`SPECULATIVE`. Provide:
- `band_rationale`: one paragraph mapping authority weight + factual
  fit to the band.
- `disclosure_recommended`: boolean; true when band is LOW (adequate
  disclosure path) or whenever a position is contrary to a
  Regulation (Form 8275-R).
- `penalty_exposure`: free-text summary keyed to § 6662(b) categories.

## Decay rules
- Drop one band when authority is `persuasive_non_authority` only.
- Drop one band when retrieved_date > 365 days for a fast-moving
  area (state SALT/PTET, R&D § 174 capitalization, OZ rules).
- Drop one band when relying on a PLR/TAM/CCA/GCM/AOD/FSA/Office
  Memorandum/Information Letter as the closest authority.
- Cannot exceed MODERATE on a Treasury-Reg-only basis where the
  underlying statute is ambiguous (Loper Bright posture).
- Cannot reach HIGH on a § 6662(b)(6) noneconomic-substance question
  without a binding judicial authority on point.
- For state tax conclusions citing only a stub-status state file
  (state file `status: stub`), cannot exceed LOW until the file is
  promoted to `reviewed` or `verified`.
- Tax Foundation, Tax Policy Center, blogs, and other current-
  awareness sources do not affect the band at all (they are
  not_authority or persuasive_non_authority and never the closest
  cite).

## Practitioner thresholds (informal)
The thresholds (20% / 33% / 40% / > 50% / 70% / 90%) are
practitioner conventions, not regulatory text. Cite AICPA SSTS levels
of confidence chart when referenced.
```

### F.4 `shared/compliance.md`

```markdown
# Compliance scaffolding

Every research, prediction, summary, planning, and notice-response
output MUST end with the verification checklist below, populated by
the human practitioner. Skills emit it as a markdown appendix; the
JSON sidecar mirrors it as `verification_checklist`.

## AICPA SSTS (effective Jan. 1, 2024)

### SSTS § 1.1 — Advising on tax positions
- [ ] Position has at least a realistic possibility of being
      sustained on its merits (≈ 1-in-3), OR meets the higher
      taxing-authority standard if applicable.
- [ ] If reasonable basis with adequate disclosure: Form 8275 /
      8275-R disclosure prepared.
- [ ] Client advised of potential penalties and disclosure options.

### SSTS § 2.3 — Use of estimates
- [ ] Exact data not practicably obtainable.
- [ ] Estimates reasonable based on facts and circumstances.
- [ ] Estimates not presented with greater precision than warranted.
- [ ] Disclosure on return assessed for unusual circumstances
      (taxpayer death/illness, records destroyed, pending
      litigation, K-1 not yet received).

## Circular 230 (31 CFR Part 10)

### § 10.22 — Diligence as to accuracy
- [ ] Reasonable care in engagement, supervision, training of any
      person whose work product is being relied on.
- [ ] Correctness of representations to Treasury verified.
- [ ] Correctness of representations to client verified.

### § 10.35 — Competence
- [ ] Practitioner has the knowledge, skill, thoroughness, and
      preparation needed for this matter (or has consulted experts /
      studied the law).

### § 10.37 — Written advice (reasonable practitioner standard)
- [ ] Reasonable factual and legal assumptions used.
- [ ] All relevant facts and circumstances reasonably considered.
- [ ] Reasonable efforts to identify and ascertain facts made.
- [ ] No unreasonable reliance on representations / projections /
      appraisals.
- [ ] Applicable law and authorities related to the facts.
- [ ] No "audit lottery" considerations taken into account.

## Disclosure flagging
- Form 8275 (general disclosure)
- Form 8275-R (regulation-contrary position)
- Form 8886 (reportable / listed transaction — required for any
  position involving § 831(b) micro-captives, syndicated
  conservation easements, or other listed transactions)

## Negative-treatment review (v1.1)

The free-source citation discipline of this pack cannot detect
implicit overrules with the same coverage as a commercial citator
(KeyCite, Shepards, BCite, Citator 2nd). The practitioner remains
responsible for:
- [ ] Running an independent citator check on every cited case for
      high-stakes positions.
- [ ] Confirming each cited Revenue Ruling, Notice, or Procedure has
      not been modified, superseded, obsoleted, or revoked.
- [ ] Confirming each cited Treasury Regulation has not been amended
      since the retrieved_date.

## Malpractice defense scaffolding
The output must capture:
- The authorities consulted and weight assigned.
- The factual record relied on (with caveats where the practitioner
  is relying on client representation).
- Alternative interpretations considered and rejected, with rationale.
- Date of research and any staleness warning.
- For state tax questions: the per-state file's `status` and
  `last_reviewed` date.
- For positions affected by recent legislation: cross-reference to
  shared/legislation-tracking.md and the relevant Public Law
  Classification Table entry.
- The practitioner's signature line and date for the checklist.
```

### F.5 `shared/live-sources.md`

```markdown
# Canonical live sources

All URLs verified live as of 2026-04-27. CI re-verifies on every PR
and push (allow up to 5 transient flakes; retry once).

## Federal — primary
- Internal Revenue Code (USLM, House.gov):
  https://uscode.house.gov/browse/prelim@title26&edition=prelim
- eCFR Title 26 (Treasury Regulations):
  https://www.ecfr.gov/current/title-26
- Federal Register — IRS agency feed:
  https://www.federalregister.gov/agencies/internal-revenue-service
- IRS.gov core: https://www.irs.gov
- Internal Revenue Manual: https://www.irs.gov/irm
- IRS Forms & Instructions: https://www.irs.gov/forms-instructions
- IRS Written Determinations (PLRs/TAMs/CCAs):
  https://www.irs.gov/written-determinations
- Internal Revenue Bulletin index:
  https://www.irs.gov/internal-revenue-bulletin
- IRS Interactive Tax Assistant:
  https://www.irs.gov/help/ita

## Federal — extended IRS resources (v1.1)
- IRS "Understanding IRS Guidance — A Brief Primer":
  https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer
- IRS Tax Code, Regulations & Official Guidance landing:
  https://www.irs.gov/privacy-disclosure/tax-code-regulations-and-official-guidance
- IRS Tax Information for Tax Professionals (hub):
  https://www.irs.gov/tax-professionals
- Basic Tools for Tax Professionals:
  https://www.irs.gov/tax-professionals/basic-tools-for-tax-professionals
- IRS Tax Statistics:
  https://www.irs.gov/statistics
- IRS Data Book (annual statistical compilation):
  https://www.irs.gov/statistics/soi-tax-stats-irs-data-book
- IRS Electronic Reading Room (FOIA):
  https://www.irs.gov/uac/electronic-reading-room
- IRS FOIA Library:
  https://www.irs.gov/privacy-disclosure/foia-library
- U.S. Income Tax Treaties (A–Z):
  https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z
- IRBs picklist (alternate):
  https://apps.irs.gov/app/picklist/list/internalRevenueBulletins.html

## Federal — courts
- U.S. Tax Court (DAWSON): https://dawson.ustaxcourt.gov
- U.S. Tax Court main site: https://www.ustaxcourt.gov
- U.S. Tax Court Rules of Practice and Procedure:
  https://www.ustaxcourt.gov/rules.html
- DAWSON Today's Opinions (freshness feed):
  https://dawson.ustaxcourt.gov/todays-opinions
- DAWSON Today's Orders (freshness feed):
  https://dawson.ustaxcourt.gov/todays-orders
- CourtListener (free federal case law): https://www.courtlistener.com
- U.S. Supreme Court: https://www.supremecourt.gov
- PACER: https://pacer.uscourts.gov

## Federal — DOJ tax enforcement (v1.1)
- U.S. Department of Justice — Tax Division:
  https://www.justice.gov/tax

## USC research tools (v1.1)

Tools at uscode.house.gov for tracing Public Laws to USC sections:
- Classification Tables (Public Law → USC):
  https://uscode.house.gov/classification/tables.shtml
- Popular Name Tool (act name → Public Law):
  https://uscode.house.gov/popularnames/popularnames.htm
- Cite Checker (verify USC citations):
  https://uscode.house.gov/cite.xhtml
- Table III — Statutes at Large mapping:
  https://uscode.house.gov/table3/table3years.htm
- Editorial Reclassification (renumbered sections):
  https://uscode.house.gov/editorialreclassification/reclassification.html
- USLM XML Downloads (bulk):
  https://uscode.house.gov/download/download.shtml

## Legislative branch (federal) (v1.1)
- Joint Committee on Taxation: https://www.jct.gov
- House Ways & Means Committee: https://waysandmeans.house.gov
- Senate Finance Committee: https://www.finance.senate.gov
- U.S. Treasury Office of Tax Policy:
  https://home.treasury.gov/policy-issues/tax-policy
- Treasury Greenbooks (Administration Revenue Proposals):
  https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals
- Congressional Budget Office — Taxes:
  https://www.cbo.gov/topics/taxes
- CBO Cost Estimates Search:
  https://www.cbo.gov/cost-estimates

## State revenue agencies (50 + DC)

All URLs are the canonical primary entry point for each jurisdiction's
revenue agency. Where a state splits administration across multiple
agencies (e.g., California FTB for income, CDTFA for sales/use, EDD
for employment), the per-state reference file at
`skills/tax-research-state-income/references/states/<XX>.md` and
`skills/tax-research-state-salesuse/references/states/<XX>.md` lists
the additional bodies. CI re-verifies these URLs on every push; up
to 5 transient flakes tolerated across the full set.

| Code | Jurisdiction | Primary agency | URL |
|---|---|---|---|
| AL | Alabama | Department of Revenue | https://www.revenue.alabama.gov |
| AK | Alaska | Dept. of Revenue (no individual income tax) | https://tax.alaska.gov |
| AZ | Arizona | Department of Revenue | https://azdor.gov |
| AR | Arkansas | Dept. of Finance & Administration | https://www.dfa.arkansas.gov |
| CA | California | Franchise Tax Board (income) / CDTFA (sales) | https://www.ftb.ca.gov |
| CO | Colorado | Department of Revenue | https://tax.colorado.gov |
| CT | Connecticut | Department of Revenue Services | https://portal.ct.gov/drs |
| DE | Delaware | Division of Revenue | https://revenue.delaware.gov |
| DC | District of Columbia | Office of Tax and Revenue | https://otr.cfo.dc.gov |
| FL | Florida | Dept. of Revenue (no individual income tax) | https://floridarevenue.com |
| GA | Georgia | Department of Revenue | https://dor.georgia.gov |
| HI | Hawaii | Department of Taxation | https://tax.hawaii.gov |
| ID | Idaho | State Tax Commission | https://tax.idaho.gov |
| IL | Illinois | Department of Revenue | https://tax.illinois.gov |
| IN | Indiana | Department of Revenue | https://www.in.gov/dor |
| IA | Iowa | Department of Revenue | https://tax.iowa.gov |
| KS | Kansas | Department of Revenue | https://www.ksrevenue.gov |
| KY | Kentucky | Department of Revenue | https://revenue.ky.gov |
| LA | Louisiana | Department of Revenue | https://revenue.louisiana.gov |
| ME | Maine | Revenue Services | https://www.maine.gov/revenue |
| MD | Maryland | Comptroller of Maryland | https://www.marylandtaxes.gov |
| MA | Massachusetts | Department of Revenue | https://www.mass.gov/orgs/massachusetts-department-of-revenue |
| MI | Michigan | Department of Treasury | https://www.michigan.gov/treasury |
| MN | Minnesota | Department of Revenue | https://www.revenue.state.mn.us |
| MS | Mississippi | Department of Revenue | https://www.dor.ms.gov |
| MO | Missouri | Department of Revenue | https://dor.mo.gov |
| MT | Montana | Department of Revenue | https://mtrevenue.gov |
| NE | Nebraska | Department of Revenue | https://revenue.nebraska.gov |
| NV | Nevada | Dept. of Taxation (no individual income tax) | https://tax.nv.gov |
| NH | New Hampshire | DRA (I&D tax repealed 2025) | https://www.revenue.nh.gov |
| NJ | New Jersey | Division of Taxation | https://www.nj.gov/treasury/taxation |
| NM | New Mexico | Taxation and Revenue Department | https://www.tax.newmexico.gov |
| NY | New York | Department of Taxation and Finance | https://www.tax.ny.gov |
| NC | North Carolina | Department of Revenue | https://www.ncdor.gov |
| ND | North Dakota | Office of State Tax Commissioner | https://www.tax.nd.gov |
| OH | Ohio | Department of Taxation | https://tax.ohio.gov |
| OK | Oklahoma | Tax Commission | https://oklahoma.gov/tax.html |
| OR | Oregon | Department of Revenue | https://www.oregon.gov/dor |
| PA | Pennsylvania | Department of Revenue | https://www.revenue.pa.gov |
| RI | Rhode Island | Division of Taxation | https://tax.ri.gov |
| SC | South Carolina | Department of Revenue | https://dor.sc.gov |
| SD | South Dakota | Dept. of Revenue (no individual income tax) | https://dor.sd.gov |
| TN | Tennessee | Dept. of Revenue (Hall tax repealed) | https://www.tn.gov/revenue |
| TX | Texas | Comptroller (no individual income tax) | https://comptroller.texas.gov |
| UT | Utah | State Tax Commission | https://tax.utah.gov |
| VT | Vermont | Department of Taxes | https://tax.vermont.gov |
| VA | Virginia | Department of Taxation | https://www.tax.virginia.gov |
| WA | Washington | DOR (no general income tax; B&O + cap gains) | https://dor.wa.gov |
| WV | West Virginia | Tax Division | https://tax.wv.gov |
| WI | Wisconsin | Department of Revenue | https://www.revenue.wi.gov |
| WY | Wyoming | Department of Revenue (no individual income tax) | https://revenue.wyo.gov |

## Multistate / sales-tax bodies
- Multistate Tax Commission: https://www.mtc.gov
- Federation of Tax Administrators: https://www.taxadmin.org
- FTA State Tax Agencies index: https://www.taxadmin.org/state-tax-agencies
- Streamlined Sales Tax Governing Board:
  https://www.streamlinedsalestax.org

## International (extended) (v1.1)
- OECD Tax: https://www.oecd.org/tax/

## Policy data — persuasive non-authority (v1.1)

These are independent policy organizations with editorial viewpoints
but reasonably well-sourced data. Tag any cite as
`weight: persuasive_non_authority`. Never authority.

- Tax Foundation Center for State Tax Policy:
  https://taxfoundation.org/center/state-tax-policy/
- Tax Policy Center (Urban-Brookings): https://www.taxpolicycenter.org
- Library of Congress History of US Income Tax:
  https://www.loc.gov/rr/business/hottopic/irs_history.html

## Free case databases — extended (v1.1)
- Legal Bitstream (free tax case search, 1990+):
  http://www.legalbitstream.com

## Current awareness — NOT authority (v1.1)

These are practitioner-facing current-awareness sources. They are
NEVER authority. Tag `weight: not_authority`. They MUST NOT be the
closest cite for any proposition.

- TaxProf Blog: https://taxprof.typepad.com
- Procedurally Taxing: https://procedurallytaxing.com
- Tax Appellate Blog (Miller & Chevalier): https://appellatetax.com

## Professional standards
- AICPA SSTS:
  https://www.aicpa-cima.com/resources/landing/statements-on-standards-for-tax-services
- AICPA Levels of Confidence chart:
  https://www.aicpa-cima.com/resources/download/levels-of-confidence-for-tax-return-positions-chart
- Circular 230 (eCFR):
  https://www.ecfr.gov/current/title-31/subtitle-A/part-10
- Circular 230 IRS hub:
  https://www.irs.gov/tax-professionals/circular-230-tax-professionals
- Circular 230 PDF (Rev. 6-2014):
  https://www.irs.gov/pub/irs-pdf/pcir230.pdf

## Mirrors (use only if primary unreachable)
- Cornell LII (IRC + CFR mirror): https://www.law.cornell.edu
- Cornell LII Title 26 (with 1939→1986 conversion tables):
  https://www.law.cornell.edu/uscode/text/26
- GovInfo (Federal Register / USC archives): https://www.govinfo.gov
```

### F.6 `shared/sources.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "version": "1.1.0",
  "updated": "2026-04-27",
  "federal_primary": {
    "irc_uslm":      "https://uscode.house.gov/browse/prelim@title26&edition=prelim",
    "ecfr_title26":  "https://www.ecfr.gov/current/title-26",
    "federal_register_irs": "https://www.federalregister.gov/agencies/internal-revenue-service",
    "irs_home":      "https://www.irs.gov",
    "irm":           "https://www.irs.gov/irm",
    "forms_pubs":    "https://www.irs.gov/forms-instructions",
    "written_determinations": "https://www.irs.gov/written-determinations",
    "irb_index":     "https://www.irs.gov/internal-revenue-bulletin",
    "ita":           "https://www.irs.gov/help/ita"
  },
  "irs_extended": {
    "guidance_primer":      "https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer",
    "tax_code_reg_guidance":"https://www.irs.gov/privacy-disclosure/tax-code-regulations-and-official-guidance",
    "tax_pros_hub":         "https://www.irs.gov/tax-professionals",
    "basic_tools_pros":     "https://www.irs.gov/tax-professionals/basic-tools-for-tax-professionals",
    "tax_statistics":       "https://www.irs.gov/statistics",
    "irs_data_book":        "https://www.irs.gov/statistics/soi-tax-stats-irs-data-book",
    "electronic_reading":   "https://www.irs.gov/uac/electronic-reading-room",
    "foia_library":         "https://www.irs.gov/privacy-disclosure/foia-library",
    "treaties_a_to_z":      "https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z",
    "irbs_picklist":        "https://apps.irs.gov/app/picklist/list/internalRevenueBulletins.html"
  },
  "federal_courts": {
    "tax_court_dawson": "https://dawson.ustaxcourt.gov",
    "tax_court_main":   "https://www.ustaxcourt.gov",
    "courtlistener":    "https://www.courtlistener.com",
    "scotus":           "https://www.supremecourt.gov",
    "pacer":            "https://pacer.uscourts.gov"
  },
  "tax_court_extended": {
    "rules":               "https://www.ustaxcourt.gov/rules.html",
    "todays_opinions":     "https://dawson.ustaxcourt.gov/todays-opinions",
    "todays_orders":       "https://dawson.ustaxcourt.gov/todays-orders"
  },
  "doj_tax_division": "https://www.justice.gov/tax",
  "uscode_tools": {
    "classification_tables":     "https://uscode.house.gov/classification/tables.shtml",
    "popular_name_tool":         "https://uscode.house.gov/popularnames/popularnames.htm",
    "cite_checker":              "https://uscode.house.gov/cite.xhtml",
    "table_iii_statutes":        "https://uscode.house.gov/table3/table3years.htm",
    "editorial_reclassification":"https://uscode.house.gov/editorialreclassification/reclassification.html",
    "uslm_downloads":            "https://uscode.house.gov/download/download.shtml"
  },
  "legislative_branch": {
    "jct":                   "https://www.jct.gov",
    "house_ways_means":      "https://waysandmeans.house.gov",
    "senate_finance":        "https://www.finance.senate.gov",
    "treasury_tax_policy":   "https://home.treasury.gov/policy-issues/tax-policy",
    "treasury_greenbooks":   "https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals",
    "cbo_taxes":             "https://www.cbo.gov/topics/taxes",
    "cbo_cost_estimates":    "https://www.cbo.gov/cost-estimates"
  },
  "state_dors": {
    "AL": "https://www.revenue.alabama.gov",
    "AK": "https://tax.alaska.gov",
    "AZ": "https://azdor.gov",
    "AR": "https://www.dfa.arkansas.gov",
    "CA": "https://www.ftb.ca.gov",
    "CO": "https://tax.colorado.gov",
    "CT": "https://portal.ct.gov/drs",
    "DE": "https://revenue.delaware.gov",
    "DC": "https://otr.cfo.dc.gov",
    "FL": "https://floridarevenue.com",
    "GA": "https://dor.georgia.gov",
    "HI": "https://tax.hawaii.gov",
    "ID": "https://tax.idaho.gov",
    "IL": "https://tax.illinois.gov",
    "IN": "https://www.in.gov/dor",
    "IA": "https://tax.iowa.gov",
    "KS": "https://www.ksrevenue.gov",
    "KY": "https://revenue.ky.gov",
    "LA": "https://revenue.louisiana.gov",
    "ME": "https://www.maine.gov/revenue",
    "MD": "https://www.marylandtaxes.gov",
    "MA": "https://www.mass.gov/orgs/massachusetts-department-of-revenue",
    "MI": "https://www.michigan.gov/treasury",
    "MN": "https://www.revenue.state.mn.us",
    "MS": "https://www.dor.ms.gov",
    "MO": "https://dor.mo.gov",
    "MT": "https://mtrevenue.gov",
    "NE": "https://revenue.nebraska.gov",
    "NV": "https://tax.nv.gov",
    "NH": "https://www.revenue.nh.gov",
    "NJ": "https://www.nj.gov/treasury/taxation",
    "NM": "https://www.tax.newmexico.gov",
    "NY": "https://www.tax.ny.gov",
    "NC": "https://www.ncdor.gov",
    "ND": "https://www.tax.nd.gov",
    "OH": "https://tax.ohio.gov",
    "OK": "https://oklahoma.gov/tax.html",
    "OR": "https://www.oregon.gov/dor",
    "PA": "https://www.revenue.pa.gov",
    "RI": "https://tax.ri.gov",
    "SC": "https://dor.sc.gov",
    "SD": "https://dor.sd.gov",
    "TN": "https://www.tn.gov/revenue",
    "TX": "https://comptroller.texas.gov",
    "UT": "https://tax.utah.gov",
    "VT": "https://tax.vermont.gov",
    "VA": "https://www.tax.virginia.gov",
    "WA": "https://dor.wa.gov",
    "WV": "https://tax.wv.gov",
    "WI": "https://www.revenue.wi.gov",
    "WY": "https://revenue.wyo.gov"
  },
  "no_individual_income_tax": ["AK", "FL", "NV", "SD", "TN", "TX", "WA", "WY"],
  "no_state_sales_tax":       ["AK", "DE", "MT", "NH", "OR"],
  "multistate": {
    "mtc":                "https://www.mtc.gov",
    "fta":                "https://www.taxadmin.org",
    "fta_state_agencies": "https://www.taxadmin.org/state-tax-agencies",
    "sstgb":              "https://www.streamlinedsalestax.org"
  },
  "international_extended": {
    "oecd_tax":             "https://www.oecd.org/tax/"
  },
  "policy_data": {
    "tax_foundation_state": "https://taxfoundation.org/center/state-tax-policy/",
    "tax_policy_center":    "https://www.taxpolicycenter.org",
    "loc_irs_history":      "https://www.loc.gov/rr/business/hottopic/irs_history.html"
  },
  "free_case_databases_extended": {
    "legal_bitstream":      "http://www.legalbitstream.com"
  },
  "current_awareness_non_authority": {
    "tax_prof_blog":        "https://taxprof.typepad.com",
    "procedurally_taxing":  "https://procedurallytaxing.com",
    "tax_appellate_blog":   "https://appellatetax.com"
  },
  "professional_standards": {
    "aicpa_ssts":            "https://www.aicpa-cima.com/resources/landing/statements-on-standards-for-tax-services",
    "aicpa_confidence_chart":"https://www.aicpa-cima.com/resources/download/levels-of-confidence-for-tax-return-positions-chart",
    "circular_230_ecfr":     "https://www.ecfr.gov/current/title-31/subtitle-A/part-10",
    "circular_230_irs":      "https://www.irs.gov/tax-professionals/circular-230-tax-professionals",
    "circular_230_pdf":      "https://www.irs.gov/pub/irs-pdf/pcir230.pdf"
  },
  "mirrors": {
    "cornell_lii":          "https://www.law.cornell.edu",
    "cornell_lii_title_26": "https://www.law.cornell.edu/uscode/text/26",
    "govinfo":              "https://www.govinfo.gov"
  }
}
```

### F.7 `shared/output-schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/KisaesDevLab/vibe-cpa-skills/shared/output-schema.json",
  "title": "Vibe CPA Skill Output Sidecar",
  "type": "object",
  "required": ["skill", "version", "generated_at", "task", "conclusion",
               "confidence_band", "authorities", "verification_checklist"],
  "properties": {
    "skill": { "type": "string" },
    "version": { "type": "string", "pattern": "^\\d+\\.\\d+\\.\\d+" },
    "generated_at": { "type": "string", "format": "date-time" },
    "task": {
      "type": "object",
      "required": ["intake", "issue"],
      "properties": {
        "intake": { "type": "object" },
        "issue": { "type": "string" },
        "taxpayer_circuit": { "type": "string" },
        "taxpayer_state": { "type": "string", "pattern": "^[A-Z]{2}$" },
        "tax_year": { "type": "integer" }
      }
    },
    "analysis": { "type": "string" },
    "conclusion": { "type": "string" },
    "confidence_band": {
      "type": "string",
      "enum": ["HIGH", "MODERATE", "LOW", "SPECULATIVE"]
    },
    "band_rationale": { "type": "string" },
    "disclosure_recommended": { "type": "boolean" },
    "penalty_exposure": { "type": "string" },
    "authorities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["authority_type", "citation", "url",
                     "retrieved_date", "quoted_text", "weight"],
        "properties": {
          "authority_type": {
            "type": "string",
            "enum": [
              "IRC", "TreasReg", "TreasuryDecision", "StatutesAtLarge",
              "RevRul", "RevProc", "Notice", "Announcement",
              "PLR", "TAM", "CCA", "GCM", "AOD", "FSA",
              "OfficeMemo", "InfoLetter",
              "IRSPub", "IRM", "ATG", "ISPPaper", "IRSNewsRelease",
              "JCT_BlueBook", "LegHistory", "Greenbook", "CBOReport",
              "SCOTUS", "CtAppeals", "TaxCt", "DistCt", "CtFedClaims",
              "StateStatute", "StateReg", "StateAdmin", "StateCt",
              "Treaty", "Form", "Instructions"
            ]
          },
          "citation": { "type": "string" },
          "url": { "type": "string", "format": "uri" },
          "retrieved_date": { "type": "string", "format": "date" },
          "quoted_text": { "type": "string", "maxLength": 600 },
          "pin_cite": { "type": "string" },
          "weight": {
            "type": "string",
            "enum": ["primary_statute", "binding_judicial", "regulation",
                     "binding_circuit", "judicial", "irs_published",
                     "legislative_history", "written_determinations",
                     "persuasive_non_authority", "not_authority"]
          },
          "weight_override_rationale": { "type": "string" },
          "chevron_replaced": { "type": "boolean" }
        }
      }
    },
    "public_laws_consulted": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["public_law", "popular_name"],
        "properties": {
          "public_law": { "type": "string" },
          "popular_name": { "type": "string" },
          "classification_tables_url": { "type": "string", "format": "uri" },
          "affected_irc_sections": {
            "type": "array",
            "items": { "type": "string" }
          }
        }
      }
    },
    "state_files_consulted": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["state_code", "skill", "status"],
        "properties": {
          "state_code": { "type": "string", "pattern": "^[A-Z]{2}$" },
          "skill": { "type": "string" },
          "status": { "type": "string", "enum": ["stub", "draft", "reviewed", "verified"] },
          "last_reviewed": { "type": "string", "format": "date" }
        }
      }
    },
    "unresolved_citations": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["proposition", "search", "date"],
        "properties": {
          "proposition": { "type": "string" },
          "search": { "type": "string" },
          "date": { "type": "string", "format": "date" }
        }
      }
    },
    "staleness_warnings": { "type": "array", "items": { "type": "string" } },
    "negative_treatment_review_required": {
      "type": "boolean",
      "description": "True for high-stakes positions; flags the residual practitioner responsibility for citator check (free-source pack cannot detect implicit overrules)"
    },
    "verification_checklist": {
      "type": "object",
      "required": ["ssts_1_1", "ssts_2_3", "circ230_10_22",
                   "circ230_10_35", "circ230_10_37"],
      "additionalProperties": { "type": "boolean" }
    },
    "disclosure_forms": {
      "type": "array",
      "items": { "enum": ["8275", "8275-R", "8886", "none"] }
    }
  }
}
```

### F.8 `shared/legislation-tracking.md` — NEW in v1.1

```markdown
# Legislation tracking

Workflow for tracing recent Public Laws to the USC sections they
amended, and for identifying authoritative legislative-history
artifacts. Used by `irc-section-lookup`, `tax-research-federal`, and
`planning-multi-year`.

## When to invoke this workflow

- User mentions a Public Law by its popular name: "TCJA", "Inflation
  Reduction Act", "OBBBA", "SECURE 2.0", "American Rescue Plan",
  "CARES Act", "Tax Cuts and Jobs Act", etc.
- User mentions a Public Law by number: "Pub. L. 117-169",
  "P.L. 119-XX", "Public Law 115-97", etc.
- User asks "what changed in [§ X] under [recent legislation]".
- User asks for "current law" on a topic where recent legislation
  may have amended the underlying statute.
- A planning skill is scoring a strategy whose eligibility depends on
  a sunset, phase-out, or amendment effective in a tax year > 2024.

## Workflow

### 1. Resolve the Public Law

If user gave a popular name:
1. Fetch the **Popular Name Tool** at
   `https://uscode.house.gov/popularnames/popularnames.htm`.
2. Locate the act by name; record its Public Law number and Statutes
   at Large citation.

If user gave a Public Law number, skip to step 2.

### 2. Retrieve the Classification Table

1. Fetch the **Classification Tables** index at
   `https://uscode.house.gov/classification/tables.shtml`.
2. Navigate to the table for the Public Law's congressional session.
3. Identify every USC section the Public Law amended, added, or
   repealed.
4. Record the table URL in the JSON sidecar's
   `public_laws_consulted[].classification_tables_url` field.
5. Record affected sections in
   `public_laws_consulted[].affected_irc_sections`.

### 3. Verify each affected section's current text

For each affected USC section:
1. Fetch the current section from
   `https://uscode.house.gov/browse/prelim@title26` (USLM canonical).
2. Confirm the text is post-amendment.
3. Cite as `IRC` with `weight: primary_statute` and pin to the
   specific subsection/paragraph.

### 4. Locate authoritative legislative-history artifacts

In order of authoritativeness:

1. **JCT Bluebook** for the relevant Congress at
   `https://www.jct.gov/publications/`. Bluebooks are typically
   published 6–12 months after enactment. Cite as `JCT_BlueBook`
   with `weight: legislative_history`.

2. **Committee reports** (House Ways & Means, Senate Finance,
   Conference). Find via:
   - `https://waysandmeans.house.gov/`
   - `https://www.finance.senate.gov/`
   - Or via congress.gov for the bill's report numbers.
   Cite as `LegHistory` with `weight: legislative_history`.

3. **Treasury Greenbook** (Administration's Fiscal Year Revenue
   Proposals) at
   `https://home.treasury.gov/policy-issues/tax-policy/revenue-proposals`.
   - **Caveat**: Greenbooks describe what the Administration *proposed*.
     Tag as `Greenbook`/`legislative_history` ONLY if the proposal
     became enacted law in substantively the same form. Otherwise tag
     `Greenbook`/`persuasive_non_authority` for descriptive use only.

4. **CBO scoring report** at `https://www.cbo.gov/topics/taxes` or
   `https://www.cbo.gov/cost-estimates`.
   - **Caveat**: CBO scores describe projected revenue effects. They
     are not interpretive authority on the meaning of the enacted
     statute. Tag as `CBOReport`/`legislative_history` only when the
     score accompanied the enacted bill. Tag
     `CBOReport`/`persuasive_non_authority` for descriptive use of
     pre-enactment scores.

### 5. Check for proposed regulations and Treasury Decisions

After legislation enacts, Treasury typically issues proposed
regulations, then final regulations. Check:

1. **Federal Register IRS feed** at
   `https://www.federalregister.gov/agencies/internal-revenue-service`
   for proposed and final rules implementing the Public Law.
2. **Treasury Decisions** are the issuance vehicle in the Federal
   Register; the codified rule appears in eCFR. Tag the issuance as
   `TreasuryDecision`/`regulation` and the codified rule as
   `TreasReg`/`regulation`.

### 6. Cite Checker (optional sanity check)

For any USC citation that may have been renumbered or reclassified,
use the **Cite Checker** at `https://uscode.house.gov/cite.xhtml` to
verify the citation resolves to current section text.

## Output requirements

When this workflow is exercised, the JSON sidecar MUST populate:
- `public_laws_consulted[]` with at least `public_law` and
  `popular_name` for each Public Law referenced.
- `classification_tables_url` for each Public Law (the URL of the
  specific table consulted).
- `affected_irc_sections[]` listing every USC § the Public Law
  amended that is material to the analysis.

## Common Public Laws — quick reference

| Popular name | Public Law | Year | Notable IRC topics |
|---|---|---|---|
| Tax Cuts and Jobs Act (TCJA) | Pub. L. 115-97 | 2017 | §199A QBI; §163(j) interest limit; §168 bonus depreciation; §1400Z OZ |
| CARES Act | Pub. L. 116-136 | 2020 | NOL changes; §163(j) relaxation; §172 carryback restoration |
| Consolidated Appropriations Act 2021 | Pub. L. 116-260 | 2020 | PPP deductibility; ERC extension |
| American Rescue Plan Act | Pub. L. 117-2 | 2021 | §6428B Recovery Rebate; CTC expansion (1 year) |
| Inflation Reduction Act (IRA) | Pub. L. 117-169 | 2022 | §55 corporate AMT; §4501 stock buyback; §45 PTC; §48 ITC; §30D EV |
| SECURE 2.0 | (in Pub. L. 117-328 div. T) | 2022 | §401(a)(9) RMD age; §408A Roth catch-up |
| One Big Beautiful Bill Act (OBBBA) | (Pub. L. 119-XX) | 2025 | TCJA permanence; many extenders; §174 R&E; §163(j) modifications |

The Public Law number for OBBBA should be verified against the
Popular Name Tool at retrieval time — this table is a quick
reference, not authority.

## Related skills

- **`irc-section-lookup`**: implements steps 1–3 and 6 as the user-
  facing primary path.
- **`tax-research-federal`**: implements steps 4–5 as part of
  legislative-history workflow.
- **`planning-multi-year`**: consults this file when scoring
  strategies whose eligibility depends on sunset/effective-date
  provisions.
- **`compliance-ssts-circular230`**: references the IRS Guidance
  Primer at
  `https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer`
  for malpractice-defense scaffolding.
```

### F.9 `shared/state-template.md`

```markdown
---
state_code: <XX>
state_name: <Full name>
status: stub                    # stub → draft → reviewed → verified
last_reviewed: 1970-01-01
last_reviewed_by: <handle>
applies_to:                     # which research skills consume this file
  - tax-research-state-income
  - tax-research-state-salesuse
---

# <Full state name> (<XX>)

> **Status: STUB.** This file contains the canonical agency entry point
> and a structural skeleton. Substantive content has not been verified
> by a practitioner. Treat as a starting pointer for live retrieval, not
> as authority. Promote to `draft` after first practitioner edit;
> `reviewed` after a second-pair review; `verified` after live
> citation-walk against current statute and regulation.

## Administrative bodies

- **Primary agency:** <name> — <URL from shared/sources.json>
- **Income tax administration:** <agency, URL>           <!-- TODO: confirm -->
- **Sales/use tax administration:** <agency, URL>        <!-- TODO: confirm -->
- **Employment tax administration:** <agency, URL>       <!-- TODO: confirm -->
- **Property/local tax administration:** <agency, URL>   <!-- TODO: confirm -->
- **Tax appeals body:** <agency, URL>                    <!-- TODO: confirm -->

## Statute and regulation citation pattern

- **Statute citation form:** <e.g., "Cal. Rev. & Tax. Code § 17041">  <!-- TODO -->
- **Regulation citation form:** <e.g., "Cal. Code Regs. tit. 18, § 17041"> <!-- TODO -->
- **Legislative website:** <URL>                                 <!-- TODO -->
- **Regulation hub:** <URL>                                      <!-- TODO -->

## Income tax overview

- **Has individual income tax?** <yes|no|limited>                <!-- TODO -->
- **Filing status / rate structure:** <flat | graduated | brackets>  <!-- TODO -->
- **Conformity to federal IRC:** <rolling | static | selective>  <!-- TODO -->
- **Conformity date (if static):** <YYYY-MM-DD>                  <!-- TODO -->
- **Standard deduction:** <amount or "follows federal">          <!-- TODO -->
- **Itemized deduction conformity:** <notes>                     <!-- TODO -->
- **Notable departures from federal:** <list>                    <!-- TODO -->
- **Resident definition / domicile rule citation:**              <!-- TODO -->
- **Convenience-of-employer rule applicable?** <yes|no>          <!-- TODO -->

## Sales and use tax overview

- **Has state sales tax?** <yes|no>                              <!-- TODO -->
- **State rate:** <%>                                            <!-- TODO -->
- **Local rates allowed?** <yes|no, range>                       <!-- TODO -->
- **Streamlined Sales Tax member?** <full | associate | no>      <!-- TODO -->
- **Wayfair economic nexus thresholds:** <$ + transaction count> <!-- TODO -->
- **Marketplace facilitator law citation:**                       <!-- TODO -->
- **Notable taxability quirks:** <SaaS, digital goods, services> <!-- TODO -->
- **Sourcing rule (origin / destination / mixed):**              <!-- TODO -->
- **Local jurisdiction count and complexity notes:**             <!-- TODO -->

## Pass-through entity tax (PTET) / SALT cap workaround

- **PTET available?** <yes|no>                                   <!-- TODO -->
- **Election entity types:** <PTE types eligible>                <!-- TODO -->
- **Election deadline / mechanics:**                              <!-- TODO -->
- **Statute citation:**                                          <!-- TODO -->
- **Practitioner notes:** <annual? irrevocable? credit at owner level?> <!-- TODO -->

## Letter ruling / advisory opinion repository

- **Repository URL:** <URL>                                      <!-- TODO -->
- **Citation form for rulings:** <e.g., "TSB-A-22(5)I (NY)">     <!-- TODO -->
- **Search interface notes:**                                    <!-- TODO -->

## Tax court / administrative appeals

- **Appeals tribunal name:** <agency>                            <!-- TODO -->
- **Decisions repository URL:**                                  <!-- TODO -->
- **Statute of limitations on assessment:** <years>              <!-- TODO -->
- **Statute of limitations on refund claim:** <years>            <!-- TODO -->

## Practitioner notes

- <Free-form bullets: special elections, unusual rules, traps,
  e.g., CA AB5, NY convenience rule, MA millionaire surtax, WA
  capital gains tax, OR statewide transit tax.>                  <!-- TODO -->

## Recent developments (last 24 months)

<!-- TODO: bullet major legislative or regulatory changes -->

## Secondary policy data (optional, NON-AUTHORITY) — v1.1

When promoting this stub to `draft` or higher, the practitioner may
consult independent policy data sources for context on conformity,
rates, and recent legislative tracking. These sources are
`persuasive_non_authority` at most and MUST NOT serve as the closest
cite for any conclusion:

- **Tax Foundation Center for State Tax Policy** —
  https://taxfoundation.org/center/state-tax-policy/
  (state conformity tables, rate tables, PTET tracker; pro-low-tax
  editorial viewpoint)
- **Tax Policy Center (Urban-Brookings)** —
  https://www.taxpolicycenter.org
  (state tax fact-sheets; centrist/progressive editorial viewpoint)

When citing either, tag as `weight: persuasive_non_authority` and
record the citation in the practitioner notes section, NOT in the
authoritative analysis.

## Sources consulted

<!-- TODO: list URL + retrieved_date for any source consulted while
     populating this file. Required before promoting status above stub. -->
```

---

## G. Skill template

Path: `docs/skill-template.md` (Claude Code copies this and fills it in for the 25 non-flagship skills).

````markdown
# `<skill-name>` — SKILL.md template

```yaml
---
name: <kebab-case-name>            # ≤ 64 chars, no "anthropic"/"claude"
description: |
  <Third-person, declarative one-paragraph description, ≤ 1024 chars.
  Front-load the use case. State concrete trigger phrases users say.
  Include "Use when ..." and at least three example user phrasings.
  No first/second person; no XML angle brackets; no audit-lottery
  language. Make sure to use this skill whenever the user mentions
  <trigger keyword 1>, <trigger keyword 2>, <trigger keyword 3>.>
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---
```

## Read before output
Before producing any output, read these files in order:
1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` (when this skill touches recent
   Public Laws or current law affected by post-2024 legislation)
6. `references/<topic>.md` for this skill (one level deep)
7. (If this is a state research skill) the relevant
   `references/states/<XX>.md` based on the user's jurisdiction.

## Workflow

### 1. Intake
Collect the minimum facts needed to answer. Use the intake schema
below. If a fact is missing and material, request it; if non-material,
proceed with a labeled assumption. For state research skills, capture
the taxpayer's state explicitly (`taxpayer_state` in the sidecar).

### 2. Analysis
Map facts to authorities using the hierarchy. For each contested
proposition, list authorities supporting and contrary, with weight.

### 3. Conclusion
State the conclusion. Assign `confidence_band` per
`shared/confidence-bands.md`. Note disclosure recommendation.

### 4. Authorities
Cite primary sources only. Every entry includes
`authority_type, citation, url, retrieved_date, quoted_text, weight`.
Use the `[CITATION NEEDED — search: <query>]` sentinel rather than
fabricating.

### 5. JSON sidecar
Emit a JSON object validating against `shared/output-schema.json`
following the markdown response. State research skills additionally
populate `state_files_consulted`. Skills that consult Public Laws
populate `public_laws_consulted`.

## Hard rules
- Never fabricate citations.
- Never claim Chevron deference for Treasury Regs (post-Loper Bright).
- Never recommend a position with a SPECULATIVE band.
- Always include the verification checklist.
- For state work: cap confidence at LOW when relying solely on a
  `status: stub` state file.
- Tax Foundation, Tax Policy Center, blogs, and other current-
  awareness sources never drive a band assignment.
- Free-source citation discipline cannot detect implicit overrules
  with comprehensive coverage. Note this in the verification
  checklist for high-stakes positions.
- Keep this SKILL.md ≤ 500 lines; push longer content to references/.

## Verification checklist (appendix)
The practitioner using this output must complete the checklist in
`shared/compliance.md` before relying on the result, including the
negative-treatment-review residual responsibility for high-stakes
positions.
````

---

## H. Custom slash commands

Path: `.claude/commands/<n>.md`. All seven below are designed for this build.

### H.1 `.claude/commands/create-skill.md`

```markdown
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
```

### H.2 `.claude/commands/add-eval.md`

```markdown
---
description: Add an eval case to a skill's eval JSON
argument-hint: [skill-name] [case-name]
allowed-tools: Read Edit Write Bash(jq:*) Glob
---
Append an eval case named "$2" to `evals/<family>/$1.json`. If the
file does not exist, create it with the schema:
{ "skill_name": "$1", "evals": [ ... ] }
Each eval must have: id, prompt, expected_output, expectations[].
Keep prompts realistic — actual phrasings a CPA would use.
Validate JSON parses: `jq . evals/<family>/$1.json`.
```

### H.3 `.claude/commands/verify-citations.md`

```markdown
---
description: Verify citations in a SKILL.md or reference file
argument-hint: [path]
allowed-tools: Read Grep Bash(jq:*) WebFetch
---
For file $1:
1. Extract every citation (IRC §, Treas. Reg., case cite, Rev. Rul.,
   PLR, Form, IRM, etc.).
2. For each, confirm the canonical URL in `shared/sources.json`
   resolves and that the cited text is present.
3. Flag any `[CITATION NEEDED — search: ...]` sentinels — these
   block phase tick-off unless intentional in template files.
4. State stub files at references/states/ use `TODO:` markers; do not
   flag those.
5. For each authority_type used in the file, confirm it appears in
   the enumeration in shared/citation-discipline.md (and in the
   authority_type enum in shared/output-schema.json).
6. Report a summary: ok, suspect, sentinel, unverifiable, taxonomy_drift.
```

### H.4 `.claude/commands/check-compliance.md`

```markdown
---
description: Verify every skill output template includes the SSTS / Circular 230 checklist
allowed-tools: Read Grep Glob
---
For every `skills/*/SKILL.md`, confirm the body includes:
- A reference to `shared/compliance.md`
- The five SSTS / Circular 230 checklist items (1.1, 2.3, 10.22,
  10.35, 10.37)
- The "Read before output" block linking the four core shared/ files
  (citation-discipline, authority-hierarchy, confidence-bands,
  compliance)
- For skills that touch recent Public Laws: a reference to
  shared/legislation-tracking.md
- The JSON sidecar emission step
- The negative-treatment-review residual-responsibility note for
  high-stakes positions
Report any skill that is missing items, with file path and line.
```

### H.5 `.claude/commands/commit-phase.md`

```markdown
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
6. `git push origin build`
7. Print last commit SHA.
```

### H.6 `.claude/commands/checkpoint.md`

```markdown
---
description: Pre-compaction checkpoint — persist progress, commit, push
allowed-tools: Bash(git:*) Edit Read
---
1. Append a session-log entry at the bottom of BUILD_PLAN.md:
   `YYYY-MM-DDTHH:MM | phase X | items: ... | last commit: <sha>`
2. `git add -A && git commit -m "chore: checkpoint" || true`
3. `git push origin build`
4. Suggest `/compact` if context is over 70% full.
```

### H.7 `.claude/commands/open-phase-pr.md`

```markdown
---
description: Open a phase PR build → main with full body
argument-hint: [phase-number]
allowed-tools: Bash(gh:*) Read
---
Open a PR from `build` to `main` titled `Phase $1`. Body must include:
- Checklist of items completed in BUILD_PLAN.md Phase $1
- Eval pass-rate summary (paste from scripts/run-evals.sh output)
- Validation output from scripts/validate.sh
- "Awaiting Kurt's review" footer
Do NOT merge. Stop after `gh pr create`.
```

---

## I. `.claude/settings.local.json`

Path: `.claude/settings.local.json` (gitignored — Bash(*) wildcard lives here, NOT in the committed `settings.json`).

```json
{
  "$schema": "https://json-schema.org/claude-code-settings.json",
  "permissions": {
    "defaultMode": "acceptEdits",
    "disableBypassPermissionsMode": "disable",
    "allow": [
      "Bash(*)",
      "Read",
      "Edit",
      "Write",
      "Grep",
      "Glob",
      "WebSearch",
      "WebFetch(domain:docs.claude.com)",
      "WebFetch(domain:code.claude.com)",
      "WebFetch(domain:platform.claude.com)",
      "WebFetch(domain:github.com)",
      "WebFetch(domain:raw.githubusercontent.com)",

      "WebFetch(domain:www.ecfr.gov)",
      "WebFetch(domain:www.irs.gov)",
      "WebFetch(domain:apps.irs.gov)",
      "WebFetch(domain:uscode.house.gov)",
      "WebFetch(domain:www.federalregister.gov)",
      "WebFetch(domain:www.law.cornell.edu)",
      "WebFetch(domain:www.govinfo.gov)",

      "WebFetch(domain:dawson.ustaxcourt.gov)",
      "WebFetch(domain:www.ustaxcourt.gov)",
      "WebFetch(domain:www.courtlistener.com)",
      "WebFetch(domain:www.supremecourt.gov)",

      "WebFetch(domain:www.justice.gov)",
      "WebFetch(domain:www.jct.gov)",
      "WebFetch(domain:waysandmeans.house.gov)",
      "WebFetch(domain:www.finance.senate.gov)",
      "WebFetch(domain:home.treasury.gov)",
      "WebFetch(domain:www.cbo.gov)",
      "WebFetch(domain:www.loc.gov)",

      "WebFetch(domain:taxfoundation.org)",
      "WebFetch(domain:www.taxpolicycenter.org)",
      "WebFetch(domain:www.legalbitstream.com)",
      "WebFetch(domain:taxprof.typepad.com)",
      "WebFetch(domain:procedurallytaxing.com)",
      "WebFetch(domain:appellatetax.com)",
      "WebFetch(domain:www.oecd.org)",

      "WebFetch(domain:www.aicpa-cima.com)",

      "WebFetch(domain:www.revenue.alabama.gov)",
      "WebFetch(domain:tax.alaska.gov)",
      "WebFetch(domain:azdor.gov)",
      "WebFetch(domain:www.dfa.arkansas.gov)",
      "WebFetch(domain:www.ftb.ca.gov)",
      "WebFetch(domain:www.cdtfa.ca.gov)",
      "WebFetch(domain:edd.ca.gov)",
      "WebFetch(domain:tax.colorado.gov)",
      "WebFetch(domain:portal.ct.gov)",
      "WebFetch(domain:revenue.delaware.gov)",
      "WebFetch(domain:otr.cfo.dc.gov)",
      "WebFetch(domain:floridarevenue.com)",
      "WebFetch(domain:dor.georgia.gov)",
      "WebFetch(domain:tax.hawaii.gov)",
      "WebFetch(domain:tax.idaho.gov)",
      "WebFetch(domain:tax.illinois.gov)",
      "WebFetch(domain:www.in.gov)",
      "WebFetch(domain:tax.iowa.gov)",
      "WebFetch(domain:www.ksrevenue.gov)",
      "WebFetch(domain:revenue.ky.gov)",
      "WebFetch(domain:revenue.louisiana.gov)",
      "WebFetch(domain:www.maine.gov)",
      "WebFetch(domain:www.marylandtaxes.gov)",
      "WebFetch(domain:www.mass.gov)",
      "WebFetch(domain:www.michigan.gov)",
      "WebFetch(domain:www.revenue.state.mn.us)",
      "WebFetch(domain:www.dor.ms.gov)",
      "WebFetch(domain:dor.mo.gov)",
      "WebFetch(domain:mtrevenue.gov)",
      "WebFetch(domain:revenue.nebraska.gov)",
      "WebFetch(domain:tax.nv.gov)",
      "WebFetch(domain:www.revenue.nh.gov)",
      "WebFetch(domain:www.nj.gov)",
      "WebFetch(domain:www.tax.newmexico.gov)",
      "WebFetch(domain:www.tax.ny.gov)",
      "WebFetch(domain:www.ncdor.gov)",
      "WebFetch(domain:www.tax.nd.gov)",
      "WebFetch(domain:tax.ohio.gov)",
      "WebFetch(domain:oklahoma.gov)",
      "WebFetch(domain:www.oregon.gov)",
      "WebFetch(domain:www.revenue.pa.gov)",
      "WebFetch(domain:tax.ri.gov)",
      "WebFetch(domain:dor.sc.gov)",
      "WebFetch(domain:dor.sd.gov)",
      "WebFetch(domain:www.tn.gov)",
      "WebFetch(domain:comptroller.texas.gov)",
      "WebFetch(domain:tax.utah.gov)",
      "WebFetch(domain:tax.vermont.gov)",
      "WebFetch(domain:www.tax.virginia.gov)",
      "WebFetch(domain:dor.wa.gov)",
      "WebFetch(domain:tax.wv.gov)",
      "WebFetch(domain:www.revenue.wi.gov)",
      "WebFetch(domain:revenue.wyo.gov)",

      "WebFetch(domain:www.mtc.gov)",
      "WebFetch(domain:www.taxadmin.org)",
      "WebFetch(domain:www.streamlinedsalestax.org)",

      "mcp__github",
      "mcp__github__*"
    ],
    "ask": [
      "Bash(git push --force *)",
      "Bash(gh release create *)",
      "Bash(gh pr merge *)"
    ],
    "deny": [
      "Read(**/.env)",
      "Read(**/.env.*)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/**)",
      "Read(~/.config/gh/**)",
      "Edit(**/.env)",
      "Edit(.git/**)",
      "Bash(rm -rf /*)",
      "Bash(rm -rf ~)",
      "Bash(rm -rf ~/*)",
      "Bash(sudo:*)",
      "Bash(su:*)",
      "Bash(curl * | bash)",
      "Bash(curl * | sh)",
      "Bash(wget * | bash)",
      "Bash(wget * | sh)",
      "Bash(ssh:*)",
      "Bash(scp:*)",
      "Bash(git push --force origin main)",
      "Bash(git push -f origin main)",
      "Bash(git push origin main *)",
      "Bash(git push origin :main)",
      "Bash(git reset --hard origin/main)",
      "Bash(gh repo delete *)",
      "Bash(gh secret set *)",
      "Bash(gh secret delete *)",
      "Bash(gh auth logout *)",
      "Bash(npm publish *)",
      "Bash(brew install *)"
    ]
  },
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": ["github"],
  "env": {
    "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "75"
  },
  "showTurnDuration": true,
  "autoUpdates": true
}
```

A safety note: read-deny rules apply only to Claude's built-in `Read` tool. They do NOT block `cat .env` in Bash. The `Bash(*)` wildcard combined with the deny list above is the practical compromise. For stricter isolation, run Claude Code inside a container; that is overkill for this build.

`.mcp.json` (committed, optional — only needed if Kurt wants the GitHub MCP server in addition to `gh` CLI):

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}" }
    }
  }
}
```

---

## J. QUESTIONS.md template

Path: `QUESTIONS.md` (committed)

```markdown
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
```

---

## K. CI workflow

Path: `.github/workflows/validate.yml`

```yaml
name: validate

on:
  push:
    branches: [main, build]
  pull_request:
    branches: [main]

permissions:
  contents: read

jobs:
  validate:
    name: validate
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install jq + yq
        run: |
          sudo apt-get update -y
          sudo apt-get install -y jq
          sudo wget -qO /usr/local/bin/yq \
            https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64
          sudo chmod +x /usr/local/bin/yq

      - name: Frontmatter — every SKILL.md has name + description ≤ 1024
        run: |
          set -euo pipefail
          fail=0
          while IFS= read -r f; do
            yq -f extract '.name' "$f" >/dev/null \
              || { echo "::error file=$f::missing name"; fail=1; }
            desc=$(yq -f extract '.description' "$f" || echo "")
            len=${#desc}
            if [ -z "$desc" ]; then
              echo "::error file=$f::missing description"; fail=1
            elif [ "$len" -gt 1024 ]; then
              echo "::error file=$f::description $len > 1024 chars"; fail=1
            fi
          done < <(find skills -name SKILL.md)
          exit $fail

      - name: JSON files parse
        run: |
          set -e
          find . -name '*.json' \
            -not -path './node_modules/*' \
            -not -path './.git/*' \
            -print0 | xargs -0 -I{} jq empty "{}"

      - name: shared/legislation-tracking.md exists (v1.1)
        run: test -f shared/legislation-tracking.md

      - name: authority_type taxonomy consistency (v1.1)
        run: |
          # Every authority_type value used in references files must
          # appear in the schema enum.
          set -e
          schema_types=$(jq -r '.properties.authorities.items.properties.authority_type.enum[]' \
                         shared/output-schema.json | sort -u)
          # Extract all authority_type strings from references files
          # (rough heuristic — flag drift, don't enforce strict match)
          if grep -rh 'authority_type' skills/*/references/ 2>/dev/null \
             | grep -oE '"[A-Za-z_]+"' | sort -u > /tmp/used_types.txt; then
            for t in $(cat /tmp/used_types.txt | tr -d '"'); do
              if ! echo "$schema_types" | grep -qx "$t"; then
                echo "::warning::authority_type '$t' used in references but not in schema enum"
              fi
            done
          fi

      - name: No fabricated-citation sentinels in published skills
        run: |
          set -e
          if grep -rn 'CITATION NEEDED' skills/ \
             | grep -v '/template' \
             | grep -v '/states/' >/dev/null; then
            echo "::error::CITATION NEEDED sentinel found in published skill"
            grep -rn 'CITATION NEEDED' skills/ \
              | grep -v '/template' \
              | grep -v '/states/'
            exit 1
          fi

      - name: State stub completeness — 51 per state skill
        run: |
          set -e
          for skill in tax-research-state-income tax-research-state-salesuse; do
            n=$(ls skills/$skill/references/states/*.md 2>/dev/null | wc -l)
            if [ "$n" -ne 51 ]; then
              echo "::error::$skill has $n state files, expected 51"
              exit 1
            fi
          done

      - name: live-sources URL liveness (allow ≤ 5 flakes; retry once)
        run: |
          set -e
          urls=$(jq -r '.. | strings? | select(test("^https?://"))' \
                 shared/sources.json | sort -u)
          fail=0
          for u in $urls; do
            if ! curl -fsSL --max-time 15 -o /dev/null "$u"; then
              sleep 3
              if ! curl -fsSL --max-time 15 -o /dev/null "$u"; then
                echo "::warning::dead URL: $u"
                fail=$((fail+1))
              fi
            fi
          done
          [ $fail -le 5 ] || { echo "too many dead URLs ($fail). Investigate."; exit 1; }

      - name: Run project validate.sh
        run: bash ./scripts/validate.sh full

      - name: Plugin validate (if Claude Code CLI available)
        run: |
          if command -v claude >/dev/null 2>&1; then
            claude plugin validate . || true
          fi
```

`scripts/validate.sh` must include a `check_state_stubs` function called from the `phase 3` and `full` branches:

```bash
check_state_stubs() {
  local expected_codes="AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY"
  local fail=0
  for skill in tax-research-state-income tax-research-state-salesuse; do
    for code in $expected_codes; do
      f="skills/$skill/references/states/$code.md"
      if [ ! -f "$f" ]; then
        echo "MISSING: $f"
        fail=$((fail+1))
      else
        actual=$(yq -f extract '.state_code' "$f" 2>/dev/null || echo "")
        if [ "$actual" != "$code" ]; then
          echo "MISMATCH: $f frontmatter state_code='$actual' (expected $code)"
          fail=$((fail+1))
        fi
      fi
    done
  done
  return $fail
}

# v1.1 addition: confirm shared/legislation-tracking.md exists
check_legislation_tracking() {
  if [ ! -f shared/legislation-tracking.md ]; then
    echo "MISSING: shared/legislation-tracking.md"
    return 1
  fi
  return 0
}
```

---

## L. Handoff prompt — paste into Claude Code

Open a fresh session in `~/code/kisaes/vibe-cpa-skills`, run `claude`, then paste this exact text as the first message:

```
You are the Vibe CPA Skills build agent. I am Kurt — CPA, founder of
Kisaes LLC, builder of the Vibe family of self-hosted CPA software.
You have my authorization to autonomously build out the entire
28-skill repository under KisaesDevLab/vibe-cpa-skills. The repo is
already bootstrapped on disk and on GitHub; you are working on the
`build` branch.

Read these in order, then begin Phase 0 of BUILD_PLAN.md:
1. CLAUDE.md
2. BUILD_PLAN.md
3. shared/citation-discipline.md
4. shared/authority-hierarchy.md
5. shared/confidence-bands.md
6. shared/compliance.md
7. shared/legislation-tracking.md
8. shared/output-schema.json
9. shared/state-template.md
10. docs/skill-template.md
11. QUESTIONS.md

Operating rules:
- This is a fully autonomous run. Never stop to ask me a question.
  When ambiguous, append to QUESTIONS.md and proceed with a labeled
  assumption (see CLAUDE.md "Non-blocking question protocol").
- Tick BUILD_PLAN.md checkboxes only after the validation command
  for that line exits 0.
- Commit after every checkbox tick. Push to `build` at least every
  five ticks. Use Conventional Commits.
- Open a PR build → main at the end of each phase via
  `/open-phase-pr <N>`. Do NOT merge; do NOT push to main; do NOT
  create GitHub Releases — those are mine.
- The three flagship SKILL.md files (tax-research-federal,
  predict-worker-classification, return-summary-1040) are exemplars.
  If they don't yet exist on disk, create them first in Phase 1
  matching the rigor and structure described in CLAUDE.md and the
  skill-template.
- Citation discipline is non-negotiable. Use the `[CITATION
  NEEDED — search: <query>]` sentinel rather than fabricating. The
  CI rejects sentinels in published skills (excluding template and
  state-stub paths), so resolve them before ticking the relevant
  checkbox.
- The authority_type taxonomy is canonical in
  shared/citation-discipline.md and shared/output-schema.json. Use
  the extended v1.1 taxonomy: TreasuryDecision, FSA, OfficeMemo,
  InfoLetter, ATG, ISPPaper, IRSNewsRelease, Greenbook, CBOReport,
  StatutesAtLarge in addition to the v1.0 set.
- You may use any necessary CLI tooling: gh, git, mkdir, jq, yq,
  curl, node, python.

State scope is ALL 50 states + DC (51 jurisdictions). Phase 3
includes creating 102 state stub files (51 each in
tax-research-state-income/references/states/ and
tax-research-state-salesuse/references/states/), each copied from
shared/state-template.md with the canonical agency URL pre-filled
from shared/sources.json. Stubs ship with status: stub and TODO
markers — they are intentionally incomplete and will be filled in
post-launch by Kurt and contributors. Do NOT block on substantive
state research; populate the frontmatter and primary agency URL,
flag the no-income-tax / no-sales-tax states in their bodies, and
move on. The state router section in each state SKILL.md must list
all 51 codes and document the routing protocol.

Public-Law tracking (v1.1): the irc-section-lookup skill must
implement the workflow in shared/legislation-tracking.md — when the
user references a Public Law by popular name (TCJA, IRA, OBBBA,
SECURE 2.0, etc.) or by Public Law number, use the USC Popular Name
Tool and Classification Tables to resolve all affected USC sections.
The tax-research-federal and planning-multi-year skills should also
read shared/legislation-tracking.md for their legislative-history
workflows.

Success criteria:
- All BUILD_PLAN.md Phase 0–6 checkboxes ticked, including the 102
  state stub files, the new shared/legislation-tracking.md file, and
  the v1.1 skill-specific reference enhancements.
- `./scripts/validate.sh full` and `./scripts/run-evals.sh full`
  exit 0 locally; CI green on the build branch.
- Final phase opens a PR build → main with title "Phase 7 — release"
  and stops, awaiting my review and tag.
- README.md is installable: a reader can follow it to install in
  Claude Code via `/plugin marketplace add KisaesDevLab/vibe-cpa-skills`
  and in claude.ai by uploading a per-skill ZIP.

Begin now: read CLAUDE.md, then BUILD_PLAN.md, then start Phase 0.
Use /checkpoint before any /compact. Use /commit-phase <N> at the
end of each phase. If you hit a BLOCKING question, log it, do
whatever you safely can in other phases, and keep going.
```

---

## M. Time, sessions, tokens, model

**Realistic envelope.** Building 28 skills with references, evals, docs, CI, 102 state stub files, and the v1.1 skill-specific reference enhancements is roughly **20–30 hours of Claude Code wall time**, spread across **3–6 sessions** (auto-compaction kicks in around 75% of context; sessions naturally cap at 2–4 hours of dense work). The v1.1 additions add ~1–2 hours over v1.0 — primarily writing `shared/legislation-tracking.md`, the skill-specific reference files, and the legislation-tracking eval case.

**Token consumption.** Rough estimate: 9M–17M total tokens (input + output) across the build. SKILL.md authoring is medium-density; eval generation, reference research, state stub generation, and Public-Law-tracking workflow research dominate. Kurt's plan tier:

| Plan | Suitability |
|---|---|
| Pro | Tight; expect to hit weekly limits and need 5+ calendar days |
| Max (5x) | Comfortable; build completes in 2–3 calendar days |
| Max (20x) / Team | Comfortable single-day build with headroom |
| API direct | Most predictable cost; budget ~$75–$220 at Sonnet 4.6 list pricing |

**Recommended model.** Default to **Sonnet 4.6** for the bulk of the build (cost/throughput balance). Switch to **Opus 4.7** for: (1) the three flagship SKILL.md drafts in Phase 1 if they still need writing, (2) the strategy library structure decisions in Phase 4, (3) any phase where evals are failing and the issue is non-obvious, (4) the `irc-section-lookup` Public-Law-to-USC workflow design in Phase 3 (it's subtle). Use **Haiku 4** for the `/commit-phase` slash command's commit-message generation only.

Model names above reflect Anthropic's April 2026 default ladder. Verify with `claude /model` before pinning.

---

## N. Recovery and troubleshooting

**Claude Code times out mid-phase.** Reopen with `claude --continue` (or fresh `claude` — CLAUDE.md + BUILD_PLAN.md re-bootstrap state). The first unticked box in the lowest open phase is the resume point. The session log at the bottom of BUILD_PLAN.md tells you the last commit SHA.

**SKILL.md fails YAML validation.** Run `yq -f extract '.description' skills/<x>/SKILL.md | wc -c`. If > 1024 chars, trim. If frontmatter fails to parse, check that `---` opens at line 1, no tabs, no XML angle brackets in the description, and `name` is kebab-case with no reserved words `anthropic`/`claude`.

**Eval harness fails on a specific skill.** Run `./scripts/run-evals.sh skill <n>` and inspect the diff. Common causes: the skill's description doesn't trigger reliably (rewrite to be more "pushy"), or the SKILL.md body asks for output the eval's `expectations[]` doesn't match. Iterate on description first; then the body; then the eval expectations.

**State stub validation fails.** Run `./scripts/validate.sh full` and look for `MISSING:` or `MISMATCH:` lines from `check_state_stubs`. A common cause is a frontmatter `state_code` field that doesn't match the filename. Either rename the file to match the frontmatter or fix the frontmatter to match the filename — the canonical 2-letter codes are listed in BUILD_PLAN.md Phase 3e.

**Authority-type taxonomy drift.** If CI's "authority_type taxonomy consistency" check warns about a value used in references but not in the schema enum, either (a) add the value to the enum in `shared/output-schema.json` AND to the list in `shared/citation-discipline.md` if it's a legitimate new type, or (b) fix the reference file to use the canonical value. Don't suppress the warning silently.

**`shared/legislation-tracking.md` missing.** CI fails immediately. The file is required in v1.1; recreate from Section F.8 of the build plan.

**GitHub Actions CI breaks.** Inspect the failing job in `gh run view <run-id> --log`. Most failures fall into: dead URL in live-sources.md (replace with a working canonical or mirror), JSON parse error in a references file (run `jq empty` locally), description > 1024 chars (trim), or missing legislation-tracking.md. The CI tolerates 5 dead URLs to absorb transient flakes across the 51 state DOR set + the v1.1 expanded source set.

**`gh` CLI hits rate limits.** `gh api rate_limit` shows budget. If exhausted, set `GH_TOKEN` to a PAT with higher quota or wait an hour.

**Claude Code logs a BLOCKING question in QUESTIONS.md.** That's the design — Kurt resolves it inline, then on the next session Claude Code reads QUESTIONS.md first, sees the resolved tag, and applies it (potentially reverting an earlier labeled assumption).

**A phase PR is stuck on CI.** The CI is the source of truth. Don't force-merge. Have Claude Code iterate on the build branch until CI goes green; the deny rules block force-pushes anyway.

**Disk runs out of space.** Eval `runs/` directories accumulate. Add `evals/runs/` to .gitignore (already there) and prune locally.

---

## O. Post-build validation checklist

Once Claude Code reports done, run all of these manually:

```bash
# 1. Inventory
find skills -maxdepth 1 -mindepth 1 -type d | wc -l    # expect 29
                                                       # (28 + cpa-pack-index)
ls -1 skills | sort

# 2. Shared file inventory (v1.1: 8 files)
ls -1 shared/                                          # expect 8 files:
                                                       # citation-discipline.md
                                                       # authority-hierarchy.md
                                                       # confidence-bands.md
                                                       # compliance.md
                                                       # legislation-tracking.md
                                                       # live-sources.md
                                                       # sources.json
                                                       # output-schema.json
                                                       # state-template.md
                                                       # (9 files actually — 8 .md + 1 .json + 1 .json)

# 3. State stub inventory — expect 51 in each
ls skills/tax-research-state-income/references/states | wc -l   # expect 51
ls skills/tax-research-state-salesuse/references/states | wc -l # expect 51

# 4. Frontmatter spot-check
for f in skills/*/SKILL.md; do
  echo "=== $f ==="
  yq -f extract '.name, .description' "$f" | head -c 200; echo
done | less

# 5. Citation-discipline spot-check on three random skills
shuf -n 3 -e skills/*/SKILL.md | while read f; do
  echo "=== $f ==="
  grep -nE 'I\.R\.C\.|Treas\. Reg\.|Rev\. Rul\.|F\.\dd|T\.C\.' "$f" | head
done

# 6. JSON parses everywhere
find . -name '*.json' -not -path './node_modules/*' -print0 \
  | xargs -0 -I{} jq empty "{}" && echo OK

# 7. Authority-type enum used in output-schema matches list in
#    citation-discipline (manual cross-check)
jq -r '.properties.authorities.items.properties.authority_type.enum[]' \
  shared/output-schema.json | sort -u

# 8. Plugin validates
claude plugin validate .

# 9. Eval pass rate
./scripts/run-evals.sh full --summary

# 10. Live URLs (allow up to 5 flakes)
jq -r '.. | strings? | select(test("^https?://"))' shared/sources.json \
  | sort -u | xargs -I{} curl -fsSL --max-time 10 -o /dev/null {} \
  && echo OK

# 11. CI green
gh pr checks --watch
gh run list --branch build --limit 5

# 12. Test install in Claude Code
claude /plugin marketplace add KisaesDevLab/vibe-cpa-skills
claude /plugin install vibe-cpa-pack@kisaes-cpa-skills
claude   # then in chat:
         # "Run a federal tax research check on §199A QBI"
         # "Research New York convenience-of-employer rule for a remote
         #  worker living in NJ working for a NY firm"
         # "What did OBBBA change in IRC §174?" (exercises Public-Law
         #  workflow added in v1.1)

# 13. Test install in claude.ai
#     - Package one skill: python -m scripts.package_skill skills/tax-research-federal
#     - Settings → Features → Skills → upload the .skill file
#     - Test prompt: "Use the federal tax research skill to research..."

# 14. Tag and release (Kurt does these — NOT Claude Code)
gh pr merge <phase-7-pr> --squash --delete-branch=false
git checkout main && git pull
git tag -a v1.0.0-beta -m "v1.0.0-beta initial release (50 states + DC; v1.1 build plan)"
git push origin v1.0.0-beta
gh release create v1.0.0-beta \
  --title "v1.0.0-beta — Vibe CPA Skills" \
  --notes-file CHANGELOG.md \
  --prerelease
```

---

## P. After Claude Code finishes

1. **Review the Phase 7 PR.** Merge into main with squash. Don't delete the build branch — keep it for fast follow-up commits.
2. **Tag and release** v1.0.0-beta as shown in Section O step 14.
3. **Smoke test in claude.ai** with one packaged skill ZIP, run a real CPA scenario end-to-end including:
   - A state-specific scenario (CA AB5, NY convenience rule, WA capital gains tax)
   - A Public-Law-tracking scenario ("what changed in §174 under OBBBA") to exercise the v1.1 legislation-tracking workflow
   - Confirm the JSON sidecar matches `shared/output-schema.json` including the `public_laws_consulted` array
4. **Smoke test in Claude Code** via `/plugin marketplace add` and `/plugin install`, then run the same scenarios.
5. **Flip the repo public** when comfortable (`gh repo edit KisaesDevLab/vibe-cpa-skills --visibility public --accept-visibility-change-consequences`).
6. **Announce.** Recommended channels: a LinkedIn post tagging the AICPA tax community, a tweet/X thread on tax-pro Twitter, a Hacker News "Show HN" post (BSL 1.1 with 4-year change date is unusual enough to draw discussion), and a short loom of one skill in action. Lead with the differentiators: open, self-hostable, citation-disciplined, SSTS-/Circular-230-aware, all-50-states + DC scope, with USC Classification Table workflow for tracking recent legislation.
7. **Solicit eval, state-stub, and legislation-tracking contributions.** Add issue templates `Eval case proposal`, `State stub promotion`, and `Public-Law tracking entry` so practitioners can submit their own real cases (sanitized), promote individual state stubs, and add new Public Laws to the legislation-tracking quick reference.
8. **Plan v1.0.0** (drop `-beta`) once you have ≥ 90% eval pass rate across all 28 skills, at least 10 external user reports confirming citation discipline holds in real practice, and at least 8 state stubs promoted to `reviewed` status.

---

## Final checklist before pasting the handoff prompt

- [ ] Section A pre-flight checks all pass.
- [ ] Bootstrap script (Section C) has been run; the repo exists on GitHub under KisaesDevLab and a `build` branch is checked out.
- [ ] CLAUDE.md (Section D), BUILD_PLAN.md (Section E), `shared/*` (Section F including `legislation-tracking.md` and `state-template.md`), `docs/skill-template.md` (Section G), seven slash commands in `.claude/commands/` (Section H), `.claude/settings.local.json` with v1.1 expanded WebFetch allowlist (Section I), QUESTIONS.md (Section J), and `.github/workflows/validate.yml` plus `scripts/validate.sh` (Section K) all exist on disk.
- [ ] You are in `~/code/kisaes/vibe-cpa-skills` and `claude` opens cleanly with the right model selected.
- [ ] You are emotionally prepared for Claude Code to log questions to QUESTIONS.md you'll need to skim periodically.

When all boxes are ticked, paste the Section L handoff prompt and let it run. Check in every few hours; resolve QUESTIONS.md inline; review the per-phase PRs as they appear.
