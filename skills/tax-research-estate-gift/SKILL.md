---
name: tax-research-estate-gift
description: |
  Federal estate, gift, and generation-skipping-transfer (GST) tax
  research skill. Covers §2031 / §2033 inclusion, §2010 unified
  credit, §2503(b) annual exclusion, §2522 / §2055 charitable
  deductions, §2056 marital deduction (incl. QTIP, QDOT),
  portability under §2010(c)(4), §2032 alternate valuation, §6166
  installment payment, GST §2611 and §2632 GST exemption
  allocation. Use when the user asks "estate tax", "gift tax",
  "GST", "Form 706", "Form 709", "Form 706-NA", "QTIP election",
  "portability", "DSUE", "annual exclusion", "alternate valuation",
  "§2010 exclusion", "§6166 installment", or "estate planning". Make
  sure to use this skill whenever the user mentions estate tax,
  gift tax, GST, Form 706, Form 709, QTIP, or portability.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-estate-gift — Estate / gift / GST research

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA Pub. L. 115-97 doubled
   §2010 exclusion through 2025; OBBBA modifications must be
   verified.
6. `references/exclusions-and-deductions.md` — §2010 / §2503 /
   §2522 / §2055 / §2056 with computation examples.
7. `references/gst-mechanics.md` — §2611 / §2632 GST exemption
   allocation.

## Operative authority

- IRC §2001 — imposition of estate tax.
- IRC §2010 — unified credit / exclusion.
- IRC §2010(c)(4) — DSUE / portability.
- IRC §§2031–2046 — gross-estate inclusion.
- IRC §2032 — alternate valuation.
- IRC §§2053–2056 — deductions (admin expenses, marital).
- IRC §2055 — charitable deduction.
- IRC §§2501–2524 — gift tax.
- IRC §2503(b) — annual exclusion.
- IRC §§2611–2664 — GST tax.
- IRC §2632 — GST exemption allocation.
- IRC §6166 — installment payment of estate tax.
- IRC §6019 — gift-tax return filing.
- Treas. Reg. §§20.2010-1 through -3 — DSUE.
- Treas. Reg. §20.2010-1(c) — anti-clawback rule.

## Workflow

### 1. Intake

- `decedent_or_donor_info`: estate vs. gift posture; date of
  death / gift.
- `tax_year`.
- `gross_estate_estimate` (estate) or `gift_amount` (gift).
- `marital_status` and `surviving_spouse_facts`.
- `children_grandchildren_facts` (for GST allocation).
- `state_residency`: state estate tax (CT, HI, IL, ME, MD, MA, MN,
  NY, OR, RI, VT, WA + DC) and state-specific exemption levels.
- `prior_lifetime_gifts`: §2001(b)(2) adjusted taxable gifts.
- `pending_planning_actions`: DAFs, QPRTs, GRATs, ILITs, IDITs,
  CRTs, etc.

### 2. Gross estate inclusion

§2031 / §2033 — value of property owned at death.

§§2034-2046 specific inclusion provisions:
- §2035 transfers within 3 years of death (limited post-1981).
- §2036 retained life estate / income / control.
- §2037 transfers taking effect at death.
- §2038 revocable transfers.
- §2039 annuities.
- §2040 joint tenancy.
- §2041 powers of appointment.
- §2042 life insurance.

### 3. Deductions

§2053 — funeral and administration expenses, debts.
§2054 — casualty / theft losses.
§2055 — charitable deduction (unlimited, with 50% / 30% / 20%
type distinctions).
§2056 — marital deduction:
- §2056(a) — outright bequest to U.S. citizen spouse.
- §2056(b)(7) — QTIP property: marital deduction for property in
  which spouse has qualifying income interest for life.
- §2056(d) — QDOT for non-citizen spouse.

### 4. Exclusion / unified credit

§2010(c) — basic exclusion amount + DSUE.

For 2025: $13.99M basic exclusion (verify year-specific). DSUE
may add up to $13.99M more (from predeceased spouse who elected
portability on Form 706).

