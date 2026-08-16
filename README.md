# AVRG — handmade fingerboards

The site for AVRG handmade fingerboards. One hand-built page, no framework, no dependencies.

- `index.html` — the whole site (single-page app).
- `site/` — everything the page loads: generated board imagery, card artwork, media, fonts, `data.js`.
- `sources/` — board photography, one folder per collection. `python3 build_site.py` regenerates `site/img/` and `site/data.js` from it.
