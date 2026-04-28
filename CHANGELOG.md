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

## [v1.0.0] — TBD

To be released after Phase 7 PR merge and Kurt-created tag.
