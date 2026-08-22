# Sound — the kit, the gate, the trigger inventory
Every noise the page makes: three synthesized voices, one gate that decides whether they happen, and the list of beats that call them. Haptics live here too, because the question "why did that not make a sound" is usually about them.
> **AUTHORED 2026-08-21 (THE SOUND PASS).** The kit itself dates to 2026-07/08 and its react history is scattered through the surface docs that own each beat — [deck-drawer.md](deck-drawer.md) for the seat and the flights, [lightbox.md](lightbox.md) for the exchange and the open, [contact-composer.md](contact-composer.md) for the stamp and the seal, [mobile.md](mobile.md) for the phone dialect. This file is the CROSS-SURFACE record: it owns the kit and the gate, not the choreography. Anchors are NAMES, never line numbers.

## The kit

One contiguous block in `index.html`, sitting just under `landBeat` and `dockActive`. **Everything is synthesized through one shared `AudioContext` — there is not a single audio file on the site, and adding one would be a new decision, not an extension.**

- **`SND_KEY` / `SNDON`** — the storage gate (`localStorage["avrg-k-snd"]`, defaults `"on"`). **There is no mute UI.** The Snd row went with the ground switcher on 2026-08-01 ("it will get a site button in time"), so the gate stays in the code and every voice still honours it; a browser that was muted before the row went stays muted. The pin is the DEFAULT, not an override.
- **`kctx()`** — lazily builds the shared context and `resume()`s it if suspended. Voices fire outside the click's gesture window (setTimeout / rAF), so the resume rides sticky activation rather than the gesture itself.
- **`kthunk()`** — the low sine drop. The dock seat, the object landing.
- **`kclick()`** — a 10ms filtered noise tick over a small triangle pitch-drop. **A button press, not an object drop** — that distinction is the whole design of the voice.
- **`kbonk()`** — THE NO. Two short low blips through a lowpass: deliberately the least glamorous thing in the kit, because a blank field is a "not yet", not a failure. **UNCALLED — see "The no that has nothing to say" below.**
- **`buzz(ms)`** — `navigator.vibrate`, fire-and-forget. **Not a voice.** It is not gated by `SNDON` and it is not gated by the phone rule; iOS has no web haptics at all and never will until Apple ships an API (the 2026-08-07 switch-input side door is CLOSED, do not re-add it).
- **`landBeat(card)`** — not a voice, a BEAT: the panel press class plus `kclick()`. Early-returns on `reduced`.

## THE GATE (2026-08-21)

`sndOk(voice)` — every synth voice's first line, so there is one place that answers "does a sound happen". Three rules, in order:

