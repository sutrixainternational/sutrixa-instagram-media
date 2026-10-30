#!/usr/bin/env python3
"""Keyword freebie checklist: 1080x1350 PNG + PDF with the Sutrixa logo.

usage: python3 tools/freebie.py spec.json out_basename   (writes out_basename.png and .pdf)

spec = {"title": "Stop these 5", "title2": "missed-call mistakes",
        "items": [["#5", "Bold line.", "Grey detail line."], ...],
        "footer": "Setup in 4 steps: ...", "links": "voxa.sutrixa.com  ·  Book a demo: sutrixa.com/connect"}

Owner rule (30 Oct 2026): no product pricing anywhere. This script refuses specs that contain
a $ amount, "/month", "per minute" or a plan name used as a price.
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FB = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"
FR = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
for alt_b, alt_r in [("/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf", "/usr/share/fonts/truetype/google-fonts/Poppins-Regular.ttf")]:
    if not os.path.exists(FB):
        FB, FR = alt_b, alt_r
BG, YEL, WHITE, GREY = (11, 20, 34), (255, 212, 0), (245, 247, 250), (160, 172, 192)
PRICE = re.compile(r"\$\s?\d|/\s?month|per\s+minute|/min\b|\bINR\b|\bUSD\b|(Launch|Growth|Scale|Elite)\s+(plan|is|:)", re.I)


def wrap(d, text, f, maxw):
    out, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if cur and d.textlength(t, font=f) > maxw:
            out.append(cur); cur = w
        else:
            cur = t
    if cur:
        out.append(cur)
    return out


def main():
    spec = json.load(open(sys.argv[1]))
    blob = json.dumps(spec)
    m = PRICE.search(blob)
    if m:
        sys.exit(f"REFUSED: pricing found ({m.group(0)!r}). Owner rule 30 Oct: no product pricing.")
    im = Image.new("RGB", (W, H), BG); d = ImageDraw.Draw(im)
    lg = Image.open(os.path.join(ROOT, "brand/logo.png")).convert("RGBA")
    lg = lg.resize((int(lg.width * 170 / lg.height), 170), Image.LANCZOS)
    im.paste(lg, (50, 45), lg)
    d.text((W - 60, 75), "FREE CHECKLIST", font=ImageFont.truetype(FB, 30), fill=YEL, anchor="ra")
    ft = ImageFont.truetype(FB, 66)
    d.text((60, 245), spec["title"], font=ft, fill=WHITE)
    d.text((60, 320), spec["title2"], font=ft, fill=YEL)
    y = 415
    fb, fr, fn = ImageFont.truetype(FB, 36), ImageFont.truetype(FR, 29), ImageFont.truetype(FB, 32)
    for num, bold, detail in spec["items"]:
        d.rounded_rectangle((60, y, 138, y + 78), 16, fill=YEL)
        d.text((99, y + 39), num, font=fn, fill=BG, anchor="mm")
        d.rectangle((170, y + 8, 205, y + 43), outline=WHITE, width=4)
        yy = y
        for ln in wrap(d, bold, fb, W - 290):
            d.text((228, yy), ln, font=fb, fill=WHITE); yy += 46
        for ln in wrap(d, detail, fr, W - 290):
            d.text((228, yy + 2), ln, font=fr, fill=GREY); yy += 40
        y = max(y + 100, yy + 30)
    d.line((60, y, W - 60, y), fill=(60, 72, 95), width=2); y += 22
    for ln in wrap(d, spec.get("footer", ""), ImageFont.truetype(FR, 28), W - 120):
        d.text((60, y), ln, font=ImageFont.truetype(FR, 28), fill=WHITE); y += 38
    y += 14
    d.text((60, y), spec.get("links", ""), font=ImageFont.truetype(FB, 29), fill=YEL); y += 44
    d.text((60, y), "@sutrixainternational  ·  Follow for one business fix a day", font=ImageFont.truetype(FR, 26), fill=GREY)
    base = sys.argv[2]
    im.save(base + ".png", optimize=True)
    im.save(base + ".pdf", resolution=150)
    print(base + ".png")


if __name__ == "__main__":
    main()
