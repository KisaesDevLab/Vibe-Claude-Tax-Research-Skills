---
name: "Split Operating Entity from Real Estate Holding Entity"
slug: split-entity-operations-vs-re
type: SE Tax
tax_type: EFR
complexity: High
irc_sections: ["§469", "§1031", "§1411", "§199A", "§267"]
forms: ["Form 1065 / 1120-S / 1040"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Splitting an operating business from the real estate it occupies
into separate entities is a foundational planning structure for
operating businesses that own their real estate. Common structure:

- **Operating Entity (S corp or LLC):** Conducts the trade or
  business; pays rent to RE entity.
- **Real Estate Entity (LLC):** Holds the real estate; receives
  rent.

Strategic benefits:

1. **Asset protection.** RE not exposed to operating business
   liability.

2. **§469 self-rental rule (#16).** Rent paid by operating
   business to commonly-controlled RE entity is recharacterized as
   nonpassive net rental INCOME (under Reg §1.469-2(f)(6)) — but
   the RECHARACTERIZATION is one-way: income recharacterized as
   nonpassive cannot be offset by passive losses; but losses
   remain passive. Practical effect: rent income is nonpassive
   (offsettable by other nonpassive income or no other income),
   but if RE entity has losses, they remain passive.

3. **§1031 like-kind exchange flexibility.** RE entity can do
   §1031; operating business assets generally cannot.

4. **Estate planning.** RE can be gifted/inherited separately
   from business.

5. **Future sale flexibility.** Sell business without selling RE
   (or vice versa).

6. **Cost-segregation maximization** on RE entity.

7. **§199A QBI optimization** — rent income may be QBI under
   Notice 2019-07 safe harbor (250 hours of rental services) if
   RE constitutes a trade or business; otherwise not QBI.

8. **NIIT planning (#69)** — net rental income may or may not be
   NIIT depending on §469 trade or business classification under
   §1411.

Limitations:
- **§267 related-party rules.** Rent must be at arm's-length;
  excess rent recharacterized.
- **§469(j)(8) self-rental fix-up.** Self-rental rule limits
  passive loss strategies but does not eliminate the need for
  arm's-length rent.
- **Operating expense allocation.** Mortgage interest, property
  tax, insurance must be properly allocated between entities.

## Primary IRC authority

- §469 — Passive activity.
- §469(c)(2) — Per-se passive treatment of rentals.
- §1031 — Like-kind exchange.
- §1411 — NIIT.
- §199A — QBI.
- §267 — Related-party rules.
- §482 — Transfer pricing (intercompany).

## Treasury regulations

- Reg §1.469-2(f)(6) — Self-rental recharacterization.
- Reg §1.469-4 — Definition of activity (grouping interaction).
- Reg §1.1411-4 — NIIT trade or business analysis.
- Reg §1.199A-1 through 1.199A-6.

## Key IRS guidance

- Notice 2019-07 — Rental real estate enterprise §199A safe harbor
  (250 hours of rental services).
- IRS Publication 925.

## Key court decisions

- **Krukowski v. Commissioner, 114 T.C. 366 (2000)** — Self-rental
  rule applied.
- **Beecher v. Commissioner, 481 F.3d 717 (9th Cir. 2007)** —
  Self-rental upheld.
- **Schwalbach v. Commissioner, 111 T.C. 215 (1998)** — Self-
  rental analysis.

## Eligibility requirements

For valid split structure:
1. Bona fide separate entities.
2. Arm's-length rent.
3. Properly documented lease agreement.
4. Each entity properly capitalized.
5. Each entity respects formalities.

## Mechanics — how it works

1. **Form RE entity** (typically LLC) and transfer real estate
   into it (or purchase RE in entity initially).
2. **Form / maintain operating entity** (S corp or LLC).
3. **Establish lease** at fair market rent supported by
   comparables or appraisal.
4. **Operating entity pays rent** to RE entity.
5. **RE entity pays mortgage, property tax, insurance, repairs,
   improvements.**
6. **Operating entity deducts rent** as §162.
7. **RE entity reports rent income.** Subject to §469 and §1411
   analysis.
8. **§469 grouping consideration (#9)** — may affect both passive
   activity classification and §199A aggregation.

## Documentation requirements

- Entity formation documents.
- Lease agreement.
- Rent comparables / appraisal (arm's-length support).
- Annual rent payment records.
- Maintenance cost allocation between entities.

## Common pitfalls / audit risks

- **Rent not at arm's-length.** Below-market rent may be
  recharacterized as gift or capital contribution; above-market
  rent may be recharacterized as dividend.
- **§267 related-party loss disallowance.**
- **Self-rental recharacterization** of rent income as nonpassive
  (limits offsetting by passive losses).
- **§199A QBI uncertainty.** Whether rental constitutes §162 trade
  or business affects QBI eligibility.
- **§1411 NIIT applicability.** Self-rental income still NII unless
  rises to §162 trade or business level under §469.
- **State entity tax overhead** — separate entity adds franchise
  tax, return filing, state-level fees.

## Recent legislative changes

- **TCJA (2017)** — Created §199A; QBI analysis now relevant for
  rental activities.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A
  §469 Pub L 119-21]`. Working assumption: framework preserved.

## State conformity considerations

State entity-tax overhead and reporting requirements vary. **CA,
NY, TX** have meaningful state-level entity taxes.

## Default confidence band rationale

**HIGH** for properly-structured arm's-length splits. Drops to
MODERATE for rent valuation issues or §199A trade-or-business
classification.

## Cross-references

- `passive-income-pigs` (#16) — self-rental rule detail.
- `grouping-of-activities` (#9).
- `1031-like-kind-exchange` (#1).
- `cost-segregation-extended` (#41).
- `qbi-deduction` (#19).
- `niit-minimization` (#69).
- `rental-strategies` (#25).
- `c-corp-state-tax-savings` (#35).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 469","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.469-2(f)(6)","url":"https://www.ecfr.gov/current/title-26","weight":"regulation"},
    {"authority_type":"TaxCt","citation":"Krukowski v. Commissioner, 114 T.C. 366 (2000)","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"Notice","citation":"Notice 2019-07","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
