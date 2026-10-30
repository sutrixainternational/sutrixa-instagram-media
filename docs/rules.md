> **30 Oct 2026 ONLY (owner approved):** the main session publishes the story Reel "Bablu ka Hotel, EP 1" (Rizstay, Hinglish, 85s, keyword LEAK) at about 7:30 PM IST. Today's 6:47 PM run must NOT render or post another Reel. Do the post-mortem, write the owner pack (LEAK keyword DM with freebies/LEAK_2026-10-30.png, Story frames, replies, comments) and log nothing new in posted.md (the main session logs it).

# Standing content rules (@sutrixainternational)

> **OWNER RULE (30 Oct 2026): NO PRODUCT PRICING anywhere** (Reels, voiceover, on-screen text, captions, Stories, highlights, carousels, freebies, comment/DM drafts). No prices, plan costs, per-minute rates, credits or discounts. Price questions get: "Prices depend on your setup. DM us or book a demo at sutrixa.com/connect." Tax figures used to teach (e.g. GST slabs, ₹ worked examples) are fine; they are not product prices. Hard gate before posting. Freebies are rendered with tools/freebie.py, which refuses any spec containing a price.
- Every Reel opens with REAL moving Gemini video (Veo, 9:16) with its audio. Never stand in a screenshot, still frame or placeholder, not even in a preview sent to the owner.
- If no new Gemini clip is in Drive, never skip the day (owner rule, 24 Oct): reuse the least-recently-used real Gemini clip from "3 - Posted" (not used in the last 3 days) with a new angle and segment. Never use stills.
- Reels must explain, not list: problem (Gemini clip) -> what the product does -> numbered steps on the real product screen with the exact UI element highlighted -> one-line outcome -> logo end card. 15-20s (see Length below).
- Sutrixa logo on every frame. Facts only from /root/.claude/instagram/products.md.
- Renderer: scratchpad/render_reel2.py (video beats, step badges, highlight boxes, music bed).
- EVERY Reel has a voice (owner rule, 24 Oct). Use the free local Kokoro TTS in scratchpad/tts (render_reel2.py: "say" per beat, "voice" in spec, refuses to render with no voice). Never vidIQ voiceover (owner will not pay). No voice = do not post.
- Storage: videos live in Google Drive only (owner rule). Never use the laptop's folders. Drive "Sutrixa Instagram" and "2 - Ready to post" are public-link (checked 24 Oct).
- Pipeline that works: Drive -> workspace via Google_Drive download_file_content (result saved to tool-results file; decode with scratchpad/drive_pull.py). Workspace -> Drive via Chrome file_upload into Drive's own upload input (patch HTMLInputElement.click to capture it, then New > File upload). Drive public link -> vidiq_video_upload -> vidiq_instagram_publish_reel.
- Gemini -> Drive is the open gap: cross-tab messaging is cut by the browser, and passing clip data through tool output is blocked. Don't retry either.

## Reach rules (24 Oct, "optimise every way possible")
- Length (changed 25 Oct weekly review): main Reel 15-20s, Trial Reel 9-12s. Evidence: viewers leave at about 4s whatever the length (median average watch 4.3s across 13 Reels). That gave 9s Reels about 50% watched and 24-32s Reels 8-25% (7 of 8). Two steps on screen, not three. Keep voice speed 1.12-1.18 and cut beats rather than rushing. Owner can revert to 25-35s.
- Frame 1 = hook: the hook text and the Gemini clip are both on screen from frame 0 (Instagram uses the first frame as the grid cover). No fade-in on beat 1.
- The hook must work on mute: on-screen text states the problem in 8 words or fewer.
- One product per Reel. Rotate Rizstay, Voxa, HR4U and Velocity (Velocity only as stated in products.md). Rizstay gets 2 of every 5 posts: it has the best real screens.
- Caption: put the search phrase in a normal sentence in the first two lines. Use one ask, rotating between "save this", "send this to a hotel owner" and "comment DEMO". Use DEMO only if the owner has agreed to handle DMs.
- (SUSPENDED 27 Oct: Meta refuses Trial Reels for this app, code 10/2207081.) Daily Trial Reel: after the main Reel is posted, render a second cut from the same clip, with a different hook formula from ig-reel and a different product step order. Publish it as a Trial Reel with trialParams {graduationStrategy: "SS_PERFORMANCE"}. Instagram shows it to non-followers first, and auto-shares it to followers if it performs. Log both posts.

