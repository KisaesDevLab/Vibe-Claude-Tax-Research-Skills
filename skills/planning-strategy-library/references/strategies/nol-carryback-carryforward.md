---
name: "Net Operating Loss (NOL) Carryback and Carryforward"
slug: nol-carryback-carryforward
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§172", "§461(l)"]
forms: ["Form 1045 (quick refund)", "Form 1040X / 1120X (amended)", "Form 1139 (corp quick refund)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

A Net Operating Loss (NOL) is the excess of allowable deductions
over gross income for the tax year. NOLs can offset taxable income
in other years through carryback and carryforward mechanisms,
producing tax refunds (for carrybacks) or tax savings in future
years (for carryforwards).

The §172 rules have changed substantially:

**Pre-TCJA (NOLs arising before 2018):** 2-year carryback,
20-year carryforward, unlimited offset of taxable income.

**TCJA (NOLs arising 2018-2020):** No carryback; indefinite
carryforward; 80% of taxable income offset limit.

**CARES Act (NOLs arising 2018-2020 only, retroactive):**
Restored 5-year carryback for those years; suspended 80% limitation
for those years; ability to elect out of carryback.

**Post-CARES (NOLs arising 2021+):** No carryback; indefinite
carryforward; 80% of taxable income offset limit (back to TCJA
rule).

This change creates intricate timing analysis: NOLs from different
years follow different rules, and the practitioner must track each
NOL year's vintage separately.

§461(l) Excess Business Loss: Created by TCJA, originally suspended
through 2020 by CARES, now permanent through 2028 (via 2022 IRA
extension; OBBBA may have extended further). Limits net business
losses to a threshold ($305,000 single / $610,000 MFJ for 2024;
indexed). Excess becomes NOL carryforward subject to §172 rules.

## Primary IRC authority

- **§172(a)** — NOL deduction.
- **§172(b)** — Carryback and carryforward periods.
- **§172(b)(2)** — 80% taxable income limitation.
- **§172(d)** — NOL definition; modifications.
- **§461(l)** — Excess business losses; created by TCJA.

## Treasury regulations

- **Reg §1.172-1 through §1.172-13** — NOL implementing regulations.
- **Reg §1.461-1** — General timing rules.

## Key IRS guidance

- **Rev. Proc. 2020-24** — CARES Act NOL implementation.
- **Notice 2020-26** — CARES Act NOL guidance.
- **Rev. Proc. 2020-50** — §168 / §172 procedural guidance.
- **IRS Publication 536** — NOLs for Individuals, Estates, and
  Trusts.

## Key court decisions

- Limited recent dispute area; rules are largely mechanical.

## Eligibility requirements

For NOL generation:
1. Deductions exceed gross income.
2. NOL determined per §172(d) modifications (no NOL deduction in
   computing NOL; limited capital loss; no §199A QBI; no §250
   FDII/GILTI; no §1202 exclusion; etc.).

For carryback (CARES Act years 2018-2020 only):
1. NOL arises in 2018, 2019, or 2020.
2. Form 1045 (individual) or Form 1139 (corporation) for quick
   refund within 12 months of year-end.
3. OR Form 1040X / 1120X amended return.
4. Election to forgo carryback under §172(b)(3).

For carryforward (post-2020):
1. Indefinite carryforward.
2. 80% of taxable income offset limit per year.

## Mechanics — how it works

1. **Determine NOL.** Compute on Schedule A of Form 1045 (individual)
   or per §172(d) for corporations.
2. **Determine vintage.** Apply rules applicable to NOL year.
3. **Coordinate with §461(l).** Determine excess business loss; convert
   to NOL.
4. **Carryback (if applicable).** File Form 1045 (individual) or
   Form 1139 (corporation) for quick refund within 12 months of
   year-end. Otherwise file Form 1040X / 1120X.
5. **Carryforward.** Track each NOL year's vintage and remaining
   balance. Apply 80% taxable income limitation per year.
6. **State NOL tracking.** Many states have separate NOL rules
   (different carryback/carryforward periods, different limits).

## Documentation requirements

- NOL computation workpapers with §172(d) modifications.
- Form 1045 / 1139 / 1040X / 1120X.
- Multi-year NOL schedule by vintage.
- §461(l) computation if applicable.
- State NOL schedules.

## Common pitfalls / audit risks

- **Failure to elect out of CARES Act carryback** — §172(b)(3)
  election if carryback would generate refund of low-tax-rate years
  while taxpayer is in higher tax bracket on carryforward.
- **Incorrect NOL modifications.** §172(d) excludes various items
  (capital losses, §199A, §250) that affect NOL determination.
- **§461(l) trap.** Net business loss limited to threshold; excess
  becomes NOL.
- **State decoupling.** Many states do not follow federal CARES Act
  carryback or 80% limit; track separately.
- **Form 1045 12-month deadline.** After the deadline, must use
  Form 1040X / 1120X (amended returns).
- **AMT NOL.** AMT NOL is a separate computation; track in parallel
  for years with AMT exposure.

## Recent legislative changes

- **TCJA (2017)** — Eliminated 2-year carryback; 80% limit;
  indefinite carryforward.
- **CARES Act (2020)** — 5-year carryback for 2018-2020 NOLs;
  suspended 80% limit for those years.
- **TCDTRA 2020 / CAA 2021** — Various technical corrections.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §172 §461(l)
  Pub L 119-21]`. Reports indicate §461(l) extended; §172 generally
  unchanged.

## State conformity considerations

State NOL rules vary widely. Major decoupling states for NOLs:
California (separate NOL system), New York, New Jersey,
Pennsylvania, Massachusetts. Track state NOLs separately.

## AICPA SSTS / Circular 230 considerations

Standard diligence; NOL utilization decisions can affect multiple
years and require careful documentation.

## Default confidence band rationale

**HIGH** for properly-computed NOLs and carryforward applications.
Drops to MODERATE for §172(d) modifications that are complex (e.g.,
NOLs interacting with §199A or §250).

## Cross-references

- **`worthless-stock-ordinary-loss`** (#30) — generates NOL.
- **`maximize-business-deductions`** (#13) — generates current-
  year deductions.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 172",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section172",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 461(l)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section461",
      "weight": "primary_statute"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2020-24",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
