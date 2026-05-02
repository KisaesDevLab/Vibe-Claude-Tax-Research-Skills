---
name: tax-elections-library
description: |
  Reference library of 24 tax elections with authority, deadline,
  where-to-file, eligibility, mechanics, sample election language,
  and pitfalls. Covers formation (§351, late-C Rev. Proc. 2009-41,
  late-S Rev. Proc. 2013-30); individual (§83(b), §163(h)(3));
  capitalization (§266, de minimis Reg. §1.263(a)-1(f), §179);
  passive (§469 grouping, REPS rental aggregation); partnership
  (§754); S corp (QSST, ESBT, §1377(a)(2), basis-reduction
  ordering, AAA ordering, §1362(d)(1) revocation, shareholder
  consent); decedent (§213(c), portability waiver); farm
  (§451(d), §451(e)). Use when the user asks "how to file §83(b)",
  "QSST language", "§754 sample", "late S election Rev. Proc.
  2013-30", "REPS aggregation", "de minimis safe harbor language",
  or any election deadline / attachment question. Use whenever
  the user asks for a tax election by name, IRC section, or
  Rev. Proc. number.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-elections-library — 24 elections with authority, deadlines, and sample language

## Read before output

Before producing any output, read in order:

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — when an OBBBA or other
   post-2024 statute may have modified an election.
6. `references/index.md` — the election index with election-code,
   slug, IRC section, and deadline at-a-glance.
7. The relevant `references/elections/<slug>.md` for the election
   in question.

## Coverage

24 elections in 8 parts:

| Part | Code | Election | Slug |
|---|---|---|---|
| A. Formation | A1 | §351 corporate formation filing attachment | `section-351-formation-attachment` |
| A. Formation | A2 | LLC late C-corp election (Rev. Proc. 2009-41) | `llc-late-c-corp-election` |
| A. Formation | A3 | S-corp late election (Rev. Proc. 2013-30) | `s-corp-late-election` |
| B. Individual | B1 | §83(b) restricted property | `section-83b-election` |
| B. Individual | B2 | §163(h)(3) "10-T" home equity as trade-or-business | `section-10t-home-equity` |
| C. Capitalization | C1 | §266 property tax / carrying-cost capitalization | `section-266-carrying-cost` |
| C. Capitalization | C2 | De minimis safe harbor (Reg. §1.263(a)-1(f)) | `de-minimis-safe-harbor-263a-1f` |
| C. Capitalization | C3 | §179 qualifying property reference | `section-179-qualifying-property` |
| D. Passive | D1 | §469 activity grouping (Reg. §1.469-4) | `section-469-grouping` |
| D. Passive | D2 | REPS rental aggregation (Reg. §1.469-9(g)(3)) | `reps-rental-aggregation` |
| E. Partnership | E1 | §754 step-up | `section-754-step-up` |
| F. S Corp | F1 | S-corp elections master grid | `s-corp-elections-master-grid` |
| F. S Corp | F2 | QSST election (§1361(d)(2)) | `qsst-election` |
| F. S Corp | F3 | ESBT election (§1361(e)(3)) | `esbt-election` |
| F. S Corp | F4 | §1377(a)(2) closing-of-books | `section-1377a2-closing-of-books` |
| F. S Corp | F5 | Reg. §1.1367-1 basis-reduction ordering | `reg-1367-1-basis-reduction-ordering` |
| F. S Corp | F6 | Reg. §1.1368-1(f)(2) E&P-before-AAA | `reg-1368-1f2-ep-before-aaa` |
| F. S Corp | F7 | Reg. §1.1368-1(f)(3) deemed dividend | `reg-1368-1f3-deemed-dividend` |
| F. S Corp | F8 | §1362(d)(1) corporate revocation | `s-corp-revocation` |
| F. S Corp | F9 | Shareholder consent to revocation | `shareholder-consent-revocation` |
| G. Decedent / Estate | G1 | §213(c) decedent medical on Form 1040 | `section-213c-decedent-medical` |
| G. Decedent / Estate | G2 | Portability election waiver (§2010(c)(5)(A)) | `portability-waiver` |
| H. Farm | H1 | §451(d) defer crop insurance proceeds | `section-451d-crop-insurance` |
| H. Farm | H2 | §451(e) defer forced livestock sale proceeds | `section-451e-forced-livestock` |

