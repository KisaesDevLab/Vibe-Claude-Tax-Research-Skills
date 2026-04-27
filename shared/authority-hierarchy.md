# Authority hierarchy

Recognized "authority" follows Treas. Reg. § 1.6662-4(d)(3)(iii). Use
this table to assign `weight` to every citation in the JSON sidecar.

For the IRS's own published view of the guidance hierarchy, see
"Understanding IRS Guidance — A Brief Primer" at
https://www.irs.gov/newsroom/understanding-irs-guidance-a-brief-primer
(cite as `IRSNewsRelease`/`persuasive_non_authority` — note that the
IRS's own characterization of authority weight is itself not authority,
but is useful as a malpractice-defense scaffolding artifact).

## Weights

| Tier | Weight key | Authorities |
|---|---|---|
| 1 | `primary_statute` | Internal Revenue Code; tax treaties + Treasury explanations; state statutes |
| 2 | `binding_judicial` | U.S. Supreme Court decisions |
| 3 | `regulation` | Treasury Regulations: final > temporary > proposed (post-Loper Bright reviewed under Skidmore); state agency regulations |
| 4 | `binding_circuit` | U.S. Court of Appeals (controlling in taxpayer's circuit; Tax Court applies the *Golsen* rule) |
| 5 | `judicial` | U.S. Tax Court regular & memorandum, District Courts, Court of Federal Claims, state appellate courts |
| 6 | `irs_published` | Revenue Rulings, Revenue Procedures, Notices, Announcements (IRB-published) |
| 7 | `legislative_history` | JCT Blue Book; committee/conference reports; floor statements by bill managers; Treasury Greenbooks; CBO reports |
| 8 | `written_determinations` | PLRs, TAMs, CCAs, GCMs, AODs, FSAs, Office Memorandums, Information Letters (citable; **no precedential value** to other taxpayers per § 6110(k)(3)) |
| 9 | `persuasive_non_authority` | IRS Publications, IRM, Forms/Instructions, Audit Technique Guides, ISP Coordinated Issue Papers, IRS News Releases — NOT authority under § 1.6662-4(d)(3)(iii) but persuasive of IRS practice; state DOR publications; policy-data sources (Tax Foundation, Tax Policy Center) |
| 10 | `not_authority` | Treatises, articles, blogs, AI/LLM outputs, tax-professional opinions — **never authority** |

## Weighting rules (§ 1.6662-4(d)(3)(ii))
- Authority that cogently relates law to facts > authority that
  states a conclusion.
- Newer trumps older for written determinations; > 10 years old
  generally accorded "very little weight."
- Implicit/explicit overrule strips authority status.

## Loper Bright disclosure
For any proposition resting on a Treasury Regulation's interpretation
of an ambiguous statute, set `chevron_replaced: true` in the sidecar
authority entry and note Skidmore review framework: thoroughness,
reasoning validity, consistency, persuasiveness.

## IRM and ATG disclosure
IRM, ATG, and ISP Paper citations get `weight: persuasive_non_authority`
and must be accompanied by a higher-tier authority for the underlying
legal proposition, OR the conclusion must be limited to "describes IRS
practice" rather than "the law requires."

## Golsen rule reminder
Tax Court follows the law of the U.S. Court of Appeals to which the
taxpayer's case is appealable. Identify the taxpayer's circuit before
weighting Court of Appeals authority.

## State authority
For state tax questions, weight in the analogous order:
state statute > state agency regulations > state appellate court
decisions > state administrative tribunal decisions > letter rulings
or advisory opinions (often non-precedential) > state DOR
publications. Per-state nuances live in the per-state reference
files at `skills/tax-research-state-{income,salesuse}/references/states/`.

Tax Foundation Center for State Tax Policy and Tax Policy Center are
secondary policy data sources useful for context (state conformity
tables, rate tables, recent legislative tracking) but are
`persuasive_non_authority` at most. They MUST NOT serve as the
closest authority for a state tax conclusion.

## Treasury Greenbooks and CBO reports
Treasury "Greenbooks" (Administration's Fiscal Year Revenue Proposals)
and CBO scoring reports describe **proposed** legislation and
projected revenue effects. They are `legislative_history` weight ONLY
when the proposal becomes enacted law and the Greenbook/CBO report
becomes part of the authoritative legislative-history record.
Otherwise they describe what was proposed, not what is law — tag as
`persuasive_non_authority` for purely descriptive use.
