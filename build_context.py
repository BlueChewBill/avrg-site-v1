#!/usr/bin/env python3
"""build_context.py — regenerates the GENERATED halves of context/ packs.

The law: derive the derivable, write only the underivable.
- context/card.md        — rewrites ONLY the block between the GEN markers;
                           the Intent half below the markers is authored by
                           hand and never touched by this script.
- context/card-bench.html — fully generated. The page's entire <style> block
                           is extracted VERBATIM from index.html so the bench
                           renders the real card dress, pixel-true, against
                           real boards from site/data.js. Never hand-edit.

Run after any change to index.html or site/data.js:
    python3 build_context.py
"""

import json
import re
import subprocess
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent
INDEX = (ROOT / "index.html").read_text()
DATA = (ROOT / "site" / "data.js").read_text()
OUT = ROOT / "context"
OUT.mkdir(exist_ok=True)


def git_stamp():
    try:
        h = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                           capture_output=True, text=True).stdout.strip()
        return h or "uncommitted"
    except Exception:
        return "unknown"


# ---------- derive ----------

collections = json.loads(re.search(r"const COLLECTIONS = (\[.*?\n\]);", DATA, re.S).group(1))
counts = {c["id"]: len(c.get("boards", [])) for c in collections}
accents = {c["id"]: c.get("accent", "") for c in collections}

css = re.search(r"<style>\n(.*?)\n</style>", INDEX, re.S).group(1)

scriptsvg = re.search(r"const SCRIPTSVG =\s*(.*?);\n", INDEX, re.S).group(1)
scriptsvg = "".join(part.strip().strip("'\"") for part in scriptsvg.split("+\n"))

dims_src = re.search(r"const DIMS_MM = (\{.*?\});", INDEX, re.S).group(1)
dims_pairs = re.findall(r'"([A-Z]+ \d+)":\s*\[([\d.]+),\s*([\d.]+)', dims_src)
dims = {ref: (w, l) for ref, w, l in dims_pairs}
dims_by_prefix = {}
for ref in dims:
    dims_by_prefix.setdefault(ref.split()[0], 0)
    dims_by_prefix[ref.split()[0]] += 1

canva_count = len(re.findall(r'"[a-z0-9-]+":', re.search(r"const CANVA = (\{.*?\});", INDEX, re.S).group(1))) if re.search(r"const CANVA = \{", INDEX) else 0
canva_files = len(list((ROOT / "site/img/cards/canva").glob("**/*.png")))

ANCHORS = [
    ("JCARDS (framev3 template)", r"const JCARDS = \{", "the ONE CARD markup — every card on the site prints from JCARDS[CARD]; CARD is pinned to \"framev3\""),
    ("jmeta", r"const jmeta|function jmeta", "shapes a data.js board into card meta (acc, ref, dims, cutouts)"),
    ("cardInner / renderColPage", r"function renderColPage", "collection-page grids (.scard slots)"),
    ("bindScards", r"function bindScards", "grid slot wiring: click/keyboard -> openLb"),
    ("renderLisst", r"function renderLisst", "YOUR PICKS page cards"),
    ("the shop conveyor", r"the shop conveyor: the home belts", "home belt cards (recycler owns their visibility)"),
    ("flyToBay", r"function flyToBay", "card -> drawer flight"),
    ("setFlip / flipStage", r"function setFlip", "the flip system (chip = the hidden-face mini)"),
    ("faceSync + FACE", r"function faceSync", "face memory: cards inherit the last-seen side"),
    ("lockCardScale", r"function lockCardScale", "grid render law: 232px then transform-down"),
    ("migrateHole", r"function migrateHole", "lb exchange re-seats the grid hole on every landing"),
    ("DIMS_MM", r"const DIMS_MM", "hand-authored real dims (data.js is generated, so these live in-page)"),
    ("CANVA / INVREF", r"const CANVA", "cutout map + canonical inventory refs (the jref/refOf law)"),
]
anchor_rows = []
for name, pat, why in ANCHORS:
    m = re.search(pat, INDEX)
    line = INDEX[:m.start()].count("\n") + 1 if m else None
    anchor_rows.append((name, line, why))

media = re.findall(r"@media[^{]+", css)
media_census = {}
for q in media:
    key = re.sub(r"\s+", " ", q.replace("@media", "").strip())
    media_census[key] = media_census.get(key, 0) + 1
