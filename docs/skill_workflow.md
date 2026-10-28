# How every ig-* skill is used (binding)

The skills live in `igpack/skills/<name>/SKILL.md`, and the synced account skills are `anthropic-skills:ig-*`. Read a skill's SKILL.md before using it. Scripts run from `igpack/skills/<name>/`. First install the voice: `mkdir -p ~/.claude/instagram && cp docs/voice.md ~/.claude/instagram/voice.md`

## Daily: the Reel run (cloud, 6:47 PM IST)
| step | skill | hard gate |
|---|---|---|
| 0 | **Post-mortem (ig-audit, single Reel)**: analyse the previous Reel(s) | Pull vidiq_instagram_owner_insights and write an entry in docs/postmortems.md: numbers vs median and benchmarks, what went wrong, changes for TODAY, reach actions. Also update yesterday's entry with its 24h numbers. Today's Reel must apply every change listed. Then update docs/lessons.md: add TRY lessons, promote a lesson seen in 2+ post-mortems to PROVEN and copy it into docs/rules.md, and mark contradicted ones DROPPED. Read docs/lessons.md before scripting. |
| 1 | **ig-reel**: write 5+ hooks from hooks.json formulas for the clip's problem | `python3 igpack/skills/ig-reel/hookscore.py hooks.txt`. Use the top hook. It must score **≥ 75 (STRONG)**, with no dealbreaker. Otherwise write more hooks. |
| 2 | **ig-reel**: script + on-screen text | `python3 igpack/skills/ig-reel/beats.py script.txt --target <preset length> --wpm 170`. Hook ≤ 2s, no beat > 4s, total within the preset range in docs/presets.md (27 Oct: informative Reels 30-50s; proof 15-25s at most 1 in 5 posts; see docs/algorithm.md). Loop the last line back to the hook where possible. |
| 2b | **Informative check** | List the facts the Reel teaches. Need ≥ 3 concrete, checkable facts or steps (docs/algorithm.md), all in docs/products.md or general verifiable knowledge. Fewer means add beats. |
| 3 | **ig-human** on the script, the on-screen text and the caption | `python3 igpack/skills/ig-human/detect.py <file>` must come back clean. Fix with humanize.py, then re-check. |
| 4 | **ig-caption** | `python3 igpack/skills/ig-caption/caption.py cap.txt --keywords "<2-3 search phrases>"` gives **READY**. |
| 5 | Trial Reel cut: **ig-reel** again with a *different* formula (also ≥ 75) | same gates |
| 6 | **ig-story**: today's 5-frame Story sequence (open, 2 content, ask at frame 4, close) | Write stories/<date>_daily.json and render with `python3 tools/story.py stories/<date>_daily.json out/` (1080x1920, logo, safe zone). Push the PNGs to branch s/<date> and give the owner the raw links plus which sticker to add on each frame in the app (poll/question/quiz on frame 4, link sticker to sutrixa.com when useful). The ask must work without a sticker too ("reply to this story"): replies arrive as DMs. Stories can't be published through the Instagram API from here. |
| 7 | **ig-reply**: sort the new comments on the last 3 posts and draft replies | Drafts go to the owner. Never post. |
| 8 | **ig-dm**: if a comment or reply shows buying intent (keyword or lead) | Draft the first DM and two follow-ups for the owner to send. |
| 9 | **ig-comment**: 10 comments for today's engagement round, on the accounts in docs/engage.md | Drafts go to the owner to post from the app. Never automated. |

## Weekly: the growth review (cloud, Sunday 10:13 AM IST)
| skill | output |
|---|---|
| **ig-audit** | Rank the last 7-14 Reels by multiple over the median, and by shares + saves per view. Winners and losers go in docs/growth.md. |
| **ig-viral** | Find what's working in the niche (Indian hotel, restaurant and small-business owners). Use WebSearch/WebFetch for public Reels and accounts. vidIQ outlier search costs credits, so use it only if credits > 0. Capture to a TSV, then run `python3 igpack/skills/ig-viral/swipe.py captured.tsv --out docs/swipe.md`. Feed the top formulas into docs/clip_topics.md and the hooks. |
| **ig-plan** | Next week's calendar. Update docs/clip_topics.md. Refresh docs/engage.md with 10 accounts: 5 reach, 3 peers, 2 buyers. |
| **ig-profile** | Re-score with igpack/skills/ig-profile/rubric.json. Send the owner the score and copy-ready fixes, since the owner edits the profile. |
| **ig-carousel** | One carousel a week from that week's best Reel topic. Render 1080x1350 slides, push them to branch c/DATE, and send the owner the links to post. |
| **ig-repurpose** | If the owner shared a long asset (a video, blog or call), turn it into the next week's Reel ideas and clip topics. |

## Never
- Never invent proof, numbers or customer results (voice.md, "Proof I can use").
- Never automate comments, DMs or follows on other accounts.
- Never feature InfraRobo.
