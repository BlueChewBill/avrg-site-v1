# Handoff — AVRG site v1 — 2026-08-29 (night)

> (The old vault→v1 porting recipe + the closed A/B trip log live in this file's git history — CLAUDE.md still points here for them.)

## Where we are

THE FRIDAY POLISH ROUND is done and fully pushed (`a1753bf` = origin HEAD, tree clean): the composer four-pack, the grid flip mini (lb-ghost dress + real flip door), the lb counter retired, both lb decode clocks retuned, THE DIMS GRAMMAR (33.0mm × 95.85mm, small units), THE ADD CHIP redesign (three reacts deep — final form: a flat EMPTY mini card in the fv3 dress, want-words retired), and THE SPARK GROWS TIERS (✦ highest on HS 06/07/16/17/18 · black-chip ✱ on HS 08/10/14). CLAUDE.md's Where-things-stand has the one-line index; every change's record is in its owning surface doc. Bench synced three times (CompUI `97d8d35` tip, census 147). Dylan's verdict on the dims/decode work: "look great. really solid change."

**The clock that matters: Dylan says ~ONE DAY left "to get it straight."** His framing at wrap: the remaining changes are **WIRING, not design** — except the LB photos, which are on HIS end (the og sheet material). Expect a finishing session, not an exploring one.

## Next task

**HIS CALL: "next session should start with the sun / board grow check in."** That's the standing sun-feel thread from THE SUNDAY DISPATCH (open-threads): the `?sun=` collide — build directions 2 + 3 so he can FEEL them (the faster entry arm · the warm ring) against the shipped feel, plus a check-in on the board hover grow. Done = variants served side-by-side (the `?sun=` param idiom), his pick baked, bench synced (the SUN wing is charted — sixteen channels; remember the T7d note: on WebKit the sun writes transform/opacity on `#lb-shadow`, never filter on `#lb-big`, and `sun-grow`'s 1.08 is hand-restated in the T7d CSS pair — a retune carries both).

Then his wiring list, as he dishes it. Known wiring candidates already on the books: **meta tags (STILL SUNDAY-CRITICAL AND UNSTARTED — no link-preview card exists; raise it before he posts the URL anywhere)**, the og sheet export+wire once his photo compositions land (the Figma → `site/img/og/` → `OG_SHEETS` loop, lightbox.md's THE ZONE LANDS is the recipe), and the splitforms key if the long form is to go live.

## Read these, skip the rest

- `.claude/docs/open-threads.md` — THE SUNDAY DISPATCH section (the sun-feel three-way's exact directions + minted decisions) and the quality-identifiers item (marks state after tonight).
- `.claude/docs/lightbox.md` — the sun section + T7d (THE SHADOW BECOMES ITS OWN ELEMENT — read before touching ANY sun channel) + THE ZONE LANDS (if og wiring comes up).
- `.claude/docs/gotchas.md` — before ANY browser verification (pane's dead rAF/RO/IO family; the private-Chrome CDP escape — private port + private profile, check /json/list ownership; motion verdicts need real Chrome, Safari bugs need his real Safari via safaridriver).
- `bench/manifest/avrg.json` — the SUN wing before retuning (the engine caveat: a Safari-hosted stage reads `#lb-big` filter as `none` BY DESIGN).
- `git log --oneline -25` — tonight's story; every record also sits in its owning doc.

Everything else is NOT needed until a task leads there. The context pack (`context/card.md`) is current at the merge; re-run `build_context.py` after any index.html change.

## Context that isn't in the code

- **Pushing was blanket-authorized tonight** ("full trust. push!") — but that was THIS session's grant; next session, pushes are his call again until he says otherwise.
- **He walks the whole site tomorrow.** Fast-and-loose screenshots incoming; tonight they were gold — an annotated crop was enough to scope every ticket. Build variants, let him pick; his three-react refinement of the add chip (stack → flat card → empty card) is the pattern: ship each react quickly, he converges fast.
- **The add-chip class is a lie kept on purpose:** the glyph is a mini CARD but the class/const stay `.fstack`/`STACKSVG` — the bench's `chip-stack-size` anchor and nine colour rules point at them; renaming is churn with no payoff. Recorded in the code comment.
- **The dims grammar's load-bearing trick:** the plain string ("33.0mm × 95.85mm") is what every dataset/comparison holds; the small-mm is write-time markup (`dimsWrite`). textContent reads identically through the spans. New dims writers must go through `dimsWrite`, and card-to-card text copies must copy innerHTML (`copyCardTexts` does).
- **Tier order IS rank order in JSPARK** (1 accent ✱ unheld · 2 black-chip ✱ · 3 ✦ highest) — renumbered once already to keep that true; keep it true. Mark tooltips are placeholders; the tag LANGUAGE + touch surfacing (lb) are still the open DM conversation.
- **Verification harness of the night:** the stale http.server on :8124 serves this repo fine (don't fight it); private headless Chrome on an own port ≥9400 + own profile is the law (two collisions avoided, one Chrome got killed by a sibling's cleanup anyway — relaunching is cheap).
- **Agent finds parked, not touched:** the desktop drawer's shelf cards are NOT pre-dressed (the "deck cards stay dressed" rule is phone-gated — cards.md's law reads unqualified; doc or gate is wrong); `landWants` writes to a surface that's always indeck-hidden; `build_context.py` hard-crashes on renamed JS consts (guarded for STACKSVG only).
- **#picon's `.deckmark` is the LAST copy of the deck-mark artwork** — the parked deckmark-cleanup chip (`silly-lamport-eced3f` worktree, still unmerged) must not delete it blindly; its open-threads line carries the caveat now.
- The chip agent's worktree (`agent-a1790076462b98696`) is merged but harness-locked — ignore it or clean it when the lock drops.

## Parked / later

- The weekend big three (og sheets ×6 + bg-removal redo · the 15–25 board batch — ORDERING LAW before touching sources/ · the spark/tags DM design — now half-built, tiers live).
- The taste calls he never got to: +List on-state border accent · stack-seat optics.
- Safari pass proper (his click-through of remaining desktop surfaces).
- The chip-hover answer option (inking the mini card's front on `.fc-list:hover`) — offered, no verdict.
- The cosmetic code cleanups (bar-inset dedup, renderPicks double-write, populate's dead branch, `.inked` no-op).
- iPad wide-touch resolution (lowest priority, unenumerated).
