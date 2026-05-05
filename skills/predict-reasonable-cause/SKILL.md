---
name: predict-reasonable-cause
description: |
  Predicts whether a taxpayer will obtain reasonable-cause abatement
  of failure-to-file (§6651(a)(1)), failure-to-pay (§6651(a)(2)), or
  accuracy-related (§6662) penalties under IRC §6664(c) (substantial-
  authority and reasonable-basis defenses) or under the IRM 20.1.1
  reasonable-cause framework. Distinguishes reasonable-cause from
  the First-Time Abatement (FTA) administrative waiver. Use when the
  user asks "can I get this penalty abated", "reasonable cause",
  "FTA", "first-time abatement", "Boyle defense", "§6664", "§6651
  penalty abatement", "ordinary business care", or "IRM 20.1.1".
  Make sure to use this skill whenever the user mentions reasonable
  cause, penalty abatement, FTA, or first-time abatement.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# predict-reasonable-cause — penalty abatement prediction

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `references/abatement-pathways.md` — §6664 / IRM 20.1.1 framework,
   FTA administrative waiver, Boyle / Niedringhaus / McMahan tests.
6. `references/irs-data-book-penalty-stats.md` — IRS Data Book
   penalty-abatement statistics (persuasive_non_authority for
   showing administrative-trend context, NOT for legal authority).

## Operative authority

- IRC §6651(a)(1) — failure-to-file penalty (5% per month, max 25%);
  reasonable-cause defense at §6651(a)(1).
- IRC §6651(a)(2) — failure-to-pay penalty (0.5% per month, max
  25%); reasonable-cause defense.
- IRC §6662 — accuracy-related penalty (20% / 40%).
- IRC §6664(c)(1) — reasonable-cause and good-faith exception to
  §6662 (substantial authority / reasonable basis with adequate
  disclosure / qualified-amended-return).
- IRC §6664(c)(2) — strict liability for §6662(b)(6) ESD non-
  disclosure; NO reasonable-cause defense.
- Treas. Reg. §301.6651-1(c)(1) — "ordinary business care and
  prudence" standard for reasonable cause.
- Treas. Reg. §1.6664-4 — accuracy-penalty reasonable-cause
  facts-and-circumstances.
- IRM 20.1.1 — Penalty Handbook; reasonable-cause framework and
  the FTA administrative waiver (IRM 20.1.1.3.6).
- United States v. Boyle, 469 U.S. 241 (1985) — reliance on agent
  for filing date is NOT reasonable cause.
- McMahan v. Commissioner, 114 F.3d 366 (2d Cir. 1997) — Boyle
  carve-out for substantive advice.

## Workflow

### 1. Intake

- `penalty_type`: §6651(a)(1) FTF, §6651(a)(2) FTP, §6662 accuracy
- `tax_year` and `assessment_date`
- `cause_alleged`: serious illness, death, casualty, reliance on
  professional, records destroyed, ignorance of law (rarely
  prevails), etc.
- `taxpayer_compliance_history`: prior 3 years for FTA eligibility
- `documentation_available`: medical records, insurance claims,
  death certificates, court filings, etc.
- `professional_advice_facts`: written tax advice received, scope
  of engagement, who the professional was, reliance reasonable

### 2. First-Time Abatement (FTA) screen

IRM 20.1.1.3.6 administrative waiver — easier than reasonable
cause:
1. Penalty must be §6651(a)(1) FTF, §6651(a)(2) FTP, or
   §6651(a)(3) failure-to-deposit (employment).
2. Compliance: filed all required returns AND paid (or arranged
   payment for) any tax due for the prior 3 years.
3. No FTA used in the prior 3 years.
4. Penalty is for a SINGLE return / period (not a pattern).

§6662 accuracy penalties are NOT eligible for FTA. Always screen
FTA first; if available, request that BEFORE asserting reasonable
cause (the IRS often grants FTA without prejudice to a later
reasonable-cause request for a separate year).

### 3. Reasonable-cause for §6651 (failure-to-file / pay)

