# Growth log: @sutrixainternational
Target set by the owner: 100,000 followers by 24 Nov 2026. Every number here is from vidIQ owner insights (Instagram's own data). Nothing is rounded up.

## Week ending 25 Oct 2026 (first weekly review)

### Numbers
- Followers: **4**. Last week: not logged (this is the first entry, so there is no baseline to compare).
- Gap to target: **99,996** followers in 30 days, which would mean about 3,333 new followers a day. Lifetime the account has 740 views and has gained 4 followers. On the current path the target will not be reached, and no change in this plan makes it reachable by 24 Nov. The honest goal for the next 30 days is the first 100-500 followers and the first Reel past 1,000 views.
- Views, last 30 days (Instagram summary): 662.
- Reels on the account: 13. Trial Reels found: **0** (isPossibleTrial false on all 13), so the daily Trial Reel step has not run yet.
- vidIQ credits: 0 (refill 13 Nov), so no paid outlier search or profile lookup this week.

| date | product | hook (first line) | len | views | x median | avg watch | watched | skip | shares | saves |
|---|---|---|---|---|---|---|---|---|---|---|
| 24 Oct | Rizstay | Your hotel's accountant. 11 PM. Again. | 32s | 69 | 2.7x | 3.6s | 11% | 68% | 1 | 0 |
| 20 Oct | AI poll | You can hand ONE task to AI today. Which one? | 24s | 12 | 0.5x | 4.1s | 17% | 33% | 0 | 0 |
| 19 Oct | Rizstay | Guests judge your hotel before they say hello. | 24s | 10 | 0.4x | 3.8s | 16% | 78% | 0 | 0 |
| 18 Oct | Velocity | Sales target hit. Real sales? Not yet. | 24s | 74 | 2.8x | 1.9s | 8% | 88% | 0 | 0 |
| 17 Oct | Automation list | 3 tasks to automate before Monday | 24s | 61 | 2.3x | 3.3s | 14% | 92% | 0 | 0 |
| 16 Oct | Voxa | Missed your kid's game for a client call? | 24s | 26 | 1.0x | 3.6s | 15% | 70% | 0 | 0 |
| 14 Oct | Rizstay | Hotel owners, what if your front desk never slept? | 24s | 17 | 0.7x | 6.0s | 25% | 46% | 0 | 0 |
| 14 Oct | Brand | Your business runs 24/7. Your team can't. | 24s | 17 | 0.7x | 11.6s | 49% | 73% | 0 | 0 |
| 11 Sep | Brand | (no caption) | 8s | 14 | 0.5x | 7.9s | 98% | 50% | 0 | 0 |
| 11 Sep | Brand | Introducing SUTRIXA INTERNATIONAL | 8s | 11 | 0.4x | 4.3s | 54% | 71% | 0 | 0 |
| 12 Aug | Rizstay | The Ultimate Experience of Running Your Hospitality Business by Itself. | 9s | 194 | 7.5x | 4.5s | 49% | 55% | 0 | 0 |
| 9 Aug | Voxa | After we reach 30s, its a juggle between family n work. | 9s | 61 | 2.3x | 39.3s | 436% (loops) | 62% | 0 | 1 |
| 30 Jul | Velocity | Automation? We Do It The Best. | 9s | 174 | 6.7x | 4.9s | 54% | 60% | 0 | 0 |

Median views 26 (all 13), 21.5 (the 8 since 14 Oct). Hook score = hookscore.py on the caption's first line (the on-screen hook was only logged for 24 Oct).

### ig-audit: what the data says (n=13, low confidence on everything)
1. **The hook is the whole problem.** Median average watch is 4.3s whatever the length. People decide in the first 3-4 seconds and leave. Skip rate is 46-92% on every Reel since 14 Oct.
2. **Length:** because everyone leaves at about 4s, the 9s Reels got about 50% watched and the 24-32s Reels 8-25%. The 9s Reels also have the most views (mean 91 vs 36), but they are 2-3 months old and had longer to collect them, so treat that part as weak. Decision: main Reels 15-20s, Trial Reels 9-12s.
3. **By product:** Rizstay 4 Reels (194, 69, 17, 10), Velocity 2 (174, 74), Voxa 2 (61, 26), brand/general 5 (61, 17, 14, 12, 11). Brand and general content is the bottom of the table. Concrete Rizstay billing is the only thing that earned a share.
4. **By hook formula:** 11 of 13 hooks match none of the 26 formulas in hooks.json. Only "3 tasks to automate" (#11) and "Hotel owners, what if..." (#14) classify. We have not been using the formulas at all.
5. **By hook score:** the one STRONG hook (81, "Your business runs 24/7") got 17 views, so the score did not predict views here. Hook scores catch bad hooks; they do not pick winners (the script says so itself).
6. **The 24 Oct hook scored 54.8**, under the >= 75 gate in skill_workflow.md. Either the on-screen hook was different or the gate was skipped. From now on posted.md logs the score.
7. **Zero follows from views** is not yet a profile problem: views are so low (10-74) that there is nothing to convert. Fix reach first, profile second.

- Best Reel this week: **24 Oct Rizstay "Your hotel's accountant. 11 PM. Again."** 69 views (2.7x median), the only share on the account. Why: a real, specific pain (GST bills at 11 PM) aimed at one person (the hotel owner), and a real product screen.
- Worst Reel this week: **19 Oct Rizstay "Guests judge your hotel before they say hello."** 10 views, 78% skip. Why: vague, nothing concrete in the first line, a list of moments rather than one problem.
- Worst hold: 18 Oct Velocity, 1.9s average watch, 88% skip, even though it had 74 views.

### ig-viral
Niche research came back empty: Instagram blocks page fetches here, YouTube is not on this session's allowlist, and vidIQ credits are 0. docs/swipe.md is our own 13 Reels in swipe format plus 4 new hooks written to the formulas. Not niche evidence.

### ig-plan decisions
- docs/clip_topics.md rewritten: Rizstay billing/KOT/CA first, 4 new topics (rizstay_kot_lost_slip, rizstay_ca_month_end, voxa_lunch_rush_missed_call, rizstay_small_hotel_big_system), brand intros, polls, generic AI lists and Velocity sales framing dropped.
- docs/rules.md: length changed to 15-20s main and 9-12s Trial; new hook guidance (#2 Negative Command and #20 Permission, concrete nouns, no questions or polls, no invented numbers). docs/skill_workflow.md and RUNBOOK.md changed to match (beats.py --target 18, 2 steps).
- docs/plan.md: next week's calendar.
- docs/engage.md: 10 accounts found via web search (5 reach, 3 peers, 2 buyers).

### ig-profile: 14 of the 36 points that could be checked from here (64 points not visible)
| item | pts | score | note |
|---|---|---|---|
| name field | 12 | 2 | "Sutrixa International": name only, no search words |
| handle | 6 | 4 | readable and sayable, but 20 characters |
| recent activity | 10 | 6 | posted in the last 7 days; no comments to reply to |
| grid legibility | 8 | 2 | top 9 include 3 brand intros, a poll and a captionless Reel |
| bio line 1, bio body, pinned three, link, highlights, photo, category/contact, stories | 64 | not scored | not visible: Instagram blocks the page here and a vidIQ profile lookup costs 5 credits (balance 0) |

Fixes, in order (the owner makes all of them in the app):
1. Name field (30 characters max), pick one: `Sutrixa | Hotel & GST software` / `Sutrixa | Hotel software India` / `Sutrixa | Hotel billing app`
2. Bio (130 characters): `Hotel or restaurant in India? Your GST bills, kitchen orders and registers, on one calm screen.` then a new line: `Runs in your browser. No installs.`
3. Link: one door, https://restaurant.rizstay.com
4. Pin three: the 24 Oct GST Reel (best so far), the GST carousel once posted (explains the offer), and a proof post when the owner has one.
5. Two live captions make claims that products.md marks as errors: 14 Oct Rizstay (DefAkOrjWRo, "Housekeeping auto-dispatched") and 16 Oct Voxa (Dejs2WJjJT7, "summarises every..."). Edit those captions or archive the posts. Also consider archiving the 3 brand intros so the top of the grid is product Reels.
6. Highlights: Rizstay, Voxa, How it works, About.

### ig-carousel
"Stop adding GST by hand." 9 slides, 1080x1350, Rizstay facts only, the real Purchase register screen with Export Excel boxed. Branch c/2026-10-25 (slides + caption.txt). Caption lint READY; ig-human 80 (slides) and 76 (caption).

### ig-repurpose
Skipped: the owner has not shared a long asset.

## Week ending 1 Nov 2026 (second weekly review)

### Run status
- **No new numbers this week.** The vidIQ connector needs to be reconnected, so vidiq_instagram_owner_insights could not run (it also blocks auto-posting since 31 Oct). Every figure below is the latest one already logged in docs/postmortems.md (reads of 28-30 Oct). Nothing is estimated or rounded up.
- Agent Reach was not installed (the install was blocked in this session). Research used WebSearch/WebFetch plus the laptop's live scans of 28-30 Oct.

### Numbers
- Followers: **28** at the last read (30 Oct, 13:51 UTC). Last week: **4**. Change: **+24** (+19 of them landed 27 Oct with the profile rewrite and the first Stories).
- Gap to target: **99,972** followers in 23 days, about **4,347 a day**. The account is gaining about 3-4 a day. The target will not be met by 24 Nov. The honest next marks: first Reel past 1,000 views, first 100 followers.
- 30 Oct (Bablu EP1, DfHupKPiiip) and 31 Oct (Missed-call math Part 2, hosted, sent to the owner to post by hand): no numbers yet.

| date | preset | product | hook (on screen) | len | views | x median | avg watch | watched | skip | shares | saves | read at |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 27 Oct | tips | Rizstay | Stop adding GST by hand at 11 PM. (80.2) | 46s | 92 | 1.36x | 13.6s | 29.5% | 68.6% | 1 | 0 | 72h |
| 29 Oct | eli5 | Rizstay | Stop losing GST input credit. Deadline: 30 November. (94.8) | 59.5s | 67 | 0.99x | 6.3s | 10.7% | 80.9% | 1 | 0 | 24h |
| 28 Oct | countdown | Voxa | Stop these 5 missed-call mistakes. (85.8) | 48.6s | 55 | 0.81x | 8.1s | 16.9% | 68.2% | 1 | 0 | 48h |
| 30 Oct | story | Rizstay | 16 ghante kaam. Paisa kahan gaya? | 47.6s | pending | | | | | | | |
| 31 Oct | countdown | Voxa | Stop losing ₹500 per missed call. (85.8) | 45.8s | not posted by the system | | | | | | | |
Median of the last 10 Reels: 67.5 views. 0 comments and 0 saves on every Reel so far.

### ig-audit (n = 3 measured Reels this week; low confidence)
- **Best: 27 Oct tips "Stop adding GST by hand at 11 PM."** 1.36x median and the best hold on the account (13.6s). Why: a plain hook with no jargon, real ₹ rules (₹7,500 room slab, 5% vs 18%), on real Rizstay screens.
- **Worst: 29 Oct eli5 "Stop losing GST input credit…"** 80.9% skip, 6.3s average. Why: 9 words of jargon at frame 0 plus a series label, a reused calm clip, Kokoro spelling "G S T", 59.5s long. The highest hookscore of the week did the worst.
- By preset: tips > eli5 ≈ countdown on views; tips > countdown > eli5 on hold. By product: Rizstay GST holds ~2x Voxa (PROVEN). By hook score: no link to results (94.8 worst, 80.2 best). By length: 46s held best, 59.5s worst. By clip: the only reused clip had the worst skip.
- Every Reel still loses 64-81% in 3 seconds. That is the bottleneck, not topic width.

### Decisions
- **Weights** (docs/presets.md): tips 4 · counter 3 · countdown 2 · eli5 2 · story 2 · stages 2 · pov 2 · proof 2 · quiz 1. Was eli5 4 · countdown 4 · tips 3 · stages 2 · pov 2 · quiz 1 · proof 1.
- **New preset: counter** (persistent background + a stat chip that climbs each beat). Seen 2 days running in the live scans (aiwith.om 29 Oct, simulateitnow 30 Oct: 7,686 shares). Built from screen beats.
- **Hooks** (docs/rules.md): two gates (hookscore ≥ 75 AND ≤ 6 words, no jargon at frame 0), one line at frame 0, ₹ or own-maths inside 3s, ask by 8s.
- **Clip topics** (docs/clip_topics.md): a 7-clip queue for 2-8 Nov matched to pillar days, dialogue clips first, folder must never be empty again.
- **Engage** (docs/engage.md): 10 accounts, each marked with how it was verified; 2 GST creators and 2 faceless peers swapped in.
- **Swipe** (docs/swipe.md): 11 niche Reels from the live scans. Likes only, no medians, so no outlier multiples.
- **Profile**: 55/100 carried from 30 Oct (not re-verified). Fixes in docs/profile_log.md.
- **Carousel**: "Your GST credit expires 30 Nov." 9 slides on branch c/2026-11-01 (caption READY, ig-human 90.4 slides / 82.7 caption).
- **ig-repurpose**: skipped, the owner hasn't shared a long asset.

## Week ending 8 Nov 2026 (third weekly review)

### Run status
- vidIQ owner insights pulled 8 Nov (~04:45 UTC). Every number below is Instagram's own, lifetime per Reel. Nothing is rounded up.
- Agent Reach: install refused by this session's safety check (2nd week). vidIQ credits 0 (refill 13 Nov). Laptop Instagram pane logged out since 31 Oct. Research = WebSearch/WebFetch of trend reports only.
- No daily Reel on 3 Nov or 6 Nov (no run those days).

### Numbers
- Followers: **32**. Last week's log: **28** (30 Oct read). Change: **+4** in 9 days.
- Gap to target: **99,968** followers in 16 days = **6,248 a day**. The account is gaining about 0.4 a day. **The 24 Nov target will not be met.** Nothing in this plan changes that, and the report says so plainly. Honest next marks: first Reel past 500 views, 50 followers.
- Account, 2-8 Nov: reach **381** accounts, **690** views. Reels last 30 days (vidIQ summary): 1,930 views.
- 0 comments and 0 saves on all 12 Reels in the window. 12 shares in total.

| date | preset | product | voice | hook (hookscore) | len | views | x median | avg watch | watched | skip | shares |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 Nov | story EP2 | Voxa | hi human | Stop losing ₹500 per missed call. (85.8) | 25s | 212 | **2.08x** | 5.9s | 23.7% | 62.6% | 2 |
| 30 Oct | story EP1 | Rizstay | hi human | 16 ghante kaam. Paisa kahan gaya? (50.6) | 47s | 186 | 1.82x | 6.4s | 13.6% | 71.0% | 2 |
| 5 Nov | story EP3 | HR4U | hi human | Stop counting staff in a register. (51.0) | 40s | 145 | 1.42x | 8.3s | 20.7% | 59.2% | 1 |
| 2 Nov | proof | Voxa | hi human | Your phone rang. Nobody picked up. (77.8) | 20s | 115 | 1.13x | 3.7s | 18.7% | 75.5% | 2 |
| 25 Oct | pre-preset | Voxa | en TTS | Stop letting your phone ring at 8 PM. (81.4) | 29s | 106 | 1.04x | 7.3s | 25.1% | 70.0% | 1 |
| 24 Oct | pre-preset | Rizstay | en TTS | Your hotel's accountant. 11 PM. Again. (54.8) | 32s | 102 | 1.00x | 4.7s | 14.8% | 69.3% | 1 |
| 27 Oct | tips | Rizstay | en TTS | Stop adding GST by hand at 11 PM. (80.2) | 46s | 99 | 0.97x | 12.6s | 27.5% | 71.1% | 1 |
| 29 Oct | eli5 | Rizstay | en TTS | Stop losing GST input credit… (94.8) | 59s | 83 | 0.81x | 5.5s | 9.4% | 78.3% | 1 |
| 7 Nov | tips | Rizstay | en TTS | Don't bill hotel dinners at 5%. (80.2) | 49s | 80 (~15h) | 0.78x | 3.1s | 6.4% | **87.9%** | 0 |
| 28 Oct | countdown | Voxa | en TTS | Stop these 5 missed-call mistakes. (85.8) | 48s | 66 | 0.65x | 7.5s | 15.6% | 71.7% | 1 |
| 26 Oct | pre-preset | Voxa | en TTS | Stop dropping your scissors… (81.4) | 32s | 64 | 0.63x | 8.3s | 25.8% | 70.2% | 0 |
| 4 Nov | counter | Rizstay | hi human | Stop charging 18% on ₹7,000 rooms. (83.2) | 26s | 189 | excluded (repeat, still live) | 6.3s | 24.3% | 58.6% | 1 |
Median of the 11 counted: **102** views. Reels on 31 Oct (hand-post) never appeared in insights: not posted.

### ig-audit (n = 11, low confidence; everything below is a bet with evidence, not proof)
- **By voice (clearest split):** Veo human-voice dialogue n=4: 164.5 views avg (1.61x), skip 67.1%, 7 shares. Narrator/Kokoro n=7: 85.7 (0.84x), skip 74.1%, 5 shares. All 4 human-voice Reels were Hindi, so voice and language are mixed up.
- **By preset:** story 1.77x (n=3) > proof 1.13x (n=1) > tips 0.88x (n=2) > eli5 0.81x (n=1) > countdown 0.65x (n=1). counter's only run was the excluded repeat (1.85x).
- **By product:** HR4U 1.42x (n=1), Voxa 1.10x (n=5), Rizstay 1.08x (n=5). No real product effect; the voice explains more.
- **By hook formula:** 9/11 are #2 Negative Command, in both top and bottom. Can't be judged until we test others.
- **By hook score:** under 75 (n=3) averaged 144 views; 75+ (n=8) 103. Third week the score runs backwards.
- **By clip/topic:** best openers are Bablu dialogue scenes; the worst is 7 Nov's landscape dinner clip cropped to portrait (87.9% skip, 3.1s avg watch). GST still holds well on 27 Oct (12.6s) but not on 7 Nov, so the opener matters more than the topic.
- **By length:** ≤30s n=3 averaged 144 views; 31-45s 104; >45s 103 with the highest skip (76%). The owner's 40-60s rule (4 Nov) is the opposite of what the views say; it's the owner's call.
- **By CTA:** 5 keyword Reels (CALLS, LEAK, PHONE, GST, RATE) = 0 comments. Send asks = all 12 shares.
- Best Reel: **1 Nov EP2 "Bablu ka phone"**: 2.08x, 2 shares. A character shouting the problem in the first second, a ₹ stake on screen, 25s.
- Worst Reel: **7 Nov "Don't bill hotel dinners at 5%"**: 0.78x at ~15h, 87.9% skip, 3.1s. Narrator over a cropped landscape clip, 49.8s, keyword ask. (Young read: re-check at 24-48h, but the skip is already the worst ever.)

### Decisions
- **Weights** (docs/presets.md): story 5 · tips 3 · counter 3 · proof 2 · stages 2 · pov 2 · countdown 1 · eli5 1 · quiz 1. Was tips 4 · counter 3 · countdown 2 · eli5 2 · story 2 · stages 2 · pov 2 · proof 2 · quiz 1.
- **New preset:** none. "No, no, no… yes!" is on watch (1 report only).
- **Hooks** (docs/rules.md, skill_workflow.md): character speaks the problem in 1s; hookscore floor 50 for spoken hooks (75 for narrator hooks); 2 non-#2 formulas this week; no landscape crops at frame 0; send ask by 8s; keyword asks paused.
- **Clip topics** (docs/clip_topics.md): 7 dialogue clips for 9-15 Nov, EN/HI alternating, all new facts, under 5 MB, native portrait. English Veo dialogue is the test of the week.
- **Engage** (docs/engage.md): 8 verified + 2 buyer slots left for the owner. @riyaazamlani removed: the handle belongs to a Turkish lyricist, not the restaurateur.
- **Swipe** (docs/swipe.md): own 11 Reels with true multiples; no niche capture possible this week.
- **Profile:** 55/100, unchanged (no fixes made yet). See docs/profile_log.md 8 Nov.
- **Carousel:** "Count your missed calls." 9 slides on branch c/2026-11-08 (caption READY, ig-human 83.9 slides / 79.5 caption, no pricing).
- **ig-repurpose:** skipped, no long asset shared.

## Week ending 15 Nov 2026 (fourth weekly review)

### Run status
- vidIQ owner insights pulled 15 Nov (~05:00 UTC), free. All numbers are Instagram's own, lifetime per Reel; nothing rounded up.
- Agent Reach: install refused by this session's safety check (3rd week). Research = WebSearch/WebFetch (Lightreel, NewEngen 13 Nov, postdom 9-15 Nov, NapoleonCat, mean.ceo) + vidIQ outlier search (credits 170 at start; 2 searches + 5 profile checks = 35 credits used).
- **Only 1 Reel posted in the 7 days 9-15 Nov** (EP5, 12 Nov). No Reel on 9, 10, 11, 13, 14 Nov (Gemini daily limit, Chrome profile mix-ups, Drive/vidIQ 502 on 13 Nov, one EP6 clip never downloaded). EP4 went out late on 8 Nov 23:55 IST.
- The 1 Nov and 8 Nov carousels (branches c/2026-11-01, c/2026-11-08) were never posted: no carousel appears in the media list.

### Numbers
- Followers: **32**. Last week: **32**. Change: **0** in 7 days.
- Gap to the 100,000 target: **99,968** in 9 days = **11,108 a day**. The account has gained 4 followers in 16 days. **The 24 Nov target will not be met**, and nothing in this plan changes that. Honest next marks: 50 followers, and a second Reel past 1,000 views.
- Account 8-15 Nov: reach **1,456** accounts, **1,688** views (last week 2-8 Nov: 381 reach, 690 views). Last 30 days: 2,279 reach, 3,531 views. follows_and_unfollows returned no data.
- 0 comments on every Reel. EP5 has the account's first 2 saves since 25 Oct.

| date | preset | product | voice | hook (hookscore) | len | views | reach | x median | avg watch | watched | skip | shares | saves |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 12 Nov | story EP5 | Rizstay | hi human | Kal 5 kilo paneer aaya. Aaj khatam? (50.6) | 40s | **1,353** | 1,240 | **10.0x** | 14.0s | 35.1% | **30.0%** | 1 | 2 |
| 8 Nov | story EP4 | Velocity | **en human** | Our food is better. So why are we empty? (34.2) | 40s | 252 | 213 | 1.87x | 9.4s | 23.5% | 45.3% | 1 | 1 |
| 1 Nov | story EP2 | Voxa | hi human | Stop losing ₹500 per missed call. (85.8) | 25s | 214 | 159 | 1.59x | 5.9s | 23.6% | 62.4% | 2 | 0 |
| 30 Oct | story EP1 | Rizstay | hi human | 16 ghante kaam. Paisa kahan gaya? (50.6) | 47s | 186 | - | 1.38x | 6.4s | 13.6% | 71.0% | 2 | 0 |
| 5 Nov | story EP3 | HR4U | hi human | Stop counting staff in a register. (51.0) | 40s | 173 | 136 | 1.28x | 7.7s | 19.3% | 61.8% | 2 | 0 |
| 7 Nov | tips | Rizstay | en TTS | Don't bill hotel dinners at 5%. (80.2) | 49s | 135 | 100 | 1.00x | 4.7s | 9.5% | 85.5% | **9** | 0 |
| 2 Nov | proof | Voxa | hi human | Your phone rang. Nobody picked up. (77.8) | 20s | 119 | 86 | 0.88x | 3.7s | 18.7% | 75.5% | 2 | 0 |
| 27 Oct | tips | Rizstay | en TTS | Stop adding GST by hand at 11 PM. (80.2) | 46s | 99 | - | 0.73x | 12.6s | 27.5% | 71.1% | 1 | 0 |
| 29 Oct | eli5 | Rizstay | en TTS | Stop losing GST input credit… (94.8) | 59s | 84 | - | 0.62x | 5.5s | 9.3% | 78.7% | 1 | 0 |
| 28 Oct | countdown | Voxa | en TTS | Stop these 5 missed-call mistakes. (85.8) | 48s | 66 | - | 0.49x | 7.5s | 15.6% | 71.7% | 1 | 0 |
| 26 Oct | pre-preset | Voxa | en TTS | Stop dropping your scissors… (81.4) | 32s | 64 | - | 0.47x | 8.3s | 25.8% | 70.2% | 0 | 0 |
| 4 Nov | counter | Rizstay | hi human | Stop charging 18% on ₹7,000 rooms. (83.2) | 26s | 195 | 159 | excluded (repeat, still live) | 6.3s | 24.2% | 58.9% | 1 | 0 |
Median of the 11 counted: **135** views (last week 102; older Reels kept gaining views, e.g. 7 Nov 80 → 135).

### ig-audit (n = 11, low confidence; EP5 is one Reel and drags every average)
- **Winner: EP5 "paneer kahaan gaya?"** 10.0x, skip 30% (account ~68%), 14.0s average watch, 1,240 reach. Why: Bablu shouts a question about a physical thing with a number inside 1s ("5 kilo paneer... khatam?"), a new character (Ramu) confesses, a real Rizstay Stock screen under Priya's line, a voice on every beat, native portrait Veo. It is the first Reel Instagram pushed well past followers.
- **Loser: 7 Nov tips "Don't bill hotel dinners at 5%"**: skip 85.5%, 4.7s watch, the Kokoro narrator over a cropped landscape clip. But it has **9 shares on 100 reach**, the best sends per reach on the account, from "SEND IT TO YOUR CA". The topic travels; the opener killed it.
- **By preset:** story n=5 mean 3.23x (median 1.59x) > tips 0.87x (n=2) ≈ proof 0.88x > eli5 0.62x > countdown 0.49x. Since 8 Nov only story Reels have been posted, so counter, stepper, stages, pov and quiz are untested.
- **By voice/language:** human voice n=6 counted (5 story + 1 proof), mean 2.83x; Kokoro n=5, mean 0.66x. English human voice n=1 (EP4) = 1.87x, so it isn't only Hindi.
- **By product:** no clean effect. Rizstay has the 10x and three of the bottom five.
- **By hook formula:** the 2 best are character questions about a concrete thing (EP5, EP4: mean 5.9x). The 7 #2 Negative Command Reels averaged 0.88x.
- **By hook score:** 4th week backwards. The two best scored 50.6 and 34.2; hooks ≥ 75 (n=7) averaged 0.83x.
- **By clip topic:** physical loss in a kitchen (paneer) and an empty restaurant beat abstract topics (GST rules, missed-call maths).
- **By length:** all 5 story Reels ran 25-47s; length doesn't separate them. 40s held 35% on EP5.
- **Views without follows:** EP5 reached 1,240 accounts and net followers stayed at 32. Per ig-audit, that's a profile problem: no pinned posts, a bio for "Enterprise AI | Agency", no highlights, no stories, and the promised "EP 6 kal" never came. Fixes go to the owner (docs/profile_log.md 15 Nov).

### Decisions
- **Weights** (docs/presets.md): story 6 · casestudy 4 (new) · tips 3 · counter 3 · stepper 2 · stages 2 · pov 2 · proof 1 · countdown 1 · eli5 1 · quiz 1. Was story 5 · tips 3 · counter 3 · proof 2 · stages 2 · pov 2 · stepper 2 · countdown 1 · eli5 1 · quiz 1.
- **New preset: casestudy** (animated business lesson: a character's money dilemma → failed fix → Kaka names the principle → viewer's maths → real product screen → payoff). From 6 niche accounts in the vidIQ outlier search, 12.6x to 632x, two of them under 1,500 followers. Swipe file: docs/swipe.md + docs/swipe_niche_2026-11-15.tsv.
- **Hooks** (docs/rules.md 15 Nov, skill_workflow.md): character questions about a concrete thing are allowed; hookscore is logged, not gated, for spoken character hooks; follow reason on screen by ~10s; only promise the next episode when its clips exist.
- **Clip topics** (docs/clip_topics.md): 16-22 Nov queue (EP6 finish, 2 casestudy, pov, counter, stages, EP7), full clip set + 1 spare before announcing an episode. New topic ids in docs/topics.md. Week plan in docs/plan.md.
- **Engage** (docs/engage.md): 10 accounts, all verified today (5 by vidIQ profile fetch, 5 by outlier-search Reels dated 23 Oct-12 Nov), including 2 real buyers (@labibs_india restaurant brand, @desitouch.vlogs food founder). 10 comment drafts, ig-human 74.3.
- **Profile:** 53/100 (13 Nov: 54). Fixes: pin EP5/EP4/EP3, bio options A/B, 3 Stories then highlights, delete the 4 Nov repeat. See docs/profile_log.md.
- **Carousel:** "Where did your paneer go?" 10 slides on branch c/2026-11-15 (caption READY; ig-human 66.8 caption / 71.5 slides; no product pricing, ₹ figures are a labelled ingredient-cost example).
- **ig-repurpose:** skipped, no long asset shared.

## Week ending 22 Nov 2026 (fifth weekly review)

### Run status
- vidIQ owner insights pulled 22 Nov (~04:50 UTC), free. All numbers are Instagram's own, lifetime per Reel; nothing rounded up. EP12 (21 Nov) is under a day old and EP11 two days old, so both will still grow.
- Agent Reach installed for the first time (v1.6.1) and `agent-reach doctor` ran, but no channel was usable: YouTube blocked by the session's network proxy (403), Reddit's helper download 403, Instagram needs a login. Research = vidIQ outlier search (2 searches, 10 credits; 100 left, renew 13 Dec) + NewEngen (20 Nov) and SocialPilot (17 Nov).
- **7 Reels in 7 days** (EP6-EP12, 15-21 Nov), all story preset. No missed day. The 22 Nov HINDI EP13 is at risk: 3 of its clips are stuck in Gemini chats because Drive for desktop on the laptop stopped syncing on 20 Nov 17:02 UTC.
- **No carousel has ever been posted**: the 1, 8 and 15 Nov carousels (branches c/2026-11-01, -08, -15) are not in the media list.

### Numbers
- Followers: **37**. Last week: **32**. Change: **+5** in 7 days.
- Gap to the 100,000 target: **99,963** with 2 days left (24 Nov) = **~49,980 a day**. **The target will not be met.** The account has gained 33 followers since 25 Oct. Honest next marks: 50 followers, and one Reel past 5,000 views.
- Account 15-22 Nov: reach **3,402** accounts (last week 1,456), views **3,988** (last week 1,688), profile visits **38**, content interactions **79**. follows_and_unfollows returned no data. Follows per reach ≈ 0.15%; profile visits per reach ≈ 1.1%.
- 0 comments on every Reel again (keyword asks on EP7, EP9, EP11 included).

| date | preset | product | lang | hook (on screen) | len | views | reach | x median | avg watch | watched | skip | shares | saves | likes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 16 Nov | story EP7 | Rizstay QR orders | hi | 10 table, 1 waiter... order mein 10 minute! | 40s | **1,561** | 1,436 | **8.2x** | 13.9s | 34.7% | 35.6% | **4** | 2 | 29 |
| 21 Nov | story EP12 | HR4U attendance | en | Pay him for 16 hours? | 40s | **1,513** | 1,388 | **8.0x** | 12.9s | 32.4% | 35.8% | 0 | 2 | 19 |
| 12 Nov | story EP5 | Rizstay stock | hi | Kal 5 kilo paneer aaya. Aaj khatam? | 40s | 1,362 | 1,248 | 7.2x | 14.0s | 35.0% | 30.2% | 1 | 2 | 23 |
| 8 Nov | story EP4 | Velocity | en | Our food is better. So why are we empty? | 40s | 257 | 216 | 1.35x | 9.4s | 23.5% | 45.4% | 1 | 1 | 5 |
| 17 Nov | story EP8 | Voxa | en | 30 enquiry calls. Only 2 bookings? | 42s | 192 | 154 | 1.01x | 5.3s | 12.6% | 70.5% | 2 | 0 | 2 |
| 15 Nov | story EP6 | HR4U onboarding | en | New chef Monday. His papers? Somewhere in here. | 40s | 190 | 164 | 1.00x | 7.1s | 17.7% | 63.6% | 1 | 0 | 3 |
| 19 Nov | story EP10 | Velocity | en | They booked the hotel across the street. | 40s | 186 | 156 | 0.98x | 8.7s | 21.9% | 48.4% | 1 | 0 | 1 |
| 5 Nov | story EP3 | HR4U | hi | Stop counting staff in a register. | 40s | 175 | 137 | 0.92x | 7.8s | 19.4% | 61.0% | 2 | 0 | 1 |
| 20 Nov | story EP11 | Rizstay front desk | hi | Mantri ji ka room free tha... | 40s | 160 | 142 | 0.84x | 9.8s | 24.5% | 34.9% | 0 | 0 | 0 |
| 18 Nov | story EP9 | HR4U training | hi | 3rd cook gone this year. | 40s | 155 | 134 | 0.82x | 6.3s | 15.9% | 54.3% | 1 | 0 | 3 |
| 7 Nov | tips | Rizstay GST | en TTS | Don't bill hotel dinners at 5%. | 49s | 137 | 101 | 0.72x | 4.6s | 9.4% | 85.7% | **9** | 0 | 1 |
| 4 Nov | counter | Rizstay GST | hi | Stop charging 18% on ₹7,000 rooms. | 26s | 201 | 162 | excluded (repeat) | 6.3s | 24.0% | 58.7% | 1 | 0 | 1 |
Median of the 11 counted (5-21 Nov): **190** views (last week 135 over 26 Oct-12 Nov).

### ig-audit (n = 11, low confidence; the account's distribution is bimodal: ~1,400+ or ~150-250)
- **Best Reel: EP7 "10 table, 1 waiter"** (8.2x, 4 shares, 29 likes, skip 35.6%). Why: Bablu says a visible floor problem with three numbers in the first second (tables, waiter, minutes); Ramu idle at the pass; Kaka's one-line principle; a real Rizstay menu/QR screen. **EP12 "Pay him for 16 hours?"** is level with it after one day, in English, so it isn't the Hindi.
- **Worst Reel (counted): 7 Nov tips "Don't bill hotel dinners at 5%"** (0.72x, skip 85.7%, narrator over a cropped landscape clip), though it still has the best sends per reach (9 on 101). **Worst this week: EP9 "3rd cook gone this year"** (0.82x, skip 54.3%): a resignation letter and a 'why' question, no visible loss in the frame. EP11 (0.84x, 0 likes) is the other: a bill at a desk.
- **By preset:** story n=10 in the window, mean 2.97x this week but median 1.0x; it holds all 3 breakouts. tips n=1 in the window, 0.72x. Nothing else was posted, so casestudy, counter, stepper, stages, pov, letterbox and quiz are still untested. The plan for 2 casestudy + pov + counter + stages last week became 7 story Reels.
- **By product:** Rizstay 2 breakouts (QR orders, stock) and 1 stall (front desk); HR4U 1 breakout (attendance) and 2 stalls (onboarding, training); Velocity and Voxa 0 of 3. Leaning: restaurant-floor and wage problems, not the product itself.
- **By hook formula:** EP7 classifies as #11; EP12 and EP5 are unclassified concrete-number questions. The 3 breakouts share a shape, not a formula id: physical loss + number + kitchen/floor scene in the first second.
- **By hook score:** 5th week with no signal. Breakouts 48-51; EP8 scored 62.6 and stalled.
- **By clip topic:** kitchen/floor/wages (paneer, tables, 16 hours) 3 of 3 broke out; desk/phone/paper (onboarding papers, enquiry calls, website, free room, training) 0 of 5.
- **By length:** every story Reel is 40-42s (owner rule), so length can't explain the split.
- **Language:** breakouts HI, EN, HI; stalls EN ×3, HI ×2. No effect.
- **Views without follows:** EP7 + EP12 reached ~2,800 accounts and the account gained 5. Profile visits were 38 for 3,402 reach. Both a reason-to-visit problem (end card) and a profile problem (0 pinned, "Enterprise AI | Agency" bio, no story ring).

### Decisions
- **Weights** (docs/presets.md): story 6 · casestudy 5 · counter 3 · tips 2 · stepper 2 · stages 2 · pov 2 · letterbox 2 · proof 1 · countdown 1 · eli5 1 · quiz 1. Was story 6 · casestudy 4 · tips 3 · counter 3 · stepper 2 · stages 2 · pov 2 · letterbox 2 · proof 1 · countdown 1 · eli5 1 · quiz 1. **2 casestudy Reels are booked for 23-29 Nov** so something other than story finally gets a count.
- **New preset:** none. "No, No, No... Yes!" is on NewEngen for a 3rd week but still has only one source.
- **Hooks** (docs/rules.md 22 Nov): kitchen/floor scene, physical loss + number in the first second, Ramu in beat 1-2; desk/phone/paper openers paused until one beats 2x; hookscore logged, not gated.
- **Clip topics** (docs/clip_topics.md): 23 EN casestudy rizstay_menu_pricing · 24 HI story hr4u_workload (new topic) · 25 EN casestudy voxa_missed_calls · 26 HI story rizstay_stock · 27 EN velocity_social_posting · 28 HI casestudy gst_hotel. All lines pre-checked against used_content.json (max 0.57).
- **Engage** (docs/engage.md): 10 accounts verified today (8 by outlier Reels dated 11-19 Nov, 2 buyers by profile fetch), including the first hotel-owner audience (@dr.shantanu_hotel_consultant). @digitalstaff.in left out (sells an AI sales agent).
- **Swipe** (docs/swipe.md, docs/swipe_niche_2026-11-22.tsv): 15 niche Reels, 15 accounts, + our 5.
- **Profile:** 57/100 (15 Nov: 53). Fixes: pin EP7/EP12/EP5, bio option C, 3 Stories then highlights, delete the 4 Nov repeat. See docs/profile_log.md 22 Nov.
- **Carousel:** "How long does one order take?" 10 slides on branch c/2026-11-22 (caption READY; ig-human 75.9 caption / 65.7 slides; no product pricing; the 8 min × 30 tables figure is a labelled example).
- **ig-repurpose:** skipped, no long asset shared.
- **Next review falls after 24 Nov**, so per the scheduled task it sends a final summary and stops.
