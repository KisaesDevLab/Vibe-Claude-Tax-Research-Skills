---
name: predict-r-and-d-credit
description: |
  Predicts whether claimed activities qualify for the IRC §41
  research credit by applying the four-part test (§41(d)(1)),
  computing qualified research expenses (QREs) under §41(b),
  selecting the regular vs. alternative simplified credit (ASC)
  method, and surfacing the §174 capitalization interaction
  (post-TCJA / OBBBA). Use when the user asks "do I qualify for
  R&D credit", "§41 research credit", "four-part test", "QRE",
  "qualified research expense", "ASC", "alternative simplified
  credit", "§174 R&E capitalization", "amortization of R&E",
  or "§280C reduced credit". Make sure to use this skill whenever
  the user mentions §41, R&D credit, R&E expenditures, or §174
  capitalization.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-r-and-d-credit — §41 research credit

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA Pub. L. 115-97 §13206
   amended §174 effective for tax years beginning after 2021
   (capitalization-and-amortization regime); subsequent legislation
   (CHIPS Act, OBBBA) altered §174 amortization periods. Verify
   the year-specific posture via Classification Tables.
6. `references/four-part-test.md` — §41(d) qualifying-activity
   tests, §41(b) QRE rules, ASC computation.

## Operative authority

- IRC §41 — research credit.
- IRC §41(d)(1) — four-part test for "qualified research".
- IRC §41(b) — qualified research expenses (wages, supplies,
  contract research, computer leasing).
- IRC §174 — research and experimental expenditures (capitalization
  and 5-year domestic / 15-year foreign amortization post-TCJA;
  OBBBA / CHIPS modifications to be verified).
- IRC §280C(c) — election to reduce credit to avoid §174 deduction
  add-back.
- Treas. Reg. §1.41-1 through §1.41-9 — comprehensive regulatory
  framework.
- United States v. McFerrin, 570 F.3d 672 (5th Cir. 2009) —
  business-component-by-business-component documentation.
- Suder v. Commissioner, T.C. Memo. 2014-201 — recordkeeping
  expectations.
- Union Carbide Corp. v. Commissioner, 697 F.3d 104 (2d Cir.
  2012) — process-of-experimentation rigor.
- Notice 2024-14 — §174 implementation Q&A; Rev. Proc. 2023-11
  for §174 method changes.

## Workflow

### 1. Intake

- `tax_year`
- `industry`: software, manufacturing, biotech, food science, etc.
- `claimed_activity_descriptions`: per business component (per §41(d)
  the four-part test applies at the business-component level)
- `qre_categories`: in-house wages, supplies, contract research
  (§41(b)(3)), basic-research payments
- `gross_receipts_history`: needed for ASC base period (prior 3
  years)
- `prior_credit_methodology`: regular method or ASC; controlled-group
  considerations
- `software_self_developed`: triggers §41(d)(4)(E) internal-use-
  software exclusion unless §1.41-4(c)(6) tests met
- `funded_research_facts`: §41(d)(4)(H) excludes funded research
  unless taxpayer retains substantial rights AND bears financial
  risk

### 2. Four-part test (§41(d)(1))

Each business component must satisfy ALL four:

1. **§174 expenditure** — qualifies as research and experimental
   expenditure.
2. **Technological in nature** — relies on principles of physical,
   biological, engineering, or computer sciences (§41(d)(1)(B)(i)).
3. **Process of experimentation** — substantially all activities
   involve evaluating one or more alternatives through systematic
   trial and error (§41(d)(1)(C)).
4. **Permitted purpose** — relates to a new or improved business
   component's function, performance, reliability, or quality
   (§41(d)(1)(B)(ii)).

Excluded categories (§41(d)(4)):
- Research after commercial production.
- Adaptation of existing business component.
- Duplication of existing business component.
- Surveys, studies, market research, advertising, management
  studies.
- Computer-software development for internal use (with §1.41-4(c)(6)
  carve-out for high-threshold-of-innovation tests).
- Research conducted outside the United States, Puerto Rico, or
  any U.S. possession (§41(d)(4)(F)).
- Research in the social sciences, arts, or humanities.
- Funded research (§41(d)(4)(H)) — funded by another person if
  taxpayer does not retain substantial rights AND does not bear
  financial risk.

### 3. QRE categories (§41(b))

- **In-house research expenses**: wages for qualified services
  (engaging in qualified research, directly supervising, directly
  supporting); supplies used or consumed in the conduct of
  qualified research; computer leasing for qualified research.
