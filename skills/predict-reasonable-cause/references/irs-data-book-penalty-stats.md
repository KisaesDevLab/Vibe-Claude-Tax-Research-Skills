# IRS Data Book — penalty-abatement statistics

## Source

The IRS Data Book is published annually at:
https://www.irs.gov/statistics/soi-tax-stats-irs-data-book

Tag any citation as:
- `authority_type: IRSPub` (Publication)
- `weight: persuasive_non_authority`

The Data Book reports penalty-assessment and penalty-abatement
counts by category. It is useful for:
- Demonstrating that abatement is administratively common (i.e.,
  the IRS abates a substantial fraction of assessed penalties).
- Setting practitioner expectations on the realistic upside of an
  abatement request.

It is NOT useful as legal authority. The Data Book reports
aggregate IRS administrative practice; it does NOT establish a
legal entitlement, nor does it bind any examiner.

## Typical statistical framing (illustrative — verify with the
current Data Book before quoting)

The Data Book historically reports:
- Civil penalties assessed against individuals, businesses,
  estate-and-gift, employment, and excise filers.
- Civil penalties abated, by category.
- Aggregate dollar amounts.

In recent years, abatement counts have varied widely by penalty
type:
- §6651 family penalties (FTF / FTP): a meaningful share of
  assessed penalties is abated, often via FTA or reasonable
  cause.
- §6662 accuracy penalties: abatement is much rarer; the
  reasonable-cause / substantial-authority defenses are heavily
  fact-dependent.
- Estimated-tax penalties (§6654 / §6655): abatement is rare;
  these are mostly mathematical and the §6654(e) waivers are
  narrow.
- Information-return / W-2 penalties (§6721 / §6722): high
  abatement rates when reasonable-cause is demonstrated.

## How to cite

When using the Data Book as administrative-trend context:

```json
{
  "authority_type": "IRSPub",
  "citation": "IRS Data Book [Year], Table [N] — Civil Penalties Assessed and Abated, by Type of Tax",
  "url": "https://www.irs.gov/statistics/soi-tax-stats-irs-data-book",
  "retrieved_date": "[YYYY-MM-DD]",
  "quoted_text": "[verbatim figure or phrase, ≤75 words]",
  "weight": "persuasive_non_authority"
}
```

The Data Book MUST NOT serve as the closest authority for the
abatement decision. The closest authority is always:
- §6651 / §6662 / §6664 (statute);
- Treas. Reg. §301.6651-1(c)(1) / §1.6664-4 (regulation);
- IRM 20.1.1 (administrative-procedure persuasive non-authority);
- Boyle, McMahan, and circuit-specific case law (judicial).

## Practitioner takeaway

Cite the Data Book only:
- To set client expectations on realistic abatement probabilities.
- In a malpractice-defense file to show that the practitioner's
  recommendation aligned with administrative trend data.

Do NOT cite the Data Book:
- As the legal basis for an abatement request.
- To support a confidence band assignment.
- In Tax Court briefs or formal protest letters as authority.
