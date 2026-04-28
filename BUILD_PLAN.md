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
- [x] Commit: `chore(p0): bootstrap shared/ + scripts + CI skeleton`
- [x] Push to build; open draft PR to main

## Phase 1 — Three flagship skills + dispatcher + eval harness

Validation: `./scripts/validate.sh phase 1 && ./scripts/run-evals.sh phase 1`

- [x] skills/cpa-pack-index/SKILL.md (always-on dispatcher; routes
      Public-Law popular names like "OBBBA"/"TCJA" to irc-section-lookup)
- [x] skills/tax-research-federal/SKILL.md (flagship)
- [x] skills/tax-research-federal/references/{authority-weights.md, retrieval-checklist.md, legislative-history.md}
- [x] skills/predict-worker-classification/SKILL.md (flagship)
- [x] skills/predict-worker-classification/references/{factors-20.md,case-law.md}
- [x] skills/return-summary-1040/SKILL.md (flagship)
- [x] skills/return-summary-1040/references/{line-keys.md,red-flags.md}
- [x] evals/research/tax-research-federal.json (≥ 3 cases; include 1
      legislative-history case exercising JCT/Greenbook/CBO citations)
- [x] evals/prediction/predict-worker-classification.json (≥ 3 cases)
- [x] evals/summary/return-summary-1040.json (≥ 3 cases)
- [x] CI green
- [x] Commit: `feat(p1): three flagships + dispatcher + eval harness`

## Phase 2 — Prediction (11) + research (4) + 1 summary + notice

Validation: `./scripts/validate.sh phase 2 && ./scripts/run-evals.sh phase 2`

Predictions (11 — worker-classification already in Phase 1):
- [x] predict-hobby-loss
- [x] predict-reasonable-comp
- [x] predict-real-estate-pro
- [x] predict-material-participation
- [x] predict-qbi-eligibility
- [x] predict-1031-qualification
- [x] predict-economic-substance
- [x] predict-debt-vs-equity
- [x] predict-innocent-spouse
- [x] predict-reasonable-cause
      (references include: irs-data-book-penalty-stats.md citing
      IRS Data Book penalty-abatement statistics as
      persuasive_non_authority)
- [x] predict-r-and-d-credit

Research (4 — federal already in Phase 1):
- [x] tax-research-entity
- [x] tax-research-payroll
- [x] tax-research-international
      (references include: treaties-a-to-z.md pointing to IRS
      Treaties A–Z; oecd-model-treaty.md pointing to OECD Tax)
- [x] tax-research-procedure
      (references include: tax-court-rules.md, doj-tax-division.md,
      irs-data-book-audit-rates.md, dawson-freshness-feeds.md)

Summary + notice:
- [x] return-summary-entity
- [x] notice-response

For each: SKILL.md + references/ + 1 eval case minimum.
- [x] Commit per family with conventional message; push frequently.

## Phase 3 — Planning (3) + remaining research (3) + utilities (5) + compliance (1) + 51 state stubs × 2 skills

Validation: `./scripts/validate.sh phase 3 && ./scripts/run-evals.sh phase 3`

### 3a. Planning skills
- [x] planning-actions-1040
- [x] planning-actions-entity
- [x] planning-multi-year
      (references include: legislation-tracking-pointer.md
      cross-referencing shared/legislation-tracking.md for
      reconciliation-bill scoring context)

### 3b. Remaining research skills (state shells + estate/gift)
- [x] tax-research-state-income (SKILL.md + references/ + state router logic)
- [x] tax-research-state-salesuse (SKILL.md + references/ + state router logic)
- [x] tax-research-estate-gift

### 3c. Utilities
- [x] irc-section-lookup
      (references include: legislation-tracking.md implementing the
      Public-Law-to-USC workflow per shared/legislation-tracking.md;
      subtitle-map.md documenting IRC Subtitles A–K)
- [x] treas-reg-lookup
      (references include: treasury-decisions.md distinguishing TDs
      from codified TreasReg)
- [x] form-line-explainer
- [x] due-date-calculator
- [x] penalty-interest-calc

### 3d. Compliance
- [x] compliance-ssts-circular230
      (references include: irs-guidance-primer.md citing the IRS
      "Understanding IRS Guidance — A Brief Primer" page)

### 3e. State stubs — tax-research-state-income (51 files)

For each jurisdiction, copy `shared/state-template.md` to
`skills/tax-research-state-income/references/states/<XX>.md`,
populate the YAML frontmatter, and pre-fill the primary agency URL
from `shared/sources.json`. Status remains `stub` until edited.

