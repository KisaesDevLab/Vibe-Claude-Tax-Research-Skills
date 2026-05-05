---
name: compliance-sas-audit
description: |
  Walks the AICPA Statements on Auditing Standards (SAS / AU-C
  clarified standards) for a nonissuer audit. Covers the AU-C 200
  series (overall objectives), AU-C 240 (fraud), AU-C 315/330
  (risk assessment / response), AU-C 540 (estimates), AU-C 570
  (going concern), AU-C 600 (group audits), AU-C 700 series
  (reporting). Routes PCAOB AS questions externally (issuer
  audits — out of scope) and Yellow Book / GAGAS questions
  externally. Use when the user asks "audit standards", "SAS",
  "AU-C", "going concern audit", "fraud risk", "audit risk
  assessment", "group audit", "audit report wording", "key audit
  matters", "modified opinion", or "qualified opinion". Make sure
  to use this skill whenever the user mentions audit, SAS, AU-C,
  audit risk, or audit reporting.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# compliance-sas-audit — SAS / AU-C audit standards (nonissuer)

Walks the AICPA Statements on Auditing Standards as codified in the
AU-C "clarified" sections. Applies to **nonissuer** audits only.
Issuer audits are governed by PCAOB AS standards (out of scope —
route externally).

## Read before output

1. `shared/citation-discipline.md` — fabrication ban; the
   `authority_domain: professional_conduct` ladder.
2. `shared/authority-hierarchy.md` — Professional Standards subsection.
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — engagement-letter required-elements module.
5. `references/au-c-overview.md` — sectional structure and common
   AU-C section numbering.
6. `references/au-c-240-fraud.md` — fraud risk assessment, response,
   communications.
7. `references/au-c-315-330-risk.md` — risk assessment + response
   (the audit-risk model).
8. `references/au-c-570-going-concern.md` — substantial-doubt
   evaluation; ASC 205-40 integration.
9. `references/au-c-600-group-audits.md` — group engagements and
   component auditor reference.
10. `references/au-c-700-reporting.md` — unmodified, modified,
    qualified, adverse, disclaimer; emphasis-of-matter; KAMs (only
    when communicated by management for nonissuer).

## Operative authority

- AICPA SAS — currently effective:
  https://www.aicpa-cima.com/resources/download/aicpa-statements-on-auditing-standards-currently-effective
- Cite as `authority_domain: professional_conduct`,
  `authority_type: AICPA_SAS`, `weight: binding_on_member`.

## Workflow

### 1. Intake

- `engagement_type`: audit (must be; if review/compilation, route to
  compliance-ssars; if attest/SOC, route to
  compliance-attestation-qm).
- `entity_type`: nonissuer (required) | issuer (route to PCAOB
  externally) | governmental (route to GAO Yellow Book externally).
- `issue_area`: planning / risk assessment | fraud | estimates |
  going concern | group audit | reporting | other AU-C.
- `framework`: GAAP | tax basis | other special-purpose framework
  (drives reporting under AU-C 800 series).
- `independence_status`: must be independent (AICPA Code §1.200);
  route to `compliance-aicpa-code` for threats and §1.295.

### 2. Issuer / governmental routing screen

If `entity_type = issuer`: route externally:
> "PCAOB AS standards apply to issuer audits. See
> https://pcaobus.org/oversight/standards. This skill defaults to
> AICPA AU-C nonissuer standards; issuer engagements out of scope."

If `entity_type = governmental` (with Single Audit / federal grant
implications): route to GAO Yellow Book externally:
> "Yellow Book (GAGAS) overlays AICPA AU-C for government entities.
> See https://www.gao.gov/yellowbook. Out of scope here."

### 3. Issue-area routing

- Planning, risk assessment, response → `references/au-c-315-330-risk.md`
- Fraud → `references/au-c-240-fraud.md`
- Accounting estimates → AU-C 540 (see `au-c-overview.md` summary)
- Going concern → `references/au-c-570-going-concern.md`
- Group audit / component auditor reference → `references/au-c-600-group-audits.md`
- Reporting / opinion modifications → `references/au-c-700-reporting.md`
- Other (related parties, subsequent events, written reps) →
  `au-c-overview.md` for routing.

### 4. Risk-assessment-driven response (the spine of an AU-C audit)

For most issue areas, the audit response is driven by AU-C 315/330:
1. Understand the entity, its environment, and ICFR.
2. Identify and assess risks of material misstatement (RMM) at the
   F/S level and at the assertion level.
3. Design and perform further audit procedures responsive to RMM.
4. Evaluate sufficiency and appropriateness of audit evidence.
5. Conclude.

Significant risks (AU-C 315.27) require:
- Specific risk-response procedures.
- Tests of details (controls testing alone is insufficient).
- Documentation of the rationale.

### 5. Specific-issue walks

Walk the relevant `references/` file. The walk produces:
- Required procedures (linked to specific AU-C paragraph).
- Documentation requirements.
- Communication requirements (with management, governance,
  regulators).
- Reporting implications (modify opinion? emphasis-of-matter?
  disclaimer?).

### 6. Conclusion

State the conclusion: required procedures the firm will perform,
expected reporting implication, communications required.

Confidence band per `shared/confidence-bands.md`. Audit-standard
conclusions typically land HIGH or MODERATE on the binding-on-member
ladder. LOW band when the issue requires consultation (industry-
specific accounting, novel transactions, complex ICFR considerations)
or when there is unresolved auditor judgment.

### 7. JSON sidecar

Emit JSON validating against `shared/output-schema.json`. Use:
- `authority_domain: professional_conduct` for cited AU-C entries.
- `verification_checklist_engagement` populated.

When ASC accounting issues come up (going concern → ASC 205-40;
loss contingencies → ASC 450; UTP → ASC 740), route to
`research-financial-reporting` or `research-asc-740` for the
substantive GAAP analysis; cite ASC entries in the audit memo with
`authority_domain: gaap`, `weight: gaap_codified`.

## Hard rules

- Never apply PCAOB AS standards in this skill — route externally.
- Never apply Yellow Book / GAGAS — route externally.
- Never claim Chevron or Skidmore deference for AU-C standards.
- Never modify an unmodified audit opinion based on unresolved
  going concern; AU-C 570 requires either adequate disclosure +
  emphasis-of-matter (substantial doubt resolved by mitigation) or
  modified opinion (substantial doubt + disclosure inadequate).
- Never approve a group audit without applying AU-C 600 reference
  decisions (reference component auditor or assume responsibility).
- Always require a signed engagement letter (AU-C 210) before
  beginning fieldwork.
- Always confirm independence (AICPA Code §1.200) before
  acceptance; route to `compliance-aicpa-code` for any threats.

## Verification checklist (appendix)

End the markdown response with the engagement-letter required-
elements module and the AICPA Code module from
`shared/compliance.md`. SSTS / Circular 230 applies only when the
audit is paired with a tax engagement.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
