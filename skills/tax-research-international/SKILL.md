---
name: tax-research-international
description: |
  Federal international-tax research skill covering inbound (foreign
  taxpayer with U.S. activities), outbound (U.S. taxpayer with
  foreign activities), CFC / GILTI / Subpart F, FDII, BEAT, FTC
  computations, treaties (LOB, residency, permanent establishment),
  expat / FEIE issues, and informational-reporting (Forms 5471,
  5472, 8865, 8938, FBAR / FinCEN 114). Use when the user asks
  "international tax", "GILTI", "Subpart F", "CFC", "PFIC", "FEIE",
  "Form 2555", "FTC", "Form 1116 / 1118", "treaty residency",
  "permanent establishment", "Form 5471", "FBAR", "Form 8938", or
  "expatriate tax". Make sure to use this skill whenever the user
  mentions GILTI, Subpart F, CFC, PFIC, treaty, FBAR, FATCA,
  Form 5471 / 5472 / 8865 / 8938, or international taxation.
license: BUSL-1.1
version: 0.1.0
allowed-tools: Read Grep Glob Bash(jq:*) WebFetch
---

# tax-research-international — Inbound / outbound / treaty research

## Read before output

1. `shared/citation-discipline.md`
2. `shared/authority-hierarchy.md`
3. `shared/confidence-bands.md`
4. `shared/compliance.md`
5. `shared/legislation-tracking.md` — TCJA created §951A GILTI,
   §245A territorial DRD, §59A BEAT, §250 FDII; OBBBA
   modifications to be verified.
6. `references/treaties-a-to-z.md` — IRS Treaties A–Z mapping and
   common LOB / residency / PE issues.
7. `references/oecd-model-treaty.md` — OECD Model Tax Convention
   and BEPS context (NOT U.S. authority, but useful for negotiating-
   text background).
8. `references/cfc-and-pfic.md` — Subpart F / GILTI / PFIC
   computational mechanics.

## Operative authority

- IRC §1 / §11 — basic tax on individuals / corporations.
- IRC §61 / §63 — gross income / taxable income.
- IRC §§861–865 — sourcing rules.
- IRC §§871–898 — taxation of nonresident aliens and foreign
  corporations.
- IRC §§901–908 — foreign tax credit.
- IRC §§911–912 — FEIE and Foreign Housing Exclusion / Deduction.
- IRC §§951–965 — Subpart F.
- IRC §951A — GILTI.
- IRC §965 — transition tax (one-time, 2017-related).
- IRC §245A — territorial DRD.
- IRC §250 — FDII / GILTI deduction.
- IRC §§367 / 367(a) / 367(b) / 367(d) — outbound and inbound
  recognition rules.
- IRC §§1291–1298 — PFIC rules.
- IRC §59A — BEAT.
- IRC §6038 / §6038A / §6038B / §6048 — informational reporting.
- 31 U.S.C. §5314 / 31 C.F.R. §1010.350 — FBAR.
- IRC §6038D and Form 8938 — specified foreign financial assets.
- U.S. tax treaties (verify text and effective dates at IRS
  Treaties A–Z page).

## Workflow

### 1. Intake

- `taxpayer_residency`: U.S. resident, NRA, dual-resident
- `taxpayer_circuit`
- `tax_year`
- `inbound_or_outbound`: classify the question
- `treaty_country`: if relevant
- `entity_structure`: CFC, foreign-disregarded, foreign
  partnership, hybrid
- `compliance_obligations_at_issue`: 5471, 5472, 8865, 8858, 8938,
  FBAR

### 2. Sourcing

§§861–865 govern income sourcing. Common categorization:
- Interest: residence of payor (§861(a)(1)).
- Dividends: residence of payor (§861(a)(2)).
- Personal services: where performed (§861(a)(3)).
- Rents and royalties: where property used (§861(a)(4)).
- Sales of inventory: title-passage rule (§861(a)(6); modified by
  TCJA §863(b)).
- Sales of personal property other than inventory: §865.

### 3. Inbound taxation

Nonresident alien individuals and foreign corporations:
- Effectively connected income (ECI): taxed at graduated rates
  (§§871(b), 882).
- Fixed, determinable, annual, or periodical (FDAP) income:
  taxed at 30% gross via withholding (§§1441, 1442) absent
  treaty reduction.
- Withholding on real-property dispositions: FIRPTA (§1445).

### 4. Outbound taxation