- [x] AL — Alabama
- [x] AK — Alaska *(no individual income tax — note in body)*
- [x] AZ — Arizona
- [x] AR — Arkansas
- [x] CA — California *(FTB primary; note CDTFA/EDD splits)*
- [x] CO — Colorado
- [x] CT — Connecticut
- [x] DE — Delaware
- [x] DC — District of Columbia
- [x] FL — Florida *(no individual income tax)*
- [x] GA — Georgia
- [x] HI — Hawaii
- [x] ID — Idaho
- [x] IL — Illinois
- [x] IN — Indiana
- [x] IA — Iowa
- [x] KS — Kansas
- [x] KY — Kentucky
- [x] LA — Louisiana
- [x] ME — Maine
- [x] MD — Maryland
- [x] MA — Massachusetts *(note 4% surtax over $1M)*
- [x] MI — Michigan
- [x] MN — Minnesota
- [x] MS — Mississippi
- [x] MO — Missouri
- [x] MT — Montana
- [x] NE — Nebraska
- [x] NV — Nevada *(no individual income tax)*
- [x] NH — New Hampshire *(I&D tax repealed 2025)*
- [x] NJ — New Jersey
- [x] NM — New Mexico
- [x] NY — New York *(note convenience-of-employer rule)*
- [x] NC — North Carolina
- [x] ND — North Dakota
- [x] OH — Ohio
- [x] OK — Oklahoma
- [x] OR — Oregon
- [x] PA — Pennsylvania
- [x] RI — Rhode Island
- [x] SC — South Carolina
- [x] SD — South Dakota *(no individual income tax)*
- [x] TN — Tennessee *(Hall tax repealed)*
- [x] TX — Texas *(no individual income tax)*
- [x] UT — Utah
- [x] VT — Vermont
- [x] VA — Virginia
- [x] WA — Washington *(capital gains tax in effect; no general income tax)*
- [x] WV — West Virginia
- [x] WI — Wisconsin
- [x] WY — Wyoming *(no individual income tax)*

Validation: `test "$(ls skills/tax-research-state-income/references/states/*.md | wc -l)" -eq 51`

### 3f. State stubs — tax-research-state-salesuse (51 files)

Same procedure. Where a state has no sales tax (AK¹, DE, MT, NH, OR),
include a reference file noting the fact and pointing to local-option
authority where applicable.
¹ Alaska has no statewide sales tax but local sales taxes; flag clearly.

- [x] AL [x] AK [x] AZ [x] AR [x] CA [x] CO [x] CT [x] DE [x] DC [x] FL
- [x] GA [x] HI [x] ID [x] IL [x] IN [x] IA [x] KS [x] KY [x] LA [x] ME
- [x] MD [x] MA [x] MI [x] MN [x] MS [x] MO [x] MT [x] NE [x] NV [x] NH
- [x] NJ [x] NM [x] NY [x] NC [x] ND [x] OH [x] OK [x] OR [x] PA [x] RI
- [x] SC [x] SD [x] TN [x] TX [x] UT [x] VT [x] VA [x] WA [x] WV [x] WI [x] WY

Validation: `test "$(ls skills/tax-research-state-salesuse/references/states/*.md | wc -l)" -eq 51`

### 3g. State router logic
Both state SKILL.md files must implement a routing pattern: when the
user mentions a state by name, abbreviation, or distinctive feature
(e.g., "FTB", "Comptroller", "convenience rule"), the skill loads the
corresponding `references/states/<XX>.md` before drafting analysis.

- [x] tax-research-state-income SKILL.md includes state router section
- [x] tax-research-state-salesuse SKILL.md includes state router section
- [x] Both list all 51 jurisdiction codes in a "Supported jurisdictions"
      block at the top of the SKILL.md body.
- [x] Both reference Tax Foundation Center for State Tax Policy as
      `persuasive_non_authority` secondary supplement (NOT authority)
      with explicit caveat language.

### 3h. Phase commit
- [x] `/commit-phase 3 "planning + state shells + 51 state stubs × 2"`

## Phase 4 — Strategy library (30 entries)

Validation: `./scripts/validate.sh phase 4`

- [x] skills/planning-strategy-library/SKILL.md
- [x] skills/planning-strategy-library/references/strategies/<slug>.md
      for all 30 strategies (list in shared/strategy-list.md derived
      from this plan's appendix)
- [x] Each strategy file: IRC §, eligibility, mechanics, citations,
      Dirty-Dozen / Listed-Transaction flag where applicable
- [x] Strategies with state-specific eligibility (PTET, CA AB5, NY
      convenience rule, MA millionaire surtax, WA capital gains tax,
      OR transit tax) reference per-state files via:
      `> See state files for jurisdiction-specific eligibility: CA, NY, ...`
- [x] Strategies materially affected by recent legislation (post-2024)
      reference shared/legislation-tracking.md and link to
      Classification Tables for the relevant Public Law.
- [x] index.md cross-references all 30
- [x] Commit: `feat(p4): 30-strategy planning library`

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

2026-04-27 | phase 2 complete | items: predict-hobby-loss + reasonable-comp evals; +9 prediction skills (real-estate-pro, material-participation, qbi-eligibility, 1031-qualification, economic-substance, debt-vs-equity, innocent-spouse, reasonable-cause, r-and-d-credit); +4 research skills (entity, payroll, international, procedure); return-summary-entity; notice-response. Validate phase 2 + run-evals phase 2 both green (4 pass / 0 fail; 20 eval files pass). Branch: build. Last commit before plan-tick: 98f591c.

2026-04-27 | phase 3 complete | items: 3a planning skills (1040, entity, multi-year); 3b state shells + estate-gift; 3c utilities (irc-section-lookup w/Public-Law-to-USC workflow, treas-reg-lookup, form-line-explainer, due-date-calculator, penalty-interest-calc); 3d compliance-ssts-circular230; 3e+3f 102 state stubs auto-generated via scripts/generate_state_stubs.py with status:stub frontmatter and primary agency URL pre-filled from shared/sources.json; 3g state router protocol implemented in both state SKILL.md files. Validate phase 3 + run-evals full both green (5 pass / 0 fail; 32+ eval files pass). Branch: build.