1. **`SNDON`**, unchanged from before.
2. **THE PHONE IS SILENT — and this SILENCED live paths, it did not merely codify a habit.** `dockActive()` (the site's own `matchMedia("(max-width: 940px)")` line) → the voice returns silently. **Dylan's ruling, 2026-08-21: the phone makes no sound but video.** Read LIVE at fire time, never cached at boot — a window dragged across 940 changes dialect with it, the same law `renderLisst` obeys.

   The phone was already silent on the paths that were *authored* silent — `pickCatch`'s landing (silent + a buzz), the soft return, the slide exchange answering in fills. **But three phone voices were LIVE and the gate took them.** Measured on the served page at a ≤940 viewport, gate removed vs. gate on:

   | phone path | pre-gate | now |
   |---|---|---|
   | deck remove, the ✕ → `mobileExitFly`'s re-stack settle | click @+321ms | silent |
   | shop/lisst chip uncheck → `renderBay`'s re-stack settle | click @+320ms | silent |
   | lightbox open flip | click @+589ms | silent |
   | mobile add (`pickCatch`) | already silent | silent |

   The first of those was DOCUMENTED as deliberate — `mobileExitFly`'s comment read "its settle click is the remove's one sound". That comment is now struck through in the file with the ruling next to it. **This is a real behaviour change on the phone, made on purpose**, not a no-op tidy — and the two re-stack paths sit on the "keep the voice" list below, which is therefore **desktop-only in effect**. The motion and `buzz()` carry those gestures on the phone now.

   The gate also turns the absence into a rule going forward, so a new call site cannot leak percussion onto the phone by forgetting.
3. **ONE VOICE, ONE COOLDOWN — 100ms, PER VOICE.** Deliberately not global: the composer's seal `kthunk` and stamp `kclick` are a designed pair ~615ms apart and both must land, and any future two-voice beat must survive too. What the cooldown stops is the same voice re-firing on top of itself.

**`buzz()` is outside the gate entirely** and stays that way. A muted Android still taps back; the phone keeps its haptics while it loses its percussion. Video elements are also outside — `#vlb`'s clips keep their native audio and their unmute.

## ONE GESTURE, ONE VOICE — the double-clicks (2026-08-21, Dylan's catch + the fix round)

**THE LAW: a gesture gets one voice, and the LANDING owns it.** Two beats can each be correct in isolation and still be a bug together, because a beat only knows its own choreography. Only the thing that starts a gesture knows another beat is already booked — so this is always a FLAG passed by the mover, never a timing window. Both instances measured were ~370-400ms apart, far outside any cooldown.

**1. The deck add (his catch).** `seatFly` renders the preseat — which re-stacks the column, and `renderBay`'s FLIP replay answers its settle with a `kclick` at 320ms — and then the flight's own `landBeat` fires at the seat 680ms in. **Measured: 8121ms and 8489ms, 368ms apart.** Fixed with `bayQuiet` + `renderBayQuiet()`: the mover raises the flag around its own render and the settle sits that one out.

**2. The lightbox toss into the deck** (found in the fix-round review). A desktop drag from an open inspection into the deck runs `seatFly` (landing beat at `DRAG_TUNE.addDur`, ~500ms) AND `tossExchange` behind it (settle `kclick` at `g.T.xDur`, ~900ms). **Measured: 393ms apart.** Fixed with an optional `quiet` argument on `tossExchange` — it has exactly ONE call site, the toss branch, so the argument is risk-free. The caller passes `seatFly`'s return value, so **a toss where nothing seated keeps its exchange voice** and is not left silent.

Note the two mechanisms differ on purpose: `renderBay` has ~20 callers so it takes a flag set around the call; `tossExchange` has one, so it takes a plain argument. Neither is a heuristic.

**Quiet (a landing beat already answers):** `seatFly`'s preseat render and its bail render (the add) · `homeFly`'s ON-STAGE branch (the remove that flies back to a visible shop slot) · `tossExchange` when called from the toss with a seat coming.

**Loud — these re-stacks ARE their gesture's one sound, do not quiet them.** *(All desktop-only in effect since the phone rule — see THE GATE.)* The shop/lisst chip uncheck (`else renderBay()`, membership only, nothing flies) · the arrow-press exchange (`deckExchange` — a different function from `tossExchange`, with no landing of its own) · the lb un-deck drag (`d.kind === "deck"` from the lb — the card springs back to the sheet, quiet by design) · `homeFly`'s OFF-STAGE branch and `mobileExitFly` (nothing lands on screen, so the re-stack is the whole sound) · the picks-page removes.

### The undone add lands silent — a ruling, not an oversight

`seatFly`'s flight callback bails before `landBeat` when the preseat is gone (`!seated`), and the re-stack that would have spoken was quieted on the promise of that landing. **Ruled 2026-08-21: silence is correct there.** The seat vanishes because membership went away mid-flight — in practice the chip was un-checked in the air — and *that* gesture already spoke: its own re-stack is a loud render. Measured: add at t0, uncheck at +220ms, **one click at +550ms** (the uncheck's settle), then nothing at the +680ms non-landing. A beat at the landing would be a second click ~130ms behind the first and would announce an arrival that never happened. The same holds for `seatFly`'s synchronous `!item` bail — nothing flew, and it returns `false` so the toss branch knows to keep its own voice.

## THE SOUND LANDS WITH THE THING — settle-sync (2026-08-21)

