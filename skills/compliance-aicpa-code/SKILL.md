---
name: compliance-aicpa-code
description: |
  Walks the AICPA Code of Professional Conduct (ET §1.000+) for a
  given engagement, threat, or scope question. Applies the
  threats-and-safeguards conceptual framework for independence
  (§1.200), screens nonattest services (§1.295), and surfaces
  conflicts (§1.110), confidentiality (§1.700), integrity (§1.100),
  general standards (§1.300), discreditable acts (§1.400), fee
  restrictions (§1.500). Routes SEC issuer / PCAOB independence
  externally. Applies state-board overlay (CA, NY, TX stricter)
  when engagement state supplied. Use when the user asks about
  "AICPA Code", "Code of Professional Conduct", "ET §1.X",
  "independence", "self-review threat", "loan to attest client",
  "nonattest scope", "§1.295", "conflict of interest",
  "confidentiality", or "ethics interpretation". Make sure to use
  this skill whenever the user mentions AICPA Code, independence,
  threats and safeguards, nonattest, or professional conduct.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# compliance-aicpa-code — AICPA Code of Professional Conduct

This skill walks a CPA engagement through the AICPA Code of
Professional Conduct using the **threats-and-safeguards conceptual
framework** that the Code applies to independence and to many other
ethics determinations.

## Read before output

1. `shared/citation-discipline.md` — fabrication ban; the AICPA
   `authority_domain: professional_conduct` ladder.
2. `shared/authority-hierarchy.md` — Professional Standards subsection
   (Phase 9): `binding_on_member`, `interpretive`, `practice_aid`.
3. `shared/confidence-bands.md` — band assignment.
4. `shared/compliance.md` — AICPA Code module + verification checklist.
5. `references/independence-framework.md` — threats-and-safeguards
   walk for ET §1.200.
6. `references/nonattest-services-1295.md` — ET §1.295 scope screen.
7. `references/state-board-overlay.md` — CA / NY / TX stricter
   independence overlays + state-board lookup workflow.

## Operative authority

- AICPA Code of Professional Conduct (live online):
  https://www.aicpa-cima.com/topic/ethics/code-of-professional-conduct
- Cite as `authority_domain: professional_conduct`,
  `authority_type: AICPA_Code`, `weight: binding_on_member`.

## Workflow

### 1. Intake

- `engagement_type`: audit | review | compilation | preparation |
  attestation | tax | advisory | nonattest-only
- `attest_client`: yes | no (drives §1.200 / §1.295 applicability)
- `engagement_state`: 2-letter code (drives state-board overlay)
- `entity_type`: nonissuer | issuer | governmental | nonprofit
  (issuer or governmental → route SEC / PCAOB / Yellow Book externally)
