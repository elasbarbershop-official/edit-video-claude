"""Build Elas tips-series reels from siri/specs.py.

usage: python3 siri/tools/build.py [slug-prefix ...]   (no args = all videos)
Per video: ElevenLabs Brian VO per scene (cached), Whisper word cues, scene compositions,
root index.html with SFX + music + locked elas-outro, SCRIPT.md and CAPTION.md.
"""
import hashlib, json, os, re, shutil, subprocess, sys, urllib.request
from html import escape

ROOT = "/home/user/edit-video-claude"
SIRI = f"{ROOT}/siri"
sys.path.insert(0, f"{SIRI}/tools"); sys.path.insert(0, SIRI)
import icons  # noqa: E402
import style2 as S2  # noqa: E402
from specs import VIDEOS  # noqa: E402

VOICE = "nPczCjzI2devNBz1zQrb"  # Brian
NAVY, YEL, CREAM = "#091936", "#ffba00", "#faf8f2"
THEME = {
    "navy": dict(bg=NAVY, text=CREAM, hl=YEL, vars=f"--ink:{CREAM};--acc:{YEL};--paper:#1c2d55;"),
    "cream": dict(bg=CREAM, text=NAVY, hl=NAVY, vars=f"--ink:{NAVY};--acc:{YEL};--paper:#ffffff;"),
    "yellow": dict(bg=YEL, text=NAVY, hl=NAVY, vars=f"--ink:{NAVY};--acc:{CREAM};--paper:#ffffff;"),
}
SFX_SRC = f"{ROOT}/keratin-vs-rebonding/assets/sfx"
PEAK = {"whoosh": 0.16, "whoosh-cinematic": 0.70, "impact-bass-1": 0.07, "pop": 0.12, "click": 0.07, "sparkle": 0.03, "typing": 0.03}
_whisper = None


def sh(*a, **k):
    return subprocess.run(a, check=True, capture_output=True, text=True, **k).stdout


def dur(f):
    return float(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f))


def f2(x):
    return f"{x:.2f}".rstrip("0").rstrip(".") if abs(x) > 1e-9 else "0"


def fit(lines, width, mx, k=0.8):
    n = max(len(l) for l in lines)
    return int(min(mx, width / (k * max(n, 1))))


def tts_text(s):
    s = re.sub(r"\b[Kk]eratin\b", lambda m: "ke-ratin", s)
    return s


# ---------------------------------------------------------------- voice + cues
def make_vo(proj, i, text):
    out = f"{proj}/assets/vo/vo{i}"
    h = hashlib.sha1(text.encode()).hexdigest()[:12]
    meta = f"{out}.json"
    if os.path.exists(meta) and json.load(open(meta)).get("hash") == h and os.path.exists(out + ".wav"):
        return json.load(open(meta))
    body = json.dumps({"text": text, "model_id": "eleven_multilingual_v2",
                       "voice_settings": {"stability": 0.5, "similarity_boost": 0.8, "style": 0.3, "use_speaker_boost": True}}).encode()
    req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE}?output_format=mp3_44100_128", data=body,
                                 headers={"xi-api-key": "proxy-injected", "Content-Type": "application/json"})
    try:
        data = urllib.request.urlopen(req, timeout=180).read()
    except urllib.error.HTTPError as e:
        raise SystemExit(f"ElevenLabs error {e.code}: {e.read()[:300]!r}")
    open(out + ".mp3", "wb").write(data)
    sh("ffmpeg", "-nostdin", "-v", "error", "-y", "-i", out + ".mp3", "-af",
       "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse",
       "-ar", "48000", "-ac", "1", out + ".wav")
    os.remove(out + ".mp3")
    global _whisper
    if _whisper is None:
        import whisper
        _whisper = whisper.load_model("small")
    r = _whisper.transcribe(out + ".wav", language="ms", word_timestamps=True)
    words = [(w["word"].strip(), round(w["start"], 2)) for s in r["segments"] for w in s["words"]]
    m = dict(hash=h, text=text, dur=round(dur(out + ".wav"), 3), words=words)
    json.dump(m, open(meta, "w"), ensure_ascii=False, indent=1)
    return m