`onSettle(el, prop, fn, fallback)`: fire on the element's own `transitionend`, timer as fallback only, first through wins. Scoped to `e.target === el` because **transitionend bubbles** and the card's children transition transform too.

**AND IT MUST NOT ADOPT SOMEONE ELSE'S LANDING** (fix round, 2026-08-21). `lbCard` is shared furniture: `stripJump`, `step`, `slideExchange` and the swipe all re-write the same `transform` on the same node. Interrupt the open flip and its `.55s` transition is **cancelled**, while the interrupting `.18s` one runs to a real `transitionend` — same target, same property — which a bare listener happily adopts. Measured on the served page, opening a lightbox and hitting the strip 150ms in:

```
transitionrun@5421  transitioncancel@5550  transitionrun@5550  transitionend@5717
   -> click FIRED at +329ms (abs 5718), mid-swap, via the onSettle listener
```

The lb's own guard tokens cannot catch this — a strip jump never touches `lbOpenN`, `lbFlying` or `lb.hidden`. **The fix: a `transitioncancel` listener that DISARMS without firing.** An interrupted flight has no settle to ride, so it falls back to the timer — which is exactly what the bare timer did before any of this. Same walk after: `click at +702ms via late`, the fallback. The timer is also `clearTimeout`ed when the real event lands, so the disarm is symmetric in both directions.

- **The lb open click** rode a flat `setTimeout(…, 430)` while `.lb-card`'s transform transition is **`.55s`** — it had been firing ~120ms BEFORE the card came to rest, and nothing in the file connected the two numbers. Now on `onSettle(lbCard, "transform", …, 700)`. Measured: the click moved from **+431ms to +563/581ms** after the press. The tokening (`lbOpenN`, `lbFlying`) is unchanged — a close or re-open inside the flight still voids it.
- **The bay re-stack click KEEPS its 320ms timer**, audited and left alone. 320 is not a guess: it is the `.3s` FLIP transition plus the two rAFs that arm it, and the same 320 is what the per-element cleanup runs on. Measured, the moved item's `transitionend` lands within a frame of the timer (`end@8118` vs the click at 8121) — riding it would move the beat ~0-20ms and hand it to an event the cleanup is racing. Re-timing that cleanup would be choreography, not sound.

**The general law:** a voice pinned to a bare constant drifts the moment its choreography is retuned, and nothing warns you. Derive it from the animation (the exchange settles already do — they ride `g.T.xDur`), ride the flight's completion callback (every `bayFlight` landing does), or ride `transitionend` with a generous fallback. A hardcoded number is only acceptable where it is provably the animation's own arithmetic, and then it should say so.

## The no that has nothing to say — PARKED, not unfinished

**`kbonk` is fully built and never called. THIS IS SETTLED — Dylan's ruling, 2026-08-21: _"its from long ago, forgot what it was even for at this point. its okay to leave for now."_ Do not treat the uncalled voice as a loose end to wire up.**

The beat it was written for — the composer's required-field rejection, complete with a gesture half (`.bdm-prev.nope` + `@keyframes envNope`, the card throwing a few px TOWARD the offending field) — **retired with the tray**. The tombstone is at `bdmHref`: *"bdmMissing/bdmNope retired with the tray — a reddit DM has no required field, so nothing can arrive half-addressed."* The CSS is orphaned for the same reason.

The site's one live required field is the lisst page's `#inq-handle`, which rejects through the browser's own native validation bubble. Giving that a voice would be a new sound on a surface that never had one — a design call, and one Dylan has parked. The voice and its gesture keep their seats: written, tuned, and one call away if a real "no" ever turns up.

## Trigger inventory (2026-08-21)

Every place the page makes a synthesized sound. Anchors are function names. **Everything below is desktop-only in effect — the gate mutes all of it at ≤940.**

