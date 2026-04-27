# Retrieval checklist

Order of operations for any federal-research task. Each step
references the canonical URL in `shared/sources.json`.

## Step 1 — Statute (IRC)

1. Pull the operative IRC section from
   https://uscode.house.gov/browse/prelim@title26&edition=prelim
   (USLM canonical). Pin to the subsection / paragraph / clause /
   subparagraph as applicable.
2. If the section has been recently amended, note the most recent
   Public Law and link to the Classification Table per
   `shared/legislation-tracking.md`.
3. If the user's tax year predates a recent amendment, retrieve the
   pre-amendment text (USLM has version history).
4. Cite as `IRC` / `primary_statute`.

## Step 2 — Treasury Regulations

1. Pull the relevant Treas. Reg. from
   https://www.ecfr.gov/current/title-26.
2. Distinguish final / temporary (§7805(e)) / proposed.
3. Check the Federal Register IRS feed for any pending
   amendment / TD or proposed reg superseding the cite:
   https://www.federalregister.gov/agencies/internal-revenue-service.
4. If the reg interprets ambiguous statutory text, set
   `chevron_replaced: true` per Loper Bright.
5. Cite as `TreasReg` / `regulation`.

## Step 3 — Binding judicial

Order: Supreme Court → Court of Appeals (taxpayer's circuit) → Tax
Court / DCt / CtFedClaims.

1. Search CourtListener (https://www.courtlistener.com) for
   case name and citation.
2. Search DAWSON (https://dawson.ustaxcourt.gov) for Tax Court
   opinions.
3. Pull the operative paragraph; quote ≤ 75 words verbatim.
4. Apply Golsen: the taxpayer's circuit's CtAppeals decision is
   binding on Tax Court for that taxpayer.
5. Note any circuit split and indicate which side the IRS has
   adopted in published guidance.
6. Cite as `SCOTUS` / `binding_judicial`, `CtAppeals` /
   `binding_circuit` (in-circuit) or `judicial` (out-of-circuit),
   `TaxCt` / `judicial`.

## Step 4 — IRS published guidance

1. Pull the IRB index at
   https://www.irs.gov/internal-revenue-bulletin or alternate
   picklist at
   https://apps.irs.gov/app/picklist/list/internalRevenueBulletins.html.
2. Verify Rev. Rul. / Rev. Proc. / Notice / Announcement is not
   superseded, modified, obsoleted, or revoked.
3. Cite as `RevRul` / `RevProc` / `Notice` / `Announcement` /
   `irs_published`.

## Step 5 — Legislative history (if applicable)

When the question implicates a recent Public Law or ambiguous
statutory text:

1. JCT Bluebook for the relevant Congress at
   https://www.jct.gov/publications/.
2. House W&M, Senate Finance, Conference reports.
3. Treasury Greenbook (only `legislative_history` weight if proposal
   enacted in same form).
4. CBO scoring report (only `legislative_history` weight if score
   accompanied enacted bill).

See `shared/legislation-tracking.md` for the full Public-Law-to-USC
workflow.

## Step 6 — Written determinations

1. https://www.irs.gov/written-determinations for PLR / TAM / CCA.
2. § 6110(k)(3) — no precedential value to other taxpayers; citable
   for IRS analysis.
3. Drop one confidence band if a written determination is the
   closest authority.
4. Cite as `PLR` / `TAM` / `CCA` / `GCM` / `AOD` / `FSA` /
   `OfficeMemo` / `InfoLetter` / `written_determinations`.

## Step 7 — Persuasive non-authority

Only after the above are exhausted, and only as supplement:

- IRS Publications, IRM, Forms / Instructions, ATG, ISP CIPs,
  IRS News Releases.
- All `persuasive_non_authority`.
- Cap conclusions to "describes IRS practice" unless paired with a
  higher-tier cite.

## Step 8 — Sentinel + sidecar

If any step above leaves a proposition ungrounded:

1. Inline: emit the sentinel pattern documented in
   `shared/citation-discipline.md`.
2. JSON sidecar `unresolved_citations[]`: `{ proposition, search,
   date }`.
3. Drop one confidence band.

## Step 9 — Negative-treatment review

For any high-stakes position (dollar amount > $50K, novel argument,
or position that relies on a Tax Court or Court of Appeals case as
the closest authority):

1. Set `negative_treatment_review_required: true` in the sidecar.
2. Note in the verification checklist that the practitioner must run
   an independent citator check (KeyCite, Shepards, BCite, Citator
   2nd) before relying on the cited case.
3. The pack uses free primary sources and cannot detect implicit
   overrules with comprehensive coverage.

## Step 10 — Output

Markdown response (memo style: Issue, Facts, Analysis, Conclusion,
Authorities, Verification checklist) followed by JSON sidecar.