def norm(w):
    w = re.sub(r"[^a-z0-9]", "", w.lower())
    return "komen" + w[7:] if w.startswith("comment") else w


def cue(vo, token, frac=0.5):
    if token:
        t = norm(token)
        for w, s in vo["words"]:
            nw = norm(w)
            if nw and (nw.startswith(t[:5]) or t.startswith(nw[:5]) and len(nw) >= 3):
                return s
    return vo["dur"] * frac


# ---------------------------------------------------------------- scene html
def scene_file(sid, theme, body_css, body_html, tl_js, first=False):
    th = THEME[theme]
    wipe = "" if first else 'tl.fromTo("#root", { clipPath: "inset(0% 0% 0% 100%)" }, { clipPath: "inset(0% 0% 0% 0%)", duration: 0.35, ease: "power3.inOut" }, 0);\n    '
    return f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; background: {th['bg']}; color: {th['text']}; font-family: "Montserrat", sans-serif; overflow: hidden; {th['vars']} }}
    #root .ic svg {{ width: 100%; height: 100%; display: block; }}
{body_css}
  </style>
  <div id="root" data-composition-id="{sid}" data-width="1080" data-height="1920">
{body_html}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {wipe}{tl_js}
    window.__timelines["{sid}"] = tl;
  </script>
