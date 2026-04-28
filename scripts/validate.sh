#!/usr/bin/env bash
# scripts/validate.sh — Vibe CPA Skills validation harness
#
# Usage:
#   ./scripts/validate.sh full
#   ./scripts/validate.sh phase <N>
#   ./scripts/validate.sh skill <skill-name>
#
# Exits 0 on success, non-zero on failure.

set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
NC='\033[0m'

PASS=0
FAIL=0
WARN=0

ok()   { echo -e "${GREEN}OK${NC}   $*"; PASS=$((PASS+1)); }
fail() { echo -e "${RED}FAIL${NC} $*"; FAIL=$((FAIL+1)); }
warn() { echo -e "${YELLOW}WARN${NC} $*"; WARN=$((WARN+1)); }

# --- helpers ---------------------------------------------------------------

require_cmd() {
  for c in "$@"; do
    if ! command -v "$c" >/dev/null 2>&1; then
      warn "missing CLI: $c (some checks will be skipped)"
      return 1
    fi
  done
}

extract_yaml_field() {
  # Reads a top-level scalar field out of a SKILL.md frontmatter block.
  # Frontmatter must start with --- on line 1 and end with --- on a line.
  local file="$1" field="$2"
  awk -v f="$field" '
    BEGIN { in_fm=0; line=0 }
    /^---[[:space:]]*$/ { line++; if (line==1) { in_fm=1; next } else if (line==2) { exit } }
    in_fm==1 {
      if ($0 ~ "^"f":") {
        sub("^"f":[[:space:]]*", "")
        # strip surrounding quotes if any
        gsub("^[\"'\''[:space:]]+|[\"'\''[:space:]]+$", "")
        print
        exit
      }
    }
  ' "$file"
}

# --- checks ---------------------------------------------------------------

check_directory_tree() {
  local missing=0
  for d in skills shared scripts evals examples docs .claude-plugin .claude .github; do
    if [ ! -d "$d" ]; then
      fail "missing directory: $d"
      missing=$((missing+1))
    fi
  done
  [ $missing -eq 0 ] && ok "directory tree present"
}

check_root_files() {
  local missing=0
  for f in CLAUDE.md BUILD_PLAN.md QUESTIONS.md LICENSE DISCLAIMER.md \
           CONTRIBUTING.md CHANGELOG.md README.md .gitignore; do
    if [ ! -f "$f" ]; then
      fail "missing root file: $f"
      missing=$((missing+1))
    fi
  done
  [ $missing -eq 0 ] && ok "root files present"
}

check_shared_files() {
  local missing=0
  for f in citation-discipline.md authority-hierarchy.md confidence-bands.md \
           compliance.md legislation-tracking.md live-sources.md \
           sources.json output-schema.json state-template.md; do
    if [ ! -f "shared/$f" ]; then
      fail "missing shared/$f"
      missing=$((missing+1))
    fi
  done
  [ $missing -eq 0 ] && ok "shared/ files present"
}

check_legislation_tracking() {
  if [ ! -f shared/legislation-tracking.md ]; then
    fail "MISSING: shared/legislation-tracking.md"
    return 1
  fi
  ok "shared/legislation-tracking.md present"
}

check_json_parse() {
  local fail_count=0
  local py=""
  # Pick a working JSON parser. On Windows, `python3` is sometimes a Microsoft
  # Store stub that satisfies `command -v` but errors when invoked; fall back
  # to plain `python` if so.
  if command -v jq >/dev/null 2>&1; then
    py=""
  elif command -v python3 >/dev/null 2>&1 && python3 -c '' >/dev/null 2>&1; then
    py="python3"
  elif command -v python >/dev/null 2>&1 && python -c '' >/dev/null 2>&1; then
    py="python"
  else
    warn "skipped JSON parse check (jq and python missing)"
    return 0
  fi
  while IFS= read -r f; do
    if [ -n "$py" ]; then
      if ! "$py" -c "import json,sys; json.load(open(sys.argv[1]))" "$f" >/dev/null 2>&1; then
        fail "JSON parse error: $f"
        fail_count=$((fail_count+1))
      fi
    else
      if ! jq empty "$f" >/dev/null 2>&1; then
        fail "JSON parse error: $f"
        fail_count=$((fail_count+1))
      fi
    fi
  done < <(find . -name '*.json' \
            -not -path './node_modules/*' \
            -not -path './.git/*' \
            -not -path './evals/runs/*')
  [ $fail_count -eq 0 ] && ok "all JSON files parse"
}

