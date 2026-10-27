# Standing content rules (@sutrixainternational)
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