</template>
"""


def title_html(sid, lines, top, size, hl_idx, theme, block_hl=False):
    th = THEME[theme]
    out, css = [], []
    for j, l in enumerate(lines):
        y = top + j * size * 1.02
        col = th["hl"] if j in hl_idx else th["text"]
        style = f"top:{y:.0f}px;font-size:{size}px;color:{col};"
        if j in hl_idx and block_hl:
            style = f"top:{y:.0f}px;font-size:{size}px;color:{YEL};background:{NAVY};padding:0 14px;margin-left:-14px;"
        out.append(f'    <div id="{sid}-t{j}" class="ttl" style="{style}">{escape(l)}</div>')
    return "\n".join(out), top + len(lines) * size * 1.02


BASE_CSS = """    .ttl { position: absolute; left: 130px; font-weight: 900; line-height: 1; letter-spacing: -0.01em; white-space: nowrap; transform-origin: 0% 50%; }
    .sub { position: absolute; left: 130px; width: 650px; font-weight: 700; font-size: 44px; line-height: 1.22; }
    .ic { position: absolute; }"""


def build_hook(sid, sc, vo, series, lead):
    lines = sc["lines"]
    size = fit(lines, 650, 118)
    t_html, bottom = title_html(sid, lines, 600, size, sc["hl"], "navy")
    html = f"""    <div id="{sid}-chip" style="position:absolute;left:130px;top:300px;padding:10px 18px;background:{YEL};color:{NAVY};font-weight:900;font-size:30px;letter-spacing:0.08em;line-height:1;">{escape(series)}</div>
    <div id="{sid}-ic" class="ic" style="left:600px;top:280px;width:270px;height:270px;">{icons.svg(sc['icon'], sid)}</div>
{t_html}
    <div id="{sid}-sub" class="sub" style="top:{bottom + 30:.0f}px;color:{CREAM};">{escape(sc['sub'])}</div>"""
    js = (f'tl.fromTo("#{sid}-ic", {{ scale: 0.88, rotation: -8 }}, {{ scale: 1, rotation: 0, duration: 0.45, ease: "back.out(2)" }}, 0);\n    '
          + "".join(f'tl.fromTo("#{sid}-t{j}", {{ scale: 1.07 }}, {{ scale: 1, duration: 0.3, ease: "power4.out" }}, {j * 0.05:.2f});\n    ' for j in range(len(lines)))
          + f'tl.fromTo("#{sid}-sub", {{ opacity: 0.0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, {lead + vo["dur"] * 0.45:.2f});')
    sfx = [("impact-bass-1", 0.0, 0.45), ("pop", lead + vo["dur"] * 0.45, 1.3)]
    return "navy", BASE_CSS, html, js, sfx


def dots_html(sid, k, n, theme):
    if n < 2:
        return ""
    th = THEME[theme]
    out = []
    x = 130
    for j in range(n):
        w = 84 if j == k else 40
        op = 1 if j <= k else 0.25
        out.append(f'<div style="position:absolute;left:{x}px;top:1160px;width:{w}px;height:14px;border-radius:7px;background:{th["text"]};opacity:{op};"></div>')
        x += w + 12
    return f'    <div id="{sid}-dots">' + "".join(out) + "</div>"


def build_point(sid, sc, vo, theme, num, k, n, lead):
    th = THEME[theme]
    size = fit(sc["title"], 700, 110)
    t_html, bottom = title_html(sid, sc["title"], 710, size, [], theme)
    mark = YEL if theme == "cream" else CREAM
    html = f"""    <div id="{sid}-num" style="position:absolute;left:130px;top:290px;z-index:1;font-weight:900;font-size:150px;line-height:1;color:{th['text']};">
      <div style="position:absolute;left:-10px;right:-10px;bottom:14px;height:46px;background:{mark};z-index:-1;"></div>{num:02d}</div>
    <div id="{sid}-ic" class="ic" style="left:490px;top:270px;width:390px;height:390px;">{icons.svg(sc['icon'], sid)}</div>
{t_html}
    <div id="{sid}-sub" class="sub" style="top:{bottom + 24:.0f}px;color:{th['text']};">{escape(sc['sub'])}</div>
{dots_html(sid, k, n, theme)}"""
    ts = lead + cue(vo, sc.get("cs"), 0.45)
    js = (f'tl.fromTo("#{sid}-num", {{ scale: 0.5, opacity: 0, transformOrigin: "0% 100%" }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.4)" }}, 0.15);\n    '
          f'tl.fromTo("#{sid}-ic", {{ scale: 0.6, rotation: -12, opacity: 0 }}, {{ scale: 1, rotation: 0, opacity: 1, duration: 0.4, ease: "back.out(2)" }}, 0.25);\n    '
          + "".join(f'tl.fromTo("#{sid}-t{j}", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.3, ease: "power3.inOut" }}, {0.35 + j * 0.12:.2f});\n    ' for j in range(len(sc["title"])))
          + f'tl.fromTo("#{sid}-sub", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, {ts:.2f});')
    sfx = [("pop", 0.15, 1.3), ("click", ts, 1.0)]
    return theme, BASE_CSS, html, js, sfx


def build_tip(sid, sc, vo, theme, lead):
    th = THEME[theme]
    size = fit(sc["title"], 720, 104)
    t_html, bottom = title_html(sid, sc["title"], 660, size, [len(sc["title"]) - 1], theme, block_hl=(theme != "navy"))
    html = f"""    <div id="{sid}-ic" class="ic" style="left:130px;top:300px;width:300px;height:300px;">{icons.svg(sc['icon'], sid)}</div>
{t_html}
    <div id="{sid}-sub" class="sub" style="top:{bottom + 26:.0f}px;color:{th['text']};">{escape(sc['sub'])}</div>"""
    ts = lead + cue(vo, sc.get("cs"), 0.5)
    js = (f'tl.fromTo("#{sid}-ic", {{ scale: 0.4, rotation: -20, opacity: 0 }}, {{ scale: 1, rotation: 0, opacity: 1, duration: 0.45, ease: "back.out(2.2)" }}, 0.2);\n    '
          + "".join(f'tl.fromTo("#{sid}-t{j}", {{ scale: 1.25, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "power4.out" }}, {0.4 + j * 0.18:.2f});\n    ' for j in range(len(sc["title"])))
          + f'tl.fromTo("#{sid}-sub", {{ opacity: 0, y: 16 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, {ts:.2f});')
    sfx = [("sparkle", 0.45, 0.35), ("click", ts, 1.0)]
    return theme, BASE_CSS, html, js, sfx


def build_rows(sid, sc, vo, lead):
    n = len(sc["items"])
    h = min(250, int(760 / n))
    rows_html, js, sfx = [], [], []
    for j, r in enumerate(sc["items"]):
        y = 400 + j * h
        tx = 130 + h
        t = lead + cue(vo, r["cue"], (j + 0.3) / n)
        rows_html.append(f"""    <div id="{sid}-r{j}" style="position:absolute;left:0;top:{y}px;width:1080px;height:{h}px;">
      <div class="ic" style="left:120px;top:0px;width:{h - 10}px;height:{h - 10}px;">{icons.svg(r['icon'], f'{sid}r{j}')}</div>
      <div style="position:absolute;left:{tx}px;top:{h / 2 - 78:.0f}px;font-weight:900;font-size:58px;line-height:1;color:{NAVY};white-space:nowrap;">{escape(r['label'])}</div>
      <div id="{sid}-d{j}" style="position:absolute;left:{tx}px;top:{h / 2 - 8:.0f}px;width:{780 - tx}px;font-weight:700;font-size:38px;line-height:1.2;color:{NAVY};">{escape(r['desc'])}</div>
    </div>""")
        js.append(f'tl.fromTo("#{sid}-r{j}", {{ x: -60, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.35, ease: "power4.out" }}, {t:.2f});')
        js.append(f'tl.fromTo("#{sid}-d{j}", {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power2.out" }}, {t + 1.1:.2f});')
        js.append(f'tl.{"set" if j == 0 else "to"}("#{sid}-hl", {{ y: {j * h}, opacity: 1{"" if j == 0 else ", duration: 0.35, ease: \"power3.inOut\""} }}, {t:.2f});')
        sfx.append(("click", t, 1.1))
    html = f'    <div id="{sid}-hl" style="position:absolute;left:100px;top:{400 - 6}px;width:700px;height:{h - 2}px;border-radius:24px;background:{YEL};opacity:0;"></div>\n'
    html += f'    <div id="{sid}-head" style="position:absolute;left:130px;top:300px;font-weight:800;font-size:54px;line-height:1;color:{NAVY};">{escape(sc["head"])}</div>\n' + "\n".join(rows_html)
    js.insert(0, f'tl.fromTo("#{sid}-head", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.35, ease: "power3.inOut" }}, 0.2);')
    return "cream", BASE_CSS, html, "\n    ".join(js), sfx


def build_compare(sid, sc, vo, lead):
    html, js, sfx = [], [], []
    for j, (key, x) in enumerate([("L", 130), ("R", 465)]):
        sd = sc[key]
        t = lead + cue(vo, sd["cue"], 0.1 if j == 0 else 0.55)
        ls = fit([sd["label"]], 280, 44)
        items = []
        for m, (sign, text) in enumerate(sd["items"]):
            yy = 300 + m * 130
            if sign == "+":
                badge = f'<svg viewBox="0 0 52 52" width="52" height="52"><circle cx="26" cy="26" r="24" fill="{YEL}"/><path d="M14 27 L23 36 L39 18" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            elif sign == "-":
                badge = f'<svg viewBox="0 0 52 52" width="52" height="52"><circle cx="26" cy="26" r="24" fill="{NAVY}"/><path d="M17 17 L35 35 M35 17 L17 35" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/></svg>'
            else:
                badge = f'<svg viewBox="0 0 52 52" width="52" height="52"><circle cx="26" cy="26" r="24" fill="{NAVY}"/><circle cx="26" cy="26" r="7" fill="{CREAM}"/></svg>'
            items.append(f'<div id="{sid}-{key}i{m}" style="position:absolute;left:18px;top:{yy}px;width:280px;"><div style="position:absolute;left:0;top:0;">{badge}</div>'
                         f'<div style="position:absolute;left:66px;top:4px;width:212px;font-weight:700;font-size:30px;line-height:1.18;color:{NAVY};">{escape(text)}</div></div>')
            js.append(f'tl.fromTo("#{sid}-{key}i{m}", {{ x: 30, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {t + 0.35 + m * 0.3:.2f});')
        html.append(f"""    <div id="{sid}-{key}" style="position:absolute;left:{x}px;top:330px;width:315px;height:780px;border-radius:28px;background:{CREAM};--ink:{NAVY};--acc:{YEL};--paper:#ffffff;">
      <div style="position:absolute;left:0;top:30px;width:315px;text-align:center;font-weight:900;font-size:{ls}px;line-height:1;color:{NAVY};">{escape(sd['label'])}</div>
      <div class="ic" style="left:67px;top:96px;width:180px;height:180px;">{icons.svg(sd['icon'], f'{sid}{key}')}</div>
      {''.join(items)}
    </div>""")
        js.insert(0, f'tl.fromTo("#{sid}-{key}", {{ y: 120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power4.out" }}, {t:.2f});')
        sfx.append(("pop", t, 1.3))
    return "navy", BASE_CSS, "\n".join(html), "\n    ".join(js), sfx


def build_cta(sid, sc, vo, lead):
    ask = sc["ask"]
    size = fit(ask, 720, 76, 0.62)
    lines = "".join(f'<div style="color:{YEL if j == len(ask) - 1 else CREAM};">{escape(l)}</div>' for j, l in enumerate(ask))
    tk = lead + cue(vo, "komen", 0.35)
    wi = [i for i, (w, s) in enumerate(vo["words"]) if norm(w).startswith("komen")]
    tw = lead + vo["words"][wi[0] + 1][1] if wi and wi[0] + 1 < len(vo["words"]) else tk + 0.4
    word = sc["word"]
    t_end = tw + 0.07 * len(word)
    html = f"""    <div id="{sid}-q" style="position:absolute;left:130px;top:330px;font-weight:900;font-size:{size}px;line-height:1.08;">{lines}</div>
    <div id="{sid}-box" style="position:absolute;left:130px;top:720px;width:650px;height:120px;border-radius:60px;background:{CREAM};">
      <div style="position:absolute;left:22px;top:22px;width:76px;height:76px;border-radius:38px;background:{YEL};"></div>
      <div id="{sid}-ph" style="position:absolute;left:124px;top:38px;color:#7d8291;font-weight:600;font-size:40px;line-height:1;">Tambah komen...</div>
      <div id="{sid}-typed" style="position:absolute;left:124px;top:34px;color:{NAVY};font-weight:900;font-size:48px;line-height:1;letter-spacing:0.04em;"></div>
      <div id="{sid}-send" style="position:absolute;right:16px;top:16px;width:88px;height:88px;border-radius:44px;background:#d7d9df;"><svg style="position:absolute;left:22px;top:22px" width="44" height="44" viewBox="0 0 44 44"><path d="M6 22 L38 6 L28 38 L22 24 Z" fill="{NAVY}"/></svg></div>
    </div>
    <div id="{sid}-reply" style="position:absolute;left:230px;top:880px;padding:22px 30px;border-radius:34px 34px 34px 8px;background:{YEL};color:{NAVY};font-weight:900;font-size:44px;line-height:1;white-space:nowrap;">{escape(sc['reply'])}</div>"""
    js = f"""tl.fromTo("#{sid}-q", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.4, ease: "power3.inOut" }}, 0.25);
    tl.fromTo("#{sid}-box", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "power4.out" }}, {max(0.6, tk - 0.6):.2f});
    tl.set("#{sid}-ph", {{ opacity: 0 }}, {tw - 0.02:.2f});
    const word = {json.dumps(word)}, typed = document.querySelector("#{sid}-typed"), st = {{ n: 0 }};
    tl.set(typed, {{ textContent: "" }}, 0);
    tl.fromTo(st, {{ n: 0 }}, {{ n: word.length, duration: {0.07 * len(word):.2f}, ease: "none", immediateRender: false, onUpdate: () => {{ typed.textContent = word.slice(0, Math.floor(st.n + 0.0001)); }} }}, {tw:.2f});
    tl.to("#{sid}-send", {{ backgroundColor: "{YEL}", duration: 0.1, ease: "none" }}, {t_end + 0.05:.2f});
    tl.fromTo("#{sid}-send", {{ scale: 1 }}, {{ scale: 0.85, duration: 0.08, ease: "power2.in", yoyo: true, repeat: 1, immediateRender: false }}, {t_end + 0.1:.2f});
    tl.fromTo("#{sid}-reply", {{ scale: 0.5, opacity: 0, transformOrigin: "0% 100%" }}, {{ scale: 1, opacity: 1, duration: 0.28, ease: "back.out(2.2)" }}, {t_end + 0.45:.2f});"""
    sfx = [("typing", tw, 0.9, min(0.75, 0.07 * len(word) + 0.2), 0.42), ("click", t_end + 0.1, 1.3), ("pop", t_end + 0.45, 1.4)]
    return "navy", BASE_CSS, html, js, sfx


# ---------------------------------------------------------------- project
def setup(proj, music):
    for d in ("compositions", "assets/vo", "assets/sfx", "assets/music", "assets/vendor"):
        os.makedirs(f"{proj}/{d}", exist_ok=True)
    shutil.copy(f"{ROOT}/keratin-vs-rebonding/assets/vendor/gsap.min.js", f"{proj}/assets/vendor/")
    for f in ("whoosh", "whoosh-cinematic", "impact-bass-1", "pop", "click", "sparkle", "typing"):
        shutil.copy(f"{SFX_SRC}/{f}.mp3", f"{proj}/assets/sfx/")
    shutil.copy(f"{SFX_SRC}/CREDITS.md", f"{proj}/assets/sfx/")
    src = {"lofi": "elas-lofi-90", "trap": "elas-trap-100"}[music]
    mp = f"{proj}/assets/music/{src}-90s.mp3"
    if not os.path.exists(mp):
        sh("ffmpeg", "-nostdin", "-v", "error", "-y", "-stream_loop", "3", "-i", f"{ROOT}/brand/music/{src}.mp3", "-t", "90", "-c:a", "libmp3lame", "-b:a", "192k", mp)
    sh(f"{ROOT}/brand/install-outro.sh", proj)
    for f in ("hyperframes.json", "package.json"):
        shutil.copy(f"{ROOT}/keratin-vs-rebonding/{f}", proj)
    return mp.split(proj + "/")[1], src


def build(v):
    slug = v["slug"]; proj = f"{SIRI}/{slug}"
    os.makedirs(proj, exist_ok=True)
    music_path, music_src = setup(proj, v["music"])
    json.dump({"id": f"elas-{slug}", "name": slug}, open(f"{proj}/meta.json", "w"))
    scenes = v["scenes"]
    vos = []
    for i, sc in enumerate(scenes):
        text = tts_text(sc["vo"])
        if sc["t"] == "cta":
            text += ' <break time="1.0s" /> Elas Barbershop.'
        vos.append(make_vo(proj, i + 1, text))
    npts = sum(1 for s in scenes if s["t"] == "point")
    t = 0.0; hosts = []; sfx_abs = []; prev_theme = None; k = 0; z = 1; vo_tags = []; outro_start = None
    alt = "cream"
    for i, sc in enumerate(scenes):
        sid = f"s{i + 1}"; vo = vos[i]
        lead = 0.15 if i == 0 else 0.3
        if sc["t"] == "hook":
            theme, css, html, js, sfx = S2.s_hook(sid, sc, vo, lead, v["series"], cue)
        elif sc["t"] in ("point", "rows"):
            theme = alt; alt = "navy" if alt == "cream" else "cream"
            if sc["t"] == "point":
                theme, css, html, js, sfx = S2.s_point(sid, sc, vo, lead, theme, k + 1, cue); k += 1
            else:
                theme, css, html, js, sfx = S2.s_rows(sid, sc, vo, lead, theme, cue)
        elif sc["t"] == "tip":
            theme, css, html, js, sfx = S2.s_tip(sid, sc, vo, lead, "yellow", cue)
        elif sc["t"] == "compare":
            theme, css, html, js, sfx = S2.s_compare(sid, sc, vo, lead, cue)
        elif sc["t"] == "cta":
            theme, css, html, js, sfx = S2.s_cta(sid, sc, vo, lead, cue)
        prev_theme = theme
        if sc["t"] == "cta":
            el = [s_ for w, s_ in vo["words"] if norm(w).startswith("elas")]
            cap_end = lead + (el[-1] if el else vo["dur"] - 1.0) + 0.45
        else:
            cap_end = lead + vo["dur"] + 0.35
        cap_css, cap_html, cap_js = S2.captions(sid, sc["vo"], vo, lead, theme, cap_end)
        open(f"{proj}/compositions/{sid}.html", "w").write(S2.scene_file(sid, theme, css, html, js, i == 0, cap_css, cap_html, cap_js))
        slot = lead + vo["dur"] + 0.35
        if sc["t"] == "cta":
            el = [s for w, s in vo["words"] if norm(w).startswith("elas")]
            outro_start = t + lead + (el[-1] if el else vo["dur"] - 1.0)
            slot = outro_start - t
        hosts.append((sid, t, slot + (0.45 if i < len(scenes) - 1 or sc["t"] == "cta" else 0), z)); z += 1
        vo_tags.append((i + 1, t + lead, vo["dur"]))
        if i > 0:
            if i % 2:
                sfx_abs.append(("whoosh", t + 0.1, 0.85, 0.57, 0))
            else:
                sfx_abs.append(("whoosh-cinematic", t - 0.45, 0.45, 1.2, 1.8))
        for s in sfx:
            name, at, vol = s[0], s[1], s[2]
            d = s[3] if len(s) > 3 else {"pop": 0.7, "click": 0.37, "sparkle": 1.8, "impact-bass-1": 2.1}.get(name, 0.6)
            ms = s[4] if len(s) > 4 else 0
            sfx_abs.append((name, max(0, t + at - PEAK[name]), vol, d, ms))
        t += slot
    total = round(outro_start + 4.2, 2)
    # lanes
    sfx_abs.sort(key=lambda x: x[1]); lanes = []; sfx_tags = []
    for n, (name, st, vol, d, ms) in enumerate(sfx_abs):
        for li, e in enumerate(lanes):
            if e <= st + 1e-6:
                lanes[li] = st + d; break
        else:
            lanes.append(st + d); li = len(lanes) - 1
        mattr = f' data-media-start="{f2(ms)}"' if ms else ""
        sfx_tags.append(f'      <audio id="sfx-{n + 1}" class="clip" src="assets/sfx/{name}.mp3" data-start="{f2(st)}" data-duration="{f2(d)}"{mattr} data-volume="{f2(vol)}" data-track-index="{li + 4}"></audio>')
    bed = 0.2 if music_src.startswith("elas-lofi") else 0.1
    peakv = 0.5 if music_src.startswith("elas-lofi") else 0.25
    host_tags = "\n".join(
        f'      <div id="{sid}" data-composition-id="{sid}" data-composition-src="compositions/{sid}.html" data-start="{f2(s)}" data-duration="{f2(d)}" data-track-index="{j % 2}" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index: {zz}"></div>'
        for j, (sid, s, d, zz) in enumerate(hosts))
    vo_html = "\n".join(f'      <audio id="vo-{n}" class="clip" src="assets/vo/vo{n}.wav" data-start="{f2(s)}" data-duration="{f2(d + 0.02)}" data-volume="1" data-track-index="3"></audio>' for n, s, d in vo_tags)
    index = f"""<!doctype html>
