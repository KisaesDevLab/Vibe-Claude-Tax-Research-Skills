# OECD Model Tax Convention — context and limits

## Source

OECD Model Tax Convention on Income and on Capital:
https://www.oecd.org/tax/treaties/

The OECD Model is published in two volumes:
- Articles and Commentary.
- Periodic updates (most recently 2017 with subsequent partial
  updates).

## Authority status (CRITICAL)

The OECD Model is NOT U.S. tax authority. Cite as:
- `authority_type: not enumerated — record in narrative only`
- `weight: persuasive_non_authority` at most.

The OECD Model and Commentary are useful for:
- Understanding the negotiating-text background of U.S. tax
  treaties (the U.S. Model is heavily influenced by the OECD
  Model).
- Understanding how other treaty partners interpret similar
  provisions.
- BEPS-driven concepts (LOB, principal-purpose test, MLI
  modifications).

The OECD Model and Commentary MUST NOT serve as the closest
authority for any U.S. tax conclusion. The relevant treaty text,
its Treasury Technical Explanation, and U.S. case law are the
controlling authorities.

## OECD vs. U.S. Model

The U.S. Model Tax Convention (most recent: 2016) departs from
OECD in several respects:
- More-detailed LOB provisions (the U.S. Model has had LOB since
  1996; OECD adopted similar concepts only in 2017 via the MLI).
- Saving clause preserving U.S. taxation of U.S. citizens
  regardless of residency.
- Specific provisions on FATCA-related information exchange.
- Broader exchange-of-information article.

A U.S. treaty negotiated in the past decade typically follows the
U.S. Model with country-specific modifications.

## BEPS / MLI context

OECD BEPS (Base Erosion and Profit Shifting) project resulted in
the Multilateral Instrument (MLI), signed June 2017 by ~ 100
jurisdictions.

The U.S. has NOT ratified the MLI but has implemented many BEPS
concepts unilaterally:
- §59A BEAT addresses base erosion.
- §951A GILTI addresses CFC profit shifting.
- §250 FDII incentivizes U.S.-located IP.
- Country-by-country reporting under §6038A / §6038C and
  Reg. §1.6038-4 (Form 8975).

When a U.S. taxpayer cites a BEPS concept (PPT, MLI Article 7),
the practitioner should distinguish between:
- BEPS as policy / negotiating context (persuasive non-authority);
- The actual U.S. statutory or regulatory implementation
  (primary authority).

## Pillar 1 / Pillar 2 (post-2021 OECD/G20 framework)

Pillar 1: reallocation of taxing rights for the largest MNEs.
Pillar 2: 15% global minimum tax (GloBE rules — Income Inclusion
Rule, Undertaxed Profits Rule, Subject to Tax Rule).

U.S. participation:
- Pillar 1: not implemented; depends on multilateral consensus.
- Pillar 2: U.S. has NOT enacted GloBE; §951A GILTI partially
  approximates IIR effects but is not a Pillar 2 implementation.
  CAMT (§55 corporate AMT, IRA 2022) is U.S.-only.

For multinational clients, Pillar 2 implementation in foreign
jurisdictions affects the U.S. tax position via:
- §901 FTC creditability of QDMTT (Qualified Domestic Minimum
  Top-Up Tax) — still under IRS analysis.
- Effect on §250 FDII / §951A GILTI computations as foreign tax
  rates change.

## Practitioner takeaway

Use the OECD Model and Commentary to:
- Understand background and negotiating intent of U.S. treaty
  provisions.
- Compare U.S. Model deviations.
- Frame BEPS / MLI / Pillar 2 issues for clients.

Do NOT use the OECD Model or Commentary as:
- The closest authority for any U.S. tax conclusion.
- Support for a confidence band assignment.
- A basis for a return position absent independent U.S.
  authority.

When citing in a research file, tag explicitly as
`persuasive_non_authority` or `not_authority` and pair with the
binding U.S. treaty text and IRC provision.

## OECD-related research workflow

1. Identify the U.S. treaty article at issue.
2. Read the relevant OECD Model article AND the U.S. Model
   article for comparison.
3. Read the Treasury Technical Explanation of the specific U.S.
   treaty.
4. Read the OECD Commentary on the relevant article ONLY for
   negotiating-text background.
5. Apply the controlling U.S. treaty text and U.S. interpretive
   authority (Treasury, Treasury Technical Explanation, U.S.
   case law).

## Citation format example

If used solely for negotiating-text context:

```json
{
  "authority_type": "not enumerated — record only in narrative",
  "citation": "OECD Model Tax Convention on Income and on Capital, Article 5, Paragraph 4, Commentary 2017",
  "url": "https://www.oecd.org/tax/treaties/",
  "retrieved_date": "[YYYY-MM-DD]",
  "quoted_text": "[verbatim, ≤75 words]",
  "weight": "persuasive_non_authority"
}
```

The OECD Model is OUTSIDE the `authority_type` enum in
shared/output-schema.json. Practitioners should record OECD Model
references in narrative or in a separate `secondary_references[]`
section rather than the `authorities[]` array.
