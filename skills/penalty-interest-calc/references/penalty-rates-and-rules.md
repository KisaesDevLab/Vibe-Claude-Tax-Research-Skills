# Penalty rates and rules — quick reference

For tax years 2024+ — verify year-specific Rev. Proc. and IRS
quarterly Rev. Rul. (interest rates) before quoting figures.

## §6651 family

### §6651(a)(1) FTF

- Rate: 5% per month (or fraction).
- Cap: 25% of unpaid tax.
- §6651(g) minimum (60+ days late): LESSER of $510 (2024) or 100%
  of unpaid tax.
- §6651(f) fraud: 15% per month / 75% cap.

### §6651(a)(2) FTP

- Rate: 0.5% per month (or fraction).
- Cap: 25% of unpaid tax.
- §6651(d) installment agreement: reduced to 0.25% / month.
- §6651(d) post-levy-demand: increased to 1.0% / month.

### §6651(a)(3) FTD

- 2% / 5% / 10% / 15% based on lateness (see SKILL).

### §6651 interaction

- Combined §6651(a)(1) + §6651(a)(2) = 5% / month effective until
  cap.
- The §6651(a)(1) rate is reduced by the §6651(a)(2) rate when
  both apply in the same month.

## §6654 individual estimated tax

- Rate: federal short-term rate + 3% (§6621(a)(2)).
- Computed quarter-by-quarter on Form 2210.
- §6654(d)(1)(B) safe harbors:
  - 90% of current-year tax; OR
  - 100% of prior-year tax (110% if AGI > $150K).
- §6654(e) waivers:
  - First-year retiree (age 62+) / first-year disability
    (§6654(e)(3)(B)).
  - Casualty / disaster.
  - Other unusual circumstances.

## §6655 corporate estimated tax

- Similar mechanism.
- Form 2220 computation.
- §6655(d) — large corp must base on current-year tax (90% safe
  harbor only); 100%-prior-year safe harbor only for Q1.
- §6655(e) annualized-installment method.

## §6662 accuracy-related

20% on understatement portion attributable to:

| Subsection | Type |
|---|---|
| §6662(b)(1) | Negligence or disregard |
| §6662(b)(2) | Substantial understatement of income tax |
| §6662(b)(3) | Substantial valuation misstatement (≥ 150% of correct value) |
| §6662(b)(4) | Substantial overstatement of pension liabilities |
| §6662(b)(5) | Substantial estate or gift valuation understatement |
| §6662(b)(6) | Disallowance of claimed tax benefits by reason of transaction lacking economic substance |
| §6662(b)(7) | Undisclosed foreign financial asset underpayment |
| §6662(b)(8) | Inconsistent estate-basis reporting |

40% under:
- §6662(h) gross-valuation-misstatement (≥ 200%).
- §6662(i) non-disclosed §6662(b)(6) ESD-failed transactions.
- §6662(j) non-disclosed foreign financial asset.

§6664(c) reasonable-cause defense AVAILABLE for §6662(b)(1)–(5).
NOT AVAILABLE for §6662(b)(6) (per §6664(c)(2) — strict
liability for ESD).

## §6663 fraud

- 75% on the underpayment portion.
- §6663(b) IRS bears burden of proof by clear and convincing
  evidence.
- Cannot stack with §6662 on the same underpayment.
- §6663(c) joint-return — applies separately to each spouse based
  on their fraud.

## §6672 Trust Fund Recovery Penalty

- 100% of trust-fund liability.
- Personal liability against responsible persons.
- Joint-and-several.
- See `tax-research-payroll/references/tfrp-and-collection.md` for
  procedural details.

## §6699 (S-corp) and §6698 (partnership) late-filing

- $245 per shareholder / partner per month (2024 — verify).
- Maximum 12 months.
- FTA available under IRM 20.1.1.3.6 (recently expanded to
  §6698 / §6699 — verify current eligibility).
- Reasonable-cause defense available.

## §6707A reportable transaction

Penalty for failure to disclose a reportable transaction (Form
8886):
- Listed transactions: 75% of the decrease in tax shown on the
  return (max $200K per transaction; min $10K).
- Other reportable transactions: 75% (max $50K; min $5K).

## §6701 aiding and abetting

$1,000 per misstatement ($10,000 for corporate aided).

## §6700 promoter penalty

50% of gross income from the promoted activity (or $1,000 per
sale).

## §6707 non-disclosure of reportable transaction by material advisor

$50,000 to $200,000 per failure to disclose (depends on type).

## §6694 / §6695 return-preparer penalties

§6694(a): unreasonable position — $1,000 per return (or 50% of
fee earned).
§6694(b): willful or reckless conduct — $5,000 per return (or
75% of fee).
§6695(a-h): various preparer-procedure penalties.

## Interest under §6601 / §6621

§6601 — interest on underpayments.
§6621(a)(2) — rate: federal short-term rate + 3%.
§6621(c) — large-corp hot interest: federal short-term + 5% on
underpayments > $100K.
§6622 — daily compounding.

Federal short-term rate set quarterly by IRS Rev. Rul. published
before each quarter. Verify current rate.

Quick reference (verify against current Rev. Rul.):

| Period | §6621(a)(2) rate (general) |
|---|---|
| Q1 2024 | 8% |
| Q2 2024 | 8% |
| Q3 2024 | 8% |
| Q4 2024 | 8% |
| Q1 2025 | (verify) |

## Computation examples

### Example 1: §6651(a)(1) + §6651(a)(2)

- Tax due: $10,000.
- Filing 4 months late, paid at filing.
- §6651(a)(1) FTF: 5% × 4 months = 20% × $10K = $2,000 (uncapped
  at 25%).
- §6651(a)(2) FTP: 0.5% × 4 months = 2% × $10K = $200.
- Combined: §6651(a)(1) effective rate is reduced by §6651(a)(2),
  so:
  - §6651(a)(1): 4.5% × 4 = 18% × $10K = $1,800.
  - §6651(a)(2): 0.5% × 4 = 2% × $10K = $200.
  - Total: $2,000.

### Example 2: §6662(b)(2) substantial understatement

- Total tax shown on return: $40,000.
- Correct tax: $58,000.
- Understatement: $18,000.
- Substantial-understatement threshold: greater of $5,000 or 10%
  of correct tax = greater of $5,000 or $5,800 = $5,800.
- Understatement of $18,000 > $5,800 → §6662(b)(2) applies.
- Penalty: 20% × $18,000 = $3,600.

### Example 3: §6601 interest

- Underpayment: $50,000.
- Period: April 15, 2024 to April 15, 2025 (1 year).
- §6621(a)(2) rate: 8% (assumed).
- Daily compounding under §6622.
- Approximate interest: $50,000 × ((1 + 0.08/365)^365 − 1) ≈
  $4,164.

## Practitioner audit-defense file

- [ ] Penalty type identified (§6651 / §6662 / §6663 / §6672 /
  §6699 etc.).
- [ ] Year-specific rates confirmed (Rev. Proc. and quarterly
  Rev. Rul. for §6601 / §6621).
- [ ] FTA screened first if §6651 family.
- [ ] Reasonable-cause defense considered (§6664(c) for §6662;
  §6651 for §6651 family).
- [ ] §6664(c)(2) strict-liability for §6662(b)(6) flagged.
- [ ] §6601 interest computed with daily compounding.
- [ ] Combined-penalty interactions analyzed (e.g., §6651(a)(1) +
  §6651(a)(2)).
