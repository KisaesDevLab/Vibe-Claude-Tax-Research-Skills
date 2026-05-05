---
name: planning-multi-year
description: |
  Generates a multi-year tax projection and action plan, accounting
  for sunset / phase-out / phase-in provisions of recent legislation
  (TCJA, IRA, SECURE 2.0, OBBBA, and any subsequent reconciliation
  bill). Tracks legislative-effective-date sensitivity for §168(k),
  §174, §163(j), §199A sunset, §1202 thresholds, §40A / §45 / §48
  green-energy credits, §401(a)(9) RMD age progression, IRMAA
  thresholds, and AMT exemption phase-outs. Reads
  shared/legislation-tracking.md for any Public-Law-driven planning
  question. Use when the user asks "multi-year planning",
  "TCJA sunset", "§199A sunset", "§168(k) phase-down", "§174 R&E
  amortization", "OBBBA changes", "Inflation Reduction Act
  credits", "SECURE 2.0", or "post-2025 planning". Make sure to use
  this skill whenever the user mentions multi-year planning,
  legislative sunsets, OBBBA, TCJA expiration, or post-2025
  positioning.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# planning-multi-year — Sunset / phase-out planning

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — Public-Law-to-USC workflow
   for resolving recent legislation impact.
6. `references/legislation-tracking-pointer.md` — cross-reference
   to shared/legislation-tracking.md for reconciliation-bill
   scoring context (per BUILD_PLAN).
7. `references/sunset-and-phaseout-calendar.md` — calendar of
   provisions sunsetting / phasing out / phasing in.

## Workflow

### 1. Intake

- `planning_horizon`: 3-year, 5-year, 10-year
- `taxpayer_facts`: similar to `planning-actions-1040` /
  `planning-actions-entity` but with multi-year projections of
  income, deductions, life events
- `pending_legislation_status`: which bills user wants modeled
  (e.g., "OBBBA-as-enacted", "post-2025-TCJA-sunset",
  "Pillar 2 GloBE", etc.)

### 2. Sunset / phase-out / phase-in identification

Use `shared/legislation-tracking.md` workflow to identify Public
Laws affecting the planning horizon. Common sunsets / phase-outs:

- **TCJA individual provisions**: §199A (20% QBI), individual rate
  brackets, individual standard deduction, §164 SALT cap, §163
  HELOC interest deduction — most expire 12/31/2025 absent
  legislative extension. OBBBA (Pub. L. 119-XX, 2025) extended /
  modified — verify per Classification Tables.
- **§168(k) bonus depreciation**: 60% (2024), 40% (2025), 20%
  (2026), 0% (2027). OBBBA may have modified — verify.
- **§174 R&E**: 5-year domestic / 15-year foreign amortization;
  OBBBA may have reverted to immediate expensing for domestic —
  verify.
- **§163(j)**: ATI definition switched from EBITDA to EBIT in
  2022. OBBBA may have reversed — verify.
- **SECURE 2.0**: §401(a)(9) RMD age 73 in 2023, 75 in 2033;
  catch-up index changes; Roth catch-up for high earners 2025
  delayed to 2026 (Notice 2023-62).
- **§55 corporate AMT (IRA 2022)**: applies to applicable
  corporations (3-year average AFSI > $1B) starting tax years
  beginning after 12/31/2022.
- **§4501 stock-buyback excise (IRA 2022)**: 1% on net buybacks.
- **§250 FDII**: 37.5% deduction → 21.875% post-2025 absent
  extension (verify OBBBA).
- **§250 GILTI deduction**: 50% → 37.5% post-2025 absent
  extension (verify OBBBA).
- **§59A BEAT**: 10% → 12.5% post-2025 absent extension (verify
  OBBBA).
- **§30D / §45W / §48 / §45 IRA green-energy credits**: various
  scheduled phase-outs and cliff dates.
- **§121 / §1031 / §401(k) / §223**: typically not legislatively-
  date-sensitive within a 5-10 year horizon but verify.

### 3. Multi-year projection

For each year in the planning horizon:
- Apply current-law marginal rates (post-OBBBA where applicable).
- Apply phase-down / phase-in adjustments per the calendar.
- Compute approximate tax liability.
- Identify cash-flow inflection points (e.g., RMDs starting,
  Medicare onset, sunset of QBI deduction).

### 4. Strategy formulation

For each material sunset / phase-out, recommend:
- **Pre-sunset acceleration**: take action while provision is
  available (e.g., Roth conversions before TCJA brackets sunset).
- **Post-sunset positioning**: structure to benefit from new
  regime (e.g., higher §164 SALT cap, lower QBI advantage,
  changed §1202 thresholds).
- **Ladder strategies**: spread Roth conversions, capital-gain
  recognitions across years to manage marginal rates.
- **Legislative-uncertainty hedging**: avoid irreversible
  commitments tied to expected-but-not-yet-enacted provisions.

### 5. Routing

Route to:
- `tax-research-federal` — interpretive questions on enacted
  provisions.
- `irc-section-lookup` — Public-Law-to-USC resolution for any
  popular-name legislation referenced.
- `tax-research-state-income` — state-conformity sunset
  alignment.
- `predict-economic-substance` — for any aggressive multi-year
  structure that may invite §7701(o) scrutiny.
- `planning-actions-1040` / `planning-actions-entity` — annual
  action lists.
- `tax-research-estate-gift` — estate-tax exclusion sunset
  planning.

### 6. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
Populate `public_laws_consulted[]` with Public Laws material to
the projection (TCJA, IRA, SECURE 2.0, OBBBA, etc.).

`confidence_band` reflects:
- HIGH for projections based on enacted law with no near-term
  modification.
- MODERATE for projections relying on TCJA-permanence /
  OBBBA-permanence assumptions.
- LOW for projections relying on pending reconciliation bills.
- SPECULATIVE for projections relying on hypothetical legislation.

## Hard rules

- Always identify the specific Public Law and its effective dates
  via `shared/legislation-tracking.md`.
- Always verify OBBBA modifications via the Classification Tables
  before quoting current-law thresholds.
- Always note legislative uncertainty in any projection beyond 24
  months.
- Drop one band when relying on a pending bill that has not been
  enacted.
- Greenbook proposals do NOT count as enacted law; tag
  `Greenbook` / `persuasive_non_authority` for descriptive use
  only.
- CBO scoring of pending bills is NOT interpretive authority; tag
  `CBOReport` / `persuasive_non_authority` for projected-revenue
  context.
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
