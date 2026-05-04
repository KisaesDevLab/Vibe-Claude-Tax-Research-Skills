# Changelog

All notable changes documented here. Format follows Keep a Changelog;
versions follow SemVer.

## [v1.0.0-beta] — 2026-04-27 (target)

### Phase 0 — bootstrap

- shared/ files: citation-discipline.md, authority-hierarchy.md,
  confidence-bands.md, compliance.md, legislation-tracking.md,
  live-sources.md, sources.json, output-schema.json,
  state-template.md.
- docs/skill-template.md.
- scripts/validate.sh, scripts/run-evals.sh, scripts/generate_state_stubs.py,
  scripts/generate_strategies.py.
- CI workflow at .github/workflows/validate.yml.
- .claude-plugin/plugin.json + marketplace.json skeletons.

### Phase 1 — flagships + dispatcher

- skills/cpa-pack-index (always-on dispatcher).
- skills/tax-research-federal (federal research flagship).
- skills/predict-worker-classification (prediction flagship).
- skills/return-summary-1040 (return summary flagship).
- evals/research/tax-research-federal.json (3 cases).
- evals/prediction/predict-worker-classification.json (3 cases).
- evals/summary/return-summary-1040.json (3 cases).

### Phase 2 — prediction + research + summary + notice

Prediction skills (11; worker-class was Phase 1):
- predict-hobby-loss, predict-reasonable-comp,
  predict-real-estate-pro, predict-material-participation,
  predict-qbi-eligibility, predict-1031-qualification,
  predict-economic-substance, predict-debt-vs-equity,
  predict-innocent-spouse, predict-reasonable-cause,
  predict-r-and-d-credit.

Research skills (4 federal; federal was Phase 1):
- tax-research-entity, tax-research-payroll,
  tax-research-international, tax-research-procedure.

Summary + notice:
- return-summary-entity, notice-response.

3 eval cases per skill.

### Phase 3 — planning + state shells + utilities + compliance

- 3a. Planning: planning-actions-1040, planning-actions-entity,
  planning-multi-year (legislation-tracking-pointer reference).
- 3b. State shells + estate-gift: tax-research-state-income,
  tax-research-state-salesuse, tax-research-estate-gift.
- 3c. Utilities (5): irc-section-lookup (Public-Law-to-USC
  workflow + subtitle-map references), treas-reg-lookup
  (treasury-decisions reference), form-line-explainer,
  due-date-calculator, penalty-interest-calc.
- 3d. Compliance: compliance-ssts-circular230 (irs-guidance-primer
  reference).
- 3e/3f. 102 state stubs auto-generated from sources.json (51
  per state research skill); status:stub frontmatter; primary
  agency URL pre-filled.
- 3g. State router protocol implemented in both state SKILL.md
  files.

3 eval cases per skill.

### Phase 4 — strategy library

- skills/planning-strategy-library/SKILL.md.
- shared/strategy-list.md (canonical 30-strategy index).
- 30 strategy reference files at
  skills/planning-strategy-library/references/strategies/<slug>.md.
- index.md cross-referencing all 30.
- scripts/generate_strategies.py (idempotent generator).

3 eval cases.

### Phase 5 — examples, docs, README, marketplace

- 7 example dirs:
  research-federal, predict-worker-classification,
  return-summary-1040, notice-response, state-research-CA,
  state-research-NY-convenience-rule, legislation-tracking-OBBBA.
- docs/install-claude-ai.md, install-claude-code.md,
  authoring-guide.md, state-stub-promotion.md,
  legislation-tracking-howto.md.
- README.md expanded with skills index, state-coverage matrix,
  authority discipline, compliance posture, Public-Law tracking,
  examples, validation, license, disclaimer, contributing.
- .claude-plugin/plugin.json + marketplace.json finalized with
  full skills list.

### Phase 6 — eval expansion + QA

- ≥ 3 eval cases per skill (33 skills × 3 = 99+ cases).
- State-router eval cases.
- Legislation-tracking eval case (OBBBA).
- Validate full + run-evals full both green.

### Phase 7 — release

- PR build → main with title "Phase 7 — release" awaiting Kurt's
  review and tag-creation approval.

## [v0.2.0-beta] — Phase 9 — 2026-05-04

AICPA professional standards + engagement letters + GAAP research.
Triggered by user request to expand the pack beyond tax-only into
the broader AICPA practice scope.

### Phase 9 — Schema additions (additive, backward-compatible)

- `shared/output-schema.json`: new `authority_domain` field
  (tax_position default | professional_conduct | gaap); extended
  `authority_type` enum with AICPA_Code / AICPA_SSARS / AICPA_SAS /
  AICPA_SSAE / AICPA_SQMS / AICPA_PracticeAid / AICPA_TPA /
  FASB_ASC / FASB_ASU / FASB_Concepts / EITF / StateBoardRule;
  extended `weight` enum with binding_on_member / interpretive /
  practice_aid / gaap_codified /
  gaap_pre_codification_grandfathered / gaap_non_authoritative;
  sibling optional verification checklists
  (verification_checklist_aicpa_code,
  verification_checklist_engagement,
  verification_checklist_gaap); state_overlay_required and
  legal_review_required flags.
