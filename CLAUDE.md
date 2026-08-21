# AVRG site (v1) — working notes for Claude

> **This repo is PUBLIC.** Everything committed here — including this file — is readable by anyone. Keep business rationale, personal context, and anything sensitive out; that belongs in Claude's local memory, which points here for project mechanics.

## What this repo is

**The site, and nothing else.** `index.html` IS the site — one hand-built file, HTML + CSS + JS inline, ~14k lines. No framework, no npm, no build step for the page itself. Media is committed directly (no LFS).

Created 2026-08-16 as a clean copy of the working page out of the workshop repo (**the vault**, `~/Projects/avrg-site`, which is 1.5GB of labs, photo archives and full react history). v1 holds the page + exactly what builds it: `index.html` is the vault's `redesign/k-home-dual.html` with its asset paths repointed, `sources/` is the build input, `site/` is the build output plus the committed media.

**The vault is RETIRED (2026-08-20, Dylan's ruling) — frozen archive, not the reference.** Every lab and tuner page, `labs.md`, `PORT.md`, the raw photography, the raw videos, `about/` staging, `AVRG brand img/`, `retired/`, `design-bundle/` and the pre-split commit history still live only there, read-only. **No more editing in the vault, no more porting** — all work happens HERE, directly. When a doc in this folder says "see the lab", that's archaeology: the lab file exists in the vault but nothing keeps up with it anymore.

**The public Pages URL still serves from the vault repo until the Saturday cutover** — see "Where things stand". That's a serving fact, not a workflow fact: changes land here only.

## Commands

- `python3 build_site.py` — reads `sources/`, writes `site/img/{thumb,full}` + `site/data.js`. Re-run any time photos in `sources/` are added, removed or moved. (`seed_boards.py` did not come across — it seeded from raw photo folders that live in the vault.)
- `python3 build_context.py` — regenerates the DERIVED halves of `context/` (the card pack's Facts block + the whole bench page). Run after any change to `index.html` or `site/data.js`. Authored Intent sections are never touched.
- Preview: `.claude/launch.json` config **`avrg-v1`** — `python3 -m http.server 8124`, serving the **repo root**. The page is `http://localhost:8124/index.html`. Never `file://`. A second config **`avrg-vault`** serves the vault working copy on :8123 (labs + the leading page live there until cutover).
- **LAN ride-along:** python's `http.server` binds all interfaces, so `:8124` reaches his phone on the same wifi (`http://192.168.1.119:8124/`) — instant, no push, no Pages cache.

## Layout

```
index.html               THE SITE — HTML + CSS + JS inline (~847KB, ~14k lines).
                         ANCHOR SEARCH IT, never read it top to bottom.
favicon.png
.nojekyll                GH Pages serves the tree as-is (no Jekyll pass)
build_site.py            sources/ -> site/img/{thumb,full} + site/data.js
README.md                the human-facing one-screen orientation
site/
  data.js                GENERATED — never hand-edit
  fonts/Satoshi-Black.otf
  img/thumb/  (84)       built from sources/
  img/full/   (84)       built from sources/
  img/logo-circle.png · img/logo-line-white.png
  img/cards/canva/ (66)  card artwork — the LIVE SUBSET of the vault's 168-file batch
  img/cards/cuts/  (6)   the originals cutouts
  media/                 covercard.mp4 + poster · story-clamps.jpg · clip-1/2.mp4 + posters
sources/                 build input, one folder per collection
  classic/     (38)      loose image = a single-photo board; subfolder = one board, many angles
  hand-shaped/ (28)
  resale/      (empty)   a live COLLECTIONS entry with no boards yet
  originals/   (6 board folders — 3 images + a description .txt each; require_desc)
```

**Path grammar inside `index.html`** — everything is repo-root-relative: `site/img/…`, `site/data.js`, `site/fonts/…`, `site/media/…`, `favicon.png`. The `IMG()` helper (`const IMG = p => (p ? "site/" + p : p)`) prefixes the data-driven image paths. The vault's `../site/`, `../videos/web/` and `card-lab/…` forms are DEAD here — full mapping table in [gotchas.md](.claude/docs/gotchas.md).

**The logo is inlined.** The single-stroke draw is an inline `<svg id="logo-draw">` (SMIL, `setCurrentTime` rewind). The `.svg` source artwork stays in the vault's brand folder — it is not a runtime dependency and does not need to be here.

## The docs — read before touching the matching surface

The deep project memory — decisions, laws, mechanics, react history — lives in `.claude/docs/`, split by surface. **Read the doc for the surface you're touching before working on it**; that's where the bitten-once lessons live. When a session lands new decisions, append them to the matching docs file (this file only gains pointers).

- [k-core.md](.claude/docs/k-core.md) — page-level: grounds, pinned CARD/LB constants, gpick, light-mode plumbing, the drawn logo.
- [header-bar.md](.claude/docs/header-bar.md) — the drawn desktop bar, the phone bar, the drop, section bar, category header posts, deck mark, the picks stack, button grammar.
- [cards.md](.claude/docs/cards.md) — ONE CARD SPEC, +List chip/tag, canva cutouts + inventory refs (the jref/refOf law).
- [lightbox.md](.claude/docs/lightbox.md) — the whole inspection view: dress regime, sun, deck/neighbours/exchange, collection strip, undersides carousel.
- [deck-drawer.md](.claude/docs/deck-drawer.md) — the desktop bay: drawer geometry 2.0, flights/arcs, drag, deck holes, close chrome, the LB carry.
- [contact-composer.md](.claude/docs/contact-composer.md) — the contact stage: envelope, letter, send/copy/flip ceremony.
- [home-shop.md](.claude/docs/home-shop.md) — the home bands, the conveyor, the collection pages, shop-all.
- [picks.md](.claude/docs/picks.md) — YOUR PICKS + the deal ceremony (the deck-is-a-page, the bench, the offer letter).
- [mobile.md](.claude/docs/mobile.md) — the phone grammar: phone passes, mobile strip, the load intro, swipes/pinch, retired dock history.
- [gotchas.md](.claude/docs/gotchas.md) — every bitten-once platform/CSS/tooling lesson, plus the v1 port laws at the bottom. Read when debugging anything weird, and before browser verification.
- **`context/` — scoped-landing context packs** (first: [context/card.md](context/card.md) + its bench page at `/context/card-bench.html` on :8124). A pack = DERIVED facts (regenerated by `build_context.py`) + AUTHORED intent/laws/success-criteria. For a scoped ticket on a surface with a pack: read the pack, then only what it points at — the pack is the landing, the `.claude/docs/` file is the archaeology.
- [open-threads.md](.claude/docs/open-threads.md) — what's still open, parked passes, undecided directions, the site thesis.
- [design-sync.md](.claude/docs/design-sync.md) — the claude.design "AVRG Site" project (its recipe still points at vault paths).

## The AVRG Bench (the tuning deck at /bench)

**What it is:** a live tuning UI over THIS page — Win2000 dress, sliders
and wells bound to the real site's values — at
**http://localhost:8124/bench/**, riding the same server that serves the
page. It owns ZERO site code: every control drives the actual page through
injected CSS overrides or the fenced, localhost-gated **BENCH shim** at the
main IIFE's foot in `index.html` (exposes `STRIP_TUNE`/`NB_TUNE`/`SUN` by
reference — the shim is the ONE sanctioned bench hook in this file; extend
it deliberately, and it retires with the pilot). Not to be confused with
`context/card-bench.html`, the card context pack's static bench page.

**Where it lives:** `bench/` here is a **symlink** to
`~/Projects/CompUI/pilot/` and is **gitignored — this repo is PUBLIC and
bench files (manifest, BUILD-SPEC, the UI) never get committed to it.**
Bench changes are committed in the CompUI repo:
`git -C ~/Projects/CompUI add pilot && git -C ~/Projects/CompUI commit`.
CompUI has no remote; nothing there gets pushed.

**The contract (canonical since 2026-08-20, Dylan's ruling):** the bench
and the site move together. A site change that touches a **charted param**
(one in `bench/manifest/avrg.json`) updates the manifest — and the bench's
ANCHORS entry when the override shape changes — **in the same session**. A
new tunable surface gets charted when first touched. Two lanes:

- **Inline (small):** retuning an already-charted value (a bake landing, a
  range widening) — just update the manifest value/note yourself.
- **Dispatch (real charting):** a new param spec, a new wing, or a
  multi-param pass — do the site edit + any shim notation here, then hand
  the **`bench-cartographer` agent** (`.claude/agents/`) a ticket: param
  ids/names, exact selectors or consts, shipped values, sensible ranges,
  couplings/laws worth recording. It edits the CompUI side, verifies
  end-to-end on the served bench, commits there, and reports back — this
  session stays pointed at the site and Dylan.

**Bench laws that bind this repo's sessions** (constitution:
`bench/BUILD-SPEC.md`): the manifest is the bench's ONLY data source;
anchors are NAMES (selectors, consts, vars) — never line numbers; params
bind to the one shared source — a bench-side fork is unconstitutional,
"separation" is a site-code change Dylan orders; locked params render
visible, never hidden; overrides replicate shipped behavior exactly,
quirks included — a shipped quirk is flagged as a find, never silently
fixed.

**Verifying bench work:** the Claude pane's frame loop is dead inside the
stage iframe — motion is unjudgeable there AND CSS transitions freeze
mid-flight (computed style reads the START value; kill the transition with
a probe rule or use the CDP harness in gotchas). Cache-bust every load
(`?v=<ts>`).

## Always-on rules (the short list)

- `site/data.js` is **generated** — never hand-edit; re-run `build_site.py`.
- **`sources/` ordering IS board identity** — ids are positional and the card-art map is keyed to them. Add new photos so they sort LAST. The full law is in [gotchas.md](.claude/docs/gotchas.md); read it before touching `sources/`.
- Serve from the **repo root** on :8124 (`avrg-v1`), never `file://`.
- **Pushing main is publishing** — GitHub Pages serves `main` at root for `bluechewbill/avrg-site-v1`. A half-built state pushed mid-session is live at a URL people have. Commit freely; **Dylan makes the push calls.**
- **Never add a ref producer** — call `jref`/`refOf` (three producers was two too many).
- The z ladder: shields (deal + menu-select + intro) 6700 · `#vlb` 7000 · topbar 6600 · flights (`.bay-fly`) 6500 · intro masthead lift 6450 · focus veil (`.fveil`) 6400 · bay 5500 · lb 5000. The bar rides ABOVE the flights on purpose; `#vlb` is the one true full-screen modal. New overlays pick a rung deliberately.
- Desktop first, then mobile. **Dylan reacts to built variants, not specs** — collide options, let him pick.
- Mobile checks go to the **iPhone 15 Pro simulator first** (393×852pt — it matches his phone); keyboard behaviour goes to his real phone, the sim runs a hardware keyboard. The Claude browser pane **cannot play motion** (dead rAF frame loop) — verify motion in real Chrome / chrome-devtools MCP. Details: [gotchas.md](.claude/docs/gotchas.md).
- **Syntax-check the inline script before verifying anything** — one stray comment kills the whole file with nothing useful in the console. The one-liner is in [gotchas.md](.claude/docs/gotchas.md).
- Board dimensions: `DIMS_MM` in `index.html` is **hand-authored**, keyed by padded ref, and feeds the hover dims-decode — all 14 hand-shaped boards + 12 of 19 classics. Tail/nose widths print in the lightbox `#lb-dims` line only ("too much noise on a card decode"). Still unmeasured: CL 03/06/08/12/16/19/26, originals, resale.
- The lb selected-state accent is deliberate — ask before removing.
- **The scroll relay SLEEPS** — `RELAY_ON = false` in the relay IIFE; the one switch gates both the CSS (`body.relayon`) and the machine. Parked, not bailed on. Do not wake it without his word.
- ~~Until cutover, the site is edited in the VAULT and PORTED here~~ **RETIRED 2026-08-20: the vault edit-and-port workflow is over — edit HERE directly.** The old porting recipe stays in [.claude/HANDOFF.md](.claude/HANDOFF.md) as history. (The 2026-08-16 A/B experiment is CLOSED — its record + trip log live in the HANDOFF; multi-item lists are just lists again.)
- **A site change that touches a charted bench param isn't done until the bench knows** — see THE AVRG BENCH section above (the change-with-charting law).

## Where things stand

- **2026-08-16: v1 was created** from the vault at commit `9aca992` (working tree clean), cleaned, and **PUBLISHED at https://bluechewbill.github.io/avrg-site-v1/**. The founding commits: THE COPY (the live site, whole, in its own house) · THE DEAD CODE COMES OUT (the takeover-case machine and `cardInner`'s photo branch, both unreachable, removed for real — only comments still name them) · THE MEMORY MOVES IN (these docs) · THE TOMBSTONES COME OUT (comment-only sweep, proven code-identical; 18 JS section banners) · the angry-0 removal. Verified same day: zero 404s, zero console errors, every route, both grounds, the phone costume.
- **What the page is at this point** — the feature state as of `9aca992`: the drop-lab header dress on both surfaces, the send takeover, the LB carry suite, THE PICKS CEREMONY (the deal, the bench, the driven glides, the deal shield), thread 3's mobile pass (THE LOAD INTRO, THE WORD IS THE DOOR, THE MENU-SELECT CEREMONY), the drawn logo on every home arrival, real board dims, and the launch trim (the foot goes home). Every react history for those lives in the surface doc that owns them.
- **The live site is still served from the VAULT repo** (`bluechewbill/avrg-site`, GH Pages) until cutover — but **the edit-in-vault-and-port workflow ENDED 2026-08-20 (the vault is retired; v1's structure passed the test)**. All changes land here; what the public URL shows lags until the Saturday cutover flips it. The old recipe + baseline hash live in `.claude/HANDOFF.md` as history.
- **2026-08-20: THE BENCH WENT CANONICAL** — the CompUI tuning bench at `/bench` and this site now move together (see THE AVRG BENCH section). Same day: THE ORIGINALS GO DEEP charted as bench wings `lb-og-thumbs` + `lb-og-desc` (census 103), and Dylan ruled LIGHT IS THE DIRECTION — dark mode comes out before launch (see open-threads).
- **The cutover checklist is LIVE — launch target Saturday 2026-08-22, ~noon (Dylan, 2026-08-20). The order:** verify the v1 live URL → Dylan buys a domain (he wants **avrg.website** and **avrg.cards** — his purchase) → a `CNAME` file here + DNS at the registrar per the GitHub Pages docs → flip the vault repo **private** (its Pages URL dies with it — free plans don't serve Pages from private repos) → future work happens in v1 directly. Optionally rename the local folders at that point so the working repo takes the familiar path; note that changes Claude's per-project memory keying.
- **Still open / parked:** see [open-threads.md](.claude/docs/open-threads.md) — the intro tweak + decode-timing threads, thread 1's desktop half, thread 2 (home collection cards), thread 3's desktop half, waking the relay, the ORIGINALS RETHINK, the iPad tweaks (lowest priority, unenumerated), sound, the browser-compat sweep.
