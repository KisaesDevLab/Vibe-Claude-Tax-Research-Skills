---
name: planning-actions-1040
description: |
  Generates a prioritized list of individual-tax planning actions
  for a given facts intake — typically downstream of return-summary-
  1040. Each action item carries an estimated tax impact, an
  implementation timeline, citations, a confidence band, and a
  recommended deadline. Covers retirement contributions, Roth
  conversions, tax-loss harvesting, charitable bunching / DAFs,
  HSA / FSA optimization, AMT triggers, NIIT planning, IRMAA
  cliffs, withholding adjustments, and §1031 / §121 timing. Routes
  contested positions to research / prediction skills. Use when the
  user asks "what planning should I consider", "year-end tax
  planning", "1040 planning", "Roth conversion advice", "tax-loss
  harvesting", "charitable bunching", "HSA / FSA optimization",
  "AMT trigger", "IRMAA cliff", "estimated-tax safe harbor",
  "withholding adjustment", or "year-end checklist". Make sure to
  use this skill whenever the user mentions individual tax planning,
  year-end planning, or 1040 planning actions.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# planning-actions-1040 — Individual planning checklist

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA permanence vs sunset,
   OBBBA modifications affecting planning windows.
6. `references/checklist-categories.md` — categorized action list
   with citations and timing notes.

## Workflow

### 1. Intake

- `tax_year` (planning year)
- `filing_status` and life-event changes
- `agi_estimate` and `tax_bracket`
- `taxable_income_band`: needed for QBI / NIIT / AMT thresholds
- `retirement_account_balances` and contribution-room status
- `charitable_giving_intent` and DAF status
- `state_residency` and state SALT-cap exposure
- `medicare_status`: relevant for IRMAA cliffs
- `health_savings_account_eligibility`
- `pending_capital_gains` and harvestable losses
- `windfalls_or_one_time_events`: stock options, RSUs, M&A
  proceeds, inheritance, etc.
- `taxpayer_circuit` and `taxpayer_state` (for routing)

### 2. Categorical checklist walk

For each category in `references/checklist-categories.md`,
identify whether action is plausible given the intake. Categories:

1. Retirement contributions (Traditional / Roth IRA, 401(k),
   SEP, Solo 401(k), defined-benefit).
2. Roth conversions (timing, IRMAA cliffs, multi-year ladder).
3. Tax-loss harvesting and wash-sale (§1091) planning.
4. Charitable contributions (bunching, DAF, QCD from IRA, stock
   donation).
5. HSA / FSA optimization (§§223 / 125 / 129).
6. AMT triggers (large §164 deduction states, ISOs, accelerated
   depreciation).
7. NIIT planning (§1411 — material participation, capital gain
   timing).
8. IRMAA Medicare premium cliffs.
9. Withholding adjustment (Form W-4) and estimated-tax safe
   harbors (§6654).
10. §121 home-sale exclusion timing.
11. §1031 like-kind exchange (route to `predict-1031-qualification`).
12. §529 / education planning.
13. Stock-option / RSU / 83(b) timing.
14. Backdoor Roth conversion (mega backdoor for 401(k) plans).
15. State-residency planning (route to `tax-research-state-income`).
16. PTET election (route to `tax-research-state-income`).
17. Estate / gift annual exclusion (route to
    `tax-research-estate-gift`).

### 3. Prioritization

Score each action by:
- Tax impact (dollars).
- Implementation cost (time, fees, complexity).
- Risk (audit / contested-position exposure).
- Time-sensitivity (year-end vs. multi-year).

Output a top-N list with rationale.

### 4. Routing

For any action requiring substantive analysis beyond the planning
checklist, route to:
- `tax-research-federal` — federal-tax interpretive questions.
- `tax-research-state-income` — state-tax planning.
- `predict-qbi-eligibility` — §199A planning.
- `predict-real-estate-pro` / `predict-material-participation` —
  rental-loss strategy.
- `predict-1031-qualification` — like-kind exchange decision.
- `predict-economic-substance` — aggressive-strategy validation.
- `tax-research-procedure` — installment-agreement / safe-harbor
  procedural advice.

### 5. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`. The
`conclusion` is a prioritized action list. Each action should
have a `confidence_band` reflecting the certainty of the tax
benefit. For aggressive strategies, route to research / prediction
skills before recommending.

## Hard rules

- Never recommend a SPECULATIVE-band strategy.
- Always note disclosure obligations (Form 8275 / 8275-R / 8886)
  for non-routine actions.
- Always cite year-specific Rev. Proc. or §1(f)(3) inflation-
  adjustment for thresholds; do NOT quote a threshold without
  retrieval.
- Drop one band when relying on a §831(b) micro-captive,
  syndicated conservation easement, or other Dirty-Dozen /
  Listed Transaction strategy — these should NOT appear in the
  recommendation list at all without a Listed-Transaction warning
  banner.
- Drop one band when state-tax planning relies solely on a
  `status: stub` per-state file.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. Note disclosure obligations for any
non-routine recommended action.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
