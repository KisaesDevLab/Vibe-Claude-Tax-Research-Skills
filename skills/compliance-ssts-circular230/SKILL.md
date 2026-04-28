---
name: compliance-ssts-circular230
description: |
  Walks the AICPA SSTS and Circular 230 compliance checklist for a
  given engagement or written-tax-advice deliverable. Verifies SSTS
  §1.1 (realistic possibility), §2.3 (estimates), and Circular 230
  §10.22 (diligence), §10.35 (competence), §10.37 (written advice
  / reasonable-practitioner standard). Identifies disclosure
  obligations (Form 8275 / 8275-R / 8886). Flags negative-treatment-
  review residual practitioner responsibility for high-stakes
  positions. Use when the user asks "is this position SSTS-
  compliant", "Circular 230 §10.37", "do I need Form 8275",
  "realistic possibility", "substantial authority", "reasonable
  basis with disclosure", or "written tax advice standards". Make
  sure to use this skill whenever the user mentions SSTS, Circular
  230, §10.22, §10.35, §10.37, Form 8275, or written tax advice.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# compliance-ssts-circular230 — SSTS / Circular 230 checklist

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md` — canonical checklist.
5. `references/irs-guidance-primer.md` — IRS "Understanding IRS
   Guidance — A Brief Primer" (per BUILD_PLAN).

## Operative authority

- AICPA Statements on Standards for Tax Services (SSTS), effective
  January 1, 2024:
  - SSTS §1.1 — Tax Position Returns and Other Tax Communications.
  - SSTS §2.3 — Use of Estimates.
- Circular 230 (31 C.F.R. Part 10):
  - §10.22 — Diligence as to accuracy.
  - §10.35 — Competence.
  - §10.37 — Requirements for written advice (reasonable-
    practitioner standard).

## Workflow

### 1. Intake

- `engagement_type`: tax position, written advice, return prep,
  notice response, planning recommendation, etc.
- `client_facts`: relevant facts and circumstances.
- `position_or_recommendation`: the substantive matter.
- `confidence_band` (per shared/confidence-bands.md).
- `disclosure_status`: Form 8275 / 8275-R / 8886 filed or
  contemplated.

### 2. SSTS § 1.1 walk

§ 1.1 — Tax Position Returns and Other Tax Communications:

- [ ] Position has at least a REALISTIC POSSIBILITY (~ 1-in-3) of
  being sustained on its merits, OR meets a higher taxing-
  authority standard if applicable (e.g., substantial-authority).
- [ ] If position relies on reasonable basis with adequate
  disclosure: Form 8275 / 8275-R prepared and filed.
- [ ] Client advised of potential penalties and disclosure options.

Confidence-band mapping (per shared/confidence-bands.md):
- HIGH (≥ 70%): clearly satisfies realistic-possibility and
  substantial-authority standards.
- MODERATE (~ 40-50%): satisfies substantial-authority standard;
  no disclosure required.
- LOW (~ 20-35%): reasonable-basis only; disclosure required.
- SPECULATIVE: does NOT meet SSTS § 1.1 — practitioner should
  decline to recommend.

### 3. SSTS § 2.3 walk

§ 2.3 — Use of Estimates:

- [ ] Exact data not practicably obtainable.
- [ ] Estimates are reasonable based on facts and circumstances.
- [ ] Estimates not presented with greater precision than
  warranted.
- [ ] Disclosure on return assessed for unusual circumstances:
  - Taxpayer death / illness.
  - Records destroyed.
  - Pending litigation.
  - K-1 not yet received.

### 4. Circular 230 § 10.22 — Diligence

- [ ] Reasonable care in engagement, supervision, and training of
  any person whose work product is being relied on.
- [ ] Correctness of representations to Treasury verified.
- [ ] Correctness of representations to client verified.

### 5. Circular 230 § 10.35 — Competence

- [ ] Practitioner has the knowledge, skill, thoroughness, and
  preparation needed for this matter.
- [ ] If lacking: practitioner has consulted with experts /
  studied applicable law.

### 6. Circular 230 § 10.37 — Written advice (reasonable-
practitioner standard)

For written tax advice:

- [ ] Reasonable factual and legal assumptions used.
- [ ] All relevant facts and circumstances reasonably considered.
- [ ] Reasonable efforts made to identify and ascertain facts.
- [ ] No unreasonable reliance on representations / projections /
  appraisals.
- [ ] Applicable law and authorities related to the facts.
- [ ] No "audit lottery" considerations taken into account.

### 7. Disclosure flagging

- Form 8275 — general disclosure for non-frivolous positions.
- Form 8275-R — regulation-contrary positions.
- Form 8886 — reportable / listed transactions:
  - §831(b) micro-captives (Notice 2016-66).
  - Syndicated conservation easements (Notice 2017-10).
  - Other listed and reportable transactions.

### 8. Negative-treatment-review residual responsibility

For high-stakes positions (large dollar amounts, novel arguments,
positions relying on Tax Court memorandum or older Court of
Appeals authority), the free-source citation discipline of this
pack cannot detect implicit overrules with comprehensive coverage.

The practitioner remains responsible for:
- [ ] Running an independent citator check (KeyCite, Shepard's,
  BCite, Citator 2nd) on every cited case.
- [ ] Confirming cited Rev. Rul. / Notice / Procedure has not
  been modified, superseded, obsoleted, or revoked.
- [ ] Confirming cited Treasury Regulation has not been amended
  since the retrieved_date.

### 9. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
`verification_checklist` populated as boolean fields:
- `ssts_1_1`: true if position meets realistic-possibility / SSTS
  § 1.1 standard.
- `ssts_2_3`: true if estimates comply with SSTS § 2.3.
- `circ230_10_22`: true if diligence-as-to-accuracy met.
- `circ230_10_35`: true if competence met.
- `circ230_10_37`: true if written-advice standards met.

Plus arbitrary `additionalProperties` for engagement-specific
items.

`disclosure_forms[]` populated: 8275, 8275-R, 8886, or "none".

Confidence band per `shared/confidence-bands.md`. HIGH for clean
compliance walks; MODERATE if disclosure obligations are
contestable; LOW if practitioner-judgment items remain open.

## Hard rules

- Never recommend a SPECULATIVE-band position (does NOT meet
  SSTS § 1.1 realistic-possibility).
- Always require Form 8275 / 8275-R disclosure for LOW-band
  reasonable-basis positions.
- Always require Form 8886 disclosure for listed / reportable
  transactions; the §6662(i) 40% strict-liability penalty applies
  to non-disclosed §6662(b)(6) ESD positions.
- Always note Skidmore-review framework for Treasury Reg
  reliance post-Loper Bright.
- Always include the negative-treatment-review residual
  practitioner responsibility for high-stakes positions.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. This skill IS the checklist
implementation; the checklist appendix is a self-reflexive
summary for the practitioner's audit-defense file.
