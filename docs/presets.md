# Reel presets (trend-based, Oct 2026). Rendered by tools/render_reel3.py

These are the formats that are working now. Sources: Lightreel's weekly IG trend report (17-24 Oct 2026), Klap's 2026 Reels trends, Lilach Bullock's "which Reels get more views" and DesignerBox's faceless formats.
Shared style on every preset: full-bleed footage (not cards on a gradient), a small Sutrixa logo in the corner on every frame, word-by-word kinetic captions synced to the Kokoro voice (current word in yellow), beat punch-ins, a loop back to frame 1, and the hook on screen from frame 0.
Instagram shows mostly-text Reels less: footage or real screens must fill the frame, and text is only headline + captions.

| preset | length | structure (beats) | best for |
|---|---|---|---|
| **proof** | 8-15s | `clip` + contrarian/"stop" headline → `screen` tap+zoom on the exact UI (the proof) → `screen` 2nd tap → `card` keyword CTA | One claim, proven instantly. Rizstay registers/GST, Voxa pricing page |
| **pov** | 10-18s | `clip` label "POV" + "POV: it's 8 PM and the phone won't stop" → `clip` 2nd segment (escalation) → `screen` the fix → `card` | Relatable pain: Voxa missed calls, month end, kitchen rush |
| **stages** | 12-20s | `clip` hook → `split` BEFORE (clip) / AFTER (screen with hl) → `screen` "STEP 2" → `card` | Before/after transformations |
| **tips** | 18-30s | `clip` "3 signs your hotel needs…" → 3 × `screen` labelled "1/3", "2/3", "3/3" → `card` save CTA | Saves: checklists, HR4U month-end, GST tips |
| **quiz** | 8-14s | `clip` question headline ("Which register does your CA ask for first?") → `screen` showing the options (hl the tabs) → `card` "Comment the number" | Comments: interaction bait. Never invent a "right answer" claim |

## Rotation rules
- The main Reel never uses the same preset as either of the previous 2 days (see docs/posted.md).
- Trial Reels are refused by Meta for this app (code 10 / 2207081, 25-26 Oct), so do not render or post them. Instead, A/B test formats across days: no preset twice in 3 days, and every preset runs at least once a week. Log the preset in docs/posted.md.
- The weekly review (ig-audit) ranks presets by views per account median, watch %, skip rate and shares+saves. Then it sets weights here.

## Weights (updated weekly by the review)
proof 3 · pov 3 · stages 2 · quiz 2 · tips 1

## Hooks
Run ig-reel's hookscore.py and use only hooks ≥ 75. Trending hook shapes that score well:
- "Stop <costly habit>…" (80)
- "Don't tell other <audience> about this <thing>" (79)
- a specific pain at a specific moment
- a contrarian claim, then instant proof
- "POV:", kept short: hookscore penalises length

CTA: "Comment <KEYWORD>" is trending, but only use it if the owner handles DMs. Otherwise use "save this" or "send this to a hotel owner".

## Research
Weekly: ig-viral with WebSearch/WebFetch for the latest trend reports and niche outliers. Agent Reach (`agent-reach`, installed from github.com/Panniantong/agent-reach) can read Instagram, YouTube and Reddit. In the cloud it only works if the owner allows those domains in claude.ai Settings > Capabilities, and Instagram also needs a login. Try `agent-reach doctor --text`, and if channels show blocked, fall back to WebSearch.
