---
name: board-batch
description: Intake recipe for a new batch of board photos into the AVRG site — pairing bg-removed shots, classifying, naming so sources/ sorts LAST, cutouts, CANVA rows, build_site.py + build_context.py, the append-only data.js check, the straightening pass. Load when Dylan drops new board photos, a batch of boards, a bg-removed batch, wants boards added to sources/, or asks for cutouts / CANVA rows.
---

# Board-batch intake — the twice-proven recipe

Proven on batch 2 (2026-08-30, 9 classics) and batch 3 (2026-08-31, 22
hand-shaped), both run by dispatched Opus implementers. Ruling history
(lilac board, HS 47) lives in `.claude/docs/cards.md`; the ordering law in
`.claude/docs/gotchas.md` ("`sources/` ordering IS board identity").

## Before you start

- **Ids are positional.** `build_site.py` numbers each collection folder in
  sort order; `CANVA`, `INVREF`, `DIMS_MM` and every hand-kept map in
  `index.html` are keyed to those ids. Nothing may land mid-order.
- The **identity migration** (filename-derived ids — open-threads.md's Misc
  queue) is chartered to land BEFORE the next big batch. Check whether it
  has; if not, the ordering law below carries the batch.
- Additions arrive in any size — he shoots in increments; a small drop is a
  valid batch.

## The steps, in order

1. **Pair the bg-removed shots by shot order** — one top + one bottom per
   board. Expect decoys: duplicate exposures, pile shots, accidental
   top-face pairs. Drop them; list what was dropped in the report.
2. **Classify** each pair into its collection (`classic` / `hand-shaped`;
   `originals` needs a description `.txt` per board folder — `require_desc`).
3. **Name so `sources/` sorts LAST.** Continue the existing naming in the
   collection folder so the new files sort after everything present. A
   loose image = a single-photo board; a subfolder = one board, many angles.
4. **Crop the cutouts straight from the alpha PNGs** — no re-masking. They
   land in `site/img/cards/cuts/` (originals) or as the CANVA pair in
   `site/img/cards/canva/` (one top + one bottom per board; the canva
   folder ships only what the live `CANVA` map points at).
5. **Add the CANVA rows** in `index.html` (+ an `INVREF` row; a `DIMS_MM`
   line once the board is measured — never guess dims).
6. `python3 build_site.py` — regenerates `site/img/{thumb,full}` +
   `site/data.js`.
7. **Assert the `site/data.js` diff is append-only.** Any changed EXISTING
   id means the sort order moved — stop, fix the naming, rebuild. This is
   the acceptance test for the whole batch.
8. `python3 build_context.py` — regenerates the derived halves of `context/`.
9. **Straightening pass:** rotate every new board onto its own silhouette
   axis (0–3.5° in practice), then rebuild both derived files again.
   **Residual lean after that is PERSPECTIVE keystone, not rotation —
   don't over-rotate; reshoot or warp** (gotchas.md).
10. Verify on `:8124` with an origin switch (`127.0.0.1:8124`) — the pane's
    `?v=` bust does not refresh `data.js` (gotchas.md). Count the rendered
    boards against the repo.
11. Commit (the diff should read: sources added, cuts/canva added, CANVA +
    INVREF rows, data.js appended, context regenerated). **Pushing is
    Dylan's call.**

## Id-range conventions (as of batch 3)

- Classics: `classic-NN` ids run in file order; inventory refs are
  non-contiguous (`classic-01` is CL 3), so the ref never sanity-checks the
  ordinal. Batch 2 landed CL 55–63 as classic-20…28.
- Hand-shaped: batch 3 landed HS 25–46 as hand-shaped-15…36
  (PS56–99 / hs25–46 in the shot naming).
- Refs come from the `INVREF` map; `jref`/`refOf` are the ONLY ref
  producers — never add a third.

## After the batch

- A new board's card art is never already here (the canva batch in v1 is a
  subset) — if a card renders blank, check the file exists before
  debugging the map.
- If the batch touched a charted bench param (sold dress, spark tiers,
  card seats), the bench must know — `bench-charting` skill.
