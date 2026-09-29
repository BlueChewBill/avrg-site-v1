# Handoff — AVRG site v1 — 2026-09-29 (the post held, the card recomposed)

## Where we are

Everything site-side is pushed and live on avrg.cards: the envelope's "send to: [mark] @" + paper grain (8542667), the new link-preview card (dbc03ec — `site/media/og-share.jpg`: Dylan's profile shot of a deck over its reflection + the white mark + "celebrating the mundane" + AVRG.cards, beside HS 06's real gallery card, top side up), and the notes (ead3b3d + this wrap). The r/Fingerboards post is **composed but NOT posted** — held to the weekend of 10-03/04. The post text (his title + the tightened body) is in Claude's memory (`avrg-reddit-post`) and was sent to him as a file; Reddit can't draft gallery posts.

## Next task

**Dylan's pre-post pass, over the rainy week — his call what's in it.** He named: "maybe even take another pass at the site and the photos before posting", and **"how the boards get organized might be part of the next pass."** For the organizing thread, start from open-threads.md's **BOARD IDENTITY LEAVES THE SORT ORDER** (his 08-29 ask: tie ids to the board, not its place in `sources/`) and gotchas.md's `sources/` ordering law. Collide options for him; don't spec at him. Then the post itself (12–3pm CT on whichever day), then the GoatCounter read (avrg.goatcounter.com; `?ref=reddit`).

## Read these, skip the rest

- `.claude/docs/k-core.md` — THE CARD RECOMPOSED (after THE LINK-PREVIEW CARD): the recipe in `.claude/og-card/` (capture-card.mjs → compose.py, byte-for-byte), the new-filename cache-bust, the baked-card coupling.
- `.claude/docs/open-threads.md` — BOARD IDENTITY + the 48-board backlog, if organizing comes up.
- `.claude/docs/gotchas.md` — the `sources/` law before touching `sources/`.

## Context that isn't in the code

- **His words:** "push it" (both pushes), "lets go with 06 (with the board top side up instead of bottom) and add 'celebrating the mundane' between the logo and the deck in small font. with AVRG.cards underneath the board reflection in the black", "the branded boards and the lack of dims for them is to keep the comments popping haha" (deliberate — don't fix).
- **The ref/id trap bit today:** a card READS its inventory ref ("HS 06") while its positional id differs (`hand-shaped-10`, art `hs6-top`; `hand-shaped-06` is another board). Always go through `jref`/`refOf`, and say which one you mean.
- **Share-card rejects** (three white-ground collides: five-board fan, eleven-board rainbow, painted trio) lost to his own layout — his layout instinct beat the generated options.
- **Card-capture rig:** the chrome-devtools MCP profile was locked by another Chrome, so `.claude/og-card/capture-card.mjs` drives headless Chrome over raw CDP (node 26's built-in WebSocket) — reusable for any 4× element capture.
- **Font gap on the image:** its two lines are SF Mono (Mac system), not the site's Space Mono. Invisible at preview size; swap if he wants exact.
- **Bench:** link-meta re-charted (CompUI b33d437); a follow-up fixing the card's key (hand-shaped-10 / hs6-top) was sent to the cartographer at wrap — check `git -C ~/Projects/CompUI log -3` for it. **CompUI is unpushed — Dylan's call.**
- **Stray:** `CLAUDE.md` carries an uncommitted edit from another tool's session (drops "Desktop first, then mobile." from a rule), plus untracked `.agents/`, `.codex/`, `AGENTS.md`, `.claude/TURNS.md`. Left untouched — ask him.
