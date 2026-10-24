"""Reel renderer v2: Gemini video beats + screen beats with highlight boxes + step badges + music bed.

spec:
{
 "out": "x.mp4", "accent": "#3fd1ff",
 "beats": [
   {"video": "clip.mp4", "vstart": 0, "dur": 5, "text": "...", "sub": "..."},
   {"image": "shot.jpg", "dur": 5, "step": "1", "text": "...", "sub": "...", "hl": [x0,y0,x1,y1]},
   {"dur": 3, "text": "...", "sub": "..."}            # text-only (end card)
 ]
}
"""
import json, subprocess, sys, os, shutil, math, tempfile
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
LOGO = Image.open(os.path.join(HERE, "..", "brand", "logo.png")).convert("RGBA")
FB = "/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf"
FM = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
BG_TOP, BG_BOT = (6, 12, 32), (10, 34, 74)


def font(p, s):
    return ImageFont.truetype(p, s)


def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def gradient():
    g = Image.new("RGB", (W, H)); d = ImageDraw.Draw(g)
    for y in range(H):
        t = y / H
        d.line([(0, y), (W, y)], fill=tuple(int(BG_TOP[i] + (BG_BOT[i] - BG_TOP[i]) * t) for i in range(3)))
    return g.convert("RGBA")


BG = gradient()
# dark scrims for video beats
TOP_SCRIM = Image.new("RGBA", (W, H), (0, 0, 0, 0))
_d = ImageDraw.Draw(TOP_SCRIM)
for y in range(420):
    _d.line([(0, y), (W, y)], fill=(0, 0, 0, int(170 * (1 - y / 420))))
for y in range(1050, H):
    _d.line([(0, y), (W, y)], fill=(0, 0, 0, int(215 * min(1, (y - 1050) / 450))))
LOGO_S = LOGO.resize((230, int(LOGO.height * 230 / LOGO.width)), Image.LANCZOS)


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


def text_block(img, text, sub, accent, y_top, size, alpha=1.0, sub_size=44):
    d = ImageDraw.Draw(img, "RGBA")
    f = font(FB, size); a = int(255 * alpha)
    y = y_top
    for ln in wrap(d, text, f, W - 150):
        x = (W - d.textlength(ln, font=f)) / 2
        d.text((x, y), ln, font=f, fill=(255, 255, 255, a), stroke_width=4, stroke_fill=(0, 0, 0, int(170 * alpha)))
        y += int(size * 1.15)
    if sub:
        fs = font(FM, sub_size); y += 16
        for ln in wrap(d, sub, fs, W - 180):
            x = (W - d.textlength(ln, font=fs)) / 2
            d.text((x, y), ln, font=fs, fill=accent + (a,), stroke_width=2, stroke_fill=(0, 0, 0, int(140 * alpha)))
            y += int(sub_size * 1.3)
    return y


def block_height(text, sub, size, sub_size=44):
    d = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    h = len(wrap(d, text, font(FB, size), W - 150)) * int(size * 1.15)
    if sub:
        h += 16 + len(wrap(d, sub, font(FM, sub_size), W - 180)) * int(sub_size * 1.3)
    return h


def badge(img, label, accent, cx, cy, alpha):
    d = ImageDraw.Draw(img, "RGBA"); r = 46
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=accent + (int(255 * alpha),))
    f = font(FB, 52); tw = d.textlength(label, font=f)
    d.text((cx - tw / 2, cy - 32), label, font=f, fill=(6, 12, 32, int(255 * alpha)))


def ease(t):
    return 1 - (1 - min(max(t, 0), 1)) ** 3


_KOKORO = None


def tts(text, voice, speed, out):
    global _KOKORO
    import soundfile as sf
    if _KOKORO is None:
        from kokoro_onnx import Kokoro
        _KOKORO = Kokoro(os.path.join(HERE, "tts", "kokoro-v1.0.onnx"), os.path.join(HERE, "tts", "voices-v1.0.bin"))
    smp, sr = _KOKORO.create(text, voice=voice, speed=speed, lang="en-us")
    sf.write(out, smp, sr)
    return len(smp) / sr


