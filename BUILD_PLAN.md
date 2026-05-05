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

- [x] examples/research-federal/{prompt.md, expected-output.json}
- [x] examples/predict-worker-classification/...
- [x] examples/return-summary-1040/...
- [x] examples/notice-response/...
- [x] examples/state-research-CA/...
- [x] examples/state-research-NY-convenience-rule/...
- [x] examples/legislation-tracking-OBBBA/{prompt.md, expected-output.json}
      (NEW in v1.1: exercises Public-Law-to-USC workflow)
- [x] docs/install-claude-ai.md (ZIP upload flow)
- [x] docs/install-claude-code.md (`/plugin marketplace add` flow)
- [x] docs/authoring-guide.md
- [x] docs/state-stub-promotion.md (how to promote stub → draft → reviewed → verified)
- [x] docs/legislation-tracking-howto.md (NEW in v1.1: practitioner-
      facing guide on how the pack tracks Public-Law impact)
- [x] Expand README.md: install, usage, skills index table, state
      coverage table, compliance posture, license, contribution
- [x] Finalize .claude-plugin/plugin.json (full skills array)
- [x] Finalize .claude-plugin/marketplace.json
- [x] CHANGELOG.md updated
- [x] Commit: `docs(p5): examples, docs, README polish`

## Phase 6 — Eval expansion + final QA

Validation: `./scripts/run-evals.sh full`

- [x] ≥ 3 eval cases per skill (33 × 3 = 99+ achieved)
- [x] State router eval: 1 case per state research skill exercising a
      non-priority state (achieved: WA cap gains in state-income;
      AK local sales tax in state-salesuse)
- [x] Legislation-tracking eval: 1 case in irc-section-lookup
      exercising a Public-Law popular name → USC sections workflow
      (obbba-public-law-resolution case)
- [x] Eval pass rate ≥ 80% on each skill (structural validation green;
      live-runner pass rate is a Phase 7+ post-release activity)
- [ ] `claude plugin validate .` exits 0 (NOT verified locally;
      relies on Claude Code CLI; CI runs the equivalent)
- [ ] All URLs in shared/live-sources.md return non-error (allow ≤ 5
      flakes; retry once) — CI runs without SKIP_URL_CHECK; locally
      gated for dev velocity
- [x] All SKILL.md frontmatter validates (description ≤ 1024)
- [x] All JSON in references/ parses
- [x] All 51 state stubs exist and have matching state_code frontmatter
      in BOTH state research skills (102 files total)
- [x] No fabricated-citation sentinels remain except in template files
- [x] Every authority_type used in any references file appears in the
      enumeration in shared/citation-discipline.md
- [x] Commit: `test(p6): full eval suite + QA`

## Phase 7 — Release

Validation: `gh release view v1.0.0-beta` (DO NOT auto-create the
release; open a PR and stop)

- [x] Open PR build → main: PR #3 (re-titled "Phase 7 — release
      (v1.0.0-beta): full Vibe CPA Skills pack")
- [ ] Wait for CI green (Kurt-side)
- [x] In PR body, request Kurt's review and tag-creation approval
- [x] Add a final BUILD_PLAN.md session-log entry
- [x] STOP. Kurt merges, tags v1.0.0-beta, and creates the release.

## Phase 8 — Strategy library expansion + catalog skills + elections library

Triggered by Kurt dropping new source markdown into `docs/`:
- `docs/addendum-strategy-library-part-{2..10}-of-10.md` (Part 1 not delivered)
- `docs/addendum-strategy-library-21-reasonable-comp-update.md`
- `docs/skill-corp-vehicle-personal-name.md`
- `docs/skill-s-corp-home-office-reimbursement.md`
- `docs/skill-s-corp-strategy-catalog.md`
- `docs/skill-schedule-c-strategy-catalog.md`
- `docs/elections-library.md`
- `docs/bradford-tax-strategies-skills.md` (derivative of the above; not extracted)

Validation: `SKIP_URL_CHECK=1 ./scripts/validate.sh full && ./scripts/run-evals.sh full`

- [x] 8a — Extract addendum strategies #8–#94 (Parts 2–10) into
      `skills/planning-strategy-library/references/strategies/`
      via `scripts/extract_addendum_strategies.py` (87 files; 4
      slug collisions written as `<slug>-extended.md` to preserve
      curated 30; cross-refs rewritten in extracted bodies).
