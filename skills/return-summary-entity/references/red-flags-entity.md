# Entity-return red-flag catalog

Routing convention: when a flag fires, surface the issue in the
summary and recommend a routing target (in backticks).

## C-corp (Form 1120)

| Pattern | Route |
|---|---|
| Officer comp very high vs receipts | `predict-reasonable-comp` |
| Shareholder loans without documentation | `predict-debt-vs-equity` |
| §382 ownership-change indicators | `tax-research-entity` (subchapter-c) |
| §163(j) interest deduction shortfall | `tax-research-entity` |
| §59A BEAT exposure (large multinational) | `tax-research-international` |
| §245A DRD claims | `tax-research-international` |
| GILTI inclusion (Schedule C) | `tax-research-international` |
| §951A high-tax election decision | `tax-research-international` |
| Personal-Holding-Company (Schedule PH) | `tax-research-entity` |
| §55 corporate AMT (post-IRA, ≥ $1B AFSI) | `tax-research-entity` |
| Constructive-dividend patterns | `tax-research-entity` (subchapter-c) |
| §332 / §368 reorganization mid-year | `tax-research-entity` |

## S-corp (Form 1120-S)

| Pattern | Route |
|---|---|
| Owner W-2 < 30% of distributions | `predict-reasonable-comp` |
| Distributions exceed AAA + basis | `tax-research-entity` (subchapter-s) |
| Built-in gains tax (§1374) | `tax-research-entity` |
| Excess net passive-investment income | `tax-research-entity` |
| Disproportionate distributions (one-class issue) | `tax-research-entity` |
| Late S-election or invalidly-formed S-corp | `tax-research-entity` (Rev. Proc. 2013-30) |
| §199A QBI eligibility | `predict-qbi-eligibility` |
| Stock or loan basis insufficient for losses (§1366(d)) | `tax-research-entity` |
| Foreign owner / NRA shareholder | `tax-research-entity` (subchapter-s) |
| Shareholder fringe benefits (§1372 / Notice 2008-1) | `tax-research-payroll` |

## Partnership (Form 1065)

| Pattern | Route |
|---|---|
| §704(b) substantial-economic-effect concerns | `tax-research-entity` (subchapter-k) |
| §704(c) built-in gain/loss tracking missing | `tax-research-entity` |
| §752 liability mis-allocation | `tax-research-entity` |
| §754 election decision (sale/death of partner) | `tax-research-entity` |
| §163(j) at partnership level + EBIE | `tax-research-entity` |
| BBA opt-out election eligibility | `tax-research-procedure` |
| Self-employment for LLC member | `tax-research-entity` (subchapter-k); flag Soroban T.C. Memo. 2023-129 |
| §199A QBI items | `predict-qbi-eligibility` |
| §465 at-risk limitations | `tax-research-entity` |
| Partnership Representative designation issues | `tax-research-procedure` |
| Foreign partner / withholding (§1446) | `tax-research-international` |
| §704(c)(1)(B) / §737 mixing-bowl 7-year tracking | `tax-research-entity` |

## Cross-entity (any form)

| Pattern | Route |
|---|---|
| Schedule M-1 / M-3 large book-tax differences | flag in summary; no routing |
| Schedule L beginning balance ≠ prior-year ending | flag; recommend reconciliation |
| Foreign disregarded entity / Form 8858 | `tax-research-international` |
| Form 5472 trigger | `tax-research-international` |
| Form 5471 trigger (US persons owning ≥10% foreign corp) | `tax-research-international` |
| State PTET election | `tax-research-state-income` |
| State pass-through credit at owner level | `tax-research-state-income` |
| Reasonable-cause for late entity-level penalty | `predict-reasonable-cause` |
| §6699 partnership / S-corp late-filing penalty | `predict-reasonable-cause` |
| Worker-classification on Schedule of compensation | `predict-worker-classification` |
| Hobby-loss pattern on activity flowing through K-1 | `predict-hobby-loss` |
| §469 passive-activity issues on rental K-1 | `predict-real-estate-pro` or `predict-material-participation` |
| §1031 like-kind exchange in current year | `predict-1031-qualification` |
| §41 R&D credit claimed | `predict-r-and-d-credit` |
| §7701(o) economic-substance concerns | `predict-economic-substance` |
| Late S-election relief | `tax-research-entity` (Rev. Proc. 2013-30) |

## Documentation gaps to flag

- Schedule L not provided when required (assets / receipts ≥
  $250K).
- Schedule M-1 / M-3 not provided when required.
- Capital-account analysis (Schedule K-1 Part II) shows tax-basis
  method NOT used.
- §754 election claimed but no statement attached.
- §469 grouping election (§1.469-9(g)) referenced but no statement
  attached.
- §704(b) special allocations claimed but no economic-effect
  documentation.
- Form 5471 / 5472 / 8865 / 8858 trigger conditions met but no
  attached form.
- BBA Partnership Representative absent or improperly designated.
