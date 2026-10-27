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
| **quiz** | 25-35s | `clip` question → `screen` options → `screen`/`clip` explain the answer with facts → `card` "comment your number" | Comments + teaching. Never invent a "right answer" claim |

**Informative rule (owner, 27 Oct):** every Reel teaches at least 3 concrete, checkable facts or steps (see docs/algorithm.md). If the script has fewer, add beats; don't stretch the beats. A new visual every 2-4s.

## Rotation rules
- The main Reel never uses the same preset as either of the previous 2 days (see docs/posted.md).
- Trial Reels are refused by Meta for this app (code 10 / 2207081, 25-26 Oct), so do not render or post them. Instead, A/B test formats across days: no preset twice in 3 days, and every preset runs at least once a week. Log the preset in docs/posted.md.
- The weekly review (ig-audit) ranks presets by views per account median, watch %, skip rate and shares+saves. Then it sets weights here.

## Weights (updated weekly by the review)
eli5 4 · countdown 4 · tips 3 · stages 2 · pov 2 · quiz 1 · proof 1 (27 Oct live scan: series formats get the most shares/saves; the weekly review re-weights from our own results)

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
