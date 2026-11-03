#!/bin/sh
# Acceptance tests for the aidomaincraft installer (no network, /tmp only).
set -eu
here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
root=$(CDPATH= cd -- "$here/.." && pwd)
setup="python3 $root/scripts/aidomaincraft_setup.py"
pass=0
fail=0

ok() { pass=$((pass+1)); echo "ok: $1"; }
bad() { fail=$((fail+1)); echo "FAIL: $1"; }

t1=$(mktemp -d)
# 1. reference-only install into empty dir
$setup install --target "$t1" >/dev/null
[ "$(grep -cF '<!-- BEGIN aidomaincraft -->' "$t1/AGENTS.md")" = "1" ] && ok "agents block count 1" || bad "agents block count"
[ "$(grep -cF '<!-- BEGIN aidomaincraft -->' "$t1/CLAUDE.md")" = "1" ] && ok "claude block count 1" || bad "claude block count"
grep -q 'aidomaincraft agents-block v5' "$t1/AGENTS.md" && ok "agents stamp v5" || bad "agents stamp"
grep -q 'aidomaincraft claude-block v5' "$t1/CLAUDE.md" && ok "claude stamp v5" || bad "claude stamp"
[ ! -e "$t1/.aidomaincraft" ] && ok "no vendor dir by default" || bad "vendor dir leaked"
[ ! -e "$t1/.gitignore" ] && ok "no gitignore by default" || bad "gitignore leaked"

# 2. idempotent reinstall
out=$($setup install --target "$t1")
echo "$out" | grep -q 'unchanged (already v5)' && ok "idempotent" || bad "idempotent: $out"

# 3. custom source/ref renders into block
t2=$(mktemp -d)
$setup install --target "$t2" --source https://example.com/fork.git --ref v9 >/dev/null
grep -q 'https://example.com/fork.git' "$t2/AGENTS.md" && ok "custom source" || bad "custom source"
grep -q -- '--branch v9' "$t2/AGENTS.md" && ok "custom ref" || bad "custom ref"

# 4. vendor mode copies snapshot + gitignore
t3=$(mktemp -d)
$setup install --target "$t3" --vendor >/dev/null
[ -f "$t3/.aidomaincraft/CHARTER.md" ] && ok "vendor charter" || bad "vendor charter"
[ -d "$t3/.aidomaincraft/items" ] && ok "vendor items" || bad "vendor items"
[ -f "$t3/.aidomaincraft/install.json" ] && ok "vendor manifest" || bad "vendor manifest"
grep -qF '.aidomaincraft/' "$t3/.gitignore" && ok "vendor gitignore" || bad "vendor gitignore"

# 5. doctor OK on reference + vendor
$setup doctor --target "$t1" >/dev/null && ok "doctor reference OK" || bad "doctor reference"
$setup doctor --target "$t3" >/dev/null && ok "doctor vendor OK" || bad "doctor vendor"

# 6. uninstall default (vendor moved aside, blocks gone)
$setup uninstall --target "$t3" >/dev/null
[ "$(grep -cF '<!-- BEGIN aidomaincraft -->' "$t3/AGENTS.md" 2>/dev/null || echo 0)" = "0" ] && ok "uninstall blocks gone" || bad "uninstall blocks"
[ ! -e "$t3/.aidomaincraft" ] && ok "uninstall vendor moved" || bad "uninstall vendor still present"
ls -d "$t3"/.aidomaincraft.removed-* >/dev/null 2>&1 && ok "removed dir kept" || bad "removed dir missing"

# 7. uninstall idempotent + purge path
$setup uninstall --target "$t3" >/dev/null && ok "uninstall idempotent" || bad "uninstall idempotent"
t4=$(mktemp -d); $setup install --target "$t4" --vendor >/dev/null
$setup uninstall --target "$t4" --purge >/dev/null
[ ! -e "$t4/.aidomaincraft" ] && ok "purge deletes" || bad "purge"
ls -d "$t4"/.aidomaincraft.removed-* >/dev/null 2>&1 && bad "purge left removed dir" || ok "purge no removed dir"

# 8. unbalanced markers refuse
t5=$(mktemp -d); printf 'x\n<!-- BEGIN aidomaincraft -->\n' > "$t5/AGENTS.md"
if $setup install --target "$t5" >/dev/null 2>&1; then bad "unbalanced accepted"; else ok "unbalanced refused"; fi