<html lang="ms" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: {NAVY}; }}
      #root {{ position: relative; width: 100%; height: 100%; }}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{f2(total)}" data-width="1080" data-height="1920">
{host_tags}
      <div id="elas-outro" data-composition-id="elas-outro" data-composition-src="compositions/elas-outro.html" data-start="{f2(outro_start)}" data-duration="4.2" data-track-index="0" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index: 50"></div>

      <!-- Music bed: brand/music/{music_src}.mp3 looped -->
      <audio id="music-bed" class="clip" src="{music_path}" data-start="0" data-duration="{f2(outro_start)}" data-volume="{bed}" data-fade-in="0.3" data-track-index="2"></audio>
      <audio id="music-outro" class="clip" src="{music_path}" data-start="{f2(outro_start)}" data-duration="4.2" data-media-start="{f2(outro_start)}" data-volume="{peakv}" data-fade-out="1.4" data-track-index="2"></audio>

      <!-- Voiceover: ElevenLabs Brian. Script: SCRIPT.md -->
{vo_html}

      <!-- SFX -->
{chr(10).join(sfx_tags)}
    </div>
    <script>
      window.__timelines = window.__timelines || {{}};
      window.__timelines["main"] = gsap.timeline({{ paused: true }});
    </script>
  </body>
</html>
"""
    open(f"{proj}/index.html", "w").write(index)
    write_docs(v, proj, total)
    return proj, total


def write_docs(v, proj, total):
    sc = v["scenes"]
    rows = "\n".join(f"| {i + 1} | {s['t']} | {s['vo']} |" for i, s in enumerate(sc))
    open(f"{proj}/SCRIPT.md", "w").write(
        f"# Skrip — {v['slug']}\n\nSiri: {v['series']}. Suara: ElevenLabs Brian. Muzik: {v['music']}. Panjang: {total:.1f} s.\n\n"
        f"| # | Babak | Voice over |\n|---|---|---|\n{rows}\n| — | outro | Elas Barbershop (logo outro dikunci) |\n")
    hook, ctas = sc[0], sc[-1]
    emo = ["✂️", "✨", "⏳", "💡", "✅", "👉"]
    bullets = []; e = 0
    for s in sc[1:-1]:
        if s["t"] in ("point", "tip"):
            bullets.append(f"{emo[e % len(emo)]} {' '.join(s['title']).title().replace(' & ', ' & ')}: {s['sub']}"); e += 1
        elif s["t"] == "rows":
            for r in s["items"]:
                bullets.append(f"{emo[e % len(emo)]} {r['label'].title()}: {r['desc']}"); e += 1
        elif s["t"] == "compare":
            for key in ("L", "R"):
                sd = s[key]
                bullets.append(f"{emo[e % len(emo)]} {sd['label'].title()}: " + ", ".join(x[1].lower() for x in sd["items"])); e += 1
    my = next((t for t in v["tags"] if "malaysia" in t), "#lelakimalaysia")
    tt = list(dict.fromkeys(v["tags"][:3] + ["#elasbarbershop", "#fyp", my]))
    ig = list(dict.fromkeys(v["tags"] + ["#rambutlelaki", "#menshairstyle", "#elasbarbershop", "#barbershopmalaysia", "#reelsmalaysia"]))[:14]
    cta_line = ctas["vo"]
    open(f"{proj}/CAPTION.md", "w").write(f"""# Caption — {v['slug']}

## TikTok

{hook['vo']}
Tengok sampai habis 👇

{cta_line} ✂️

{' '.join(tt)}

## Instagram

{hook['vo']} 👇

{chr(10).join(bullets)}

{cta_line} Atau DM kami untuk tempah slot 📩

{' '.join(ig)}
""")


if __name__ == "__main__":
    want = sys.argv[1:]
    for v in VIDEOS:
        if want and not any(v["slug"].startswith(w) for w in want):
            continue
        proj, total = build(v)
        print(f"built {v['slug']}  {total:.1f}s", flush=True)
