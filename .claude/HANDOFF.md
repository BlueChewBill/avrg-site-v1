# Handoff — AVRG site v1 — 2026-08-28 (night)

> (The old vault→v1 porting recipe + the closed A/B trip log that used to live here are in this file's git history — CLAUDE.md still points here for them.)

## Where we are

THE SUNDAY DISPATCH is done and live: eleven tickets (five little-fixes + four from Dylan's real-glass round + a six-angle review's fix stack + the bench sync) all merged and **pushed to avrg.cards** at `baed119`+. Dylan's phone test came back all-green (grid IDs, the AVRG-then-land beat, whole-card pinch, no shadow blob). **Mac Safari's shadow blob survived the first cure** → the **T7b escalation agent was IN FLIGHT when this session wrapped**, in worktree `.claude/worktrees/agent-a87f778c12e97efaa`. Dylan opens the next session after it lands.

## Next task

**Land T7b.** If the wrap session already merged/pushed it (check `git log --oneline -5` for a "T7b" merge), the task is just: collect Dylan's Safari re-test verdict and act on it. If the worktree still sits unmerged: read the agent's report (task output under the previous session's tasks dir if reachable, else the worktree's commit message + diff), review, merge, syntax-check (the gotchas one-liner), push on Dylan's word, then he tests Mac Safari — hover a lightbox card, leave, watch the settle. Done = soft board-shaped shadow at rest after hover-leave cycles on his glass. His diagnostics that steered it: the blob is RECTANGULAR (the img's box, alpha dropped) and appears ONLY at the hover-leave settle — the suspect is Safari re-rasterizing at the inline→stock filter swap; the first-line cure was "never clear the inline filter on WebKit — park it at stock," fallback shadow-as-element (WebKit-scoped, Chrome byte-identical, SUN values untouched, write-target change = bench note).

Then, his named queue for the session: **the `?sun=` collide** (build directions 2+3 so he can feel them: faster entry arm · the warm ring — see open-threads THE SUNDAY DISPATCH), **the taste calls** (+List on-state border accent · stack-seat optics), and **more bug squashing / final functional tuning he's staring at** — he'll dish these live; expect fast-and-loose screenshots, they were gold tonight.

## Read these, skip the rest

- `.claude/docs/open-threads.md` — THE SUNDAY DISPATCH section (the minted decisions incl. the sun-feel three-way) + THE WEEKEND QUEUE (the standing big three).
- `.claude/docs/lightbox.md` — the lb sun section + THE ZONE entries, needed for T7b review and the sun collide.
- `.claude/docs/gotchas.md` — before ANY browser verification (the pane's dead rAF/RO/IO family; the two-sessions private-Chrome CDP escape; the T7 Safari lessons).
- `git log --oneline -30` — tonight's story in commit messages; every ticket's record also sits in its owning surface doc.

Everything else in the repo is NOT needed until a task leads there. The context pack (`context/card.md`) is regenerated and current at `baed119`.

## Context that isn't in the code

- **Pushing main is publishing.** Dylan made three push calls tonight; keep it his call.
- **The sun "regression" was disproved by measurement** — og on-card == classic exactly; his baseline was the flank bug's overdrive. Don't re-litigate; build the collide and let him feel it.
- **The ID-flip grammar as ruled:** desktop rest AVRG → hover decodes to ID; open lb shows ID (its landing IS the decode); touch grids rest the ID (no hover to earn it); phone lb shows AVRG until touchdown. Wide-touch (hover:none ≥941) rests the ID directly — the chip is that viewport's only ID read.
- **Verification tooling law of the night:** parallel agents MUST use private ports + private Chrome profiles (three collisions happened anyway — check `/json/list` ownership); the iOS sim's `touch2_path` two-finger injection never reaches page handlers (CDP touch emulation is the pinch path); stale `http.server`s squat 8242/8244 on this Mac.
- **Meta tags stay Sunday-critical and unstarted** (his explicit "for later") — no link-preview card exists; raise it before he posts.
- **The deckmark cleanup chip** (`silly-lamport-eced3f` worktree) runs in its own session — merge its branch when it reports, don't redo it.
- Style of the night that worked: tight tickets with don't-touch lists + real-engine verification evidence; he reacts to built things and screenshots, never specs.

## Parked / later

- The weekend queue's big three (og sheets ×6 + bg-removal redo, the 15–25 board batch — ORDERING LAW, the spark/tags DM design) — need him, in his order.
- The `--barInset` dedup + a seat-inset bench dial (cartographer find, cosmetic).
- renderPicks' double-container write + missing self-gate signature (review noted, non-urgent since the dealt-away/eager fixes).
- The `.inked` no-op class on the bay + its stale comment (review find, cosmetic).
- populate's dead touch pos-decode branch (`LB !== "deck"` is constant-false) — cleanup candidate.
- Safari pass proper (his click-through of remaining desktop surfaces) — tonight covered logo + shadow only.
