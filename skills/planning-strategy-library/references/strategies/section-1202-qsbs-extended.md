---
name: "§1202 Qualified Small Business Stock (QSBS) Exclusion"
slug: section-1202-qsbs
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§1202", "§1045", "§1244"]
forms: ["Form 8949 with §1202 exclusion code", "Schedule D"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§1202 is one of the most valuable but underutilized provisions in
the Code. Excludes (under current rules) up to **100% of capital
gain** on sale of "Qualified Small Business Stock" (QSBS), with a
per-issuer limit of the **greater of $10 million or 10× basis**.
Held five years or more.

Exclusion percentage by acquisition date:
- After September 27, 2010: **100% exclusion**.
- August 11, 1993 to February 17, 2009: 50%.
- February 18, 2009 to September 27, 2010: 75%.

For 100% exclusion stock, the gain is also exempt from §1411 NIIT.

§1045 rollover: gains from QSBS held >6 months can be rolled into
new QSBS within 60 days, deferring (not excluding) gain. §1045
restarts the §1202 holding period.

OBBBA reportedly modified §1202 — possibly increasing the exclusion
cap or holding period rules. Verify via Classification Tables.

## Primary IRC authority

- §1202 — 50%/75%/100% exclusion of gain from QSBS sale.
- §1202(a) — Exclusion percentages.
- §1202(b) — Per-issuer limit ($10M or 10× basis).
- §1202(c) — QSBS definition.
- §1202(d) — Qualified small business definition.
- §1202(e) — Active business requirement.
- §1202(h) — Tacked holding period for gifts and inheritance.
- §1045 — Rollover.

## Treasury regulations

- Reg §1.1202-2 (proposed; not finalized) — limited regulatory
  guidance. Most §1202 interpretation via case law and IRS
  pronouncements.

## Key IRS guidance

- PLR 201717010 — QSBS active business eligibility.
- PLR 202144026 — Recent QSBS PLR.
- CCA 201610006 — Corporate redemptions and §1202.

## Key court decisions

- **Owen v. Commissioner, T.C. Memo. 2012-21** — QSBS analysis;
  active business requirement.

## Eligibility requirements

QSBS:
1. **Domestic C corporation** (NOT S corp; NOT LLC taxed as
   partnership).
2. **Qualified small business** at issuance: aggregate gross
   assets ≤$50 million immediately before and after issuance.
3. **Original-issue acquisition** from corporation; not secondary
   market. Cash, property, or services rendered.
4. **Hold ≥5 years.**
5. **Active business requirement** — at least 80% of corporation's
   assets used in active conduct of qualified trade or business.
6. **Not a disqualified business** under §1202(e)(3): professional
   services, banking, insurance, financing, leasing, investing,
   farming, mining/oil & gas, hotels, restaurants.

§1045 rollover:
1. Original QSBS held >6 months.
2. New QSBS purchased within 60 days of sale.
3. Election made on timely return.

## Mechanics — how it works

1. **Verify QSBS status at issuance.** Critical — moment-of-
   issuance test.
2. **Document original issuance.** Stock certificate, board
   resolution, valuation, gross assets.
3. **Track 5-year holding period.**
4. **Verify active business throughout holding.**
5. **Sale or exchange.** Recognize gain.
6. **Exclude under §1202.** Form 8949 with code "Q"; Schedule D
   adjustment.
7. **Per-issuer limit.** $10M or 10× basis, lifetime per issuer.

## Documentation requirements

- Stock certificate.
- Corporate gross assets at issuance.
- Active business activity records.
- Annual confirmation of qualified business activity.
- Form 8949 with §1202 exclusion code.

## Common pitfalls / audit risks

- **S corp / LLC stock not eligible.** Common error: founders
  incorporate as LLC or S corp and lose §1202 entirely.
- **Active business test failure.** Holding company structures
  must satisfy 80% active business test.
- **Disqualified business creep.** Manufacturing pivoting to
  consulting may lose qualified status.
- **Original-issue requirement.** Secondary market acquisitions
  not QSBS.
- **Per-issuer limit.** $10M lifetime per issuer; spousal
  allocation possible.
- **Gift / inheritance.** Holding period and basis tack to donee.

## Recent legislative changes

- §1202(a)(4) 100% exclusion (2010 amendment, made permanent 2015).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1202
  Pub L 119-21]`. Reports indicate possible increase in $50M gross
  assets cap and/or per-issuer exclusion limit.

## State conformity considerations

State conformity varies significantly. **California** does NOT
conform; full state tax on QSBS gain. **Pennsylvania** does not
conform.

## AICPA SSTS / Circular 230 considerations

Verify qualification at multiple time points: issuance, throughout
hold, and sale. Documentation for original issuance often deficient.

## Default confidence band rationale

**HIGH** for clearly-qualifying QSBS with proper documentation.
Drops to MODERATE for aggressive interpretations or holding-company
structures.

## Cross-references

- `worthless-stock-ordinary-loss` (#30) — companion §1244.
- `installment-sale` (#33) — alternative if §1202 unavailable.
- `qoz-reinvestment` (#34) — alternative deferral.
- `gifting-stock` (#46) — gifting QSBS implications.
- `employee-stock-options` (#68).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1202","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1202","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1045","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1045","weight":"primary_statute"},
    {"authority_type":"TaxCt","citation":"Owen v. Commissioner, T.C. Memo. 2012-21","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
