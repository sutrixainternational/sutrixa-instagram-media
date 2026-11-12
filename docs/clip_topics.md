# Gemini clip topics. Rewritten by the weekly review, 8 Nov 2026
Evidence (vidIQ owner insights, 8 Nov, lifetime, 11 counted Reels, median 102 views): **the 4 Reels that opened on a Veo character speaking averaged 1.61x median; the 7 narrator Reels 0.84x.** The best Reel of the month is EP2 "Bablu ka phone" (212 views, 2.08x, 2 shares). The worst opener is 7 Nov: a landscape dinner clip cropped to portrait under a narrator (87.9% skip). So the queue below is **dialogue clips only, native portrait, one speaker per clip**, and it alternates English and Hindi (owner rule 6 Nov).

Every clip: vertical 9:16 (native, never a landscape crop), 8s, Indian setting, natural sound, no text, no logos. The problem moves in the first second and the line starts inside ~1s. Prompt shape: subject + action + camera move + style + light + specs, 50-100 words. **Export under 5 MB** (720x1280 is fine): the Drive connector drops bigger files and the cloud can't fetch Drive directly (7 Nov). Keep at least 2 unused clips in "1 - Gemini clips".

Standing lessons (still binding):
- **Gemini UI changed (11 Nov):** the "+" / "Upload & tools" menu now opens EMPTY on a freshly loaded page. Video lives at sidebar "More" -> "Videos" (URL gemini.google.com/u/0/videos): a "Describe your video" box with an aspect button under it (pick "Portrait (9:16)"). After sending, the prompt shows as a user-query bubble and the send button turns into "Stop response". Work in a NEW tab (it is the active, painted tab); an old background tab reports window 0x0 and freezes.
- ONE speaker per clip: Gemini refused every two-speaker prompt (5 Nov).
- No studio names in prompts ("Pixar-like" fails). Write "Colourful 3D animated cartoon style with soft, rounded, stylised characters" (4 Nov).
- Write the spoken line into the prompt so Veo's own voice says it: Hindi: `says in Hindi, with a natural warm voice: "..."`. English: `says in English, with a natural Indian accent, in a warm human voice: "..."`. Lines under ~7s.
- Name files `YYYY-MM-DD_dlg_<en|hi>_<topic>.mp4`. Chrome saves Gemini downloads to the laptop's Downloads folder.
- If Google shows an "unusual traffic" check, never solve it; stop and retry later.
- **No repeats** (owner rule 4 Nov): no clip, line, hook, story angle or fact used in the last 21 days. Facts below are picked from products.md lines not yet taught; `tools/no_repeat.py check` decides on the day.

## Characters (keep identical every time)
BABLU: chubby 35-year-old Indian hotel owner, round face, thin moustache, messy black hair, light blue half-sleeve shirt with a pen in the pocket, brown trousers. KAKA: thin 70-year-old tea seller, thick white handlebar moustache, NO beard, NO glasses, grey woollen cap, maroon checked muffler, brown shawl over a cream sweater. PRIYA: 24-year-old receptionist, neat bun, maroon blazer. All three can speak English or Hindi.

## Next week (9-15 Nov), in order. Language alternates (7 Nov EN, so 8 Nov HI, 9 Nov EN...)
| # | file name | day · lang · preset | scene + spoken line (frame 0 = problem moving) | new facts (docs/products.md) |
|---|---|---|---|---|
| 1 | 2026-11-09_dlg_en_ep4_priya_clockout | Mon · EN · story (Bablu ka Hotel EP4) | Priya at the front desk at night, phone in hand, worried, handheld push-in, cartoon style. Says in English: "Sir, I forgot to clock out yesterday. Does it say I worked twenty hours?" Second clip `_kaka_en_idle`: Kaka alone at his stall, in English: "Beta, it closes the idle session itself. She just sends a correction." | HR4U: idle sessions auto-close; correction requests; attendance export CSV/JSON/PDF |
| 2 | 2026-11-10_dlg_hi_kitchen_waste | Tue · HI · counter | Hotel kitchen, a cook tips spoiled paneer into a bin, Bablu walks in, static close-up then tilt up to his face. Says in Hindi: "Yeh paneer kisne phenka? Kitne ka tha? Kisi ko pata nahi!" | Rizstay: waste log records the loss + who logged it; purchases restock; roles: one sign-in, a dashboard for Kitchen and Owner |
| 3 | 2026-11-11_dlg_en_clinic_four_lines | Wed · EN · stages | Realistic small clinic, receptionist with a queue in front, two phones ringing, handheld. Says in English, flustered: "Hold please... hold please... four lines are ringing and I'm alone." | Voxa: setup = describe the business → train on FAQs/catalogue → connect number/calendar → live; "from idea to live agent in an afternoon"; qualifies leads; CRM integrations (HubSpot, Zoho, Salesforce) |
| 4 | 2026-11-12_dlg_hi_ep5_qr_menu | Thu · HI · story (EP5) | Bablu's restaurant, a guest waving for the menu, the waiter running, cartoon style. Bablu says in Hindi: "Menu do, order lo, phir kitchen bhaago... ek waiter, das table!" Clip 2 `_kaka_qr`: Kaka alone: "Table pe QR laga. Guest khud dekhe, khud order kare." | Rizstay: table QR menu → browse and order; private stay code shows the guest their stay and amenities (check no_repeat: 7 Nov used the stay code); 3-step setup, no installs |
| 5 | 2026-11-13_dlg_en_saree_shop_posting | Fri · EN · pov | Realistic saree shop owner (woman, 40s) behind the counter, customers waiting, phone open on Instagram, sighs. Says in English: "I opened this shop to sell sarees, not to post on Instagram every day." Handheld push-in | Velocity: posts written every week; owner approves on the phone, nothing goes out without approval; one-page website with a WhatsApp button; replies to comments and forwards messages |
| 6 | 2026-11-14_dlg_hi_moment_salon | Sat · HI · proof (moment, 15-25s) | Realistic salon owner mid-haircut, phone buzzing in her apron. Says in Hindi: "Ek haath mein kainchi, ek mein phone... kaise sambhalun?" Slow push-in | Voxa: books appointments; resolves requests; voice that callers can interrupt (barge-in was 2 Nov: check no_repeat) |
| 7 | 2026-11-15_dlg_en_new_joiner_docs | Sun · EN · counter | Realistic office, a new hire holding a folder of papers, confused, looking around. Says in English: "Nobody told me where to send my documents." | HR4U: onboarding stages pending docs → background check → cleared → active; appointment letter acknowledged in the inbox |