- **Contract research expenses (§41(b)(3))**: 65% of the amount
  paid to a non-employee for qualified research (75% for "qualified
  research consortium" payments; 100% for prepaid contract amounts
  in narrow circumstances).
- **Basic research payments (§41(b)(1)(B)(ii))**: Payments to
  qualified universities and other qualified organizations.

Wages must be allocable to qualified services. The "substantially
all" rule of §1.41-2(c) deems all of an employee's wages qualified
if at least 80% of services are qualified.

### 4. Methodology — Regular vs. ASC

**Regular method (§41(a)(1))**: 20% of QREs in excess of base
amount. Base amount = fixed-base percentage × average annual
gross receipts of prior 4 years; minimum of 50% of current-year
QREs. Fixed-base percentage frozen at 1984-1988 level for taxpayers
in existence then; rebuttable presumption for "start-up" taxpayers.

**Alternative Simplified Credit (§41(c)(4))**: 14% of QREs in
excess of 50% of average QREs for the prior 3 years. If no QREs
in any of the 3 prior years, ASC = 6% of current-year QREs.

ASC is generally preferred for taxpayers without long fixed-base
percentage history, taxpayers in growing industries, or taxpayers
who lack 1984-1988 records.

### 5. §280C(c) reduced credit election

Default rule: §174 deduction is reduced by the amount of the
research credit (preventing double benefit). The §280C(c)(2)
election allows the taxpayer to take a REDUCED credit instead:
- Reduced credit = credit × (1 − maximum corporate rate).
- For a 21% corporate rate, reduced credit = credit × 0.79.

The election is made on a timely-filed (with extensions) original
return. Cannot be made on an amended return or via §301.9100
relief except in limited circumstances.

### 6. §174 capitalization interaction (post-TCJA)

Tax years beginning after 12/31/2021: §174 R&E expenditures must
be capitalized and amortized:
- 5 years for domestic R&E.
- 15 years for foreign R&E.

The §41 research credit is generally favorable post-TCJA because:
- §41 base computation is unaffected by §174 amortization rules
  (QREs are still computed in the year incurred).
- §41 credit value is enhanced relative to the now-amortized §174
  deduction.

OBBBA (Pub. L. 119-XX, 2025) modified §174 — verify the current-
year posture via shared/legislation-tracking.md. Check whether
the OBBBA reverted to immediate expensing for domestic R&E or
modified the amortization period.

### 7. Documentation requirements

§41 credit claims face heightened scrutiny:
- Form 6765 with detailed QRE breakdown.
- Project / business-component-by-business-component documentation
  (per McFerrin, Suder).
- Contemporaneous records of process-of-experimentation steps
  (hypothesis, test plan, outcome, iteration).
- Time-tracking by employee for the substantially-all rule.
- Schedule of contract-research payments and 65% / 75% / 100%
  classification.

The IRS issued FAQ 25 (2022) requiring expanded documentation in
amended-return claims (5 items required for refund claims based on
research credit).

### 8. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: clear technological / process-of-experimentation activities;
  contemporaneous documentation; ASC applied; §280C election made.
- MODERATE: documentation gaps; some activities may be excluded
  (internal-use software, market research, adaptation).
- LOW: poor documentation; amended-return claim subject to FAQ 25
  scrutiny; activities resemble engineering or software development
  without process-of-experimentation discipline.
- SPECULATIVE: claimed activities largely fall in §41(d)(4)
  exclusions; no contemporaneous records.

### 9. Authorities + sidecar

Cite §41, §174, §280C, relevant Treas. Regs., and case law. JSON
sidecar validates against `shared/output-schema.json`. For
post-TCJA / OBBBA posture, populate `public_laws_consulted[]`.

## Hard rules

- Always apply the four-part test BUSINESS-COMPONENT-BY-BUSINESS-
  COMPONENT (not at the project or company level).
- Always check §41(d)(4) exclusions (internal-use software,
  funded research, foreign location, etc.).
- Drop one band when documentation is reconstructive.
- Drop one band when amended-return claim is involved (FAQ 25
  scrutiny).
- §41(d)(4)(F) foreign-research exclusion is statutory; no Reg
  override.
- Never claim Chevron deference for Treas. Reg. §1.41-4 or §1.174-2.
- Verify current-year §174 posture before stating amortization
  periods.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. ALWAYS include the negative-treatment-
review residual practitioner responsibility for §41 work given
the IRS's FAQ 25 enforcement posture and the magnitude of typical
credit claims.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
