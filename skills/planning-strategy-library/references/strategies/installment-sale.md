---
name: "Installment Sale (§453)"
slug: installment-sale
type: Cap Gains
tax_type: CAG
complexity: High
irc_sections: ["§453", "§453A", "§453B"]
forms: ["Form 6252", "Schedule D"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§453 installment sale treatment defers gain recognition over the
period of payment receipt rather than recognizing all gain in the
year of sale. The mechanics:

1. **Gross profit ratio:** Gross profit / contract price.
2. **Each principal payment** triggers gain recognition equal to
   payment × gross profit ratio.
3. **Interest on the deferred portion** is taxed currently as
   ordinary interest income.

The strategy is foundational for sellers receiving multi-year
payments, particularly for:
- Sale of real estate.
- Sale of closely-held business.
- Sale to family members.

Limitations and exceptions:
- **§453(b)(2)(A):** Inventory and dealer property does NOT qualify
  (must recognize all gain in year of sale).
- **§453(b)(2)(B):** Publicly-traded property does NOT qualify
  (deemed payment in full at sale).
- **§453(g):** Sale of depreciable property to controlled entity —
  installment method denied.
- **§453(e):** Related-party rules — second disposition by related
  party within 2 years triggers acceleration.
- **§453A:** For nondealer installment sales >$150,000, interest
  charge on deferred tax (the "tax on the deferred tax").
- **§1231 property:** Recapture (§§1245, 1250) recognized in year
  of sale regardless of installment method (cannot defer recapture).

## Primary IRC authority

- **§453** — Installment method.
- **§453A** — Special rules for nondealer installment sales.
- **§453B** — Gain or loss on disposition of installment obligations.
- **§1245** — Depreciation recapture (personal property).
- **§1250** — Depreciation recapture (real property).

## Treasury regulations

- **Reg §15A.453-1** — Installment method.
- **Reg §1.453-2 through §1.453-12** — Various installment rules.

## Key IRS guidance

- **Rev. Rul. 84-46** — Interest computation under §453A.
- IRS Publication 537 — Installment Sales.

## Key court decisions

- **Commissioner v. South Texas Lumber Co., 333 U.S. 496 (1948)** —
  Substantial economic interest doctrine.
- **Manuel D. Mayerson v. Commissioner, 47 T.C. 340 (1966)** —
  Election timing.

## Eligibility requirements

1. **Disposition is a sale or other disposition** under §1001.
2. **At least one payment** received after the close of the tax
   year of the sale.
3. **Property qualifies** — not inventory; not publicly-traded
   securities; not under §453(g) restrictions.
4. **Election available by default** (must affirmatively elect
   OUT if cash-method recognition preferred).
5. **§453(e) compliance** — second disposition by related party
   within 2 years not made.

## Mechanics — how it works

1. **Determine gross profit and contract price.**
   - Gross profit: Selling price − adjusted basis − selling
     expenses.
   - Contract price: Selling price (less qualifying assumed debt
     under §453(f)(7)).
   - Gross profit ratio: Gross profit / contract price.
2. **Recapture recognition in year of sale.** §§1245 / 1250
   ordinary income recognized regardless of installment method.
3. **Annual gain recognition.** Each principal payment × gross
   profit ratio.
4. **Interest on note.** Reported as ordinary interest income;
   minimum rate under §1274 / §483 if note interest below AFR.
5. **§453A interest charge** if note >$150,000.
6. **Form 6252** — annual installment sale reporting.

## Documentation requirements

- Sale agreement / contract.
- Promissory note.
- Closing statement.
- Form 6252 each year payment is received.
- Recapture computation worksheet.

## Common pitfalls / audit risks

- **Recapture not recognized in year of sale.** §1245/§1250
  recapture cannot be deferred under installment method.
- **§453(g) trap.** Sale of depreciable property to >50%-controlled
  entity blocks installment method.
- **§453(e) acceleration.** Related-party second disposition
  within 2 years.
- **§453A interest charge underestimated.** Computed on deferred
  tax × applicable underpayment rate.
- **Interest below AFR.** Imputed interest under §1274/§483
  recharacterizes part of principal as interest.
- **Wraparound mortgage interaction.** Complex interplay with
  §453(f)(3) and §453(f)(7).
- **Pledge of installment obligation as collateral.** §453A(d)
  treats pledge as receipt of cash.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §453
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §453 generally complete. **California, Wisconsin**
have unique installment sale rules.

## AICPA SSTS / Circular 230 considerations

Standard diligence; complex computation requires care.

## Default confidence band rationale

**HIGH** — clear statutory and regulatory framework. Drops to
MODERATE for §453(g) controlled-entity edge cases or §453(e)
related-party scenarios.

## Cross-references

- **`1031-like-kind-exchange`** (#1) — alternative deferral.
- **`qoz-reinvestment`** (#34) — alternative deferral.
- **`deferred-sales-trust`** (#29) — aggressive variant.
- **`capital-gain-offsets`** (#32).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 453",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section453",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 453A",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section453A",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 15A.453-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
