# Contributing

Issues and PRs welcome. By submitting, you agree your contribution is
licensed under the project's BSL 1.1 license. All SKILL.md changes must
pass `./scripts/validate.sh` and include at least one eval case.

## Quick links

- [BUILD_PLAN.md](BUILD_PLAN.md) — phase-by-phase build plan and the
  source of truth for what ships in v1.0.0-beta.
- [docs/skill-template.md](docs/skill-template.md) — template for every
  new skill.
- [shared/citation-discipline.md](shared/citation-discipline.md) — the
  rules every output must follow.
- [docs/state-stub-promotion.md](docs/state-stub-promotion.md) — how to
  promote per-state reference stubs to draft → reviewed → verified.

## Required for SKILL.md PRs

1. YAML frontmatter validates: `name` ≤ 64 chars (kebab-case), no
   reserved words `anthropic`/`claude`; `description` ≤ 1024 chars.
2. Body ≤ 500 lines. Push longer reference content to
   `references/<topic>.md` one level deep.
3. Workflow with Intake → Analysis → Conclusion → Authorities → JSON
   sidecar that validates against `shared/output-schema.json`.
4. Hard rules section explicitly forbidding fabricated citations.
5. SSTS + Circular 230 verification checklist appendix.
6. At least one eval case in `evals/<family>/<skill>.json`.
7. `./scripts/validate.sh skill <skill-name>` exits 0.

## Required for state-stub PRs

1. Frontmatter `state_code` matches the filename (`<XX>.md`).
2. The `applies_to` list covers the relevant skills (income / sales-use).
3. If promoting status above `stub`, every `TODO:` marker must be
   resolved or replaced with a `[CITATION NEEDED — search: ...]`
   sentinel for items still requiring research.
4. Update `last_reviewed` and `last_reviewed_by`.
