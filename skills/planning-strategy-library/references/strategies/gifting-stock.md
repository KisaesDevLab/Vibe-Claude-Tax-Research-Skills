---
name: "Gifting Appreciated Stock (and Other Securities)"
slug: gifting-stock
type: Income Shifting
tax_type: EFR
complexity: High
irc_sections: ["§1015", "§170", "§2503", "§2511", "§2522"]
forms: ["Form 709", "Form 8283"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

Gifting appreciated stock has multiple distinct planning uses:

1. **Charitable gifts of appreciated stock.** Donor deducts FMV
   under §170; avoids capital gain on sale; charity receives full
   FMV. Works only for long-term appreciated property.

2. **Family income shifting.** Gifting income-producing stock to
   lower-bracket family members (subject to kiddie tax §1(g)).

3. **Estate freeze.** Lifetime gifts use donor's lifetime gift tax
   exclusion ($13.61M per person 2024; possibly modified by
   OBBBA), removing future appreciation from estate.

4. **§1015 carryover basis.** Donee takes donor's basis (with
   special loss-property rules); gain on later sale may be
   significant.

5. **§2503(b) annual exclusion.** $18,000 per donor per donee
   (2024); not counted toward lifetime exclusion.

6. **Crummey trust gifts.** Gifts to trust qualify for §2503(b)
   if beneficiaries have demand right.

7. **§2522 charitable gift tax exclusion.**

## Primary IRC authority

- §170 — Charitable contributions deduction.
- §1014 — Basis at death (step-up).
- §1015 — Basis of property acquired by gift.
- §1411 — NIIT on net investment income.
- §2501 — Gift tax imposed.
- §2503(b) — Annual exclusion.
- §2510 — Lifetime gift exclusion.
- §2522 — Gift to charity exclusion.

## Treasury regulations

- Reg §1.170A-1 through §1.170A-17 — Charitable contributions.
- Reg §1.1014-1, §1.1015-1 — Basis.
- Reg §25.2503-1 through §25.2503-6 — Gift annual exclusion.
- Reg §25.2522(a)-1 — Charitable gift exclusion.

## Key IRS guidance

- Rev. Rul. 71-447 — Charity must have control over donated
  property.
- IRS Publication 526 — Charitable Contributions.
- IRS Publication 561 — Determining Value of Donated Property.

## Key court decisions

- **Crummey v. Commissioner, 397 F.2d 82 (9th Cir. 1968)** —
  Demand-right power makes gift "present interest" qualifying for
  annual exclusion.
- **Smith v. Commissioner, 78 T.C. 350 (1982), aff'd, 730 F.2d
  1356 (10th Cir. 1984)** — Charitable contribution valuation.

## Eligibility requirements

Charitable stock gift:
1. Long-term appreciated property (held >1 year).
2. Donee is qualified §170(c) charity.
3. Form 8283 if FMV >$500; appraisal if >$5,000 (with publicly-
   traded exception).
4. AGI limits: 30% for appreciated long-term capital gain property
   to public charities; excess carries forward 5 years.

Family gift:
1. Annual exclusion gifts: ≤$18,000/donor/donee/year (2024).
2. Lifetime exclusion gifts: ≤$13.61M lifetime per donor (2024;
   verify post-OBBBA).
3. Form 709 filed for split gifts or gifts >$18,000.

## Mechanics — how it works

Charitable gift:
1. **Identify long-term appreciated stock.**
2. **Transfer to charity** via brokerage transfer.
3. **Donor deducts FMV** (subject to AGI limits).
4. **Form 8283;** appraisal if >$5,000 (publicly-traded exception).

Family gift:
1. **Determine donor's basis.**
2. **Transfer stock** by brokerage transfer.
3. **Donee takes carryover basis** (no step-up).
4. **Form 709** if exceeds annual exclusion.

## Documentation requirements

- Brokerage transfer records.
- Charity acknowledgment letter; Form 8283.
- Form 709 (if applicable).
- Donor basis records.

## Common pitfalls / audit risks

- **Short-term gain property to charity.** Deduction limited to
  basis.
- **Loss property gifts.** Donee uses lesser of donor basis or
  FMV at gift for loss computation.
- **§170 substantiation.** Contemporaneous written acknowledgment
  required; appraisal for noncash >$5,000.
- **AGI limit miscalculation.** 30% / 50% / 60% limits depend on
  property type and donee.
- **Kiddie tax.** §1(g) imposes parent's bracket on dependent
  children's unearned income.

## Recent legislative changes

- **TCJA (2017)** — Doubled lifetime gift / estate exclusion;
  scheduled to sunset end of 2025.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §2010
  §2503 Pub L 119-21]`. Reports indicate lifetime exclusion made
  permanent at $15M+ inflation-adjusted level.

## State conformity considerations

**Connecticut** has state gift tax. Most states don't. State
conformity to charitable contribution deduction varies.

## Default confidence band rationale

**HIGH** for clearly-qualified gifts. Drops to MODERATE for
appraisal valuation issues.

## Cross-references

- `charitable-donation-appreciated` (#51).
- `donor-advised-fund` (#54).
- `charitable-planning` (#53).
- `income-shifting-family-member` (#48).
- `section-1202-qsbs-extended` (#43).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 170","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 1015","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1015","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 2503(b)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section2503","weight":"primary_statute"},
    {"authority_type":"CtAppeals","citation":"Crummey v. Commissioner, 397 F.2d 82 (9th Cir. 1968)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
