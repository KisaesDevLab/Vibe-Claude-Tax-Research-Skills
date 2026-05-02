---
name: "R&D Credit (§41) and §174 R&E Capitalization"
slug: r-and-d-credit-strategy
type: Credit/Payment
tax_type: CREDIT
complexity: High
irc_sections: ["§41", "§174", "§280C(c)"]
forms: ["Form 6765", "Form 8974 (payroll offset)"]
state_specific: true
caution: true
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
cross_reference_skills: ["predict-r-and-d-credit"]
---

> **Caution:** §41 R&D Credit is a high-IRS-scrutiny area. The LB&I
> R&D Audit Roadmap systematically challenges documentation. Many
> small businesses claim the credit based on aggressive promoter
> calculations without substantiating the §41(d) four-part test.
> Improperly-claimed credits trigger §6662 accuracy penalties.
> Practitioners must require contemporaneous nexus documentation.

## Overview

§41 incentivizes business expenditures on qualified research. The
credit (20% of QREs above base, or simplified 14% / 6% under
Alternative Simplified Credit) offsets income tax. For qualifying
small businesses, §41(h) allows the credit to offset payroll taxes
(up to $500,000) for businesses with gross receipts under $5M and
within their first 5 years.

§174 capitalization (post-TCJA): TCJA effective 2022 eliminated
current deduction of R&E. Domestic R&E capitalized over 5 years;
foreign R&E over 15 years; software development treated as R&E.

OBBBA reportedly restored current expensing of domestic R&E.
Verify via Classification Tables — consequential restoration if
confirmed.

## Primary IRC authority

- §41 — Credit for increasing research activities.
- §41(b) — QREs: wages, supplies, contract research (65%).
- §41(c) — Base amount.
- §41(c)(5) — Alternative Simplified Credit.
- §41(d) — Qualified research definition (four-part test).
- §41(h) — Payroll tax election (qualified small business).
- §174 — R&E expenditures (post-TCJA capitalization).
- §280C(c) — Reduction of §174 deduction by amount of credit.

## Treasury regulations

- Reg §1.41-1 through §1.41-9.
- Reg §1.41-4 — Qualified research definition.
- Reg §1.41-2 — Qualified research expenses.

## Key IRS guidance

- Notice 2023-63 — §174 post-TCJA procedural guidance.
- Rev. Proc. 2023-11 — §174 accounting method change.
- Rev. Proc. 2023-8 — §174 software development.
- LB&I R&D Audit Roadmap — IRS audit approach.
- CCM 20214101F — R&D refund claim documentation.

## Key court decisions

- **Suder v. Commissioner, T.C. Memo. 2014-201** — Section 41
  documentation; nexus between wages and qualified research.
- **Trinity Industries, Inc. v. United States, 691 F. Supp. 2d 688
  (N.D. Tex. 2010)** — Qualified research project definition.
- **Geosyntec Consultants, Inc. v. United States, 776 F.3d 1330
  (11th Cir. 2015)** — Funded research exclusion.
- **Union Carbide Corp. v. Commissioner, T.C. Memo. 2009-50** —
  Process of experimentation.
- **Populous Holdings, Inc. v. Commissioner, T.C. Memo. 2019-118** —
  Architects qualifying for §41.

## Eligibility requirements

§41(d) four-part test for qualified research:
1. **Permitted purpose** — new or improved business component.
2. **Technological in nature** — physical/biological/engineering/CS.
3. **Process of experimentation** — systematic trial and error.
4. **Elimination of uncertainty** — capability/methodology/design.

Excluded under §41(d)(4): post-commercial-production research,
adaptation, duplication, surveys, internal-use software (limited),
funded research.

§41(h) payroll offset: gross receipts <$5M; no gross receipts >5
years before; election on Form 6765.

## Mechanics — how it works

1. **Identify qualified projects** satisfying four-part test.
2. **Identify QREs:** wages, supplies, 65% contract research,
   cloud/computer rental.
3. **Compute credit** — Regular (20%) or ASC (14%/6%).
4. **§280C(c) election.**
5. **Form 6765** with return.
6. **§41(h) payroll offset election** (Form 8974 quarterly).
7. **§174 capitalization** (5-year domestic / 15-year foreign).

## Documentation requirements

- Project documentation linking activities to four-part test.
- Time tracking by qualified project (contemporaneous).
- Wage allocation by project.
- Supply consumption records.
- Contract research agreements (risk allocation).
- Process of experimentation documentation.

## Common pitfalls / audit risks

- **Insufficient nexus documentation.** Most common audit failure.
- **Routine vs. qualified.** Established product development.
- **Internal-use software trap.** §41(d)(4)(E).
- **Funded research exclusion.** Risk-shifted contracts.
- **§41(h) eligibility.** Strict gross receipts/age limits.
- **§174 capitalization** mistakes post-TCJA.
- **R&D refund claim documentation** per CCM 20214101F.

## Recent legislative changes

- **TCJA (2017)** — §174 capitalization effective 2022.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §174 §41
  research expensing Pub L 119-21]`. Reports indicate restoration
  of current expensing for domestic R&E effective 2025+.

## State conformity considerations

State R&D credits independent. CA, PA, TX, NY, MA. State conformity
to §174 varies.

## AICPA SSTS / Circular 230 considerations

Heavily audit-targeted. Verify documentation; avoid promoter
estimates; recommend Form 8275 disclosure for borderline positions.

## Default confidence band rationale

**MODERATE** — well-established but heavily fact-driven. HIGH only
with rigorous contemporaneous documentation.

## Cross-references

- `predict-r-and-d-credit` (predict skill).
- `misc-tax-credits` (#38).
- `income-shifting-to-c-corp` (#47).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 41","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section41","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 174","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section174","weight":"primary_statute"},
    {"authority_type":"TreasReg","citation":"Treas. Reg. § 1.41-4","url":"https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1","weight":"regulation"},
    {"authority_type":"Notice","citation":"Notice 2023-63","url":"https://www.irs.gov/irb","weight":"irs_published"},
    {"authority_type":"TaxCt","citation":"Suder v. Commissioner, T.C. Memo. 2014-201","url":"https://www.ustaxcourt.gov","weight":"judicial"},
    {"authority_type":"CtAppeals","citation":"Geosyntec Consultants, Inc. v. United States, 776 F.3d 1330 (11th Cir. 2015)","url":"https://www.courtlistener.com","weight":"binding_circuit"}
  ]
}
```
