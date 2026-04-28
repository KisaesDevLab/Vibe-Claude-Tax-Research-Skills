# Penalty abatement pathways

## Pathway map

| Pathway | Penalty types | Source | Difficulty |
|---|---|---|---|
| First-Time Abatement (FTA) | §6651(a)(1), (a)(2), (a)(3) | IRM 20.1.1.3.6 | Easy — administrative |
| Reasonable cause (§6651) | §6651 family | Treas. Reg. §301.6651-1(c)(1) | Moderate — facts-and-circumstances |
| Reasonable cause (§6662) | §6662 family (except (b)(6)) | §6664(c)(1) + Treas. Reg. §1.6664-4 | Moderate-to-hard |
| Statutory exceptions | Various | §6651(a)(1) flush ("not due to willful neglect") | Variable |
| First-Time Penalty Abatement Coordinator | All categories | IRM 20.1.1 | Procedural escalation |

## FTA — IRM 20.1.1.3.6

Conditions:
1. Penalty is §6651(a)(1) FTF, §6651(a)(2) FTP, or §6651(a)(3)
   failure-to-deposit.
2. Compliance: filed all required returns AND paid (or arranged
   payment for) any tax due for the prior 3 years.
3. No FTA used in the prior 3 years (prior FTA in years 4+ allowed).
4. Penalty is for a SINGLE return / period (not a pattern).
5. Estimated-tax penalty under §6654 / §6655 is NOT eligible.

How to request:
- Phone the IRS taxpayer-service line and ask for FTA.
- Write to the taxpayer's service center referencing IRM 20.1.1.3.6.
- For Form 941 / 940 employment-tax penalties, contact the
  business-section practitioner line.

§6662 accuracy penalties are NOT FTA-eligible; FTA is limited to
§6651 family failures.

## §6651 reasonable-cause — Treas. Reg. §301.6651-1(c)(1)

"Ordinary business care and prudence" standard:
- Taxpayer made the failure despite the exercise of ordinary
  business care and prudence; AND
- Either could not file/pay timely OR did not know there was a
  filing/payment obligation.

### Causes that succeed when documented

- **Serious illness / hospitalization**: Verified medical records
  for taxpayer or close family member; contemporaneous with the
  filing/payment period.
- **Death**: Death certificate; close-family relationship.
- **Casualty / records loss**: Police reports, insurance claims,
  fire/flood reports, ransomware incident reports.
- **Records inaccessible**: Bankruptcy trustee retention; ongoing
  litigation custody; records held by an embezzling employee.
- **Substantive professional advice**: Written advice from a
  competent professional that no return was due or that a
  position was correct (NOT advice on the filing-date itself —
  Boyle bars that).

### Causes that fail

- "I forgot" / "I was busy" — does not meet ordinary-care.
- Ignorance of the law (limited exceptions for first-time filers,
  statutory complexity).
- Software / online-system failure absent contemporaneous
  documentation of the failure and timely retry.
- Reliance on agent for filing date — Boyle.

## United States v. Boyle, 469 U.S. 241 (1985)

Executor relied on attorney to file estate-tax return; attorney
missed the deadline. Supreme Court held that reliance on a tax
professional for the filing-date itself is NOT reasonable cause.
The taxpayer is responsible for knowing and meeting the deadline.

The Boyle holding is unforgiving on facts indistinguishable from
its own. Practitioners attempt to carve out:
- Substantive-advice reliance (McMahan).
- E-filing / IRS system failure ('Notice 2010-13' line of
  guidance).
- Disability or incapacity preventing the taxpayer from
  ascertaining the deadline.

## McMahan v. Commissioner, 114 F.3d 366 (2d Cir. 1997)

Carve-out from Boyle: when the taxpayer relies on an advisor's
SUBSTANTIVE advice (e.g., that no return is required), the
reliance can constitute reasonable cause. The advisor must:
- Be a competent professional.
- Have all the necessary information.
- Provide advice based on applicable law.

McMahan is good law in the 2d Cir. and has been followed in
varying degrees in other circuits. Cite the binding circuit's
post-Boyle case law before relying on McMahan.

## §6662 reasonable-cause — §6664(c)(1)

Treas. Reg. §1.6664-4 facts-and-circumstances. Most-significant
factors:
- Taxpayer's experience, knowledge, education.
- Effort to assess proper tax liability.
- Reliance on advice of a tax professional.

§1.6664-4(b)(1) reliance on professional requires:
1. Advisor with sufficient expertise (CPA, attorney, EA in the
   relevant subject area).
2. Necessary and accurate information provided to advisor.
3. Reliance in good faith.
4. Advice based on all pertinent facts and applicable law (not
   reliance on a generic conclusion).

§6664(c)(2) — NO reasonable-cause defense for §6662(b)(6)
(non-disclosed economic-substance-doctrine-failed transaction).
Strict liability.

## Substantial-authority / reasonable-basis with disclosure

§6662(d)(2)(B):
- **Substantial authority** (~ 40% probability): no penalty even
  without disclosure.
- **Reasonable basis** (~ 20% probability): penalty avoided ONLY
  with adequate disclosure (Form 8275, 8275-R for reg-contrary
  positions).

See `shared/confidence-bands.md` for the band-to-standard mapping.

## §6662(d)(2)(C) — qualified amended return

Filing a qualified amended return (QAR) before:
- The IRS contacts the taxpayer for examination of the return;
  AND
- Various other procedural triggers.

The QAR resets the position; the originally-filed return's items
are no longer at issue. Practical use: when a position is
discovered to lack reasonable basis, file a QAR before the IRS
audit to eliminate accuracy-penalty exposure.

## IRM 20.1.1.3 — Reasonable Cause Considerations

The IRM provides a structured framework for IRS exam-personnel
review of reasonable-cause requests. Practitioner should mirror
this structure in the abatement request:
1. Statement of facts.
2. Identification of the penalty.
3. Application of the reasonable-cause standard.
4. Supporting documentation.
5. Citation to applicable Treas. Regs. and case law.
6. Explanation of why the cause is "for the period at issue".

## Letter format for an abatement request

**Heading**: Taxpayer name, SSN/EIN, Tax Year, Penalty section,
amount.

**Statement of facts**: Concise narrative tying the cause to the
period of the penalty.

**Application of standard**: "We respectfully request abatement
under §6651(a)(1) on grounds of reasonable cause ... ordinary
business care and prudence was exercised ... [cite Treas. Reg.
§301.6651-1(c)(1)]."

**Documentation**: Attach medical records, death certificates,
insurance claims, etc.

**Conclusion**: Explicit request for abatement and a refund of
any payments already made on the penalty.

## Practitioner audit-defense file

- [ ] FTA eligibility screened first.
- [ ] Compliance for prior 3 years confirmed.
- [ ] Cause documented contemporaneously where possible.
- [ ] Boyle / McMahan analysis explicit if professional reliance
  asserted.
- [ ] §6662 analysis distinguishes from §6662(b)(6) strict
  liability.
- [ ] Substantial-authority / reasonable-basis-with-disclosure
  pathway considered for §6662 abatement.
- [ ] IRS Data Book penalty-abatement statistics consulted only
  for administrative-trend context (`persuasive_non_authority`).
