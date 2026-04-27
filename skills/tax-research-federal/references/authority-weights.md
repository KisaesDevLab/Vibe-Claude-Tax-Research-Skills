# Authority weights — federal-specific notes

This reference supplements `shared/authority-hierarchy.md` with
federal-tax-specific weighting nuances the skill must apply.

## Quick reference

| Authority | Default weight | Notes |
|---|---|---|
| IRC | `primary_statute` | Quote the operative subsection / paragraph; pin to flush-language where applicable. |
| Treasury Regulations (final) | `regulation` | Set `chevron_replaced: true` on any rule interpreting ambiguous statute post-Loper Bright. |
| Treasury Regulations (temporary) | `regulation` | Limited 3-year sunset under §7805(e). |
| Treasury Regulations (proposed) | `persuasive_non_authority` | Does NOT reach `regulation` weight until finalized — but represents IRS position. |
| Treasury Decisions | `regulation` | Issuance vehicle; cite the codified text in eCFR. |
| U.S. Supreme Court | `binding_judicial` | Trumps everything below. |
| U.S. Court of Appeals (taxpayer's circuit) | `binding_circuit` | Tax Court applies Golsen; Court of Federal Claims applies its own circuit (Federal Circuit). |
| U.S. Court of Appeals (other circuits) | `judicial` | Persuasive; flag splits explicitly. |
| U.S. Tax Court (regular) | `judicial` | Subject to Golsen. |
| U.S. Tax Court (memorandum) | `judicial` | Slightly lower persuasive weight than regular opinions. |
| U.S. District Court | `judicial` | |
| U.S. Court of Federal Claims | `judicial` | Refund jurisdiction. |
| Revenue Ruling | `irs_published` | IRB-published; IRS may reverse. |
| Revenue Procedure | `irs_published` | Procedural rules; check for superseded. |
| Notice | `irs_published` | Often interim guidance; check IRB. |
| Announcement | `irs_published` | Lower than Rev. Rul.; non-precedential within IRS practice. |
| PLR / TAM / CCA / GCM / AOD / FSA / OfficeMemo / InfoLetter | `written_determinations` | § 6110(k)(3) — no precedential value to other taxpayers; citable for the IRS's own analysis. |
| IRS Publication | `persuasive_non_authority` | Reflects IRS view; not authority under § 1.6662-4(d)(3). |
| IRM | `persuasive_non_authority` | Internal practice manual. |
| Audit Technique Guide | `persuasive_non_authority` | Examiner field reference. |
| ISP Coordinated Issue Paper | `persuasive_non_authority` | Coordinated-issue program. |
| IRS News Release | `persuasive_non_authority` | Headline; verify against published guidance. |
| JCT Bluebook | `legislative_history` | Detailed explanation typically published 6–12 months after enactment. |
| Committee report (HW&M / Sen. Fin. / Conf.) | `legislative_history` | Especially probative when statute is ambiguous. |
| Treasury Greenbook | `legislative_history` (only if enacted as proposed) / else `persuasive_non_authority` | Tag carefully — Greenbooks describe what was proposed. |
| CBO scoring report | `legislative_history` (only if score accompanied enacted bill) / else `persuasive_non_authority` | Not interpretive authority. |
| Treaty + Treasury technical explanation | `primary_statute` | Treaties have statute-equivalent weight; Treasury explanations are quasi-legislative-history. |

## Loper Bright operating rules

After Loper Bright Enterprises v. Raimondo, 144 S. Ct. 2244 (2024),
Chevron is no longer good law. For any cited Treasury Regulation:

1. Assess whether the regulation interprets ambiguous statutory text.
2. If yes, set `chevron_replaced: true` in the citation entry.
3. Apply Skidmore review: thoroughness of the agency's reasoning,
   validity of its analysis, consistency over time, persuasiveness.
4. Do not assert "the Reg controls" without engaging the Skidmore
   factors.
5. Cap confidence at MODERATE on a Reg-only basis where the statute
   is ambiguous.

## Golsen rule

The Tax Court applies the law of the U.S. Court of Appeals to which
the taxpayer's case is appealable (Golsen v. Commissioner, 54 T.C. 742
(1970), aff'd, 445 F.2d 985 (10th Cir. 1971)). Identify the taxpayer's
circuit before weighting Court-of-Appeals authority.

## § 6662 substantial-authority weighting rules

Per Treas. Reg. § 1.6662-4(d)(3)(ii):

- An authority that cogently relates law to the facts is given more
  weight than one that merely states a conclusion.
- Newer trumps older for written determinations; > 10 years old
  receives "very little weight."
- An authority that has been overruled, modified, or revoked is no
  longer authority.
- Sub-regulatory IRS pronouncements (IRM, ATG, Pub) are NOT authority
  for substantial-authority purposes.

## Circuit-split detection heuristic

When two Court-of-Appeals decisions reach inconsistent results on the
same legal issue:
1. Note the split explicitly in the analysis section.
2. State which circuit the taxpayer is in (Golsen).
3. State which side the IRS has taken in published guidance.
4. Cap confidence band at MODERATE unless the taxpayer's circuit's
   authority is clearly on point.
