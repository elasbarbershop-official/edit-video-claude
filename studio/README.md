# ELA'S AI Content Studio: Di Sebalik Kerusi Barber

The production system for Ela's Barbershop's faceless animated reels. It covers the series
**DI SEBALIK KERUSI BARBER, BY ELA'S** ("Lebih daripada sekadar gunting rambut.") and the earlier
tips series. Every video is rendered in 9:16 for TikTok, Reels and Shorts, and in full-screen 16:9 for YouTube.

## How it fits together

| Part | Where | What it does |
|---|---|---|
| Topic database (70 titles, 7 categories) | `studio/content/topics.json` | Title, category, sub-series, style, status, linked video slug, fact-check flag |
| 30-day calendar | `studio/content/calendar.json`, `CALENDAR.md` | Keeps the Mon/Wed/Fri tips already scheduled in Metricool and fills Tue/Thu/Sat/Sun from the weekday themes |
| Brand / video / voice config | `studio/config/*.json` | Colours, fonts, logo, outro, formats, loudness, voice and pronunciation |
| Scripts and storyboards | `siri/specs.py` | One entry per video. Every scene has its voiceover line, on-screen text and visual type, plus cue words that time each animation to the spoken word |
| Animation engine | `siri/tools/build.py`, `style2.py`, `style_biz.py`, `stickman.py`, `character.py`, `icons.py` | Builds HyperFrames compositions from the spec, in both 9:16 and 16:9 (`--16x9`) |
| Voiceover | `build.py` → ElevenLabs Brian | Cached per line. Whisper takes word timestamps from the real audio, so captions and animations follow the actual speech |
| Subtitles | `style2.captions` | Burned-in, word by word, with the spoken word highlighted |
| Render + mix | `siri/tools/finish.sh` | Lint/layout/contrast check, render, loudness −15 LUFS |
| Captions | `CAPTION.md` per video | TikTok and Instagram text in the house pattern (see the root `CLAUDE.md`) |
| Publishing | Metricool (connected) | Scheduled by Claude only after you approve |

### Why HyperFrames rather than Remotion

The brief suggested Remotion. This repo already renders reliably with HyperFrames (HTML + GSAP,
headless Chromium + FFmpeg), and the locked logo outro, music beds, voice pipeline and 20 finished
videos all use it. Switching to Remotion would add a second toolchain and a licence question for
company use, and it would not improve the output. Both tools render code-based animation to MP4.

### Colours

`config/brand.json` uses the colours sampled from the official logo (#091936 / #FFBA00 / #FAF8F2).
The brief listed #0A1A37 / #FCBE06 / #F8F7F2, which look the same on screen. Keeping the logo values
means every scene matches the locked outro exactly.

## Commands

```bash
cd studio
npm run topics                       # list all 70 topics with status
npm run topics -- --cat D            # one category (A–G)
npm run calendar -- --days 30 --start 2026-11-26
npm run generate -- 31               # build 9:16 + 16:9 projects for topic 31 (needs a script in siri/specs.py)
npm run render -- 31                 # build and render both, then set the status to Review
python3 tools/studio.py add "Tajuk baharu?" --cat F
python3 tools/studio.py status 31 Approved
python3 tools/studio.py perf 31 views=1200 likes=80 comments=12 shares=9 saves=30 --platform tiktok
npm run report                       # category ranking from the real numbers you recorded
```

Status flow: Idea → Research → Script → Storyboard → Production → Rendering → Review → Approved → Scheduled → Published.

## Asking Claude in plain Malay

Open Claude Code in this repo and say what you want. Claude writes the script into `siri/specs.py`,
builds it, reviews the frames, renders both sizes, writes `CAPTION.md` and asks before scheduling. For example:

- "Hasilkan video untuk tajuk 32."
- "Hasilkan tujuh video untuk minggu ini." (Claude takes the next seven calendar slots)
- "Hasilkan video mengenai perbezaan Pomade dan Hair Wax." (topic 51)
- "Jadualkan video 21 di Metricool hari Selasa 1 Dis." (only after you approve the render)

## Pilot video

`siri/renders/21-kedai-penuh-tapi-rugi.mp4` (9:16) and `siri/renders/landscape/21-kedai-penuh-tapi-rugi-16x9.mp4`
are topic 31, "Kedai gunting penuh pelanggan, tetapi kenapa masih rugi?" (44.7 s, Brian voice, −15.8 LUFS).
The scenes are: a full shop of stickman barbers that dims into a worried owner and an RM0 wallet; sales vs
profit charts with a ≠ stamp; an RM100 cost split (gaji, sewa, elektrik, peralatan, produk, operasi) whose
balance counts down to RM10, labelled as an illustrative example; a clipper that turns into a management
dashboard; a follow card; and the locked logo outro. Status: **Review**, not yet scheduled.

## Costs

| Service | Used for | Cost |
|---|---|---|
| ElevenLabs Starter (already subscribed) | Brian voiceover | Monthly plan; one 45 s video uses roughly 700–900 characters |
| Metricool (already connected) | Scheduling and analytics | Your current plan |
| HyperFrames, FFmpeg, Whisper, Chromium | Rendering, alignment | Free and local |
| Music beds and SFX in `brand/` | Sound | Generated or royalty-free, licence notes in `assets/sfx/CREDITS.md` |

## Not built yet (honest list)

- **Dashboard** (brief section 21). The command line and Claude Code do these jobs for now.
- **Automatic script writing inside the tool.** There is no AI API key in the pipeline. Claude Code writes the scripts on request, and you approve them.
- **Research engine with source lists.** Health (A), history (E) and product (F) topics are flagged `needs_fact_check`. Claude checks sources when writing those scripts and marks anything it cannot verify.
- **Styles B (cinematic 2.5D), D (documentary) and E (product explainer).** Only styles A (2D motion graphics and character) and C (stickman business) exist. Style E needs official ELA'S Barber Care product photos and verified product claims before it can be built.
- **Thumbnails, SRT export and 1:1 format.**
- **Automatic analytics import.** Numbers are recorded with `perf`. Metricool analytics can be read on request.
