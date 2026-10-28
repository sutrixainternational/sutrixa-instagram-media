#!/usr/bin/env python3
"""Highlight covers: 1080x1920, icon area centred (Instagram crops a circle from the middle).
usage: python3 tools/story_cover.py outdir LABEL [LABEL...]"""
import os, sys
from PIL import Image, ImageDraw, ImageFont
W, H = 1080, 1920
FB = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
for lab in sys.argv[2:]:
    im = Image.new("RGB", (W, H), (11, 20, 40)); d = ImageDraw.Draw(im)
    r = 420; cx, cy = W // 2, H // 2
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 212, 0))
    size = 150
    while True:
        f = ImageFont.truetype(FB, size)
        if d.textlength(lab, font=f) < 2 * r - 120 or size < 60: break
        size -= 8
    tw = d.textlength(lab, font=f); bb = d.textbbox((0, 0), lab, font=f)
    d.text((cx - tw / 2, cy - (bb[3] + bb[1]) / 2), lab, font=f, fill=(11, 20, 40))
    p = os.path.join(out, f"cover_{lab.lower()}.png"); im.save(p); print(p)
