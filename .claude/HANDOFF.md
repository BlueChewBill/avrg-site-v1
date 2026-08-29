# Handoff — AVRG site v1 — 2026-08-28 (night)

> (The old vault→v1 porting recipe + the closed A/B trip log that used to live here are in this file's git history — CLAUDE.md still points here for them.)

## Where we are

THE SUNDAY DISPATCH is done and live: eleven tickets (five little-fixes + four from Dylan's real-glass round + a six-angle review's fix stack + the bench sync) all merged and **pushed to avrg.cards** at `baed119`+. Dylan's phone test came back all-green (grid IDs, the AVRG-then-land beat, whole-card pinch, no shadow blob). **Mac Safari's shadow blob survived the first cure** → the **T7b escalation agent was IN FLIGHT when this session wrapped**, in worktree `.claude/worktrees/agent-a87f778c12e97efaa`. Dylan opens the next session after it lands.

## Next task

**T7d IS THE STANDING CURE AND IS PUSHED** — the bug got NAMED (WebKit #207586, the filter fed a partial source rect on incremental repaint; trunk-fixed 2026-05, ships ~Safari 27 = the recorded EXIT condition for the whole WebKit fork) and the endorsed structural cure landed: on WebKit the lb board shadow is its own `#lb-shadow` ghost img (filter frozen at `brightness(0)`, moved by transform/opacity; the real img's drop-shadow is off there). Verified on Dylan's REAL Safari (mechanism proof: no drop-shadow raster exists at any beat), Chrome pixel-inert, phone path untouched. **The sun's WebKit write target moved (filter-on-#lb-big → transform/opacity-on-#lb-shadow) — a sun-wing bench re-chart was dispatched at wrap time; confirm it landed (CompUI log).** Two taste details for his glass: the Safari hover shadow now GLIDES with the grow (transform is the safe channel — T7's stepped look is two deletable transition lines in the T7d block if he prefers the snap), and a possible half-pixel board shift on Safari (sub-pixel snapping without the filter). **HIS VERDICT LANDED, SAME SESSION: "its clean!" — THE SHADOW THREAD IS CLOSED.** The taste details (glide-vs-snap, half-pixel) drew no objection. The sun-wing bench re-chart LANDED (CompUI `c40e251`, C12 record; census 145, zero value drift — all sixteen SUN channels verified against the served page). Three notes it left: (1) a tuner on a Safari-hosted bench stage will see `#lb-big`'s filter as `none` BY DESIGN — check the wing's engine caveat before declaring the sun dead; (2) a latent land-mine is recorded: if a SOLD hero ever becomes real, the `sold-filter` rule would put a drop-shadow back on the img on the one engine that can't repaint it — currently inert (0 matching elements), but it's the first thing to check if the blob ever returns; (3) `sun-grow`'s 1.08 is hand-restated in the T7d CSS pair — a retune must carry both (the manifest row says where); binding them is Dylan's call.
~~superseded lineage:~~ **T7c SUPERSEDED T7b AND WAS PUSHED** (merge after `2dbc874`): never-swap — WebKit parks the sun's shadow at the CSS rest value (the cqw string) so the corrupt authority-swap beat never exists; T7b's nudge retired (it was the residual-lines source). **Verified on Dylan's REAL Safari via safaridriver — Remote Automation is now ON on his Mac and his iPhone's Web Inspector is ON** (memory + gotchas T7c entry carry the recipe; harnesses in the old session scratchpad t7c/). Dylan watched the verification run live and his early read was "looks fixed" — the next session still opens on his post-push hard-refresh verdict. One lockstep law minted: `SUN_PARK` (the JS const) must match `.d7f .frame img`'s rest filter — commented at both. Remaining Safari suspect if a blob EVER appears at lb close: `.softout` still transitions filter (phone-only arm today, structurally unreachable — documented).
~~T7b history:~~ **T7b LANDED AND WAS PUSHED** (merge after `1d64d20`; the fix: "SAFARI'S RASTER HEALS" — WebKit-only, at sun release the board img's layer is torn down and rebuilt with no painted frame between, forcing the from-scratch repaint his glass proved clean; Chrome provably inert, SUN untouched, no bench change). The task is: **collect Dylan's Mac Safari verdict** — hover a lightbox card (HS 04 was his repro), leave, watch the settle, repeat a few cycles. If clean → done, close the thread in gotchas. If the blob survives → the agent's report names the escalation ladder: (b) never-swap/park-the-inline-filter with a sold-board carve-out, then stage-2 shadow-as-element; ALSO worth asking him to flip Safari's Develop → "Allow remote automation" — a working safaridriver harness for his REAL Safari is saved in the old session's scratchpad (`t7b/safari-probe.js` pattern; rebuild it if gone) and would give this bug family a true repro rig. One extra suspect his report flagged: `.softout` (lb close) still transitions filter .93s in WebKit — if he ever sees a blob at lb CLOSE, that's the fix (extend T7's prune to it).

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
