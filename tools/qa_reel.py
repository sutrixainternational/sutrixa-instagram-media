#!/usr/bin/env python3
"""Hard quality gate for every Reel (owner, 8 Nov 2026: "check the quality of the content you posted").

usage:
  python3 tools/qa_reel.py spec  spec.json            # before rendering (render_reel3 runs this)
  python3 tools/qa_reel.py video spec.json out.mp4    # after rendering (render_reel3 runs this)

Refuses, with reasons, anything that made the 4 Nov and 7 Nov Reels bad:
  - computer (Kokoro/TTS) narration. Every voiced beat must be a real Veo dialogue clip
    (clip_voice) or carry a clip's audio (audio_src). Only the owner can lift this: "owner_ok_tts": true.
  - one clip carrying the Reel: a single video file may be on screen at most 12 s in total
  - beats longer than 9 s (a new visual every few seconds)
  - app screenshots too short to fill a phone screen (height/width < 1.6), which the renderer
    stretches and smears; highlight boxes outside the screenshot
  - length outside 40-60 s; loudness outside -16..-12 LUFS; black frames; frozen picture > 2.5 s
"""
import json, os, re, subprocess, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_PER_VIDEO = 12.0
MAX_BEAT = 9.0
MIN_ASPECT = 1.6


def _p(path):
    return path if os.path.isabs(path) else os.path.join(ROOT, path)


def check_spec(spec):
    errs, per_video, total = [], {}, 0.0
    for i, b in enumerate(spec.get("beats", []), 1):
        dur = float(b.get("dur") or 0)
        total += dur
        say = (b.get("say") or "").strip()
        voiced_by_clip = b.get("clip_voice") or b.get("audio_src")
        if say and not voiced_by_clip and not spec.get("owner_ok_tts"):
            errs.append(f"beat {i}: computer voice (TTS) for \"{say[:40]}\". Use a real Veo dialogue clip (clip_voice) or a clip's audio (audio_src)")
        if not dur:
            errs.append(f"beat {i}: no fixed dur (only clip-voiced beats with explicit dur are allowed)")
        if dur > MAX_BEAT:
            errs.append(f"beat {i}: {dur:.1f}s on one visual (max {MAX_BEAT}s)")
        if b.get("kind") in ("clip", "card", "split") and b.get("video"):
            per_video[b["video"]] = per_video.get(b["video"], 0) + dur
        if b.get("kind") == "screen" and b.get("image"):
            try:
                im = Image.open(_p(b["image"]))
                if im.height / im.width < MIN_ASPECT:
                    errs.append(f"beat {i}: screenshot {b['image']} is {im.width}x{im.height}; too short for a phone screen (needs height/width >= {MIN_ASPECT}). Use a taller capture")
                hl = b.get("hl")
                if hl and (hl[0] < 0 or hl[1] < 0 or hl[2] > im.width or hl[3] > im.height or hl[2] <= hl[0] or hl[3] <= hl[1]):
                    errs.append(f"beat {i}: highlight box {hl} is outside {b['image']} ({im.width}x{im.height})")
            except FileNotFoundError:
                errs.append(f"beat {i}: missing image {b['image']}")
    for v, s in per_video.items():
        if s > MAX_PER_VIDEO:
            errs.append(f"{v} is on screen {s:.1f}s in total (max {MAX_PER_VIDEO}s): one clip must not carry the Reel")
    if not 40 <= total <= 60:
        errs.append(f"planned length {total:.1f}s (owner rule: 40-60s)")
    return errs


def check_video(path):
    errs = []
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
                               capture_output=True, text=True).stdout.strip() or 0)
    if not 40 <= dur <= 60.5:
        errs.append(f"rendered length {dur:.1f}s (40-60s)")
    log = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128", "-vf",
                          "blackdetect=d=0.3:pix_th=0.08,freezedetect=n=0.002:d=2.5", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)
    if m and not -16 <= float(m[-1]) <= -12:
        errs.append(f"loudness {m[-1]} LUFS (want about -14)")
    for bs, be in re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", log):
        errs.append(f"black frames {bs}-{be}s")
    for fs in re.findall(r"freeze_start: ([\d.]+)", log):
        errs.append(f"frozen picture from {fs}s (>2.5s without change)")
    return errs


if __name__ == "__main__":
    mode, spec_path = sys.argv[1], sys.argv[2]
    spec = json.load(open(spec_path))
    e = check_spec(spec) if mode == "spec" else check_video(sys.argv[3])
    if e:
        print("QA REFUSED:\n" + "\n".join(" - " + x for x in e))
        sys.exit(1)
    print("QA OK")
