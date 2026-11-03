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

# 14. wireframe-docs suites live under ignored .aidomaincraft/.tmp (v10.8)
grep -q '\.aidomaincraft/\.tmp/wireframes/<suite>' "$root/items/wireframe-docs/README.md" && ok "wireframe suite path" || bad "wireframe suite path missing"
grep -q 'flows/' "$root/items/wireframe-docs/README.md" && ok "flows in item" || bad "flows missing in item"
grep -q 'brief\.md' "$root/items/wireframe-docs/README.md" && ok "brief in item" || bad "brief missing in item"
grep -q 'git check-ignore' "$root/items/wireframe-docs/README.md" && ok "wireframe gitignore check" || bad "wireframe gitignore check missing"
grep -q '\.aidomaincraft/\.tmp/wireframes/<suite>' "$root/domains/ui/using-wireframe-docs.md" && ok "using suite path" || bad "using suite path missing"
[ -f "$root/items/wireframe-docs/convention/flows.md" ] && ok "flows doc exists" || bad "flows doc missing"
[ -f "$root/items/wireframe-docs/convention/brief-template.md" ] && ok "brief template exists" || bad "brief template missing"
[ -f "$root/items/wireframe-docs/convention/constraints.md" ] && ok "constraints doc exists" || bad "constraints doc missing"
[ -f "$root/items/wireframe-docs/scripts/check-flow.py" ] && ok "check-flow exists" || bad "check-flow missing"
[ -f "$root/items/wireframe-docs/scripts/build-flow.py" ] && ok "build-flow exists" || bad "build-flow missing"
[ -f "$root/items/wireframe-docs/scripts/check-suite.py" ] && ok "check-suite exists" || bad "check-suite missing"
[ -f "$root/items/wireframe-docs/templates/player.template.html" ] && ok "player template exists" || bad "player template missing"
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
printf '# Page: P\n\n## Section: S\n- `Button` **B** — note: n | states: default, focus\n' > "$t8/t-tree.md"
printf '{"page": "P", "values": {"B": "bee"}}' > "$t8/t-data.json"
printf '<div data-wf-page="Q"><div data-wf-breakpoint="sm" data-wf-width="360"><section data-wf-section="S" data-wf-layout="stack"></section></div></div>' > "$t8/t-wire.html"
if python3 "$root/items/wireframe-docs/scripts/verify-pair.py" "$t8/t-tree.md" "$t8/t-wire.html" "$t8/t-data.json" >/dev/null 2>&1; then bad "drifting pair passed"; else ok "drifting pair FAIL"; fi
rm -rf "$t8"

# 16. wireframe-docs v10.7: vocab + data + guidelines (checked 03/11/2026)
[ "$(grep -c '^[A-Za-z]*$' "$root/items/wireframe-docs/convention/component-roles.md" 2>/dev/null || echo 0)" -ge 60 ] && ok "vocab pinned 60+" || bad "vocab list short"
grep -q '^Accordion: group$' "$root/items/wireframe-docs/convention/component-roles.md" && ok "role-map present" || bad "role-map missing"
grep -q '^fade-scale: ' "$root/items/wireframe-docs/convention/animations.md" && ok "anim catalog present" || bad "anim catalog missing"
grep -q 'ref:' "$root/items/wireframe-docs/convention/animations.md" && ok "ref rule documented" || bad "ref rule missing"
[ -f "$root/items/wireframe-docs/convention/references.md" ] && ok "references doc exists" || bad "references doc missing"
[ -f "$root/items/wireframe-docs/convention/data-schema.md" ] && ok "data schema exists" || bad "data schema missing"
[ -f "$root/items/wireframe-docs/examples/data.json" ] && ok "example data exists" || bad "example data missing"
python3 "$root/items/wireframe-docs/scripts/check-guidelines.py" "$root/items/wireframe-docs/examples/tree.md" > "$t1.guide" 2>&1 && ok "guidelines example SCORE" || bad "guidelines example FAIL"
grep -q 'SCORE: 6/6' "$t1.guide" && ok "guidelines 6/6" || bad "guidelines score wrong"
t9=$(mktemp -d)
printf '# Page: P\n\n## Section: S\n- `Button` **B** — note: n | states: default\n' > "$t9/t-tree.md"
printf '{"page": "P", "values": {"B": "bee"}}' > "$t9/t-data.json"
if python3 "$root/items/wireframe-docs/scripts/check-guidelines.py" "$t9/t-tree.md" "$t9/t-data.json" >/dev/null 2>&1; then bad "missing focus passed"; else ok "missing focus FAIL"; fi
cp "$root/items/wireframe-docs/examples/tree.html" "$t9/t-wire.html"
cp "$root/items/wireframe-docs/examples/tree.md" "$t9/t-tree.md"
cp "$root/items/wireframe-docs/examples/data.json" "$t9/data.json"
python3 -c "import json;p='$t9/data.json';d=json.load(open(p));d['values']['Email']='khong-co-trong-html';json.dump(d,open(p,'w'),ensure_ascii=False)"
if python3 "$root/items/wireframe-docs/scripts/verify-pair.py" "$t9/t-tree.md" "$t9/t-wire.html" "$t9/data.json" >/dev/null 2>&1; then bad "missing value passed"; else ok "missing value FAIL"; fi
rm -rf "$t9"

