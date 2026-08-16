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

## The porting recipe — vault edits come here

Pre-cutover changes get made in the **vault working copy** (the page
that is actually live) and ported into v1 at session end. Deliberate:
it is the test of whether v1's structure survives real change.

1. Get the delta:
   `git -C ~/Projects/avrg-site diff 9aca992..HEAD -- redesign/k-home-dual.html`
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

**Baseline: `9aca992`.** Vault HEAD was the same commit at handoff time,
so the delta is currently EMPTY — the first port has nothing to carry.

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

- His named next tasks, in his order: **(1) slight INTRO TWEAKS —
  timing and size** (every clock is a named knob in the intro driver);
  **(2) the BOARD-DIMENSION DECODE + decode timing across the site** —
  he said he'll consult an already-built lab for that one, so let HIM
  name it (the labs are in the vault).
- Thread 1's desktop half (the landing around the draw), thread 2 (home
  collection cards redesign), thread 3's desktop half (drop-row
  navigations still teleport above 941).
- The relay wake; the ORIGINALS RETHINK; the iPad feel pass; the sound
  pass; the browser-compat sweep (Safari vs Chrome).
