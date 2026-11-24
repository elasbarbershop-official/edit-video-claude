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