# 9. version prints 3 axes (installer + template + CHARTER + installed)
$setup version --target "$t1" > "$t1.ver"
grep -q 'installer 1.1.0' "$t1.ver" && ok "version installer" || bad "version installer"
grep -q 'template agents-block.md: v5' "$t1.ver" && ok "version template" || bad "version template"
grep -q 'source CHARTER: v10' "$t1.ver" && ok "version charter" || bad "version charter"
grep -q 'AGENTS.md: block v5' "$t1.ver" && ok "version installed" || bad "version installed"

# 10. check-update up-to-date, then flags a stale v1 block
$setup check-update --target "$t1" >/dev/null && ok "check-update clean" || bad "check-update clean"
t6=$(mktemp -d); $setup install --target "$t6" >/dev/null
sed -i 's/aidomaincraft agents-block v5/aidomaincraft agents-block v1/; s/aidomaincraft claude-block v5/aidomaincraft claude-block v1/' "$t6/AGENTS.md" "$t6/CLAUDE.md"
if $setup check-update --target "$t6" >/dev/null 2>&1; then bad "check-update missed stale"; else ok "check-update flags stale"; fi
$setup check-update --target "$t6" 2>&1 | grep -q 'UPDATE AVAILABLE' && ok "suggests update" || bad "no update suggestion"
$setup doctor --target "$t6" >/dev/null 2>&1 && bad "doctor missed stale" || ok "doctor flags stale"
grep -q 'Agent-first versions' "$t1/AGENTS.md" && ok "block has agent-first mapping" || bad "block missing agent-first mapping"
grep -q 'ask for confirmation first' "$t1/AGENTS.md" && ok "block asks before upgrade" || bad "block missing ask-first rule"
grep -q 'có bản mới không' "$t1/AGENTS.md" && ok "block maps plain user asks" || bad "block missing plain-ask mapping"
grep -q 'Agent-first versions' "$t1/CLAUDE.md" && ok "claude block agent-first" || bad "claude block agent-first"

# 10b. absolute compliance: 5 classes + hard list + adapt-and-approve
for c in must-read env-gate must-follow must-verify must-not; do
  grep -q -- "$c" "$t1/AGENTS.md" && ok "class $c" || bad "missing class $c"
done
for h in hallmark reactbits skillry awesome-opus5-5-videos delegation; do
  grep -q -- "$h" "$t1/AGENTS.md" && ok "hard $h" || bad "missing hard $h"
done
grep -q 'Adapt-and-approve' "$t1/AGENTS.md" && ok "adapt-approve" || bad "missing adapt-approve"
grep -q 'Approval gate' "$t1/AGENTS.md" && ok "approval gate" || bad "missing approval gate"
grep -q 'never offered as options' "$t1/AGENTS.md" && ok "red line" || bad "missing red line"
grep -q 'Core-fidelity' "$t1/AGENTS.md" && ok "core-fidelity" || bad "missing core-fidelity"
grep -q 'Handoff format' "$t1/AGENTS.md" && ok "handoff format" || bad "missing handoff format"
grep -q 'Invariant core / Customizable surface' "$t1/AGENTS.md" && ok "core triad pointer" || bad "missing core triad pointer"
grep -q 'Core-fidelity' "$t1/CLAUDE.md" && ok "claude core-fidelity" || bad "claude missing core-fidelity"
grep -q 'Absolute compliance' "$t1/CLAUDE.md" && ok "claude compliance" || bad "claude missing compliance"

# 11. upgrade refreshes stale blocks in one command
$setup upgrade --target "$t6" >/dev/null
grep -q 'aidomaincraft agents-block v5' "$t6/AGENTS.md" && ok "upgrade to v5" || bad "upgrade"
$setup check-update --target "$t6" >/dev/null && ok "clean after upgrade" || bad "still stale after upgrade"
$setup upgrade --target "$t6" | grep -q 'unchanged (already v5)' && ok "upgrade idempotent" || bad "upgrade idempotent"

# 12. vendor upgrade refreshes snapshot
t7=$(mktemp -d); $setup install --target "$t7" --vendor >/dev/null
echo STALE > "$t7/.aidomaincraft/CHARTER.md"
$setup upgrade --target "$t7" >/dev/null
grep -q STALE "$t7/.aidomaincraft/CHARTER.md" && bad "vendor snapshot not refreshed" || ok "vendor snapshot refreshed"

