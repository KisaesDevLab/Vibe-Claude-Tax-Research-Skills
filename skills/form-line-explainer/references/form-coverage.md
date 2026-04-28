# Form coverage and citation chains

For each common form, document the year-specific revision used,
the line / box / schedule structure, and the citation chain.

## Form 1040

Year-specific revisions; line numbers shift annually. Use the
year-appropriate version of `return-summary-1040/references/line-keys.md`.

Key citation chains:
- Line 1a (W-2 wages) → §61(a)(1), §3401(a), §3402.
- Line 11 (AGI) → §62.
- Line 12 (standard deduction OR itemized) → §63, §67.
- Line 13 (QBI deduction) → §199A.
- Line 15 (taxable income) → §63.
- Line 16 (tax) → §1, §1(j).
- Line 17 (Schedule 2 additions: AMT, etc.) → §55.

## Form 1120 / 1120-S / 1065

Use the line-keys references in `return-summary-entity/references/`.

## Form 941 (employer's quarterly federal tax return)

Boxes 1-13:
- Number of employees.
- Wages, tips, etc. — §3401(a) / §3121(a) wages.
- Federal income tax withheld — §3402.
- Taxable Social Security wages — §3121(a) up to wage base.
- Taxable Social Security tips — §3121(q).
- Taxable Medicare wages and tips — §3101(b) (no cap).
- Total taxes before adjustments.
- Section 3121(q) Notice and Demand — Tax Due on Unreported Tips.
- ...

## Form 940 (FUTA)

Annual employer's federal unemployment-tax return.
- §3301 — 6% gross rate.
- §3302 — credit for state UI taxes paid timely (up to 5.4%).
- §3306(c)(7) — domestic-service exception.

## Form 706 / 706-NA (estate tax)

Schedule by schedule:
- Schedule A: Real Estate.
- Schedule B: Stocks and Bonds.
- Schedule C: Mortgages, Notes, Cash.
- Schedule D: Insurance on Decedent's Life.
- Schedule E: Jointly Owned Property.
- Schedule F: Other Miscellaneous Property.
- Schedule G: Transfers During Decedent's Life.
- Schedule H: Powers of Appointment.
- Schedule I: Annuities.
- Schedule J: Funeral Expenses and Expenses Incurred in
  Administering Property Subject to Claims.
- Schedule K: Debts of the Decedent and Mortgages and Liens.
- Schedule L: Net Losses During Administration / Expenses
  Incurred in Administering Property Not Subject to Claims.
- Schedule M: Bequests, etc., to Surviving Spouse (Marital
  Deduction).
- Schedule O: Charitable, Public, and Similar Gifts and Bequests.
- Schedule P: Credit for Foreign Death Taxes.
- Schedule Q: Credit for Tax on Prior Transfers.
- Schedule R: Generation-Skipping Transfer Tax.
- Schedule R-1: Generation-Skipping Transfer Tax — Direct Skips
  from a Trust — Payment Voucher.
- Schedule U: Qualified Conservation Easement Exclusion.

## Form 709 (gift tax)

- Schedule A: gifts subject to gift tax.
- Schedule B: gifts of prior years (used in computing tentative
  tax).
- Schedule C: DSUE / portability allocation.
- Schedule D: GST tax on direct skips.

## Schedule A (itemized deductions)

- Line 1: Medical and dental expenses (§213).
- Line 5: SALT (state and local taxes — §164, capped at $10K
  per §164(b)(6) post-TCJA).
- Line 8: Interest paid (§163).
- Line 11: Charitable contributions (§170).
- Line 15: Casualty and theft losses (§165 — limited to disaster
  losses post-TCJA).
- Line 16: Other miscellaneous (post-TCJA limited per §67(g)).

## Schedule B (interest and dividends)

- Part I: Interest income (§61(a)(4)).
- Part II: Ordinary dividends (§61(a)(7)).
- Part III: Foreign accounts (FBAR / Form 8938 trigger).

## Schedule C (sole proprietor)

