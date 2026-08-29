# Card — context pack

> The scoped-landing briefing for the card. Facts below are DERIVED (regenerate
> with `python3 build_context.py`); everything under **Intent** is AUTHORED —
> the why the code can't say. Deep react history lives in
> [.claude/docs/cards.md](../.claude/docs/cards.md) — this file is the landing,
> that file is the archaeology.

## Facts

<!-- GEN:BEGIN — written by build_context.py, do not hand-edit this block -->
*Derived 2026-08-29 · commit 166d6ee · index.html 17152 lines*

**The card in numbers**
- Boards it draws: originals 7 · hand-shaped 14 · classic 19 · resale 0 — 40 total
- Accents (per collection, ride in as `--acc`): originals `#e84a27` · hand-shaped `#4a9eff` · classic `#f5c842` · resale `#8b5cf6`
- Real dims in `DIMS_MM`: 26 boards (CL 12, HS 14) — the rest fall back to `PH_DIMS`/blank
- Cutout art shipped: 74 files under `site/img/cards/canva/` · `CANVA` map entries: 37
- Dress spec: 125 `.d7f` selector references in the page CSS · 152 `cqw` declarations (the ONE CARD SPEC container math)

**Where it's drawn — anchor names, not line numbers** (line cited = at derivation; ANCHOR-SEARCH the name, the line is just a hint)
- `JCARDS (framev3 template)` (index.html:7144) — the ONE CARD markup — every card on the site prints from JCARDS[CARD]; CARD is pinned to "framev3"
- `jmeta` (index.html:7026) — shapes a data.js board into card meta (acc, ref, dims, cutouts)
- `cardInner / renderColPage` (index.html:7978) — collection-page grids (.scard slots)
- `bindScards` (index.html:7962) — grid slot wiring: click/keyboard -> openLb
- `renderLisst` (index.html:8302) — YOUR PICKS page cards (one producer for both dresses: YOUR PICKS on the dock side, My Lisst on desktop)
- `renderBay` (index.html:13117) — draws the drawer/bay shelf cards — the shelf's producer (flyToBay is only the flight)
- `the shop conveyor` (index.html:12399) — home belt cards (recycler owns their visibility)
- `flyToBay` (index.html:15739) — card -> drawer flight
- `setFlip / flipStage` (index.html:16309) — the flip system (chip = the hidden-face mini)
- `faceSync + FACE` (index.html:7114) — face memory: cards inherit the last-seen side
- `lockCardScale` (index.html:7945) — grid render law: 232px then transform-down
- `migrateHole` (index.html:11208) — lb exchange re-seats the grid hole on every landing
- `cardDressOn / cardDressOff` (index.html:6744) — the hover decode pair: name<->dims, ref<->AVRG, status in/out — display is a TEXT WRITE, never CSS
- `stayLand / dockDress` (index.html:6720) — the static text lands (no hover to earn a decode) — note: stayLand resolves dims||name, so THE LB CARD ALREADY RESTS ON DIMS on desktop
- `DRESS_TEXTS` (index.html:6664) — the four text slots the dress systems own (.fc-ref .ft, .nmt, .sttxt, .fc-list .ft)
- `DIMS_MM` (index.html:6972) — hand-authored real dims (data.js is generated, so these live in-page)
- `CANVA / INVREF` (index.html:6860) — cutout map + canonical inventory refs (the jref/refOf law)

**Environments** (each is a producer above): collection grids · home belts · the lightbox card · drawer/bay shelves · flights · YOUR PICKS · the blank card (`.scard.indeck` costume) — the add chip's phone-only costume went universal 2026-08-29, so there is no dock-gated card dress left

**Breakpoint census** (distinct `@media` conditions in the page, by rule count):
- `(hover: hover)` ×26
- `(max-width: 940px)` ×14
- `(min-width: 941px)` ×11
- `(prefers-reduced-motion: reduce)` ×8
- `(max-width: 720px)` ×4
- `(min-width: 721px)` ×2
- `(max-width: 1260px) and (min-width: 941px)` ×2
- `(hover: none), (max-width: 720px)` ×1
- `(min-width: 941px) and (hover: hover)` ×1
- `(hover: hover) and (min-width: 941px)` ×1