# 13. REGISTRY in sync with items/ (CHARTER v10 §4b)
reg="$root/items/REGISTRY.md"
[ -f "$reg" ] && ok "registry exists" || bad "registry missing"
for d in "$root"/items/*/; do
  n=$(basename "$d")
  [ "$n" = "REGISTRY.md" ] && continue
  grep -q "| \`$n\` " "$reg" && ok "registry has $n" || bad "registry missing $n"
done
while IFS= read -r line; do
  case "$line" in
    "| \`"*)
      n=$(printf '%s' "$line" | sed 's/^| `\([^`]*\)`.*/\1/')
      [ -d "$root/items/$n" ] && ok "registry row live: $n" || bad "registry orphan row: $n"
      origin=$(printf '%s' "$line" | awk -F'|' '{print $3}')
      case "$origin" in
        *nội\ tại*)
          grep -q 'Nguồn gốc' "$root/items/$n/README.md" && ok "$n has Nguon goc" || bad "$n missing Nguon goc"
          grep -q 'Áp dụng' "$root/items/$n/README.md" && ok "$n has Ap dung" || bad "$n missing Ap dung"
          ;;
      esac
      ;;
  esac
done < "$reg"

# 14. wireframe-docs drafts stay under ignored .aidomaincraft/.tmp dated folders (v10.6)
grep -q '\.aidomaincraft/\.tmp/wireframes/' "$root/items/wireframe-docs/README.md" && ok "wireframe dated path" || bad "wireframe dated path missing"
grep -q 'YYYY-MM-DD-HHmm' "$root/items/wireframe-docs/README.md" && ok "wireframe datetime folders" || bad "datetime folder rule missing"
grep -q 'git check-ignore' "$root/items/wireframe-docs/README.md" && ok "wireframe gitignore check" || bad "wireframe gitignore check missing"
grep -q '\.aidomaincraft/\.tmp/wireframes/' "$root/domains/ui/using-wireframe-docs.md" && ok "using dated path" || bad "using dated path missing"
grep -q 'templates/viewer\.html' "$root/items/wireframe-docs/README.md" && ok "viewer in item" || bad "viewer missing in item"
[ -f "$root/items/wireframe-docs/templates/viewer.html" ] && ok "viewer file exists" || bad "viewer file missing"
for w in 360 768 1366 1920; do
  grep -q "$w" "$root/items/wireframe-docs/templates/viewer.html" && ok "viewer has $w" || bad "viewer missing $w"
done
for w in 320 390 412 430 800 834 1280 1440 1600 2560; do
  grep -q "$w" "$root/items/wireframe-docs/convention/tree-format.md" && ok "variant $w documented" || bad "variant $w missing"
done
grep -qF '.aidomaincraft/' "$root/.gitignore" && ok "root gitignores aidomaincraft" || bad "root aidomaincraft not ignored"

# 15. wireframe-docs pair model: no build.py, standalone check, verified pair (v10.4)
[ ! -e "$root/items/wireframe-docs/scripts/build.py" ] && ok "no build.py" || bad "build.py still present"
! grep -rn 'scripts/build\.py' "$root/items/wireframe-docs/" "$root/domains/ui/using-wireframe-docs.md" "$root/domains/ui/README.md" 2>/dev/null | grep -v __pycache__ && ok "no build.py invocations" || bad "stale build.py invocations"
grep -q 'verify-pair' "$root/items/wireframe-docs/README.md" && ok "pair in item" || bad "pair missing in item"
grep -q 'data-wf-' "$root/items/wireframe-docs/convention/tree-format.md" && ok "wireframe standard" || bad "wireframe standard missing"
grep -q '4 breakpoints' "$root/items/wireframe-docs/README.md" && ok "4 breakpoints" || bad "4 breakpoints missing"
python3 "$root/items/wireframe-docs/scripts/check.py" "$root/items/wireframe-docs/examples/tree.md" >/dev/null 2>&1 && ok "example tree PASS" || bad "example tree FAIL"
python3 "$root/items/wireframe-docs/scripts/verify-pair.py" "$root/items/wireframe-docs/examples/tree.md" "$root/items/wireframe-docs/examples/tree.html" >/dev/null 2>&1 && ok "example pair PASS" || bad "example pair FAIL"
t8=$(mktemp -d)
printf '# Page: P\n\n## Section: S\n- `Button` **B** — note: n | states: default\n' > "$t8/t-tree.md"
printf '<div data-wf-page="Q"><div data-wf-breakpoint="sm" data-wf-width="360"><section data-wf-section="S" data-wf-layout="stack"></section></div></div>' > "$t8/t-wire.html"
if python3 "$root/items/wireframe-docs/scripts/verify-pair.py" "$t8/t-tree.md" "$t8/t-wire.html" >/dev/null 2>&1; then bad "drifting pair passed"; else ok "drifting pair FAIL"; fi
rm -rf "$t8"

rm -rf "$t1" "$t2" "$t3" "$t4" "$t5" "$t6" "$t7" "$t1.ver"
echo "---"
echo "pass=$pass fail=$fail"
[ "$fail" = "0" ]