Proof stays ≤ 1 in 5 posts and story ≤ 2 a week (presets.md). Velocity has not been posted since 18 Oct: #5 is its first Reel under the new rules, so log it carefully.

## Keep making (proven lane)
- A Veo character saying the problem in the first second (1.61x vs 0.84x, n=4 vs 7).
- Rizstay GST numbers any GST business can use, but only facts not taught in the last 21 days (the room slab, hotel restaurant 18%/5% and input-credit facts are blocked until 19-28 Nov).
- A voice on every beat (PROVEN 7 Nov): lay a character line or narration over each product screen.

## Dropped (losers, do not make again)
- Landscape clips cropped to portrait (7 Nov: 87.9% skip, 3.1s average watch).
- Narrator-only openers when a dialogue clip could be made (0.84x median, n=7).
- Calm desk/accountant shots with no motion at frame 0 (29 Oct: 78.3% skip).
- Brand intros, polls, generic "AI automation" lists, vague hotel-experience lines, Velocity "sales target" framing (25 Oct review).
- Voxa website marketing pages as the main visual (28 Oct).

## Series plan
- **Bablu ka Hotel** (story, max 2 a week): EP4 HR4U clock-out (EN), EP5 Rizstay QR menu (HI). One product per episode, a new story each time.
- **Moment Reels** (proof length): one 8s scene with a real-looking owner speaking, then 2-3 fact screens with a voice on each.
- ELI5 and countdown are down to weight 1 (presets.md): run each once in the next two weeks, with a dialogue opener, to re-test.

## Clip-run log (hourly dialogue-clip task)
- 2026-11-10 14:07 UTC: BLOCKED, no clip made. Claude in Chrome reports 4 connected browsers ("Browser 1-4", Windows) and none selected for the session, so it refuses every browser action until the owner picks one. Next Reel = HINDI (8 Nov EN was last valid); next story = queue #2 kitchen waste (rizstay_stock). Drive "1 - Gemini clips" has 0 unused Hindi dlg clips; last clips made 8 Nov 18:41 UTC. Owner notified. Later runs: if still blocked, don't notify again the same day.
- 2026-11-10 16:06 UTC: still BLOCKED, no clip made. Claude in Chrome now lists 2 connected browsers ("Browser 1", "Browser 2", Windows), none selected; the task must not pick one itself. Next = HINDI, queue #2 kitchen waste (rizstay_stock). Drive still has 0 unused Hindi dlg clips. Owner already notified at 14:07, not notified again.
- 2026-11-11 12:35-12:55 IST (main session): made 2026-11-11_dlg_hi_ep5_bablu_paneer (10s, 720x1280, speech 3.1-9.2s) and 2026-11-11_dlg_hi_ep5_ramu_waste (10s, speech 1.6-6.3s); new character RAMU: plump 45-year-old Indian hotel cook, round cheeks, short grey-black hair, small neat moustache, white cook's apron over a checked shirt, white cook's cap. Two extra Bablu takes were generated by accident (UI lag made a resend look necessary): chats 198c9c4a3ac533e5 and c3d9a56716414c08, not downloaded. Then the daily video limit: the Videos prompt box goes read-only (contenteditable=false) a few seconds after the page loads. Lesson: after clicking send, wait up to 40 s for the prompt bubble before deciding it failed; each resend can cost a video.
- 2026-11-12 07:07 UTC: STOPPED, no clip made. Selected "Browser 2" as the owner chose, but Gemini there is signed in as a personal Google account (display name "Daipayan Das", Pro), not Sutrixa International, so per the owner rule the task stopped (the Browser 1/2 labels may have swapped on reconnect). Nothing was sent to Gemini. Next Reel needing clips = ENGLISH (EP5 Hindi is rendered with all 5 clips, waiting on vidIQ reconnect); planned story = queue #7 new joiner docs (hr4u_onboarding_docs), since #1 (hr4u_attendance_payroll, 5 Nov) and #5 (velocity_social_posting, 8 Nov) are inside 14 days and #3 clinic overlaps voxa_missed_calls (2 Nov). Drive has 0 unused English dlg clips; last clip 11 Nov 18:03 UTC. Owner not notified (under 24 h).
