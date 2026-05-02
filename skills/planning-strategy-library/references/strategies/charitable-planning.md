---
name: "Charitable Planning (Umbrella Reference)"
slug: charitable-planning
type: Itemized Ded
tax_type: EFR
complexity: Low
irc_sections: ["§170", "§408(d)(8)", "§642(c)", "§664", "§642(c)(5)"]
forms: ["Schedule A", "Form 8283", "Form 5227 (split-interest trust)"]
state_specific: true
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

This file is the umbrella reference for charitable planning,
cross-referencing the more specific charitable strategies. Major
charitable vehicles and techniques:

1. **Direct giving (#51).** Cash or appreciated property to public
   charity or private foundation.

2. **Donor Advised Fund (DAF) (#54).** Single contribution → DAF;
   donor recommends grants over time. Immediate deduction;
   tax-free growth in DAF.

3. **Qualified Charitable Distributions (QCDs) (#78).** From IRA
   directly to charity; up to $105,000 (2024); satisfies RMD;
   excluded from gross income.

4. **Charitable Remainder Trust (CRT).** Donor contributes property
   to trust; trust pays donor (or beneficiary) annuity or unitrust
   payment for term; remainder to charity. Deduction at funding
   for present value of remainder interest.

5. **Charitable Lead Trust (CLT).** Reverse of CRT — charity
   receives annuity for term, remainder to family. Estate / gift
   tax planning vehicle.

6. **Private Foundation.** Donor establishes §501(c)(3) private
   foundation; donor maintains control over grants. Deduction
   limits (30% AGI for cash; 20% AGI for appreciated). §4940 net
   investment income excise tax.

7. **Private Operating Foundation.** Treated more favorably than
   private non-operating foundation (50% / 30% AGI limits).

8. **Pooled Income Fund.** Charity-administered fund pooling
   contributions; donor receives pro rata share of fund income for
   life.

9. **Charitable Gift Annuity.** Donor transfers property to
   charity in exchange for annuity for life; immediate partial
   deduction.

10. **Bargain Sale.** Sale to charity at less than FMV; treated
    partly as sale and partly as charitable gift.

11. **Conservation Easement.** Donation of property restriction
    for conservation; requires careful structure. Syndicated
    conservation easements are listed transactions (Notice 2017-10).

The charitable planning decision tree:

**Q1: Is donor at or near required minimum distribution age?**
- Yes + has IRA → consider QCD (#78). Excellent option.

**Q2: Does donor want to time deduction now but make grants later?**
- Yes → DAF (#54).

**Q3: Does donor want lifetime income from contributed assets?**
- Yes → CRT or charitable gift annuity.

**Q4: Does donor want family to inherit appreciation?**
- Yes → CLT.

**Q5: Does donor want active control over grant-making?**
- Yes → Private foundation (with awareness of restrictions).

**Q6: Simple appreciated stock gift?**
- Yes → direct gift (#51) or to DAF.

## Primary IRC authority

- §170 — Charitable deduction.
- §408(d)(8) — QCD.
- §642(c) — Charitable trust deduction.
- §664 — Charitable remainder trust.
- §170(f)(2) — CRT and CLT rules.
- §170(h) — Conservation easement.
- §509 — Private foundation classification.
- §4940-4945 — Private foundation excise taxes.

## Treasury regulations

- Reg §1.170A-1 through §1.170A-17.
- Reg §1.664-1 through §1.664-4.
- Reg §1.642(c)-1 through §1.642(c)-7.

## Key IRS guidance

- IRS Publication 526.
- IRS Publication 561.
- IRS Publication 4221-PF (private foundations).
- IRS Publication 4221-PC (public charities).

## Cross-references

This file is a router; specific authorities live in cross-
referenced files.

- `charitable-donation-appreciated` (#51) — primary direct giving.
- `donor-advised-fund` (#54).
- `qcd` (#78).
- `gifting-stock` (#46).
- `charitable-llc` (#52) — caution flag.
- `family-limited-partnership` (#55) — caution flag.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {"authority_type":"IRC","citation":"I.R.C. § 170","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section170","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 664","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section664","weight":"primary_statute"},
    {"authority_type":"IRC","citation":"I.R.C. § 408(d)(8)","url":"https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section408","weight":"primary_statute"}
  ]
}
```