def render(spec):
    accent = hexrgb(spec.get("accent", "#3fd1ff"))
    work = tempfile.mkdtemp(dir=os.path.dirname(os.path.abspath(spec["out"])))
    # voiceover: every beat with "say" gets narration; beat stretches to fit the line
    vo_voice, vo_speed = spec.get("voice", "af_heart"), spec.get("speed", 1.05)
    vo_files = []
    for bi, b in enumerate(spec["beats"]):
        if b.get("say"):
            vp = os.path.join(work, f"vo{bi}.wav")
            L = tts(b["say"], vo_voice, vo_speed, vp)
            b["dur"] = max(b["dur"], round(L + 0.5, 2))
            vo_files.append(vp)
        else:
            vo_files.append(None)
    if spec.get("require_voice", True) and not any(vo_files):
        raise SystemExit("REFUSING: reel has no voiceover (owner rule)")
    fdir = os.path.join(work, "f"); os.makedirs(fdir)
    n = 0
    audio_parts = []  # (kind, path/None, dur)
    for bi, b in enumerate(spec["beats"]):
        dur = b["dur"]; nf = int(round(dur * FPS))
        vframes = None
        if b.get("video"):
            vdir = os.path.join(work, f"v{bi}"); os.makedirs(vdir)
            subprocess.run(["ffmpeg", "-v", "error", "-ss", str(b.get("vstart", 0)), "-t", str(dur), "-i", b["video"],
                            "-vf", f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS}",
                            os.path.join(vdir, "%05d.jpg")], check=True)
            vframes = sorted(os.listdir(vdir))
            apath = os.path.join(work, f"a{bi}.wav")
            r = subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(b.get("vstart", 0)), "-t", str(dur), "-i", b["video"],
                                "-vn", "-ac", "2", "-ar", "44100", apath])
            audio_parts.append(apath if r.returncode == 0 and os.path.exists(apath) else None)
        else:
            audio_parts.append(None)
        shot = Image.open(b["image"]).convert("RGB") if b.get("image") else None
        for i in range(nf):
            t = i / FPS
            fade = 1.0 if (bi == 0) else ease(t / 0.3)
            if vframes:
                fr = Image.open(os.path.join(vdir, vframes[min(i, len(vframes) - 1)])).convert("RGBA")
                fr.alpha_composite(TOP_SCRIM)
                img = fr
                img.alpha_composite(LOGO_S, ((W - LOGO_S.width) // 2, 90))
                size = b.get("size", 80)
                bh = block_height(b["text"], b.get("sub"), size)
                text_block(img, b["text"], b.get("sub"), accent, H - 260 - bh, size, fade)
            elif shot is not None:
                img = BG.copy()
                img.alpha_composite(LOGO_S, ((W - LOGO_S.width) // 2, 90))
                size = b.get("size", 66)
                ty = 330
                if b.get("step"):
                    badge(img, b["step"], accent, W // 2, ty + 10, fade); ty += 80
                end_y = text_block(img, b["text"], b.get("sub"), accent, ty, size, fade, sub_size=40)
                # screen card
                cw = 760; s = cw / shot.width
                z = 1.0 + 0.04 * (t / dur); s2 = s * z
                sw, sh = int(shot.width * s2), int(shot.height * s2)
                big = shot.resize((sw, sh), Image.LANCZOS)
                card_y = max(end_y + 40, 760)
                maxh = H - card_y - 120
                ox = (sw - cw) // 2
                crop = big.crop((ox, 0, ox + cw, min(sh, maxh)))
                card = Image.new("RGBA", (cw + 16, crop.height + 16), (255, 255, 255, 255))
                card.paste(crop, (8, 8))
                if b.get("hl"):
                    x0, y0, x1, y1 = b["hl"]
                    hd = ImageDraw.Draw(card, "RGBA")
                    pulse = 0.5 + 0.5 * math.sin(t * 6)
                    a = int(255 * ease((t - 0.4) / 0.4))
                    pad = 8
                    box = [x0 * s2 - ox + 8 - pad, y0 * s2 + 8 - pad, x1 * s2 - ox + 8 + pad, y1 * s2 + 8 + pad]
                    hd.rounded_rectangle(box, 18, outline=(255, 140, 0, a), width=int(7 + 3 * pulse))
                mask = Image.new("L", card.size, 0)
                ImageDraw.Draw(mask).rounded_rectangle([0, 0, card.width - 1, card.height - 1], 34, fill=255)
                cimg = Image.new("RGBA", card.size, (0, 0, 0, 0)); cimg.paste(card, (0, 0), mask)
                img.alpha_composite(cimg, ((W - cimg.width) // 2, card_y))
            else:
                img = BG.copy()
                img.alpha_composite(LOGO_S, ((W - LOGO_S.width) // 2, 90))
                size = b.get("size", 92)
                bh = block_height(b["text"], b.get("sub"), size)
                text_block(img, b["text"], b.get("sub"), accent, (H - bh) // 2, size, fade)
            img.convert("RGB").save(os.path.join(fdir, f"f{n:05d}.jpg"), quality=92)
            n += 1
    total = n / FPS
    # audio: clip audio where present, otherwise silence; plus soft music bed
    segs = []
    for bi, b in enumerate(spec["beats"]):
        p = os.path.join(work, f"s{bi}.wav")
        base = os.path.join(work, f"b{bi}.wav")
        if audio_parts[bi]:
            vol = 0.3 if vo_files[bi] else 0.9
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", audio_parts[bi], "-af", f"apad,atrim=0:{b['dur']},volume={vol}", "-ar", "44100", "-ac", "2", base], check=True)
        else:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", str(b["dur"]), "-i",
                            "anullsrc=channel_layout=stereo:sample_rate=44100", base], check=True)
        if vo_files[bi]:
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", base, "-i", vo_files[bi], "-filter_complex",
                            f"[1:a]aresample=44100,pan=stereo|c0=c0|c1=c0,adelay=250|250,volume=1.6[v];[0:a][v]amix=inputs=2:duration=first:normalize=0,atrim=0:{b['dur']}",
                            "-ar", "44100", "-ac", "2", p], check=True)
        else:
            shutil.copy(base, p)
        segs.append(p)
    lst = os.path.join(work, "a.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in segs))
    voice = os.path.join(work, "voice.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "pcm_s16le", voice], check=True)
    # music bed: slow chord pad (A minor -> F -> C -> G), 2s per chord
    chords = [(220, 261.63, 329.63), (174.61, 220, 261.63), (130.81, 196, 261.63), (196, 246.94, 293.66)]
    expr_parts = []
    for k, ch in enumerate(chords):
        tone = "+".join(f"sin(2*PI*{f}*t)" for f in ch)
        expr_parts.append(f"(between(mod(t,8),{2*k},{2*k+2})*({tone}))")
    expr = "0.03*(" + "+".join(expr_parts) + ")*(0.6+0.4*sin(2*PI*0.25*t))"
    music = os.path.join(work, "music.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-t", str(total), "-i",
                    f"aevalsrc='{expr}':s=44100:c=stereo", "-af",
                    f"lowpass=f=1400,afade=t=in:d=1.5,afade=t=out:st={max(total-2,0)}:d=2", music], check=True)
    mix = os.path.join(work, "mix.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", voice, "-i", music, "-filter_complex",
                    "amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", "44100", mix], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(fdir, "f%05d.jpg"),
                    "-i", mix, "-shortest", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "19",
                    "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", spec["out"]], check=True)
    shutil.rmtree(work)
    print("wrote", spec["out"], total, "s")


if __name__ == "__main__":
    render(json.load(open(sys.argv[1])))
