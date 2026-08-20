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

## THE A/B EXPERIMENT — RAN AND CLOSED (2026-08-16)

The same 12-item prompt ran in both repos on parallel `ab-run`
branches. **The vault's implementation won** ("vaults changes win by
some pixels") and was ported here whole (the port-log entry below);
this repo's losing branch is DELETED, its record preserved here.

**What this repo's run proved:** the scoped docs carried **11 of 12
items without leaving the repo**. The one exception was item 2 — the
decode-lab knob grammar was unimplementable without reading the
vault's `redesign/decode-slowmo.html` end to end, and the cure is now
a permanent pointer in lightbox.md (the lab is the authority for the
collapse decode's dials). Also surfaced: the VAULT's own labs.md never
catalogued that lab — the lean repo's scout found a hole in the rich
repo's docs.

**The trip log (everything the run retrieved from outside this repo):**
- `vault redesign/` (ls) — located the decode lab. CHANGED THE WORK.
- `vault redesign/decode-slowmo.html` (read end to end) — THE trip:
  every phrase in item 2 is a dial there. Item 2 was UNIMPLEMENTABLE
  without it. The prescribed doc line now exists (lightbox.md).
- `vault .claude/docs/labs.md` (grep) — no decode-slowmo entry;
  confirmed the lab file is the sole authority. Did not change work.
- `vault .claude/docs/open-threads.md` (grep) — context only.
Nothing else left the repo.

**The losing run, for the record** (10 commits, deleted branch): all
12 implemented; its distinctive answers were three collideable tile
variants behind a `?tiles=` switch (the vault's single fv3 re-dress
won), a scrollspy it called "the spy inside the sleeping relay"
(convergent with the vault's watcher — BOTH independently refused to
wake RELAY_ON), and an identical 80vw call on item 6. Its four
verification-trap gotchas were harvested into gotchas.md; the rest
retired with the branch.

## The porting recipe — vault edits come here

Pre-cutover changes get made in the **vault working copy** (the page
that is actually live) and ported into v1 at session end. Deliberate:
it is the test of whether v1's structure survives real change.

1. Get the delta (`<baseline>` = the hash recorded below, not a fixed one):
   `git -C ~/Projects/avrg-site diff <baseline>..HEAD -- redesign/k-home-dual.html`
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

**Baseline: `9170375`.**

**Port log**
- `c54a2a2` (2026-08-20) — **THE ORIGINALS GO DEEP**, commit-scoped port (not
  a baseline diff): the og-scoped lb photos+info (see lightbox.md's entry).
  4 hunks, 4 clean, no new paths (CUT/IMG are runtime helpers, already
  repointed). **NOTE: the baseline hash below is STALE** — the 2026-08-19
  ports (S1/S2, the flip mark) were cherry-picked without updating it, and a
  translated full-file diff now measures ~2010 divergent lines: partly v1's
  own founding cleanups (permanent by design), partly what looks like
  UNPORTED vault work (the Satoshi-Light face + tagline tick from
  2026-08-17, the deck-mark T3/T4 retirement). A reconciliation pass — walk
  the vault log since `9170375`, classify each commit ported/pending/
  vault-only — is an open chore; until then port commit-scoped, as this one
  and the 08-19 ports did.
- `762f975 → 9170375` (2026-08-16) — **the A/B experiment's WINNER**: the
  vault half's all-12 implementation (`e8774a5`) plus the chevron re-seat
  on his react (`9170375`). 49 hunks, **49 clean** — no fuzz, no offsets,
  no rejects; the `RELAY_ON` marker that fuzzed last time sat outside
  this delta. **One path translated**, the only one the diff introduces:
  the blank-card art, `../site/img/avrgbg-buttonflip.png` →
  `site/img/avrgbg-buttonflip.png`. **The asset itself came across** —
  the vault web-sized the raw 5.2MB export to 413201 bytes (713×800);
  both repos now hold identical bytes (md5 `8d044a6e…`), and main's
  5.2MB original is gone. The divergence check held again: v1-vs-vault
  came out identical before and after **except the one expected new
  pair** (the buttonflip repoint), which is what a newly-introduced path
  is supposed to add. Verified headless (private CDP Chrome, own port +
  profile — the MCP profile was another session's): zero console errors,
  exceptions, failed requests and boot errors on all six routes; and the
  1440×790 lightbox measured **byte-for-byte the same as the vault's own
  served page** — card 265px, dims line identical, both chevrons seated
  18×30 at top 402 / left 525·896.
  **Note:** main carries the winner now; the losing `ab-run` was
  harvested (trip log + verification gotchas above/in gotchas.md) and
  deleted. The winner's surface laws are appended to cards / contact-
  composer / header-bar / lightbox / mobile / home-shop docs.
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