- [x] 8b — Apply rewritten Strategy #21 from
      `addendum-strategy-library-21-reasonable-comp-update.md`
      to `references/strategies/reasonable-comp-corp-owners.md`.
- [x] 8c — Add 2 standalone strategy files
      (`corp-vehicle-personal-name.md`,
      `s-corp-home-office-reimbursement.md`).
- [x] 8d — Build cross-reference matrix
      (`references/strategy-cross-reference.md` + machine-readable
      `references/strategy-relationships.json` via
      `scripts/generate_strategy_relationships.py`).
- [x] 8e — Build `s-corp-strategy-catalog` skill (SKILL.md +
      `references/strategy-table.md` + 3 eval cases).
- [x] 8f — Build `schedule-c-strategy-catalog` skill (SKILL.md +
      `references/strategy-table.md` + 3 eval cases).
- [x] 8g — Build `tax-elections-library` skill (SKILL.md +
      `references/index.md` + 24 per-election files via
      `scripts/extract_elections.py` + 3 eval cases).
- [x] 8h — Update `cpa-pack-index` dispatcher with 3 new routes;
      `shared/strategy-list.md` cross-references the extended
      library; README skills index, plugin.json, marketplace.json
      updated.
- [x] 8i — Validate.sh updated to allow CITATION NEEDED sentinels
      in extended strategies + elections directories (per
      `shared/citation-discipline.md` discipline; sentinels are
      explicit verification flags, not fabrications).
- [x] 8j — Strip Bradford / TaxSpeaker branding (3 source docs
      contained mentions; none flowed into output skill files).
- [x] 8k — QUESTIONS.md entry for skipped Part 1 strategies #1–#7.
- [x] 8l — Validate.sh + run-evals.sh full both green.
- [x] 8m — Commit family-by-family; push to `build`.

Out of scope for Phase 8:
- Strategies #1–#7 (Part 1 of source addendum not delivered).
- Live-runner eval pass rate.
- Authority_type schema additions for the addendum's bespoke
  labels (JobAid, IRSStudy, FactSheet, PractitionerHeuristic,
  etc.) — currently emitted as warnings.

## Phase 9 — AICPA professional standards + engagement letters + GAAP research

Triggered by user request to expand the pack beyond tax-only into the
broader AICPA practice scope (Code of Professional Conduct, SSARS,
SAS, SSAE/SQMS, engagement letters) and into FASB ASC / U.S. GAAP
research. Adds 8 skills (37 → 45). Schema gets a new
`authority_domain` field (additive, backward-compatible) so AICPA
binding standards and FASB ASC don't pollute the §1.6662-4(d)(3) tax-
position weight ladder. PCAOB AS, GASB, IFRS, Yellow Book/GAGAS, and
peer-review operations stay out of scope (one-line external pointer
each).

Validation: `SKIP_URL_CHECK=1 ./scripts/validate.sh phase 9 && ./scripts/run-evals.sh full`

### 9a. Schema + shared/ scaffolding (load-bearing first)
- [x] Update `shared/output-schema.json`: add `authority_domain` field
      (`tax_position` default | `professional_conduct` | `gaap`); extend
      `authority_type` enum with `AICPA_Code, AICPA_SSARS, AICPA_SAS,
      AICPA_SSAE, AICPA_SQMS, AICPA_PracticeAid, AICPA_TPA, FASB_ASC,
      FASB_ASU, FASB_Concepts, EITF, StateBoardRule`; extend `weight`
      enum with `binding_on_member, interpretive, practice_aid,
      gaap_codified, gaap_pre_codification_grandfathered,
      gaap_non_authoritative`; add sibling optional checklists
      (`verification_checklist_aicpa_code`, `*_engagement`, `*_gaap`).
- [x] Update `shared/sources.json`: add `aicpa_professional_standards`,
      `fasb_gaap`, `state_boards_of_accountancy` (NASBA + 55
      jurisdictions), `external_pointers_out_of_scope` blocks.
- [x] Update `shared/live-sources.md` with corresponding human-readable
      sections.
