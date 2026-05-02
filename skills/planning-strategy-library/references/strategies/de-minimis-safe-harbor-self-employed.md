---
name: "De Minimis Safe Harbor — Self-Employed"
slug: de-minimis-safe-harbor-self-employed
type: SE Tax
tax_type: EFR
complexity: Low
irc_sections: ["§263(a)"]
forms: ["No specific form; election annually on timely return"]
state_specific: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Self-employed application of de minimis safe harbor (see #28 for
corporate context). Reg §1.263(a)-1(f) allows election to deduct
tangible property under threshold:

- **$2,500 per item** for non-AFS taxpayers (most self-employed).
- **$5,000 per item** for AFS taxpayers (rare for self-employed).

Annual election required by attached statement.

For sole proprietors, the de minimis safe harbor is the simplest
mechanism for routine small-asset purchases (computers, peripherals,
small office equipment, tools, etc.). Avoids depreciation tracking
on items individually under threshold.

## Primary IRC authority

- §263(a) — Capital expenditures.
- §162(a) — Trade or business expenses.

## Treasury regulations

- Reg §1.263(a)-1(f) — De minimis safe harbor.

## Key IRS guidance

- Notice 2015-82 — Threshold increase.
- Rev. Proc. 2015-20 — Small business tangible property
  procedures.

## Eligibility requirements

For non-AFS:
1. Item cost ≤$2,500 per item (per invoice or substantiated per
   item).
2. Annual election attached to timely-filed return.
3. Property is not inventory.

## Mechanics — how it works

1. **Annual election** via attached statement.
2. **Apply threshold per item.**
3. **Deduct items under threshold** as Schedule C ordinary expense.
4. **Items over threshold** continue under §168 / §179 / §168(k).

## Documentation requirements

- Election statement attached to return.
- Invoices substantiating per-item cost.

## Common pitfalls / audit risks

- **Annual election forgotten.** Must be made each year.
- **Per-invoice vs. per-item.** Threshold per item; one invoice
  for multiple items qualifies if each item is under threshold.
- **Inventory disqualified.**

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §263 de
  minimis Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity generally complete.

## Default confidence band rationale

**HIGH** — explicit regulatory safe harbor.

## Cross-references

- `de-minimis-safe-harbor` (#28).
- `bonus-and-section-179-depreciation` (#12).
- `bonus-179-depreciation-self-employed` (#89).
- `accountable-plan-self-employed` (#84).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 263(a)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section263","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.263(a)-1(f)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"Notice","citation":"Notice 2015-82","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
