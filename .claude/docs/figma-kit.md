# The Figma site kit — the site's parts as mockup assets

**File:** "AVRG — Site Kit" · `https://www.figma.com/design/2QS87sR9PBcckdYhFrPsIJ`
(Dylan's own Figma team, `team::1620987893342153680`, pro tier. Private file — the URL alone grants nobody access.)

## What it is

A **mockup kit**, not a source of truth. Built 2026-08-20 on Dylan's ask: *"take all the components
of the avrg site and make them into figma assets I can use for mockups… almost like our bench…
just different assets so I can move them around / change fonts / colors."* He is new to Figma
("basically using it like advanced MS Paint"), so the kit is built for dragging and reacting, not
for design-system hygiene.

**The site does not read from it and never will.** Same standing rule as the old mockups: *Figma is
a translation layer, not the iteration target* — real iteration happens in `index.html` on :8124.
**The kit is allowed to drift stale.** If a surface changes materially and Dylan is mocking on it,
re-measure and update the kit; otherwise leave it. This is NOT the bench's change-with-charting
law — there is no contract here.

## How it was built (repeat this recipe if a surface gets added)

Values were **measured off the running page**, not read out of the CSS — the ONE CARD SPEC is
`cqw`-based, so source values only resolve correctly against a live 232px container.

1. Serve on :8124, open at 1440×900, route to `#shop-all`.
2. `getComputedStyle` + `getBoundingClientRect` on the real nodes; card values taken from a
   **visible `.scard .d7f`** (the first `.d7f` in the DOM is a hidden `.mtblank` and measures 0×0 —
   its `cqw` values resolve against the wrong container and come back garbage).
3. Cloud Figma MCP (`use_figma`) writes the file. `upload_assets` for the real PNG/JPGs.

## What's in the file

| Page | Holds |
|---|---|
| `01 · Read me` | Plain-English orientation written for a Figma beginner — Assets panel, editing text, the K scale tool, Detach instance. |
| `02 · Foundations` | 16 colour **variables** (collection "AVRG", one Light mode) as swatches · 11 **text styles** as a specimen board · the five source images. |
| `03 · Card` | 9 components + an annotated anatomy board + a three-state board. |
| `04 · Home page` | 11 components + a full 1440 desktop home mockup assembled from them. |

**20 components** land in the Assets panel. Naming is `Surface / Part` so the panel groups them.

## Decisions worth keeping

- **Colours are variables, not paint styles** — Dylan's ask was literally "change fonts / colors",
  and a variable is the one place that changes everything at once.
- **The card scales as one object.** Every child of `Card / Full` (and of `Card part / Inner frame`)
  carries `constraints: SCALE`, so the card is a photographic reduction at any size — the same law
  `lockCardScale` enforces on the site. **Caveat recorded in the read-me:** a plain corner-drag does
  not shrink text inside *nested* instances (the chips). The Scale tool (**K**) does. The 1440
  mockup's belt cards were built with `instance.rescale(172/232)` for exactly this reason.
- **The monogram is the real vector**, imported from the inline `#logo-draw` markup via
  `createNodeFromSvg`. **Declare the SVG at its display size** (`width="150" height="159.6"` with
  the viewBox unchanged) — importing at `982×1045` and then `resize()`-ing leaves the 28-unit
  strokes at original scale and the mark renders as a black blob. Same trap applies to the deck
  mark and the +List glyph.
- **Chips show their hover text.** On the live card `.sttxt` and `.fc-list .ft` are empty at rest
  (the decode writes them on hover). The kit ships them written — legibility beats fidelity in a
  mockup — and the component descriptions say so.
- **Resting-vs-hover, generally:** the kit is the *decoded* card. Rails at 41%, no lift, no fill.

## The Satoshi trap (bitten here)

`listAvailableFontsAsync` over the **cloud** MCP does not see locally-installed fonts. Satoshi Black
**is** installed (`~/Library/Fonts/Satoshi-Black.otf`, and the repo ships it at
`site/fonts/Satoshi-Black.otf`) but came back missing, so `Display / Section title` was built on
**Archivo Black** as a stand-in. The fix is one edit in the desktop app: set that text style's font
to Satoshi Black. Both the read-me and the foundations page say so. **Do not "fix" this by telling
him to install the font — he already has it.**

Space Mono Bold and Bricolage Grotesque (Regular / ExtraBold) resolved fine — they are Google fonts.

## Not in the kit yet

The lightbox, the deck drawer, the contact composer, YOUR PICKS, the mobile costume, the collection
grid page, the drop menu's mobile rows. Add them the same way if he starts mocking on them.
