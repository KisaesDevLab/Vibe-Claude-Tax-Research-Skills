# AT-C §105 — Common Concepts for Attestation Engagements

AT-C §105 establishes common concepts that apply to all
attestation engagements (examinations, reviews, agreed-upon
procedures) under SSAE.

## Definitions (AT-C §105 .10)

- **Subject matter** — the matter on which the practitioner is
  reporting (e.g., entity's internal control, sustainability
  metrics, compliance with a regulation).
- **Criteria** — the benchmarks used to measure or evaluate the
  subject matter.
- **Responsible party** — the party (usually management) who is
  responsible for the subject matter.
- **Engaging party** — the party that engages the practitioner.
  May be the responsible party or a third party.
- **Intended users** — the parties for whom the report is intended.

## Pre-conditions for an attestation engagement (AT-C §105 .25)

The practitioner must:
- Confirm that the criteria are suitable (relevance, objectivity,
  measurability, completeness).
- Confirm that the criteria are available to intended users.
- Confirm independence (for examination and review; AUP may be
  performed without independence with disclosure).
- Confirm engagement-team competence and capabilities.
- Obtain agreement on the terms of engagement.

If pre-conditions are not met → decline.

## Engagement letter (AT-C §105 .A18)

Required before the engagement begins. Must include:
- Objective and scope.
- Responsibilities of the practitioner (criteria, evidence,
  reporting).
- Responsibilities of the responsible party / engaging party
  (subject matter, internal control, providing evidence).
- Identification of the criteria.
- Reference to the form and content of the report.
- Statement of inherent limitations.
- Independence affirmation (or, for AUP, disclosure if not
  independent).
- Communication framework.

Cross-reference: `engagement-letter-library/references/letters/`
provides per-engagement-type templates including SOC 1, SOC 2, AUP.

## Suitable criteria (AT-C §105 .26)

Criteria are suitable when they are:
- **Relevant**: aligned with the subject matter and the engagement
  objective.
- **Objective**: capable of being applied with reasonable
  consistency by knowledgeable practitioners.
- **Measurable**: subject matter can be evaluated against them.
- **Complete**: all relevant factors that could affect the
  conclusions are addressed.
- **Available**: known and accessible to the intended users.

Examples of suitable criteria:
- COSO 2013 Internal Control Framework (for ICFR examinations).
- AICPA Trust Services Criteria 2017 (for SOC 2 / SOC 3).
- Established performance / sustainability frameworks (TCFD, GRI,
  ISSB, etc., depending on the engagement).
- Specific contractual provisions (for compliance attestations).

If criteria are unsuitable: decline (cannot perform an attestation
on insufficient criteria).

## Engagement evidence (AT-C §105 .29)

Sufficient appropriate evidence to support the practitioner's
opinion / conclusion / findings:
- Examinations: high level of assurance — extensive procedures.
- Reviews: limited assurance — less extensive procedures (inquiry
  + analytical typically).
- AUP: as agreed by the parties — only those procedures, no more.

## Materiality (AT-C §105 .31)

Materiality is applied to engagement subject matter as
appropriate. For ICFR examinations: financial-statement-level
materiality. For non-financial subject matter (controls at a
service organization for SOC 2 trust criteria): qualitative
materiality based on impact on intended users.

## Documentation (AT-C §105 .50)

- Engagement letter.
- Subject matter and criteria.
- Procedures performed (nature, timing, extent).
- Evidence obtained.
- Conclusions reached.
- Communications with management / governance / engaging party.

## Engagement-team independence (AT-C §105 .25 c)

- Examinations and reviews: independence per AICPA Code §1.200
  required.
- AUP: independence not required, but lack of independence must
  be disclosed in the AUP report.

Cross-reference: `compliance-aicpa-code` for threats-and-safeguards
analysis.

## Communications (AT-C §105)

- Engagement-team-level: communication of significant findings,
  consultations, governance matters.
- With responsible party: significant findings, scope changes,
  identified misstatements.
- With engaging party (if different): findings affecting their
  intended use of the report.

## Quality management (AT-C §105 + SQMS 1 / SQMS 2)

- Engagement performed within firm's SQMS 1 quality management
  system.
- Engagement quality review (EQR) under SQMS 2 when the firm's
  risk assessment indicates EQR is required.
- See `sqms-1-firm-qm.md` and `sqms-2-engagement-quality-review.md`.

## Cross-references

- Examinations: `at-c-205-examinations.md`.
- SOC engagements: `at-c-soc-engagements.md`.
- SQMS 1 firm-level: `sqms-1-firm-qm.md`.
- SQMS 2 EQR: `sqms-2-engagement-quality-review.md`.
- Independence: route to `compliance-aicpa-code`.

## Authority

Cite from AICPA SSAE currently-effective:
https://www.aicpa-cima.com/resources/download/aicpa-ssaes-currently-effective.
Tag `authority_domain: professional_conduct`,
`authority_type: AICPA_SSAE`, `weight: binding_on_member`. Pin-cite
to AT-C §105 paragraph.