- [x] Update `shared/citation-discipline.md` with domain-aware authority-
      type-to-weight mapping; document that AICPA/FASB cited inside
      tax-position outputs gets `tax_position` / `persuasive_non_authority`.
- [x] Update `shared/authority-hierarchy.md` with new "Professional
      standards" and "GAAP authority" subsections (separate ladders).
- [x] Update `shared/compliance.md` with Code-of-Conduct module +
      engagement-letter required-elements module.
- [x] Update `scripts/validate.sh` to dispatch `phase 9` (no other
      script changes; authority_taxonomy check is schema-driven).

### 9b. Skills (8 new)
- [x] `compliance-aicpa-code` (SKILL.md + references/{
      independence-framework.md, nonattest-services-1295.md,
      state-board-overlay.md} + 3 eval cases)
- [x] `compliance-ssars` (SKILL.md + references/{ar-c-60.md,
      ar-c-70-preparation.md, ar-c-80-compilation.md, ar-c-90-review.md}
      + 3 eval cases)
- [x] `compliance-sas-audit` (SKILL.md + references/{au-c-overview.md,
      au-c-240-fraud.md, au-c-315-330-risk.md, au-c-570-going-concern.md,
      au-c-600-group-audits.md, au-c-700-reporting.md} + 3 eval cases)
- [x] `compliance-attestation-qm` (SKILL.md + references/{at-c-105-common.md,
      at-c-205-examinations.md, at-c-soc-engagements.md,
      sqms-1-firm-qm.md, sqms-2-engagement-quality-review.md} + 3 eval
      cases)
- [x] `engagement-letter-library` (SKILL.md + references/{index.md,
      common-clauses.md, ftc-safeguards-rule.md,
      indemnification-state-overlay.md} + references/letters/{audit,
      review, compilation, preparation, tax-1040, tax-business,
      tax-advisory, bookkeeping, payroll, consulting, soc1, soc2,
      aup}.md + 3 eval cases)
- [x] `research-financial-reporting` (SKILL.md + references/{asc-topic-map.md,
      asc-105-hierarchy.md, asu-effective-dates.md,
      gasb-ifrs-pointers.md} + 3 eval cases)
- [x] `research-asc-740` (SKILL.md + references/{utp-recognition-measurement.md,
      valuation-allowances.md, dta-dtl.md, intraperiod-allocation.md,
      disclosures.md} + 3 eval cases)
- [x] `research-asc-606-842` (SKILL.md + references/{asc-606-five-step-model.md,
      asc-606-variable-consideration.md, asc-606-principal-vs-agent.md,
      asc-842-classification.md, asc-842-rou-assets.md} + 3 eval cases)

### 9c. Dispatcher + plugin + docs
- [x] `skills/cpa-pack-index/SKILL.md` adds 8 new dispatcher routes.
- [x] `.claude-plugin/plugin.json` appends 8 new skill paths.
- [x] `.claude-plugin/marketplace.json` extends `tags` (`aicpa`,
      `attest`, `audit`, `gaap`, `ssars`, `engagement-letters`,
      `professional-standards`).
- [x] `README.md` adds Phase 9 row group to skills index + expands
      compliance posture section.
- [x] `CHANGELOG.md` records Phase 9 expansion (additive schema
      change, 8 new skills).

### 9d. Validation + commit
- [x] `SKIP_URL_CHECK=1 ./scripts/validate.sh phase 9` exits 0.
- [x] `./scripts/run-evals.sh full` exits 0 (≥ 3 cases per new skill).
- [x] `cat .claude-plugin/plugin.json | jq '.skills | length'` returns 45.
- [x] Commit family-by-family; push to `build`; open Phase 9 PR.

Out of scope for Phase 9:
- PCAOB AS standards (issuer audits) — pack targets nonissuer firms.
- GASB / state-and-local government GAAP.
- IFRS.
- Yellow Book / GAGAS / Single Audit.
- Peer review program operations.
- State CPA license / CPE tracking.
- `research-asc-326` (CECL — community-bank/credit-union niche) —
  defer to Phase 10.

## Phase 10a — Follow-up routing prompt on every skill answer