# 17. wireframe-docs suites + flows + player + check-suite (v10.8)
t10=$(mktemp -d)
mkdir -p "$t10/suite/checkout" "$t10/suite/flows"
printf '# Brief: Demo\n\n## Muc tieu\n- x\n\n## Yeu cau\n- REQ-01: thu email\n- REQ-02: xac nhan don\n' > "$t10/suite/brief.md"
cp "$root/items/wireframe-docs/examples/tree.md" "$t10/suite/checkout/tree.md"
cp "$root/items/wireframe-docs/examples/tree.html" "$t10/suite/checkout/tree.html"
cp "$root/items/wireframe-docs/examples/data.json" "$t10/suite/checkout/data.json"
printf '# Flow: Mua\n\n- Entry: checkout @ sm\n\n## Step 1: Nhap\n- Page: checkout | Action: `Button` **Đặt hàng** | Expect: ok\n- go: back\n' > "$t10/suite/flows/mua.md"
printf '# Flow: Nhap\n\n- Entry: checkout @ sm\n\n## Step 1: Dien\n- Page: checkout | Expect: thay chu\n- Input: Email = Email\n- go: back\n' > "$t10/suite/flows/nhap.md"
python3 "$root/items/wireframe-docs/scripts/check-flow.py" "$t10/suite" >/dev/null 2>&1 && ok "flow PASS" || bad "flow FAIL"
python3 "$root/items/wireframe-docs/scripts/build-flow.py" "$t10/suite" >/dev/null 2>&1 && ok "player built" || bad "player build FAIL"
[ -f "$t10/suite/player.html" ] && ok "player.html exists" || bad "player.html missing"
grep -q '"inputs": \[\["Email", "Email"\]\]' "$t10/suite/player.html" && ok "input DSL embedded" || bad "input DSL missing"
grep -q '#stage .frame' "$t10/suite/player.html" && ok "wireframe CSS scoped" || bad "CSS not scoped"
if grep -q '}body{' "$t10/suite/player.html"; then bad "wireframe body leaks to shell"; else ok "no body leak"; fi
if command -v node >/dev/null 2>&1; then
  python3 -c "import re;s=open('$t10/suite/player.html',encoding='utf-8').read();m=re.search(r'<script>(.*)</script>',s,re.S);open('$t10/p.js','w',encoding='utf-8').write(m.group(1))" && node --check "$t10/p.js" >/dev/null 2>&1 && ok "player JS valid" || bad "player JS invalid"
fi
python3 "$root/items/wireframe-docs/scripts/check-suite.py" "$t10/suite" > "$t10.suite" 2>&1 && ok "suite PASS" || bad "suite FAIL"
grep -q 'SUITE .* 0 FAIL' "$t10.suite" && ok "suite 0 FAIL" || bad "suite has FAIL"
printf '# Flow: Xau\n\n- Entry: nowhere @ sm\n\n## Step 1: A\n- Page: nowhere\n' > "$t10/suite/flows/xau.md"
if python3 "$root/items/wireframe-docs/scripts/check-flow.py" "$t10/suite/flows/xau.md" >/dev/null 2>&1; then bad "bad flow passed"; else ok "bad flow FAIL"; fi
rm -f "$t10/suite/flows/xau.md"
mkdir -p "$t10/nopage"
printf '# Brief: X\n' > "$t10/nopage/brief.md"
if python3 "$root/items/wireframe-docs/scripts/check-suite.py" "$t10/nopage" >/dev/null 2>&1; then bad "empty suite passed"; else ok "empty suite FAIL"; fi
rm -rf "$t10" "$t10.suite"

