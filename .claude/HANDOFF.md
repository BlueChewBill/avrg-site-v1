# Handoff — AVRG site v1 — 2026-08-23 (the zone's first board is live)

> Previous handoffs live in this file's git history.

## Where we are

**THE ZONE IS LIVE ON ITS FIRST BOARD.** avrg.cards serves everything
through commit `94f92bf`; one local commit (`f4b1c7d`, the ghost-column
fix) is unpushed and rides the next push. The night's landings, all
recorded in their surface docs:

- **OG 05 (Short Steep) went through the whole og loop**: Dylan composed
  the sheet on the kit's "07 · OG Sections" page → Claude pulled it by
  MCP at the canvas's own 2× (960×1280) → `site/img/og/og-05-section.png`
  → one `OG_SHEETS` line → the og LB renders it right of the card.
  Sheetless boards keep the old spread column. His og bench bake landed
  the same night (clip 300 wide, columns +80 down, strip costume).
- **The phone add-flight is fixed and baked** (variant A = `PICK_TUNE`,
  rides z 6650 OVER the bar, lands on the new mini's seat, touchdown is
  the reveal). The `?pickfly` collide is retired.
- **The half-drawn logo is fixed** (Blink SMIL freeze; drawRestore heals
  with a rewind+jump seek).
- **Bench fully synced**: pick-flight wing + zone dials charted, bake
  values synced — CompUI `5d342ef` + `4dfd245`, census 144.

**Dylan's parting note: "the figma page has most of the material there
now... thats half the battle"** — the remaining six sheets are mostly
COMPOSED on the kit page, awaiting finish + export.

## Next task

**Run the og loop on the next finished sheets.** For each canvas Dylan
says is ready (or links): export via Figma MCP (file
`2QS87sR9PBcckdYhFrPsIJ`, the "07 · OG Sections" page — pull the node at
scale 1, canvases are already 960×1280) → save as
`site/img/og/og-NN-section.png` (NN = the board's og ref number) → add
one `OG_SHEETS` line in index.html (beside DIMS_MM) → verify on :8124
(og LB shows the sheet; exchange to a sheetless board still shows the
spread) → commit. Done = every composed board renders its sheet.
No bench work needed per sheet (the zone dials are charted; only value
retunes would touch the manifest).

## Read these, skip the rest

- `.claude/docs/lightbox.md` — THE ZONE LANDS entry (the seat's whole
  anatomy: OG_SHEETS, #og-zone, the dials, the ghost-column fix, the
  no-fold-clamp reasoning) + the bake record above it.
- `index.html` anchor-search: `OG_SHEETS` (the manifest), `og-zone`
  (seat + CSS), `THE OG SPREAD` (the og rule the dials live on).
- `.claude/docs/mobile.md` tail — only if touching the phone add flight.
- CLAUDE.md "Where things stand" — the 2026-08-22/23 night entry.

Everything else is NOT needed. The og LB is desktop-only; og mobile is
parked.

## Context that isn't in the code

- **The export recipe that works:** Dylan pastes a Figma canvas link →
  `get_screenshot` first to identify the board (cheap), then
  `download_assets` with png/scale 1 → curl the export URL. His canvases
  are already 2× size, so scale 1 = the spec'd 960×1280. He does NOT
  need to touch Figma's export panel — this loop replaced it.
- **Board↔file naming:** NN = the og ref number = the sources/originals
  folder prefix (01 og-orange-piro · 02 peach-piro · 03 purple-purple ·
  04 rainbow · 05 shortsteep-DGFB · 06 yellow-blue · 07 bluepiro).
  OG 05 was identified by its sheet's "DGFB x FB Connoisseur" caption —
  confirm the board with Dylan when a sheet's identity isn't obvious.
- **Zone laws:** no fold-fit clamp on purpose (the ruling defines the
  box at 1440×900; small-window tails are the spread's own behavior and
  a react, not a pre-invented law). ~5px of sheet margin clips at a
  960-wide window — known, invisible, accepted. --ogColTop moves the
  zone too (his bake set it 80).
- **The left "short text" seat is NOT built** — the ruling puts short
  per-board text under the clip, but his copy doesn't exist yet. The
  clip caption stands alone. Build it when the words arrive, not before.
- **Blink SMIL law (k-core has the full record):** a timing-attribute
  rewrite re-freezes a frozen animate at oldActive/newDur progress, and
  only a REAL rewind seek recomputes — nudge seeks (±1ms..±500ms, any
  deferral) are all no-ops. If SMIL clocks ever get rewritten anywhere
  again, heal with setCurrentTime(0) then setCurrentTime(past-end).
- **His energy/read:** the composing is the effortful half for him;
  export+wire is "half the battle" already won. Keep the loop
  frictionless — he links, Claude lands it.

## Parked / later

- The unpushed `f4b1c7d` — push with the next batch (Dylan calls pushes).
- Per-board clips (the one stand-in cut still serves every og board;
  the seat + gate exist, `#og-clipseat`).
- The left short-text seat (waits on his per-board copy).
- og mobile view (after the desktop set completes).
- The Safari sweep (the 2026-08-22 handoff's plan still stands — board
  grow/cursor-chase symptoms + the -webkit selection fixes; grew MORE
  relevant now that flights ride over the bar).
- The dark base CSS proven-identical sweep, calipers/DIMS_MM session
  (originals still unmeasured), thread 2 (plates), thread 3 desktop
  half, relay (his word only), sound design half, iPad (lowest).