- All existing skills' outputs continue to validate without
  modification.

### Phase 9 — Shared / live sources

- `shared/sources.json`: aicpa_professional_standards (Code, SSARS,
  SAS, SSAE, SQMS, practice aids, technical Q&A); fasb_gaap (FASB
  home, ASC Basic View, ASU index, Concepts Statements, EITF
  abstracts); state_boards_of_accountancy (NASBA + 55
  jurisdictions: 50 states + DC + GU + PR + VI + MP);
  external_pointers_out_of_scope (PCAOB, GASB, IFRS, GAO);
  ftc_safeguards_rule.
- `shared/live-sources.md`: corresponding human-readable sections.
- `shared/citation-discipline.md`: domain-aware authority-type-to-
  weight mapping; cross-domain citation guidance; no Chevron
  analog for AICPA / FASB.
- `shared/authority-hierarchy.md`: new "Professional standards"
  and "GAAP authority" subsections with separate ladders.
- `shared/compliance.md`: AICPA Code module + engagement-letter
  required-elements module + GAAP research scaffolding.

### Phase 9 — New skills (8)

Compliance / professional standards (4):
- `compliance-aicpa-code` — AICPA Code of Professional Conduct
  (ET §1.000+); threats-and-safeguards independence framework;
  §1.295 nonattest; state-board overlay (CA, NY, TX known
  stricter).
- `compliance-ssars` — SSARS / AR-C 60 (general) + 70
  (preparation) + 80 (compilation) + 90 (review); lack-of-
  independence handling for AR-C 80.27.
- `compliance-sas-audit` — SAS / AU-C clarified audit standards
  (200/210/220/230/240/315/330/540/570/600/700-series) for
  nonissuer audits. PCAOB AS routed externally.
- `compliance-attestation-qm` — AT-C 105/205/215/320 attestation
  + SOC 1/2/3 + SQMS 1 firm QM + SQMS 2 engagement quality
  reviews.

Engagement letters (1):
- `engagement-letter-library` — Engagement-letter framework +
  fillable templates for 13 engagement types (audit, review,
  compilation, preparation, tax-1040, tax-business, tax-advisory,
  bookkeeping, payroll, consulting, SOC 1, SOC 2, AUP). FTC
  Safeguards Rule clause for tax engagements. Indemnification
  state overlay (CA Bus. & Prof. Code §5063.1, IL, NJ for
  attest). AICPA Ethics Interpretation §1.400.205 attest-
  indemnification limitation.

GAAP / FASB ASC research (3):
- `research-financial-reporting` — General FASB ASC research;
  routes by Topic family; ASC 105-10 hierarchy; ASU effective-
  date workflow. Routes other ASC topics here.
- `research-asc-740` — ASC 740 income tax accounting; ASC
  740-10-25 two-step UTP recognition + measurement (FIN 48);
  cross-references tax-research-federal for substantial-
  authority analysis underlying UTP; valuation allowances; DTA /
  DTL; intraperiod allocation; ASU 2023-09 disclosures.
- `research-asc-606-842` — ASC 606 revenue recognition (five-step
  model; variable consideration; principal vs agent; license
  revenue) + ASC 842 leases (lessee classification; ROU asset;
  sale-leaseback).

Total skills: 37 → 45.

### Phase 9 — Dispatcher / plugin / docs

- `skills/cpa-pack-index/SKILL.md`: 8 new dispatcher routes.
- `.claude-plugin/plugin.json`: 8 new skill paths + version 0.2.0.
- `.claude-plugin/marketplace.json`: extended tags (aicpa, attest,
  audit, ssars, engagement-letters, professional-standards, gaap,
  asc).
- `README.md`: Phase 9 row groups in skills index + 5 new
  compliance / engagement / GAAP categories.

### Phase 9 — Eval coverage

- 8 new eval files (3 cases each) under
  `evals/compliance/`, `evals/planning/`, `evals/research/`.
- The existing `evals/research/compliance-ssts-circular230.json`
  is grandfathered in place to avoid CI noise.

### Phase 9 — Out of scope (deferred to Phase 10 / future)

- PCAOB AS standards (issuer audits) — single external pointer
  in `compliance-sas-audit`.
- GASB / state-and-local government GAAP — pointer in
  `research-financial-reporting`.
- IFRS — pointer in `research-financial-reporting`.
- Yellow Book / GAGAS / Single Audit — pointer in
  `compliance-sas-audit`.
- Peer review program operations.
- State CPA licensure / CPE tracking.
- `research-asc-326` (CECL — community-bank/credit-union niche).

## [v1.0.0] — TBD

To be released after Phase 7 PR merge and Kurt-created tag.
