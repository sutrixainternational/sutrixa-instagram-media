# Reel presets (trend-based, Oct 2026). Rendered by tools/render_reel3.py

These are the formats that are working now. Sources: Lightreel's weekly IG trend report (17-24 Oct 2026), Klap's 2026 Reels trends, Lilach Bullock's "which Reels get more views" and DesignerBox's faceless formats.
Shared style on every preset: full-bleed footage (not cards on a gradient), a small Sutrixa logo in the corner on every frame, word-by-word kinetic captions synced to the Kokoro voice (current word in yellow), beat punch-ins, a loop back to frame 1, and the hook on screen from frame 0.
Instagram shows mostly-text Reels less: footage or real screens must fill the frame, and text is only headline + captions.

| preset | length | structure (beats) | best for |
|---|---|---|---|
| **tips** (core) | 40-55s | `clip` hook "3 registers your CA asks for every month" → 3-5 × `screen`/`clip` beats labelled "1/3", "2/3"… Each teaches one concrete fact with tap+zoom on the real UI → `card` "send this to your accountant" | Teaching, saves and sends. HR4U month end, GST basics, Voxa setup |
| **stages** | 30-45s | `clip` hook → `split` BEFORE (clip) / AFTER (screen with hl) → 2-3 × `screen` "STEP 1/2/3", explaining what changes and why → `card` | Before/after with the how |
| **pov** | 30-40s | `clip` "POV" + a specific moment → `clip` escalation → 2-3 × `screen` "here's the fix", each with a fact → `card` | Relatable pain, then a taught fix |
| **proof** | 15-25s | `clip` contrarian/"stop" headline → `screen` tap+zoom proof → 1-2 × `screen` fact → `card` | A single striking claim. At most 1 in 5 posts |
| **eli5** (series, NEW 27 Oct) | 40-60s | `clip` hook "<stakes>. <jargon>, explained like you're 5." with top_label "PART N" → 1 analogy beat (`clip`, everyday object) → 2-3 × `screen`/`clip` with the real fact and numbers → `screen` where it shows in the product → `card` "Which word should I explain next? Comment it. Part N+1 tomorrow." | Jargon the owner hears but never had explained: GST input credit, CGST/SGST, KOT, TDS on salary, PF/ESI, AI receptionist, Google Business Profile |
| **countdown** (series, NEW 27 Oct) | 45-60s | `clip` hook "Stop these 5 <mistakes>. Number 1 costs you every <time>." → 5 × beats labelled "#5" down to "#1", each one mistake + its fix with a fact → `card` "Save this. Part 2 Friday." | Mistakes lists. The most saves. Biggest-stakes item last so people stay |
| **story** (series, NEW 30 Oct, owner-approved) | 70-90s | Recurring original 3D-cartoon characters (Bablu = owner, Kaka = tea-stall mentor; never resemble real people) drawn in Gemini images → `scene` beats with Ken Burns → problem escalates (2-3 scenes) → mentor names the concept ("paisa teen jagah se leak") → each point = scene + real product `screen` with a fact → payoff scene → contrast `card` ("thaka owner vs smart owner") → share card + "EP N+1". Hinglish voice (hm_omega, lang hi, Devanagari `tts`, Roman captions), `bed: pad`. Spec: stories/specs/bablu_ep1_hinglish.json | Selling through a story; 2x a week max |
| **counter** (NEW 1 Nov, weekly review) | 30-40s | ONE persistent background for the whole Reel (a real product screen or a plain canvas) with a fixed stat chip in one corner that climbs beat by beat ("registers on 1 screen: 1/5 → 5/5", "missed calls answered: 0 → 5", "₹ kept: ₹0 → ₹800"). `clip` hook (≤ 6 words, problem in motion, chip already visible at 0) → 3-5 × `screen` beats on the same background, each lights one item with an `hl` box, a numbered card ("01"…"05") and one fact; the chip ticks up on every beat → `card` final number + SAVE/SEND. Ask by 8s. Numbers must be the viewer's own maths, a labelled example, or from docs/products.md: never an invented result | Any list where progress can be counted. Source: docs/trends.md 29 Oct (aiwith.om "5 jagah": canvas + counter 0 → 40 users, 191 shares) and 30 Oct (simulateitnow: one persistent scene + live % bars, 7,686 shares on 92K likes). 2 days running, faceless, fits render_reel3 screen beats |
| **quiz** | 25-35s | `clip` question → `screen` options → `screen`/`clip` explain the answer with facts → `card` "comment your number" | Comments + teaching. Never invent a "right answer" claim |

