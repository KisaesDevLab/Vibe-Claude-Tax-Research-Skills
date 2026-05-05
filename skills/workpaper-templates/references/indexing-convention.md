# Indexing convention

The indexing convention is the firm's filing system for engagement
workpapers. It groups workpapers by F/S caption and engagement
phase, and provides a consistent reference scheme that survives
staff turnover, software migration, and regulatory inspection.

The convention here is a starting point. Most firms inherit a
convention from their workpaper software (CCH ProSystem fx
Engagement, Caseware, Thomson Reuters Practice CS, AuditLogic,
or others), and the firm-level methodology document specifies any
deviations.

## Two top-level files

Every engagement file has two top-level segments:

### Permanent file (`PF`)
Documents that span multiple periods. Built once and updated as
relevant events occur.

| Index | Contents |
|---|---|
| PF-1 | Articles of incorporation / formation; certificate of good standing |
| PF-2 | Bylaws / operating agreement / partnership agreement |
| PF-3 | Stockholder / member / partner agreements; buy-sell |
| PF-4 | Recent board / shareholder / member meeting minutes |
| PF-5 | Material long-term contracts (customer master agreements, real-estate leases > 1 yr, equipment leases, IP licenses, employment agreements) |
| PF-6 | Long-term debt agreements (loans, lines of credit, bonds, mortgages) |
| PF-7 | Insurance schedule (D&O, E&O, GL, property, workers' comp, cyber) |
| PF-8 | Retirement plan and deferred-compensation plan documents |
| PF-9 | Tax returns: federal / state / local — current and 3 prior years |
| PF-10 | Engagement letter (current period) — though some firms file in current file too |
| PF-11 | Independence documentation (firm-level) |
| PF-12 | Permanent client correspondence (organizational changes, structural events) |

### Current file (`CF` — or just letter-numeric without prefix)
Documents specific to the period under engagement.

## Current-file alphanumeric scheme

Workpapers in the current file follow an alphanumeric scheme that
groups by F/S caption. The scheme below is a common default; firms
adapt to match their methodology and software.

### Planning section
| Index | Contents |
|---|---|
| 100 | Engagement summary / cover |
| 110 | Engagement letter (current period) |
| 120 | Independence assessment + AICPA Code §1.200 threats memo |
| 130 | Risk-assessment memo (audits — AU-C §315) |
| 140 | Materiality determination memo |
| 150 | Audit / engagement plan |
| 160 | Fraud-inquiry memo (audits — AU-C §240) |
| 170 | Going-concern indicators memo (when relevant) |
| 180 | Engagement budget / time tracking |
| 190 | Workpaper indexing convention + tickmark legend |

### Asset captions (A–G)
| Index | Caption |
|---|---|
| A | Cash and cash equivalents |
| B | Accounts and notes receivable |
| C | Inventory |
| D | Property, plant, and equipment (D-2 for ROU lease assets) |
| E | Investments and intangibles |
| F | Prepaid expenses and other current assets |
| G | Other assets and deferred charges |

### Equity captions (H)
| Index | Caption |
|---|---|
| H | Equity (capital contributions, distributions, retained earnings) |

### Liability captions (K–M)
| Index | Caption |
|---|---|
| K | Accounts payable and accrued liabilities |
| L | Lease liability (ASC 842) and other accruals |
| M | Long-term debt |

### Tax captions (T)
| Index | Caption |
|---|---|
| T | Income taxes (current + deferred — ASC 740) |
| T-2 | Sales / use tax accruals |
| T-3 | Other tax accruals |

### Income statement captions (R, S, OE, T-IS)
| Index | Caption |
|---|---|
| R | Revenue |
| S | Cost of revenue / cost of goods sold |
| OE | Operating expenses |
| OI | Other income and loss |
| T-IS | Income tax expense |

### Reporting / wrap-up section (900-series)
| Index | Contents |
|---|---|
| 900 | Subsequent-events review |
| 910 | Management representation letter |
| 920 | Governance communication letter (audits — AU-C §260) |
| 930 | Draft financial statements |
| 940 | Draft audit / review / compilation report |
| 950 | Engagement Quality Reviewer (EQR) review notes (SQMS 2 when required) |
| 960 | Open-items / points-forward memo |
| 970 | Engagement file lock-down memo (AU-C §230.16 — within 60 days) |

## Sub-indexing

Sub-indices use periods or hyphens. Firm preference governs.

| Sub-index | Meaning |
|---|---|
| `A-1` | First sub-workpaper under caption A (e.g., bank rec for primary operating account) |
| `A-1.1` | First substantive procedure WP under sub-lead A-1 |
| `A-2` | Second sub-workpaper under caption A |
| `A-CONFIRM` | Confirmation responses for caption A (audits) |

Indexing depth is engagement-driven. A small engagement may go
only one level deep (`A`, `A-1`, `A-2`); a complex audit goes
several levels deep (`A-1.1.1`).

## Index assignment rule

- Lead sheet at the caption level uses the caption letter (e.g.,
  `A` for Cash lead sheet).
- Sub-leads use letter-number (e.g., `A-1`, `A-2`).
- Substantive procedure WPs use letter-number-period-number (e.g.,
  `A-1.1`).
- Cross-references between WPs are explicit, not implied.

## Software conventions

| Software | Default indexing |
|---|---|
| CCH ProSystem fx Engagement | Tree structure with caption groupings; supports custom letter prefixes. |
| Caseware Working Papers | Document folders with leadsheets; each leadsheet has a fixed account-mapping reference. |
| Thomson Reuters Practice CS | Engagement-level folder structure with fixed templates per engagement type. |
| Karbon / spreadsheet-based | Worksheet tabs with manual indexing; lead sheet on row 1 of each tab. |

## File-completeness checklist

Before the engagement file is locked down per AU-C §230.16 (within
60 days after report-release date):

- [ ] Every PBC item is `received` or `withdrawn` (no `open`).
- [ ] Every workpaper has preparer / reviewer / partner sign-off.
- [ ] Every tickmark used appears on the legend.
- [ ] Every lead-sheet caption ties to TB and to the issued F/S.
- [ ] Open review notes (preparer / reviewer / EQR) are cleared.
- [ ] Subsequent-events review covers through report-release date.
- [ ] Management representation letter is dated as of the report
      release date and signed by management.
- [ ] Governance communication letter (AU-C §260) is delivered (audits).
- [ ] Engagement-quality-review (SQMS 2) sign-off is in the file
      where required.
- [ ] Final F/S draft and report draft archived in the 900-series.
