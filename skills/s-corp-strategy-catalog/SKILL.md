---
name: s-corp-strategy-catalog
description: |
  Catalog of ten high-leverage S corporation tax strategies mapped
  to specific lines on Form 1120-S and the shareholder K-1. Covers
  reasonable compensation, ≥2% shareholder health insurance,
  hire-your-child, sell-home-before-rental-conversion, accountable-
  plan home office, Augusta Rule (§280A(g)) home rental, depreciation
  reimbursement, vehicle reimbursement, travel reimbursement, and
  cell-phone working-condition fringe. Each catalog entry routes to
  the underlying detail strategy file. Use when the user asks
  "S corp tax strategies", "Form 1120-S strategies", "S corp owner
  tax planning", "reasonable comp for owner", "Augusta Rule",
  "accountable plan home office", "Section 179 vehicle reimbursement",
  "S corp shareholder health insurance", "S corp hire kids", or
  about any specific 1120-S line. Make sure to use this skill
  whenever the user mentions S corporation owner-level tax planning,
  the Form 1120-S, or accountable-plan reimbursement to a 2%+
  shareholder-employee.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# s-corp-strategy-catalog — 10 S corporation strategies, mapped to Form 1120-S

Catalog skill that turns natural-language S-corp planning questions
into a Form 1120-S line-mapped strategy answer with citations and
links to the underlying detail strategy files.

## Read before output

Before producing any output, read in order:

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — when an OBBBA-affected provision
   is implicated (§174 R&E, §163(j), §168(k), §179 limits).
6. `references/strategy-table.md` — the Form 1120-S line map.
7. The relevant
   `skills/planning-strategy-library/references/strategies/<slug>.md`
   for the strategy under analysis.

## Form 1120-S line map (ten strategies)

| # | Strategy | 1120-S line | Detail file (planning-strategy-library) |
|---|---|---|---|
| 1 | Reduce owner W-2 wages | Line 7 (Compensation of officers) | `reasonable-comp-corp-owners.md` (and existing `s-corp-reasonable-comp.md`) |
| 2 | ≥2% shareholder health insurance | Line 7 | `health-insurance-s-corp.md` |
| 3 | Employ your child | Line 8 (Salaries and wages) | `hiring-kids.md` |
| 4 | Sell home to S corp before rental conversion | Line 14 (Depreciation) | `primary-home-sale-exclusion.md` (§121) + `cost-segregation.md` |
| 5 | Accountable-plan home office reimbursement | Line 19 (Other deductions) | `s-corp-home-office-reimbursement.md` |
| 6 | Augusta Rule (§280A(g)) home rental | Line 11 (Rents) | `augusta-rule-280a-g.md` |
| 7 | Depreciation reimbursement (PLR 200930029) | Line 19 | `corp-vehicle-personal-name.md` |
| 8 | Vehicle reimbursement | Line 19 | `corp-vehicle-personal-name.md` |
| 9 | Travel reimbursement | Line 19 | `reimbursement-business-expenses.md` |
| 10 | Cell-phone working-condition fringe | Line 18 (Employee benefit programs) | (Notice 2011-72; see catalog table) |

Strategies #5, #7, #8, #9 share the **accountable plan**
(Treas. Reg. §1.62-2) as their operational backbone.

## Workflow

### 1. Intake

- `tax_year`
- `entity`: confirm S corp election in effect (Form 2553 filed; QSST/
  ESBT for trust shareholders).
- `owner_facts`: %-ownership, W-2 wages currently paid, distributions,
  taxpayer's circuit (for *Watson*-style reasonable-comp Golsen
  weighting), state.
- `strategy_query`: by strategy name, 1120-S line number, or topic
  ("how do I reimburse home office", "Augusta Rule").

### 2. Strategy lookup

Match the query to the catalog row in `references/strategy-table.md`.
Load the linked detail file from `planning-strategy-library`. If the
query maps to multiple strategies (e.g., "reimbursement"), surface
all candidates and ask the user to refine, OR walk each in turn.

### 3. Eligibility analysis

