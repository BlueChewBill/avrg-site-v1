# Handoff — AVRG site v1 — 2026-08-16

## Where we are

**This repo was born today.** The live site — the vault's
`redesign/k-home-dual.html` — now lives here as `index.html` with its
asset paths repointed, beside exactly what builds it (`sources/` →
`build_site.py` → `site/`). Two commits: THE COPY, then THE DEAD CODE
COMES OUT (the takeover-case machine and `cardInner`'s photo branch,
both already unreachable). Nothing about the page's behaviour changed
in the move.

**Copied from the vault at `9aca992`** (`~/Projects/avrg-site`, working
tree clean at the time). That hash is the **port baseline** — see below.

**The live site is still the VAULT's Pages deploy.** v1 is PUBLISHED at
**https://bluechewbill.github.io/avrg-site-v1/** (verified 2026-08-16:
zero 404s, zero console errors, all routes render, all 88 home images
load, mobile costume correct — bay parked, ground forced white, intro
runs, YOUR PICKS renders). Until cutover there are two public copies of
the same page; the vault's is the one people have the link to.

## THE A/B EXPERIMENT — this session may be its v1 half (seeded 2026-08-16)

Dylan is firing ONE multi-item prompt at TWO sessions: one opened in
the vault (`~/Projects/avrg-site`), one opened HERE. Same list,
different repo memory — the test is whether this repo's scoped docs
carry a real working session. **If your opening prompt is a list of
site changes, this is that run.** The rules:

1. **Branch first: `git checkout -b ab-run` before any edit.** All
   work and commits land on the branch, never `main` — main must stay
   at the port baseline so the compare (and whichever side is not
   kept) unwinds clean. Push nothing; Dylan makes the push calls.
2. **Agents are GREEN-LIT** — Dylan's explicit go-ahead to spawn
   subagents / agent workflows for this run's work.
3. **The vault may be consulted** (it is the archive, as these docs
   already say) — **but LOG EVERY TRIP:** at wrap, list each thing
   retrieved from outside this repo and whether it CHANGED the work.
   That list is the experiment's real product — it tells Dylan what
   belongs in these docs versus where the vault pointer is
   over-inviting.
4. One list item references `avrgbg-buttonflip.png` — staged at
   `site/img/avrgbg-buttonflip.png`, a raw 3009×3375 / 5.2MB brand
   export; web-size it before shipping it.
5. Otherwise work the list like a normal session: desktop-first where
   it applies, the sim for mobile verification, the same laws as ever.

## The porting recipe — vault edits come here

Pre-cutover changes get made in the **vault working copy** (the page
that is actually live) and ported into v1 at session end. Deliberate:
it is the test of whether v1's structure survives real change.

1. Get the delta:
   `git -C ~/Projects/avrg-site diff 762f975..HEAD -- redesign/k-home-dual.html`
2. Apply those hunks to `index.html` here. The two files are
   **identical modulo the path repoints**, so hunk context matches
   unless the hunk itself touches a path.
3. Translate any path the diff introduces:
   `../site/` → `site/` · `media/` → `site/media/` ·
   `../videos/web/` → `site/media/` ·
   `card-lab/canva/` → `site/img/cards/canva/` ·
   `card-lab/cuts/` → `site/img/cards/cuts/` ·
   `../favicon.png` → `favicon.png`
4. **Port any new asset the diff references** — a new canva cutout, a
   new clip, a new photo. v1 ships the live SUBSET (66 of the vault's
   168 canva files), so a new board's card art will NOT already be here.
5. Serve `:8124` (`avrg-v1`) and check the page actually boots — the
   inline-script syntax check in `gotchas.md` first, then the browser.
6. **Update the baseline hash in this file** to the vault's new HEAD.

**Baseline: `762f975`.**

**Port log**
- `9aca992 → 762f975` (2026-08-16) — intro react 3 + the dims/flip card
  pass. 18 hunks, 17 clean and 1 at fuzz 1 (v1's own `RELAY_ON` marker
  comment sits in that hunk's trailing context, in `renderShopAll`).
  No path translation was needed: the flip chip rides the derived
  `m.img`/`m.bot`, so v1's repoints flow through. **The recipe held** —
  v1's divergence from the vault came out byte-identical before and
  after, which is the check worth repeating: diff v1 against the OLD
  vault commit, port, diff against the NEW one, and the two divergences
  must match.

## The cutover checklist — parked, on Dylan's word, in order

1. **Verify the v1 live URL** — the Pages deploy renders, boards load,
   media plays, favicon lands.
2. **Dylan buys the domain** — he wants **avrg.website** and
   **avrg.cards**. His purchase, not ours.
3. **`CNAME` file in this repo + DNS at the registrar**, per the GitHub
   Pages custom-domain docs. No code change is needed for the domain
   itself: `siteUrl()` derives from `location.href`, so every DM/contact
   deep link follows the new address automatically.
4. **Flip the vault repo private.** Its Pages URL dies with it — free
   plans do not serve Pages from private repos. That is the point of
   doing it after step 3, not before.
5. **Future work happens in v1 directly** — the vault-edit→port loop
   ends here. Optionally rename the local folders so the working repo
   takes the familiar path; note that changes Claude's per-project
   memory keying, so the accumulated project memory follows the folder
   name, not the repo.

## Standing constraints

- **Do not wake the scroll relay.** `RELAY_ON = false` is a deliberate
  park (one switch gates the CSS and the machine). Its tuning/feel pass
  and phone translation are post-v1, on his ask.
- **Dylan makes the push calls.** Pushing `main` is publishing.
- **iPad changes are lowest priority and unenumerated** — he checked the
  header on glass ("header looks good") and wants "a few more" changes
  he has not listed. Wait for him to raise them; don't go hunting.
- **Design exploration happens against the VAULT's labs**, which did not
  come across. Ship the result here.
- **The approved surfaces are approved** — the picks page, the select
  ceremony, the mobile pass. Do not reopen without his ask.

## Read these, skip the rest

- `CLAUDE.md` — the index: layout, always-on rules, the docs map.
- `.claude/docs/gotchas.md` — the v1 section at the bottom (port paths,
  the canva subset, the sources-ordering law), then the newest platform
  entries; the pane's rAF wedge is live again, so probe before trusting
  any motion check.
- `.claude/docs/<surface>.md` — whichever surface the task touches.
- `index.html` — **ANCHOR SEARCH ONLY** (~14k lines). Useful anchors:
  `THE INTRO`, `.fveil`, `#logo-draw`, `decodeInto`/`decodeTo`,
  `DIMS_MM`, `renderPicks`, `playMenuSelect`, `RELAY_ON`.

## Parked / later (from the vault's threads)

- ~~His named next tasks (1) intro tweaks (2) the board-dimension
  decode~~ — **BOTH LANDED 2026-08-16 and were PORTED here** (the
  `762f975` port: draw ×2 + seat + specks + bleed, the mobile dims
  decode, the flip chip — records in mobile.md + k-core.md). Awaiting
  his react; decode TIMING/feel tuning may still follow (the lab he
  named is in the vault).
- Thread 1's desktop half (the landing around the draw), thread 2 (home
  collection cards redesign), thread 3's desktop half (drop-row
  navigations still teleport above 941).
- The relay wake; the ORIGINALS RETHINK; the iPad feel pass; the sound
  pass; the browser-compat sweep (Safari vs Chrome).
