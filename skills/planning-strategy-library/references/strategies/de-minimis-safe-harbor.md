---
name: "De Minimis Safe Harbor for Small Asset Purchases (Reg §1.263(a)-1(f))"
slug: de-minimis-safe-harbor
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§263(a)"]
forms: ["No specific form; election made annually on timely return"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

The de minimis safe harbor under Reg §1.263(a)-1(f) — part of the
2014 "Tangible Property Regulations" — allows a taxpayer to elect to
deduct (rather than capitalize) tangible property under a per-item
threshold:

- **$5,000 per item** for taxpayers with an "applicable financial
  statement" (AFS) — generally a CPA-audited or reviewed financial
  statement filed with SEC, or used for certain credit/regulatory
  purposes.
- **$2,500 per item** for taxpayers without an AFS.

The election covers:
- Tangible property other than inventory or land.
- Property under the threshold per invoice or per item (as
  substantiated on invoice).

Annual election required by attaching statement to timely-filed
return. Plan must:
1. Treat amounts under threshold as deductible for non-tax purposes
   (book treatment matches tax for AFS taxpayers).
2. Have written accounting policy at the start of the year (for
   AFS taxpayers).

The strategy is foundational for small businesses and an essential
companion to the §168(k) / §179 strategy (#12). For items under
$2,500 ($5,000 with AFS), the de minimis safe harbor is simpler
than tracking §168 depreciation or §179 elections.

## Primary IRC authority

- **§263(a)** — Capital expenditures.
- **§162(a)** — Ordinary and necessary business expenses.

## Treasury regulations

- **Reg §1.263(a)-1(f)** — De minimis safe harbor.
- **Reg §1.263(a)-1(f)(1)(ii)(D)** — Definition of applicable
  financial statement.
- **Reg §1.263(a)-2** — Amounts paid to acquire tangible property.
- **Reg §1.263(a)-3** — Amounts paid to improve tangible property.
- **Reg §1.263(a)-4** — Amounts paid to acquire intangibles.

## Key IRS guidance

- **Notice 2015-82** — Increased threshold from $500 to $2,500 for
  non-AFS taxpayers.
- **Rev. Proc. 2015-20** — Procedures for small businesses to
  apply tangible property regs without filing Form 3115.

## Key court decisions

- Limited dispute area; rules are mechanical.

## Eligibility requirements

For non-AFS taxpayer:
1. Item cost ≤$2,500 per item (per invoice or substantiated per
   item).
2. Annual election attached to timely-filed return.
3. Property is not inventory.

For AFS taxpayer:
1. Item cost ≤$5,000.
2. Written accounting procedure in effect at start of year.
3. Treats amounts under threshold as expensed for AFS purposes.
4. Annual election.

## Mechanics — how it works

1. **Adopt written accounting policy** (AFS taxpayers — required
   by start of year; non-AFS taxpayers — recommended but not
   required by statute).
2. **Apply threshold per item.** Single invoice for multiple items
   — threshold per item, not per invoice.
3. **Deduct items under threshold** as ordinary business expense
   in year placed in service.
4. **Items over threshold** continue under §168 depreciation /
   §179 / §168(k) bonus.
5. **Annual election** via attached statement to return.

## Documentation requirements

- Written accounting policy (AFS) or evidence of consistent
  treatment.
- Election statement attached to return.
- Invoices substantiating per-item cost.

## Common pitfalls / audit risks

- **Failure to make annual election.** Election is required each
  year; failure means default capitalization rules apply.
- **AFS threshold confusion.** Many small businesses assume $5,000
  applies; actual non-AFS limit is $2,500.
- **Per-invoice vs. per-item.** Threshold applies per item, not
  per invoice. A single invoice for ten $2,000 chairs ($20,000
  total) — each chair item is under $2,500 and qualifies.
- **No written policy at start of year (AFS).** Disqualifies
  election for AFS taxpayers.
- **Inventory items.** Inventory does not qualify regardless of
  per-item cost.

## Recent legislative changes

- **2014 Final Tangible Property Regulations** — Original framework.
- **Notice 2015-82** — Threshold increase.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA tangible
  property regulations §263 Pub L 119-21]`. Working assumption: no
  changes; threshold remains $2,500 / $5,000.

## State conformity considerations

State conformity to Reg §1.263(a)-1(f) is generally complete.

## AICPA SSTS / Circular 230 considerations

Standard diligence; routine planning area.

## Default confidence band rationale

**HIGH** — explicit regulatory safe harbor with clear IRS-imposed
thresholds.

## Cross-references

- **`bonus-and-section-179-depreciation`** (#12) — companion
  strategy for items over threshold.
- **`maximize-business-deductions`** (#13) — broader framework.
- **`de-minimis-safe-harbor-self-employed`** (#93) — Schedule C
  variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 263(a)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section263",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.263(a)-1(f)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2015-82",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2015-20",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