media_census = dict(sorted(media_census.items(), key=lambda kv: -kv[1]))

d7f_rules = css.count(".d7f")
cqw_count = css.count("cqw")

stamp = f"{date.today().isoformat()} · commit {git_stamp()} · index.html {INDEX.count(chr(10)) + 1} lines"

# ---------- context/card.md (generated block only) ----------

gen_lines = [
    "<!-- GEN:BEGIN — written by build_context.py, do not hand-edit this block -->",
    f"*Derived {stamp}*",
    "",
    "**The card in numbers**",
    f"- Boards it draws: " + " · ".join(f"{k} {v}" for k, v in counts.items()) + f" — {sum(counts.values())} total",
    f"- Accents (per collection, ride in as `--acc`): " + " · ".join(f"{k} `{v}`" for k, v in accents.items()),
    f"- Real dims in `DIMS_MM`: {len(dims)} boards (" + ", ".join(f"{k} {v}" for k, v in sorted(dims_by_prefix.items())) + ") — the rest fall back to `PH_DIMS`/blank",
    f"- Cutout art shipped: {canva_files} files under `site/img/cards/canva/` · `CANVA` map entries: {canva_count}",
    f"- Dress spec: {d7f_rules} `.d7f` selector references in the page CSS · {cqw_count} `cqw` declarations (the ONE CARD SPEC container math)",
    "",
    "**Where it's drawn — anchor names, not line numbers** (line cited = at derivation; ANCHOR-SEARCH the name, the line is just a hint)",
]
for name, line, why in anchor_rows:
    loc = f"index.html:{line}" if line else "NOT FOUND — re-derive"
    gen_lines.append(f"- `{name}` ({loc}) — {why}")
gen_lines += [
    "",
    "**Environments** (each is a producer above): collection grids · home belts · the lightbox card · drawer/bay shelves · flights · YOUR PICKS · the blank card (`.scard.indeck` costume) · phone chip costume (dock-gated)",
    "",
    "**Breakpoint census** (distinct `@media` conditions in the page, by rule count):",
]
for k, v in media_census.items():
    gen_lines.append(f"- `{k}` ×{v}")
gen_lines += [
    "",
    "**Data sources**: `site/data.js` (GENERATED — never hand-edit; rerun `build_site.py`) · in-page hand tables: `DIMS_MM`, `CANVA`, `PH_DIMS`, demo maps",
    "<!-- GEN:END -->",
]
gen_block = "\n".join(gen_lines)

card_md = OUT / "card.md"
if card_md.exists():
    src = card_md.read_text()
    new = re.sub(r"<!-- GEN:BEGIN.*?<!-- GEN:END -->", gen_block, src, flags=re.S)
    card_md.write_text(new)
else:
    card_md.write_text(f"""# Card — context pack

> The scoped-landing briefing for the card. Facts below are DERIVED (regenerate
> with `python3 build_context.py`); everything under **Intent** is AUTHORED —
> the why the code can't say. Deep react history lives in
> [.claude/docs/cards.md](../.claude/docs/cards.md) — this file is the landing,
> that file is the archaeology.

## Facts

{gen_block}

## Intent (authored — edit freely, the generator never touches this)

*(to be written)*

## Success criteria for changes here

*(to be written)*
""")

# ---------- context/card-bench.html ----------

samples = []
hs = [b for c in collections if c["id"] == "hand-shaped" for b in c["boards"]]
cl = [b for c in collections if c["id"] == "classic" for b in c["boards"]]
og = [b for c in collections if c["id"] == "originals" for b in c["boards"]]


def dims_str(ref):
    r = dims.get(ref.replace("HS ", "HS ").replace("CL ", "CL "))
    return f"{r[0]} × {r[1]} MM" if r else ""


