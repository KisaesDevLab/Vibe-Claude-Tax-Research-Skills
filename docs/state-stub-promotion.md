# State stub promotion guide

State per-state files at
`skills/tax-research-state-{income,salesuse}/references/states/<XX>.md`
ship with `status: stub`. This document describes how to promote
a stub through the four-status ladder.

## Status ladder

| Status | Meaning | Confidence cap |
|---|---|---|
| `stub` | Auto-generated; only primary agency URL populated | LOW |
| `draft` | First practitioner edit; some content added | MODERATE |
| `reviewed` | Second-pair review by another practitioner | HIGH (with caveats) |
| `verified` | Live citation walk against current statute / regulation / DOR guidance | HIGH (full) |

The confidence-band-decay rule (per
`shared/confidence-bands.md`) caps state-tax conclusions at LOW
when the per-state file is `stub`. Promoting the state file is the
primary mechanism by which state research moves to higher
confidence.

## Promotion: stub → draft

### Trigger

A practitioner needs to use the per-state file for substantive
analysis or contributes content as part of an engagement.

### Steps

1. Open the per-state file at
   `skills/tax-research-state-income/references/states/<XX>.md`
   (or `salesuse/references/states/<XX>.md`).
2. Edit the YAML frontmatter:
   - `status: draft`
   - `last_reviewed: <YYYY-MM-DD>` (today's date).
   - `last_reviewed_by: <github-handle>`.
3. Replace `<!-- TODO -->` markers with substantive content:
   - Confirm the primary agency URL.
   - Fill in income-tax-administration / sales-tax-administration
     / employment-tax-administration / property-tax-administration
     / appeals-tribunal entries.
   - Cite specific statutes (e.g., "Cal. Rev. & Tax. Code
     § 17041") and regulations.
   - Provide year-specific rate / threshold information.
   - Identify state-specific quirks (PTET, convenience-of-employer,
     ABC test, etc.).
4. For items that still require research, leave a sentinel:
   `[CITATION NEEDED — search: <specific query>]`.
5. Add to "Recent developments" section any post-24-month
   legislative or regulatory changes affecting the state.
6. Update the practitioner-notes block with engagement-relevant
   observations.

### Validation

Run:

```bash
./scripts/validate.sh full
```

The state-stub check confirms 51 files exist per skill with
matching `state_code` frontmatter. The fabricated-citation
sentinel check is excluded for `references/states/` paths (so
sentinels are tolerated in stub files), but `[CITATION NEEDED]`
should be replaced with real citations as soon as possible.

### Commit

```bash
git commit -m "docs(state-<XX>): promote to draft + populate <topic>"
```

## Promotion: draft → reviewed

### Trigger

A second practitioner reviews the draft for accuracy, completeness,
and consistency with the canonical Vibe CPA pack style.

### Reviewer checklist

- [ ] Citations verified against canonical sources (state
  statutes, regulations, DOR guidance).
- [ ] All `<!-- TODO -->` markers replaced with substantive
  content or `[CITATION NEEDED — search: ...]` sentinels.
- [ ] Year-specific rate / threshold information matches current
  Rev. Proc. / Notice / DOR pronouncement.
- [ ] State-specific quirks adequately documented.
- [ ] Practitioner-notes section captures non-obvious nuances.
- [ ] No fabricated citations.
- [ ] No client-confidential data, PII, or jurisdictional
  out-of-scope content.
- [ ] Frontmatter `status: reviewed`; `last_reviewed:` updated.

### Steps

1. Reviewer reads the draft and identifies issues.
2. Reviewer either:
   - Approves: edit frontmatter to `status: reviewed`; update
     `last_reviewed:` and `last_reviewed_by:`.
   - Requests revisions: leave PR comments.
3. Once approved, merge to main per repository workflow.

## Promotion: reviewed → verified

### Trigger

A practitioner conducts a live citation walk against current state
statute, regulation, and DOR guidance — typically as part of an
engagement requiring HIGH-band confidence on a state-tax position.

### Verification walk

1. For each cited state statute:
   - Pull current text from the state legislative website.
   - Confirm citation form matches the file's documented pattern.
   - Note any amendments since last review.
2. For each cited state regulation:
   - Pull current text from the state regulatory hub.
   - Confirm the regulation is in force.
   - Note any pending or recent amendments.
3. For each cited DOR pronouncement (Rev. Rul. equivalent,
   advisory opinion, technical bulletin):
   - Confirm the pronouncement has not been modified, superseded,
     or revoked.
   - Note any subsequent guidance.
4. For state appellate / administrative tribunal decisions:
   - Run citator check (KeyCite, Shepard's, BCite, or comparable).
   - Confirm no implicit overrules.
5. Update the file:
   - Replace any `[CITATION NEEDED]` sentinels with real citations.
   - Update `retrieved_date` annotations (if any).
   - Update `last_reviewed:` and `last_reviewed_by:`.
   - Set `status: verified`.

### Documentation

Verified files merit highest confidence in state-tax research.
However, even verified files have a freshness window — typically
12 months — beyond which the practitioner should re-walk.

## Annual maintenance

Verified files should be re-walked annually:
- For tax-rate / threshold updates.
- For regulatory amendments.
- For new state legislation affecting the file's content.
- For appellate or administrative tribunal decisions on cited
  authorities.

The `last_reviewed:` field tracks the most-recent walk. When older
than 365 days, the file's confidence cap drops back to MODERATE
per the freshness-decay rule in `shared/confidence-bands.md`.

## Reverting

If a verified file is found to contain incorrect content:
1. Open a PR demoting the file to `draft` or `reviewed` (whichever
   is appropriate).
2. Document the reason in the PR description.
3. Update `last_reviewed:` and `last_reviewed_by:` to reflect the
   demotion review.

## Cross-skill consistency

When a state file is promoted in one skill (e.g.,
`tax-research-state-income/CA.md`), check the parallel state file
in the other skill (`tax-research-state-salesuse/CA.md`) for
consistency. The administrative-bodies block, statute citation
pattern, and recent-developments section should align.

## Strategy-library cross-references

State-specific strategies (PTET, §1031 with CA Form 3840
reporting, §1202 with CA / PA non-conformity, etc.) reference
per-state files. Promoting a per-state file does NOT automatically
promote strategies that reference it — but those strategies become
more reliable when their per-state files reach `reviewed` or
`verified`.

## Workflow summary

```
[bootstrap]    stub
[engagement]   stub → draft (single practitioner edit)
[review]       draft → reviewed (second-pair review)
[citation walk] reviewed → verified (live citation walk)
[stale]        verified → reviewed (auto-decay at 365 days from last_reviewed)
[error found]  any → draft (revert with PR documentation)
```
