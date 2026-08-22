# Handoff — AVRG site v1 — 2026-08-22 (LAUNCH DAY)

> The 2026-08-16 handoff this file replaces (the port recipe, the port
> baseline hash `9aca992`, the closed A/B experiment record) lives in this
> file's git history — CLAUDE.md's references to "the HANDOFF" for that
> history mean the pre-08-22 versions.

## Where we are

Yesterday (08-21) was the big pre-launch session, fully landed and
verified, **NOTHING PUSHED — main is 34+ commits ahead of origin, and
pushing IS publishing the launch.** What landed:

- **THE LANDING BAKED** — the desktop arrival ceremony (draw big at .42
  viewport, ×2 draw, sections land originals→shaped→routed, video from
  left, clamp print below the fold) is now the default home arrival.
  Thread 1's desktop half is CLOSED. Record: k-core.md THE LANDING.
- **THE SOUND PASS** — one gate on the synth kit: phone fully silent
  except video (Dylan's ruling), per-voice cooldown, one-gesture-one-voice
  (deck add AND the lb toss), lb-open click settle-synced. Record: the new
  `.claude/docs/sounds.md`.
- **THE INTRO BELT** — the phone load intro can no longer strand a sealed
  white page on a dead main script (Dylan's real stuck-page bug, reproduced
  then killed; 13s self-contained belt in the arm). Record: mobile.md.
- **THE BENCH LANDING WING** — 22 params charted in CompUI (commits
  07285b6 → 9b66146), replay action, resizable stage/params splitter
  (his ask). The wing survives the bake; every desktop stage load now arms.
- **DOMAINS** — avrg.cards (primary, CNAME committed) + avrg.website
  (301 forwarder, the bio joke). DNS live and verified at Porkbun.

## Next task

**Dylan's ruling: the ORIGINALS LB round is TOP PRIORITY.** The
anatomy-sheet direction from his PEACH/PIRO mockup: board-first spec
sheet — big deck photo, numbered callouts doing the explaining, GRIP/TOP
+ PROFILE/CONCAVE tiles, bottom status bar (available · name · one-of-one
· dims · WANT). It replaces the card-center og spread as the destination;
the card stays the doorway. Done for round 1 = a static dress collision
on Peach/Piro's REAL assets (2 anatomy variants vs the shipped spread),
his react. Then: data wiring to per-board folders, og-wing re-chart
(bench law — the og wings change shape → cartographer dispatch), og
mobile view.

He is organizing per-board folders (outside the repo, likely Desktop):
`anatomy.jpg · grip.jpg · profile.jpg · angle.jpg · clip.mp4 · info.txt`
with info.txt lines `NAME / DIMS / 1: / 2: / 3: / COPY`. If the folders
line up, the LB becomes data wiring. Ask if they're ready; don't block
on them for the dress collision (Peach/Piro has shippable assets in
`sources/originals/` + `site/img/`).

## Pre-push checklist (the cutover — HIS call, target today ~noon)

1. Page `<title>` still says "dual ground" — outward-facing, fix before push.
2. og per-board clips: ONE stand-in cut serves all six boards — resolve
   or gate the seat (open-threads.md's og entry).
3. Push main → GH Pages binds avrg.cards (CNAME is in) → repo Settings →
   Pages → Enforce HTTPS once the cert issues → verify the live URL.
4. Flip the vault repo (`bluechewbill/avrg-site`) private — its Pages URL
   dies with it. Future work continues here.

## Read these, skip the rest

- `.claude/docs/lightbox.md` — the og spread record; the surface the round redesigns.
- `.claude/docs/open-threads.md` — the ORIGINALS RETHINK history ("they
  need a lot of explaining" is the thesis the anatomy sheet answers).
- `context/card.md` — the card pack (regenerated 08-21) for card-adjacent work.
- `.claude/docs/k-core.md` (THE LANDING section) — only if touching home.
- `.claude/docs/sounds.md` — only if touching sounds (the law lives there).

Everything else is NOT needed for the originals round.

## Context that isn't in the code

- **Dylan-speak:** "routed" = the classic line (hand-shaped vs routed).
- **Landing laws:** drawSpeed ships as a ride-start SMIL rescale — NEVER
  bake the SVG clocks (the phone intro shares the SVG and derives its
  beats from them). The clamp print below the fold is RULED a fun find —
  don't "fix" it upward. Open design Q, low priority: the mid-session
  home-return draw plays base speed while the arrival draws ×2 — one-liner
  if he wants them matched.
- **Sounds:** kbonk stays parked on his word. The lb-open click moved
  ~130ms later (true settle) — he hasn't explicitly blessed the listen.
- **Bench:** `land-veil-dur` stays LOCKED (a live driver needs a dual-path
  applier Dylan would have to order). A deliberately-slowed bench ride can
  be swept by the arm's 12s belt mid-ride (recorded find, harmless shipped).
- **Verification laws (all in gotchas.md / sounds.md):** parallel CDP
  harnesses need PRIVATE debug ports; parallel agents namespace their
  scratchpad dirs; double-loading the 900KB page wedges a headless
  renderer; a shallow deck (<3 cards) hides re-stack sound regressions.

## Parked / later

- **Blur-on-fades pass** — never started; the belt edge fades are
  `::before/::after` overlays that can take backdrop-filter + a mask
  feather; `.topbar`/`.fveil` are the in-file precedent. Collide 2–3
  strengths.
- **Calipers** — CL 03/06/08/12/16/19/26 + originals + resale → `DIMS_MM`
  type-in session (he dictates).
- **New boards** — photos land in `sources/` (ORDERING LAW: sort LAST),
  then `build_site.py`.
- **About page** — vault `about/ABOUT-BUILD.md`: 9 beats, his trim target
  5–6; media exists for beats 4/5/6/8; his hunt is 1/2/3/7/9;
  `Automatic.MP4` needs a web-compressed cut. Desktop one-screen, phone
  vertical scroll. Low priority, his words.
- **Chips raised, fate unknown** (re-raise if wanted): seatFly landing-rect
  guard (card arcs to corner if deck re-renders mid-add-flight); closeLb's
  430ms teardown vs the .55s flight.
- **Small wrinkles on record:** clearIntro doesn't clear the pose transform
  (the belt covers the user-visible case); the phone intro transiently
  overflows horizontally ~900ms in (settles, pre-existing); the arm belt
  doesn't cancel driver timers (bench-only).
- **Post-launch tier:** the dark base CSS proven-identical sweep; the
  Safari/browser-compat sweep; iPad pass; waking the relay (his word only);
  the three-scheme ground picker.
