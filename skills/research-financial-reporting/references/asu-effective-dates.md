# ASU effective-date workflow

Before stating any ASC rule as current law, verify which ASUs
have amended the relevant subsection and confirm effective dates
for the entity.

## Step-by-step workflow

### 1. Identify the relevant ASC subsection

Pin-cite to ASC TTT-SS-SS-SS (e.g., ASC 606-10-25-1).

### 2. Identify ASUs that have amended that subsection

Visit the ASU index:
https://www.fasb.org/page/PageContent?pageId=/standards/accounting-standards-updates-issued.html

For the ASC topic in question, identify all ASUs issued and not
yet effective for the entity, plus all ASUs that have already
amended the topic.

### 3. Confirm effective date for the entity

ASUs typically have different effective dates for:
- **Public business entities (PBE)**: usually one-year-earlier
  effective date.
- **All other entities (private companies, NFPs, EBPs)**: usually
  one-year-later effective date.
- **SRCs (smaller reporting companies)**: align with PBE most
  often, but ASU may carve out a delayed effective date.
- **Investment companies**: separate effective dates in some
  ASUs.

Effective date typically expressed as:
- "Annual periods beginning after [DATE]" (calendar-year reporters
  apply for years starting on or after that date).
- "Interim periods within annual periods beginning after [DATE]."

Early adoption may be:
- Permitted (most ASUs allow early adoption).
- Required (rare).
- Not permitted (rare).

### 4. Cite the post-amendment ASC

After the ASU is effective for the entity, cite the post-amendment
ASC paragraph (the ASU's content has been codified into ASC). Do
NOT cite the ASU itself for the substantive rule.

If the ASU has not yet been adopted (early-adoption period):
- Cite the pre-amendment ASC for current period.
- Note in the analysis: "ASU [NUMBER] is effective for [PBE/non-
  PBE] for periods beginning after [DATE]; entity has not early
  adopted."

### 5. Verify with FASB ASC

The Codification at https://asc.fasb.org provides:
- Pending content boxes that show post-amendment text alongside
  current text during transition periods.
- Effective-date overlays.
- ASU cross-references.

### 6. Cite ASUs as the issuance vehicle (only when transitional)

When discussing a transition period or pending amendment:
- Cite the ASU number for context.
- Cite the ASC paragraph as the substantive rule.
- Tag the ASU as `authority_type: FASB_ASU`,
  `authority_domain: gaap`, `weight: gaap_codified` (because the
  ASU content is the codified rule, just at a future effective
  date).

## Recently issued ASUs of broad interest (illustrative)

This is an illustrative list, NOT authority. Verify current status
at the FASB ASU index.

- **ASU 2023-06** (Disclosures — Codification Improvements based
  on SEC's S-K disclosure requirements) — implementation in
  recent year ends.
- **ASU 2023-07** (Segment Reporting — Improvements to Reportable
  Segment Disclosures) — effective for PBE annual periods after
  Dec. 15, 2023, interim after Dec. 15, 2024.
- **ASU 2023-08** (Crypto Assets) — effective for fiscal years
  beginning after Dec. 15, 2024.
- **ASU 2023-09** (Income Taxes — Disclosures) — effective for
  PBE Dec. 15, 2024, all other entities Dec. 15, 2025.
- **ASU 2024-01** (Stock Compensation — Profits Interest Awards) —
  effective for PBE Dec. 15, 2024.
- **ASU 2024-03** (Income Statement — Reporting Comprehensive
  Income — Disaggregation of Income Statement Expenses, "DISE")
  — effective for PBE annual after Dec. 15, 2026.
- **ASU 2024-04** (Debt — Induced Conversions of Convertible Debt)
  — effective for PBE Dec. 15, 2025.
- **ASU 2025-01** through ASU 2025-XX (current year ASUs to be
  verified at retrieval time).

## Documentation in research output

When the ASU effective-date analysis is material to the conclusion,
document:
- The relevant ASUs identified.
- The entity's reporter classification (PBE / non-PBE).
- The effective date(s) and whether the entity has adopted /
  is required to adopt / has elected to early-adopt.
- The transition method (full retrospective, modified retrospective,
  prospective).
- Disclosure of the change required by ASC 250 if a change in
  accounting principle.

## Cross-references

- ASC 250 (Accounting Changes): codifies the requirement to
  disclose accounting principle changes.
- ASC 105 hierarchy: confirms ASC is the source; ASUs are issuance
  vehicles.
- AICPA SAS (audit-side adoption considerations): route to
  `compliance-sas-audit` for SAS 145 risk-of-material-misstatement
  considerations regarding new accounting standards.

## Authority

- Cite the post-amendment ASC paragraph as
  `authority_type: FASB_ASC`, `weight: gaap_codified`.
- Cite the ASU as `authority_type: FASB_ASU`,
  `weight: gaap_codified` (issuance, not separate authority).