- Line 1: Gross receipts.
- Line 4: Cost of goods sold (Form 1125-A).
- Lines 8-25: deductions.
- Line 28: Total expenses.
- Line 31: Net profit / loss → Form 1040 Line 8 (other income).
  Net SE income → Schedule SE.

## Schedule D (capital gains / losses)

- §1(h) capital-gains rates.
- §1211(b) net capital loss limit ($3,000 / year against ordinary
  income; carryforward).
- §1091 wash-sale rule.
- §1411 NIIT on net investment income.

## Schedule E (rental real estate, royalties, partnerships,
S-corps, trusts)

- Part I: Rental real estate.
- Part II: Income or loss from partnerships and S-corps (K-1).
- Part III: Income or loss from estates and trusts (K-1).
- §469 passive-activity loss limitation considerations.
- §163(j) limitation if applicable.

## Form 8949 (sales and other dispositions of capital assets)

- Box A: short-term covered (1099-B reported with basis).
- Box B: short-term covered (1099-B reported without basis).
- Box C: short-term not on 1099-B.
- Box D: long-term covered.
- Box E: long-term covered, no basis reported.
- Box F: long-term not on 1099-B.
- Adjustment codes column (g): wash-sale, §1031, §453, §1202
  exclusion, etc.

## Form 8606 (nondeductible IRA)

- Tracks basis in Traditional IRAs (§408).
- Required for any nondeductible Traditional IRA contribution.
- Triggers pro-rata calculation under §408(d)(2) for
  partial-conversion / partial-withdrawal scenarios.

## Form 4562 (depreciation and amortization)

- Part I: §179 expensing.
- Part II: §168(k) bonus depreciation.
- Part III: MACRS depreciation.
- Part IV: §167 / §168 detailed schedules.
- Part V: §280F listed property.
- Part VI: §197 amortization (intangibles).

## Form 4797 (sales of business property)

- §1231 / §1245 / §1250 character analysis.
- §1245 ordinary recapture.
- §1250 unrecaptured-§1250 gain (max 25% rate per §1(h)(11)).

## Form 8825 (rental real estate income / expense for
partnerships and S-corps)

- Allocates rental real estate items by property.
- Reconciles to Schedule K Line 2.

## Form 5471 / 5472 / 8865 / 8858

International information returns. Route to
`tax-research-international` for substantive analysis.

## Form 8938 (specified foreign financial assets)

§6038D — specified foreign financial assets > thresholds
(varies by filing status and residency).

## Form 8606 / 8915-F / etc. — special-purpose forms

Year-specific forms; route to relevant skill for substantive
analysis.

## Common cross-form citation

| Form | Underlying section |
|---|---|
| W-2 Box 1 | §3401(a) wages |
| W-2 Box 3 | §3121(a) (FICA wages, capped at OASDI base) |
| W-2 Box 5 | §3121(b) (Medicare wages, uncapped) |
| W-2 Box 12 D | §401(k) elective deferrals (reduces Box 1, NOT Box 3/5) |
| W-2 Box 12 W | HSA contributions made through employer (§223) |
| W-2 Box 14 | Other (informational) |
| 1099-NEC | §3508 statutory non-employee, §3121(d)(2), §6041, §6041A |
| 1099-MISC | §6041 / §6041A |
| 1099-DIV | §301 / §316 — dividend |
| 1099-INT | §61(a)(4) interest |
| 1099-B | §6045 broker reporting |
| 1099-S | §6045(e) gross-proceeds-from-real-estate-transactions reporting |
| 1099-K | §6050W third-party-network reporting (gross before refunds) |
| 1099-R | §72 / §401(k) / §408 distributions from retirement |
| 1099-SA | §223(d) HSA distributions |
| 5498 | §408(i) IRA contribution reporting |

## Year-specific revisions

When responding to a form-line question:
1. Confirm tax year.
2. Pull the year-specific form / instructions from
   `https://www.irs.gov/forms-instructions`.
3. Note any changes in line numbering from prior year.
4. Cite the year-specific form / instructions in the JSON
   sidecar.
