"""Reel renderer v3: trend presets (see docs/presets.md).

Full-bleed footage, small corner logo on every frame, word-by-word kinetic captions
synced to the Kokoro voice, app-demo tap + zoom on real screens, labelled stages,
beat-synced punch-ins, optional loop back to the first frame.

spec:
{
 "out": "x.mp4", "preset": "proof|pov|stages|tips|quiz", "accent": "#FFD400",
 "voice": "af_heart", "speed": 1.15, "beat_bpm": 100, "loop": true,
 "beats": [
   {"kind": "clip",   "video": "clip.mp4", "vstart": 0, "say": "...", "headline": "...", "label": "POV"},
   {"kind": "screen", "image": "shots/rz_registers.jpg", "hl": [x0,y0,x1,y1], "tap": true, "say": "...", "label": "STEP 1"},
   {"kind": "split",  "video": "clip.mp4", "image": "shot.jpg", "top_label": "BEFORE", "bottom_label": "AFTER", "say": "..."},
   {"kind": "card",   "video": "clip.mp4", "headline": "Comment DEMO", "say": "..."}
 ]
}
Every beat needs "say" (the renderer refuses a Reel with no voice). dur = voice length + pad unless "dur" is given and longer.
"""
import json, math, subprocess, sys, os, shutil, math, tempfile, re
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = Image.open(os.path.join(HERE, "..", "brand", "logo.png")).convert("RGBA")
FB = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FM = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
_F = {}


def font(p, s):
    k = (p, s)
    if k not in _F:
        _F[k] = ImageFont.truetype(p, s)
    return _F[k]


def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def ease(t):
    t = min(max(t, 0.0), 1.0); return 1 - (1 - t) ** 3


LOGO_C = LOGO.resize((150, int(LOGO.height * 150 / LOGO.width)), Image.LANCZOS)


