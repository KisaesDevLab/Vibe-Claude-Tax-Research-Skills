---
name: "Qualified Charitable Distribution (QCD) from IRA"
slug: qcd
type: Retirement
tax_type: EFR
complexity: Low
irc_sections: ["§408(d)(8)", "§170"]
forms: ["Form 1099-R", "Form 1040"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

§408(d)(8) Qualified Charitable Distribution (QCD) is a powerful
charitable giving vehicle for IRA owners age 70½ or older. The
mechanism:

1. **Direct transfer from IRA to qualified charity.**
2. **Up to $105,000 (2024; indexed by SECURE 2.0)** per year per
   IRA owner.
3. **Excluded from gross income** (does NOT appear in AGI).
4. **Counts toward Required Minimum Distribution (RMD)** for the
   year.
5. **No charitable deduction** (because not in income).

The exclusion-from-AGI feature is the key benefit — it produces
multiple downstream advantages:

- **§121 §22 §86 phaseouts** based on AGI / MAGI not affected.
- **Medicare IRMAA** brackets not triggered.
- **Social Security taxation** (up to 85% at high AGI) not
  affected.
- **§213 medical deduction threshold** (7.5% of AGI) not raised.
- **§170 charitable deduction AGI limits** not consumed.
- **Effective for non-itemizers** (post-TCJA standard deduction
  era).

QCD is generally superior to taking RMD and donating proceeds
because:
- Donating proceeds requires itemizing for §170 deduction.
- Itemized deduction may not fully offset RMD income.
- AGI-driven phaseouts hit harder at higher income.

SECURE 2.0 added one-time election to fund Charitable Gift
Annuity (CGA) or Charitable Remainder Trust (CRT) up to $53,000
(2024) from QCD; verify implementation.

## Primary IRC authority

- §408(d)(8) — Qualified charitable distributions.
- §408(d)(8)(B) — $105,000 limit (post-SECURE 2.0; was $100,000
  pre-SECURE 2.0).
- §408(d)(8)(F) — One-time CGA/CRT (SECURE 2.0).
- §170(c) — Qualified charitable organizations.
- §401(a)(9) — RMD requirements.

## Treasury regulations

- Reg §1.408-8 — RMD rules.
- Reg §1.408-1 — Individual retirement accounts general.

## Key IRS guidance

- IRS Publication 590-B — Distributions from IRAs.
- Notice 2007-7 — QCD initial guidance.

## Eligibility requirements

1. **IRA owner age 70½+** (NOT age 73 RMD threshold —
   §408(d)(8)(B)(ii)).
2. **Distribution from Traditional or Roth IRA** (NOT from
   employer-sponsored plan; rollover to IRA first).
3. **Direct transfer to charity** — IRA custodian sends directly
   to charity (or makes check payable to charity but delivered to
   account holder for delivery).
4. **Recipient is qualified §170(c) charity** — NOT donor advised
   fund, NOT private foundation (with limited exceptions for
   certain public charities), NOT supporting organization.
5. **Up to $105,000 (2024) per IRA owner.**

## Mechanics — how it works

1. **Verify charity §170(c) status** — most public charities
   qualify; DAFs and private foundations do NOT.
2. **Contact IRA custodian** — request QCD distribution.
3. **Custodian sends check directly to charity** OR makes payable
   to charity for delivery by IRA owner.
4. **Form 1099-R issued** by IRA custodian — typically Box 1
   shows total distribution including QCD amount; Box 2a (taxable
   amount) often shows full amount because custodian doesn't know
   QCD treatment.
5. **Taxpayer reports on Form 1040** Line 4a (gross IRA
   distribution); Line 4b (taxable amount) is the gross
   distribution MINUS the QCD amount.
6. **Write "QCD" next to Line 4b.**
7. **Counts toward RMD** for the year.

## Documentation requirements

- Form 1099-R from IRA custodian.
- Charity acknowledgment letter (substantiation per §170(f)(8)).
- Custodian distribution records showing direct transfer.

## Common pitfalls / audit risks

- **Age requirement (70½, not 73).** Common error post-SECURE Act
  RMD age change.
- **Indirect distribution.** If IRA owner takes distribution to
  personal account first and then donates, NOT a QCD.
- **DAF / private foundation as recipient.** Disqualifies QCD.
- **SEP-IRA / SIMPLE IRA QCD.** Restrictions on "ongoing"
  SEP/SIMPLE — consult guidance.
- **§408(b) annuity contracts.** May or may not qualify.
- **Form 1099-R Box 2a inflated.** Need to manually adjust on
  Form 1040.
- **Roth IRA QCD.** Permitted but typically wasteful (Roth
  distributions already tax-free).
- **Coordination with §401(a)(9) RMD.** QCD counts toward RMD;
  ensure full RMD satisfied.
- **State tax treatment.** Some states do not conform; QCD may be
  state-taxable.

## Recent legislative changes

- **PATH Act (2015)** — Made QCD permanent.
- **SECURE Act (2019)** — Increased RMD age to 72.
- **SECURE 2.0 (2022)** — Increased $100K to $105K (indexed);
  RMD age to 73; one-time CGA/CRT $50K (indexed to $53K for 2024).
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §408(d)(8)
  Pub L 119-21]`. Working assumption: SECURE 2.0 framework
  preserved.

## State conformity considerations

State conformity to QCD varies. **California** does not conform
fully; QCD may be taxable at state level.

## Default confidence band rationale

**HIGH** — clear statutory framework; well-established practice.

## Cross-references

- `charitable-donation-appreciated` (#51).
- `donor-advised-fund` (#54).
- `charitable-planning` (#53).
- `traditional-ira-contributions` (#83).
- `niit-minimization` (#69) — AGI reduction benefit.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 408(d)(8)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 170(c)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"Notice","citation":"Notice 2007-7","url":"https://www.irs.gov/irb","weight":"irs_published"}
  ]
}
```
