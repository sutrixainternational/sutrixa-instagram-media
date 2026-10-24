# Daily Reel runbook: @sutrixainternational

Runs in the cloud with the owner's laptop off. Read `docs/rules.md` and `docs/products.md` first. They are binding.

## Accounts and IDs
- Instagram via vidIQ: platformAccountId `39219443167670371`
- Drive (avideb.sutrixa@gmail.com), "Sutrixa Instagram": `1jv8ZtkafPJkN0hC1egm9WQ7zeNAA7b5o`
  - "1 - Gemini clips": `19vBnQ4z_n14gAwyFYX7WDtbNUjIEylul` (the weekly batch lands here, named `YYYY-MM-DD_topic.mp4`)
  - "2 - Ready to post": `1BlgQeRI9Nkjs37z3su-mW0Q4D7pXs0jr`
  - "3 - Posted": `10Fg1ou0kQzzg7GPcHJYKKDPhXSbdBBFE`

## Steps
1. `bash setup.sh`
2. Pick today's clip from "1 - Gemini clips". Find it with Google_Drive search_files (parentId), then download_file_content. The result is saved to a tool-results file, so run `python3 tools/drive_pull.py <file> work/clip.mp4`. **No clip means no Reel.** Message the owner.
3. Script it with the ig-reel skill: score the hook, one product, one problem. Then 3 steps on the real screen (`shots/`) with `hl` boxes on the exact UI element, a one-line outcome, and an end card. Every beat gets a `say` line. Run the ig-human pass on all text.
4. Write `work/spec.json` (see `docs/example_spec.json`). Render with `python3 tools/render_reel2.py work/spec.json`. It refuses to render with no voice.
5. Check it: extract frames with ffmpeg, look at them, and confirm the logo, the voice and the facts.
6. Caption: ig-caption skill, `python3 tools/caption.py cap.txt --keywords "..."`. It must be READY. Max 5 hashtags, one ask.
7. Host: `git checkout --orphan v/DATE`, then `git rm -rf --cached .`, add only `reel.mp4`, commit, and push the branch.
   The URL is `https://raw.githubusercontent.com/sutrixainternational/sutrixa-instagram-media/v/DATE/reel.mp4`.
8. Run vidiq_video_upload(url). Then vidiq_instagram_publish_reel with isAiGenerated true (Gemini footage). Poll the containerId until PUBLISHED.
9. Leave the `v/DATE` branch in place. The git proxy refuses branch deletes. Log the post in `docs/posted.md` on main: date, permalink, hook and product. Push main.
10. Comments: ig-reply skill on the latest posts. **Drafts only.** Send them to the owner for batch approval.