## Hook guidance (weekly review, 25 Oct)
- The gate is real: hookscore.py >= 75 on the line that is actually on screen at frame 0. The 24 Oct hook ("Your hotel's accountant. 11 PM. Again.") scores 54.8, so it went out under the gate. Log the score in docs/posted.md for every post.
- What scored >= 75 this week: #2 Negative Command with a concrete object ("Stop writing KOTs by hand. 1 lost slip is 1 angry table." 95; "Stop splitting CGST and SGST yourself. Your bill can do it." 81; "Stop adding room and restaurant GST by hand at 11 PM." 80) and #20 Permission ("Your 20-room hotel doesn't need an enterprise system." 78).
- Name the thing they touch: GST, KOT, register, CA, front desk, 11 PM. "Front desk never slept" and "guests judge your hotel" scored 45-49 and got 10-17 views.
- Never a question or a poll as the hook (20 Oct poll: 35, 12 views). Never the brand name in the hook (25).
- Numbers in hooks must be true or obviously the viewer's own situation. No invented stats ("loses 1 order a night") and no competitor prices.
- First 2 seconds: problem visible in the Gemini clip AND stated in 8 words or fewer on screen. The audience leaves at 3-4s, so the payoff of the hook must land inside 2s.
- Presets (27 Oct, owner: "not a fixed preset for every reel"): every Reel uses a trend preset from docs/presets.md via tools/render_reel3.py, rotated, with no preset repeated within 3 days (Trial Reels are refused by Meta, so A/B across days). The weekly review re-weights presets from the results.

- Informative + algorithm (27 Oct): read docs/algorithm.md. Every Reel teaches ≥ 3 concrete facts, is 30-50s (proof preset 15-25s at most 1 in 5), and is built to be sent or saved. This overrides the 25 Oct 15-20s length rule.

