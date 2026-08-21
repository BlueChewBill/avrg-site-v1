# The Figma site kit — the site's parts as mockup assets

**File:** "AVRG — Site Kit" · `https://www.figma.com/design/2QS87sR9PBcckdYhFrPsIJ`
(Dylan's own Figma team, `team::1620987893342153680`, pro tier. Private file — the URL alone grants nobody access.)

## What it is

**A sketchpad that sits BEFORE the build.** Dylan's framing, 2026-08-20, and it is the whole brief:
*"the figma file can be its own thing. its just so i can move things freely and get a feel for what
I want before we do the site/bench building."* He is new to Figma ("basically using it like advanced
MS Paint"), so it is built for dragging and reacting, not for design-system hygiene.

**It is its own thing.** The site does not read from it, it does not mirror the site, and there is
**no change-with-charting law here** — that contract belongs to the bench alone. The kit is allowed
to drift stale and nothing in it can break anything. Re-measure a surface only when he starts
mocking on it and the kit's version has gone wrong enough to mislead him.

This also supersedes the old "Figma is a translation layer" note in Claude's memory: it is not a
translation of finished work, it is where the work gets FELT OUT first. When a mock here turns into
a direction, THAT is when site/bench building starts.

## How it was built (repeat this recipe for a new surface)

Values were **measured off the running page**, not read out of the CSS — the ONE CARD SPEC is
`cqw`-based, so source values only resolve correctly against a live 232px container.

1. Serve on :8124, open at 1440×900, route to the surface.
2. `getComputedStyle` + `getBoundingClientRect` on the real nodes.
   - Card values must come from a **visible `.scard .d7f`** — the first `.d7f` in the DOM is a
     hidden `.mtblank` that measures 0×0, and its `cqw` values resolve against the wrong container
     and come back garbage.
   - **Wait for the flight to land before reading.** A lightbox read at 1200ms returns the card at
     its GRID position mid-scale. ~2s, and check for the `.in` class.
   - **The deck drawer will not open in the Claude pane at all** — see gotchas.md, the rAF family.
     Use chrome-devtools MCP and click `#bay-panel`.
3. Cloud Figma MCP (`use_figma`) writes the file. `upload_assets` for the real PNG/JPGs.

## What's in the file

| Page | Holds |
|---|---|
| `01 · Read me` | Plain-English orientation written for a Figma beginner — Assets panel, editing text, the K scale tool, Detach instance. |
| `02 · Foundations` | 16 colour **variables** (collection "AVRG", one Light mode) as swatches · 11 **text styles** as a specimen board · the nine source images. |
| `03 · Card` | 9 components + an annotated anatomy board + a three-state board. |
| `04 · Home page` | 11 components + a full 1440 desktop home mockup. |
| `05 · Lightbox` | 9 components + TWO full pages — the standard inspection and the originals spread. |
| `06 · Deck drawer` | 6 components + a full page with the drawer out and the shop making room. |

**35 components** land in the Assets panel. Naming is `Surface / Part` so the panel groups them.

## Decisions worth keeping

- **Colours are variables, not paint styles** — his ask was literally "change fonts / colors", and a
  variable is the one place that changes everything at once.
- **ONE CARD, THREE SIZES — and the kit proves the law.** Measured, not assumed: the lightbox card
  is `Card / Full` at **1.532×** (355.5 wide; its 8.5px chip type computes to 13.0265 = 8.5 × 1.532)
  and the drawer's shelf card is the same card at **0.698×** (162 wide). Nothing is re-laid-out at
  any size. If a future session finds a surface where that *isn't* true, that is a site bug, not a
  kit bug.
- **The card scales as one object.** Every child of `Card / Full` (and of `Card part / Inner frame`)
  carries `constraints: SCALE`. **Caveat recorded in the read-me:** a plain corner-drag does not
  shrink text inside *nested* instances (the chips). The Scale tool (**K**) does, and
  `instance.rescale(k)` does — which is how every scaled card in the mockups was placed.
- **The lightbox card is the DRESSED card.** Built by instancing `Card / Full`, rescaling, then
  detaching (top-level then every nested instance in a loop) and restyling: chips fill black, ref
  reads AVRG, the name slot rests on dims, the want-word replaces "+ LIST", and the hard slab
  shadow goes SOFT (`0 15 40 rgba(0,0,0,.35)`) because the card is lifted rather than sitting.
- **There is no lightbox scrim.** The focus effect is `body.lb-fade #colpage { opacity: .08 }` — the
  whole page behind simply drops to 8%. Both full pages reproduce it as an 8% group, not a fill.
- **The drawer's shadow throws LEFT** (`-7px 9px 0 -1px`), mirroring the card's right-throw, because
  the drawer comes from the right edge. Same hard-slab law, opposite hand.
- **The deck holes are in the mockups on purpose** — a decked board leaves a real empty slot in the
  grid. Two holes out of six reads as intentional; three out of six read as broken, so the drawer
  page was rebuilt with fewer.
- **Chips show their hover text.** On the live card `.sttxt` and `.fc-list .ft` are empty at rest.
  The kit ships them written — legibility beats fidelity in a mockup — and the descriptions say so.

## Traps this cost time on

- **Declare an imported SVG at its DISPLAY size.** `createNodeFromSvg` at `982×1045` then
  `resize()` leaves the monogram's 28-unit strokes at original scale and it renders as a black blob.
  Set `width`/`height` on the `<svg>` and leave the viewBox alone. Same for the deck mark and glyphs.
- **You cannot `appendChild` into an INSTANCE.** Adding a third board tag to the drawer head failed
  with *"New parent is an instance or is inside of an instance"*. Add it to the COMPONENT; every
  instance inherits it.
- **Zero-length SVG paths (`M8 12h.01`) may not survive import** — the speech-bubble's three dots
  were rebuilt as real `<circle>`s.
- **Don't guess node ids between calls.** A component id assumed from a previous return was actually
  a RECTANGLE and the whole script threw. `findAllWithCriteria({types:["COMPONENT"]})` first.

## The Satoshi trap (re-tested 2026-08-20 — still stands)

`listAvailableFontsAsync` over the **cloud** MCP does not see locally-installed fonts. Satoshi Black
**is** installed (`~/Library/Fonts/Satoshi-Black.otf`, and the repo ships it at
`site/fonts/Satoshi-Black.otf`) but comes back missing, so `Display / Section title` was built on
**Archivo Black** as a stand-in.

**Enabling the LOCAL Figma Dev Mode MCP does not fix this** — Dylan enabled it mid-session and
`figma.loadFontAsync({family:"Satoshi", style:"Black"})` still threw *"The font family Satoshi does
not exist"* for Black, Bold and Regular. The local server is read/codegen only; it does not host
plugin execution. The fix stays a one-edit manual swap in his desktop app: set that text style's
font to Satoshi Black. Both the read-me and the foundations page say so. **Do not "fix" this by
telling him to install the font — he already has it.**

Space Mono Bold and Bricolage Grotesque (Regular / ExtraBold) resolve fine — they are Google fonts.

## Not in the kit yet

The contact composer, YOUR PICKS + the deal ceremony, the mobile costume, the collection grid page
as its own mockup, the drop menu's mobile rows. Add them the same way if he starts mocking on them.