def corner_logo(img):
    # soft dark pill behind the logo so it reads on any footage
    pad = 14
    pill = Image.new("RGBA", (LOGO_C.width + pad * 2, LOGO_C.height + pad * 2), (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle([0, 0, pill.width - 1, pill.height - 1], 22, fill=(0, 0, 0, 110))
    img.alpha_composite(pill, (36, 70))
    img.alpha_composite(LOGO_C, (36 + pad, 70 + pad))


def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines


def headline(img, text, y, size=84, alpha=1.0, box=True):
    d = ImageDraw.Draw(img, "RGBA"); f = font(FB, size)
    lines = wrap(d, text, f, W - 140); lh = int(size * 1.12)
    a = int(255 * alpha)
    if box:
        tw = max(d.textlength(l, font=f) for l in lines)
        bx0 = (W - tw) / 2 - 34; bx1 = (W + tw) / 2 + 34
        d.rounded_rectangle([bx0, y - 22, bx1, y + lh * len(lines) + 10], 28, fill=(255, 255, 255, int(235 * alpha)))
        col, stroke = (10, 10, 10, a), 0
    else:
        col, stroke = (255, 255, 255, a), 5
    for ln in lines:
        d.text(((W - d.textlength(ln, font=f)) / 2, y), ln, font=f, fill=col, stroke_width=stroke, stroke_fill=(0, 0, 0, a))
        y += lh
    return y


def chip(img, text, accent, y=230, alpha=1.0):
    d = ImageDraw.Draw(img, "RGBA"); f = font(FB, 44)
    tw = d.textlength(text, font=f)
    x0 = (W - tw) / 2 - 28
    d.rounded_rectangle([x0, y, x0 + tw + 56, y + 76], 38, fill=accent + (int(255 * alpha),))
    d.text((x0 + 28, y + 12), text, font=f, fill=(10, 10, 10, int(255 * alpha)))


def caption_words(text):
    """Join spelled-out acronyms for display: 'G S T' -> 'GST', 'C A.' -> 'CA.'"""
    toks = text.split(); out = []; i = 0
    single = lambda w: re.fullmatch(r"[A-Z][^\w\s]*", w) is not None
    while i < len(toks):
        j = i
        while j < len(toks) and single(toks[j]) and (j == i or re.fullmatch(r"[A-Z]", toks[j - 1])):
            j += 1
        if j - i >= 2:  # a run of 2+ single capitals is a spelled acronym
            out.append("".join(toks[i:j])); i = j
        else:
            out.append(toks[i]); i += 1
    return out


def word_times(text, total, start=0.25):
    words = caption_words(text)
    weights = [len(re.sub(r"\W", "", w)) + 2 for w in words]
    span = max(total - start - 0.15, 0.3); s = sum(weights); t = start; out = []
    for w, k in zip(words, weights):
        d = span * k / s; out.append((w, t, t + d)); t += d
    return out


def kinetic(img, wt, t, accent, y=1380, size=88):
    """Show the 1-3 word chunk containing the current word; current word in accent."""
    if not wt: return
    idx = None
    for i, (_, a, b) in enumerate(wt):
        if a <= t < b: idx = i; break
    if idx is None:
        if t >= wt[-1][2]: idx = len(wt) - 1
        else: return
    c0 = (idx // 3) * 3; chunk = wt[c0:c0 + 3]
    d = ImageDraw.Draw(img, "RGBA"); f = font(FB, size)
    words = [w for w, _, _ in chunk]
    line = " ".join(words)
    # shrink to fit
    while d.textlength(line, font=f) > W - 120 and size > 50:
        size -= 6; f = font(FB, size)
    x = (W - d.textlength(line, font=f)) / 2
    pop = 1.0
    for j, (w, a, b) in enumerate(chunk):
        col = accent if (c0 + j) == idx else (255, 255, 255)
        d.text((x, y), w, font=f, fill=col + (255,), stroke_width=7, stroke_fill=(0, 0, 0, 255))
        x += d.textlength(w + " ", font=f)


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    r = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    x = (r.width - w) // 2; y = (r.height - h) // 2
    return r.crop((x, y, x + w, y + h))


def extract_frames(video, vstart, dur, work, tag, w=W, h=H):
    vdir = os.path.join(work, tag); os.makedirs(vdir, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-ss", str(vstart), "-t", str(dur), "-i", video,
                    "-vf", f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={FPS}",
                    os.path.join(vdir, "%05d.jpg")], check=True)
    fr = sorted(os.listdir(vdir))
    if not fr:  # clip shorter than vstart: fall back to start
        subprocess.run(["ffmpeg", "-v", "error", "-t", str(dur), "-i", video, "-vf",
                        f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={FPS}",
                        os.path.join(vdir, "%05d.jpg")], check=True)
        fr = sorted(os.listdir(vdir))
    return vdir, fr


def vframe(vdir, fr, i):
    # ping-pong if the clip segment is shorter than the beat
    n = len(fr)
    if n == 0: return Image.new("RGB", (W, H))
    k = i % (2 * n - 1) if n > 1 else 0
    if k >= n: k = 2 * n - 2 - k
    return Image.open(os.path.join(vdir, fr[k])).convert("RGB")


def punch(im, t, bpm, strength=0.035):
    """Beat-synced punch-in: a quick zoom at every beat."""
    if not bpm: return im
    period = 60.0 / bpm; ph = (t % period) / period
    z = 1 + strength * max(0, 1 - ph * 4)
    if z <= 1.001: return im
    w, h = im.size; cw, ch = int(w / z), int(h / z)
    return im.crop(((w - cw) // 2, (h - ch) // 2, (w - cw) // 2 + cw, (h - ch) // 2 + ch)).resize((w, h), Image.LANCZOS)


SCRIM = Image.new("RGBA", (W, H), (0, 0, 0, 0))
_d = ImageDraw.Draw(SCRIM)
for _y in range(360):
    _d.line([(0, _y), (W, _y)], fill=(0, 0, 0, int(150 * (1 - _y / 360))))
for _y in range(1150, H):
    _d.line([(0, _y), (W, _y)], fill=(0, 0, 0, int(190 * min(1, (_y - 1150) / 500))))


def screen_frame(shot, t, dur, hl, tap, accent):
    """Full-bleed phone screen: starts showing the top, taps the target, zooms into it."""
    s = W / shot.width
    full = shot.resize((W, int(shot.height * s)), Image.LANCZOS)
    bg = cover(shot, W, H).filter(ImageFilter.GaussianBlur(30)).convert("RGBA")
    bg.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 120)))
    if hl:
        x0, y0, x1, y1 = [v * s for v in hl]
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    else:
        cx, cy = W / 2, full.height / 3
    zt = ease((t - 0.9) / 0.7) if hl else 0.0
    z = 1 + 0.55 * zt
    # viewport centred toward the target as we zoom
    vw, vh = W / z, min(H, full.height) / z
    vx = min(max(cx - vw / 2, 0), W - vw) * zt
    vy0 = 0 if full.height <= H else min(max(cy - H / 2, 0), full.height - H) * min(1, t / 0.9)
    vy = vy0 + (min(max(cy - vh / 2, 0), full.height - vh) - vy0) * zt
    crop = full.crop((int(vx), int(vy), int(vx + vw), int(vy + vh))).resize((W, int(vh * z)), Image.LANCZOS)
    img = bg
    oy = max(0, (H - crop.height) // 2)
    img.paste(crop, (0, oy))
    d = ImageDraw.Draw(img, "RGBA")
    if hl:
        # target box in screen coords
        bx0 = (x0 - vx) * z; by0 = (y0 - vy) * z + oy; bx1 = (x1 - vx) * z; by1 = (y1 - vy) * z + oy
        if t > 0.5:
            a = int(255 * ease((t - 0.5) / 0.3))
            d.rounded_rectangle([bx0 - 10, by0 - 10, bx1 + 10, by1 + 10], 20, outline=accent + (a,), width=9)
        if tap and 0.45 < t < 1.25:
            p = (t - 0.45) / 0.8
            r = 30 + 70 * p
            tx, ty = (bx0 + bx1) / 2, (by0 + by1) / 2
            d.ellipse([tx - r, ty - r, tx + r, ty + r], outline=(255, 255, 255, int(255 * (1 - p))), width=8)
            d.ellipse([tx - 26, ty - 26, tx + 26, ty + 26], fill=(255, 255, 255, int(200 * (1 - p))))
    return img


def scene_frame(img, t, dur, move="in"):
    """Illustrated story scene: slow Ken Burns move (in/out/left/right/up) with a tiny handheld drift."""
    base = cover(img, int(W * 1.18), int(H * 1.18))
    p = ease(t / max(dur, 0.1)) if dur else 0
    z = {"in": 1.0 + 0.12 * p, "out": 1.12 - 0.12 * p}.get(move, 1.08)
    cw, ch = W * 1.18 / z, H * 1.18 / z
    cx, cy = base.width / 2, base.height / 2
    if move == "left": cx += (0.5 - p) * (base.width - cw) * 0.9
    if move == "right": cx -= (0.5 - p) * (base.width - cw) * 0.9
    if move == "up": cy += (0.5 - p) * (base.height - ch) * 0.9
    cx += 6 * math.sin(t * 1.3); cy += 5 * math.cos(t * 1.1)
    x0 = min(max(cx - cw / 2, 0), base.width - cw); y0 = min(max(cy - ch / 2, 0), base.height - ch)
    return base.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch))).resize((W, H), Image.LANCZOS)


