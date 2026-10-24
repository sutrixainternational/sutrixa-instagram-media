# Standing content rules (@sutrixainternational)
- Every Reel opens with REAL moving Gemini video (Veo, 9:16) with its audio. Never stand in a screenshot, still frame or placeholder, not even in a preview sent to the owner.
- If the Gemini clip can't be pulled into the workspace, stop and say so; do not render or show a version without it.
- Reels must explain, not list: problem (Gemini clip) -> what the product does -> numbered steps on the real product screen with the exact UI element highlighted -> one-line outcome -> logo end card. 25-35s.
- Sutrixa logo on every frame. Facts only from /root/.claude/instagram/products.md.
- Renderer: scratchpad/render_reel2.py (video beats, step badges, highlight boxes, music bed).
- EVERY Reel has a voice (owner rule, 24 Oct). Use the free local Kokoro TTS in scratchpad/tts (render_reel2.py: "say" per beat, "voice" in spec, refuses to render with no voice). Never vidIQ voiceover (owner will not pay). No voice = do not post.
- Storage: videos live in Google Drive only (owner rule). Never use the laptop's folders. Drive "Sutrixa Instagram" and "2 - Ready to post" are public-link (checked 24 Oct).
- Pipeline that works: Drive -> workspace via Google_Drive download_file_content (result saved to tool-results file; decode with scratchpad/drive_pull.py). Workspace -> Drive via Chrome file_upload into Drive's own upload input (patch HTMLInputElement.click to capture it, then New > File upload). Drive public link -> vidiq_video_upload -> vidiq_instagram_publish_reel.
- Gemini -> Drive is the open gap: cross-tab messaging is cut by the browser, and passing clip data through tool output is blocked. Don't retry either.
