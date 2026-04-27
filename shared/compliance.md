# Compliance scaffolding

Every research, prediction, summary, planning, and notice-response
output MUST end with the verification checklist below, populated by
the human practitioner. Skills emit it as a markdown appendix; the
JSON sidecar mirrors it as `verification_checklist`.

## AICPA SSTS (effective Jan. 1, 2024)

### SSTS § 1.1 — Advising on tax positions
- [ ] Position has at least a realistic possibility of being
      sustained on its merits (≈ 1-in-3), OR meets the higher
      taxing-authority standard if applicable.
- [ ] If reasonable basis with adequate disclosure: Form 8275 /
      8275-R disclosure prepared.
- [ ] Client advised of potential penalties and disclosure options.

### SSTS § 2.3 — Use of estimates
- [ ] Exact data not practicably obtainable.
- [ ] Estimates reasonable based on facts and circumstances.
- [ ] Estimates not presented with greater precision than warranted.
- [ ] Disclosure on return assessed for unusual circumstances
      (taxpayer death/illness, records destroyed, pending
      litigation, K-1 not yet received).

## Circular 230 (31 CFR Part 10)

### § 10.22 — Diligence as to accuracy
- [ ] Reasonable care in engagement, supervision, training of any
      person whose work product is being relied on.
- [ ] Correctness of representations to Treasury verified.
- [ ] Correctness of representations to client verified.

### § 10.35 — Competence
- [ ] Practitioner has the knowledge, skill, thoroughness, and
      preparation needed for this matter (or has consulted experts /
      studied the law).

### § 10.37 — Written advice (reasonable practitioner standard)
- [ ] Reasonable factual and legal assumptions used.
- [ ] All relevant facts and circumstances reasonably considered.
- [ ] Reasonable efforts to identify and ascertain facts made.
- [ ] No unreasonable reliance on representations / projections /
      appraisals.
- [ ] Applicable law and authorities related to the facts.
- [ ] No "audit lottery" considerations taken into account.

## Disclosure flagging
- Form 8275 (general disclosure)
- Form 8275-R (regulation-contrary position)
- Form 8886 (reportable / listed transaction — required for any
  position involving § 831(b) micro-captives, syndicated
  conservation easements, or other listed transactions)

## Negative-treatment review (v1.1)

The free-source citation discipline of this pack cannot detect
implicit overrules with the same coverage as a commercial citator
(KeyCite, Shepards, BCite, Citator 2nd). The practitioner remains
responsible for:
- [ ] Running an independent citator check on every cited case for
      high-stakes positions.
- [ ] Confirming each cited Revenue Ruling, Notice, or Procedure has
      not been modified, superseded, obsoleted, or revoked.
- [ ] Confirming each cited Treasury Regulation has not been amended
      since the retrieved_date.

## Malpractice defense scaffolding
The output must capture:
- The authorities consulted and weight assigned.
- The factual record relied on (with caveats where the practitioner
  is relying on client representation).
- Alternative interpretations considered and rejected, with rationale.
- Date of research and any staleness warning.
- For state tax questions: the per-state file's `status` and
  `last_reviewed` date.
- For positions affected by recent legislation: cross-reference to
  shared/legislation-tracking.md and the relevant Public Law
  Classification Table entry.
- The practitioner's signature line and date for the checklist.