- Company-wide (27 Oct, owner): Sutrixa sells Rizstay, Voxa, HR4U and Velocity, not only Rizstay. Follow the pillar shares and the weekly calendar in docs/strategy.md (Mon HR4U · Tue Rizstay · Wed Voxa · Thu Rizstay · Fri Velocity · Sat Voxa · Sun HR4U or the week's best). Each Reel belongs to a named series and ends with "Follow for one business fix a day."

- **Ask placement (PROVEN 28 Oct, lessons.md):** never rely on an end-only ask. 3 Reels in a row with an end-only "share this" got 0 shares. Every Reel puts its send/save ask mid-Reel at the strongest fact, then repeats or swaps it at the end.
- **Teach with numbers the viewer doesn't already know (PROVEN 29 Oct, lessons.md):** GST/tax Reels hold ~2x longer than Voxa missed-call Reels (13.6-15.7s vs 7.6-8.8s). Every Reel's strongest fact is a ₹ figure, a date, a rate or a rule, never a USD price or a feature claim.
- **Read Reels at 24h** for post-mortems (1h numbers come from warm viewers and overstate retention).

## Viral playbook (live Instagram scan, 27 Oct; see docs/swipe.md)
- **Every Reel belongs to a numbered series** with a visible top label: "PART 3" (eli5), "#5 → #1" (countdown) or "1/3" (tips). The end card promises the next part and day ("Part 4 tomorrow"), which gives a reason to follow.
- **Length 40-60s** for eli5/countdown/tips (the winners we saw ran 37-82s). A new visual or fact every 2-4s, no padding. Proof stays 15-25s.
- **One everyday analogy per jargon word** (the ELI5 rule). No unexplained jargon anywhere in the voice.
- **The mid-Reel send ask** sits at the strongest fact: "Send this to whoever does your billing". The end asks for a comment: "Which word should I explain next?" Comments become the next topics in docs/clip_topics.md.
- **Caption:** line 1 is the payoff plus the series name. Add one short Hinglish line for Indian owners (e.g. "Bill galat toh GST galat."), then the facts as lines. The voice stays English.
- **Comment-KEYWORD giveaways: ON (owner, 27 Oct, "yes do it").** At most every other Reel (alternate with the send ask so the account doesn't look like a bait page). Rules:
  1. One short keyword that matches the Reel, e.g. GST, PAYROLL, CALLS, LEADS. Say it in the voice ("Comment GST and I'll send you the checklist"), show it on the end card, and put it in caption line 2.
  2. The freebie must exist BEFORE posting: a one-page checklist built only from facts in the Reel and docs/products.md. Render it as a 1080x1350 PNG (and PDF) with the logo, commit it to main at freebies/<KEYWORD>_<date>.png, and use its raw.githubusercontent.com link. Log it in docs/freebies.md (keyword, Reel, link).
  3. The owner pack (ig-dm) gives the owner a copy-ready DM for that keyword: thanks + the link + one soft question ("Do you bill by hand or on software right now?"), plus 2 follow-ups for people who reply. The owner sends them from the app within a few hours. The system never sends DMs or replies.
  4. Ask the commenter to follow ("Follow so the DM doesn't land in requests"): Instagram puts DMs from non-followed accounts in requests, and the ask also converts commenters to followers.
  5. Never promise something the owner can't deliver (no "free demo call" unless the owner says so).
- Don't model on hotel/restaurant news accounts (low engagement). Model on business-education creators.

## Stay on trend (owner, 27 Oct: "always be updated what's trending")
- Every day the laptop task scans Instagram (read-only, in the logged-in built-in browser) and appends to docs/trends.md: 5-10 Reels from Explore, the Reels feed and searches ("business tips", "GST", "restaurant business", "hotel business", "small business India", "AI tools"), with likes, comments, shares, length, hook text and format, plus 3 lines on "what fits Sutrixa".
- The daily Reel run reads the latest docs/trends.md entry first. If a format has appeared 2+ days in a row with strong numbers and fits our brand, adapt it today (our facts, our footage, our voice; never copy anyone's video, audio or words). New formats get added to docs/presets.md as recipes.
- Trending ≠ fits. Skip dances, memes about people, politics, and any trend that needs a face on camera (we are faceless), or claims we can't back.

## Stories and Highlights (owner, 28 Oct: "create highlights, post stories")
- Every day has a 5-frame Story sequence rendered by tools/story.py (see skill_workflow step 6). Today's Voxa set: stories/2026-10-28_daily.json.
- Highlights (set up once, then kept fresh): START · RIZSTAY · VOXA · HR4U · VELOCITY, from stories/highlights_v1.json, with covers from tools/story_cover.py. Add a FREEBIES highlight once the first keyword checklist exists, and a REELS-of-the-week story every Sunday.
- Publishing: the Instagram API used here can't post Stories, and instagram.com on desktop has no Story upload. Stories are posted by the owner from the phone, or by the laptop task through Meta Business Suite (business.facebook.com) once the owner has logged into it in the built-in browser. Never type a login.

## From the external skills (28 Oct, see docs/skills_ext.md)
- Trend scan: for the 2 strongest Reels each day, write an edit-anatomy beat sheet (shot, cut rhythm, on-screen text, caption style, motion, overlays, sound, hook frame, pacing curve) and 3-5 signature moves in docs/trends.md. Copy the editing grammar only, never their script, footage, audio or bit.
- Comments without saves are a red flag (claude-ig algorithm-2026). Keyword days must still carry a save line and a screenshot-worthy frame, so the freebie Reel also teaches.
- Every Reel passes the screenshot test: one frame worth screenshotting.
- Stories: 3-7 a day is the cadence for accounts under 10k (claude-ig). Never more than 7.
- Captions and scripts: marketingskills/social "No AI tells": no "it's not X, it's Y", no "The result? ...", no broetry, no engagement bait ("Agree?"), no emoji bullets, no em dashes.

## Human voice (owner, 30 Oct: "voiceover is very humanly" on DbzTILTNcyZ)
- That Reel (8 Aug, 9.4s) got avg watch 34.9s = **387% watched** (people replayed it ~4x), the best retention the account has ever had. Its voice is not TTS: it is **Veo's own generated dialogue/audio inside the Gemini clip**.
- From now on, prefer **Veo native voice**: write the spoken line INTO the Gemini video prompt (`He says in Hindi, with a natural warm voice: "..."`), keep each line under ~7 seconds so it fits one 8s clip, and keep the clip's own audio at full volume in the render (no Kokoro over it).
- Story Reels: characters speak their own lines in Veo clips (one clip per key line, Hinglish). Kokoro narration only fills gaps (product screens, the end card) and should be minimal. Never mix two different voices for the same character.
- Short "moment" Reels like DbzTILTNcyZ (one relatable 8-10s scene with dialogue + a one-line caption) are a valid format again: they loop, and replays count. Add the logo, keep captions of the dialogue, no screen beats needed.
- Gemini video quota is limited per day: the hourly clip task should spend it on dialogue clips first.
