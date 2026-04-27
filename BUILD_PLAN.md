# Build Plan — Vibe CPA Skills

**Goal:** Ship `v1.0.0-beta` with 28 skills, 1 dispatcher, 8 shared
files, 102 state stub files, full eval harness, README, and a green CI.

Tick `[x]` only after the validation command for that line exits 0.

---

## Phase 0 — Bootstrap verification & shared/

Validation: `./scripts/validate.sh phase 0`

- [x] Confirm directory tree matches: skills/ shared/ scripts/ evals/
      examples/ docs/ .claude-plugin/ .claude/ .github/
- [x] Confirm files: CLAUDE.md, BUILD_PLAN.md, QUESTIONS.md,
      LICENSE (BSL 1.1), DISCLAIMER.md, CONTRIBUTING.md,
      CHANGELOG.md, README.md, .gitignore
- [x] Write shared/citation-discipline.md
- [x] Write shared/authority-hierarchy.md
- [x] Write shared/confidence-bands.md
- [x] Write shared/compliance.md
- [x] Write shared/live-sources.md (incl. all 50 + DC table; incl.
      extended IRS, Tax Court, USC tools, legislative branch,
      policy data, international, current-awareness sections)
- [x] Write shared/sources.json (incl. all 51 state_dors entries
      AND extended blocks: irs_extended, tax_court_extended,
      doj_tax_division, uscode_tools, legislative_branch,
      policy_data, international_extended, free_case_databases_extended,
      current_awareness_non_authority)
- [x] Write shared/output-schema.json
- [x] Write shared/state-template.md (incl. optional Secondary
      policy data section)
- [x] Write shared/legislation-tracking.md (NEW in v1.1)
- [x] Write docs/skill-template.md
- [x] Write scripts/validate.sh (validates frontmatter, description
      length, JSON parse, URL liveness, state-stub completeness,
      authority_type taxonomy consistency)
- [x] Write scripts/run-evals.sh (subagent-pair harness; reads
      evals/<family>/<skill>.json)
- [x] Write .github/workflows/validate.yml
- [x] Write .claude-plugin/plugin.json skeleton
- [x] Write .claude-plugin/marketplace.json skeleton
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
