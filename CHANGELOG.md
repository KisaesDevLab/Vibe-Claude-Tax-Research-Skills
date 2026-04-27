# Changelog

All notable changes documented here. Format follows Keep a Changelog;
versions follow SemVer.

## [Unreleased]

- Phase 0: bootstrap repo skeleton, shared/ files (citation-discipline,
  authority-hierarchy, confidence-bands, compliance, legislation-tracking,
  live-sources, sources.json, output-schema.json, state-template),
  docs/skill-template.md, scripts (validate.sh, run-evals.sh),
  CI workflow, plugin skeleton, .claude/commands.
- Phase 1: three flagship skills (tax-research-federal,
  predict-worker-classification, return-summary-1040),
  cpa-pack-index dispatcher, eval harness with ≥3 cases per flagship.
- Phase 2: 10 prediction skills + 3 research skills + return-summary-entity
  + notice-response.
- Phase 3: 3 planning skills + 3 research skills + 5 utilities +
  compliance skill + 102 state stubs (51 each in two state research
  skills).
- Phase 4: planning-strategy-library with 30 strategy entries.
- Phase 5: examples, install docs, README, marketplace metadata.
- Phase 6: full eval suite + QA pass.
