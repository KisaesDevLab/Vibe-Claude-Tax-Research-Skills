---
name: "Ordinary Loss on Worthless Stock (§165(g) and §1244)"
slug: worthless-stock-ordinary-loss
type: Business Sale
tax_type: EFR
complexity: Low
irc_sections: ["§165(g)", "§1244"]
forms: ["Form 8949", "Schedule D", "Form 4797"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Two distinct provisions allow loss recognition on worthless stock:

**§165(g) — Worthless securities (capital loss):** A security that
becomes wholly worthless during the taxable year creates a capital
loss as if the security were sold on the last day of the year for
zero. This is the default treatment for most stock that becomes
worthless.

**§1244 — Ordinary loss on small business stock:** Stock issued by a
qualifying small business corporation, when sold or worthless,
creates an ordinary loss (rather than capital loss) up to $50,000
single / $100,000 MFJ per year. Excess loss treated as capital loss.
This is a powerful rule for entrepreneurs whose business fails.

§1244 requires the stock to be:
1. Issued by a "small business corporation" (aggregate amount
   received for stock + paid-in surplus ≤ $1,000,000 at time of
   issuance).
2. Issued for money or property (not for services or other stock).
3. Held by the original purchaser (no transferees).
4. Issued by a corporation that derives more than 50% of its
   receipts from active trade or business (over the 5 prior years
   or, if shorter, all of operations).

§1244 is one of the most under-utilized provisions in the Code
because (a) practitioners often forget about it when a small business
fails, and (b) documentation requirements at issuance (a §1244
designation in the corporate records) are routinely omitted at
formation.

## Primary IRC authority

- **§165(a)** — Losses generally deductible.
- **§165(c)** — Losses for individuals limited to certain
  categories.
- **§165(g)** — Worthless securities.
- **§165(g)(3)** — Worthless securities of affiliated corporation
  (operating loss treatment).
- **§166** — Bad debts.
- **§1244** — Losses on small business stock.
- **§1211** — Limitation on capital losses ($3,000 ordinary income
  offset for individuals).
- **§1212** — Capital loss carryovers.

## Treasury regulations

- **Reg §1.165-5** — Worthless securities.
- **Reg §1.1244-1 through §1.1244-6** — §1244 implementing
  regulations.

## Key IRS guidance

- IRS Publication 535 — Business Expenses (§166 bad debt).
- IRS Publication 550 — Investment Income and Expenses.

## Key court decisions

- **Boehm v. Commissioner, 326 U.S. 287 (1945)** — Worthlessness
  must be evidenced by an "identifiable event" — the year of
  worthlessness is a question of fact.
- **Morton v. Commissioner, 38 B.T.A. 1270 (1938), aff'd, 112 F.2d
  320 (7th Cir. 1940)** — Stock not "wholly worthless" if any
  reasonable hope of recovery remains.

## Eligibility requirements

For §165(g) capital loss:
1. Security is a "security" within meaning of §165(g)(2) — generally
   includes stock and bonds in registered form.
2. Security becomes "wholly worthless" during the year.
3. Worthlessness evidenced by identifiable event — bankruptcy
   liquidation, etc.

For §1244 ordinary loss:
1. Stock issued by domestic corporation.
2. Corporation was "small business corporation" at time of issuance
   (≤$1M aggregate paid-in capital).
3. Stock issued for money or property other than stock or
   securities.
4. Taxpayer is the original purchaser of the stock.
5. Corporation derives >50% of receipts from active trade/business
   (not investments) over 5 prior years.

## Mechanics — how it works

For §165(g):
1. **Establish worthlessness in current year.** Document
   identifiable event (bankruptcy, dissolution, etc.).
2. **Compute loss.** Adjusted basis (typically purchase price + any
   capital contributions).
3. **Report on Form 8949 / Schedule D.** Treated as long-term capital
   loss if held >1 year; short-term otherwise.
4. **§1211(b) $3,000 ordinary income offset** for individuals;
   excess carries forward.

For §1244:
1. **Establish §1244 status at issuance** (this is the hardest
   part). Document in corporate minutes that stock is §1244 stock.
2. **Track basis** to original cost (no step-up; no transferees).
3. **At loss event,** report §1244 ordinary loss up to $50,000 /
   $100,000 limit on Form 4797 (ordinary loss). Excess on Form 8949
   / Schedule D as capital loss.

## Documentation requirements

For §165(g):
- Stock certificate or DRS evidence of ownership.
- Documentation of identifiable worthlessness event.
- Purchase records for basis.

For §1244:
- Corporate minutes designating stock as §1244 stock at issuance.
- Corporation's gross receipts records over 5 prior years.
- Original purchase documentation (no transferees).
- $1M paid-in-capital cap evidence.

## Common pitfalls / audit risks

- **Worthlessness in wrong year.** Identifiable-event timing matters.
  IRS may argue worthlessness occurred in prior year (refund barred)
  or future year (premature deduction).
- **§1244 not documented at formation.** Single biggest issue. The
  designation must be made at issuance, not retroactively.
- **§1244 stock to transferee.** §1244 status doesn't carry to
  transferees (donee, heir, second-hand purchaser).
- **§1244 "small business corporation" determination.**
  Documentation of $1M cap and 50% active receipts test.
- **§1244 LLC stock.** §1244 applies only to corporate stock; LLC
  membership interests do not qualify (taxed as partnership unless
  C-corp election).
- **§166 bad debt vs. §165(g) worthless security.** Different
  treatment depending on instrument and relationship.

## Recent legislative changes

- No material recent statutory changes to §165(g) or §1244.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1244 §165
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §165(g) and §1244 is generally complete.

## AICPA SSTS / Circular 230 considerations

The most common compliance issue is failure to claim §1244 ordinary
treatment because of inadequate documentation at issuance. SSTS §1.4
reasonable inquiry into client's prior corporate documentation at
the time of loss recognition.

## Default confidence band rationale

**HIGH** for properly-documented §1244 elections and clear-cut
worthlessness events. Drops to MODERATE when worthlessness timing
is uncertain or when §1244 documentation is reconstructed from
secondary sources.

## Cross-references

- **`nol-carryback-carryforward`** (#15) — §1244 ordinary loss
  becomes part of NOL.
- **`section-1202-qsbs-extended`** (#43) — companion provision for gain
  exclusion (opposite outcome).
- **`installment-sale`** (#33) — alternative if business sells
  rather than fails.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 165(g)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section165",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1244",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1244",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.1244-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "Boehm v. Commissioner, 326 U.S. 287 (1945)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    }
  ]
}
```
