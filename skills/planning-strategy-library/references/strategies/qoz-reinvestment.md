---
name: "Qualified Opportunity Zone (QOZ) Reinvestment"
slug: qoz-reinvestment
type: Cap Gains
tax_type: CAG
complexity: High
irc_sections: ["§1400Z-1", "§1400Z-2"]
forms: ["Form 8949", "Form 8997", "Form 8996 (QOF)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

The Qualified Opportunity Zone (QOZ) program, created by TCJA in
§§1400Z-1 and 1400Z-2, allows taxpayers to defer (and partially
reduce) capital gains by reinvesting them into a Qualified
Opportunity Fund (QOF) within 180 days. Three benefits historically:

1. **Deferral:** Capital gain deferred until earlier of (a) sale of
   the QOF investment or (b) December 31, 2026.
2. **Reduction:** Originally, 10% basis step-up if held 5 years; 15%
   if held 7 years (largely expired due to 2026 recognition date).
3. **Exclusion:** If held 10+ years, basis stepped up to FMV at
   sale, eliminating gain on QOF appreciation.

For 2024-2025 investments, the 5-year and 7-year basis step-ups are
no longer achievable before the December 31, 2026 mandatory
recognition date. The remaining benefits are deferral until 2026
(short-term value) and the 10-year exclusion of QOF appreciation
(the substantial long-term value).

OBBBA may have extended the QOZ program. Verify via Classification
Tables.

## Primary IRC authority

- **§1400Z-1** — Designation of qualified opportunity zones.
- **§1400Z-2** — Special rules for capital gains invested in QOFs.
- **§1400Z-2(a)** — Deferral election.
- **§1400Z-2(b)** — Time for deferred gain recognition.
- **§1400Z-2(c)** — Special rule for investments held for 10 years.
- **§1400Z-2(d)** — QOF definition and 90% asset test.

## Treasury regulations

- **Reg §1.1400Z2(a)-1 through §1.1400Z2(f)-1** — Comprehensive
  QOZ regulations (final 2019 / corrected 2020).

`chevron_replaced: true` flagged on the entire QOZ regulations
package — these regulations heavily interpret ambiguous statutory
provisions and operate well beyond the bare statute.

## Key IRS guidance

- **Rev. Proc. 2018-16** — QOZ designation procedures.
- **Notice 2020-39** — COVID-era 180-day extension relief.
- **Notice 2021-10** — Additional COVID relief.

## Key court decisions

- Limited dispute area; relatively new program.

## Eligibility requirements

For deferral election:
1. Capital gain (short-term or long-term; §1231 net gains; §1245
   recapture not eligible to defer).
2. Reinvested into a Qualified Opportunity Fund (QOF) within 180
   days from the sale date (or for §1231 gains, from end of tax
   year).
3. QOF satisfies 90% asset test under §1400Z-2(d)(1).

For QOF status:
1. Domestic corporation or partnership.
2. Self-certifies as QOF on Form 8996.
3. 90% of assets are Qualified Opportunity Zone Property (QOZP).

For QOZP:
1. Qualified Opportunity Zone Business Property (QOZBP); OR
2. Stock or partnership interest in a Qualified Opportunity Zone
   Business (QOZB).
3. QOZB requirements: 70% of assets are QOZBP; less than 5% of
   assets are nonqualified financial property; substantial
   improvement requirements; etc.

## Mechanics — how it works

1. **Realize capital gain.** Sell appreciated capital asset.
2. **Identify QOF investment** within 180 days.
3. **Make deferral election** on Form 8949 with code "Z" and
   Form 8997.
4. **Annual Form 8997** during deferral period.
5. **December 31, 2026** — Recognize originally-deferred gain
   (regardless of whether QOF investment is sold).
6. **10-year holding** — Election to step basis to FMV at sale of
   QOF, eliminating gain on appreciation since investment.

## Documentation requirements

- Documentation of original capital gain (Form 8949).
- Form 8997 annual report.
- QOF Form 8996 self-certification (annual).
- QOZP / QOZB documentation.
- Holding period records.

## Common pitfalls / audit risks

- **180-day deadline missed.** No relief outside specific
  catastrophe extensions.
- **QOF 90% test failure.** Penalties and potential loss of QOF
  status.
- **QOZB 70% test failure.** Same.
- **Substantial improvement test for QOZBP.** For real estate, must
  improve basis by at least 100% within 30 months of acquisition.
- **Original-use vs. substantial-improvement.** Existing buildings
  not in original use must satisfy substantial improvement.
- **Recapture timing in 2026.** Even taxpayers in 2025 will recognize
  the originally-deferred gain on December 31, 2026 — this is
  unavoidable.

## Recent legislative changes

- **TCJA (2017)** — Created §§1400Z-1, 1400Z-2.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA QOZ Pub L 119-21
  classification table]`. Reports indicate OBBBA extended the QOZ
  program with potentially new designations and revised dates.
  Verify exact provisions.

## State conformity considerations

State conformity to QOZ deferral varies. **California, Mississippi,
North Carolina** do not conform. **New York, Massachusetts** have
mixed conformity.

## AICPA SSTS / Circular 230 considerations

QOZ structures are complex and procedural. Practitioner should
verify QOF certification and confirm QOZP requirements at investment
and at testing dates.

## Default confidence band rationale

**MODERATE** — extensive regulatory complexity with multiple
points of failure. HIGH only for properly-structured investments
with QOF certification confirmed and QOZP documented.

## Cross-references

- **`installment-sale`** (#33) — alternative deferral.
- **`1031-like-kind-exchange`** (#1) — alternative for real estate
  gains.
- **`capital-gain-offsets`** (#32).
- **`section-1202-qsbs-extended`** (#43).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1400Z-2",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1400Z-2",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.1400Z2(a)-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation",
      "chevron_replaced": true
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2020-39",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
