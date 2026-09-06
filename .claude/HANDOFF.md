# Handoff — AVRG site v1 — 2026-09-06 (the og sheets go live)

## Where we are

The originals' lightbox right column is a LIVE TEMPLATE now, shipped and pushed (main `2ef7d32` + this wrap's docs commit; avrg.cards serves it). The day in one line: Dylan asked to see his og sheet sketches in the Figma kit and get a layout of Claude's own → the OG 06 collide (his photos, a structured layout) → his ruling **"go with option 2, template it for the rest"** → `OG_TPL`, a hand-authored manifest beside `OG_SHEETS` in `index.html`, renders four photo seats + three spec strings + a length arrow per board inside the same 480×640 zone; OG 05 keeps its baked C sheet (baked outranks live). Then the bench wing (`og-template`, CompUI `ff2811b`) and its finds landed on his "make the changes": the template owns `--ogtMargin` / `--ogtGuide` / `--ogtArrow` / `--ogtArrowW`, labels track `.22em`. A re-chart ticket went to the cartographer at wrap (unlock two rows, re-anchor the calc() seats, arrow rows onto the vars, a padlock row for the arrow's JS seat) — its result + the CompUI push are recorded below the wrap note if it landed before close.

**Landed after the wrap note:** the re-chart finished — **CompUI `cdc7fe8`, PUSHED on Dylan's "push when the cartographer lands."** Census 191 → 192 (139 live · 53 locked · 0 changed). `ogt-margin` and `ogt-guide-ink` are LIVE (driving `--ogtMargin` 0–80 canvas px and `--ogtGuide`); `ogt-guide-inset` is retired-as-locked (the site linked the guide's inset to the margin — one source, one driver; re-splitting it is a manifest split he orders, site-side `--ogtGuideInset`); `ogt-arrow-seat` is a new locked row (the JS default; the honest dial is `OG_TPL`'s per-board `arrow` column — a slider on the default would drive five boards and leave OG 07's own seat behind). Forced re-unit: `ogt-strip-seat` reads canvas px now (103 = the old 8.05%, exactly) because the composing calc can't be written in %. Verified in real Chrome: shipped seats byte-exact, margin 0/40/80 moves every seat with the right edge pinned at 960 − margin and the profile foot 21 inside the guide, split + margin compose instead of racing, ink ⇄ dash both orders, arrow weight/ink move shaft + head + label together, OG 05 untouched under seven live overrides, reset clean. No site-side finds carried out. Both repos level with origin at close.

## Next task

**Dylan's spec fills.** Every dash on a live sheet is an empty string in `OG_TPL` (`index.html`, right after `OG_SHEETS`): OG 01 `dims` / `trucks` / `wheels` / `len`, OG 02 `dims` / `len`, OG 06 `trucks`. He dictates, they land as plain strings (dims in the `31.5mm × 89.75mm` shape — `dimsRich` renders the small mm; `len` is the arrow label, e.g. `89.75 mm`, empty = no arrow). Then `build_context.py`, parse check, commit. Done = no dash on any templated original at 1920.

If he opens elsewhere: the dims backlog is still live (42 boards without `DIMS_MM`, list in open-threads' THE AUDIT WALK); an OG 01 close-up shoot would retire the two soft sips crops (`site/img/og/og-01-a.jpg`, `-b.jpg` — swap the paths in the row); the OG 03 hero could be his deck close-up (`69:698` in the kit) instead of the site's angled top.

## Read these, skip the rest

- `.claude/docs/lightbox.md` — THE OG 06 COLLIDE + THE OG TEMPLATE (the two entries at the foot): the manifest shape, the seat geometry in canvas px, the vars, the bench record, what's open. Read before touching `#og-tpl`, `OG_TPL` or `ogTplWrite`.
- `index.html` — anchor-search `const OG_TPL` (the rows + the writer), `#og-tpl {` (the CSS block, ~60 lines), `id="og-tpl"` (the markup). Nothing else in the file is needed for the fills.
- `.claude/docs/figma-kit.md` — the 2026-09-06 section at the foot: where the sheets live on the 07 page, the read trap (reads of `204:77` / `61:10` die in SSE truncation — screenshot instead), the tile-export recipe.
- `.claude/docs/gotchas.md` — the foot entry: chrome-devtools MCP Chrome at 150% zoom (`emulate 2880x1620x1` → CSS 1920; confirm `innerWidth`), and the pane freezes the lb flight (real Chrome for anything inside `#lb`).
- `.claude/docs/open-threads.md` — the og entry's 2026-09-06 addendum (what superseded what, the open list).

Everything else is NOT needed until a task leads there. Re-run `build_context.py` after any `index.html` change; parse-check before any browser look.

## Context that isn't in the code

- **His words, verbatim:** "go with option 2, template it for the rest. some of the boards have different photos / not stock angles. so feel free to use whichever ones as long as the profile, trucks, and wheels make it in" · "push it" · "make the changes. and land them" · "lets wrap and push when the cartographer land[s]".
- **The ZONE ruling's "no template law" is superseded, not deleted:** per-board freedom survives as the baked override (a ref in `OG_SHEETS` never reaches `OG_TPL`). OG 05 is the only baked board. Nobody asked whether OG 05 should join the template — leave it unless he says.
- **Specs are his words from the kit's sheets; nothing was guessed.** The OG 02 dims in the old callout cluster ("33.5 × 97.5") were NOT used — that string is `PH_DIMS`' demo. The kit's OG 01 canvas holds Bluepiro (OG 07), flagged in lightbox.md; the site's OG 01 is the orange Piro.
- **Photo quality tiers:** his Figma crops (03/04/06/07) and the OG 02 launch-week close-ups are sharp; OG 01's two sips crops from 1500px marble shots are soft stand-ins. The hero seat takes `object-fit: cover` + per-row `hpos`; OG 07's hero is the top cutout with `hfit: "contain"`.
- **The strip is equal thirds on purpose** — the collide's 416/188/228 split starved the trucks column (three lines into the profile). The seat (58.75% → margin+815) holds two value lines at 2.3cqw; don't grow the value size without moving the profile.
- **Bench state at wrap:** `og-template` wing landed (`ff2811b`, 17 rows, two locked). The vars refactor changed anchor declarations → the re-chart ticket is with the cartographer; until it lands the bench's geometry rows template the OLD literal declarations (they'll still override, but the margin/guide rows stay locked). CompUI push: Dylan said "push when the cartographer lands" — that grant covers this wrap only.
- **Verification rig today:** the cloud Figma MCP for reads/writes/exports (chunk page reads; certain nodes truncate regardless); real Chrome via chrome-devtools for every lb screenshot (`.shots/ogt-*.jpeg`, gitignored); the pane only for the shop.
- **Figma side:** Claude's frame `SECTION · OG 06 · yellow-blue · CLAUDE'S LAYOUT` (`228:65`, at (5300, 2400) under his OG 06) stays as the template's drawing; the export staging frame was deleted; his canvases untouched.

## Parked / later

- Per-board clips (the one stand-in cut still serves all seven originals), og mobile (the template obeys the desktop gate), OG 05 joining the template — all his call.
- The identity migration before the 48-board batch; the dims backlog; the originals' description copy (the `.txt` seats).
- The `?sun=`/`?grow=`/`?hud=` collide plumbing stays by his ruling; `?msgfx=`, `?rowmax=`/`?rowgap=` are unbaked 08-05 knobs.
- The maker's mark in the lb; the share tags (`twitter:site` needs his X handle); the logo media dropdown.