# 18. wireframe-docs review UX: snippet + Pages tab + scale-fit + chips hidden + click-card (v10.10)
[ -f "$root/items/wireframe-docs/templates/review-snippet.html" ] && ok "snippet exists" || bad "snippet missing"
grep -q 'WF_REVIEW_SNIPPET' "$root/items/wireframe-docs/templates/review-snippet.html" && ok "snippet marker" || bad "snippet marker missing"
grep -q 'WF_REVIEW_SNIPPET' "$root/items/wireframe-docs/examples/tree.html" && ok "example embeds snippet" || bad "example missing snippet"
grep -q 'view-pages' "$root/items/wireframe-docs/templates/player.template.html" && ok "player Pages tab" || bad "Pages tab missing"
grep -q 'btn-pages' "$root/items/wireframe-docs/templates/player.template.html" && ok "player Pages button" || bad "Pages button missing"
grep -q 'wf-review .chip' "$root/items/wireframe-docs/templates/player.template.html" && ok "player hides chips" || bad "player chips visible"
grep -q 'wf-card' "$root/items/wireframe-docs/templates/player.template.html" && ok "player click-card" || bad "player card missing"
grep -q 'fitBox' "$root/items/wireframe-docs/templates/player.template.html" && ok "player scale-fit" || bad "player scale-fit missing"
grep -q 'action-tag' "$root/items/wireframe-docs/templates/player.template.html" && ok "player action tag" || bad "action tag missing"
grep -q 'fitScale\|scale(' "$root/items/wireframe-docs/templates/viewer.html" && ok "viewer scale-fit" || bad "viewer scale-fit missing"
grep -q 'thu %\|% thu\|scale %' "$root/items/wireframe-docs/templates/viewer.html" && ok "viewer scale caption" || bad "viewer caption missing"
if command -v node >/dev/null 2>&1; then
  python3 -c "import re;s=open('$root/items/wireframe-docs/templates/viewer.html',encoding='utf-8').read();m=re.search(r'<script>(.*)</script>',s,re.S);open('/tmp/opencode/v.js','w',encoding='utf-8').write(m.group(1))" && node --check /tmp/opencode/v.js >/dev/null 2>&1 && ok "viewer JS valid" || bad "viewer JS invalid"
  python3 -c "s=open('$root/items/wireframe-docs/templates/review-snippet.html',encoding='utf-8').read();a=s.rfind('<script>');b=s.rfind('</script>');open('/tmp/opencode/s.js','w',encoding='utf-8').write(s[a+8:b])" && node --check /tmp/opencode/s.js >/dev/null 2>&1 && ok "snippet JS valid" || bad "snippet JS invalid"
fi
grep -q 'review-snippet' "$root/items/wireframe-docs/convention/tree-format.md" && ok "convention snippet rule" || bad "convention rule missing"
grep -q 'review-snippet' "$root/items/wireframe-docs/README.md" && ok "item docs snippet" || bad "item docs missing"
grep -q 'bp=" + state.type\|bp=" + k' "$root/items/wireframe-docs/templates/viewer.html" && ok "viewer bp param" || bad "viewer bp missing"
grep -q '\[hidden\]' "$root/items/wireframe-docs/templates/viewer.html" && ok "viewer hidden rule" || bad "viewer hidden missing"
grep -q 'ov-inner' "$root/items/wireframe-docs/templates/viewer.html" && ok "viewer grid wrapper" || bad "grid wrapper missing"
grep -q 'data-wf-breakpoint' "$root/items/wireframe-docs/templates/review-snippet.html" && ok "snippet bp filter" || bad "snippet bp filter missing"
grep -q 'max-width:100%' "$root/items/wireframe-docs/templates/review-snippet.html" && ok "snippet canvas fit" || bad "canvas fit missing"
grep -q 'wf-info' "$root/items/wireframe-docs/templates/review-snippet.html" && ok "snippet badge" || bad "snippet badge missing"
grep -q 'wf-ctrl' "$root/items/wireframe-docs/templates/review-snippet.html" && ok "snippet ctrl mode" || bad "ctrl mode missing"
grep -q 'BP_H' "$root/items/wireframe-docs/templates/player.template.html" && grep -q 'h: 740' "$root/items/wireframe-docs/templates/viewer.html" && ok "viewport heights" || bad "viewport heights missing"
grep -q 'fr-fit' "$root/items/wireframe-docs/templates/viewer.html" && ok "grid gap wrapper" || bad "grid gap missing"
grep -q '| Khổ |.*| Cao viewport |' "$root/items/wireframe-docs/convention/tree-format.md" && ok "convention heights" || bad "heights missing in convention"
grep -q 'ov-info' "$root/items/wireframe-docs/templates/player.template.html" && ok "dialog icon button" || bad "dialog icon missing"
! grep -q 'body.wf-review' "$t10/suite/player.html" && ok "no snippet CSS leak" || bad "snippet CSS leaked"
grep -q '__TITLE_DATA__\|PAGE_TITLES' "$root/items/wireframe-docs/templates/player.template.html" && ok "player page titles" || bad "titles missing"
grep -q 'TITLE_DATA' "$root/items/wireframe-docs/scripts/build-flow.py" && ok "build emits titles" || bad "build titles missing"
grep -q 'Nhập ' "$root/items/wireframe-docs/templates/player.template.html" && ok "player input tag" || bad "input tag missing"
grep -q 'stage-overlay' "$root/items/wireframe-docs/templates/player.template.html" && ok "overlay in-stage" || bad "overlay missing"
if grep -q 'id="overlay"' "$root/items/wireframe-docs/templates/player.template.html"; then bad "fixed overlay remains"; else ok "no fixed overlay"; fi

rm -rf "$t1" "$t2" "$t3" "$t4" "$t5" "$t6" "$t7" "$t1.ver" "$t1.guide"
echo "---"
echo "pass=$pass fail=$fail"
[ "$fail" = "0" ]
