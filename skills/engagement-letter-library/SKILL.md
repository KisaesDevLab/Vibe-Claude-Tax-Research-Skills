---
name: engagement-letter-library
description: |
  Engagement-letter template library + required-elements framework.
  Generates per-engagement-type templates with bracketed fields,
  paired with a checklist derived from AR-C §60.A21, AU-C §210,
  AT-C §105 .A18, and AICPA Tax Section practice aids. Covers
  audit, review, compilation, preparation, tax (1040 / business /
  advisory), bookkeeping, payroll, consulting, SOC 1, SOC 2, AUP.
  Includes FTC Safeguards Rule clause for tax engagements. Flags
  state indemnification limits (CA Bus. & Prof. Code §5063.1, IL,
  NJ for attest). Use when the user asks "engagement letter",
  "scope of work", "audit engagement letter", "tax engagement
  letter", "limitation of liability", or any request to draft or
  review engagement-letter language. Make sure to use this skill
  whenever the user mentions engagement letter, scope of services,
  or engagement-letter template.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# engagement-letter-library — Engagement letter scaffolding

Mega-skill (planning-strategy-library pattern). Generates a starting
template for each engagement type, with bracketed fields, paired
with a required-elements checklist tied to the relevant AICPA
standard (AR-C §60, AU-C §210, AT-C §105, Tax Section practice
aids).