For each candidate strategy, check the entity-type and ownership
preconditions documented in the detail file. Flag any disqualifying
fact (e.g., FICA exemption under §3121(b)(3)(A) does NOT apply when
the parent's entity is an S corporation — only Schedule C / parent-
only partnerships qualify).

### 4. Mechanics walk

Walk the detail file's mechanics: deadlines, documentation,
substantiation, accountable-plan resolution language. For
accountable-plan strategies, confirm the three-prong test
(business connection, substantiation, return of excess) under
Treas. Reg. §1.62-2(c).

### 5. 1120-S line placement

State the specific Form 1120-S line where the deduction lands and
any K-1 box affected (Box 1 ordinary income, Box 16 distributions,
Box 17 §199A items).

### 6. Reasonable-comp interaction (every strategy)

Reducing officer W-2 wages (#1) interacts with every other strategy
on this catalog because it changes the §199A wage limit, the
§3121 / §3306 wage base, and the Box 14 reporting. Always run the
*Watson* / *Sean McAlary* / *Sinopoli* substance check — see
`reasonable-comp-corp-owners.md`. For high-stakes engagements,
route to `predict-reasonable-comp`.

### 7. State conformity

Note state non-conformity that materially affects the strategy:

- California — no §168(k) bonus; §179 capped at $25,000.
- New York — selective conformity; no state §199A.
- Pennsylvania — no §168(k) bonus.
- Texas — franchise tax: §179 in COGS allowed; bonus disallowed in
  COGS.
- New Hampshire — BPT applies to S corps.
- Tennessee — Excise & Franchise tax on net earnings.

Route to `tax-research-state-income` for the per-state file.

### 8. Recent legislation (OBBBA)

OBBBA-affected items in this catalog:

- §168(k) bonus permanence and 100% reinstatement for property
  acquired after 1/19/2025 (verify against Classification Tables —
  see `shared/legislation-tracking.md`).
- §179 limit and SUV cap for 2025/2026.
- §163(j) modifications.
- §174 R&E (interaction with #9 travel/training reimbursements only
  in narrow cases).

Always verify current-year figures via the Classification Tables
workflow before quoting them as fact.

### 9. Conclusion + JSON sidecar

Emit a markdown conclusion with the strategy name, 1120-S line
placement, eligibility result, and confidence band. Follow with a
JSON sidecar validating against `shared/output-schema.json`.
`authorities[]` must use the project's enumerated `authority_type`
values (no `non_precedential_irs`, no `PublicLaw` — use
`written_determinations` for PLRs and `StatutesAtLarge` for OBBBA
public-law citations).

For OBBBA-implicated analyses, populate `public_laws_consulted[]`
with `Pub. L. 119-21` and the affected IRC sections per
`shared/legislation-tracking.md`.

## Hard rules

- This skill catalogs and routes; it does NOT replace the detail
  strategy files. Always load and cite the underlying
  `planning-strategy-library/references/strategies/<slug>.md`.
- Never set reasonable comp without running the
  *Watson*/*McAlary*/*Sinopoli* substance check; route to
  `predict-reasonable-comp` for any aggressive position.
- Never claim Chevron deference for Treas. Reg. §1.62-2 (or any
  reg) — Loper Bright posture requires Skidmore framing.
- Augusta Rule (#6) is absolute on the 14-day limit; the 15th day
  disqualifies the *entire* exclusion. Cite *Sinopoli* for the
  rate-and-purpose substance check.
- Hire-your-child (#3) under an S corp does NOT get §3121(b)(3)(A)
  FICA exemption — that is sole-prop / parent-only-partnership
  only. Do not surface the exemption in S-corp answers.
- For any §1239 / §121 home-sale-to-corp position (#4), allocate
  between land and structure; only the structure-allocable gain
  is at §1239 risk.
- PLR 200930029 (#7) has no precedential value to other
  taxpayers under §6110(k)(3) — cite as
  `weight: written_determinations`, not as binding authority.
- Inflation-indexed amounts (§179 limits, SS wage base, QBI
  thresholds, standard deduction) MUST be the year-appropriate
  figure. Verify before quoting.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md` (SSTS §1.1, §2.3; Circular 230 §10.22,
§10.35, §10.37; negative-treatment review residual responsibility
for any cited case law).

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
