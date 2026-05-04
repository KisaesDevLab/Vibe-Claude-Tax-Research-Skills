---
name: compliance-attestation-qm
description: |
  Walks AICPA AT-C attestation standards (SSAE) and the firm-level
  quality-management standards (SQMS 1, SQMS 2, A-QM). Routes
  between AT-C 105 (common concepts), AT-C 205 (examination), AT-C
  210 (review), AT-C 215 (agreed-upon procedures), and AT-C 320
  (SOC 1) / AT-C 205 (SOC 2 / SOC 3). Implements SQMS 1 firm-level
  quality-management risk assessment and SQMS 2 engagement quality
  reviews. Use when the user asks "SOC 1", "SOC 2", "Type 1", "Type
  2", "AT-C", "SSAE", "examination engagement", "agreed-upon
  procedures", "AUP", "SQMS 1", "SQMS 2", "engagement quality
  review", "EQR", "quality management", or "firm-level QM". Make
  sure to use this skill whenever the user mentions SOC, AT-C,
  SSAE, attestation engagements, AUP, examination, or quality
  management standards.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# compliance-attestation-qm — Attestation engagements + firm QM

Walks AICPA Statements on Standards for Attestation Engagements
(SSAE / AT-C clarified format) and the firm-level Statements on
Quality Management Standards (SQMS). PCAOB attestation standards
(issuer-related) are out of scope; this skill routes externally
when needed.

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md` — Professional Standards subsection.
3. `shared/confidence-bands.md`
4. `shared/compliance.md` — engagement-letter required-elements +
   AICPA Code modules.
5. `references/at-c-105-common.md` — common concepts across all AT-C
   engagements (independence, engagement letter, criteria, evidence,
   reporting).
6. `references/at-c-205-examinations.md` — examination engagements
   (highest assurance under AT-C); used for SOC 2 reports.
7. `references/at-c-soc-engagements.md` — SOC 1 (AT-C 320), SOC 2,
   SOC 3 — service organization reporting.
8. `references/sqms-1-firm-qm.md` — firm system of quality
   management.
9. `references/sqms-2-engagement-quality-review.md` — engagement
   quality reviews.

## Operative authority

- AICPA SSAE (AT-C currently effective):
  https://www.aicpa-cima.com/resources/download/aicpa-ssaes-currently-effective
- SQMS 1: https://www.aicpa-cima.com/resources/download/sqms-no-1-a-firm-s-system-of-quality-management
- SQMS 2: https://www.aicpa-cima.com/resources/download/sqms-no-2-engagement-quality-reviews
- Cite as `authority_domain: professional_conduct`,
  `authority_type: AICPA_SSAE` (for AT-C) or `AICPA_SQMS` (for
  SQMS), `weight: binding_on_member`.

## Workflow

### 1. Intake

- `engagement_type`: examination | review | agreed-upon procedures
  (AUP) | SOC 1 | SOC 2 | SOC 3 | direct-examination | quality
  management (firm-level)
- `subject_matter`: e.g., internal control over financial
  reporting, controls at a service organization, sustainability /
  ESG metrics, compliance with specific criteria, etc.
- `criteria`: who established them; suitability and availability
- `entity_type`: nonissuer (this skill) | issuer (route to PCAOB)
- `independence_status`: independent (required for examination /
  review) | not independent (AUP only, with disclosure)
- `firm_qm_question`: yes (route to SQMS 1 / 2 references) | no

### 2. Issuer / governmental routing

If user mentions SOC for SEC issuer purpose / public-company
internal control over financial reporting (ICFR) → route to PCAOB
externally.

### 3. AT-C 105 — common concepts

Walk `references/at-c-105-common.md`:
- Engagement letter required (AT-C §105 .A18).
- Criteria must be suitable and available to intended users.
- Independence required for examination and review (AT-C §105 .25);
  AUP may be performed without independence with required
  disclosure.
- Engagement evidence (sufficient, appropriate).
- Materiality applied as appropriate to the engagement.
- Documentation per AT-C 105 documentation rules.

### 4. Engagement-type routing

- **Examination** (highest level of assurance, "reasonable assurance")
  — AT-C 205. Walk `at-c-205-examinations.md`. SOC 2 examination
  reports use AT-C 205. SOC 1 uses AT-C 320 (which references AT-C
  205 mechanics).
- **Review** (limited assurance) — AT-C 210. Less common in
  practice than examinations.
- **Agreed-upon procedures (AUP)** — AT-C 215. The practitioner
  performs only those specific procedures the client and intended
  users have agreed to. Findings are reported; NO opinion or
  conclusion. Independence is NOT required (with disclosure).
- **Direct examination** — examination where the practitioner
  measures or evaluates the underlying subject matter against the
  criteria, without management's measurement. AT-C 205.

### 5. SOC engagements

- **SOC 1** (Service Organization Control 1) — controls at a
  service organization relevant to user entities' ICFR. AT-C 320.
  Output: Type 1 (description and design as of a point in time)
  or Type 2 (description, design, and operating effectiveness over
  a period).
- **SOC 2** — controls at a service organization relevant to
  Trust Services Criteria (security, availability, processing
  integrity, confidentiality, privacy). AT-C 205. Type 1 or Type 2.
- **SOC 3** — public-use general report on Trust Services
  Criteria. Less detailed than SOC 2.

### 6. SQMS engagement-quality questions

If `firm_qm_question = yes`:
- SQMS 1 — firm system of quality management (firm-level risk
  assessment, governance, ethics, acceptance/continuance, engagement
  performance, resources, information/communication, monitoring/
  remediation). Implementation deadline December 15, 2025.
- SQMS 2 — engagement quality reviews. Required for all audit and
  certain attest engagements when SQMS 1 risk assessment indicates
  it. EQR objective and process distinct from EQR's role under
  prior standards.

### 7. Conclusion

State the engagement-type confirmation, required procedures,
expected report wording (by reference to AT-C illustrative examples
or AICPA SOC guides), and any SQMS-1 firm-level implications.

Confidence band per `shared/confidence-bands.md`. Most attestation-
standards conclusions land HIGH or MODERATE. LOW band when criteria
suitability is uncertain or when the engagement falls between
attestation types.

### 8. JSON sidecar

`authority_domain: professional_conduct`,
`verification_checklist_engagement` populated, plus
`verification_checklist_aicpa_code` if independence threats were
evaluated.

## Hard rules

- Never apply PCAOB attestation standards in this skill — route
  externally.
- Never permit an AT-C 205 examination or AT-C 210 review without
  independence.
- For AUP (AT-C 215) without independence, the AUP report must
  state lack of independence.
- Always confirm criteria suitability before accepting any AT-C
  engagement (AT-C §105 establishes criteria-suitability
  requirements).
- Never claim Chevron or Skidmore deference for AT-C / SQMS
  standards.
- Never let an AICPA Practice Aid drive the closest-authority
  citation; always cite the AT-C or SQMS section directly.

## Verification checklist (appendix)

End the markdown response with the engagement-letter required-
elements module + AICPA Code module from `shared/compliance.md`.
