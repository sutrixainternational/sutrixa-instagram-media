#!/usr/bin/env python3
"""Refuse a Reel that repeats content already posted (owner rule, 4 Nov 2026).

usage:
  python3 tools/no_repeat.py check  spec.json      # exit 1 + reasons if it repeats
  python3 tools/no_repeat.py record spec.json DATE URL   # after posting, add it to the ledger

The spec must carry a "meta" block:
  "meta": {
    "story": "HR4U: staff attendance + leave + salary slips",   # one-line plot / angle
    "clips_src": ["2026-11-04_dlg_ep3_staff_call.mp4", ...],      # Drive file names of every clip used
    "facts": ["hr4u_clockin_one_tap", "hr4u_live_view", ...],      # short fact ids taught
    "hook": "on-screen hook text",
    "lang": "en" or "hi"                                           # alternate with the last Reel
  }
Spoken lines are read from every beat's "say".

Characters may repeat. These may NOT:
  - any clip file already used in a posted Reel (no reused footage, no reused dialogue)
  - a spoken line or hook that is >= 60% similar to one already posted
  - a fact id taught in the last 21 days (teach something new; same product is fine)
  - the same story angle (>= 60% similar) as any earlier Reel
"""
import datetime as dt, difflib, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "docs", "used_content.json")
SIM = 0.60
FACT_DAYS = 21
TOPIC_DAYS = 14


def norm(s):
    return re.sub(r"[^a-z0-9₹% ]+", " ", (s or "").lower()).split()


def sim(a, b):
    a, b = " ".join(norm(a)), " ".join(norm(b))
    if not a or not b:
        return 0.0
    return difflib.SequenceMatcher(None, a, b).ratio()


def lines_of(spec):
    out = []
    for b in spec.get("beats", []):
        s = (b.get("say") or "").strip()
        if len(norm(s)) >= 3:
            out.append(s)
    return out


def load():
    return json.load(open(LEDGER)) if os.path.exists(LEDGER) else {"posts": []}


def check(spec, today=None):
    led = load()
    meta = spec.get("meta") or {}
    errs = []
    for k in ("story", "clips_src", "facts", "hook", "lang", "topic"):
        if not meta.get(k):
            errs.append(f"meta.{k} missing: the spec must declare it")
    # Owner rule 6 Nov 2026: alternate languages, one English Reel then one Hindi Reel.
    if meta.get("lang") and meta["lang"] not in ("en", "hi"):
        errs.append(f"meta.lang must be 'en' or 'hi', got {meta['lang']!r}")
    if meta.get("lang") and led["posts"]:
        valid = [p for p in led["posts"] if not p.get("rejected_by_owner")]
        last = sorted(valid, key=lambda p: p["date"])[-1]
        if last.get("lang") == meta["lang"]:
            errs.append(f"language repeats: the last Reel ({last['date']}) was also '{meta['lang']}'. Alternate English and Hindi (owner rule 6 Nov)")
    today = today or dt.date.today()
    # Owner 8 Nov: a SUBJECT may not come back within 14 days, however the facts are worded.
    # topic = short subject id from docs/topics.md, e.g. gst_hotel, voxa_missed_calls, hr4u_attendance_payroll
    for p in led["posts"]:
        age = (today - dt.date.fromisoformat(p["date"][:10])).days
        if meta.get("topic") and p.get("topic") == meta["topic"] and age <= TOPIC_DAYS:
            errs.append(f"topic '{meta['topic']}' was already the subject on {p['date']} ({age} days ago; cool-down {TOPIC_DAYS} days)")
    used_clips = {c.lower(): p["date"] for p in led["posts"] for c in p.get("clips_src", [])}
    for c in meta.get("clips_src", []):
        base = re.sub(r"^used_[0-9+\-_]*", "", c.lower())
        for u, d in used_clips.items():
            ub = re.sub(r"^used_[0-9+\-_]*", "", u)
            if base == ub or base in ub or ub in base:
                errs.append(f"clip reused: {c} (already in the {d} Reel)")
                break
    for ln in lines_of(spec):
        for p in led["posts"]:
            for old in p.get("lines", []):
                r = sim(ln, old)
                if r >= SIM:
                    errs.append(f"spoken line repeats {p['date']} ({r:.0%}): \"{ln}\" ~ \"{old}\"")
    for p in led["posts"]:
        r = sim(meta.get("hook", ""), p.get("hook", ""))
        if r >= SIM:
            errs.append(f"hook repeats {p['date']} ({r:.0%}): \"{p.get('hook')}\"")
        r = sim(meta.get("story", ""), p.get("story", ""))
        if r >= SIM:
            errs.append(f"story angle repeats {p['date']} ({r:.0%}): \"{p.get('story')}\"")
        age = (today - dt.date.fromisoformat(p["date"][:10])).days
        if age <= FACT_DAYS:
            dup = set(meta.get("facts", [])) & set(p.get("facts", []))
            if dup:
                errs.append(f"facts already taught {p['date']} ({age} days ago): {sorted(dup)}")
    return errs


def record(spec, date, url):
    led = load()
    meta = spec["meta"]
    led["posts"].append({"date": date, "url": url, "story": meta["story"], "hook": meta["hook"],
                         "clips_src": meta["clips_src"], "facts": meta["facts"], "lang": meta.get("lang"), "topic": meta.get("topic"), "lines": lines_of(spec)})
    json.dump(led, open(LEDGER, "w"), ensure_ascii=False, indent=1)
    print(f"recorded {date} in {LEDGER}")


if __name__ == "__main__":
    cmd, path = sys.argv[1], sys.argv[2]
    spec = json.load(open(path))
    if cmd == "check":
        e = check(spec)
        if e:
            print("REFUSED: repeats posted content (owner rule 4 Nov: no repeated content)")
            print("\n".join(" - " + x for x in e))
            sys.exit(1)
        print("OK: nothing repeats")
    elif cmd == "record":
        record(spec, sys.argv[3], sys.argv[4])