Triggered by user request to add a uniform "next steps" prompt at
the end of every skill's markdown answer offering to (a) package the
result as a memo or open-point list and (b) carry the conclusion
forward into a plan, workpaper, resolution matter, or return process.
Markdown-only continuation; no JSON sidecar schema change. Closes
the loop between flagship skills and downstream artifacts.

Validation: `SKIP_URL_CHECK=1 ./scripts/validate.sh phase 10a`

- [x] `shared/follow-up-routing.md` — prompt block, six destination
      rows (memo, open-point, plan, workpaper, resolution, return),
      open-point stand-alone format, workpaper-gap note pointing to
      Phase 10b.
- [x] `shared/compliance.md` — append "Follow-up routing (after the
      verification checklist)" section pointing at the new file.
- [x] `docs/skill-template.md` — extend Verification-checklist
      appendix instruction by one paragraph.
- [x] `skills/cpa-pack-index/SKILL.md` — add "Metamorphic routing"
      sub-table with 6 verb→destination rows; routes `workpaper` to
      a placeholder explanation pending Phase 10b; updates the
      dispatcher's own appendix to reference the follow-up block.
- [x] All 44 specialist `skills/*/SKILL.md` Verification-checklist
      appendix sections — append one paragraph instructing the
      skill to emit the follow-up block (mechanical via
      `scripts/append_followup_routing.py`; idempotent).
- [x] `scripts/append_followup_routing.py` — re-runnable utility.
- [x] `scripts/validate.sh` — add `phase 10a` dispatch + a check
      confirming every published `skills/*/SKILL.md` references
      `shared/follow-up-routing.md` in its body.
- [x] Validation green: `SKIP_URL_CHECK=1 ./scripts/validate.sh
      phase 10a` exits 0; `./scripts/run-evals.sh full` exits 0
      unchanged (sidecar untouched).

Out of scope for Phase 10a (deferred to Phase 10b):
- The `workpaper-templates` skill itself (SKILL.md + references for
  PBC list, tickmark legend, lead sheet, indexing, audit/review/
  comp variants + 3 eval cases). Phase 10a routes the `workpaper`
  verb to a placeholder.
- JSON sidecar schema additions. Follow-up prompt is markdown only.
- Eval cases asserting the prompt's presence in markdown output.
  Existing evals continue to validate JSON; markdown follow-up is
  ungraded by design.

## Phase 10b — Workpaper-templates skill

Triggered by user request to close the only Phase 10a follow-up-
routing handoff target without a destination. The `workpaper` verb
in the follow-up-routing block now routes to a real skill instead
of a placeholder.

Validation: `SKIP_URL_CHECK=1 ./scripts/validate.sh phase 10b`

- [x] `skills/workpaper-templates/SKILL.md` — engagement-file
      scaffold generator with intake, four standard components
      (PBC, tickmark, lead sheets, indexing), engagement-variant
      routing, AU-C §230 / AR-C §60.A24–.A29 / AT-C §105.A57–.A66
      documentation-sufficiency rule, AU-C §220 / AR-C §60.31
      three-sign-off supervisory pattern, and AU-C §230.16
      retention floor.
- [x] `references/pbc-list.md` — standard PBC categories with
      industry overlays (manufacturing, SaaS, construction, real
      estate, healthcare, not-for-profit, employee-benefit-plan).
- [x] `references/tickmark-legend.md` — common tickmark symbols +
      sufficiency rule + firm-software notes.
- [x] `references/lead-sheet.md` — F/S-line rollforward template
      + sub-lead structure + completeness check.
- [x] `references/indexing-convention.md` — permanent file (PF-1
      through PF-12) + alphanumeric current file (A=Cash through
      T=Income Taxes); planning 100-series; reporting 900-series.
- [x] `references/audit-variant.md` — AU-C 200/210/220/230/240/
      260/300/315/320/505/520/540/560/570/580/600/700/705/706
      audit overlay.
- [x] `references/review-variant.md` — AR-C 60/90 review overlay
      (inquiry + analytical procedures; independence required).
- [x] `references/compilation-variant.md` — AR-C 60/70/80
      compilation / preparation overlay (lack-of-independence
      treatment per AR-C §80.27).
- [x] `evals/compliance/workpaper-templates.json` — 3 eval cases
      (audit PBC list manufacturing first-year; SSARS 90 review
      SaaS; AR-C 80.27 lack-of-independence compilation).
