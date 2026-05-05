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

## AICPA Code of Professional Conduct (Phase 9 — when applicable)

When a skill output touches independence, integrity/objectivity,
conflicts of interest, confidentiality, or non-tax engagement
acceptance, populate `verification_checklist_aicpa_code` instead of
(or in addition to) the SSTS/Circular-230 checklist above.

### ET §1.200 — Independence (threats-and-safeguards conceptual framework)
- [ ] Threats identified (self-review, advocacy, familiarity, self-
      interest, undue influence, management participation).
- [ ] Threats evaluated (acceptable level / not at acceptable level).
- [ ] Safeguards applied where threats are not at an acceptable level
      (firm-level, engagement-level, or threats-cannot-be-mitigated
      → independence impaired, decline / withdraw).
- [ ] Documentation of threats and safeguards in engagement file.

### ET §1.295 — Nonattest services to attest clients
- [ ] Management responsibilities NOT assumed by the firm.
- [ ] Client agrees to assign individual with suitable skill,
      knowledge, and experience to oversee the nonattest service.
- [ ] Client evaluates adequacy and results of services performed.
- [ ] Client accepts responsibility for the results.
- [ ] Specific prohibited services screened (bookkeeping for an
      audit client → permitted if §1.295 conditions met; financial-
      information system design and implementation, internal audit
      outsourcing, legal services → restrictions apply).

### ET §1.700 — Confidential client information
- [ ] No disclosure without specific consent (subject to ET §1.700.001
      exceptions: subpoena, peer review, ethics investigation).
- [ ] Confidentiality clause in engagement letter active.

### ET §1.110 — Conflicts of interest
- [ ] Conflicts identified (current and reasonably foreseeable).
- [ ] Disclosure to all affected clients made.
- [ ] Specific consent obtained where required.
- [ ] Documentation in engagement file.

### State-board overlay (when engagement state supplied)
- [ ] Engagement state identified.
- [ ] State board independence rule consulted (if stricter than
      AICPA, apply state rule).
- [ ] CA / NY / TX known stricter overlays; full per-state list in
      `shared/sources.json` under `state_boards_of_accountancy`.

## Engagement letter required elements (Phase 9 — when applicable)

When a skill output is an engagement-letter template or scope-of-work
review, populate `verification_checklist_engagement`. Required
elements derive from AR-C §60.A21 (compilation/review/preparation),
AU-C §210 (audit), AT-C §105 .A18 (attestation), and AICPA Tax
Section practice aids (tax engagements).

### Common required elements
- [ ] Engagement objective, scope, and deliverables identified.
- [ ] Responsibilities of management and CPA delineated.
- [ ] Limitations of the engagement disclosed.
- [ ] Fee arrangement disclosed (hourly / fixed / contingent — note
      contingent-fee restrictions under ET §1.510).
- [ ] Termination provisions stated.
- [ ] Signed by both parties (firm + client) before work commences.

### Attest-engagement-specific
- [ ] Independence affirmed (or compilation-without-independence
      disclaimer for AR-C 80 lack-of-independence reports).
- [ ] Inherent limitations of audit / review acknowledged.
- [ ] Subsequent-events reporting period identified (audit only).

### Tax-engagement-specific
- [ ] FTC Safeguards Rule data-security clause present (16 CFR
      Part 314 applies to all tax preparers).
- [ ] §7216 disclosure consent for any third-party use of return
      information.
- [ ] Specification of returns covered (year, jurisdictions, forms).
- [ ] Reliance-on-client-records disclaimer.
- [ ] Penalty / interest exposure framework noted (without violating
      Circular 230 §10.37 audit-lottery prohibition).

### Indemnification / limitation of liability — state overlay
- [ ] CA Bus. & Prof. Code §5063.1 — limits indemnification on
      certain engagements; full scope in
      `engagement-letter-library/references/indemnification-state-overlay.md`.
- [ ] IL, NJ — restrict limitation-of-liability on attest
      engagements.
- [ ] AICPA Ethics Interpretation §1.400.205 — indemnification
      provisions on attest engagements may impair independence.
- [ ] Output is a TEMPLATE FRAMEWORK, not legal advice. Firm counsel
      must review before client use; UPL rules vary by state.

## GAAP research scaffolding (Phase 9 — when applicable)

When a skill output is FASB ASC research, populate
`verification_checklist_gaap`. Required confirmation:
- [ ] ASC Topic / Subtopic / Section / Subsection identified.
- [ ] All ASUs through the engagement reporting date verified for
      effective-date applicability (early adoption permitted? deferred?).
- [ ] Disclosure requirements per ASC topic identified.
- [ ] Non-authoritative sources (Concepts Statements, AICPA TPAs,
      SEC SAB cited persuasively for nonissuers) flagged as such.
- [ ] If GAAP question implicates governmental entity → route to
      GASB externally (out of scope).
- [ ] If GAAP question implicates IFRS reporter → route to IFRS
      externally (out of scope).

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

## Follow-up routing (after the verification checklist)

Phase 10a addition. After the verification checklist appendix and
before the JSON sidecar, every skill's markdown response MUST emit
the follow-up-routing block defined in `shared/follow-up-routing.md`.
The block offers the user two orthogonal handoffs — package the
result (`memo` | `open-point`) and carry the conclusion forward
(`plan` | `workpaper` | `resolution` | `return`) — and the
dispatcher routes the user's reply to the destination skill listed
in that file.

The follow-up block is markdown only. It does NOT modify the JSON
sidecar; the user's response triggers a fresh skill invocation that
produces its own sidecar.
