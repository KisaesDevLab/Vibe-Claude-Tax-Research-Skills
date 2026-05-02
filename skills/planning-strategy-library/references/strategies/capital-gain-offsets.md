---
name: "Capital Gain Offsets and Loss Harvesting"
slug: capital-gain-offsets
type: Cap Gains
tax_type: CAG
complexity: Medium
irc_sections: ["§1211", "§1212", "§1091", "§1222"]
forms: ["Form 8949", "Schedule D"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Capital gain offset planning involves coordinating capital gains and
losses to minimize tax. The mechanics under §§1211-1222:

1. **Net short-term against short-term; net long-term against
   long-term.** Within each character class.
2. **Net short-term loss against long-term gain** (and vice versa)
   if either class produces a net loss.
3. **§1211(b) limit:** Individual capital losses limited to capital
   gains plus $3,000 ordinary income offset per year.
4. **§1212 carryforward:** Excess capital losses carry forward
   indefinitely (individuals); 5-year carryforward and 3-year
   carryback (corporations).
5. **§1091 wash sale rule:** Losses disallowed if substantially
   identical securities purchased within 30 days before or after
   the sale.

The classic year-end strategies:
- **Tax-loss harvesting:** Sell losing positions to offset realized
  gains. Replace with similar (but not "substantially identical")
  positions to maintain market exposure.
- **Specific lot identification:** When selling part of a position
  with multiple lots, identify specific lots to maximize loss /
  minimize gain.
- **Year-end gain timing:** Defer realization of gains to next year
  if expected to be in lower bracket.
- **Carryforward management:** Track carryforwards by character
  (short-term vs. long-term).

For high-income taxpayers, §1411 NIIT (3.8%) applies to net
investment income including net capital gains; coordination with
NIIT is part of the analysis.

## Primary IRC authority

- **§1211** — Limitation on capital losses.
- **§1212** — Capital loss carryovers.
- **§1091** — Loss from wash sales of stock or securities.
- **§1222** — Other terms relating to capital gains and losses.
- **§1223** — Holding period rules.
- **§1411** — NIIT.

## Treasury regulations

- **Reg §1.1211-1** — Limitations.
- **Reg §1.1212-1** — Capital loss carryovers.
- **Reg §1.1091-1** — Wash sales.
- **Reg §1.1411-1 through §1.1411-10** — NIIT regulations.

## Key IRS guidance

- IRS Publication 550 — Investment Income and Expenses.
- IRS Publication 564 — Mutual Fund Distributions.

## Key court decisions

- **Helvering v. Bashford, 302 U.S. 454 (1938)** — Substantially
  identical securities concept.

## Eligibility requirements

For §1211 / §1212 loss treatment:
1. Capital asset disposed of in taxable transaction.
2. Holding period determined under §1223.
3. Loss not disallowed by §1091 wash sale, §267 related-party,
   §183 hobby loss, or other disallowance provision.

For §1091 wash sale avoidance:
1. Replacement security not "substantially identical" to security
   sold.
2. Replacement period: 30 days before sale through 30 days after.
3. Watch for indirect wash sales (spouse purchases; IRA purchases).

## Mechanics — how it works

1. **Year-end tax planning review.** Identify realized gains and
   losses YTD; identify unrealized losses on losing positions.
2. **Loss harvesting candidates.** Securities with significant
   unrealized losses where market exposure can be maintained.
3. **Verify §1091 compliance.** Replacement security must not be
   substantially identical.
4. **Specific identification.** Use specific lot ID for mutual
   funds and equities (vs. average cost basis); this requires
   contemporaneous identification at sale.
5. **Coordinate with NIIT.** §1411 NIIT applies to net investment
   income; loss harvesting reduces NIIT base.
6. **Track carryforwards** by character (short-term, long-term).

## Documentation requirements

- Brokerage statements showing transactions.
- Specific identification documentation (if used).
- Form 8949 / Schedule D.
- Wash sale tracking (broker generally provides on 1099-B Box 1g).

## Common pitfalls / audit risks

- **Wash sale violations.** Repurchase within 30 days defeats
  loss; basis added to replacement security.
- **Indirect wash sales.** Spouse, controlled corporation, IRA
  purchases all trigger §1091.
- **Substantially identical determination.** Different mutual
  funds tracking same index may or may not be "substantially
  identical" — fact-intensive.
- **Specific identification not made at sale.** Default is FIFO
  for stocks; average cost for mutual funds.
- **Holding period miscalculation.** Long-term requires more than
  one year holding.
- **§267 related-party loss disallowance.** Loss on sale to
  related party (spouse, ancestor, descendant, controlled corp)
  is disallowed.

## Recent legislative changes

- **TCJA (2017)** — No direct capital loss changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1211 §1212
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §1211 / §1212 generally complete. **California**
imposes state-specific carryforward rules. **Pennsylvania** does
not allow capital loss carryforward against ordinary income.

## AICPA SSTS / Circular 230 considerations

Standard diligence; routine year-end planning.

## Default confidence band rationale

**HIGH** — clear statutory framework. Drops to MODERATE only for
substantially identical security determinations or related-party
disallowance edge cases.

## Cross-references

- **`installment-sale`** (#33).
- **`niit-minimization`** (#69).
- **`qoz-reinvestment`** (#34) — alternative to loss harvesting
  for large gains.
- **`charitable-donation-appreciated`** (#51) — alternative use of
  appreciated positions.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1211",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1211",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1091",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1091",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1411",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1411",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.1091-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
