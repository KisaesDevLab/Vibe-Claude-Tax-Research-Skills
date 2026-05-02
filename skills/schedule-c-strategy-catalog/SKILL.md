---
name: schedule-c-strategy-catalog
description: |
  Catalog of ten high-leverage tax strategies for Schedule C sole
  proprietors and single-member LLCs (default tax treatment),
  mapped to specific lines on Schedule C and Form 8829. Covers
  §105 HRA spouse-employee plan, hire-your-child §3121(b)(3)(A)
  FICA exemption, employ-your-spouse, rent-from-spouse SE
  avoidance under §1402(a)(1), home office post-1999 §280A(c)(1),
  §132(e) de minimis fringe, heavy-vehicle + home-office combo,
  domestic-travel majority-of-days rule, §274(c) seven-day / 25%
  foreign-travel rule, and cell-phone working-condition fringe.
  Use when the user asks "Schedule C strategies", "sole prop",
  "SMLLC", "Form 8829", "§105 HRA", "hire-your-child sole prop",
  "rent from spouse", "heavy vehicle Schedule C", or about any
  Schedule C line. Make sure to use whenever the user mentions
  sole proprietorship, Schedule C, single-member LLC, or Form 8829
  home office in a planning context.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# schedule-c-strategy-catalog — 10 Schedule C / SE strategies, mapped to Schedule C lines

Catalog skill that turns natural-language sole-prop / SMLLC planning
questions into a Schedule C / Form 8829 line-mapped strategy answer
with citations and links to the underlying detail strategy files.

## Read before output

Before producing any output, read in order:

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — when an OBBBA-affected
   provision is implicated (§168(k), §179 limits, standard
   deduction figures).
6. `references/strategy-table.md` — the Schedule C line map.
7. The relevant
   `skills/planning-strategy-library/references/strategies/<slug>.md`.

## Schedule C / Form 8829 line map (ten strategies)

| # | Strategy | Schedule C line | Detail file (planning-strategy-library) |
|---|---|---|---|
| D1 | §105 HRA spouse-employee health plan | Line 14 (Employee benefit programs) | `hra-merp.md` |
| D2 | Employ your child (§3121(b)(3) FICA exempt) | Line 26 (Wages) + Line 23 (Taxes) | `hiring-kids-self-employed.md` |
| D3 | Employ your spouse (with §105 HRA combo) | Line 26 + Line 14 | `wages-spouse-parents.md` + `hra-merp.md` |
| D4 | Rent from your spouse (Schedule E avoids SE tax) | Line 20a / 20b (Rent or lease) | `split-entity-operations-vs-re.md` |
| D5 | Home office (Form 8829 / simplified) | Line 30 (via Form 8829) | `home-office-deduction-self-employed.md` |
| D6 | §132(e) de minimis fringe | Line 14 | (Reg. §1.132-6; see catalog) |
| D7 | Heavy vehicle + home office combo | Line 9 (Car and truck) | `business-vehicle-self-employed.md` |
| D8 | Domestic travel — majority-of-days rule | Line 24a (Travel) | `accountable-plan-self-employed.md` |
| D9 | Foreign travel — §274(c) seven-day / 25% rule | Line 24a | `accountable-plan-self-employed.md` |
| D10 | Cell phone — non-compensatory business reasons | Line 25 (Utilities) or Line 18 (Office expense) | (Notice 2011-72) |

## Workflow

### 1. Intake

- `tax_year`
- `entity`: sole prop / single-member LLC / parent-only partnership
  (the FICA exemption under §3121(b)(3)(A) is entity-specific).
- `filing_status` and dependents (for child-employment strategy
  and §1(g) kiddie-tax sanity check).
- `taxpayer_state` (state non-conformity flags, especially CA, NY,
  MA, NJ on bonus depreciation; AB5 ABC test for state worker
  classification).
- `strategy_query`: by name, line, or topic.

### 2. Strategy lookup

Match the query to the catalog row in `references/strategy-table.md`.
Load the linked detail file. Multiple-mapping queries surface all
candidates.

### 3. Eligibility analysis

Each strategy has entity-type preconditions. Check them first:

