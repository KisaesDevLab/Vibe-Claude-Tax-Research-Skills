---
name: "Income Shifting to Lower Tax Rate Family Member"
slug: income-shifting-family-member
type: Income Shifting
tax_type: EFR
complexity: Medium
irc_sections: ["§1(g)", "§73", "§704(e)", "§267"]
forms: ["Form 8615 (Kiddie Tax)", "Form 1040 dependent return"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

> **Caution:** Income shifting to family members is constrained by
> the §1(g) "kiddie tax" (children under 24 dependents), §704(e)
> family partnership rules, and IRS attention to economic substance.
> Pure assignment of income (without underlying property transfer)
> is ineffective under Lucas v. Earl. Substance requires bona fide
> property transfer, not paper-only allocation.

## Overview

Income shifting to family members in lower tax brackets has been
foundational tax planning for decades. The economics are
straightforward: a parent in the 37% bracket transfers
income-producing assets (stocks, bonds, partnership interests) to
a child in the 0%/10%/12% bracket, reducing family-aggregate tax.

Substantive constraints:

1. **§1(g) "kiddie tax"** — Unearned income above threshold
   ($2,600 for 2024) of dependent children under age 18 (or
   full-time students under 24) is taxed at parent's marginal
   bracket. Effectively disallows income shifting for typical
   dependent children.

2. **§704(e) family partnership rules** — In family partnerships,
   donee partner is recognized only if capital is a material
   income-producing factor and the donee actually owns the
   capital interest. Service partnerships generally cannot use
   family partnership splitting.

3. **Lucas v. Earl, 281 U.S. 111 (1930)** — Assignment of income
   doctrine: the person who earns income is taxed on it. Cannot
   simply "assign" salary or business profits to family members.

4. **§267 related-party rules** — Loss disallowance and matching
   rules between family members.

5. **Bona fide gift requirement** — Property transfers must be
   genuine, irrevocable gifts; donor cannot retain control.

Effective strategies focus on (a) bona fide gifts of capital
property to adult children (above kiddie tax age), (b) hiring
children for legitimate work (#49), (c) wages to spouse for actual
services (#50), and (d) §704(e) family partnerships where capital
is material income-producing factor.

## Primary IRC authority

- §1(g) — Kiddie tax.
- §73 — Services of child taxed to child if performed.
- §704(e) — Family partnerships.
- §267 — Related-party transactions.
- §1015 — Carryover basis on gift.
- §2503(b) — Annual exclusion (companion).

## Treasury regulations

- Reg §1.1(g)-1, §1.1(i)-1 — Kiddie tax.
- Reg §1.704-1(e) — Family partnerships.
- Reg §1.267(c)-1 — Constructive ownership.

## Key IRS guidance

- IRS Publication 929 — Tax Rules for Children and Dependents.

## Key court decisions

- **Lucas v. Earl, 281 U.S. 111 (1930)** — Assignment of income
  doctrine.
- **Helvering v. Horst, 311 U.S. 112 (1940)** — Taxation of income
  attributable to property transferred to family member.
- **Commissioner v. Culbertson, 337 U.S. 733 (1949)** — Family
  partnership requirements.

## Eligibility requirements

For asset gift income shifting:
1. Bona fide irrevocable gift of property.
2. Donee actually receives ownership rights.
3. Donor does not retain control or beneficial enjoyment.
4. Annual exclusion under §2503(b) or lifetime exclusion used for
   gift tax purposes.

For §704(e) family partnership:
1. Capital is material income-producing factor.
2. Donee partner's interest is bona fide and actually owned.
3. Allocation of income consistent with capital interest.
4. Donor partner receives reasonable compensation for services.

## Mechanics — how it works

1. **Identify income-producing property** suitable for transfer
   (long-term holdings; income-producing securities; rental real
   estate interests).
2. **Annual exclusion gifts** — $18,000/donor/donee (2024).
3. **Bona fide transfer** — change of legal title, brokerage account
   ownership, deed.
4. **Kiddie tax planning** — for children under 24 dependents,
   §1(g) limits effectiveness; gifts to adult children most
   effective.
5. **§704(e) family partnership** — capital partnership; donee
   partners with bona fide interest.
6. **Track basis carryover** — §1015.
7. **Form 8615** for dependent children with unearned income above
   threshold.

## Documentation requirements

- Gift documentation (transfer records, deed, brokerage transfer).
- Form 709 if exceeds annual exclusion.
- For partnership: bona fide partnership agreement; donee actually
  receiving K-1.
- Donor's basis records (carryover).

## Common pitfalls / audit risks

- **Kiddie tax surprise.** §1(g) makes shift ineffective for
  dependent children under 24.
- **Lucas v. Earl assignment.** Pure income assignment without
  property transfer is ineffective.
- **§704(e) family partnership.** Service partnerships cannot use
  family partnership splitting.
- **Retained control.** Donor retaining beneficial enjoyment
  invalidates gift.
- **Constructive ownership.** §267 may collapse intra-family
  transactions.
- **State conformity.** State kiddie tax rules vary.

## Recent legislative changes

- **TCJA (2017)** — Modified §1(g) kiddie tax to use trust rates
  (later reverted by SECURE Act 2019 to parent rates).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1(g)
  Pub L 119-21]`. Working assumption: kiddie tax framework
  unchanged.

## State conformity considerations

State conformity to §1(g) generally complete. State income tax
rates affect benefit.

## Default confidence band rationale

**MODERATE** — clear statutory framework but fact-intensive
substance requirements. HIGH for adult-child gifts of capital
property; LOW for service-income assignment attempts.

## Cross-references

- `gifting-stock` (#46).
- `hiring-kids` (#49).
- `wages-spouse-parents` (#50).
- `family-limited-partnership` (#55).
- `529-savings-plan` (#57).
- `college-student-strategies` (#60).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 1(g)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 704(e)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section704","weight":"primary_statute"},
    {"authority_type":"SCOTUS","citation":"Lucas v. Earl, 281 U.S. 111 (1930)","url":"https://www.supremecourt.gov","weight":"binding_judicial"},
    {"authority_type":"SCOTUS","citation":"Helvering v. Horst, 311 U.S. 112 (1940)","url":"https://www.supremecourt.gov","weight":"binding_judicial"},
    {"authority_type":"SCOTUS","citation":"Commissioner v. Culbertson, 337 U.S. 733 (1949)","url":"https://www.supremecourt.gov","weight":"binding_judicial"}
  ]
}
```
