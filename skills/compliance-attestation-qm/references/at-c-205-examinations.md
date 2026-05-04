# AT-C §205 — Examination Engagements

AT-C §205 governs examination engagements (the highest assurance
level under SSAE — "reasonable assurance"). Used for SOC 2
examination reports and many other attestations on internal
control, compliance, sustainability metrics, etc.

## Engagement objectives (AT-C §205 .10)

To express an opinion on whether:
- The subject matter is fairly stated, in all material respects,
  in accordance with (or based on) the criteria. OR
- The responsible party's assertion regarding the subject matter
  is fairly stated, in all material respects.

## Engagement preconditions

Per AT-C §105 .25:
- Criteria suitable and available.
- Independence (required for examination).
- Practitioner competence.
- Agreement on terms.

Plus AT-C §205 specific:
- Responsible party agrees to provide its written assertion to the
  practitioner (where applicable).
- Practitioner expects to obtain sufficient evidence.

## Required procedures (AT-C §205 .15+)

### Risk assessment
- Identify and assess risks of material misstatement of the subject
  matter.
- Consider control environment and design of controls relevant to
  the engagement objectives.

### Audit-like procedures
- Inquiry, observation, inspection, recalculation, confirmation.
- Tests of controls when the engagement plans rely on operating
  effectiveness (Type 2 reports).
- Substantive procedures responsive to assessed risks.

### Materiality
- Applied to the subject matter:
  - For financial-control examinations (e.g., ICFR): financial
    statement materiality.
  - For non-financial subject matter (SOC 2 trust services
    criteria): qualitative materiality reflecting user-entity
    needs.

### Evidence sufficiency and appropriateness
- Practitioner evaluates whether the evidence obtained provides
  reasonable assurance for the opinion.
- Insufficient evidence → scope limitation → modify opinion or
  withdraw.

## Reporting (AT-C §205 .60+)

### Standard examination report (illustrative)

Two formats:
1. **Direct opinion** — practitioner expresses opinion directly on
   the subject matter (whether subject matter is fairly stated,
   etc.).
2. **Opinion on the assertion** — practitioner expresses opinion on
   whether responsible party's assertion is fairly stated (still
   provides reasonable assurance, but the assertion is the
   intermediate step).

The choice depends on the engagement. SOC 1 and SOC 2 examinations
typically use the assertion-based format because management's
description and assertion are central artifacts.

### Modified opinions (AT-C §205 .65–.A88)

- **Qualified opinion** — material misstatement in the subject
  matter / assertion OR scope limitation, but effect not
  pervasive.
- **Adverse opinion** — material AND pervasive misstatement.
- **Disclaimer of opinion** — scope limitation that is material AND
  pervasive, OR multiple uncertainties precluding opinion.

### Restrictions on use
- Examination reports may be restricted-use (only specified parties
  may rely on them) when subject matter or criteria are tailored to
  specific users (e.g., a SOC 1 examination report typically
  restricts use to user entities and their auditors).

## Subsequent events (AT-C §205 .35)

Inquire about events between the date of the subject matter and
the date of the report. Modify subject matter / report if a
material event has occurred.

## Written representations (AT-C §205 .55)

Written representations from the responsible party covering:
- The subject matter and the assertion.
- Completeness of information provided.
- Fraud or suspected fraud known to management.
- Compliance with criteria.
- Subsequent events.

## Documentation (AT-C §205 .80)

- Engagement letter and assertion.
- Risk assessment.
- Procedures performed.
- Evidence obtained.
- Conclusions and rationale.
- Communications with responsible party / engaging party / governance.

## Cross-references

- Common concepts: `at-c-105-common.md`.
- SOC 1 / SOC 2: `at-c-soc-engagements.md`.
- Independence: route to `compliance-aicpa-code`.
- Group and component examinations: AT-C §205 plus group-audit
  analogues from AU-C §600 (reference only).

## Authority

Cite from AICPA SSAE currently-effective. AT-C §205. Pin-cite to
specific paragraph. Tag `authority_domain: professional_conduct`,
`authority_type: AICPA_SSAE`, `weight: binding_on_member`.