- D1 (§105 HRA spouse-employee): single-employee employer rule
  (Notice 2015-17). Multi-employee disqualifies.
- D2 (FICA-exempt child): sole prop / single-member LLC default /
  parent-only partnership only. NOT available in S corp / C corp /
  LLC taxed as corp.
- D4 (rent from spouse): real-property rent excluded from SE under
  §1402(a)(1); equipment-only rentals can be SE-taxed unless leased
  *with* real estate. Run *Bobo v. Commissioner* substantial-
  services test.

### 4. Mechanics walk

Walk the detail file's mechanics. For D5 (home office), distinguish
the two methods:

- **Actual expense (Form 8829)**: % × actual expenses; depreciation
  (39-year SL); carryover for excess deductions; §1250 unrecaptured
  gain on later sale (max 25% per §1(h)(6)(A)).
- **Simplified method**: $5 × sq ft up to 300 sq ft = $1,500 max;
  no depreciation, no carryover, no §1250 recapture.

### 5. Schedule C line placement

State the specific Schedule C line (or Form 8829 line) and any
follow-on impact on Schedule SE (most Schedule C deductions reduce
the SE tax base; §162(l) self-employed health insurance does NOT
under §1402(a)(12)).

### 6. SE-tax interaction

Most Schedule C deductions reduce both income tax base AND SE tax
base. Exceptions worth flagging:

- §162(l) above-the-line health insurance: reduces income tax base
  ONLY; SE base unaffected (post-2010 §1402(a)(12) repeal).
- ½ SE tax above-the-line: standard.
- Retirement plan contributions: reduce income tax base ONLY.

### 7. State conformity

Surface non-conformity that materially affects the strategy:

- California — no §168(k) bonus; §179 capped; AB5 ABC test
  reclassifies many independent contractors to employees.
- New York — IT-225 modifications for bonus; convenience-of-employer
  rule for non-resident remote workers.
- Massachusetts — no bonus depreciation conformity; 4% surtax over
  $1M.
- Pennsylvania — no §168(k) bonus.
- AK / FL / NV / SD / TN / TX / WA / WY — no individual income tax
  (non-conformity moot for income-tax purposes; sales/use rules and
  state-specific franchise / B&O taxes still apply).

Route to `tax-research-state-income` for the per-state file.

### 8. Recent legislation (OBBBA)

OBBBA-affected items in this catalog: §168(k) bonus permanence and
100% reinstatement post-1/19/2025; §179 limits for 2025/2026;
standard deduction figures ($15,750 single 2025; $16,100 single
2026). Verify against Classification Tables — see
`shared/legislation-tracking.md`.

### 9. Conclusion + JSON sidecar

Markdown conclusion with the strategy name, Schedule C / Form 8829
line placement, eligibility result, and confidence band. JSON
sidecar validates against `shared/output-schema.json`. Use the
project's enumerated `authority_type` values (no `non_precedential_irs`
or `PublicLaw` — use `written_determinations` and
`StatutesAtLarge`). Populate `public_laws_consulted[]` for any
OBBBA-implicated analysis.

## Hard rules

- This skill catalogs and routes; load and cite the underlying
  `planning-strategy-library/references/strategies/<slug>.md`.
- Never recommend the §3121(b)(3)(A) child-FICA exemption for an
  S corp or C corp employer — it is sole prop / SMLLC default /
  parent-only partnership only.
- For rent-from-spouse (D4), always run the *Bobo* substantial-
  services check; do not assume Schedule E treatment when services
  are hotel-like.
- For home office (D5), distinguish the two methods and surface the
  §1250 unrecaptured-gain consequence under the actual-expense
  method on later sale.
- For foreign travel (D9), the §274(c) seven-day rule treats < 7
  days entirely as business if business purpose qualifies; ≥ 7 days
  requires a day-by-day allocation.
- Inflation-indexed amounts MUST be year-appropriate. Verify the
  current Rev. Proc. before quoting any figure.
- §105 HRA single-employee rule (Notice 2015-17) — cannot apply in
  multi-employee plans without ICHRA / QSEHRA / EBHRA structure
  (Notice 2013-54 standalone-HRA prohibition otherwise triggers
  §4980D $100/day per employee penalty).
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`.