def tts_factory():
    k = {}
    def tts(text, voice, speed, out, lang="en-us"):
        import soundfile as sf
        if "m" not in k:
            from kokoro_onnx import Kokoro
            k["m"] = Kokoro(os.path.join(HERE, "tts", "kokoro-v1.0.onnx"), os.path.join(HERE, "tts", "voices-v1.0.bin"))
        smp, sr = k["m"].create(text, voice=voice, speed=speed, lang=lang)
        sf.write(out, smp, sr)
        return len(smp) / sr
    return tts


def render(spec):
    accent = hexrgb(spec.get("accent", "#FFD400"))
    bpm = spec.get("beat_bpm", 100)
    outdir = os.path.dirname(os.path.abspath(spec["out"]))
    work = tempfile.mkdtemp(dir=outdir)
    tts = tts_factory()
    voice, speed = spec.get("voice", "af_heart"), spec.get("speed", 1.15)
    beats = spec["beats"]
    for bi, b in enumerate(beats):
        if not b.get("say"):
            raise SystemExit(f"REFUSING: beat {bi} has no 'say' line (every beat is voiced)")
        vp = os.path.join(work, f"vo{bi}.wav"); L = tts(b.get("tts", b["say"]), voice, speed, vp, spec.get("lang", "en-us"))
        b["_vo"], b["_vl"] = vp, L
        b["dur"] = max(b.get("dur", 0), round(L + 0.45, 2))
        b["_wt"] = word_times(b["say"], L + 0.25)
    fdir = os.path.join(work, "f"); os.makedirs(fdir)
    n = 0; t_global = 0.0; taps = []
    first_frame = None
    for bi, b in enumerate(beats):
        dur = b["dur"]; nf = int(round(dur * FPS)); kind = b["kind"]
        vd = fr = None; shot = None
        if b.get("video"):
            if kind == "split":
                vd, fr = extract_frames(b["video"], b.get("vstart", 0), dur, work, f"v{bi}", W, H // 2)
            else:
                vd, fr = extract_frames(b["video"], b.get("vstart", 0), dur, work, f"v{bi}")
        if b.get("image"):
            shot = Image.open(b["image"]).convert("RGB")
        if kind == "screen" and b.get("tap"):
            taps.append(t_global + 0.45)
        for i in range(nf):
            t = i / FPS
            if kind == "clip":
                img = punch(vframe(vd, fr, i), t_global + t, bpm if b.get("punch", True) else 0).convert("RGBA")
                img.alpha_composite(SCRIM)
            elif kind == "screen":
                img = screen_frame(shot, t, dur, b.get("hl"), b.get("tap"), accent)
                img.alpha_composite(SCRIM)
            elif kind == "scene":
                img = scene_frame(shot, t, dur, b.get("move", "in")).convert("RGBA")
                img.alpha_composite(SCRIM)
            elif kind == "split":
                top = vframe(vd, fr, i).convert("RGBA")
                bot = cover(shot, W, H // 2).convert("RGBA") if shot else Image.new("RGBA", (W, H // 2))
                if b.get("hl") and shot:
                    bot = screen_frame(shot, t, dur, b["hl"], b.get("tap"), accent).crop((0, H // 4, W, H // 4 + H // 2))
                img = Image.new("RGBA", (W, H)); img.paste(top, (0, 0)); img.paste(bot, (0, H // 2))
                dd = ImageDraw.Draw(img); dd.rectangle([0, H // 2 - 5, W, H // 2 + 5], fill=(255, 255, 255, 255))
                for lab, yy, col in ((b.get("top_label"), H // 2 - 110, (230, 60, 60)), (b.get("bottom_label"), H // 2 + 30, (40, 190, 110))):
                    if lab:
                        f = font(FB, 46); tw = dd.textlength(lab, font=f)
                        dd.rounded_rectangle([40, yy, 40 + tw + 48, yy + 78], 20, fill=col + (255,))
                        dd.text((64, yy + 12), lab, font=f, fill=(255, 255, 255, 255))
            else:  # card
                base = vframe(vd, fr, i) if vd else (cover(shot, W, H) if shot else Image.new("RGB", (W, H), (8, 14, 34)))
                img = base.filter(ImageFilter.GaussianBlur(18)).convert("RGBA")
                img.alpha_composite(Image.new("RGBA", (W, H), (0, 0, 0, 110)))
            if b.get("label") and kind != "split":
                chip(img, b["label"], accent, alpha=1.0 if bi == 0 else ease(t / 0.2))
            if b.get("headline"):
                hy = 820 if kind == "card" else 340
                headline(img, b["headline"], hy, size=96 if kind == "card" else 80,
                         alpha=1.0 if bi == 0 else ease(t / 0.2), box=(kind != "card"))
            kinetic(img, b["_wt"], t, accent, y=1420 if kind != "split" else 1700)
            corner_logo(img)
            out = img.convert("RGB")
            if first_frame is None: first_frame = out.copy()
            out.save(os.path.join(fdir, f"f{n:05d}.jpg"), quality=92); n += 1
        t_global += dur
    if spec.get("loop", True) and first_frame is not None:
        last = Image.open(os.path.join(fdir, f"f{n-1:05d}.jpg")).convert("RGB")
        for i in range(10):  # 0.33s crossfade back to the opening frame
            Image.blend(last, first_frame, (i + 1) / 10).save(os.path.join(fdir, f"f{n:05d}.jpg"), quality=92); n += 1
        t_global += 10 / FPS
    total = n / FPS
    # ---- audio: per-beat (ambient clip sound ducked + voice), then beat bed + tap clicks
    segs = []
    for bi, b in enumerate(beats):
        base = os.path.join(work, f"b{bi}.wav"); seg = os.path.join(work, f"s{bi}.wav")
        ok = False
        if b.get("video"):
            r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(b.get("vstart", 0)), "-t", str(b["dur"]), "-i", b["video"],
                                "-vn", "-af", f"apad,atrim=0:{b['dur']},volume=0.28", "-ar", "44100", "-ac", "2", base])
            ok = r.returncode == 0 and os.path.exists(base) and os.path.getsize(base) > 1000
        if not ok:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", str(b["dur"]), "-i",
                            "anullsrc=channel_layout=stereo:sample_rate=44100", base], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base, "-i", b["_vo"], "-filter_complex",
                        f"[1:a]aresample=44100,pan=stereo|c0=c0|c1=c0,adelay=250|250,volume=1.7[v];[0:a][v]amix=inputs=2:duration=first:normalize=0,atrim=0:{b['dur']}",
                        "-ar", "44100", "-ac", "2", seg], check=True)
        segs.append(seg)
    if spec.get("loop", True):
        tail = os.path.join(work, "tail.wav")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", str(10 / FPS), "-i",
                        "anullsrc=channel_layout=stereo:sample_rate=44100", tail], check=True); segs.append(tail)
    lst = os.path.join(work, "a.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in segs))
    voice_track = os.path.join(work, "voice.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "pcm_s16le", voice_track], check=True)
    p = 60.0 / bpm if bpm else 0.6
    kick = f"0.55*sin(2*PI*(50+90*exp(-mod(t,{p})*30))*mod(t,{p}))*exp(-mod(t,{p})*9)"
    hat = f"0.06*(random(0)*2-1)*exp(-mod(t+{p/2},{p})*60)"
    clicks = "+".join(f"0.5*sin(2*PI*2400*(t-{tc:.3f}))*exp(-abs(t-{tc:.3f})*90)*between(t,{tc:.3f},{tc+0.08:.3f})" for tc in taps) or "0"
    bed = os.path.join(work, "bed.wav")
    if spec.get("bed") == "pad":  # gentle story bed: soft chord with slow swell, no kick
        expr = "0.05*(sin(2*PI*110*t)+0.7*sin(2*PI*164.8*t)+0.6*sin(2*PI*220*t)+0.4*sin(2*PI*277.2*t))*(0.75+0.25*sin(2*PI*0.12*t))"
    else:
        expr = f"0.35*({kick}+{hat})+{clicks}"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", f"{total:.3f}", "-i",
                    f"aevalsrc='{expr}':s=44100:c=stereo", "-af",
                    f"afade=t=in:d=0.3,afade=t=out:st={max(total-0.6,0):.2f}:d=0.6", bed], check=True)
    mix = os.path.join(work, "mix.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", voice_track, "-i", bed, "-filter_complex",
                    "[1:a]volume=0.45[bd];[0:a][bd]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11",
                    "-ar", "44100", mix], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(fdir, "f%05d.jpg"),
                    "-i", mix, "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "19",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", spec["out"]], check=True)
    shutil.rmtree(work)
    print("wrote", spec["out"], round(total, 1), "s", spec.get("preset"))


if __name__ == "__main__":
    render(json.load(open(sys.argv[1])))
