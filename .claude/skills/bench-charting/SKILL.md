---
name: bench-charting
description: The AVRG Bench workflow — charting a site change on the bench (CompUI's tuning deck at /bench), writing a bench-cartographer ticket, the inline-vs-dispatch lanes, the bench laws, and the bench-verification traps. Load whenever a change touches a charted param, a bench wing/dial/bake/census comes up, the bench needs syncing to CompUI, or the change-with-charting law applies.
---

# Bench charting — the AVRG Bench workflow

Root `CLAUDE.md` keeps the standing rules (what the bench is, the BENCH shim
is the one sanctioned hook, `bench/` is a gitignored symlink — **never commit
bench files to the public v1 repo**, pushing CompUI is Dylan's call). This
skill is the procedure.

**Where it lives:** `bench/` in v1 is a **symlink** to `~/Projects/CompUI/pilot/`.
Bench changes are committed in the CompUI repo:
`git -C ~/Projects/CompUI add pilot && git -C ~/Projects/CompUI commit`.
Bench home page: **http://localhost:8124/bench/**, riding the same server that
serves the site (Dylan's own — attach, never start/kill anything on :8124).

## The contract (canonical since 2026-08-20, Dylan's ruling)

The bench and the site move together. A site change that touches a
**charted param** (one in `bench/manifest/avrg.json`) updates the manifest —
and the bench's ANCHORS entry when the override shape changes — **in the same
session**. A new tunable surface gets charted when first touched. Two lanes:

- **Inline (small):** retuning an already-charted value (a bake landing, a
  range widening) — just update the manifest value/note yourself.
- **Dispatch (real charting):** a new param spec, a new wing, or a
  multi-param pass — do the site edit + any shim notation here, then hand
  the **`bench-cartographer` agent** (`.claude/agents/bench-cartographer.md`)
  a ticket. It edits the CompUI side, verifies end-to-end on the served
  bench, commits there, and reports back — this session stays pointed at
  the site and Dylan.

## What a cartographer ticket must contain

- param ids/names
- exact selectors or consts (anchors are NAMES, never line numbers)
- shipped values
- sensible ranges
- couplings/laws worth recording (and any shipped quirk to flag as a find)

## Bench laws that bind this repo's sessions

Constitution: `bench/BUILD-SPEC.md`.

- the manifest is the bench's ONLY data source;
- anchors are NAMES (selectors, consts, vars) — never line numbers;
- params bind to the one shared source — a bench-side fork is
  unconstitutional; "separation" is a site-code change Dylan orders;
- locked params render visible, never hidden;
- overrides replicate shipped behavior exactly, quirks included — a shipped
  quirk is flagged as a find, never silently fixed.

## Verifying bench work

The Claude pane's frame loop is dead inside the stage iframe — motion is
unjudgeable there AND CSS transitions freeze mid-flight (computed style
reads the START value; kill the transition with a probe rule or use the CDP
harness in `.claude/docs/gotchas.md`). Cache-bust every load (`?v=<ts>`) —
and remember the pane's `?v=` only busts the HTML; subresources need an
origin switch (`localhost` → `127.0.0.1`), see gotchas.
