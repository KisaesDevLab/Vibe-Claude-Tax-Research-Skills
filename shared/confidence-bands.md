# Confidence bands

Confidence bands map IRC § 6662 substantial-authority standards to
labels every prediction/research/planning output must include.

| Band | Approx. probability | Statutory label | Penalty implication |
|---|---|---|---|
| **HIGH** | ≥ 70% (informal "should") to ≥ 90% ("will") | More likely than not (> 50%) when at the floor; "should/will" above | Avoids accuracy-related penalty without disclosure; meets FIN 48/ASC 740 recognition |
| **MODERATE** | ~ 40–50% | Substantial authority (§ 6662(d)(2)(B)(i)) | Avoids substantial-understatement penalty without disclosure |
| **LOW** | ~ 20–35% | Reasonable basis (Reg. § 1.6662-3(b)(3)) | Avoids negligence penalty **only with adequate disclosure** (Form 8275 / 8275-R) |
| **SPECULATIVE** | < 20% | Below reasonable basis | Penalty risk; do not recommend |

## Required band assignment

Every prediction or research conclusion MUST carry a band. The
sidecar field `confidence_band` is one of `HIGH`, `MODERATE`, `LOW`,
`SPECULATIVE`. Provide:
- `band_rationale`: one paragraph mapping authority weight + factual
  fit to the band.
- `disclosure_recommended`: boolean; true when band is LOW (adequate
  disclosure path) or whenever a position is contrary to a
  Regulation (Form 8275-R).
- `penalty_exposure`: free-text summary keyed to § 6662(b) categories.

## Decay rules
- Drop one band when authority is `persuasive_non_authority` only.
- Drop one band when retrieved_date > 365 days for a fast-moving
  area (state SALT/PTET, R&D § 174 capitalization, OZ rules).
- Drop one band when relying on a PLR/TAM/CCA/GCM/AOD/FSA/Office
  Memorandum/Information Letter as the closest authority.
- Cannot exceed MODERATE on a Treasury-Reg-only basis where the
  underlying statute is ambiguous (Loper Bright posture).
- Cannot reach HIGH on a § 6662(b)(6) noneconomic-substance question
  without a binding judicial authority on point.
- For state tax conclusions citing only a stub-status state file
  (state file `status: stub`), cannot exceed LOW until the file is
  promoted to `reviewed` or `verified`.
- Tax Foundation, Tax Policy Center, blogs, and other current-
  awareness sources do not affect the band at all (they are
  not_authority or persuasive_non_authority and never the closest
  cite).

## Practitioner thresholds (informal)
The thresholds (20% / 33% / 40% / > 50% / 70% / 90%) are
practitioner conventions, not regulatory text. Cite AICPA SSTS levels
of confidence chart when referenced.