**Informative rule (owner, 27 Oct):** every Reel teaches at least 3 concrete, checkable facts or steps (see docs/algorithm.md). If the script has fewer, add beats; don't stretch the beats. A new visual every 2-4s.

## Rotation rules
- The main Reel never uses the same preset as either of the previous 2 days (see docs/posted.md).
- Trial Reels are refused by Meta for this app (code 10 / 2207081, 25-26 Oct), so do not render or post them. Instead, A/B test formats across days: no preset twice in 3 days, and every preset runs at least once a week. Log the preset in docs/posted.md.
- The weekly review (ig-audit) ranks presets by views per account median, watch %, skip rate and shares+saves. Then it sets weights here.

## Weights (updated weekly by the review)
tips 4 · counter 3 · countdown 2 · eli5 2 · story 2 · stages 2 · pov 2 · proof 2 · quiz 1 (1 Nov review, from the latest reads we have; vidIQ was disconnected so no new pull. tips 27 Oct = best: 92 views 1.36x median, 13.6s avg, 29.5% watched, 1 share. countdown 28 Oct: 55 views 0.81x, 8.1s, 16.9%. eli5 29 Oct: 67 views 0.99x, 6.3s, 10.7%, worst skip 80.9%. story EP1 30 Oct and countdown Part 2 31 Oct: no numbers yet, so held at 2. proof up 1 → 2 because avg watch is 6-14s on every Reel and proof is the only preset that fits inside it (still max 1 in 5). counter is new, weighted 3 on 2 days of strong trend data. n = 1 Reel per preset, and preset is mixed up with product (tips/eli5 = Rizstay, countdown = Voxa): these are bets, not proof)

## Hooks
Live scan 27 Oct, scored with hookscore.py: "Stop these 5 billing mistakes. Number 1 costs you every night." 93.8 · "Your 5 GST mistakes. Number 1 costs you every month." 84.4 · "You're losing money on GST input credit. Explained like you're 5." 79.4. A bare "explained like you're 5" with no stakes scores only 51-55, so **ELI5 hooks always lead with the money/stakes**. "Are you also scared of…?" scored 28: don't use it.
Run ig-reel's hookscore.py and use only hooks ≥ 75. Trending hook shapes that score well:
- "Stop <costly habit>…" (80)
- "Don't tell other <audience> about this <thing>" (79)
- a specific pain at a specific moment
- a contrarian claim, then instant proof
- "POV:", kept short: hookscore penalises length

CTA: "Comment <KEYWORD>" is trending, but only use it if the owner handles DMs. Otherwise use "save this" or "send this to a hotel owner".

## Research
Weekly: ig-viral with WebSearch/WebFetch for the latest trend reports and niche outliers. Agent Reach (`agent-reach`, installed from github.com/Panniantong/agent-reach) can read Instagram, YouTube and Reddit. In the cloud it only works if the owner allows those domains in claude.ai Settings > Capabilities, and Instagram also needs a login. Try `agent-reach doctor --text`, and if channels show blocked, fall back to WebSearch.

### 1 Nov review
Agent Reach could not be installed this run (the install was blocked in this session), so research used WebSearch/WebFetch plus the laptop's live Instagram scans in docs/trends.md (28-30 Oct). Also on watch, not yet a preset: "What even is <jargon>?" (NewEngen's "WTF is…" trend, under 15s, text up 2-3s, cut to the product: our wording drops the swear, voice.md) and Lightreel 17-24 Oct "6-18s proof Reels" and "don't tell your friends" app demos with keyword delivery. Both back short Reels; test them through the proof preset first.