check_skill_frontmatter() {
  local fail_count=0
  while IFS= read -r f; do
    local name desc
    name="$(extract_yaml_field "$f" name)"
    desc="$(awk '
      BEGIN { in_fm=0; line=0; in_desc=0; out=""; }
      /^---[[:space:]]*$/ { line++; if (line==1) { in_fm=1; next } else if (line==2) { exit } }
      in_fm==1 {
        if ($0 ~ /^description:[[:space:]]*\|/) { in_desc=1; next }
        if (in_desc==1) {
          if ($0 ~ /^[A-Za-z_-]+:/) { in_desc=0 }
          else { out = out $0 "\n"; next }
        }
        if ($0 ~ /^description:[[:space:]]*[^|]/) {
          sub(/^description:[[:space:]]*/, "")
          out = $0
        }
      }
      END { print out }
    ' "$f")"

    if [ -z "$name" ]; then
      fail "$f: missing 'name' frontmatter"
      fail_count=$((fail_count+1))
      continue
    fi
    if [ ${#name} -gt 64 ]; then
      fail "$f: name '$name' is ${#name} chars (max 64)"
      fail_count=$((fail_count+1))
    fi
    case "$name" in
      *anthropic*|*claude*)
        fail "$f: name '$name' uses reserved word"
        fail_count=$((fail_count+1))
      ;;
    esac
    if [ -z "$desc" ]; then
      fail "$f: missing 'description' frontmatter"
      fail_count=$((fail_count+1))
      continue
    fi
    local len=${#desc}
    if [ "$len" -gt 1024 ]; then
      fail "$f: description $len chars > 1024"
      fail_count=$((fail_count+1))
    fi
  done < <(find skills -name SKILL.md 2>/dev/null)
  [ $fail_count -eq 0 ] && ok "SKILL.md frontmatter validates"
}

check_no_sentinels() {
  if grep -rn 'CITATION NEEDED' skills/ 2>/dev/null \
       | grep -v '/template' \
       | grep -v '/states/' >/dev/null; then
    fail "CITATION NEEDED sentinel found in published skill (excludes template + states/)"
    grep -rn 'CITATION NEEDED' skills/ \
       | grep -v '/template' \
       | grep -v '/states/' | head -20
    return 1
  fi
  ok "no fabricated-citation sentinels in published skills"
}

check_state_stubs() {
  local expected_codes="AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY"
  local fail_count=0
  for skill in tax-research-state-income tax-research-state-salesuse; do
    if [ ! -d "skills/$skill/references/states" ]; then
      warn "skipped state-stub check for $skill (directory missing — Phase 3 not started)"
      continue
    fi
    for code in $expected_codes; do
      f="skills/$skill/references/states/$code.md"
      if [ ! -f "$f" ]; then
        fail "MISSING: $f"
        fail_count=$((fail_count+1))
      else
        actual="$(extract_yaml_field "$f" state_code)"
        if [ "$actual" != "$code" ]; then
          fail "MISMATCH: $f frontmatter state_code='$actual' (expected $code)"
          fail_count=$((fail_count+1))
        fi
      fi
    done
  done
  [ $fail_count -eq 0 ] && ok "state stubs complete (51 per state research skill)"
}

check_authority_taxonomy() {
  local schema_types py=""
  if command -v jq >/dev/null 2>&1; then
    schema_types="$(jq -r '.properties.authorities.items.properties.authority_type.enum[]' \
                    shared/output-schema.json 2>/dev/null | sort -u)"
  elif command -v python3 >/dev/null 2>&1 && python3 -c '' >/dev/null 2>&1; then
    py="python3"
  elif command -v python >/dev/null 2>&1 && python -c '' >/dev/null 2>&1; then
    py="python"
  else
    warn "skipped authority_type taxonomy check (jq and python missing)"
    return 0
  fi
  if [ -n "$py" ]; then
    schema_types="$($py -c "import json; [print(t) for t in sorted(set(json.load(open('shared/output-schema.json'))['properties']['authorities']['items']['properties']['authority_type']['enum']))]" 2>/dev/null)"
  fi
  if [ -z "$schema_types" ]; then
    fail "could not extract authority_type enum from shared/output-schema.json"
    return 1
  fi
  # Heuristic: pull "authority_type": "X" tokens out of references/
  local drift=0
  if find skills -path '*/references/*' -name '*.md' 2>/dev/null | head -1 >/dev/null; then
    local used
    used="$(grep -rho '"authority_type"[[:space:]]*:[[:space:]]*"[A-Za-z_]*"' skills/*/references/ 2>/dev/null \
            | sed -E 's/.*"([A-Za-z_]+)"$/\1/' | sort -u)"
    for t in $used; do
      if ! echo "$schema_types" | grep -qx "$t"; then
        warn "authority_type '$t' used in references but not in schema enum"
        drift=$((drift+1))
      fi
    done
  fi
  [ $drift -eq 0 ] && ok "authority_type taxonomy consistent with schema enum"
}

check_url_liveness() {
  if ! command -v curl >/dev/null 2>&1; then
    warn "skipped URL liveness (curl missing)"
    return 0
  fi
  if [ "${SKIP_URL_CHECK:-}" = "1" ]; then
    warn "URL liveness check skipped (SKIP_URL_CHECK=1)"
    return 0
  fi
  local urls py=""
  if command -v jq >/dev/null 2>&1; then
    urls="$(jq -r '.. | strings? | select(test("^https?://"))' shared/sources.json | sort -u)"
  elif command -v python3 >/dev/null 2>&1 && python3 -c '' >/dev/null 2>&1; then
    py="python3"
  elif command -v python >/dev/null 2>&1 && python -c '' >/dev/null 2>&1; then
    py="python"
  else
    warn "skipped URL liveness (jq and python missing)"
    return 0
  fi
  if [ -n "$py" ]; then
    urls="$($py -c "
import json,re
def walk(o):
  if isinstance(o,str):
    if re.match(r'^https?://',o): print(o)
  elif isinstance(o,dict):
    for v in o.values(): walk(v)
  elif isinstance(o,list):
    for v in o: walk(v)
walk(json.load(open('shared/sources.json')))
" | sort -u)"
  fi
  local fail_count=0
  local total=0
  for u in $urls; do
    total=$((total+1))
    if ! curl -fsSL --max-time 15 -o /dev/null "$u" 2>/dev/null; then
      sleep 2
      if ! curl -fsSL --max-time 15 -o /dev/null "$u" 2>/dev/null; then
        warn "dead URL: $u"
        fail_count=$((fail_count+1))
      fi
    fi
  done
  if [ "$fail_count" -gt 5 ]; then
    fail "too many dead URLs ($fail_count of $total). Investigate."
    return 1
  fi
  ok "URL liveness check ($total URLs, $fail_count flakes ≤ 5 budget)"
}

check_skill() {
  # Per-skill validation
  local skill="$1"
  local f="skills/$skill/SKILL.md"
  if [ ! -f "$f" ]; then
    fail "skill not found: $skill"
    return 1
  fi
  local name desc
  name="$(extract_yaml_field "$f" name)"
  if [ -z "$name" ]; then
    fail "$f: missing name"
    return 1
  fi
  if ! grep -q 'shared/citation-discipline.md' "$f"; then
    fail "$f: missing reference to shared/citation-discipline.md"
    return 1
  fi
  if ! grep -q 'shared/compliance.md' "$f"; then
    fail "$f: missing reference to shared/compliance.md"
    return 1
  fi
  ok "skill $skill validates"
}

# --- entry points ---------------------------------------------------------

run_phase_0() {
  check_directory_tree
  check_root_files
  check_shared_files
  check_legislation_tracking
  check_json_parse
}

run_phase_1() {
  check_directory_tree
  check_shared_files
  check_skill_frontmatter
  check_json_parse
  check_no_sentinels
  for s in cpa-pack-index tax-research-federal predict-worker-classification \
           return-summary-1040; do
    [ -d "skills/$s" ] && check_skill "$s"
  done
}

run_phase_2() {
  check_skill_frontmatter
  check_json_parse
  check_no_sentinels
  check_authority_taxonomy
}

run_phase_3() {
  check_skill_frontmatter
  check_json_parse
  check_no_sentinels
  check_state_stubs
  check_authority_taxonomy
}

run_phase_4() {
  check_skill_frontmatter
  check_json_parse
  check_no_sentinels
}

run_phase_5() {
  check_skill_frontmatter
  check_json_parse
  check_authority_taxonomy
  if [ -f .claude-plugin/plugin.json ]; then ok "plugin.json present"; else fail "missing plugin.json"; fi
  if [ -f .claude-plugin/marketplace.json ]; then ok "marketplace.json present"; else fail "missing marketplace.json"; fi
}

run_phase_6() {
  check_directory_tree
  check_root_files
  check_shared_files
  check_legislation_tracking
  check_json_parse
  check_skill_frontmatter
  check_no_sentinels
  check_state_stubs
  check_authority_taxonomy
}

run_full() {
  check_directory_tree
  check_root_files
  check_shared_files
  check_legislation_tracking
  check_json_parse
  check_skill_frontmatter
  check_no_sentinels
  check_state_stubs
  check_authority_taxonomy
  check_url_liveness
}

main() {
  local mode="${1:-full}"
  case "$mode" in
    full)   run_full ;;
    phase)
      local n="${2:-0}"
      case "$n" in
        0) run_phase_0 ;;
        1) run_phase_1 ;;
        2) run_phase_2 ;;
        3) run_phase_3 ;;
        4) run_phase_4 ;;
        5) run_phase_5 ;;
        6) run_phase_6 ;;
        7) run_full ;;
        *) fail "unknown phase: $n"; exit 2 ;;
      esac
    ;;
    skill)
      local s="${2:-}"
      [ -n "$s" ] || { fail "usage: validate.sh skill <name>"; exit 2; }
      check_skill "$s"
    ;;
    *) fail "usage: validate.sh full | phase <N> | skill <name>"; exit 2 ;;
  esac

  echo
  echo "Summary: pass=$PASS fail=$FAIL warn=$WARN"
  [ $FAIL -eq 0 ]
}

main "$@"