| beat | voice | where | when it fires |
|---|---|---|---|
| deck exchange settle (the arrow press) | `kclick` | `deckExchange` | `setTimeout(…, dur)`, `dur = g.T.xDur` — derived. Always loud: this gesture has no landing of its own |
| toss exchange settle | `kclick` | `tossExchange` | same, derived — **but quiet when the toss seats a card**, whose landing owns the gesture (one call site passes the flag) |
| lb OPEN flight landing | `kclick` | `openLb` | `onSettle(lbCard, "transform")`, 700ms fallback; disarms on `transitioncancel` so an interrupted flip falls to the fallback |
| lb close touchdown | `kclick` via `landBeat` | `closeLb` | inside the teardown timer (930 soft / 430 snap); soft = phone = silent both ways now |
| shelf → lb arc settle | `kclick` | `shelfToLbArc` | `bayFlight` completion callback |
| lb → shelf arc landing | `landBeat` | `lbToShelfArc` | `bayFlight` completion callback |
| deck re-stack settle | `kclick` | `renderBay` | `setTimeout(…, 320)`, suppressed by `bayQuiet` |
| fly-back landing | `landBeat` | `homeFly` | `bayFlight` completion callback |
| deck seat landing | `landBeat` | `seatFly` | `bayFlight` completion callback — **silent when the seat vanished mid-flight** (see the ruling above) |
| composer envelope stamp | `kclick` | the composer's `stamp` | on the press beat |
| composer wax seal | `kthunk` | the composer's `sealed` | `bdmT(…, SEAL_TUNE.drop)` |
| — | `kbonk` | nowhere | see above |

Haptics (`buzz`) ride the bench toggles, the lb page-turn, `pickCatch`'s landing, the picks departure swipe and the drag grab. **A `buzz` is not in this table on purpose** — it is not a sound, and it does not follow these rules.

## Verifying sound work

The voices cannot be HEARD in any harness available here, so verify the GATE, not the audio: instrument `sndOk` to push `{voice, why, t}` onto a window array, drive the page over the served port with a headless-Chrome CDP script (the gotchas escape — the browser pane's dead frame loop cannot complete a `bayFlight`, so no landing beat ever fires there), and count fires per gesture. **Build a BEFORE copy with just the change reverted and run the identical walk** — that is what turned "the add double-clicks" from a report into 8121/8489.

Five things that cost real time here, worth knowing before the next pass:

- **Capture `new Error().stack` in the instrumentation.** A count tells you a click happened; the stack tells you WHICH beat fired it. `sndOk < kclick < … < HTMLDivElement.land` is what proved the lb open was adopting a foreign transition's end rather than firing late.
- **Clear `localStorage` in `Page.addScriptToEvaluateOnNewDocument`, and navigate ONCE.** A deck left over from the last walk turns an add into a remove and every count reads wrong — but two back-to-back loads of this 900KB page wedge the renderer (seen three times: the page target silently resets to `about:blank` and every later `evalx` hangs). One navigate with a clear-on-new-document gives a clean deck without the second load.
- **Seed the deck to 3+ before testing a re-stack.** Removing the only card, or the last of two, moves nothing — `moved` is false, no settle click, and the walk reads as a silent regression that isn't one.
- **Re-query by `data-id` at click time.** Any render boundary replaces the chip node, so a handle grabbed before the render is detached and its click does nothing (gotchas' detached-node law, met again).
- **The strip minis are `pointer-events: none`.** A `.lbsmini.click()` does nothing; the lane resolves its target from HOVER (`sFocus`), so an interrupt test needs a real `Input.dispatchMouseEvent` mousemove over the lane and then a click there.

## Still open

- ~~kbonk's beat~~ **CLOSED 2026-08-21 — parked by Dylan** (see "The no that has nothing to say"). Not an open thread.
- **A mute button.** Promised since 2026-08-01, still unbuilt. When it lands it writes `SND_KEY`; nothing else needs to change.
- **Per-ground sound sets** were parked with the ground switcher and died with the dark ground (2026-08-20). One light ground, one sound set.
- **T2's landing variants** left a `TODO(T1)` in the `?land=` CSS block — "the draw's touchdown wants a sound". That is a NEW trigger on a new surface, not a re-timing; it needs a beat chosen and Dylan's ear, and it must respect the phone rule (the landing variants are desktop-scoped already).