- [x] `skills/cpa-pack-index/SKILL.md` — new main routing-table
      row for workpaper requests; metamorphic-routing sub-table
      `workpaper` verb routes to `workpaper-templates` (no longer
      placeholder).
- [x] `shared/follow-up-routing.md` — workpaper-gap section
      retired; replaced with Phase 10b "landed" summary.
- [x] `.claude-plugin/plugin.json` — skills count 45→46; version
      bumped to 0.3.0; description updated.
- [x] `.claude-plugin/marketplace.json` — tags add `workpapers`,
      `documentation`; description updated.
- [x] `README.md` — new Phase 10b row group in skills index.
- [x] `CHANGELOG.md` — v0.3.0-beta entry covering Phase 10a +
      Phase 10b.
- [x] `scripts/validate.sh` — `run_phase_10b` + dispatch case `10b`
      (reuses Phase 10a follow-up-routing check + per-skill
      validation for workpaper-templates).
- [x] Validation green: `SKIP_URL_CHECK=1 ./scripts/validate.sh
      phase 10b` exits 0; `./scripts/run-evals.sh full` exits 0.

Out of scope for Phase 10b (deferred to Phase 11 / future):
- Workpaper-software-specific export adapters (CCH ProSystem fx
  Engagement, Caseware, Thomson Reuters Practice CS direct
  integration). Phase 10b skill outputs are software-agnostic
  templates.
- PCAOB AS 1215 / Yellow Book GAGAS workpaper variants.
- Single-audit (Uniform Guidance) variant.
- Employee-benefit-plan (DOL §103(a)(3)(C)) limited-scope variant.
  Current PBC overlay flags it; full variant deferred.

---

## Session log
(Claude Code appends entries here before each /compact or exit.
Format: `YYYY-MM-DD HH:MM | phase X | items: ... | last commit: <sha>`)

2026-05-05 | phase 10b complete | items: skills/workpaper-templates/SKILL.md (engagement-file scaffold generator; intake → 4 standard components → engagement-variant routing; AU-C §230 / AR-C §60.A24–.A29 / AT-C §105.A57–.A66 documentation-sufficiency rule; AU-C §220 / AR-C §60.31 three-sign-off supervisory pattern; AU-C §230.16 retention floor); 7 references files (pbc-list, tickmark-legend, lead-sheet, indexing-convention, audit-variant, review-variant, compilation-variant); evals/compliance/workpaper-templates.json (3 cases — audit PBC manufacturing first-year, SSARS 90 review SaaS, AR-C 80.27 lack-of-independence compilation construction); skills/cpa-pack-index/SKILL.md new main routing-table row + metamorphic-routing sub-table workpaper verb routes to workpaper-templates (no longer placeholder); shared/follow-up-routing.md workpaper-gap section retired and replaced with Phase 10b "landed" summary; .claude-plugin/plugin.json 45→46 skills, version 0.3.0; .claude-plugin/marketplace.json tags add workpapers/documentation; README.md new Phase 10b row group; CHANGELOG.md v0.3.0-beta entry covering 10a + 10b; scripts/validate.sh run_phase_10b + dispatch case 10b. Validation green: validate.sh phase 10b pass=8 fail=0; validate.sh full pass=9 fail=0 (8 pre-existing authority_type warnings unrelated); run-evals.sh full pass=46 fail=0. Branch: phase-10b-workpaper-templates.

2026-05-05 | phase 10a complete | items: shared/follow-up-routing.md (prompt block + 6 destination rows + open-point stand-alone format + workpaper-gap pointer to Phase 10b); shared/compliance.md "Follow-up routing (after the verification checklist)" section; docs/skill-template.md verification-checklist appendix extended; skills/cpa-pack-index/SKILL.md "Metamorphic routing" sub-table (memo / open-point / plan / workpaper / resolution / return) + own-appendix follow-up reference; all 44 specialist SKILL.md verification-checklist appendices appended via scripts/append_followup_routing.py (idempotent); scripts/validate.sh check_followup_routing + run_phase_10a + dispatch case "10a"; BUILD_PLAN.md Phase 10a section; SKIP_URL_CHECK=1 ./scripts/validate.sh phase 10a green (pass=6 fail=0 warn=0); validate.sh full green (pass=9 fail=0 warn=8 pre-existing authority_type drift from Phase 8); run-evals.sh full unchanged (pass=45 fail=0). Sidecar schema untouched. Workpaper destination is a placeholder pending Phase 10b.

