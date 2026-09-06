# Handoff — AVRG site v1 — 2026-09-05 (the audit walk + the chip bake)

## Where we are

Everything on v1 is pushed and live at avrg.cards (main = origin = the served page, byte-identical at wrap). The day was an audit walk Dylan asked for while he calipered boards, and it closed a lot: the OG 07 DRAFT line off the live lb, the empty RESALE section out of shop-all, accessibility 89 → 96, THE CUTOUTS GO WEBP (card art 54 → 15 MB on disk, the desktop home boot 19 → ~5 MB), tail · nose on the dims line's second row, the desktop minis strip back up top (a regression from the counter's retirement), and the add chip's round 7 — corner mark tucked under the chip, then his pick off two collides, **B + tight, baked and pushed**: the chip is the ref pill's 26px box at every width, word 11px, the card glyph redrawn to the bar mini's recipe. Records are in the owning docs (log.md's 2026-09-05 entry lists them all). Tree is clean except this wrap's docs commit.

**In flight at wrap:** a `bench-cartographer` agent was charting the NEW `chip-word-size` dial in CompUI (`.d7f .fc-list { font-size }` + the `.ft` line-height coupling; ticket text is in this session's transcript, the spec is in cards.md's THE BAKE entry). It commits in CompUI on its own; CompUI is NOT pushed (Dylan's call — two local commits ahead: the two chip rows re-baked at 0bfc82d, plus the cartographer's when it lands). If the next session finds CompUI's `pilot/manifest/avrg.json` without a `chip-word-size` row, the agent didn't finish: re-issue the ticket (the bench-charting skill has the shape; the numbers are 4.7414cqw shipped, range 3.5–6, coupling to the 13px `.ft` line, consumer lb-chips).

## Next task

No task was named at wrap. Dylan is mid-dims: **the dims backlog** is the live thread — 42 of 71 boards with no `DIMS_MM` line (all 7 OG, HS 25–46, CL 55–63 + the four solds) and 18 with width+length only (list by ref in open-threads.md's THE AUDIT WALK). His type-in lands in `DIMS_MM` in `index.html` (keyed by padded ref, `[w, l]` or `[w, l, tail, nose]` in mm) — then `build_context.py`, parse check, commit. Done = the refs he dictates print in the lb dims line (row 1 width × length, row 2 tail · nose).

If he opens on something else, the candidates in his weight order are in open-threads.md's audit addendum: the originals copy (OG 02–06 empty; type into `sources/originals/NN-slug/*.txt`, rebuild), the two home contrast greys (taste), the leftover URL switches, the share tags, the logo media dropdown (never started).

## Read these, skip the rest

- `.claude/docs/open-threads.md` — THE AUDIT WALK section + its addendum: the open list, in his order, with the dims refs.
- `.claude/docs/cards.md` — THE ADD CHIP COLLIDE IS UP → round 7b → THE BAKE: the chip's current numbers and why (26 box, 11px word, 22px glyph on a 13 seat, the tight recipe). Read before touching the chip or `STACKSVG`.
- `.claude/docs/lightbox.md` — the three 2026-09-05 entries at the foot: the DRAFT filter, the dims second row, THE MINIS COME BACK UP TOP (the `D` flag in `deckGeom` — don't "simplify" it back to `H`).
- `.claude/docs/gotchas.md` — the two new ones at the foot: a retired element's offsetHeight is 0; the app's Browser pane blanks on the lightbox (real Chrome for lb geometry, screenshots into `.shots/`).
- `.claude/skills/board-batch/SKILL.md` step 4 — cutouts are `.webp` now; a PNG dropped in `site/img/cards/` is invisible to the page.

Everything else is NOT needed until a task leads there. Re-run `build_context.py` after any `index.html` change; parse-check before any browser look.

## Context that isn't in the code

- **His reads today, verbatim where it matters:** "the two lines are fine. in fact. we should move tail and nose measurements to sit on the second row universally" · "remove the restock foot note" (read as the whole empty section — a heading with nothing under it read worse; the fork is in home-shop.md, one-line flip back) · "pixels are off on the inner edge of the card. add reads small. chip is too tall. im open to suggestions beyond the design it is now" · "see if we can get the card in the chip to read more like a blank mini. with its hair line inner frame and space around the dot. understandable if its to tight" · "b and tight. bake it and push".
- **The chip's box law now:** 26 = padding 13 + a 13px line; BOTH the word (line-height 13) and the glyph (22 drawn, −4.5/−4.5 margins) bleed inside that line. Changing either seat number breaks the ref-pill parity he just picked.
- **The WebP batch is done, and future batches must encode** — the board-batch skill's step 4 says so; `CUT`/`BOT` and `build_context.py` spell `.webp`, the `CANVA` map values never carry an extension.
- **Push cadence today:** he said "push" three times (both repos with CompUI's CLAUDE.md; "bake it and push"). That grant ended with the session — pushes are his call again. CompUI is never pushed by a session.
- **Verification tooling this session:** the desktop app's Browser pane worked for the shop and phone emulation but painted white on the lightbox; the chrome-devtools MCP's real Chrome did all lb measurement (kill it at the end — done at wrap). Synthetic click chains (`pointerdown → click` dispatched at the card centre) open the lb reliably; `:hover` still needs real input.
- **Two one-liners on his word** (not done, noted in open-threads): the phone's dockDress writes plain `ADD` vs desktop's `ADD +`; the strip sits ~29px higher than the 08-19 layout now that the counter's air is gone — unjudged by him.
- **The a11y items left on the home** (video note `#a1a1a1`, band subtitles `#939393`) are design greys — taste, likely charted; I left them alone on purpose.

## Parked / later

- The originals' remaining asset ends (six og sheets, three Vision-cut cards, the stand-in clip, og phone lb) — unchanged, open-threads.
- The identity migration before the 48-board batch — unchanged.
- The `?sun=`/`?grow=`/`?hud=` collide plumbing stays by his ruling; `?msgfx=` and `?rowmax=`/`?rowgap=` are unbaked 08-05 knobs, retire on his word.
- The maker's mark in the lb and its touch surfacing; the share tags (`twitter:site` needs his X handle).