**Hard rule, prominent:** outputs are *templates and frameworks*,
not legal advice. State-bar UPL rules vary; firm counsel must
review every engagement letter before client use. AICPA practice-
aid sample letters are starting points, not adoptable as-is.

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md` — Professional Standards subsection.
3. `shared/confidence-bands.md`
4. `shared/compliance.md` — engagement-letter required-elements module.
5. `references/index.md` — directory of per-engagement templates.
6. `references/common-clauses.md` — clauses that recur across
   engagement types (fee/billing, dispute resolution, termination,
   confidentiality, e-signature).
7. `references/ftc-safeguards-rule.md` — FTC Safeguards Rule
   (16 CFR Part 314) data-security clause for tax engagements.
8. `references/indemnification-state-overlay.md` — CA / IL / NJ
   limits and AICPA Ethics Interpretation §1.400.205 attest-
   independence implications.
9. `references/letters/<engagement-type>.md` — the specific
   per-engagement template.

## Operative authority

For each engagement type, the operative AICPA standard:
- Audit: AU-C §210, plus AU-C 200 / 230 / 260 / 265 / 300 series.
- Review (SSARS): AR-C §60.A21 + §90.10.
- Compilation (SSARS): AR-C §60.A21 + §80.10.
- Preparation (SSARS): AR-C §60.A21 + §70.10.
- Attestation / SOC: AT-C §105 .A18 + §205 (or §320 for SOC 1).
- Tax: AICPA Tax Section practice aids; AICPA SSTS §1.4 (engagement
  agreements); IRS Circular 230 §10.32 (compilation of returns
  obligations); FTC Safeguards Rule.

Cite as `authority_domain: professional_conduct`,
`authority_type: AICPA_SAS / AICPA_SSARS / AICPA_SSAE / AICPA_PracticeAid`,
`weight: binding_on_member` for standards, `practice_aid` for
practice aids. Tag `legal_review_required: true` in the JSON
sidecar.

## Workflow

### 1. Intake

- `engagement_type`: audit | review | compilation | preparation |
  tax-1040 | tax-business | tax-advisory | bookkeeping | payroll |
  consulting | soc1 | soc2 | aup | other
- `client_type`: individual | partnership | LLC | S-corp | C-corp |
  trust | estate | nonprofit | governmental
- `engagement_state`: 2-letter code (drives state-overlay
  indemnification + state-board independence)
- `firm_safeguards_program_status`: in place | being implemented |
  not yet (drives FTC Safeguards Rule clause for tax engagements)
- `attest_independence_required`: yes (audit/review/attestation/
  SOC) | no (tax/advisory/AUP)
- `prior_year_engagement_letter`: signed | not signed | first-year
- `unusual_features`: e.g., contingent fee (route to AICPA Code
  §1.510), litigation support (advocacy threat), large-dollar
  exposure (limitation of liability, indemnification, malpractice
  coverage).

### 2. Engagement-type routing

Route to `references/letters/<engagement-type>.md`:
- audit → `letters/audit.md`
- review → `letters/review.md`
- compilation → `letters/compilation.md`
- preparation → `letters/preparation.md`
- tax-1040 → `letters/tax-1040.md`
- tax-business → `letters/tax-business.md`
- tax-advisory → `letters/tax-advisory.md`
- bookkeeping → `letters/bookkeeping.md`
- payroll → `letters/payroll.md`
- consulting → `letters/consulting.md`
- soc1 → `letters/soc1.md`
- soc2 → `letters/soc2.md`
- aup → `letters/aup.md`

### 3. Required elements walk

Apply the required-elements checklist from `shared/compliance.md`
+ engagement-specific elements from the AICPA standard:
- [ ] Engagement objective and scope.
- [ ] Responsibilities of management vs. firm.
- [ ] Limitations of the engagement.
- [ ] Identification of framework / criteria.
- [ ] Form and content of any report (or notation of no report).
- [ ] Fee arrangement (hourly / fixed / contingent — note §1.510
      contingent-fee restrictions).
- [ ] Termination provisions.
- [ ] Communication framework.
- [ ] Signed by both parties.

### 4. Common-clauses overlay

From `references/common-clauses.md`, layer in clauses applicable to
the engagement:
- Confidentiality (AICPA Code §1.700; for tax engagements, IRC
  §7216).
- Records retention.
- Subcontractors / specialists.
- Use of firm name / report restrictions.
- Disputes / arbitration / mediation.
- Force majeure.
- Governing law (typically engagement state).
- E-signature (E-SIGN Act + UETA most jurisdictions).

### 5. FTC Safeguards Rule (tax engagements)

For ANY tax engagement (1040, business, advisory), apply
`references/ftc-safeguards-rule.md`:
- The firm is a "financial institution" under 16 CFR §314.2.
- Engagement letter should reference firm's written information
  security program.
- Required mention of:
  - Designated Qualified Individual.
  - Risk assessment.
  - Incident response.
  - Encryption / access controls.
  - Data retention / disposal.
  - Vendor / service-provider oversight.
- Practitioner-required clause: "Firm has implemented a written
  information security program in compliance with the FTC
  Safeguards Rule (16 CFR Part 314)..."

### 6. Indemnification / limitation of liability — state overlay

Walk `references/indemnification-state-overlay.md`:
- **California**: Cal. Bus. & Prof. Code §5063.1 imposes
  restrictions on indemnification and limitations of liability
  on attest engagements. Firm-level liability cannot be
  indemnified by client for firm's gross negligence or willful
  misconduct.
- **Illinois**: limitation-of-liability clauses on attest
  engagements are unenforceable.
- **New Jersey**: similar restrictions on attest indemnification.
- **AICPA Ethics Interpretation §1.400.205**: indemnification
  provisions on attest engagements may impair independence.
  Engagement letter for an attest engagement should NOT include
  client indemnification of firm for firm's own acts.

For non-attest engagements (tax, advisory, bookkeeping):
limitation-of-liability is more often enforceable but state-by-state
overlay still applies.

### 7. Output

Generate the engagement letter template with:
- Brief preamble explaining what the template is and what fields
  to fill in.
- The full template with `[BRACKETED FIELDS]` for firm name, client
  name, engagement period, scope, fee, etc.
- A required-elements checklist appended for the firm to confirm.
- A "practitioner notes" section flagging risks (state-overlay
  indemnification, FTC Safeguards, contingent-fee restrictions).

Conclude with: "This is a TEMPLATE FRAMEWORK. Firm counsel must
review before client use. Specific scope, fee, and risk-allocation
language should be tailored to the engagement and the firm's
malpractice insurance / risk-management program."

### 8. Conclusion + sidecar

- `legal_review_required: true`.
- `verification_checklist_engagement` populated.
- Confidence band: typically MODERATE for the framework correctness
  (HIGH for standardized engagements, LOW for novel arrangements
  requiring counsel-driven customization).
- Cite the engagement-specific AICPA standard with
  `authority_domain: professional_conduct`,
  `weight: binding_on_member`.

## Hard rules

- Output is a TEMPLATE FRAMEWORK, not legal advice. Firm counsel
  must review before client use.
- State-bar UPL rules vary; do not warrant any template as
  jurisdiction-specific compliance.
- Never include indemnification of firm for firm's own gross
  negligence or willful misconduct on an attest engagement (AICPA
  Ethics Interpretation §1.400.205 implies independence
  impairment).
- Never recommend a contingent fee for an attest engagement, return
  preparation, or amended return (AICPA Code §1.510 prohibition).
- Always include FTC Safeguards Rule clause for tax engagements.
- Always require firm to confirm engagement state to apply
  appropriate state overlay.
- Never claim Chevron or Skidmore deference.
- The verification-flag sentinel pattern (see
  `shared/citation-discipline.md`) is permitted within
  per-engagement template files (the per-template files ship with
  bracketed fields and may include verification flags for attorney
  or firm-counsel input).

## Verification checklist (appendix)

End the markdown response with the engagement-letter required-
elements module + AICPA Code module (for confidentiality and
independence) from `shared/compliance.md`.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
