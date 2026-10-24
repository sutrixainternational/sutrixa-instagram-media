# Standing content rules (@sutrixainternational)
- Every Reel opens with REAL moving Gemini video (Veo, 9:16) with its audio. Never stand in a screenshot, still frame or placeholder, not even in a preview sent to the owner.
- If no new Gemini clip is in Drive, never skip the day (owner rule, 24 Oct): reuse the least-recently-used real Gemini clip from "3 - Posted" (not used in the last 3 days) with a new angle and segment. Never use stills.
- Reels must explain, not list: problem (Gemini clip) -> what the product does -> numbered steps on the real product screen with the exact UI element highlighted -> one-line outcome -> logo end card. 25-35s.
- Sutrixa logo on every frame. Facts only from /root/.claude/instagram/products.md.
- Renderer: scratchpad/render_reel2.py (video beats, step badges, highlight boxes, music bed).
- EVERY Reel has a voice (owner rule, 24 Oct). Use the free local Kokoro TTS in scratchpad/tts (render_reel2.py: "say" per beat, "voice" in spec, refuses to render with no voice). Never vidIQ voiceover (owner will not pay). No voice = do not post.
- Storage: videos live in Google Drive only (owner rule). Never use the laptop's folders. Drive "Sutrixa Instagram" and "2 - Ready to post" are public-link (checked 24 Oct).
- Pipeline that works: Drive -> workspace via Google_Drive download_file_content (result saved to tool-results file; decode with scratchpad/drive_pull.py). Workspace -> Drive via Chrome file_upload into Drive's own upload input (patch HTMLInputElement.click to capture it, then New > File upload). Drive public link -> vidiq_video_upload -> vidiq_instagram_publish_reel.
- Gemini -> Drive is the open gap: cross-tab messaging is cut by the browser, and passing clip data through tool output is blocked. Don't retry either.

## Reach rules (24 Oct, "optimise every way possible")
- Length: aim for 25-35s total. Keep the voice speed at 1.12-1.18 and cut beats rather than rushing. Watch-through beats length.
- Frame 1 = hook: the hook text and the Gemini clip are both on screen from frame 0 (Instagram uses the first frame as the grid cover). No fade-in on beat 1.
- The hook must work on mute: on-screen text states the problem in 8 words or fewer.
- One product per Reel. Rotate Rizstay, Voxa, HR4U and Velocity (Velocity only as stated in products.md). Rizstay gets 2 of every 5 posts: it has the best real screens.
- Caption: put the search phrase in a normal sentence in the first two lines. Use one ask, rotating between "save this", "send this to a hotel owner" and "comment DEMO". Use DEMO only if the owner has agreed to handle DMs.
- Daily Trial Reel: after the main Reel is posted, render a second cut from the same clip, with a different hook formula from ig-reel and a different product step order. Publish it as a Trial Reel with trialParams {graduationStrategy: "SS_PERFORMANCE"}. Instagram shows it to non-followers first, and auto-shares it to followers if it performs. Log both posts.
