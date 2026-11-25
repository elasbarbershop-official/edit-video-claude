# Elas Barbershop — video projects

Each folder (e.g. `vijay-transformasi/`, `keratin-vs-rebonding/`) is a HyperFrames project for
Elas Barbershop social reels (1080×1920, Malay).

## Brand rules — apply to EVERY video

1. **End every video with the locked logo outro.** Install it with `brand/install-outro.sh <project>`,
   then mount `compositions/elas-outro.html` as the last scene, 4.2 s long, starting on the word
   "Elas" in the voiceover (or the final beat). Keep the previous scene running ~0.4 s past that
   point so the wipe reveals over it. Never edit the outro inside a project; change the master in
   `brand/elas-outro/` and re-install it everywhere.
2. **Background music on every video.** Bed tracks are in `brand/music/` (`elas-lofi-90.mp3` default,
   `elas-trap-100.mp3` energetic). They are 30 s seamless loops: extend to the film length with
   ffmpeg `-stream_loop`, put them in the root as `<audio id="music-bed">`, about 0.25 volume under
   voice, raised to about 0.6 over the outro, with a fade-out at the end.
3. Colours: navy `#091936`, yellow `#FFBA00`, off-white `#FAF8F2`. Font: Montserrat 800/900.
4. Voiceover: ElevenLabs "Brian" (`nPczCjzI2devNBz1zQrb`, `eleven_multilingual_v2`). Write
   "Ke-ratin" in TTS text so it is pronounced correctly; add `<break time="0.5s" />` before punchlines.
5. Finish at about −15 LUFS (`loudnorm=I=-15:TP=-1.5`) with no clipping.
6. **Every finished video gets a `CAPTION.md`** in its project folder, delivered with the render:
   - **TikTok:** 2–3 short lines in Malay: the hook question, a "tengok sampai habis" pull, and a
     comment CTA (e.g. Komen "KERATIN"). Then 5–6 hashtags: 2–3 topic tags, `#elasbarbershop`,
     `#fyp`, and one Malaysia tag.
   - **Instagram:** the hook, then 3–4 key points as emoji bullets (✂️ ✨ ⏳), the verdict, and a
     comment/DM-to-book CTA. Add any footnote the video has (e.g. "bergantung pada jenis rambut").
     Then 10–14 hashtags mixing topic, Malaysian hair/barber tags, `#reelsmalaysia` and `#elasbarbershop`.
   - Claims must match the video. No invented prices, locations or results. Ask for the shop's
     location hashtag rather than guessing one.
7. **Animated explainer style (default for tips/education reels):** build with the generator in
   `siri/` (`siri/specs.py` → `python3 siri/tools/build.py <slug>` → `siri/tools/finish.sh <slug>`).
   It applies the house style: the Elas 2D character (`siri/tools/character.py`) as the hero,
   word-by-word captions with the spoken word highlighted, a short top title with one keyword in a
   yellow block, tick badge pills, navy/cream alternating scenes, yellow tip scenes, diagonal stripe
   transitions, the comment-box CTA, music bed and the locked logo outro. New topics are added as
   entries in `siri/specs.py`.
8. **Landscape (16:9, 1920×1080) versions are full screen.** Never put the portrait video in the
   middle with side panels. Build the landscape natively at 1920×1080 and end it with
   `compositions/elas-outro-16x9.html` (installed by `brand/install-outro.sh`):
   - Animated siri videos: `python3 siri/tools/build.py --16x9 <slug>` → `siri/tools/finish.sh <slug>-16x9`
     (renders to `siri/renders/landscape/<slug>-16x9.mp4`). Text column left, character on the right.
   - Real footage: a `landscape/` HyperFrames project beside the portrait one (see
     `vijay-transformasi/landscape/`): footage fills the frame (cover crop framed on the hair), text on
     the left over a navy gradient, before/after side by side, same VO, music and finished audio mix.
   - YouTube gets the 16:9 version as a normal video (not a Short).
9. **Content studio (`studio/`)** for the series "DI SEBALIK KERUSI BARBER — BY ELA'S" (tagline "Lebih
   daripada sekadar gunting rambut."). 70 topics are in `studio/content/topics.json` and the 30-day plan
   is `studio/tools/studio.py calendar`. Weekday themes: Mon hair myths, Tue business, Wed style,
   Thu history, Fri barber life, Sat products, Sun motivation. A new video is an entry in `siri/specs.py`
   with `topic_id`. Business and story topics use the scene types `shop/chart/split/morph/follow`
   (`siri/tools/style_biz.py`, stickman). Build it with `studio.py make <id> --render` (both sizes).
   Rules: never invent the founder's experience, testimonials, customer stories, prices or product
   claims; label every money figure as "contoh ilustrasi"; health topics need reliable sources, no
   diagnosis or cure claims, and should suggest seeing a professional; nothing is scheduled without the
   owner's approval. Set the topic's status as you go (Idea → … → Published).
10. **Posting pattern (Metricool, auto-publish, Asia/Kuala_Lumpur), one set per video:** Instagram Reel 10:00 ·
    Google Business Profile 11:00 (type "photo" = video to the gallery, no text; Google takes videos of 30 s
    or less, so post `siri/renders/gbp/<slug>-30s.mp4` made by `python3 siri/tools/gbp_cut.py <slug>`) ·
    Facebook Reel 12:00 · YouTube Short 9:16 16:00 · TikTok 18:00 · Threads 20:00 (TikTok caption without
    #fyp, under 500 characters) · YouTube normal video 16:9 14:00 (moved from 21:00 per Metricool best-time data). Animated videos are marked AI-generated
    on IG/YT/TikTok; real-customer footage is not. Media URLs are the public raw.githubusercontent links on
    this branch, so push the renders before scheduling.