## Workflow

### 1. Intake

- `election_query`: by code (e.g., "F4"), by slug, by IRC section
  ("§83(b)"), by Rev. Proc. number ("2013-30"), or by topic ("how
  do I aggregate rentals as a real estate professional").
- `transaction_facts`: enough to determine eligibility and
  applicable deadline (e.g., date of property transfer for §83(b);
  date of S-corp formation for late-S relief; tax year for §754
  partnership step-up).
- `taxpayer_state`: for state-conformity flags (CA / NY / MA / NJ
  bonus and §179 non-conformity affects C2, C3; state portability
  rules vary for G2).

### 2. Election lookup

Match the query to a slug per `references/index.md`. Load
`references/elections/<slug>.md`. If multiple elections plausibly
apply (e.g., an S corp formed late wants both A2 and A3 on the
table), surface all candidates and walk each.

### 3. Deadline + relief check

Election deadlines are typically strict. **§9100 relief** under
Reg. §301.9100-1 et seq. is sometimes available for regulatory
elections but rarely for statutory ones. Identify whether the
relevant election is statutory (no §9100 relief) or regulatory
(possible §9100 relief), and surface the requirements (good faith;
no prejudice to the government).

Specific reliefs to surface:

- **A2 — LLC late C-corp**: Rev. Proc. 2009-41 (3 years 75 days
  after intended effective date).
- **A3 — S-corp late**: Rev. Proc. 2013-30 (3 years 75 days; one
  combined election covers Form 2553 + late QSST/ESBT + late
  classification).
- **B1 — §83(b)**: 30 days, jurisdictional, no §9100 relief.
- **D1 / D2 — §469**: regulatory; §9100 relief may be available
  for Reg. §1.469-9(g) aggregation late filings (Rev. Proc.
  2011-34 procedure).
- **E1 — §754**: regulatory; §9100 relief frequently granted.

### 4. Sample election language

Reproduce the sample language from the relevant election file.
Customize for the taxpayer's facts; do NOT silently alter
substantive language.

### 5. Where to file

State the precise filing destination (with return; separate to
service center; both). For elections with attach-to-return
mechanics, identify the form line or attachment statement number
where applicable.

### 6. Conclusion + JSON sidecar

Markdown conclusion: deadline, where to file, sample language
attached, eligibility result, confidence band (typically HIGH for
straight statutory / regulatory elections; MODERATE if relying on
§9100 relief or an unsettled facts pattern). JSON sidecar
validates against `shared/output-schema.json`.

## Hard rules

- Never assert §9100 relief is available without identifying the
  specific authority granting it (the regulation, Rev. Proc., or
  PLR — and PLRs have no precedential value to other taxpayers
  under §6110(k)(3)).
- Never alter the substantive sample election language. Customize
  identifiers (taxpayer name, FEIN, transfer date, valuation) but
  preserve the operative election statement verbatim.
- For B1 (§83(b)), the 30-day deadline is jurisdictional. Late
  filing voids the election; surface this prominently.
- For F1 (S-corp master grid), distinguish elections that require
  shareholder consent from those that the corporation makes alone.
- For state implications, route to `tax-research-state-income`
  (e.g., CA does not conform to §179 / bonus depreciation
  acceleration; CA portability has no equivalent because no
  estate tax in 2025).
- If the election is materially affected by a recent Public Law
  (TCJA, SECURE 2.0, OBBBA), use `shared/legislation-tracking.md`
  to verify current authority via the Classification Tables before
  reproducing sample language.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`.
