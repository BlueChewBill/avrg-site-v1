# Handoff — AVRG site v1 — 2026-08-29 (evening, second session)

> Dylan, at goodnight: "tell the next guy i said hi." Hi. /salute

> (The old vault→v1 porting recipe + the closed A/B trip log live in this file's git history — CLAUDE.md still points here for them.)

## Where we are

THE SLUGGISH-SUN HUNT is closed and everything is pushed (`b59080c`-era, tree should be clean after the wrap commit): the sun had been drowning since 08-28 — 655ebac's `.panel:hover` reword out-specified the `.suntrack` transition mute, so every per-frame sun write restarted the .94s hover glide in every browser. Dylan's screenshots cracked it; the mute is armored; his verdict on the healed engine: **"thats the feel."** Same session: the link-preview meta pass landed (og:/twitter: + composed `site/media/og-share.png` — the Sunday-critical item is DONE), the inventory went honest (CL 06/08/16/19 MIA→SOLD via `JGONE`; the inception demo lies CL 05 "Sold"/HS 02 "Pending" came out), CL 03/12/26 got measured, and the board backlog was re-counted at 48 (19 CL + 29 HS undocumented). CLAUDE.md's Where-things-stand has the one-liner; lightbox.md owns the sun record; two new gotchas (the specificity-tie landmine + synthetic-events-can't-see-:hover).

**The sun-feel thread is settled by his ruling:** the engine is healed and any residual taste adjustment he'll do himself "with the bench tuning later." The `?sun=`/`?grow=`/`?hud=` collide plumbing is still IN the file (param-gated, verified inert on the bare URL) — it retires whenever he declares the boundary question dead; don't strip it unprompted.

## Next task

**HIS LIST, two items, desktop first:**

1. **Another pass on the "add" chip** — the `.fstack` mini-card glyph on `.fc-list` (cards.md's THE ADD CHIP redesign, three reacts deep: flat EMPTY mini card in the fv3 dress). No spec given at wrap — open by getting his react/direction, then build variants (his three-react refinement pattern: ship each react fast, he converges). Remember: the class/const names are a kept lie (`.fstack`/`STACKSVG` — bench anchors point at them, don't rename).

2. **A new desktop dropdown from the top-left AVRG bar logo** — for now ONE entry: **media**, doing exactly what clicking the home-page spine video does today (`openVlb` — `#vlb`, the one true full-screen modal, z 7000). Then **re-present that clicked view more like the card lightbox: the playing video gets FLANKERS of the other videos** (today `#vlb` has poster thumbs in `#vlb-thumbs`; he wants the lb's neighbour grammar instead — flanking videos beside the hero). Check what the bar logo's click currently does (header-bar.md) before hanging a dropdown off it, and rhyme the dropdown with the existing drop grammar rather than inventing a new one. This is likely the long-waited home for the vault's `videos/web/` riding clips (open-threads line ~30) — but only the three shipped clips are in `site/media/` today; more clips = his export call, ask before hauling vault media.

Done for (2) = the dropdown opens on the logo on desktop 941+, media entry opens `#vlb`, and `#vlb` shows the hero video with the other clips as flankers in the lb language — his react round included.

## Read these, skip the rest

- `.claude/docs/header-bar.md` — the bar + the drop grammar before touching the logo seat.
- `.claude/docs/lightbox.md` — THE VIDEO LIGHTBOX section (the `#vlb` machinery: `VIDEOS` table, `clipEls`, the cover-slot-is-the-spine-video law, open/close FLIP) + the LB DECK/flanker grammar it should start rhyming with. THE SUN WAS DROWNING IN THE HOVER GLIDE if any sun work comes up.
- `.claude/docs/cards.md` — THE ADD CHIP section for task 1.
- `.claude/docs/gotchas.md` — before ANY browser verification. New this session: synthetic events never set `:hover` (hover-gated bugs need real CDP input), and kill the chrome-devtools MCP's Chrome when verification wraps (it hijacks Dylan's Dock relaunch).
- `git log --oneline -20` — tonight's story.

Everything else is NOT needed until a task leads there. Re-run `build_context.py` after any index.html change.

## Context that isn't in the code

- **Push cadence tonight was per-drop on his word ("push it") — that grant ended with the session; pushes are his call again.**
- **The meta-tag wing LANDED after goodnight** — CompUI `771142a`, census 147→168: the `link-meta` wing, 21 locked rows, a new tier 4 minted ("the document head, nothing on the stage to drive"). The full record + the share image's measured recipe now live in **k-core.md's THE LINK-PREVIEW CARD** (the recipe's only durable home — the compose script wasn't kept). Cartographer finds parked there for Dylan: the shadow's crescent outside the frame (charm or 10px-low, his call), the near-house throw ratio, missing `twitter:site`/`og:locale`/`twitter:image:alt` (twitter:site needs his X handle), and a bench-side `bakeText()` UTC date quirk (evening bakes stamp tomorrow — flagged, not fixed). Also learned: **CompUI has a GitHub remote now** (CLAUDE.md updated); local commits sit ahead of it, pushing CompUI is Dylan's call.
- **The share card is composed, not shot** — white ground, inverted line logo, HS 04's painted `-bottom` face (hs2/3/4 lead with `-bottom` as the card front), hard offset shadow, hairline frame. Recipe in commit a5a3522's message. If Dylan wants a different board on it, it's a re-render, and DM apps cache previews (re-scrape via opengraph.xyz after changes).
- **Dylan's feel reports are precise instruments** — this session's whole arc. When his glass and your probes disagree, the glass wins; go hunting for what the probe can't express. (Saved to memory too.)
- **The identity migration is chartered but parked** (open-threads Misc queue): filename-derived board ids, the originals' NN-prefix playbook generalized, byte-identical data.js diff as acceptance. **Do it BEFORE the 48-board batch.** His framing: not urgent.
- **The 48-board batch**: additions sort LAST (safe by the ordering law); per-board site cost is one CANVA line + one dims line + a cutout pair; he shoots in increments, any size drop is valid.
- Caliper list still open: HS 10/15/18 tail/nose, originals if ever.

## Parked / later

- The sun wake-boundary question (accept vs `?sun=4` vs warm ring, grow size) — HIS bench-tuning territory now; collide plumbing stays until he calls it.
- The weekend big three minus what closed: og sheets ×6 export+wire (Figma material mostly composed) · the 48-board batch (ORDERING LAW; identity migration first) · spark tag language + touch surfacing (the DM conversation).
- +List on-state border accent · stack-seat optics (Sunday-dispatch taste calls, still unjudged).
- The deckmark cleanup chip (own session, #picon `.deckmark` caveat) · the cosmetic code cleanups · Safari pass proper · iPad (lowest).
