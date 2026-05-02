# Vibe CPA Skills — Strategy Library Addendum (94 Strategies)

**Part 4 of 10** — Strategies #28 through #37.

**Part navigation:**
- Part 1: Exec summary, master index, PART A build-plan addendum, strategies #1–#7
- Part 2: Strategies #8–#17
- Part 3: Strategies #18–#27
- **Part 4: Strategies #28–#37** ← this file
- Part 5: Strategies #38–#47
- Part 6: Strategies #48–#57
- Part 7: Strategies #58–#67
- Part 8: Strategies #68–#77
- Part 9: Strategies #78–#86
- Part 10: Strategies #87–#94 + cross-reference matrix

---

## Strategy #28: De Minimis Safe Harbor

**File:** `references/strategies/de-minimis-safe-harbor.md`

```markdown
---
name: "De Minimis Safe Harbor for Small Asset Purchases (Reg §1.263(a)-1(f))"
slug: de-minimis-safe-harbor
type: Business - Other
tax_type: EFR
complexity: Medium
irc_sections: ["§263(a)"]
forms: ["No specific form; election made annually on timely return"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

The de minimis safe harbor under Reg §1.263(a)-1(f) — part of the
2014 "Tangible Property Regulations" — allows a taxpayer to elect to
deduct (rather than capitalize) tangible property under a per-item
threshold:

- **$5,000 per item** for taxpayers with an "applicable financial
  statement" (AFS) — generally a CPA-audited or reviewed financial
  statement filed with SEC, or used for certain credit/regulatory
  purposes.
- **$2,500 per item** for taxpayers without an AFS.

The election covers:
- Tangible property other than inventory or land.
- Property under the threshold per invoice or per item (as
  substantiated on invoice).

Annual election required by attaching statement to timely-filed
return. Plan must:
1. Treat amounts under threshold as deductible for non-tax purposes
   (book treatment matches tax for AFS taxpayers).
2. Have written accounting policy at the start of the year (for
   AFS taxpayers).

The strategy is foundational for small businesses and an essential
companion to the §168(k) / §179 strategy (#12). For items under
$2,500 ($5,000 with AFS), the de minimis safe harbor is simpler
than tracking §168 depreciation or §179 elections.

## Primary IRC authority

- **§263(a)** — Capital expenditures.
- **§162(a)** — Ordinary and necessary business expenses.

## Treasury regulations

- **Reg §1.263(a)-1(f)** — De minimis safe harbor.
- **Reg §1.263(a)-1(f)(1)(ii)(D)** — Definition of applicable
  financial statement.
- **Reg §1.263(a)-2** — Amounts paid to acquire tangible property.
- **Reg §1.263(a)-3** — Amounts paid to improve tangible property.
- **Reg §1.263(a)-4** — Amounts paid to acquire intangibles.

## Key IRS guidance

- **Notice 2015-82** — Increased threshold from $500 to $2,500 for
  non-AFS taxpayers.
- **Rev. Proc. 2015-20** — Procedures for small businesses to
  apply tangible property regs without filing Form 3115.

## Key court decisions

- Limited dispute area; rules are mechanical.

## Eligibility requirements

For non-AFS taxpayer:
1. Item cost ≤$2,500 per item (per invoice or substantiated per
   item).
2. Annual election attached to timely-filed return.
3. Property is not inventory.

For AFS taxpayer:
1. Item cost ≤$5,000.
2. Written accounting procedure in effect at start of year.
3. Treats amounts under threshold as expensed for AFS purposes.
4. Annual election.

## Mechanics — how it works

1. **Adopt written accounting policy** (AFS taxpayers — required
   by start of year; non-AFS taxpayers — recommended but not
   required by statute).
2. **Apply threshold per item.** Single invoice for multiple items
   — threshold per item, not per invoice.
3. **Deduct items under threshold** as ordinary business expense
   in year placed in service.
4. **Items over threshold** continue under §168 depreciation /
   §179 / §168(k) bonus.
5. **Annual election** via attached statement to return.

## Documentation requirements

- Written accounting policy (AFS) or evidence of consistent
  treatment.
- Election statement attached to return.
- Invoices substantiating per-item cost.

## Common pitfalls / audit risks

- **Failure to make annual election.** Election is required each
  year; failure means default capitalization rules apply.
- **AFS threshold confusion.** Many small businesses assume $5,000
  applies; actual non-AFS limit is $2,500.
- **Per-invoice vs. per-item.** Threshold applies per item, not
  per invoice. A single invoice for ten $2,000 chairs ($20,000
  total) — each chair item is under $2,500 and qualifies.
- **No written policy at start of year (AFS).** Disqualifies
  election for AFS taxpayers.
- **Inventory items.** Inventory does not qualify regardless of
  per-item cost.

## Recent legislative changes

- **2014 Final Tangible Property Regulations** — Original framework.
- **Notice 2015-82** — Threshold increase.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA tangible
  property regulations §263 Pub L 119-21]`. Working assumption: no
  changes; threshold remains $2,500 / $5,000.

## State conformity considerations

State conformity to Reg §1.263(a)-1(f) is generally complete.

## AICPA SSTS / Circular 230 considerations

Standard diligence; routine planning area.

## Default confidence band rationale

**HIGH** — explicit regulatory safe harbor with clear IRS-imposed
thresholds.

## Cross-references

