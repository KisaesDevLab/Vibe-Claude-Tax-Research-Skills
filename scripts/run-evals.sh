#!/usr/bin/env bash
# scripts/run-evals.sh — Vibe CPA Skills eval harness
#
# Usage:
#   ./scripts/run-evals.sh full
#   ./scripts/run-evals.sh phase <N>
#   ./scripts/run-evals.sh skill <skill-name>
#   ./scripts/run-evals.sh full --summary
#
# This is a structural validator for eval files (NOT a live LLM runner).
# A live runner is out of scope for the build harness; the project ships
# eval JSON that a downstream tool can execute with subagent pairs.
#
# What this script enforces:
# - Every eval JSON parses.
# - Every eval JSON has the shape: { "skill_name", "evals": [ ... ] }.
# - Every eval case has: id, prompt, expected_output, expectations[].
# - Each skill referenced in evals/<family>/<skill>.json maps to a
#   skills/<skill>/SKILL.md that exists.
#
# Exits 0 if all eval JSON files validate; non-zero otherwise.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

PASS=0
FAIL=0

ok()   { echo "OK   $*"; PASS=$((PASS+1)); }
fail() { echo "FAIL $*"; FAIL=$((FAIL+1)); }

JQ_PRESENT=0
PY=""
if command -v jq >/dev/null 2>&1; then
  JQ_PRESENT=1
elif command -v python3 >/dev/null 2>&1 && python3 -c '' >/dev/null 2>&1; then
  PY="python3"
elif command -v python >/dev/null 2>&1 && python -c '' >/dev/null 2>&1; then
  PY="python"
fi

validate_eval_file() {
  local f="$1"
  if [ "$JQ_PRESENT" -eq 0 ]; then
    if [ -n "$PY" ]; then
      "$PY" - "$f" <<'PY'
import json, sys
p = sys.argv[1]
d = json.load(open(p))
assert isinstance(d, dict), f"{p}: not an object"
assert "skill_name" in d, f"{p}: missing skill_name"
assert "evals" in d and isinstance(d["evals"], list), f"{p}: missing evals[]"
for c in d["evals"]:
    for k in ("id","prompt","expected_output","expectations"):
        assert k in c, f"{p}:{c.get('id','?')}: missing {k}"
    assert isinstance(c["expectations"], list) and c["expectations"], \
        f"{p}:{c['id']}: expectations[] must be non-empty list"
print("OK", p)
PY
      [ $? -eq 0 ] && ok "$f" || fail "$f"
      return
    fi
    fail "no jq or python available; cannot validate $f"
    return
  fi
  if ! jq -e 'type == "object"
              and has("skill_name")
              and (.evals | type == "array")
              and (.evals | length > 0)
              and (.evals | all(has("id") and has("prompt")
                                and has("expected_output")
                                and (.expectations | type == "array")
                                and (.expectations | length > 0)))
             ' "$f" >/dev/null 2>&1; then
    fail "$f: schema invalid"
    return
  fi
  local skill_name
  skill_name="$(jq -r '.skill_name' "$f")"
  if [ ! -f "skills/$skill_name/SKILL.md" ]; then
    fail "$f: skill_name '$skill_name' has no skills/$skill_name/SKILL.md"
    return
  fi
  ok "$f (skill=$skill_name)"
}

run_filter() {
  local pattern="$1"
  local found=0
  while IFS= read -r f; do
    found=1
    validate_eval_file "$f"
  done < <(find evals -path "$pattern" -name '*.json' 2>/dev/null)
  if [ $found -eq 0 ]; then
    echo "NOTE no eval files matched: $pattern"
  fi
}

run_phase() {
  local n="$1"
  case "$n" in
    1)
      validate_eval_file evals/research/tax-research-federal.json 2>/dev/null \
        || true
      validate_eval_file evals/prediction/predict-worker-classification.json 2>/dev/null \
        || true
      validate_eval_file evals/summary/return-summary-1040.json 2>/dev/null \
        || true
      # Iterate all phase-1 files via filter:
      while IFS= read -r f; do
        validate_eval_file "$f"
      done < <(find evals -name '*.json' 2>/dev/null \
                | grep -E '(tax-research-federal|predict-worker-classification|return-summary-1040)\.json$')
      ;;
    *)
      while IFS= read -r f; do
        validate_eval_file "$f"
      done < <(find evals -name '*.json' 2>/dev/null)
      ;;
  esac
}

run_full() {
  while IFS= read -r f; do
    validate_eval_file "$f"
  done < <(find evals -name '*.json' 2>/dev/null)
}

run_skill() {
  local s="$1"
  local found=0
  while IFS= read -r f; do
    found=1
    validate_eval_file "$f"
  done < <(find evals -name "$s.json" 2>/dev/null)
  if [ $found -eq 0 ]; then
    fail "no eval file found for skill: $s"
  fi
}

main() {
  local mode="${1:-full}"
  case "$mode" in
    full)
      run_full
      ;;
    phase)
      run_phase "${2:-1}"
      ;;
    skill)
      run_skill "${2:-}"
      ;;
    *)
      echo "usage: run-evals.sh full | phase <N> | skill <name>"
      exit 2
      ;;
  esac

  # Strip trailing flag like --summary if present (informational only)
  echo
  echo "Summary: pass=$PASS fail=$FAIL"
  [ $FAIL -eq 0 ]
}

main "$@"