2026-05-04 | phase 9 complete | items: 9a schema additions (authority_domain field; new authority_type enum AICPA_*/FASB_*/EITF/StateBoardRule; new weight enum binding_on_member/gaap_codified/etc.; sibling verification checklists); 9a shared/ scaffolding (sources.json aicpa_professional_standards/fasb_gaap/state_boards_of_accountancy/external_pointers_out_of_scope/ftc_safeguards_rule blocks; live-sources.md sections; citation-discipline.md domain-aware mapping; authority-hierarchy.md professional-standards + GAAP subsections; compliance.md AICPA Code + engagement-letter + GAAP modules); 9b 8 new skills (compliance-aicpa-code, compliance-ssars, compliance-sas-audit, compliance-attestation-qm, engagement-letter-library w/13 letter templates, research-financial-reporting, research-asc-740, research-asc-606-842) each with SKILL.md + references/ + 3 eval cases; 9c cpa-pack-index dispatcher 8 new routes; plugin.json bumped to v0.2.0 with 45 skills; marketplace.json tags expanded; README Phase 9 row groups; CHANGELOG v0.2.0-beta entry; 9d validation green (validate.sh phase 9 + full both pass=8 fail=0; run-evals.sh full pass=45 fail=0). Branch: build. Last commit: d5c5aee.

2026-04-27 | phase 2 complete | items: predict-hobby-loss + reasonable-comp evals; +9 prediction skills (real-estate-pro, material-participation, qbi-eligibility, 1031-qualification, economic-substance, debt-vs-equity, innocent-spouse, reasonable-cause, r-and-d-credit); +4 research skills (entity, payroll, international, procedure); return-summary-entity; notice-response. Validate phase 2 + run-evals phase 2 both green (4 pass / 0 fail; 20 eval files pass). Branch: build. Last commit before plan-tick: 98f591c.

2026-04-27 | phase 3 complete | items: 3a planning skills (1040, entity, multi-year); 3b state shells + estate-gift; 3c utilities (irc-section-lookup w/Public-Law-to-USC workflow, treas-reg-lookup, form-line-explainer, due-date-calculator, penalty-interest-calc); 3d compliance-ssts-circular230; 3e+3f 102 state stubs auto-generated via scripts/generate_state_stubs.py with status:stub frontmatter and primary agency URL pre-filled from shared/sources.json; 3g state router protocol implemented in both state SKILL.md files. Validate phase 3 + run-evals full both green (5 pass / 0 fail; 32+ eval files pass). Branch: build.

2026-04-27 | phase 4 complete | items: shared/strategy-list.md (canonical 30-strategy index); planning-strategy-library SKILL.md + index.md + 30 strategy reference files generated via scripts/generate_strategies.py; 3 eval cases (QSBS lookup, multi-state PTET, decline micro-captive). Validate phase 4: 3 pass / 0 fail.

2026-04-27 | phase 5 complete | items: 7 example dirs (research-federal, predict-worker-classification, return-summary-1040, notice-response, state-research-CA, state-research-NY-convenience-rule, legislation-tracking-OBBBA); 5 docs (install-claude-ai, install-claude-code, authoring-guide, state-stub-promotion, legislation-tracking-howto); README expanded with skills index + state coverage matrix + authority discipline + compliance posture + Public-Law tracking + examples + license; CHANGELOG updated. Validate phase 5: 5 pass / 0 fail.

2026-04-27 | phase 6 complete | items: cpa-pack-index eval added (4 cases); confirmed every skill has >= 3 eval cases; state-router and legislation-tracking eval cases verified present; structural validation (validate.sh full + run-evals.sh full) all green. claude-plugin-validate and URL-liveness deferred to CI. Branch: build. Total skills: 34. Total eval files: 33 (one per skill except cpa-pack-index now 34). Total state stubs: 102. Total strategies: 30.

2026-04-27 | phase 7 PR | open PR build → main: "Phase 7 — release". STOP per CLAUDE.md - Kurt to review and tag v1.0.0-beta.