§2010(c)(4) DSUE — portability:
- Filed timely on Form 706 by predeceased spouse's estate.
- Late portability relief: Rev. Proc. 2022-32 — automatic for
  estates not required to file Form 706.

§2010(c)(3) — basic exclusion sunsets 12/31/2025 absent
extension; reverts to ~$7M (inflation-adjusted) for 2026+.
Treas. Reg. §20.2010-1(c) anti-clawback rule preserves the
benefit of pre-sunset gifts.

OBBBA may have permanent — verify per Classification Tables.

### 5. Annual exclusion

§2503(b) — $19,000 / donee for 2025 (verify year-specific).

§2503(b)(2) — present-interest requirement; Crummey withdrawal
power often used in trust contexts.

§2503(c) — minor's trust special rules.

§2503(e) — direct payments for educational and medical care
(unlimited; no annual exclusion impact).

§529(c)(2)(B) — 5-year-front-load for §529 contributions.

### 6. Generation-skipping transfer (GST) tax

§2611 — taxable termination, taxable distribution, direct skip.

§2632 — GST exemption allocation:
- $13.99M basic exemption 2025 (verify; identical to estate
  basic exclusion).
- Automatic-allocation rules and elections.

GST tax rate: 40% (matches highest estate / gift rate, §2641).

§2632(a)(1) — GST exemption may be allocated to:
- Direct skip transfers automatically.
- Indirect skips automatically per §2632(c) (post-EGTRRA).
- Other transfers via election.

### 7. Special-use valuation and §6166

§2032A — special-use valuation for qualified family farms /
businesses; reduces value by up to $1.39M (2024 — verify).

§6166 — installment payment of estate tax for estates > 35% of
adjusted gross estate consisting of closely-held business
interests; 14-year payment period with deferred-interest 10-year
period.

### 8. Estate-planning structures

Common structures (route to specialist; this skill flags rather
than implements):
- Revocable living trust.
- ILIT (Irrevocable Life Insurance Trust) — §2042 inclusion
  avoidance.
- GRAT (Grantor Retained Annuity Trust) — §2702 mechanics.
- QPRT (Qualified Personal Residence Trust) — §2702.
- IDIT / IDGT (Intentionally Defective Grantor Trust) — sale to
  trust.
- CRT / CRAT / CRUT (Charitable Remainder Trust) — §664.
- CLAT / CLUT (Charitable Lead Trust) — §170(f)(2).
- DAF (Donor-Advised Fund) — §170 deduction.

### 9. State estate / inheritance tax

State estate tax states (verify per per-state file):
- CT, DC, HI, IL, ME, MD, MA, MN, NY, OR, RI, VT, WA.

State inheritance tax states (different mechanism):
- IA (repealed), KY, MD (both estate and inheritance), NE, NJ,
  PA.

Per-state exemption levels often LOWER than federal; state estate
tax planning often the binding constraint for taxpayers below the
federal threshold.

Route per-state estate / inheritance issues to
`tax-research-state-income` per-state file (state estate tax is
typically administered by the state DOR even though it's not
income tax).

### 10. Conclusion + sidecar

JSON sidecar validates against `shared/output-schema.json`.
Confidence band per `shared/confidence-bands.md`.

For TCJA-sunset / OBBBA-permanence-related questions, populate
`public_laws_consulted[]`.

## Hard rules

- Always identify whether question is gift, estate, or GST.
- Always verify §2010 exclusion against year-specific Rev. Proc.
- Always check portability (DSUE) availability for surviving-
  spouse questions.
- Never claim Chevron deference for Treas. Reg. §20.2010-1
  anti-clawback (post-Loper Bright Skidmore review).
- For state estate-tax questions, route to
  `tax-research-state-income` per-state file.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. For high-stakes positions (multi-
million-dollar gifts, complex trust structures), include the
negative-treatment-review residual practitioner responsibility.
