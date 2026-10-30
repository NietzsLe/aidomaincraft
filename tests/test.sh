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
grep -q 'aidomaincraft agents-block v4' "$t1/AGENTS.md" && ok "agents stamp v4" || bad "agents stamp"
grep -q 'aidomaincraft claude-block v4' "$t1/CLAUDE.md" && ok "claude stamp v4" || bad "claude stamp"
[ ! -e "$t1/.aidomaincraft" ] && ok "no vendor dir by default" || bad "vendor dir leaked"
[ ! -e "$t1/.gitignore" ] && ok "no gitignore by default" || bad "gitignore leaked"

# 2. idempotent reinstall
out=$($setup install --target "$t1")
echo "$out" | grep -q 'unchanged (already v4)' && ok "idempotent" || bad "idempotent: $out"

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
grep -q 'template agents-block.md: v4' "$t1.ver" && ok "version template" || bad "version template"
grep -q 'source CHARTER: v8' "$t1.ver" && ok "version charter" || bad "version charter"
grep -q 'AGENTS.md: block v4' "$t1.ver" && ok "version installed" || bad "version installed"

# 10. check-update up-to-date, then flags a stale v1 block
$setup check-update --target "$t1" >/dev/null && ok "check-update clean" || bad "check-update clean"
t6=$(mktemp -d); $setup install --target "$t6" >/dev/null
sed -i 's/aidomaincraft agents-block v4/aidomaincraft agents-block v1/; s/aidomaincraft claude-block v4/aidomaincraft claude-block v1/' "$t6/AGENTS.md" "$t6/CLAUDE.md"
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
grep -q 'Absolute compliance' "$t1/CLAUDE.md" && ok "claude compliance" || bad "claude missing compliance"

# 11. upgrade refreshes stale blocks in one command
$setup upgrade --target "$t6" >/dev/null
grep -q 'aidomaincraft agents-block v4' "$t6/AGENTS.md" && ok "upgrade to v4" || bad "upgrade"
$setup check-update --target "$t6" >/dev/null && ok "clean after upgrade" || bad "still stale after upgrade"
$setup upgrade --target "$t6" | grep -q 'unchanged (already v4)' && ok "upgrade idempotent" || bad "upgrade idempotent"

# 12. vendor upgrade refreshes snapshot
t7=$(mktemp -d); $setup install --target "$t7" --vendor >/dev/null
echo STALE > "$t7/.aidomaincraft/CHARTER.md"
$setup upgrade --target "$t7" >/dev/null
grep -q STALE "$t7/.aidomaincraft/CHARTER.md" && bad "vendor snapshot not refreshed" || ok "vendor snapshot refreshed"

rm -rf "$t1" "$t2" "$t3" "$t4" "$t5" "$t6" "$t7" "$t1.ver"
echo "---"
echo "pass=$pass fail=$fail"
[ "$fail" = "0" ]
