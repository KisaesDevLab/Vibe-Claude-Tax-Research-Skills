# SOC engagements — SOC 1, SOC 2, SOC 3

SOC (System and Organization Controls) engagements report on
controls at a service organization. The AICPA defines three
report types and references AT-C standards for each.

## SOC 1 — Controls relevant to user entities' ICFR (AT-C §320)

- **Subject matter**: management's description of the service
  organization's system AND the design (Type 1) or design and
  operating effectiveness (Type 2) of controls.
- **Criteria**: control objectives (defined by service organization,
  reflecting impact on user-entity ICFR).
- **Standard**: AT-C §320 (Reporting on an Examination of Controls
  at a Service Organization Relevant to User Entities' Internal
  Control over Financial Reporting).
- **User**: user entities (service organization customers) and their
  auditors who consider the service organization's controls in
  their financial-statement audits.

### Report types
- **Type 1** — management's description and the design of controls
  AS OF a point in time.
- **Type 2** — management's description, design, AND operating
  effectiveness of controls FOR a period of time (typically 6 or
  12 months).

### Use restriction
SOC 1 report use is restricted to:
- Management of the service organization.
- User entities of the service organization's system.
- Auditors of user entities.

### Common practical issues
- Control objectives must reflect the service organization's
  impact on user-entity F/S; cannot be vague (e.g., "transactions
  are processed accurately" alone is insufficient — must tie to
  specific user-entity F/S assertions).
- Subservice organizations (carve-out vs inclusive method) — the
  report must specify which method is used.
- Complementary user entity controls (CUECs) — controls at user
  entities that the service organization assumes are in place to
  achieve the control objectives.

## SOC 2 — Trust Services Criteria (AT-C §205)

- **Subject matter**: management's description of the system AND
  the suitability of the design (Type 1) or design and operating
  effectiveness (Type 2) of controls relevant to the AICPA Trust
  Services Criteria.
- **Criteria**: AICPA Trust Services Criteria 2017 (TSP §100A):
  - **Security** (common criteria — required in every SOC 2)
  - **Availability**
  - **Processing integrity**
  - **Confidentiality**
  - **Privacy**
- **Standard**: AT-C §205 (examination engagement).

### Report types
- Type 1: design as of a point in time.
- Type 2: design and operating effectiveness over a period.

### Use restriction
SOC 2 reports are typically restricted to:
- Management of the service organization.
- Specified parties (user entities, business partners,
  prospective customers, regulators) who:
  - Have sufficient knowledge to understand the report.
  - Have agreed to take responsibility for sufficiency of the
    procedures and the criteria.

### Trust Services Categories — choosing scope
- Security is mandatory.
- The other four are optional based on user-entity needs.
- Privacy is the broadest in scope and triggers the most
  jurisdictional / regulatory considerations.

### Common practical issues
- Subservice organizations: carve-out vs inclusive.
- Complementary subservice organization controls (CSOCs).
- Mapping to common security frameworks (NIST CSF, ISO 27001) is
  a value-add, not a requirement of SOC 2 itself.
- Cybersecurity risk reporting (separate AICPA framework) is NOT
  a SOC 2 alternative.

## SOC 3 — General-use report on Trust Services Criteria

- **Subject matter**: similar to SOC 2.
- **Output**: a general-use, summarized report — no detailed
  description of system / controls / testing.
- **Use**: marketing tool; can be distributed publicly.
- **Standard**: AT-C §205 (the underlying examination is the same
  as SOC 2; the deliverable is more abbreviated).

## Engagement letter (AT-C §105 + SOC-specific guidance)

The engagement letter must include:
- The SOC report type (SOC 1 / 2 / 3, Type 1 / 2).
- Reporting period.
- Subservice organization treatment (carve-out / inclusive).
- Trust Services Categories (for SOC 2 / 3).
- Restrictions on use.
- Independence affirmation.
- AT-C §105 + §205 / §320 standards reference.

Cross-reference: `engagement-letter-library/references/letters/soc1.md`
and `.../soc2.md`.

## Independence

Required for SOC engagements (examinations under AT-C §205 / §320).
Route any threats to `compliance-aicpa-code`.

## Cross-references

- Common AT-C concepts: `at-c-105-common.md`.
- Examinations: `at-c-205-examinations.md`.
- AICPA SOC for Service Organizations hub: cite as AICPA
  SSAE-companion guidance (not a separate authority).
- Engagement letters: `engagement-letter-library/references/letters/soc1.md`,
  `.../soc2.md`.

## Authority

Cite from AICPA SSAE currently-effective. AT-C §320 for SOC 1;
AT-C §205 for SOC 2 / SOC 3. AICPA Trust Services Criteria 2017
(TSP §100A) for SOC 2 / 3 criteria. Tag
`authority_domain: professional_conduct`,
`authority_type: AICPA_SSAE`, `weight: binding_on_member`.
