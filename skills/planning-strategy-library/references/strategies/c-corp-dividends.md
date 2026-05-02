---
name: "C Corporation Dividend Planning"
slug: c-corp-dividends
type: C Corp
tax_type: CAG
complexity: Low
irc_sections: ["§301", "§316", "§1(h)(11)", "§531-537"]
forms: ["Form 1099-DIV"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

C corporation dividend planning involves the timing and
characterization of distributions to shareholders. The framework:

1. **§301 / §316:** A distribution is a dividend to the extent of
   the corporation's earnings and profits (E&P). Distributions in
   excess of E&P are first applied against shareholder basis (not
   taxable; basis reduction); any further excess is capital gain.
2. **§1(h)(11) qualified dividend rate:** Most dividends to
   individual shareholders are taxed at preferential long-term
   capital gains rates (0%, 15%, or 20% based on taxable income
   threshold).
3. **§531-537 accumulated earnings tax:** Penalty 20% tax on
   "unreasonable" accumulation of earnings beyond reasonable
   business needs. This indirectly forces distribution of excess
   earnings.
4. **§541 personal holding company tax:** Penalty 20% tax on PHCs
   that fail to distribute earnings.

The strategic decision: when and how much to distribute as
dividends. C corp tax rates (21% post-TCJA) are lower than top
individual rates, so retaining earnings inside the corporation
defers personal-level tax. But §531/§541 penalties limit excessive
retention, and the qualified dividend rate makes annual
distribution often tax-efficient.

For closely-held C corps, the comp/dividend mix interacts with
reasonable compensation analysis (#21). Excessive comp risks
recharacterization as dividend (corp loses §162 deduction);
inadequate comp risks IRS reclassification as constructive dividend
(reverse problem).

## Primary IRC authority

- **§301** — Distributions of property by corporations.
- **§301(c)** — Treatment as dividend / return of capital / capital
  gain.
- **§316** — Definition of dividend.
- **§312** — Earnings and profits computation.
- **§1(h)(11)** — Qualified dividend rate.
- **§531-537** — Accumulated earnings tax.
- **§541-547** — Personal holding company tax.
- **§243** — Dividends-received deduction (corporate shareholders).

## Treasury regulations

- **Reg §1.301-1** — Distributions.
- **Reg §1.316-1** — Dividend definition.
- **Reg §1.312-1 through §1.312-15** — Earnings and profits.
- **Reg §1.531-1 through §1.537-3** — Accumulated earnings tax.

## Key IRS guidance

- IRS Publication 542 — Corporations.
- IRS Publication 550 — Investment Income.

## Key court decisions

- **Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030
  (1965)** — "Bardahl formula" for reasonable working capital
  needs (§531 defense).
- **Atlas Tool Co. v. Commissioner, 70 T.C. 86 (1978), aff'd, 614
  F.2d 860 (3d Cir. 1980)** — Constructive dividend principles.

## Eligibility requirements

For qualified dividend rate under §1(h)(11):
1. Dividend paid by domestic corporation or qualified foreign
   corporation.
2. Holding period satisfied: stock held more than 60 days during
   the 121-day period beginning 60 days before ex-dividend date.
3. Not a hedged or short position.

For §243 corporate dividends-received deduction:
- 50% / 65% / 100% deduction based on ownership percentage in payer.

## Mechanics — how it works

1. **Determine current and accumulated E&P.** Annual E&P
   computation; track historical accumulated E&P.
2. **Plan distribution amount.** Consider:
   - Excess working capital.
   - §531 reasonable accumulation defense (Bardahl formula).
   - Owner cash needs.
   - Tax bracket optimization (qualified dividend rate vs. retention).
3. **Authorize distribution** by board resolution.
4. **Pay distribution.** Issue check or credit shareholder account.
5. **File Form 1099-DIV.** Box 1a total ordinary dividends; Box 1b
   qualified dividends (assuming holding period met).

## Documentation requirements

- E&P computation schedule.
- Board resolutions authorizing dividends.
- Form 1099-DIV.
- §531 reasonable accumulation analysis (defensive documentation).

## Common pitfalls / audit risks

- **Constructive dividends.** Personal expenses paid by corp,
  excessive compensation, below-market loans to shareholders,
  rent on shareholder property — all may be recharacterized as
  dividends.
- **§531 accumulated earnings tax exposure.** Unreasonable
  accumulation beyond business needs.
- **§541 PHC tax exposure.** Closely-held holding companies with
  passive income.
- **E&P computation errors.** E&P does not equal taxable income;
  several specific adjustments under §312.
- **Holding period failure.** §1(h)(11) qualified dividend rate
  denied without 60-day holding period.

## Recent legislative changes

- **TCJA (2017)** — Reduced C corp rate to 21%; preserved §1(h)(11)
  qualified dividend rate.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §11 corporate
  rate Pub L 119-21]`. Working assumption: 21% rate maintained.

## State conformity considerations

State C corp tax rates vary. State conformity to qualified dividend
treatment varies; some states tax dividends as ordinary income.

## AICPA SSTS / Circular 230 considerations

Standard diligence; constructive dividend issues require careful
client communication.

## Default confidence band rationale

**HIGH** for ordinary dividends under E&P. Drops to MODERATE when
constructive dividend issues are present, or when §531 accumulation
defense is thin.

## Cross-references

- **`reasonable-comp-corp-owners`** (#21) — comp/dividend
  bilateral issue.
- **`income-shifting-to-c-corp`** (#47).
- **`c-corp-misc-deductions`** (#42).
- **`c-corp-state-tax-savings`** (#35).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 301",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section301",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1(h)(11)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 531",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section531",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030 (1965)",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    }
  ]
}
```
