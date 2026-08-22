# Handoff — AVRG site v1 — 2026-08-22 (post-launch)

> Previous handoffs (the launch-day briefing, the old port recipe) live in
> this file's git history.

## Where we are

**THE SITE IS LIVE at https://avrg.cards.** The cutover ran in the small
hours of launch day: 35 commits pushed, domain bound, cert issued, Enforce
HTTPS on, avrg.website 301-forwards, vault repo flipped private (old URL
dead). Every push to main now publishes immediately.

Same session, the **originals LB direction SETTLED — THE ZONE ruling**
(record: open-threads.md's og entry, 2026-08-22): card stays the constant,
right of it a defined **480×640 zone** each original fills with its own
hand-composed sheet. Dylan composes at 2× (960×1280) in the Figma kit —
page **"07 · OG Sections — fill per board"** (six canvases, OG 02 seeded).
The kit's "Originals LB Mockup" page holds the six reaction variants
(A–F) that got us here. His per-board loop: bg-removed top+bottom cutouts
for the card → find a clip → compose the section. Sections may differ per
board on purpose; spec-only captions, no ply line, no color-salesman copy.

## Next task

Depends on what Dylan brings (he said the site "might be a Sunday thing"):

1. **If a composed section exists** (or he wants help composing): export
   it at 2× to `site/img/og/og-NN-section.png`, then build the site-side
   seat — og LB: card centered, zone right (480×640 @1× reference, scales
   with the LB), clip + short text left. Done = the first board's new LB
   live-ready on :8124, desktop. The og-wing bench re-chart
   (cartographer dispatch) rides this landing.
2. **The Safari sweep** — he raised it at session end, it's newly urgent
   because the site is PUBLIC now. Good phone-free candidate. Plan already
   given to him: desktop Safari pass on his Mac (console + walk every
   route/ceremony), fix the small stuff (playsinline, -webkit- prefixes,
   audio unlock timing, JS feature gates). iOS is already largely proven —
   every iPhone browser is WebKit and the phone costume was built/tested
   against his iPhone + the sim all along.
   **His remembered symptoms (start here):** the board grow + cursor-chase
   interactions misbehaving, and Safari treating the board image like a
   copyable photo — selecting/highlighting it mid-interaction. That last
   one is the classic macOS Safari image-drag/selection behavior; the
   known-cheap fixes are `-webkit-user-select: none` +
   `-webkit-user-drag: none` (+ `-webkit-touch-callout: none`) on the
   interactive imagery and their hover containers. Grow/chase jank likely
   wants transform/will-change checks in Safari's compositor. He may run
   a walkthrough himself and bring notes.

## Read these, skip the rest

- `.claude/docs/open-threads.md` (og entry, 2026-08-22 tail) — THE ZONE
  ruling record; the contract for the og work.
- `.claude/docs/lightbox.md` — the og spread the zone build replaces.
- `.claude/docs/gotchas.md` — before any browser verification (and the
  Safari sweep).
- CLAUDE.md "Where things stand" — launch + zone entries updated 08-22.

Everything else is NOT needed. The Figma kit file is
`2QS87sR9PBcckdYhFrPsIJ` ("AVRG — Site Kit"); mockup archaeology lives
there, not in the repo.

## Context that isn't in the code

- **The zone contract:** the site renders exactly the 480×640 box; what's
  inside is baked per-board in Figma. This deliberately KILLS the
  template-consistency problem (photos no longer need to match across
  boards). The card carries dims/AVAILABLE/WANT — the sheet never repeats
  them.
- **Figma mechanics:** uploaded Peach/Piro assets live in the kit (bottom
  cutout hash reused across variants). The kit's Satoshi trap still
  stands (Archivo Black stand-in). Loose drag-parts sit above the mockup
  frames.
- **Launch facts:** GH Pages API path used for the cutover:
  `gh api repos/BlueChewBill/avrg-site-v1/pages` (status/cert), PUT with
  `https_enforced=true` once cert approved. The og stand-in clip (one cut,
  six boards) knowingly shipped.
- **His energy:** pool work Saturday morning; today ran slower than he
  hoped — keep Sunday's scope tight, one board end-to-end beats six
  half-wired.

## Parked / later

- og mobile view (after the first desktop board lands).
- Per-board folders (his Desktop) — spec now: bottom-cut + top-cut +
  free-form raw shots + clip.mp4 + info.txt (name/dims only).
- The og-wing bench re-chart — dispatch WITH the zone landing, not before.
- Blur-on-fades pass, calipers/DIMS_MM session, about page, thread 2
  (home collection cards via the plate lab), thread 3 desktop half,
  relay (his word only), iPad (lowest).
- Post-launch tier now ACTIVE tier: the Safari/browser-compat sweep (see
  Next task), the dark base CSS proven-identical sweep.