- **`bonus-and-section-179-depreciation`** (#12) — companion
  strategy for items over threshold.
- **`maximize-business-deductions`** (#13) — broader framework.
- **`de-minimis-safe-harbor-self-employed`** (#93) — Schedule C
  variant.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 263(a)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section263",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.263(a)-1(f)",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2015-82",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2015-20",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #29: Deferred Sales Trust (DST)

**File:** `references/strategies/deferred-sales-trust.md`

```markdown
---
name: "Deferred Sales Trust (DST)"
slug: deferred-sales-trust
type: Business Sale
tax_type: EFR
complexity: High
irc_sections: ["§453", "§671-679"]
forms: ["Form 6252", "Form 1041 (trust filing)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
aggressive: true
caution: true
confidence_default_band: LOW
last_obbba_review: "N/A"
---

> **AGGRESSIVE STRATEGY WARNING:** Deferred Sales Trust ("DST") is a
> commercially-marketed structure that uses an installment-note sale
> to a non-grantor trust as a deferral mechanism. The IRS has not
> blessed the structure with formal guidance; the principal authority
> cited by promoters (the "monetized installment sale" structures
> related but distinct) is precisely the area the IRS has actively
> challenged. **Notice 2023-34** designated certain monetized
> installment sale transactions as listed transactions requiring
> Form 8886 disclosure. While "Deferred Sales Trust" promoters argue
> their structure differs from the listed monetized installment sale,
> the IRS has not affirmed this distinction. Practitioners advising
> on DST should: (a) verify whether the specific structure falls
> within Notice 2023-34's listed transaction definition, (b)
> recommend Form 8886 disclosure as a precaution if any indicia
> apply, (c) recommend Form 8275 disclosure for the underlying
> §453/§671 position, and (d) understand that this is a high-risk
> position that may not survive IRS challenge.

## Overview

The Deferred Sales Trust (DST) is a commercially-marketed estate
and tax planning structure intended to defer recognition of capital
gains on the sale of appreciated property (real estate, business
interests, etc.). The mechanics:

1. Seller transfers appreciated property to an irrevocable
   non-grantor trust in exchange for a long-term installment note
   secured by the trust's assets.
2. Trust sells the property to a third-party buyer for cash.
3. Trust holds the cash and pays interest and principal to seller
   per the installment note over time.
4. Seller defers gain under §453 (installment sale) until note
   payments are received.
5. Trust invests proceeds; trust earnings (which are paid out as
   note interest to seller) are taxed currently.

The structure is theoretically analogous to a §453 installment sale
to an unrelated buyer. Promoters argue the trust acts as an
unrelated third-party buyer, allowing §453 deferral. Critics (and
likely the IRS) argue the trust is essentially a conduit lacking
economic substance, that the seller retains constructive receipt of
proceeds, and that the structure should be collapsed.

The closely-related "monetized installment sale" structures
(Notice 2023-34, with predecessor guidance Memorandum 20123401F)
were designated as listed transactions requiring Form 8886
disclosure. The DST proponents distinguish their structure from the
listed transaction. The IRS has not formally accepted that
distinction.

## Primary IRC authority

- **§453** — Installment method.
- **§453(b)(1)** — Definition of installment sale.
- **§453(c)** — Installment method recovery.
- **§453(e)** — Related-party rules (potential issue).
- **§453(f)** — Definitions.
- **§453(g)** — Sale of depreciable property to controlled entity
  (potential issue).
- **§453A** — Special rules for nondealer installment sales above
  $150,000 (interest charge on deferred gain).
- **§671-679** — Grantor trust rules (DST is structured as a
  non-grantor trust).
- **§469** — Interaction with passive activity rules.
- **§4965** — Tax-exempt entity prohibited transaction rules
  (some DST variants).

## Treasury regulations

- **Reg §15A.453-1** — Installment method.
- **Reg §1.671-1 through §1.679-2** — Grantor trust rules.

## Key IRS guidance

- **Notice 2023-34** — Designated certain monetized installment
  sale transactions as listed transactions requiring Form 8886
  disclosure. The Notice describes structures where a seller "sells"
  property to a related or controlled intermediary in exchange for
  an installment note, and the intermediary then arranges
  monetization (often via loans secured by the note proceeds).
- **CCA 201747005** — IRS Chief Counsel Advice analyzing a DST-like
  structure; concluded the seller had constructive receipt and
  recharacterized the transaction.
- **PLR 200329010** — One PLR (with limited applicability) appears
  to validate a structure; promoters cite this. PLRs are not
  precedential authority for other taxpayers (§6110(k)(3)).

## Key court decisions

- **Estate of Stranahan v. Commissioner, 472 F.2d 867 (6th Cir.
  1973)** — Pre-payment of an annuity recharacterized as
  constructive receipt; analogous principle.
- No major direct case law specifically on the DST structure.

## Eligibility requirements

If pursuing the structure (with full disclosure of risk to client):

1. Property is a capital asset (real estate, closely-held business
   interest, etc.).
2. Trust is structured as a non-grantor trust with independent
   trustee.
3. Installment note has commercially reasonable terms (fair market
   interest rate, reasonable amortization).
4. Trust has economic substance (independent investment, real
   trustee duties).
5. Seller does not retain control over trust assets or investment
   decisions.
6. Form 8275 disclosure attached to return.
7. Form 8886 disclosure if Notice 2023-34 listed-transaction
   indicia apply.

## Mechanics — how it works (as structured)

1. **Pre-sale planning.** Engage qualified estate planning counsel.
   Set up irrevocable non-grantor trust with independent trustee.
2. **Transfer property to trust** in exchange for long-term
   installment note. The note specifies interest rate, principal
   repayment schedule (typically 10-30 year amortization).
3. **Trust sells property to ultimate buyer** for cash.
4. **Trust invests cash proceeds.**
5. **Trust pays seller per installment note.** Interest payments
   are ordinary income to seller; principal payments trigger
   recognition of deferred capital gain ratably.
6. **§453A interest charge** if total note exceeds $150,000 and
   nondealer status; computed on gross gain.

## Documentation requirements

- Trust formation documents.
- Independent trustee agreement.
- Installment note with commercially reasonable terms.
- Property sale documents.
- Trust investment records.
- Form 8275 disclosure.
- Form 8886 disclosure if applicable.

## Common pitfalls / audit risks

- **Listed transaction designation.** Notice 2023-34 may apply.
- **Constructive receipt challenge.** IRS may argue seller has
  effective control over trust assets.
- **Sham trust / agency challenge.** If trustee lacks independence
  or trust lacks economic substance, structure may be collapsed.
- **§453(e) related-party trap.** If trust is "related" under §453(f)
  attribution rules, accelerated recognition may result.
- **§453A interest charge.** Substantial economic cost on large
  deferrals.
- **State recognition risk.** State may not recognize deferral
  even if federal does (or vice versa).
- **No formal IRS validation.** PLR 200329010 has very limited
  applicability and is not authority for other taxpayers.

## Recent legislative changes

- **Notice 2023-34** — Listed transaction designation for
  monetized installment sales.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §453
  installment sale Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §453 is generally complete. Some states (CA,
NJ) have unique installment sale rules that may not parallel
federal treatment.

## AICPA SSTS / Circular 230 considerations

This is an aggressive position. Practitioner should:
- Review the structure in detail.
- Recommend Form 8275 disclosure.
- Evaluate Form 8886 disclosure under Notice 2023-34.
- Document client's understanding of risks.
- Consider whether the practitioner can satisfy SSTS §1.1 realistic
  possibility standard or whether disclosure is required.

## Default confidence band rationale

**LOW** — Notice 2023-34 listed transaction risk; lack of formal
IRS validation; aggressive economic substance position. The
position is defensible only with extensive disclosure (Form 8275 and
potentially Form 8886) and acceptance of audit risk.

## Cross-references

- **`installment-sale`** (#33) — straightforward §453 alternative.
- **`1031-like-kind-exchange`** (#1) — alternative deferral for
  real estate.
- **`qoz-reinvestment`** (#34) — alternative deferral for capital
  gains.
- **`charitable-llc`** (#52) — different aggressive structure.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 453",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section453",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2023-34",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "CCA",
      "citation": "CCA 201747005",
      "url": "https://www.irs.gov/written-determinations",
      "weight": "written_determinations"
    },
    {
      "authority_type": "CtAppeals",
      "citation": "Estate of Stranahan v. Commissioner, 472 F.2d 867 (6th Cir. 1973)",
      "url": "https://www.courtlistener.com",
      "weight": "binding_circuit"
    }
  ]
}
```
```

---

## Strategy #30: Worthless Stock — Ordinary Loss

**File:** `references/strategies/worthless-stock-ordinary-loss.md`

```markdown
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
- **`section-1202-qsbs`** (#43) — companion provision for gain
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
```

---

## Strategy #31: C Corp Dividends

**File:** `references/strategies/c-corp-dividends.md`

```markdown
---
name: "C Corporation Dividend Planning"
slug: c-corp-dividends
type: C Corp
tax_type: CAG
complexity: Low
irc_sections: ["§301", "§316", "§1(h)(11)", "§531-537"]
forms: ["Form 1099-DIV"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

C corporation dividend planning involves the timing and
characterization of distributions to shareholders. The framework:

1. **§301 / §316:** A distribution is a dividend to the extent of
   the corporation's earnings and profits (E&P). Distributions in
   excess of E&P are first applied against shareholder basis (not
   taxable; basis reduction); any further excess is capital gain.
2. **§1(h)(11) qualified dividend rate:** Most dividends to
   individual shareholders are taxed at preferential long-term
   capital gains rates (0%, 15%, or 20% based on taxable income
   threshold).
3. **§531-537 accumulated earnings tax:** Penalty 20% tax on
   "unreasonable" accumulation of earnings beyond reasonable
   business needs. This indirectly forces distribution of excess
   earnings.
4. **§541 personal holding company tax:** Penalty 20% tax on PHCs
   that fail to distribute earnings.

The strategic decision: when and how much to distribute as
dividends. C corp tax rates (21% post-TCJA) are lower than top
individual rates, so retaining earnings inside the corporation
defers personal-level tax. But §531/§541 penalties limit excessive
retention, and the qualified dividend rate makes annual
distribution often tax-efficient.

For closely-held C corps, the comp/dividend mix interacts with
reasonable compensation analysis (#21). Excessive comp risks
recharacterization as dividend (corp loses §162 deduction);
inadequate comp risks IRS reclassification as constructive dividend
(reverse problem).

## Primary IRC authority

- **§301** — Distributions of property by corporations.
- **§301(c)** — Treatment as dividend / return of capital / capital
  gain.
- **§316** — Definition of dividend.
- **§312** — Earnings and profits computation.
- **§1(h)(11)** — Qualified dividend rate.
- **§531-537** — Accumulated earnings tax.
- **§541-547** — Personal holding company tax.
- **§243** — Dividends-received deduction (corporate shareholders).

## Treasury regulations

- **Reg §1.301-1** — Distributions.
- **Reg §1.316-1** — Dividend definition.
- **Reg §1.312-1 through §1.312-15** — Earnings and profits.
- **Reg §1.531-1 through §1.537-3** — Accumulated earnings tax.

## Key IRS guidance

- IRS Publication 542 — Corporations.
- IRS Publication 550 — Investment Income.

## Key court decisions

- **Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030
  (1965)** — "Bardahl formula" for reasonable working capital
  needs (§531 defense).
- **Atlas Tool Co. v. Commissioner, 70 T.C. 86 (1978), aff'd, 614
  F.2d 860 (3d Cir. 1980)** — Constructive dividend principles.

## Eligibility requirements

For qualified dividend rate under §1(h)(11):
1. Dividend paid by domestic corporation or qualified foreign
   corporation.
2. Holding period satisfied: stock held more than 60 days during
   the 121-day period beginning 60 days before ex-dividend date.
3. Not a hedged or short position.

For §243 corporate dividends-received deduction:
- 50% / 65% / 100% deduction based on ownership percentage in payer.

## Mechanics — how it works

1. **Determine current and accumulated E&P.** Annual E&P
   computation; track historical accumulated E&P.
2. **Plan distribution amount.** Consider:
   - Excess working capital.
   - §531 reasonable accumulation defense (Bardahl formula).
   - Owner cash needs.
   - Tax bracket optimization (qualified dividend rate vs. retention).
3. **Authorize distribution** by board resolution.
4. **Pay distribution.** Issue check or credit shareholder account.
5. **File Form 1099-DIV.** Box 1a total ordinary dividends; Box 1b
   qualified dividends (assuming holding period met).

## Documentation requirements

- E&P computation schedule.
- Board resolutions authorizing dividends.
- Form 1099-DIV.
- §531 reasonable accumulation analysis (defensive documentation).

## Common pitfalls / audit risks

- **Constructive dividends.** Personal expenses paid by corp,
  excessive compensation, below-market loans to shareholders,
  rent on shareholder property — all may be recharacterized as
  dividends.
- **§531 accumulated earnings tax exposure.** Unreasonable
  accumulation beyond business needs.
- **§541 PHC tax exposure.** Closely-held holding companies with
  passive income.
- **E&P computation errors.** E&P does not equal taxable income;
  several specific adjustments under §312.
- **Holding period failure.** §1(h)(11) qualified dividend rate
  denied without 60-day holding period.

## Recent legislative changes

- **TCJA (2017)** — Reduced C corp rate to 21%; preserved §1(h)(11)
  qualified dividend rate.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §11 corporate
  rate Pub L 119-21]`. Working assumption: 21% rate maintained.

## State conformity considerations

State C corp tax rates vary. State conformity to qualified dividend
treatment varies; some states tax dividends as ordinary income.

## AICPA SSTS / Circular 230 considerations

Standard diligence; constructive dividend issues require careful
client communication.

## Default confidence band rationale

**HIGH** for ordinary dividends under E&P. Drops to MODERATE when
constructive dividend issues are present, or when §531 accumulation
defense is thin.

## Cross-references

- **`reasonable-comp-corp-owners`** (#21) — comp/dividend
  bilateral issue.
- **`income-shifting-to-c-corp`** (#47).
- **`c-corp-misc-deductions`** (#42).
- **`c-corp-state-tax-savings`** (#35).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 301",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section301",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1(h)(11)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 531",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section531",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TaxCt",
      "citation": "Bardahl Manufacturing Corp. v. Commissioner, 24 T.C.M. 1030 (1965)",
      "url": "https://www.ustaxcourt.gov",
      "weight": "judicial"
    }
  ]
}
```
```

---

## Strategy #32: Capital Gain Offsets

**File:** `references/strategies/capital-gain-offsets.md`

```markdown
---
name: "Capital Gain Offsets and Loss Harvesting"
slug: capital-gain-offsets
type: Cap Gains
tax_type: CAG
complexity: Medium
irc_sections: ["§1211", "§1212", "§1091", "§1222"]
forms: ["Form 8949", "Schedule D"]
state_specific: false
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

Capital gain offset planning involves coordinating capital gains and
losses to minimize tax. The mechanics under §§1211-1222:

1. **Net short-term against short-term; net long-term against
   long-term.** Within each character class.
2. **Net short-term loss against long-term gain** (and vice versa)
   if either class produces a net loss.
3. **§1211(b) limit:** Individual capital losses limited to capital
   gains plus $3,000 ordinary income offset per year.
4. **§1212 carryforward:** Excess capital losses carry forward
   indefinitely (individuals); 5-year carryforward and 3-year
   carryback (corporations).
5. **§1091 wash sale rule:** Losses disallowed if substantially
   identical securities purchased within 30 days before or after
   the sale.

The classic year-end strategies:
- **Tax-loss harvesting:** Sell losing positions to offset realized
  gains. Replace with similar (but not "substantially identical")
  positions to maintain market exposure.
- **Specific lot identification:** When selling part of a position
  with multiple lots, identify specific lots to maximize loss /
  minimize gain.
- **Year-end gain timing:** Defer realization of gains to next year
  if expected to be in lower bracket.
- **Carryforward management:** Track carryforwards by character
  (short-term vs. long-term).

For high-income taxpayers, §1411 NIIT (3.8%) applies to net
investment income including net capital gains; coordination with
NIIT is part of the analysis.

## Primary IRC authority

- **§1211** — Limitation on capital losses.
- **§1212** — Capital loss carryovers.
- **§1091** — Loss from wash sales of stock or securities.
- **§1222** — Other terms relating to capital gains and losses.
- **§1223** — Holding period rules.
- **§1411** — NIIT.

## Treasury regulations

- **Reg §1.1211-1** — Limitations.
- **Reg §1.1212-1** — Capital loss carryovers.
- **Reg §1.1091-1** — Wash sales.
- **Reg §1.1411-1 through §1.1411-10** — NIIT regulations.

## Key IRS guidance

- IRS Publication 550 — Investment Income and Expenses.
- IRS Publication 564 — Mutual Fund Distributions.

## Key court decisions

- **Helvering v. Bashford, 302 U.S. 454 (1938)** — Substantially
  identical securities concept.

## Eligibility requirements

For §1211 / §1212 loss treatment:
1. Capital asset disposed of in taxable transaction.
2. Holding period determined under §1223.
3. Loss not disallowed by §1091 wash sale, §267 related-party,
   §183 hobby loss, or other disallowance provision.

For §1091 wash sale avoidance:
1. Replacement security not "substantially identical" to security
   sold.
2. Replacement period: 30 days before sale through 30 days after.
3. Watch for indirect wash sales (spouse purchases; IRA purchases).

## Mechanics — how it works

1. **Year-end tax planning review.** Identify realized gains and
   losses YTD; identify unrealized losses on losing positions.
2. **Loss harvesting candidates.** Securities with significant
   unrealized losses where market exposure can be maintained.
3. **Verify §1091 compliance.** Replacement security must not be
   substantially identical.
4. **Specific identification.** Use specific lot ID for mutual
   funds and equities (vs. average cost basis); this requires
   contemporaneous identification at sale.
5. **Coordinate with NIIT.** §1411 NIIT applies to net investment
   income; loss harvesting reduces NIIT base.
6. **Track carryforwards** by character (short-term, long-term).

## Documentation requirements

- Brokerage statements showing transactions.
- Specific identification documentation (if used).
- Form 8949 / Schedule D.
- Wash sale tracking (broker generally provides on 1099-B Box 1g).

## Common pitfalls / audit risks

- **Wash sale violations.** Repurchase within 30 days defeats
  loss; basis added to replacement security.
- **Indirect wash sales.** Spouse, controlled corporation, IRA
  purchases all trigger §1091.
- **Substantially identical determination.** Different mutual
  funds tracking same index may or may not be "substantially
  identical" — fact-intensive.
- **Specific identification not made at sale.** Default is FIFO
  for stocks; average cost for mutual funds.
- **Holding period miscalculation.** Long-term requires more than
  one year holding.
- **§267 related-party loss disallowance.** Loss on sale to
  related party (spouse, ancestor, descendant, controlled corp)
  is disallowed.

## Recent legislative changes

- **TCJA (2017)** — No direct capital loss changes.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §1211 §1212
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §1211 / §1212 generally complete. **California**
imposes state-specific carryforward rules. **Pennsylvania** does
not allow capital loss carryforward against ordinary income.

## AICPA SSTS / Circular 230 considerations

Standard diligence; routine year-end planning.

## Default confidence band rationale

**HIGH** — clear statutory framework. Drops to MODERATE only for
substantially identical security determinations or related-party
disallowance edge cases.

## Cross-references

- **`installment-sale`** (#33).
- **`niit-minimization`** (#69).
- **`qoz-reinvestment`** (#34) — alternative to loss harvesting
  for large gains.
- **`charitable-donation-appreciated`** (#51) — alternative use of
  appreciated positions.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1211",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1211",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1091",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1091",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1411",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1411",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.1091-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
```

---

## Strategy #33: Installment Sale

**File:** `references/strategies/installment-sale.md`

```markdown
---
name: "Installment Sale (§453)"
slug: installment-sale
type: Cap Gains
tax_type: CAG
complexity: High
irc_sections: ["§453", "§453A", "§453B"]
forms: ["Form 6252", "Schedule D"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

§453 installment sale treatment defers gain recognition over the
period of payment receipt rather than recognizing all gain in the
year of sale. The mechanics:

1. **Gross profit ratio:** Gross profit / contract price.
2. **Each principal payment** triggers gain recognition equal to
   payment × gross profit ratio.
3. **Interest on the deferred portion** is taxed currently as
   ordinary interest income.

The strategy is foundational for sellers receiving multi-year
payments, particularly for:
- Sale of real estate.
- Sale of closely-held business.
- Sale to family members.

Limitations and exceptions:
- **§453(b)(2)(A):** Inventory and dealer property does NOT qualify
  (must recognize all gain in year of sale).
- **§453(b)(2)(B):** Publicly-traded property does NOT qualify
  (deemed payment in full at sale).
- **§453(g):** Sale of depreciable property to controlled entity —
  installment method denied.
- **§453(e):** Related-party rules — second disposition by related
  party within 2 years triggers acceleration.
- **§453A:** For nondealer installment sales >$150,000, interest
  charge on deferred tax (the "tax on the deferred tax").
- **§1231 property:** Recapture (§§1245, 1250) recognized in year
  of sale regardless of installment method (cannot defer recapture).

## Primary IRC authority

- **§453** — Installment method.
- **§453A** — Special rules for nondealer installment sales.
- **§453B** — Gain or loss on disposition of installment obligations.
- **§1245** — Depreciation recapture (personal property).
- **§1250** — Depreciation recapture (real property).

## Treasury regulations

- **Reg §15A.453-1** — Installment method.
- **Reg §1.453-2 through §1.453-12** — Various installment rules.

## Key IRS guidance

- **Rev. Rul. 84-46** — Interest computation under §453A.
- IRS Publication 537 — Installment Sales.

## Key court decisions

- **Commissioner v. South Texas Lumber Co., 333 U.S. 496 (1948)** —
  Substantial economic interest doctrine.
- **Manuel D. Mayerson v. Commissioner, 47 T.C. 340 (1966)** —
  Election timing.

## Eligibility requirements

1. **Disposition is a sale or other disposition** under §1001.
2. **At least one payment** received after the close of the tax
   year of the sale.
3. **Property qualifies** — not inventory; not publicly-traded
   securities; not under §453(g) restrictions.
4. **Election available by default** (must affirmatively elect
   OUT if cash-method recognition preferred).
5. **§453(e) compliance** — second disposition by related party
   within 2 years not made.

## Mechanics — how it works

1. **Determine gross profit and contract price.**
   - Gross profit: Selling price − adjusted basis − selling
     expenses.
   - Contract price: Selling price (less qualifying assumed debt
     under §453(f)(7)).
   - Gross profit ratio: Gross profit / contract price.
2. **Recapture recognition in year of sale.** §§1245 / 1250
   ordinary income recognized regardless of installment method.
3. **Annual gain recognition.** Each principal payment × gross
   profit ratio.
4. **Interest on note.** Reported as ordinary interest income;
   minimum rate under §1274 / §483 if note interest below AFR.
5. **§453A interest charge** if note >$150,000.
6. **Form 6252** — annual installment sale reporting.

## Documentation requirements

- Sale agreement / contract.
- Promissory note.
- Closing statement.
- Form 6252 each year payment is received.
- Recapture computation worksheet.

## Common pitfalls / audit risks

- **Recapture not recognized in year of sale.** §1245/§1250
  recapture cannot be deferred under installment method.
- **§453(g) trap.** Sale of depreciable property to >50%-controlled
  entity blocks installment method.
- **§453(e) acceleration.** Related-party second disposition
  within 2 years.
- **§453A interest charge underestimated.** Computed on deferred
  tax × applicable underpayment rate.
- **Interest below AFR.** Imputed interest under §1274/§483
  recharacterizes part of principal as interest.
- **Wraparound mortgage interaction.** Complex interplay with
  §453(f)(3) and §453(f)(7).
- **Pledge of installment obligation as collateral.** §453A(d)
  treats pledge as receipt of cash.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §453
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State conformity to §453 generally complete. **California, Wisconsin**
have unique installment sale rules.

## AICPA SSTS / Circular 230 considerations

Standard diligence; complex computation requires care.

## Default confidence band rationale

**HIGH** — clear statutory and regulatory framework. Drops to
MODERATE for §453(g) controlled-entity edge cases or §453(e)
related-party scenarios.

## Cross-references

- **`1031-like-kind-exchange`** (#1) — alternative deferral.
- **`qoz-reinvestment`** (#34) — alternative deferral.
- **`deferred-sales-trust`** (#29) — aggressive variant.
- **`capital-gain-offsets`** (#32).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 453",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section453",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 453A",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section453A",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 15A.453-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation"
    }
  ]
}
```
```

---

## Strategy #34: Qualified Opportunity Zone Reinvestment

**File:** `references/strategies/qoz-reinvestment.md`

```markdown
---
name: "Qualified Opportunity Zone (QOZ) Reinvestment"
slug: qoz-reinvestment
type: Cap Gains
tax_type: CAG
complexity: High
irc_sections: ["§1400Z-1", "§1400Z-2"]
forms: ["Form 8949", "Form 8997", "Form 8996 (QOF)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "2025-07-04"
---

## Overview

The Qualified Opportunity Zone (QOZ) program, created by TCJA in
§§1400Z-1 and 1400Z-2, allows taxpayers to defer (and partially
reduce) capital gains by reinvesting them into a Qualified
Opportunity Fund (QOF) within 180 days. Three benefits historically:

1. **Deferral:** Capital gain deferred until earlier of (a) sale of
   the QOF investment or (b) December 31, 2026.
2. **Reduction:** Originally, 10% basis step-up if held 5 years; 15%
   if held 7 years (largely expired due to 2026 recognition date).
3. **Exclusion:** If held 10+ years, basis stepped up to FMV at
   sale, eliminating gain on QOF appreciation.

For 2024-2025 investments, the 5-year and 7-year basis step-ups are
no longer achievable before the December 31, 2026 mandatory
recognition date. The remaining benefits are deferral until 2026
(short-term value) and the 10-year exclusion of QOF appreciation
(the substantial long-term value).

OBBBA may have extended the QOZ program. Verify via Classification
Tables.

## Primary IRC authority

- **§1400Z-1** — Designation of qualified opportunity zones.
- **§1400Z-2** — Special rules for capital gains invested in QOFs.
- **§1400Z-2(a)** — Deferral election.
- **§1400Z-2(b)** — Time for deferred gain recognition.
- **§1400Z-2(c)** — Special rule for investments held for 10 years.
- **§1400Z-2(d)** — QOF definition and 90% asset test.

## Treasury regulations

- **Reg §1.1400Z2(a)-1 through §1.1400Z2(f)-1** — Comprehensive
  QOZ regulations (final 2019 / corrected 2020).

`chevron_replaced: true` flagged on the entire QOZ regulations
package — these regulations heavily interpret ambiguous statutory
provisions and operate well beyond the bare statute.

## Key IRS guidance

- **Rev. Proc. 2018-16** — QOZ designation procedures.
- **Notice 2020-39** — COVID-era 180-day extension relief.
- **Notice 2021-10** — Additional COVID relief.

## Key court decisions

- Limited dispute area; relatively new program.

## Eligibility requirements

For deferral election:
1. Capital gain (short-term or long-term; §1231 net gains; §1245
   recapture not eligible to defer).
2. Reinvested into a Qualified Opportunity Fund (QOF) within 180
   days from the sale date (or for §1231 gains, from end of tax
   year).
3. QOF satisfies 90% asset test under §1400Z-2(d)(1).

For QOF status:
1. Domestic corporation or partnership.
2. Self-certifies as QOF on Form 8996.
3. 90% of assets are Qualified Opportunity Zone Property (QOZP).

For QOZP:
1. Qualified Opportunity Zone Business Property (QOZBP); OR
2. Stock or partnership interest in a Qualified Opportunity Zone
   Business (QOZB).
3. QOZB requirements: 70% of assets are QOZBP; less than 5% of
   assets are nonqualified financial property; substantial
   improvement requirements; etc.

## Mechanics — how it works

1. **Realize capital gain.** Sell appreciated capital asset.
2. **Identify QOF investment** within 180 days.
3. **Make deferral election** on Form 8949 with code "Z" and
   Form 8997.
4. **Annual Form 8997** during deferral period.
5. **December 31, 2026** — Recognize originally-deferred gain
   (regardless of whether QOF investment is sold).
6. **10-year holding** — Election to step basis to FMV at sale of
   QOF, eliminating gain on appreciation since investment.

## Documentation requirements

- Documentation of original capital gain (Form 8949).
- Form 8997 annual report.
- QOF Form 8996 self-certification (annual).
- QOZP / QOZB documentation.
- Holding period records.

## Common pitfalls / audit risks

- **180-day deadline missed.** No relief outside specific
  catastrophe extensions.
- **QOF 90% test failure.** Penalties and potential loss of QOF
  status.
- **QOZB 70% test failure.** Same.
- **Substantial improvement test for QOZBP.** For real estate, must
  improve basis by at least 100% within 30 months of acquisition.
- **Original-use vs. substantial-improvement.** Existing buildings
  not in original use must satisfy substantial improvement.
- **Recapture timing in 2026.** Even taxpayers in 2025 will recognize
  the originally-deferred gain on December 31, 2026 — this is
  unavoidable.

## Recent legislative changes

- **TCJA (2017)** — Created §§1400Z-1, 1400Z-2.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA QOZ Pub L 119-21
  classification table]`. Reports indicate OBBBA extended the QOZ
  program with potentially new designations and revised dates.
  Verify exact provisions.

## State conformity considerations

State conformity to QOZ deferral varies. **California, Mississippi,
North Carolina** do not conform. **New York, Massachusetts** have
mixed conformity.

## AICPA SSTS / Circular 230 considerations

QOZ structures are complex and procedural. Practitioner should
verify QOF certification and confirm QOZP requirements at investment
and at testing dates.

## Default confidence band rationale

**MODERATE** — extensive regulatory complexity with multiple
points of failure. HIGH only for properly-structured investments
with QOF certification confirmed and QOZP documented.

## Cross-references

- **`installment-sale`** (#33) — alternative deferral.
- **`1031-like-kind-exchange`** (#1) — alternative for real estate
  gains.
- **`capital-gain-offsets`** (#32).
- **`section-1202-qsbs`** (#43).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 1400Z-2",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section1400Z-2",
      "weight": "primary_statute"
    },
    {
      "authority_type": "TreasReg",
      "citation": "Treas. Reg. § 1.1400Z2(a)-1",
      "url": "https://www.ecfr.gov/current/title-26/chapter-I/subchapter-A/part-1",
      "weight": "regulation",
      "chevron_replaced": true
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2020-39",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #35: C Corp State Tax Savings

**File:** `references/strategies/c-corp-state-tax-savings.md`

```markdown
---
name: "C Corporation State Tax Savings"
slug: c-corp-state-tax-savings
type: Credit/Payment
tax_type: CREDIT
complexity: Medium
irc_sections: ["§164", "§7701", "§482"]
forms: ["State corporate income tax returns"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: MODERATE
last_obbba_review: "N/A"
---

## Overview

C corporation state tax planning involves multiple strategic levers
to minimize state-level tax burden:

1. **Nexus management.** Avoiding state nexus where possible;
   establishing favorable nexus where economically substantive.
2. **Apportionment optimization.** State apportionment formulas
   (typically based on payroll, property, sales — though many
   states have moved to single-sales-factor) can be optimized
   through structural decisions.
3. **State of incorporation / commercial domicile.** Some states
   (Nevada, Delaware, Wyoming) have no corporate income tax;
   incorporation there alone does not avoid taxation in operating
   states (nexus follows operations) but can affect commercial
   domicile and certain tax characterizations.
4. **Holding company structures.** Delaware, Nevada, and other
   no-tax states sometimes used for IP holding companies that
   license to operating subsidiaries (subject to §482 transfer
   pricing and state addback rules).
5. **State tax credits.** R&D credits, jobs credits, investment
   credits, film credits — vary substantially by state.
6. **Combined / unitary reporting.** Multistate operations may face
   combined reporting requirements that limit shifting; understand
   whether each state requires combined or separate filing.
7. **Public Law 86-272 protection.** Federal law that limits state
   income tax on out-of-state sellers whose only in-state activity
   is solicitation of sales of tangible personal property. Has been
   significantly narrowed by states (e.g., MTC's 2021 statement;
   California, NY, NJ adoptions) for digital and SaaS activities.

## Primary IRC authority

- **§164** — State and local taxes deductible (no $10K cap for C
  corps; the cap applies only to individuals).
- **§482** — Transfer pricing.
- **§7701** — Definitions.

## State authority

State-by-state. Reference state stub files.

## Treasury regulations

- **Reg §1.482-1 through §1.482-9** — Transfer pricing.

## Key federal authority

- **Public Law 86-272 (15 U.S.C. §§ 381-384)** — Solicitation-only
  protection.
- **Quill Corp. v. North Dakota, 504 U.S. 298 (1992)** —
  Substantial nexus pre-Wayfair.
- **South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018)** —
  Eliminated physical presence requirement; established economic
  nexus framework.

## Key state guidance and developments

- **MTC Statement on Public Law 86-272 (revised August 2021)** —
  States MTC's position that internet activities (cookies, mobile
  apps, customer support chat) exceed mere solicitation. Widely
  adopted by states.
- **California FTB TAM 2022-01** — Adopted MTC position.
- **New York Tax Bulletin TB-CT-816** — Adopted MTC position.

## Eligibility requirements

Vary by strategy. Common considerations:
1. State nexus determination (each state's rules).
2. Apportionment factor application.
3. P.L. 86-272 protection (if applicable).
4. Combined / separate filing methodology (state-specific).

## Mechanics — how it works

1. **Multistate footprint analysis.** Determine nexus in each state.
2. **Apportionment review.** Optimize factor mix (single-sales vs.
   three-factor; throwback rules; cost-of-performance vs.
   market-based sourcing for services).
3. **Holding company evaluation.** §482-compliant licensing of IP
   from holding company to operating subsidiaries.
4. **State credit utilization.** Survey credits in operating states.
5. **Wayfair compliance.** Track economic nexus thresholds in each
   state where economic activity occurs.
6. **P.L. 86-272 review.** Especially for online businesses
   post-MTC 2021 statement.
7. **Annual review.** State law changes affect prior-year planning.

## Documentation requirements

- Multistate apportionment workpapers.
- §482 transfer pricing documentation (if intercompany).
- State tax credit applications.
- P.L. 86-272 activity tracking.

## Common pitfalls / audit risks

- **Holding company addback rules.** Many states (NJ, IL, MA, PA,
  WI) require addback of intercompany interest, royalties, etc.
- **Combined/unitary reporting.** Cannot shift income across
  related entities in combined-reporting states.
- **P.L. 86-272 erosion.** State adoption of MTC 2021 position
  may eliminate prior planning.
- **Single-sales-factor states.** Significantly different from
  three-factor states; sourcing rules become critical.
- **Economic nexus.** Wayfair-driven tracking required in 50 states.

## Recent legislative changes

- **Wayfair (2018)** — Economic nexus framework.
- **MTC 2021 statement** — P.L. 86-272 erosion.
- **Many state-level changes** — single-sales-factor adoptions,
  PTET enactments, throwback repeals.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA state tax
  Pub L 119-21]`. Federal-level OBBBA impact on state taxation
  generally limited.

## State conformity considerations

This entire strategy is fundamentally state-by-state.

## AICPA SSTS / Circular 230 considerations

Multistate planning requires careful documentation and regular
review for state law changes.

## Default confidence band rationale

**MODERATE** — fact and state-specific. HIGH for established
positions in conforming states; LOW for aggressive positions
challenging post-Wayfair / post-MTC 2021 frameworks.

## Cross-references

- **`ptet-salt-workaround`** (#17) — pass-through variant.
- **`state-tax-savings`** (#40) — individual variant.
- **`income-shifting-to-c-corp`** (#47).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 482",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section482",
      "weight": "primary_statute"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "South Dakota v. Wayfair, Inc., 138 S. Ct. 2080 (2018)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    }
  ]
}
```
```

---

## Strategy #36: EV Credits (Post-IRA, Post-OBBBA)

**File:** `references/strategies/ev-credits.md`

```markdown
---
name: "Electric Vehicle Tax Credits (§30D, §25E, §45W)"
slug: ev-credits
type: Credit/Payment
tax_type: CREDIT
complexity: High
irc_sections: ["§30D", "§25E", "§45W"]
forms: ["Form 8936", "Schedule A of Form 8936", "Form 8910"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "2025-07-04"
---

## Overview

The Inflation Reduction Act (IRA) of 2022 substantially overhauled
the EV credit framework. The current structure (subject to OBBBA
modifications):

1. **§30D Clean Vehicle Credit:** Up to $7,500 for new clean
   vehicles. Conditions:
   - **$3,750** for vehicles meeting critical minerals requirement
     (post-2024: 50%; rising annually).
   - **$3,750** for vehicles meeting battery components requirement
     (post-2024: 60%; rising annually).
   - Income limits: Modified AGI ≤$300K MFJ / $225K HoH / $150K
     single (lookback to either current or prior year, whichever
     better).
   - MSRP limits: $80K SUVs/trucks/vans; $55K cars.
   - Final assembly in North America.
   - Foreign Entity of Concern (FEOC) restrictions.
2. **§25E Used Clean Vehicle Credit:** Up to $4,000 (or 30% of
   purchase price, lesser of). Conditions:
   - Vehicle priced ≤$25,000.
   - Used by qualified taxpayer for first time.
   - Income limits: $150K MFJ / $112,500 HoH / $75K single.
3. **§45W Commercial Clean Vehicle Credit:** Up to $7,500 (light
   vehicles) or $40,000 (heavy vehicles >14,000 lbs GVWR). For
   business-use vehicles. No income or MSRP limits.

The credits became transferable to dealers at point of sale starting
2024 (§30D(g)(2)) — buyers can take credit as immediate purchase
discount rather than wait until tax filing.

OBBBA may have substantially modified or terminated EV credits.
Verify via Classification Tables.

## Primary IRC authority

- **§30D** — New Clean Vehicle Credit.
- **§30D(d)** — Critical minerals requirement.
- **§30D(e)** — Battery components requirement.
- **§30D(f)** — Income and MSRP limits.
- **§30D(g)** — Transfer to dealer election.
- **§25E** — Used Clean Vehicle Credit.
- **§45W** — Commercial Clean Vehicle Credit.

## Treasury regulations

- **Reg §1.30D-1 through §1.30D-6** — Final regulations issued
  2024.
- **Reg §1.25E-1** — Used clean vehicle.
- **Reg §1.45W-1** — Commercial clean vehicle.

## Key IRS guidance

- **Notice 2023-1** — Initial guidance on §30D after IRA.
- **Rev. Proc. 2023-33** — Dealer transfer mechanics.
- **Rev. Proc. 2024-26** — FEOC clarification.
- **IRS Fuel Economy and Environment Labels** — MSRP and
  classification.
- **DOE/EPA fueleconomy.gov** — Eligible vehicle list.

## Key court decisions

- Limited dispute area; relatively new framework.

## Eligibility requirements

For §30D (new vehicle):
1. New, qualifying clean vehicle.
2. Final assembly in North America.
3. Critical minerals + battery components requirements.
4. Income below threshold.
5. MSRP below threshold.
6. Transfer to dealer election (optional).

For §25E (used vehicle):
1. Vehicle ≥2 model years older than year of purchase.
2. Vehicle priced ≤$25,000.
3. First sale to qualified buyer.
4. Income below threshold.

For §45W (commercial):
1. Vehicle used in business.
2. Acquired for use, not resale.
3. Made by qualifying manufacturer.
4. No income/MSRP limits.

## Mechanics — how it works

1. **Pre-purchase verification.** Confirm vehicle qualifies
   (fueleconomy.gov; manufacturer documentation).
2. **Income lookback.** Use lower of current or prior year MAGI for
   §30D and §25E.
3. **Transfer election (if applicable).** Buyer transfers credit
   to dealer at point of sale; receives discount.
4. **Form 8936** with return.
5. **Recapture.** Vehicle ceasing to qualify or income exceeding
   threshold (post-purchase) may trigger recapture.

## Documentation requirements

- Manufacturer certification.
- VIN registration.
- Purchase agreement showing MSRP and final assembly.
- Form 8936 / 8936-A.
- Income documentation supporting threshold.

## Common pitfalls / audit risks

- **Critical minerals / battery components changes.** Annual
  thresholds increase; vehicle eligible in 2024 may not qualify in
  2025.
- **FEOC restrictions.** Vehicles with battery components from
  foreign entities of concern (post-2024 critical minerals; 2025
  battery) disqualify.
- **Income threshold.** Spouse income aggregation; current-year
  vs. prior-year lookback flexibility.
- **MSRP determination.** "Manufacturer's suggested retail price"
  is the key; not invoice price.
- **Transfer to dealer election** is irrevocable.
- **Recapture if ceased to qualify.**

## Recent legislative changes

- **IRA (2022)** — Created the modern §30D / §25E / §45W framework.
- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA EV credits
  §30D §25E §45W Pub L 119-21 classification table]`. Reports
  indicate significant OBBBA modifications, possibly including
  early termination, modified income limits, or expanded categories.
  This is one of the most consequential OBBBA verifications
  practitioners need to perform.

## State conformity considerations

State EV credits (CA Clean Vehicle Rebate Project, CO state
credits, etc.) may be additional or independent of federal.

## AICPA SSTS / Circular 230 considerations

EV credit changes are dynamic; practitioner should verify current-
year rules at time of advice. Income lookback and transfer-to-
dealer election require careful planning.

## Default confidence band rationale

**HIGH** for vehicles clearly meeting requirements. Drops to
MODERATE for borderline income, MSRP, or critical minerals/battery
component qualifications.

## Cross-references

- **`misc-tax-credits`** (#38).
- **`business-vehicle-usage`** (#4) — interaction with §45W.
- **`bonus-and-section-179-depreciation`** (#12) — interaction
  with depreciation.

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 30D",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section30D",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 25E",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section25E",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 45W",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section45W",
      "weight": "primary_statute"
    },
    {
      "authority_type": "Notice",
      "citation": "Notice 2023-1",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    },
    {
      "authority_type": "RevProc",
      "citation": "Rev. Proc. 2023-33",
      "url": "https://www.irs.gov/irb",
      "weight": "irs_published"
    }
  ]
}
```
```

---

## Strategy #37: Late Penalties / Interest

**File:** `references/strategies/late-penalties-interest.md`

```markdown
---
name: "Late Filing / Late Payment Penalty and Interest Management"
slug: late-penalties-interest
type: Credit/Payment
tax_type: CREDIT
complexity: Medium
irc_sections: ["§6651", "§6601", "§6404", "§6664(c)"]
forms: ["Form 843 (penalty abatement claim)"]
state_specific: true
dirty_dozen: false
listed_transaction: false
reportable_transaction: false
confidence_default_band: HIGH
last_obbba_review: "N/A"
---

## Overview

This strategy addresses penalty and interest management — primarily
penalty abatement and interest reduction — when taxpayers find
themselves with late-filed or late-paid returns. The mechanisms:

1. **First-time abatement (FTA)** under IRM 20.1.1.3.6.1: One-time
   abatement of certain failure-to-file, failure-to-pay, and
   failure-to-deposit penalties for taxpayers with clean compliance
   history (3 prior tax years with no penalties; current
   filing/payment compliance).
2. **Reasonable cause** under §6651(a)(1) and §6664(c): Penalties
   abated for "reasonable cause and not willful neglect."
3. **Interest abatement under §6404(e):** Interest on tax may be
   abated if attributable to "ministerial or managerial" delay by
   the IRS. Limited to delays in IRS performance, not initial
   determinations.
4. **§6601 interest accrual:** Interest on underpayments at
   federal short-term rate plus 3% (small business C corps and
   underpayments above $100K large corporate underpayment use
   different rates).

The §6651 penalties:
- **§6651(a)(1) failure to file:** 5% per month, max 25%, of unpaid
  tax.
- **§6651(a)(2) failure to pay:** 0.5% per month, max 25%, of unpaid
  tax. Reduces failure-to-file by failure-to-pay during overlapping
  months.
- **§6651(a)(3) failure to pay assessment:** 0.5% per month, max
  25%, after notice of assessment.

The §6662 accuracy-related penalties (20% generally, 40% for
gross valuation overstatements) are addressed in `predict-reasonable-
cause` (predict skill) and `penalty-abatement` (#66).

## Primary IRC authority

- **§6651** — Failure to file return or pay tax.
- **§6601** — Interest on underpayment.
- **§6404** — Abatements (interest).
- **§6404(e)** — Interest abatement for IRS error or delay.
- **§6664(c)** — Reasonable cause defense to accuracy penalty.

## Treasury regulations

- **Reg §301.6651-1** — Failure to file or pay.
- **Reg §301.6404-2** — Interest abatement.

## Key IRS guidance

- **IRM 20.1** — Penalty Handbook.
- **IRM 20.1.1.3.6.1** — First-Time Abate (FTA).
- **Rev. Proc. 84-35** — Small partnership failure to file
  reasonable cause.
- **IRS Penalty Relief Information**:
  https://www.irs.gov/payments/penalty-relief

## Key court decisions

- **United States v. Boyle, 469 U.S. 241 (1985)** — Reliance on
  attorney/CPA to file is NOT reasonable cause for late filing
  (taxpayer's nondelegable duty).
- **In re Carlson, 126 F.3d 915 (7th Cir. 1997)** — Reasonable
  cause analysis.

## Eligibility requirements

For first-time abate (FTA):
1. Penalty is failure to file, failure to pay, or failure to
   deposit.
2. No penalty assessed in prior 3 tax years (penalty-free history).
3. Currently filed (or filed extension) and paid (or arranged
   payment).

For reasonable cause:
1. Taxpayer exercised "ordinary business care and prudence" but
   was nevertheless unable to file or pay on time.
2. Documented circumstances: serious illness, death, natural
   disaster, records destruction, IRS/postal delays, reliance on
   CPA for substantive tax position (NOT for filing).
3. Boyle limit: reliance on agent for filing alone is not
   reasonable cause.

For §6404(e) interest abatement:
1. Interest attributable to delay in IRS performing ministerial or
   managerial act.
2. No significant aspect of error attributable to taxpayer.

## Mechanics — how it works

For FTA:
1. **Verify clean compliance history** (last 3 years).
2. **Request FTA orally** during phone contact with IRS, OR
3. **Submit Form 843** for FTA abatement.
4. IRS typically grants if requirements met.

For reasonable cause:
1. **Document circumstances** (medical records, records of
   destruction, etc.).
2. **Submit Form 843** with detailed reasonable cause statement.
3. IRS evaluates against Boyle and IRM 20.1 standards.

For §6404(e):
1. **Identify specific IRS delay**.
2. **Submit Form 843** with delay documentation.

## Documentation requirements

- Form 843 with detailed explanation.
- Supporting documentation (medical, disaster, etc.).
- Compliance history showing FTA eligibility.

## Common pitfalls / audit risks

- **Boyle preclusion.** Reliance on CPA/attorney to file is not
  reasonable cause.
- **Failure to demonstrate "ordinary business care and prudence."**
  Generic statements rejected.
- **Interest cannot be abated for taxpayer error.** §6404(e)
  applies only to IRS-side delay.
- **§6651(a)(2) reduction** of FTF by FTP — taxpayers and
  practitioners often miscalculate.
- **Failure to request FTA first.** FTA is automatic; reasonable
  cause is not. Use FTA when available.

## Recent legislative changes

- **OBBBA (2025)** — `[CITATION NEEDED — search: OBBBA §6651
  Pub L 119-21]`. Working assumption: no changes.

## State conformity considerations

State penalty regimes are independent. Each state has its own
abatement procedures.

## AICPA SSTS / Circular 230 considerations

Standard diligence; practitioner should pursue FTA before
reasonable cause when both available.

## Default confidence band rationale

**HIGH** for FTA when eligibility is clear. **MODERATE** for
reasonable cause depending on documentation strength.

## Cross-references

- **`penalty-abatement`** (#66) — broader penalty abatement
  framework.
- **`predict-reasonable-cause`** (predict skill).

## Authorities (JSON sidecar fragment)

```json
{
  "authorities": [
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 6651",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6651",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRC",
      "citation": "I.R.C. § 6404(e)",
      "url": "https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title26-section6404",
      "weight": "primary_statute"
    },
    {
      "authority_type": "IRM",
      "citation": "IRM 20.1.1.3.6.1, First Time Abate (FTA)",
      "url": "https://www.irs.gov/irm/part20",
      "weight": "persuasive_non_authority"
    },
    {
      "authority_type": "SCOTUS",
      "citation": "United States v. Boyle, 469 U.S. 241 (1985)",
      "url": "https://www.supremecourt.gov",
      "weight": "binding_judicial"
    }
  ]
}
```
```

---

**End of Part 4 of 10.** Strategies #28 through #37 delivered.

**Continue to Part 5 of 10** for strategies #38 through #47 (Misc Tax Credits, R&D Credit, State Tax Savings, Cost Segregation, C Corp Misc Deductions, §1202 QSBS, Corporate-Owned VUL, §127 Education Assistance, Gifting Stock, Income Shifting to C Corp).