- `threat_pattern`: short description of the fact pattern (e.g.,
  "loan from attest client", "spouse employed by client", "drafted
  client journal entries", "audit for last 8 years partner-in-charge")
- `relationships`: any financial / employment / familial / business
  relationships between firm/partner/staff and the client
- `prior_year_treatment`: how the firm treated this matter previously

### 2. Issuer / governmental routing screen (FIRST STEP)

If `entity_type = issuer` OR user mentions SEC, EDGAR, 10-K, S-1,
PCAOB-registered, public company:
> "This skill defaults to AICPA Code (nonissuer). For SEC issuer
> independence, apply Reg S-X Rule 2-01 and PCAOB Rule 3500T. See
> https://pcaobus.org/oversight/standards. Out of scope here."
> Stop and route externally.

If `entity_type = governmental` OR user mentions Single Audit /
federal grant / Yellow Book / GAGAS:
> "GAO Yellow Book independence is a rules-plus-conceptual hybrid
> distinct from AICPA. See https://www.gao.gov/yellowbook. This
> skill does not cover GAGAS independence. Out of scope."
> Stop and route externally.

### 3. ET §1.200 — Independence (when `attest_client = yes`)

Apply the **threats-and-safeguards conceptual framework**:

1. **Identify threats**:
   - Self-review (auditing own work product)
   - Advocacy (acting as attorney / promoter for client)
   - Familiarity (long association, family relationship)
   - Self-interest (financial interest in client)
   - Undue influence (client pressure, gifts)
   - Management participation (making management decisions)
2. **Evaluate severity**:
   - Acceptable level → no action required.
   - Not at acceptable level → safeguards required.
3. **Apply safeguards**:
   - Created by profession / standards (rotation, peer review)
   - Implemented by client (governance, audit committee)
   - Implemented by firm (separate engagement teams, EQR)
4. **Reassess**: if threats cannot be reduced to an acceptable level
   even with safeguards, **independence is impaired**. Decline the
   attest engagement or withdraw.

Walk `references/independence-framework.md` for the catalog of common
fact patterns and the safeguards that work / don't work for each.

### 4. ET §1.295 — Nonattest services to attest clients (when `attest_client = yes`)

Nonattest services (bookkeeping, tax prep, IT consulting, internal
audit) provided to an attest client are **independence killers** if
not scoped per §1.295. The four conditions all must hold:

- [ ] Firm does NOT assume management responsibilities.
- [ ] Client agrees in writing to assign an individual with suitable
      skill, knowledge, and experience to oversee the service.
- [ ] Client evaluates the adequacy of services performed.
- [ ] Client accepts responsibility for the results.

Specific service screens (per §1.295.115–.180):
- Bookkeeping → permitted with §1.295 safeguards; cannot post journal
  entries that are management decisions.
- Financial information system design and implementation →
  permitted only for specific routine items; no architectural design.
- Internal audit outsourcing → permitted but high-threat; firm cannot
  perform ongoing monitoring as a management function.
- Legal services → generally prohibited.
- Forensic accounting / litigation support → permitted with
  scoping; advocacy threat for litigation services to attest client.

Walk `references/nonattest-services-1295.md` for service-by-service
analysis.

### 5. ET §1.110 — Conflicts of interest

For any engagement (attest or non-attest):
- [ ] Conflicts identified (current and reasonably foreseeable).
- [ ] If conflict exists: disclose to all affected clients; obtain
      specific consent; document in engagement file.
- [ ] If consent cannot be obtained or conflict is unmanageable:
      decline / withdraw.

### 6. ET §1.700 — Confidential client information

- [ ] No disclosure without specific consent EXCEPT:
  - Subpoena / court order / regulatory inquiry (ET §1.700.001).
  - Peer review (with confidentiality agreement).
  - Ethics investigation by AICPA / state board.
- [ ] Tax return preparer §7216 disclosure consent is a separate
      requirement (criminal statute) — route to
      `compliance-ssts-circular230` for §7216 walk.

### 7. ET §1.100 / §1.300 / §1.400 / §1.500 — Other modules

Apply when relevant:
- §1.100 Integrity and Objectivity — no subordination of judgment
  to client / employer.
- §1.300 General Standards — competence (§1.300.001), professional
  care, planning and supervision, sufficient relevant data.
- §1.400 Acts Discreditable — false / misleading representations,
  retention of client records, discrimination, solicitation
  prohibited under tax-rules conditions.
- §1.500 Fees and Other Types of Remuneration —
  - §1.510 Contingent fees: prohibited for attest, return prep,
    amended returns (with narrow exceptions);
  - §1.520 Commissions and Referral Fees: disclosure required;
    prohibited for attest clients.

### 8. State-board overlay (when `engagement_state` supplied)

- [ ] Look up engagement state in `shared/sources.json -> state_boards_of_accountancy.boards`.
- [ ] Check `references/state-board-overlay.md` for known stricter
      states (CA, NY, TX confirmed; full per-state list grows over
      time).
- [ ] If state board rule is stricter than AICPA Code, apply state
      rule and emit `state_overlay_required: true` in the sidecar.

### 9. Conclusion

State the conclusion: independence preserved / impaired; nonattest
scope OK / requires §1.295 safeguards / impairs independence;
conflict manageable / requires withdrawal; confidentiality clear /
disclosure required.

Confidence band per `shared/confidence-bands.md`. Most AICPA Code
conclusions land HIGH (clear authority on point) or MODERATE (fact-
specific threats-and-safeguards assessment). LOW band when the
relevant ethics interpretation post-dates the citation freshness
window or when a state-board overlay is required but not yet
researched.

### 10. JSON sidecar

Emit JSON validating against `shared/output-schema.json`. Use:
- `authority_domain: professional_conduct` for every cited AICPA
  authority.
- `verification_checklist_aicpa_code` populated (independence threats
  identified, safeguards documented, conflicts disclosed,
  confidentiality clause active, §1.295 conditions confirmed).
- `state_overlay_required: true | false`.

## Hard rules

- Never apply SEC / PCAOB independence rules in this skill — route
  externally.
- Never apply Yellow Book / GAGAS independence — route externally.
- Never claim Chevron or Skidmore deference for AICPA standards
  (no Chevron analog applies).
- Never let an AICPA Practice Aid or Technical Q&A be the closest
  authority for a binding-on-member conclusion (drop one band).
- Always emit `state_overlay_required` when an engagement state is
  supplied and a stricter state rule is on point.
- For tax-only engagements, this skill applies to fee, conflict, and
  confidentiality questions; tax-position conclusions still flow
  through `compliance-ssts-circular230`.

## Verification checklist (appendix)

End the markdown response with the AICPA Code module from
`shared/compliance.md` (independence, §1.295, conflicts,
confidentiality, state overlay). Tax-position items from
SSTS/Circular-230 are applicable only when the engagement is a tax
engagement; otherwise omit.
