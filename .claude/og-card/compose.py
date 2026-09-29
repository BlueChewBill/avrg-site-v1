from PIL import Image, ImageChops, ImageDraw, ImageFont
"""The link-preview card, site/media/og-share.jpg (1200x630).
Run from anywhere:  python3 .claude/og-card/compose.py [CARDREF] [PHOTO_PANEL_W]
Needs card-<REF>.png beside it first (node .claude/og-card/capture-card.mjs "HS 06",
run from this folder with the avrg-v1 server up on :8124)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
W, H = 1200, 630
PW = int(sys.argv[2]) if len(sys.argv) > 2 else 700   # photo panel width
card_ref = sys.argv[1] if len(sys.argv) > 1 else "HS06"

# left: the profile shot, fit to the panel width, sky extended upward
ph = Image.open(f"{HERE}/profile.jpg").convert("RGB")
ph = ph.resize((PW, round(ph.height * PW / ph.width)), Image.LANCZOS)
top = H - ph.height
left = Image.new("RGB", (PW, H))
# per-column average of the photo's top rows, stretched up; the photo fades in over 90px
col = ph.crop((0, 0, PW, 40)).resize((PW, 1), Image.BOX).resize((PW, H), Image.BICUBIC)
left.paste(col, (0, 0))
fade = 90
mask = Image.linear_gradient("L").resize((PW, fade))
left.paste(ph.crop((0, 0, PW, fade)), (0, top), mask)
left.paste(ph.crop((0, fade, PW, ph.height)), (0, top + fade))

# the white line mark, centred over the board
lg = Image.open(f"{REPO}/site/img/logo-line-white.png").convert("RGBA")
lg = lg.crop(lg.getbbox()); s = 150
lg = lg.resize((s, round(s * lg.height / lg.width)), Image.LANCZOS)
board_cx = round((70 + 915) / 2 * PW / 1016)
board_top = top + round(295 * PW / 1016)
left = left.convert("RGBA")
LOGO_Y = 56
left.alpha_composite(lg, (board_cx - lg.width // 2, LOGO_Y))

MONO = "/System/Library/Fonts/SFNSMono.ttf"
def tracked(img, text, cx, y, size, fill, track):
    """Centre a letter-spaced line on cx (the card chip's tracked-mono voice)."""
    d = ImageDraw.Draw(img); f = ImageFont.truetype(MONO, size)
    ws = [d.textlength(ch, font=f) for ch in text]
    w = sum(ws) + track * (len(text) - 1); x = cx - w / 2
    for ch, cw in zip(text, ws):
        d.text((x, y), ch, font=f, fill=fill); x += cw + track

# the tagline, midway between the mark's foot and the deck's tail
mid = (LOGO_Y + lg.height + board_top) // 2
tracked(left, "celebrating the mundane", board_cx, mid - 11, 17, (235, 235, 230, 235), 2.2)
# the address, down in the black under the reflection
tracked(left, "AVRG.cards", board_cx, H - 58, 19, (200, 200, 195, 255), 3)

# right: the real gallery card on the site's white
card = Image.open(f"{HERE}/card-{card_ref}.png").convert("RGB")
bb = ImageChops.difference(card, Image.new("RGB", card.size, "white")).getbbox()
card = card.crop(bb)
ch = 540
card = card.resize((round(card.width * ch / card.height), ch), Image.LANCZOS)
out = Image.new("RGBA", (W, H), "white")
out.alpha_composite(left, (0, 0))
rx = PW + (W - PW - card.width) // 2
out.paste(card, (rx, (H - ch) // 2))
out.convert("RGB").save(f"{REPO}/site/media/og-share.jpg", quality=90, optimize=True, progressive=True, subsampling=0); print("wrote site/media/og-share.jpg", card.size)
