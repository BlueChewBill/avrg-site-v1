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
2. **THE PHONE IS SILENT.** `dockActive()` (the site's own `matchMedia("(max-width: 940px)")` line) → the voice returns silently. This was ALREADY the shipped behaviour, authored by absence: the soft return lands silent, the slide exchange answers in fills, `pickCatch` is a silent landing plus a buzz, `mobileExitFly`'s comment says the re-stack click is the remove's one sound. Every one of those was a separate ruling in the same direction. **The gate turns a habit into a rule**, so a new call site cannot leak percussion onto the phone by forgetting. Read LIVE at fire time, never cached at boot — a window dragged across 940 changes dialect with it, the same law `renderLisst` obeys.
3. **ONE VOICE, ONE COOLDOWN — 100ms, PER VOICE.** Deliberately not global: the composer's seal `kthunk` and stamp `kclick` are a designed pair ~615ms apart and both must land, and any future two-voice beat must survive too. What the cooldown stops is the same voice re-firing on top of itself.

**`buzz()` is outside the gate entirely** and stays that way. A muted Android still taps back; the phone keeps its haptics while it loses its percussion. Video elements are also outside — `#vlb`'s clips keep their native audio and their unmute.

## THE LANDING OWNS THE VOICE — the add double-click (2026-08-21, Dylan's catch)

Adding a card to the deck clicked TWICE. Both clicks were correct in isolation: `seatFly` renders the preseat (which re-stacks the column, and `renderBay`'s FLIP replay answers its settle with a `kclick` at 320ms), and then the flight's own `landBeat` fires at the seat 680ms in. **Measured on the served page: 8121ms and 8489ms — 368ms apart**, far outside any cooldown, so a time-based fix could never have caught it.

The fix is a FLAG, because only the mover knows a beat is already booked: `bayQuiet` + `renderBayQuiet()`. The mover raises it around its own render and the settle sits that one out.

**Quiet (a landing beat already answers):** `seatFly`'s preseat render and its bail render (the add) · `homeFly`'s ON-STAGE branch (the remove that flies back to a visible shop slot).

**Loud — these re-stacks ARE their gesture's one sound, do not quiet them:** the shop/lisst chip uncheck (`else renderBay()`, membership only, nothing flies) · the lb un-deck drag (`d.kind === "deck"` from the lb — the card springs back to the sheet, quiet by design) · `homeFly`'s OFF-STAGE branch and `mobileExitFly` (both say so in their own comments: nothing lands on screen, so the re-stack is the whole sound) · the picks-page removes.

## THE SOUND LANDS WITH THE THING — settle-sync (2026-08-21)

`onSettle(el, prop, fn, fallback)`: fire on the element's own `transitionend`, timer as fallback only, first through wins. Scoped to `e.target === el` because **transitionend bubbles** and the card's children transition transform too.

- **The lb open click** rode a flat `setTimeout(…, 430)` while `.lb-card`'s transform transition is **`.55s`** — it had been firing ~120ms BEFORE the card came to rest, and nothing in the file connected the two numbers. Now on `onSettle(lbCard, "transform", …, 700)`. Measured: the click moved from **+431ms to +563/581ms** after the press. The tokening (`lbOpenN`, `lbFlying`) is unchanged — a close or re-open inside the flight still voids it.
- **The bay re-stack click KEEPS its 320ms timer**, audited and left alone. 320 is not a guess: it is the `.3s` FLIP transition plus the two rAFs that arm it, and the same 320 is what the per-element cleanup runs on. Measured, the moved item's `transitionend` lands within a frame of the timer (`end@8118` vs the click at 8121) — riding it would move the beat ~0-20ms and hand it to an event the cleanup is racing. Re-timing that cleanup would be choreography, not sound.

**The general law:** a voice pinned to a bare constant drifts the moment its choreography is retuned, and nothing warns you. Derive it from the animation (the exchange settles already do — they ride `g.T.xDur`), ride the flight's completion callback (every `bayFlight` landing does), or ride `transitionend` with a generous fallback. A hardcoded number is only acceptable where it is provably the animation's own arithmetic, and then it should say so.

## The no that has nothing to say

**`kbonk` is fully built and never called, and that is currently correct.** The beat it was written for — the composer's required-field rejection, complete with a gesture half (`.bdm-prev.nope` + `@keyframes envNope`, the card throwing a few px TOWARD the offending field) — **retired with the tray**. The tombstone is at `bdmHref`: *"bdmMissing/bdmNope retired with the tray — a reddit DM has no required field, so nothing can arrive half-addressed."* The CSS is orphaned for the same reason.

The site's one live required field is the lisst page's `#inq-handle`, which rejects through the browser's own native validation bubble. **Giving that a voice is a design call for Dylan, not a wiring job** — it would mean a new sound on a surface that never had one. Until then the voice and its gesture keep their seats; both are written, tuned, and one call away.

## Trigger inventory (2026-08-21)

Every place the page makes a synthesized sound. Anchors are function names.

| beat | voice | where | when it fires |
|---|---|---|---|
| deck exchange settle | `kclick` | `deckExchange` | `setTimeout(…, dur)`, `dur = g.T.xDur` — derived |
| toss exchange settle | `kclick` | `tossExchange` | same, derived |
| lb OPEN flight landing | `kclick` | `openLb` | `onSettle(lbCard, "transform")`, 700ms fallback |
| lb close touchdown | `kclick` via `landBeat` | `closeLb` | inside the teardown timer (930 soft / 430 snap); soft = phone = silent both ways now |
| shelf → lb arc settle | `kclick` | `shelfToLbArc` | `bayFlight` completion callback |
| lb → shelf arc landing | `landBeat` | `lbToShelfArc` | `bayFlight` completion callback |
| deck re-stack settle | `kclick` | `renderBay` | `setTimeout(…, 320)`, suppressed by `bayQuiet` |
| fly-back landing | `landBeat` | `homeFly` | `bayFlight` completion callback |
| deck seat landing | `landBeat` | `seatFly` | `bayFlight` completion callback |
| composer envelope stamp | `kclick` | the composer's `stamp` | on the press beat |
| composer wax seal | `kthunk` | the composer's `sealed` | `bdmT(…, SEAL_TUNE.drop)` |
| — | `kbonk` | nowhere | see above |

Haptics (`buzz`) ride the bench toggles, the lb page-turn, `pickCatch`'s landing, the picks departure swipe and the drag grab. **A `buzz` is not in this table on purpose** — it is not a sound, and it does not follow these rules.

## Verifying sound work

The voices cannot be HEARD in any harness available here, so verify the GATE, not the audio: instrument `sndOk` to push `{voice, why, t}` onto a window array, drive the page over the served port with a headless-Chrome CDP script (the gotchas escape — the browser pane's dead frame loop cannot complete a `bayFlight`, so no landing beat ever fires there), and count fires per gesture. **Build a BEFORE copy with just the change reverted and run the identical walk** — that is what turned "the add double-clicks" from a report into 8121/8489. Clear `localStorage` between runs: a deck left over from the last walk turns an add into a remove and every count reads wrong.

## Still open

- **kbonk's beat** — needs Dylan's call (above).
- **A mute button.** Promised since 2026-08-01, still unbuilt. When it lands it writes `SND_KEY`; nothing else needs to change.
- **Per-ground sound sets** were parked with the ground switcher and died with the dark ground (2026-08-20). One light ground, one sound set.
- **T2's landing variants** left a `TODO(T1)` in the `?land=` CSS block — "the draw's touchdown wants a sound". That is a NEW trigger on a new surface, not a re-timing; it needs a beat chosen and Dylan's ear, and it must respect the phone rule (the landing variants are desktop-scoped already).
