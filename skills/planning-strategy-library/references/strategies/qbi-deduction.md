---
name: "Qualified Business Income (QBI) Deduction"
slug: qbi-deduction
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§199A"]
forms: ["Form 8995 / 8995-A"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
cross_reference_skills: ["predict-qbi-eligibility"]
---

> **Cross-reference:** This strategy file complements
> `predict-qbi-eligibility`. The predict skill performs the
> eligibility analysis (whether a specific business qualifies);
> this strategy file describes the planning use case.

## Overview

§199A allows a 20% deduction on Qualified Business Income (QBI) for
non-corporate owners of pass-through entities (sole proprietors,
partnerships, S corporations, LLCs, certain trusts, certain rental
real estate). The deduction is below-the-line but does not require
itemizing.

The 20% rate is subject to:
1. **Wage / UBIA limit** (above income thresholds).
2. **Specified Service Trade or Business (SSTB) phase-out** (above
   income thresholds).
3. **20% taxable income overall cap.**

The thresholds for 2024:
- **Below $383,900 MFJ / $191,950 single:** Full 20% deduction;
  no wage limit; no SSTB exclusion.
- **Phase-in zone:** $383,900–$483,900 MFJ; $191,950–$241,950
  single.
- **Above phase-in:** Wage / UBIA limit applies (greater of 50% of
  W-2 wages or 25% of W-2 wages plus 2.5% of UBIA of qualified
  property); SSTB completely excluded.

OBBBA permanence: §199A was scheduled to sunset after 2025 under
TCJA. OBBBA reportedly made §199A permanent. Verify exact
provisions.

## Primary IRC authority

- **§199A** — QBI deduction. Statute and structure.
- **§199A(b)(2)** — Combined QBI amount calculation.
- **§199A(b)(3)** — Phase-in for SSTBs and W-2/UBIA limit.
- **§199A(c)** — QBI definition.
- **§199A(d)** — SSTB definition.
- **§199A(e)** — Other definitions (W-2 wages, UBIA).

## Treasury regulations

- **Reg §1.199A-1 through 1.199A-6** — Comprehensive implementing
  regulations.
- **Reg §1.199A-3** — QBI definition and computation.
- **Reg §1.199A-4** — Aggregation of trades or businesses.
- **Reg §1.199A-5** — SSTB definition.
- **Reg §1.199A-6** — Trust and estate rules.

`chevron_replaced: true` flagged on Reg §1.199A-5 SSTB definition
(post-Loper Bright). The regulation interprets the ambiguous
statutory term "specified service trade or business" with detailed
examples and de minimis rules. Practitioners relying on the
regulation's specific examples should note Skidmore review now
applies.

## Key IRS guidance

- **Notice 2019-07** — Safe harbor for rental real estate
  enterprise as §199A trade or business (250 hours of rental
  services).
- **Rev. Proc. 2019-38** — Updated rental real estate safe harbor.

## Key court decisions

- Limited recent dispute area; statute and regulations relatively
  recent.

## Eligibility requirements

See `predict-qbi-eligibility` for detailed eligibility analysis. Key:
1. QBI from qualified trade or business (not SSTB above threshold;
   not C corp).
2. Below-threshold taxpayers: no further limits.
3. Above-threshold: W-2/UBIA limit and SSTB exclusion apply.

SSTB categories under §199A(d)(2):
- Health
- Law
- Accounting
- Actuarial science
- Performing arts
- Consulting
- Athletics
- Financial services
- Brokerage services
- Any trade or business where the principal asset is the reputation
  or skill of one or more of its employees or owners

Engineering and architecture are explicitly excluded from SSTB
treatment under §199A(d)(2)(A).

## Mechanics — how it works

1. **Identify each trade or business** for §199A purposes.
2. **Compute QBI per business.**
3. **Apply SSTB analysis if above threshold.**
4. **Apply W-2/UBIA limit if above threshold.**
5. **Aggregation election.** Reg §1.199A-4 allows aggregation under
   conditions: same person directly or by attribution owns 50%+ of
   each business; aggregation reported and tracked annually; same
   tax year; not SSTB; meet two of three tests (similar products/
   services, sharing facilities/personnel, operationally interdependent).
6. **Form 8995 (simplified) or 8995-A (full).**

## Documentation requirements

See predict skill.

## Common pitfalls / audit risks

See predict skill.

## Recent legislative changes

- **TCJA (2017)** — Created §199A.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §199A
  permanence Pub L 119-21]`. Reports indicate §199A made permanent.

## State conformity considerations

State decoupling on QBI varies. Major decoupling states:
California, New York, New Jersey, Pennsylvania (no QBI for state).

## AICPA SSTS / Circular 230 considerations

See predict skill.

## Default confidence band rationale

**HIGH** for clear-fact patterns. See predict skill for fact-
specific analysis.

## Cross-references

- **`predict-qbi-eligibility`** (predict skill) — primary
  qualification analysis.
- **`reasonable-comp-corp-owners`** (#21) — interaction with §199A
  W-2 wage limit (S corp owner wages count toward W-2 limit).
- **`real-estate-professional-extended`** (#20) — REPS rental qualifying
  as §199A trade or business.
- **`grouping-of-activities`** (#9) — interacts with §199A
  aggregation.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 199A",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section199A",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.199A-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.199A-5",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation",
      "chevron_replaced": true
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2019-07",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