Treas. Reg. §301.6651-1(c)(1): "ordinary business care and prudence"
standard. The taxpayer must have:
- Made the failure despite the exercise of ordinary business care
  and prudence; AND
- Either could not file/pay timely OR did not know there was a
  filing/payment obligation.

Causes that ROUTINELY succeed when documented:
- Serious illness / hospitalization of taxpayer or close family
  member.
- Death of taxpayer or close family member.
- Records destruction (fire, flood, theft, including digital
  ransomware).
- Inability to obtain records due to circumstances beyond control
  (e.g., bankruptcy trustee withholding records).
- Reliance on substantive tax advice from a competent professional
  (NOT mere reliance for filing-date — Boyle bars that).

Causes that ROUTINELY fail:
- Ignorance of the law (with limited exceptions for first-time
  filers and statutory complexity).
- Software / online-system failure unless extensively documented.
- "I forgot" or "I was busy".
- Reliance on agent for the filing date itself (Boyle).

### 4. Reasonable-cause for §6662 (accuracy)

§6664(c)(1) and Treas. Reg. §1.6664-4: reasonable-cause and good-
faith exception. Factors:
- Taxpayer's experience, knowledge, education.
- Reliance on professional advice (must be reasonable; advisor
  must have all relevant facts; advice must address tax issues
  specifically).
- Taxpayer's effort to assess proper tax liability.

For substantial-authority / reasonable-basis defenses see
shared/confidence-bands.md mapping.

§6664(c)(2): NO reasonable-cause defense for §6662(b)(6)
(non-disclosed economic-substance-doctrine-failed transactions —
strict liability).

### 5. Reliance on professional — Boyle / McMahan framework

Boyle v. United States, 469 U.S. 241 (1985):
- Reliance on a tax professional for the FILING DATE is NOT
  reasonable cause. The taxpayer is responsible for knowing the
  filing deadline.

McMahan v. Commissioner, 114 F.3d 366 (2d Cir. 1997):
- Reliance on substantive advice (e.g., that no return is required,
  or that a particular position is correct) CAN constitute
  reasonable cause if the reliance is reasonable.

Practical line: ministerial-task reliance ≠ reasonable cause;
substantive-advice reliance = reasonable cause if four conditions
met (Treas. Reg. §1.6664-4(b)(1)):
1. Advisor was a competent professional with sufficient expertise.
2. Taxpayer provided necessary and accurate information.
3. Taxpayer relied in good faith.
4. Advice was based on all pertinent facts and applicable law.

### 6. Conclusion

Confidence band per `shared/confidence-bands.md`:

- HIGH: clear FTA eligibility OR documented serious illness /
  death / records destruction with contemporaneous documentation.
- MODERATE: substantive-advice reliance with documentation; first-
  time complex-statute confusion with good-faith effort.
- LOW: reliance for filing date (Boyle bars); software failure
  inadequately documented; ignorance of law absent extenuating
  circumstances.
- SPECULATIVE: pattern of late filings; willful disregard;
  §6662(b)(6) ESD non-disclosure.

### 7. Authorities + sidecar

Cite §6651, §6662, §6664, relevant Treas. Regs., IRM 20.1.1, and
Boyle / McMahan. The IRS Data Book penalty statistics may be
cited as `IRSPub` / `persuasive_non_authority` to provide
administrative-trend context but NEVER as the closest authority.
JSON sidecar validates against `shared/output-schema.json`.

## Hard rules

- Always screen FTA first; many practitioners miss the easy path.
- Never assert filing-date reliance under Boyle.
- Never apply reasonable-cause to §6662(b)(6) (strict liability).
- Drop one band when reliance on professional is asserted but the
  professional lacked relevant facts.
- Drop one band when the cause alleged is recurring across
  multiple years.
- The IRS Data Book is `persuasive_non_authority` only; never let
  it drive a band assignment.

## Verification checklist (appendix)

End with the SSTS / Circular 230 checklist from
`shared/compliance.md`. For high-stakes positions (six-figure
penalty exposure), include the negative-treatment-review residual
practitioner responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