U.S. shareholders of CFCs:
- §951(a) — Subpart F inclusion.
- §951A — GILTI inclusion.
- §250 — 50% deduction on GILTI (37.5% on FDII).
- §960 — indirect FTC.

§245A — 100% DRD on §245A-eligible foreign-source dividends.

§59A BEAT — modified §59A imposes minimum tax on certain
deductible payments to related foreign parties.

### 5. Foreign tax credit (§901)

Direct FTC: §901 — credit for foreign taxes paid by U.S.
taxpayer.

§904 limitation by income basket:
- Passive category (§904(d)(2)(B)).
- General category.
- Foreign branch (post-TCJA).
- GILTI (separate basket per §904(d)(1)(A)).

§904(j) — election out for individuals with passive ≤ $300 ($600
MFJ) and only passive-category foreign tax.

### 6. Treaties

U.S. tax treaties modify the IRC for residents of the treaty
country. Key provisions:
- Residency tiebreaker (Article 4).
- Permanent establishment (Article 5).
- Business profits (Article 7).
- Dividends, interest, royalties (Articles 10, 11, 12 — reduced
  withholding rates).
- Limitation on benefits (LOB — Article 22 in modern U.S. model).
- Mutual agreement procedure (MAP — Article 25).

§7852(d)(1) — later-in-time rule between treaty and statute.

§894 — special rules for treaty benefits to hybrid entities.

Treaty texts: IRS Treaties A–Z page (see `references/treaties-a-
to-z.md`).

### 7. FEIE (§911)

§911(a) — qualified individual may exclude foreign earned income
up to annual limit (verify year-specific Rev. Proc.; e.g., $126,500
for 2024).

§911(d) — qualified individual:
- Bona-fide residence test; OR
- Physical-presence test (330 days in any 12 consecutive months).

§911(c) — Foreign Housing Exclusion / Deduction.

### 8. Informational reporting

- Form 5471 — U.S. shareholder of foreign corporation.
- Form 5472 — foreign-owned U.S. corporation / disregarded entity.
- Form 8865 — U.S. partner of foreign partnership.
- Form 8858 — foreign disregarded entity.
- Form 8938 — specified foreign financial assets (§6038D).
- FinCEN 114 / FBAR — > $10,000 aggregate foreign financial
  accounts.
- Form 3520 / 3520-A — foreign trusts and gifts from foreign
  persons.

§6038 / §6038A penalty: $10,000 per failure (with continuation
penalty up to $50,000); criminal penalties under §7203 for willful
failure to file.

§6038D Form 8938 penalty: $10,000 per failure (continuation up to
$50,000). 40% accuracy-related penalty on undisclosed foreign
financial-asset underpayment (§6662(j)).

§5314 / §5321 FBAR penalty: $10,000 non-willful per violation;
willful penalty up to greater of $100,000 or 50% of account
balance per violation. Bittner v. United States, 598 U.S. 85
(2023): non-willful penalty assessed PER REPORT, not PER ACCOUNT.

### 9. Conclusion + sidecar

Confidence band per `shared/confidence-bands.md`. Cite IRC, Treas.
Regs., relevant treaty text (NOT OECD Model — that's persuasive
non-authority), case law. JSON sidecar validates against
`shared/output-schema.json`. For high-stakes positions, populate
`negative_treatment_review_required: true`.

## Hard rules

- Never fabricate treaty article numbers; verify via IRS Treaties
  A–Z.
- Never claim Chevron deference for international Treas. Regs;
  many were promulgated under broad delegation authority and are
  Loper-Bright-vulnerable.
- Never cite the OECD Model Treaty as authority for a U.S. tax
  position; it is `persuasive_non_authority` for negotiating-text
  background only.
- Drop one band when relying on a Competent Authority MAP
  agreement (no precedential effect).
- Drop one band when relying on the §911 FEIE for a partial-year
  presence absent the bona-fide-residence prong.
- Always route to FBAR / Form 8938 obligations; under-disclosure
  is a major source of practitioner liability.
- Always include the verification checklist appendix.

## Verification checklist (appendix)

End the markdown response with the SSTS / Circular 230 checklist
from `shared/compliance.md`. International-tax positions almost
always warrant the negative-treatment-review residual practitioner
responsibility.

After the verification checklist, emit the follow-up-routing block
per `shared/follow-up-routing.md` (Phase 10a). The block offers the
user two orthogonal handoffs — package the result (`memo` or
`open-point`) and carry the conclusion forward (`plan` | `workpaper`
| `resolution` | `return`) — and the dispatcher routes the user's
reply to the destination skill.
