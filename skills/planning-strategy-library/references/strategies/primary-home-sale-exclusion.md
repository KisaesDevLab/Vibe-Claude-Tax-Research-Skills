---
name: "Primary Home Sale Exclusion (§121)"
slug: primary-home-sale-exclusion
type: Personal - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§121", "§1031(h)"]
forms: ["Form 8949", "Schedule D"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§121 allows a taxpayer to exclude up to:
- **$250,000 (single)** of gain from sale of principal residence.
- **$500,000 (married filing jointly)** of gain from sale of
  principal residence.

The exclusion is available once every 2 years and requires
satisfaction of two tests:

1. **Ownership test:** Taxpayer owned the property for at least 2
   of the last 5 years before sale.
2. **Use test:** Taxpayer used the property as principal residence
   for at least 2 of the last 5 years before sale.

The 2-year periods need not be continuous and need not coincide.

For MFJ $500K exclusion:
- Either spouse meets ownership test.
- Both spouses meet use test.
- Neither spouse used §121 exclusion in last 2 years.

Partial exclusion under §121(c) for sales due to:
- Change in employment (50+ miles).
- Health.
- Unforeseen circumstances (death, divorce, multiple births,
  involuntary conversion, etc.).

Pro rata exclusion based on time of qualifying use ÷ 2 years.

Recapture exception under §121(d)(11): non-qualified use after
2008 reduces exclusion proportionally if property was rented or
used for business.

§121(d)(10): For property converted from §1031 like-kind exchange
replacement to primary residence — must hold ≥5 years post-
exchange before §121 applies.

## Primary IRC authority

- §121 — Sale of principal residence.
- §121(a) — Exclusion.
- §121(b) — Limitations.
- §121(c) — Partial exclusion.
- §121(d) — Special rules (depreciation recapture, §1031, non-
  qualified use, etc.).
- §1031(h) — Coordination with like-kind exchange.

## Treasury regulations

- Reg §1.121-1 through §1.121-4.

## Key IRS guidance

- IRS Publication 523 — Selling Your Home.

## Key court decisions

- **Gates v. Commissioner, 135 T.C. 1 (2010)** — Property partially
  destroyed by fire; "principal residence" analysis.
- **Reesink v. Commissioner, T.C. Memo. 2012-118** — Principal
  residence test.

## Eligibility requirements

1. **Ownership ≥2 of last 5 years.**
2. **Use as principal residence ≥2 of last 5 years.**
3. **Not used §121 in last 2 years.**
4. **MFJ extra requirements** for $500K limit.

## Mechanics — how it works

1. **Determine basis** — original purchase + improvements -
   prior depreciation.
2. **Compute gain** — sale price - selling costs - basis.
3. **Apply §121 exclusion.** Up to $250K / $500K.
4. **Non-qualified use** — pro rata reduction post-2008.
5. **Depreciation recapture** — depreciation taken since May 6,
   1997 must be recaptured (taxed as unrecaptured §1250 gain;
   max 25%).
6. **Form 8949 / Schedule D** for any taxable gain.

## Documentation requirements

- Closing statements (purchase and sale).
- Improvements records (basis additions).
- Use and ownership timeline.
- Depreciation records (if business/rental use).

## Common pitfalls / audit risks

- **Property converted to rental and back.** Non-qualified use
  reduces exclusion.
- **Multiple residences.** Only "principal" residence qualifies.
- **2-year cap on exclusion.** Cannot use again within 2 years.
- **§1031 replacement converted to residence.** 5-year hold
  required under §121(d)(10).
- **Spouse §121 use during last 2 years.** Disqualifies $500K MFJ.
- **Inheritance basis.** Inherited property has step-up under
  §1014; §121 may not apply.
- **Depreciation recapture.** Taxed even if §121 excludes
  remaining gain.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §121
  Pub L 119-21]`. Some reports indicate proposals to increase
  $250K / $500K limits (which haven't been adjusted since 1997).
  Verify final OBBBA provision.

## State conformity considerations

State conformity to §121 generally complete. **Massachusetts,
Pennsylvania** have unique residence-sale treatment.

## Default confidence band rationale

**HIGH** — clear statutory framework.

## Cross-references

- `1031-like-kind-exchange` (#1) — interaction.
- `installment-sale` (#33).
- `capital-gain-offsets` (#32).
- `state-tax-savings` (#40) — domicile change interaction.
- `rental-strategies` (#25) — converted-rental interaction.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 121","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section121","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.121-1","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TaxCt","citation":"Gates v. Commissioner, 135 T.C. 1 (2010)","url":"https://www.ustaxcourt.gov","weight":"judicial"}
  ]
}
```
