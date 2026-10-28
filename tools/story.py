#!/usr/bin/env python3
"""Render Instagram Story frames (1080x1920 PNG) for @sutrixainternational.

usage: python3 tools/story.py spec.json outdir/

spec = {"frames": [ {
    "name": "01_start",            # output file stem
    "kicker": "START HERE",        # small pill at the top (optional)
    "headline": "Run your hotel from *one calm screen*",   # *...* = yellow
    "image": "shots/rz_dashboard.jpg",   # optional product screen
    "bullets": ["GST bill ...", "..."],  # optional
    "foot": "sutrixa.com"          # optional bottom line
}]}

Every frame carries the Sutrixa logo. Content stays inside the story safe zone (y 250-1600),
per ig-story: the profile row sits above and the reply bar below.
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
SAFE_TOP, SAFE_BOT = 250, 1600
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
if not os.path.exists(FM):
    FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf"
YEL = (255, 212, 0)
WHITE = (245, 247, 250)
MUTED = (170, 182, 204)


def font(p, s):
    return ImageFont.truetype(p, s)


def bg():
    im = Image.new("RGB", (W, H))
    top, bot = (9, 16, 32), (20, 38, 70)
    px = im.load()
    for y in range(H):
        t = y / H
        c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
        for x in range(W):
            px[x, y] = c
    # soft glow
    glow = Image.new("L", (W, H), 0)
    ImageDraw.Draw(glow).ellipse((W - 700, -300, W + 300, 700), fill=70)
    glow = glow.filter(ImageFilter.GaussianBlur(160))
    im = Image.composite(Image.new("RGB", (W, H), (40, 90, 170)), im, glow)
    return im


def logo(im):
    lg = Image.open(os.path.join(ROOT, "brand/logo.png")).convert("RGBA")
    h = 110
    lg = lg.resize((int(lg.width * h / lg.height), h), Image.LANCZOS)
    pad = 18
    pill = Image.new("RGBA", (lg.width + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle((0, 0, pill.width - 1, pill.height - 1), 30, fill=(255, 255, 255, 240))
    pill.alpha_composite(lg, (pad, pad))
    im.paste(pill, (60, SAFE_TOP - 10), pill)
    return SAFE_TOP - 10 + pill.height


def wrap_rich(d, text, f, maxw):
    """Split into lines; returns list of lines, each a list of (word, yellow)."""
    tokens, yel = [], False
    for part in re.split(r"(\*)", text):
        if part == "*":
            yel = not yel
            continue
        for w in part.split():
            tokens.append((w, yel))
    lines, cur = [], []
    for w in tokens:
        test = " ".join(x for x, _ in cur + [w])
        if cur and d.textlength(test, font=f) > maxw:
            lines.append(cur)
            cur = [w]
        else:
            cur.append(w)
    if cur:
        lines.append(cur)
    return lines


def draw_rich(d, y, text, size, maxw=W - 140, x0=70):
    f = font(FB, size)
    while True:
        lines = wrap_rich(d, text, f, maxw)
        if len(lines) <= 4 or size <= 52:
            break
        size -= 6
        f = font(FB, size)
    lh = int(size * 1.18)
    for ln in lines:
        x = x0
        for w, yl in ln:
            d.text((x, y), w, font=f, fill=YEL if yl else WHITE)
            x += d.textlength(w + " ", font=f)
        y += lh
    return y


def card(im, path, y, maxh):
    sh = Image.open(os.path.join(ROOT, path)).convert("RGB")
    maxw = W - 160
    s = min(maxw / sh.width, maxh / sh.height)
    sh = sh.resize((int(sh.width * s), int(sh.height * s)), Image.LANCZOS)
    x = (W - sh.width) // 2
    mask = Image.new("L", sh.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, sh.width - 1, sh.height - 1), 34, fill=255)
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((x + 10, y + 24, x + sh.width + 10, y + sh.height + 24), 34, fill=(0, 0, 0, 150))
    shadow = shadow.filter(ImageFilter.GaussianBlur(24))
    im.paste(shadow, (0, 0), shadow)
    im.paste(sh, (x, y), mask)
    return y + sh.height


def render(fr, out):
    im = bg()
    d = ImageDraw.Draw(im)
    y = logo(im) + 50
    if fr.get("kicker"):
        f = font(FB, 34)
        tw = d.textlength(fr["kicker"], font=f)
        d.rounded_rectangle((70, y, 70 + tw + 48, y + 62), 31, fill=YEL)
        d.text((94, y + 9), fr["kicker"], font=f, fill=(12, 18, 32))
        y += 100
    y = draw_rich(d, y, fr["headline"], fr.get("size", 84)) + 30
    foot_h = 90 if fr.get("foot") else 0
    if fr.get("bullets"):
        f = font(FM, fr.get("bsize", 44 if fr.get("image") else 54))
        for b in fr["bullets"]:
            lines = wrap_rich(d, b, f, W - 230)
            d.ellipse((80, y + 18, 104, y + 42), fill=YEL)
            for ln in lines:
                x = 130
                for w, yl in ln:
                    d.text((x, y), w, font=f, fill=YEL if yl else WHITE)
                    x += d.textlength(w + " ", font=f)
                y += int(f.size * 1.32)
            y += 22
        y += 10
    if fr.get("image"):
        room = SAFE_BOT - foot_h - y - 20
        if room > 480:
            y = card(im, fr["image"], y + 10, room) + 20
    if fr.get("foot"):
        f = font(FB, 46)
        t = fr["foot"]
        tw = d.textlength(t, font=f)
        yy = SAFE_BOT - 76
        d.rounded_rectangle(((W - tw) / 2 - 36, yy, (W + tw) / 2 + 36, yy + 76), 38, outline=YEL, width=4)
        d.text(((W - tw) / 2, yy + 10), t, font=f, fill=YEL)
    im.save(out, optimize=True)


def main():
    spec = json.load(open(sys.argv[1]))
    out = sys.argv[2]
    os.makedirs(out, exist_ok=True)
    for fr in spec["frames"]:
        p = os.path.join(out, fr["name"] + ".png")
        render(fr, p)
        print(p)


if __name__ == "__main__":
    main()