def card_html(b, acc, extra_cls="", st="avail", st_txt="AVAILABLE"):
    ref = b.get("ref", "")
    name = (b.get("name") or ref).upper()
    d = dims_str(ref)
    sold = " sold" if st == "gone" else ""
    return (
        f'<div class="d7f{sold}{extra_cls}" style="--acc:{acc}"><div class="panel">'
        '<div class="inframe"><i class="ctl"></i><i class="cbr"></i><i class="dgl"></i><i class="dgr"></i></div>'
        f'<div class="corner"><span class="fchip fc-ref"><span class="ft" data-ref="{ref}">{ref}</span></span></div>'
        f'<div class="stage"><img loading="lazy" src="site/{b["thumb"]}" alt="{name}"></div>'
        '<div class="info">'
        f'<span class="nm"><span class="nmt" data-nm="{name}" data-dims="{d}">{name}</span></span>'
        "</div>"
        + ("" if st == "gone" else
           f'<button class="fchip fc-list d7f-cta" data-id="{b["id"]}"><span class="fl"><span class="ft"></span>{scriptsvg}'
           '<span class="fmini" aria-hidden="true"></span></span></button>')
        + f'<span class="fst {st}"><span class="dot"></span><span class="sttxt">{st_txt}</span></span>'
        "</div></div>"
    )


bench_css = """
  body { background: #101314; padding: 30px 34px 80px; }
  .cbx-h { font: 800 22px/1.2 "Satoshi", system-ui, sans-serif; color: #f2efe8; letter-spacing: .04em; margin: 0 0 4px; }
  .cbx-sub { font: 400 13px/1.5 system-ui, sans-serif; color: #8b948f; max-width: 72ch; margin: 0 0 26px; }
  .cbx-sub code { color: #c8d2cc; }
  .cbx-sec { font: 700 11px/1 system-ui, sans-serif; letter-spacing: .14em; color: #6f7a74; text-transform: uppercase; margin: 34px 0 14px; }
  .cbx-row { display: flex; gap: 26px; align-items: flex-start; flex-wrap: wrap; }
  .cbx-slot { flex: none; }
  .cbx-cap { font: 500 11px/1.4 system-ui, sans-serif; color: #8b948f; margin-top: 10px; max-width: 232px; }
  .cbx-cap b { color: #d8dfda; }
"""

sample_rows = []
b0 = cl[2] if len(cl) > 2 else cl[0]
sample_rows.append(('The spec scales — same card, three widths (ONE CARD SPEC: every internal dimension is cqw)', [
    (180, card_html(b0, accents["classic"]), "180px"),
    (232, card_html(b0, accents["classic"]), "232px — the reference width"),
    (300, card_html(b0, accents["classic"]), "300px"),
]))
sample_rows.append(('States & collections (hover a card — the dress is the real CSS)', [
    (232, card_html(hs[0], accents["hand-shaped"]), f'<b>{hs[0]["ref"]}</b> · hand-shaped accent · real dims decode on the live page'),
    (232, card_html(og[0], accents["originals"]), f'<b>{og[0].get("ref", "OG")}</b> · originals accent'),
    (232, card_html(cl[0], accents["classic"], st="gone", st_txt="SOLD"), f'<b>{cl[0]["ref"]}</b> · sold dress (chip retired on gone cards)'),
    (232, '<div class="scard indeck" style="width:232px">' + card_html(hs[1], accents["hand-shaped"]) + "</div>",
     "the BLANK CARD — this board is in the deck; the slot keeps the panel and wears the mark"),
]))

rows_html = []
for title, slots in sample_rows:
    cells = "".join(
        f'<div class="cbx-slot" style="width:{w}px">{html}<div class="cbx-cap">{cap}</div></div>'
        for w, html, cap in slots)
    rows_html.append(f'<div class="cbx-sec">{title}</div><div class="cbx-row">{cells}</div>')

bench = f"""<!doctype html>
<!-- GENERATED by build_context.py — {stamp}. Do not hand-edit; rerun the script. -->
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>card — bench</title>
<base href="../">
<style>
{css}
</style>
<style>
{bench_css}
</style>
</head><body>
<h1 class="cbx-h">CARD — BENCH</h1>
<p class="cbx-sub">The real card dress (the page's entire CSS, extracted verbatim at generation) on real boards from <code>site/data.js</code>. Meta is simplified: refs are data.js fallbacks (the live page derives canonical <code>INVREF</code> refs), no flip chips (needs the <code>CANVA</code> map), and decode/ceremony JS is absent — this bench shows the <b>dress</b>, the live page owns the <b>behavior</b>. Serve from the repo root (:8124), never file://.</p>
{"".join(rows_html)}
</body></html>
"""
(OUT / "card-bench.html").write_text(bench)

print(f"context/card.md — facts block regenerated ({stamp})")
print(f"context/card-bench.html — {len(css.splitlines())} CSS lines extracted, {sum(len(s) for _, s in sample_rows)} sample cards")
