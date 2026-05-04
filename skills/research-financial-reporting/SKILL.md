---
name: research-financial-reporting
description: |
  General FASB Accounting Standards Codification (ASC) research
  skill. Routes by ASC Topic family (200 Presentation, 300 Assets,
  400 Liabilities, 500 Equity, 600 Revenue, 700 Expenses, 800 Broad
  Transactions, 900 Industry). Walks ASC 105-10 hierarchy
  (authoritative vs. non-authoritative). Routes income-tax accounting
  to research-asc-740 and revenue/leases to research-asc-606-842.
  Routes GASB (governmental), IFRS, and PCAOB (issuer) externally.
  Use when the user asks "ASC", "FASB", "GAAP research", "financial
  reporting", "ASU", "EITF", "Concepts Statement", "ASC 250 change
  in estimate", "ASC 805 business combinations", "ASC 350 goodwill
  impairment", "ASC 326 CECL", or "book-tax difference" (when GAAP
  side dominates). Make sure to use this skill whenever the user
  mentions GAAP, ASC, FASB, ASU, financial reporting, or any ASC
  topic by number that isn't 740 / 606 / 842.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# research-financial-reporting — FASB ASC research (general)

Mirrors the `tax-research-federal` shape but for U.S. GAAP. Walks
the ASC hierarchy (Topic → Subtopic → Section → Subsection,
e.g., ASC 805-10-25-15), tracks ASUs and effective dates, flags
non-authoritative sources, and routes high-volume topics to
sibling skills.

## Read before output

1. `shared/citation-discipline.md` — authority_domain: gaap.
2. `shared/authority-hierarchy.md` — GAAP authority subsection
   (Phase 9): `gaap_codified` vs `gaap_non_authoritative`.
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — GAAP research scaffolding module.
5. `references/asc-topic-map.md` — ASC topic-to-skill routing.
6. `references/asc-105-hierarchy.md` — ASC 105 GAAP hierarchy
   (authoritative vs. non-authoritative).
7. `references/asu-effective-dates.md` — ASU tracking workflow.
8. `references/gasb-ifrs-pointers.md` — out-of-scope external
   pointers.

## Operative authority

- FASB Accounting Standards Codification:
  https://asc.fasb.org (Basic View free with registration;
  Professional View paid).
- ASUs: https://www.fasb.org/page/PageContent?pageId=/standards/accounting-standards-updates-issued.html
- Concepts Statements (non-authoritative per ASC 105-10-05-2):
  https://www.fasb.org/page/PageContent?pageId=/standards/concepts-statements.html
- Cite ASC content as `authority_domain: gaap`,
  `authority_type: FASB_ASC`, `weight: gaap_codified`. ASUs cite
  to ASC location for codified content; the ASU itself is the
  issuance vehicle.

## Workflow

### 1. Intake

- `entity_type`: nonissuer (typical for this pack) | issuer
  (route to PCAOB for audit; GAAP itself still applies) |
  governmental (route to GASB externally) | nonprofit (ASC
  applies; specific industry topics in ASC 958)
- `framework`: U.S. GAAP | private-company alternatives (PCC) |
  IFRS (route externally)
- `asc_topic`: e.g., "805 business combinations", "350 goodwill",
  "250 change in estimate"
- `tax_year` / `fiscal_year_end`: integer (drives ASU effective-
  date analysis)
- `issue`: free text
- `book_tax_difference_implicated`: yes (route to research-asc-740
  for the tax accrual side) | no

### 2. Out-of-scope routing

- **Governmental entity**: GASB Codification governs
  (https://gars.gasb.org). ASC does NOT apply. Out of scope here.
- **IFRS reporter**: IFRS Foundation (https://www.ifrs.org). Out
  of scope.
- **PCAOB / issuer audit**: PCAOB AS standards govern audit, not
  GAAP itself. ASC still applies for the F/S; route audit
  questions to PCAOB externally.

### 3. ASC 105 hierarchy (apply to every citation)

ASC 105-10 (the "Generally Accepted Accounting Principles" topic)
establishes that ASC is the **single source** of authoritative
U.S. GAAP for non-governmental entities.

- **Authoritative**: ASC content (post-2009 codification);
  pre-2009 EITF / SFAS / SOP / TPB / SEC SAB (only those carried
  forward into ASC verbatim or by reference).
- **Non-authoritative** (per ASC 105-10-05-2):
  - FASB Concepts Statements (CON 1–8).
  - AICPA Technical Practice Aids (TPAs) NOT codified into ASC.
  - SEC SAB cited for nonissuers (persuasive only).
  - Industry / accounting textbooks.
  - Pronouncements of other standard-setters in different
    contexts (e.g., GASB, IFRS).

### 4. Topic routing

Walk `references/asc-topic-map.md`:
- **740 Income Taxes** → route to `research-asc-740`.
- **606 Revenue / 842 Leases** → route to `research-asc-606-842`.
- **205 Presentation / Going concern (205-40)** → here; AU-C 570
  audit-side from `compliance-sas-audit`.
- **250 Accounting Changes / Errors** → here.
- **326 CECL** → here (deferred from sibling skill in Phase 10).
- **350 Intangibles / Goodwill** → here.
- **450 Contingencies** → here.
- **805 Business Combinations / 810 Consolidation** → here.
- **815 Derivatives / 820 Fair Value** → here.
- **825 Financial Instruments / 830 Foreign Currency** → here.
- **958 Not-for-Profit** → here (ASC 958 specific subtopics).
- All other ASC topics → here.

### 5. ASU effective-date verification

Before stating any ASC rule as current:
- Identify the ASU(s) that have amended the relevant subsection.
- Verify the effective date for the entity (public business
  entity vs. all other entities; calendar-year vs. fiscal-year).
- Check early-adoption permitted / required / not permitted.
- Cite the post-amendment ASC location, NOT the pre-amendment
  ASC or the ASU itself.

Walk `references/asu-effective-dates.md`.

### 6. Disclosure requirements

Most ASC topics include a disclosure subtopic (ASC X-X-50). Walk
the disclosure requirements separately from recognition /
measurement and ensure all required disclosures are surfaced.

### 7. Conclusion

State the GAAP conclusion: recognition, measurement, presentation,
disclosure. Note any non-authoritative sources used (Concepts
Statements, AICPA TPAs cited persuasively).

Confidence band per `shared/confidence-bands.md`. ASC questions
typically land HIGH (clear codified rule) or MODERATE (judgment-
heavy area like fair-value Level 3, going concern, contingencies).
LOW band for novel transactions or where ASUs are recent and
practice is still developing.

### 8. JSON sidecar

`authority_domain: gaap` for ASC citations.
`verification_checklist_gaap` populated.

## Hard rules

- Never cite a Concepts Statement (CON) as authoritative —
  `gaap_non_authoritative` always (per ASC 105-10-05-2).
- Never cite SEC SAB as authoritative for a nonissuer (persuasive
  only).
- Never apply GASB to a non-governmental entity.
- Never apply IFRS to a U.S. GAAP reporter (unless the entity
  has elected dual reporting).
- Always verify effective dates of relevant ASUs before stating
  current law.
- Always identify disclosure requirements separately from
  recognition / measurement.
- Always cite to the codified ASC location, not the ASU or
  pre-codification SFAS / EITF / SOP.
- Never claim Chevron or Skidmore deference for ASC (no Chevron
  analog applies to FASB).

## Verification checklist (appendix)

End the markdown response with the GAAP research scaffolding
module from `shared/compliance.md` (ASC topic confirmed; ASUs
through effective date verified; disclosure requirements
identified; non-authoritative sources flagged).
