---
name: "Passive Income Generators (PIGs) and Passive Loss Absorption"
slug: passive-income-pigs
type: Business - Other
tax_type: EFR
complexity: High
irc_sections: ["§469"]
forms: ["Form 8582"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
caution: true
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

A "Passive Income Generator" (PIG) is an investment that produces
§469 passive income, used strategically to absorb suspended passive
losses from other passive activities. The §469 rules require that
passive losses be deductible only against passive income; losses in
excess of passive income suspend and carry forward (with eventual
release upon complete disposition under §469(g)). PIGs invert this
problem by intentionally generating passive income that the
taxpayer can offset with otherwise-suspended losses.

Common PIG structures:
- **Limited partnership interests in income-producing businesses.**
- **Working interests in oil and gas** (NOT a passive activity under
   §469(c)(3) — but if structured to fail working-interest exception,
   becomes passive).
- **Net leased real estate** — by statute and regulation a passive
  activity (no material participation possible).
- **Carried-interest shells** structured around passive treatment.

The classic PIG structure was the subject of significant abuse in
the 1980s and 1990s (sham passive income generators); the IRS has
brought numerous challenges. Modern PIG planning requires economic
substance — the income-producing activity must be real, not merely
a tax conduit.

## Primary IRC authority

- **§469(a)** — General PAL disallowance.
- **§469(c)** — Definitions of passive activity.
- **§469(c)(2)** — Per-se passive treatment of rentals.
- **§469(c)(3)** — Working interest exception (oil & gas).
- **§469(d)(1)** — Passive activity loss definition.
- **§469(g)** — Disposition of activity.
- **§469(h)** — Material participation tests.

## Treasury regulations

- **Reg §1.469-1 through §1.469-11** — Implementing regulations.
- **Reg §1.469-2(f)(6)** — Self-rental recharacterization rule.
- **Reg §1.469-2T(f)** — Recharacterization of passive income to
  nonpassive in certain situations (the "trap" — net rental income
  from property leased to a related taxpayer's nonpassive business
  is recharacterized as nonpassive, defeating PIG strategy if not
  carefully structured).

## Key IRS guidance

- **IRS Publication 925** — Passive Activity and At-Risk Rules.

## Key court decisions

- **Schwalbach v. Commissioner, 111 T.C. 215 (1998)** — Self-rental
  rule analysis.
- **Krukowski v. Commissioner, 114 T.C. 366 (2000)** — Self-rental
  applied; net rental income recharacterized as nonpassive.
- **Beecher v. Commissioner, 481 F.3d 717 (9th Cir. 2007)** —
  Affirmed self-rental recharacterization.

## Eligibility requirements

For an investment to be a valid PIG:
1. Activity must be a passive activity under §469(c).
2. Income must be passive income, not subject to recharacterization
   under Reg §1.469-2T(f).
3. Income must have economic substance (real income from real
   activity).
4. Taxpayer must not materially participate.

## Mechanics — how it works

1. **Identify suspended passive losses.** Typically from rental real
   estate or LP interests.
2. **Source PIG investment.** Common: LP interest in income-
   producing real estate; LP interest in operating business; net
   lease commercial property.
3. **Verify passive characterization.** Apply §469 tests; verify no
   recharacterization risk under Reg §1.469-2T(f).
4. **Hold long enough to generate income.** Match passive income
   to passive losses on Form 8582.
5. **Avoid self-rental trap.** Property rented to taxpayer's own
   business (or commonly-owned business) is recharacterized as
   nonpassive net income — destroying PIG utility.

## Documentation requirements

- Investment documents (LP agreement, etc.).
- Schedule K-1s.
- Form 8582 with passive activity tracking.
- Self-rental analysis if applicable.

## Common pitfalls / audit risks

- **Self-rental recharacterization.** If passive income comes from
  property rented to a business in which taxpayer materially
  participates, Reg §1.469-2T(f)(6) recharacterizes the income as
  nonpassive — defeating the PIG strategy.
- **Sham PIG.** Investments without economic substance are
  challenged.
- **Working interest oil & gas.** §469(c)(3) excludes working
  interests from passive — careful structuring required if the goal
  is passive income.
- **Material participation in PIG.** Inadvertent material
  participation defeats passive treatment.
- **Loss release on disposition.** Disposing of the PIG itself
  triggers release of THAT activity's losses, not the underlying
  losses the PIG was meant to absorb.

## Recent legislative changes

- **TCJA (2017)** — No direct §469 changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §469 PIG
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §469 is generally complete; PIG strategy flows
through.

## AICPA SSTS / Circular 230 considerations

PIG strategies attract IRS scrutiny. Practitioner must verify
economic substance and absence of recharacterization.

## Default confidence band rationale

**MODERATE** — depends on absence of self-rental recharacterization
and economic substance. **LOW** for aggressive structures or
investments with thin operating substance.

## Cross-references

- **`active-participation-real-estate`** (#3) — alternative for
  $25K offset.
- **`grouping-of-activities`** (#9) — alternative loss absorption
  through grouping.
- **`real-estate-professional-extended`** (#20) — REPS releases all rentals
  from passive treatment.
- **`predict-material-participation`** (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 469",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section469",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.469-2(f)(6)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Krukowski v. Commissioner, 114 T.C. 366 (2000)",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    }
  ]
}
```
