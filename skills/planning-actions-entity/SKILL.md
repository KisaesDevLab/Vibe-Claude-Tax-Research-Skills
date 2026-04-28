---
name: planning-actions-entity
description: |
  Generates a prioritized list of entity-tax planning actions for
  C-corp / S-corp / partnership / LLC clients — typically downstream
  of return-summary-entity. Each action carries an estimated tax
  impact, implementation timeline, citations, a confidence band, and
  recommended deadline. Covers entity-level retirement plans,
  reasonable-comp optimization, §199A planning, §163(j) management,
  PTET elections, depreciation acceleration / §179 / §168(k), §382
  NOL planning, §1202 QSBS, and accountable-plan implementation.
  Use when the user asks "entity planning", "C-corp planning",
  "S-corp planning", "partnership planning", "PTET strategy",
  "QSBS §1202", "§179 / §168(k) bonus depreciation", "accountable
  plan", "§163(j) management", or "year-end entity planning". Make
  sure to use this skill whenever the user mentions entity tax
  planning, C-corp planning, S-corp planning, partnership planning,
  or PTET.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# planning-actions-entity — Entity planning checklist

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA / IRA / OBBBA effects
   on §163(j), §168(k), §174, §59 / §59A, §250.
6. `references/entity-checklist-categories.md` — categorized action
   list with citations and timing notes.

## Workflow

### 1. Intake

- `entity_type`: C-corp, S-corp, partnership, LLC (single- or
  multi-member)
- `tax_year` (planning year)
- `revenue_band`: drives §163(j) small-taxpayer exception, §59A
  BEAT, §55 corporate AMT, R&D-related interactions
- `industry`: relevant for SSTB classification, manufacturing
  bonus depreciation, R&D
- `owner_facts`: number of owners, family-attribution status,
  reasonable-comp posture
- `state_footprint`: PTET eligibility, multi-state nexus
- `pending_transactions`: M&A, capital expenditures, formation /
  liquidation events

### 2. Categorical checklist walk

For each category in `references/entity-checklist-categories.md`:

#### Entity-level retirement plans

- 401(k) with employer match + profit-sharing.
- Cash-balance / defined-benefit plan for high earners.
- SIMPLE IRA / SEP-IRA for small employers.

#### Reasonable comp (S-corp specifically)

Route to `predict-reasonable-comp` for substantive analysis.

#### §199A planning

Route to `predict-qbi-eligibility` for substantive analysis.

#### §163(j) management

- Small-taxpayer exception (§163(j)(3)): 3-year average gross
  receipts < $30M (verify year-specific) — exempts from §163(j).
- Election to be excepted real-property trade or business
  (§163(j)(7)(B)).
- ATI computation under post-2022 EBIT-basis rules.
- EBIE allocation at partnership level.

#### Depreciation: §179 / §168(k)

- §179: $1.16M expensing 2024 (verify year-specific Rev. Proc.);
  $2.89M phase-out threshold.
- §168(k) bonus depreciation: 60% for property placed in service
  in 2024; 40% for 2025; 20% for 2026; 0% for 2027 and later
  (TCJA phase-out — verify OBBBA modifications).
- Cost-segregation study to accelerate.
- §263A UNICAP / capitalization analysis.

#### State PTET elections

Route to `tax-research-state-income` per-state file. Many states:
- NY (TR 2021-103 / etc.).
- CA (FTB Form 3804).
- NJ (BAIT).
- IL.
- CT (PE Tax).
- 30+ states have enacted PTET.

#### §1202 Qualified Small Business Stock

§1202 — exclusion of up to 100% of gain on sale of QSBS held > 5
years. Eligibility:
- Domestic C-corp.
- Aggregate gross assets ≤ $50M (adjusted) at issuance.
- Active business (not personal-service business).

OBBBA modifications to §1202 thresholds — verify current.

§1045 rollover — defer §1202 gain by purchasing replacement QSBS.

#### Accountable plan (§62(c))

Required to make employee reimbursements pre-tax. Three
conditions:
1. Business connection.
2. Substantiation within reasonable time.
3. Return of excess within reasonable time.

#### Deferred compensation (§409A)

§409A non-qualified deferred-compensation rules. Severe penalty
(20% additional tax + premium-interest) for failures.

Document plan in writing; comply with timing-of-deferral and
distribution-trigger requirements.

#### M&A planning

- §351 / §368 / §332 reorganization analysis.
- §338(h)(10) joint-election for asset-deal treatment.
- §382 NOL limitation post-acquisition.

Route to `tax-research-entity` for substantive M&A analysis.

#### §174 R&E capitalization

Post-TCJA: 5-year domestic / 15-year foreign amortization.
OBBBA modifications — verify.

§280C(c) reduced credit election to coordinate with §41 R&D
credit.

Route to `predict-r-and-d-credit` for §41 substantive analysis.

#### Worker classification

Route to `predict-worker-classification` for substantive analysis.

#### Notice / audit response

Route to `notice-response` for IRS-notice triage.

### 3. Prioritization

Score each action by:
- Tax impact (dollars).
- Complexity / cost.
- Risk (audit / contested-position exposure).
- Time-sensitivity.

### 4. Routing

For substantive analysis, route to:
- `tax-research-entity` — substantive entity questions.
- `tax-research-state-income` — state planning.
- `tax-research-international` — cross-border planning.
- `predict-reasonable-comp` / `predict-qbi-eligibility` /
  `predict-r-and-d-credit` / `predict-worker-classification` /
  `predict-economic-substance` — prediction skills.
- `predict-1031-qualification` — like-kind exchange.

### 5. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`. The
`conclusion` is a prioritized action list. Each action with
estimated impact, deadline, and confidence band.

## Hard rules

- Never recommend a SPECULATIVE-band strategy.
- Never recommend §831(b) micro-captive, syndicated conservation
  easement, or other Listed Transaction without a Form 8886
  warning banner.
- Always cite year-specific Rev. Proc. or §1(f)(3) inflation-
  adjustment for thresholds; do NOT quote a threshold without
  retrieval.
- Drop one band when state-tax planning relies solely on a
  `status: stub` per-state file.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note disclosure obligations for any
non-routine recommended action.