**Data sources**: `site/data.js` (GENERATED — never hand-edit; rerun `build_site.py`) · in-page hand tables: `DIMS_MM`, `CANVA`, `PH_DIMS`, demo maps
<!-- GEN:END -->

## Intent (authored — edit freely, the generator never touches this)

**Purpose.** The card IS the shelf. Every other surface — home belts, drop, picks, lightbox — exists to route people to cards or to inspect what a card holds. It must read as a physical object: paper panel, rounded, shadow as a depth cue, never UI chrome.

**The laws a change here must not break** (each earned the hard way — receipts in [.claude/docs/cards.md](../.claude/docs/cards.md)):

- **ONE CARD SPEC** — `.d7f` is a CSS container; every internal dimension is cqw at the 232px reference (a px fallback line precedes each cqw line for pre-2022 Safari). Grids render at 232 then transform down (`lockCardScale`). Never add a px-only internal dimension; never hand-scale a card per surface — the spec scales it.
- **The four-state mirror** — any chip-state addition must touch all four systems: `:hover`, `.tset`, `.hold`, `.bay-fly.held`. Miss one and the chip blinks mid-flight.
- **One ref law** — never add a ref producer; call `jref`/`refOf`. (Three producers was two too many.)
- **Shadow laws** — never hand-draw a filter shadow on a transform-scaled element (the pinch scales board + shadow as one silhouette); the shadow-over-text rule lives on stage imgs; the card's hover shadow is the spec'd one, not a per-surface improvisation.
- **The blank card is a costume on grids, a true hole on belts** — grids: `.scard.indeck` hides via `visibility` (never `display` — `lockCardScale` still measures it). Belts: true holes, because the recycler stomps inline visibility per frame and would fight a costume.
- **Face memory has one reader** — the `FACE` set is written by three gestures but read in ONE place (the template). New render paths inherit it for free; do not add a second reader.
- **The card decode is width × length only** — tail/nose is lightbox-only ("too much noise on a card decode"). Phones don't decode want-words. Status text is written by JS — the text IS the state.
- **The lazy law works FOR us** — hidden imgs are 0×0 boxes that never load. Costumes must preserve it.
- **Rest == rest, no touchdown pop** — a flight drains its texts mid-air toward its DESTINATION's rest state (`buildFly`'s drain). Any change to what a surface rests on must ride the drain too, or cards pop at landing.
- **PH_DIMS is a placeholder table** — `jmeta.dimsPh` merges `DIMS_MM` (real) with `PH_DIMS` (demo values). Anything that makes dims MORE prominent makes the placeholders more prominent too; know which table a string came from.

**Taste.** No borders on the card face. No new chrome without a react round. Changes to how the card *looks* are collided as variants for Dylan to react to — never spec'd straight to done.

## Success criteria for a scoped change here

1. **Syntax-check the inline script first** (one stray comment kills the whole 15k-line file silently — the one-liner is in [gotchas.md](../.claude/docs/gotchas.md)).
2. Serve from the repo root on **:8124** — never `file://`. Browser-console checks: the whole inline script is one IIFE — nothing is reachable on `window`; drive checks through synthetic DOM events on real elements. Deck membership (`myLisst`) persists across reloads — a "fresh" check may start with boards already decked.
3. Verify, minimum: desktop ≥1280 hover dress · **iPhone 15 Pro sim (393×852)** grid + lightbox · card→lb open/close flight lands every edge · flip in grid AND lb · blank-card behavior with a board decked · home belts still recycle.
4. If the change is gated/experimental: defaults stay **bit-identical** (pixel-verify).
5. Rerun `python3 build_context.py` so the Facts above stay honest; append the decision + why to [.claude/docs/cards.md](../.claude/docs/cards.md).
6. Commit; **Dylan makes the push calls** (pushing main is publishing).
7. **Until cutover, the vault leads** — pre-launch site changes land in the vault working copy and PORT here (recipe in [.claude/HANDOFF.md](../.claude/HANDOFF.md)). A card ticket that starts in v1 must say why it's exempt.
