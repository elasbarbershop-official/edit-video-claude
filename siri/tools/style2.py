"""Style 2: illustrated character hero, word-by-word captions, highlight titles,
badge pills and diagonal stripe transitions. Used by build.py."""
import difflib, json, re
from html import escape

import icons
import character

NAVY, YEL, CREAM = "#091936", "#ffba00", "#faf8f2"
THEME = {
    "navy": dict(bg=NAVY, text=CREAM, vars=f"--ink:{CREAM};--acc:{YEL};--paper:#1c2d55;", shirt=CREAM,
                 hl_css=f"color:{YEL};", cap_hl=f"background:{YEL};color:{NAVY};"),
    "cream": dict(bg=CREAM, text=NAVY, vars=f"--ink:{NAVY};--acc:{YEL};--paper:#ffffff;", shirt="#091936",
                  hl_css=f"background:{YEL};color:{NAVY};padding:0 14px;margin-left:-14px;", cap_hl=f"background:{YEL};color:{NAVY};"),
    "yellow": dict(bg=YEL, text=NAVY, vars=f"--ink:{NAVY};--acc:{CREAM};--paper:#ffffff;", shirt="#091936",
                   hl_css=f"background:{NAVY};color:{YEL};padding:0 14px;margin-left:-14px;", cap_hl=f"background:{NAVY};color:{YEL};"),
}
CAP_TOP = 1112
# Landscape (16:9 full screen): text column on the left (x 130-1010), hero on the right (centre x 1440).
LAND = False
HX = 1440


def Y(y):
    """Portrait y -> landscape y (text column moves up by 190 px)."""
    return y - 190 if LAND else y


def WH():
    return (1920, 1080) if LAND else (1080, 1920)


def norm(w):
    w = re.sub(r"[^a-z0-9]", "", w.lower())
    return "komen" + w[7:] if w.startswith("comment") else w


def fit(lines, width, mx, k=0.8):
    n = max(len(l) for l in lines)
    return int(min(mx, width / (k * max(n, 1))))


# ------------------------------------------------------------ captions
def align(text, vo):
    toks = re.findall(r"[^\s]+", text)
    disp = [re.sub(r"[.,;:]+$", "", t).upper() for t in toks]
    a = [norm(t) for t in toks]
    b = [norm(w) for w, _ in vo["words"]]
    times = [None] * len(toks)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for blk in sm.get_matching_blocks():
        for i in range(blk.size):
            times[blk.a + i] = vo["words"][blk.b + i][1]
    for tag, i1, i2, j1, j2 in sm.get_opcodes():  # replaced runs: map proportionally
        if tag == "replace":
            for k in range(i1, i2):
                jj = j1 + int((k - i1) * (j2 - j1) / max(1, i2 - i1))
                times[k] = vo["words"][min(jj, len(vo["words"]) - 1)][1]
    # fill gaps by interpolation
    known = [(i, t) for i, t in enumerate(times) if t is not None]
    if not known:
        known = [(0, 0.0)]
    for i in range(len(times)):
        if times[i] is None:
            prev = max([k for k in known if k[0] < i], default=(-1, 0.0), key=lambda k: k[0])
            nxt = min([k for k in known if k[0] > i], default=(len(times), vo["dur"]), key=lambda k: k[0])
            times[i] = prev[1] + (nxt[1] - prev[1]) * (i - prev[0]) / max(1, nxt[0] - prev[0])
    for i in range(1, len(times)):  # monotonic
        times[i] = max(times[i], times[i - 1] + 0.05)
    return list(zip(disp, times, toks))


def captions(sid, text, vo, lead, theme, end, box=None):
    th = THEME[theme]
    words = align(text, vo)
    chunks, cur = [], []
    for w in words:
        if cur and sum(len(x[0]) for x in cur) + len(w[0]) > 15:  # keep every chunk on one line
            chunks.append(cur); cur = []
        cur.append(w)
        if len(cur) == 3 or sum(len(x[0]) for x in cur) >= 12 or re.search(r"[.,?!]$", w[2]):
            chunks.append(cur); cur = []
    if cur:
        chunks.append(cur)
    html, js = [], []
    for c, ch in enumerate(chunks):
        t0 = lead + ch[0][1]
        t1 = lead + chunks[c + 1][0][1] if c + 1 < len(chunks) else end
        spans = " ".join(f'<span id="{sid}-w{c}_{j}" style="padding:2px 10px;border-radius:8px;">{escape(w[0])}</span>' for j, w in enumerate(ch))
        html.append(f'    <div id="{sid}-c{c}" class="cap" style="opacity:0;">{spans}</div>')
        js.append(f'tl.set("#{sid}-c{c}", {{ opacity: 1 }}, {t0:.2f}); tl.fromTo("#{sid}-c{c}", {{ scale: 0.9 }}, {{ scale: 1, duration: 0.12, ease: "power2.out", immediateRender: false }}, {t0:.2f}); tl.set("#{sid}-c{c}", {{ opacity: 0 }}, {t1:.2f});')
        for j, w in enumerate(ch):
            tw = lead + w[1]
            tn = lead + ch[j + 1][1] if j + 1 < len(ch) else t1
            hl = th["cap_hl"]
            bg = re.search(r"background:([^;]+)", hl).group(1); fg = re.search(r"color:([^;]+)", hl).group(1)
            js.append(f'tl.set("#{sid}-w{c}_{j}", {{ backgroundColor: "{bg}", color: "{fg}" }}, {tw:.2f}); tl.set("#{sid}-w{c}_{j}", {{ backgroundColor: "rgba(0,0,0,0)", color: "{th["text"]}" }}, {tn:.2f});')
    left, top, width, fs = box or ((130, 905, 880, 56) if LAND else (190, CAP_TOP, 590, 50))
    css = f"""    .cap {{ position: absolute; left: {left}px; top: {top}px; width: {width}px; text-align: {'left' if LAND and not box else 'center'}; font-weight: 900; font-size: {fs}px; line-height: 1.25;
      letter-spacing: 0.01em; color: {th['text']}; transform-origin: {'0%' if LAND and not box else '50%'} 50%; }}"""
    return css, "\n".join(html), "\n    ".join(js)


# ------------------------------------------------------------ pieces
def hero(sid, icon, theme, top, height, key="h"):
    """Character when the icon names a person/look, else the flat icon."""
    cv = character.from_icon(icon)
    if LAND:
        top, height, cx = 90, 990, HX
    else:
        cx = 500
    if cv:
        w = int(height * 600 / 760)
        svg = character.character(f"{sid}{key}", shirt=THEME[theme]["shirt"], **cv)
        return f'<div id="{sid}-{key}" class="hero" style="left:{cx - w // 2}px;top:{top}px;width:{w}px;height:{height}px;">{svg}</div>', True
    s = int(height * (0.62 if LAND else 0.8))
    return f'<div id="{sid}-{key}" class="hero ic" style="left:{cx - s // 2}px;top:{top + (height - s) // 2}px;width:{s}px;height:{s}px;">{icons.svg(icon, sid + key)}</div>', False


def title(sid, lines, top, size, theme, hl_last=True):
    th = THEME[theme]; out = []
    for j, l in enumerate(lines):
        y = Y(top) + j * size * 1.04
        extra = th["hl_css"] if (hl_last and j == len(lines) - 1) else ""
        out.append(f'    <div id="{sid}-t{j}" class="ttl" style="top:{y:.0f}px;font-size:{size}px;color:{th["text"]};{extra}">{escape(l)}</div>')
    return "\n".join(out), Y(top) + len(lines) * size * 1.04


def badge(sid, text, theme, top):
    fg = NAVY
    bg = YEL if theme != "yellow" else CREAM
    pos = f"left:130px;top:{top}px;max-width:860px;" if LAND else f"left:500px;top:{top}px;transform:translateX(-50%);max-width:560px;"
    return (f'    <div style="position:absolute;{pos}width:max-content;">'
            f'<div id="{sid}-bd" style="display:flex;align-items:center;gap:14px;padding:12px 26px 12px 14px;border-radius:40px;background:{bg};color:{fg};'
            f'font-weight:900;font-size:34px;line-height:1.15;box-shadow:0 6px 0 rgba(9,25,54,0.25);">'
            f'<svg width="46" height="46" viewBox="0 0 46 46" style="flex:none"><circle cx="23" cy="23" r="21" fill="{NAVY}"/>'
            f'<path d="M12 24 L20 32 L34 15" fill="none" stroke="{bg}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
            f'<span>{escape(text.upper())}</span></div></div>')


BASE_CSS = """    .ttl { position: absolute; left: 130px; font-weight: 900; line-height: 1; letter-spacing: -0.01em; white-space: nowrap; transform-origin: 0% 50%; }
    .hero { position: absolute; transform-origin: 50% 100%; }
    .hero svg, .ic svg { width: 100%; height: 100%; display: block; }
    .chip { position: absolute; left: 130px; top: CHIPTOPpx; padding: 9px 16px; font-weight: 900; font-size: 30px; letter-spacing: 0.08em; line-height: 1; }"""


def base_css():
    return BASE_CSS.replace("CHIPTOP", str(Y(300)))


def hero_js(sid, key="h", at=0.1, dur=3.0):
    return (f'tl.fromTo("#{sid}-{key}", {{ y: 80, scale: 0.92, opacity: 0 }}, {{ y: 0, scale: 1, opacity: 1, duration: 0.45, ease: "back.out(1.6)" }}, {at:.2f});\n    '
            f'tl.to("#{sid}-{key}", {{ scale: 1.025, duration: {max(0.6, dur):.2f}, ease: "sine.inOut" }}, {at + 0.45:.2f});')


def chip(sid, text, theme):
    bg, fg = (YEL, NAVY) if theme != "yellow" else (NAVY, YEL)
    return f'    <div id="{sid}-chip" class="chip" style="background:{bg};color:{fg};">{escape(text)}</div>'


# ------------------------------------------------------------ scenes
def s_hook(sid, sc, vo, lead, series, cue):
    theme = "navy"
    size = fit(sc["lines"], 860 if LAND else 700, 104 if LAND else 92)
    t_html, bottom = title(sid, sc["lines"], 360, size, theme, hl_last=False)
    t_html = re.sub(rf'(id="{sid}-t(\d+)" class="ttl" style="[^"]*?)color:{CREAM};', lambda m: m.group(1) + (f"color:{YEL};" if int(m.group(2)) in sc["hl"] else f"color:{CREAM};"), t_html)
    htop = int(bottom + 20); hh = 1080 - htop
    is_char = character.from_icon(sc["icon"]) is not None
    h_html, _ = hero(sid, sc["icon"] if is_char else "person", theme, htop, hh)
    if not is_char:
        fx, fy = (HX + 170, 120) if LAND else (610, htop + 20)
        h_html += (f'\n    <div id="{sid}-fi" class="ic" style="position:absolute;left:{fx}px;top:{fy}px;width:200px;height:200px;">'
                   f'{icons.svg(sc["icon"], sid + "fi")}</div>')
    html = chip(sid, series, theme) + "\n" + t_html + "\n    " + h_html
    js = "".join(f'tl.fromTo("#{sid}-t{j}", {{ scale: 1.08 }}, {{ scale: 1, duration: 0.3, ease: "power4.out" }}, {j * 0.05:.2f});\n    ' for j in range(len(sc["lines"])))
    js += (f'tl.fromTo("#{sid}-h", {{ scale: 0.94 }}, {{ scale: 1, duration: 0.5, ease: "back.out(1.6)" }}, 0);\n    '
           f'tl.to("#{sid}-h", {{ scale: 1.025, duration: {vo["dur"]:.2f}, ease: "sine.inOut" }}, 0.5);')
    if not is_char:
        js += f'\n    tl.fromTo("#{sid}-fi", {{ rotation: -14, scale: 0.8 }}, {{ rotation: 6, scale: 1, duration: 0.6, ease: "back.out(2)" }}, 0.05);'
    sfx = [("impact-bass-1", 0.0, 0.45)]
    return theme, base_css(), html, js, sfx


def s_point(sid, sc, vo, lead, theme, num, cue):
    size = fit(sc["title"], 860 if LAND else 700, 92 if LAND else 80)
    t_html, bottom = title(sid, sc["title"], 364, size, theme)
    htop = int(bottom + 10); hh = 1095 - htop
    h_html, _ = hero(sid, sc["icon"], theme, htop, hh)
    ts = lead + cue(vo, sc.get("cs"), 0.45)
    html = chip(sid, f"{num:02d}", theme) + "\n" + t_html + "\n    " + h_html + "\n" + badge(sid, sc["sub"], theme, int(bottom + 60) if LAND else 988)
    js = (f'tl.fromTo("#{sid}-chip", {{ scale: 0.4, opacity: 0, transformOrigin: "0% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.4)" }}, 0.2);\n    '
          + "".join(f'tl.fromTo("#{sid}-t{j}", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.3, ease: "power3.inOut" }}, {0.3 + j * 0.12:.2f});\n    ' for j in range(len(sc["title"])))
          + hero_js(sid, "h", 0.35, vo["dur"]) + "\n    "
          + f'tl.fromTo("#{sid}-bd", {{ scale: 0.5, opacity: 0, transformOrigin: "50% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.2)" }}, {ts:.2f});')
    return theme, base_css(), html, js, [("pop", 0.2, 1.2), ("click", ts, 1.1)]


def s_tip(sid, sc, vo, lead, theme, cue):
    size = fit(sc["title"], 860 if LAND else 700, 100 if LAND else 88)
    t_html, bottom = title(sid, sc["title"], 330, size, theme)
    htop = int(bottom + 20); hh = 1095 - htop
    h_html, _ = hero(sid, sc["icon"], theme, htop, hh)
    ts = lead + cue(vo, sc.get("cs"), 0.5)
    html = t_html + "\n    " + h_html + "\n" + badge(sid, sc["sub"], theme, int(bottom + 60) if LAND else 988)
    js = ("".join(f'tl.fromTo("#{sid}-t{j}", {{ scale: 1.25, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.25, ease: "power4.out" }}, {0.3 + j * 0.18:.2f});\n    ' for j in range(len(sc["title"])))
          + hero_js(sid, "h", 0.4, vo["dur"]) + "\n    "
          + f'tl.fromTo("#{sid}-bd", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.2)" }}, {ts:.2f});')
    return theme, base_css(), html, js, [("sparkle", 0.4, 0.35), ("click", ts, 1.1)]


def s_rows(sid, sc, vo, lead, theme, cue):
    """One character whose look changes on each row's cue, with a level meter."""
    n = len(sc["items"])
    th = THEME[theme]
    html = [f'    <div id="{sid}-head" style="position:absolute;left:130px;top:{Y(300)}px;font-weight:800;font-size:44px;line-height:1;color:{th["text"]};">{escape(sc["head"])}</div>']
    seg_w = int((650 - (n - 1) * 14) / n)
    base = Y(470) + 20 + (n - 1) * 14
    meter = []
    for j, r in enumerate(sc["items"]):
        x = 130 + j * (seg_w + 14)
        meter.append(f'<div id="{sid}-m{j}" style="position:absolute;left:{x}px;top:{Y(470)}px;width:{seg_w}px;height:{20 + j * 14}px;border-radius:8px;background:{th["text"]};opacity:0.18;transform-origin:50% 100%;"></div>'
                     f'<div style="position:absolute;left:{x}px;top:{base + 10}px;width:{seg_w}px;text-align:center;font-weight:800;font-size:28px;color:{th["text"]};">{escape(r["label"].split()[0])}</div>')
    meter = [m.replace(f'top:{Y(470)}px;width:{seg_w}px;height:{20 + j * 14}px', f'top:{base - (20 + j * 14)}px;width:{seg_w}px;height:{20 + j * 14}px') for j, m in enumerate(meter)]
    html.append("    " + "".join(meter))
    htop = base + 50; hh = 1070 - htop
    js, sfx = [f'tl.fromTo("#{sid}-head", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.35, ease: "power3.inOut" }}, 0.15);'], []
    times = []; prev = -1.0
    for j, r in enumerate(sc["items"]):
        raw = cue(vo, r["cue"], (j + 0.3) / n, prev); prev = raw
        t = lead + raw; times.append(t)
        size = fit([r["label"]], 520, 76)
        hh_html, _ = hero(sid, r["icon"], theme, htop, hh, key=f"h{j}")
        html.append(f'    <div id="{sid}-L{j}" style="position:absolute;left:130px;top:{Y(360)}px;font-weight:900;font-size:{size}px;line-height:1;white-space:nowrap;{th["hl_css"]}color:{NAVY if theme != "navy" else YEL};opacity:0;">{escape(r["label"])}</div>')
        html.append("    " + hh_html)
        html.append(badge(f"{sid}-{j}", r["desc"], theme, base + 90 if LAND else 988).replace(f'id="{sid}-{j}-bd"', f'id="{sid}-bd{j}"'))
    for j, t in enumerate(times):
        nxt = times[j + 1] if j + 1 < n else None
        js.append(f'tl.fromTo("#{sid}-L{j}", {{ opacity: 0, x: -30 }}, {{ opacity: 1, x: 0, duration: 0.25, ease: "power3.out" }}, {t:.2f});')
        js.append(f'tl.fromTo("#{sid}-h{j}", {{ opacity: 0, scale: 0.96 }}, {{ opacity: 1, scale: 1, duration: 0.3, ease: "power2.out" }}, {t:.2f});')
        js.append(f'tl.fromTo("#{sid}-m{j}", {{ opacity: 0.18, backgroundColor: "{th["text"]}" }}, {{ opacity: 1, backgroundColor: "{YEL}", duration: 0.2, ease: "none" }}, {t:.2f});')
        js.append(f'tl.fromTo("#{sid}-bd{j}", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.2)" }}, {t + 0.6:.2f});')
        if nxt is not None:
            js.append(f'tl.to(["#{sid}-L{j}", "#{sid}-bd{j}"], {{ opacity: 0, duration: 0.15, ease: "none" }}, {nxt - 0.05:.2f});')
            js.append(f'tl.to("#{sid}-h{j}", {{ opacity: 0, duration: 0.3, ease: "none" }}, {nxt:.2f});')
        sfx.append(("pop", t, 1.2))
    # hide all later characters at start
    init = "".join(f'tl.set("#{sid}-h{j}", {{ opacity: 0 }}, 0); tl.set("#{sid}-bd{j}", {{ opacity: 0 }}, 0); ' for j in range(n))
    return theme, base_css(), "\n".join(html), init + "\n    " + "\n    ".join(js), sfx


def s_compare(sid, sc, vo, lead, cue):
    theme = "navy"
    html, js, sfx = [], [], []
    cw = 440 if LAND else 315  # card width
    for j, (key, x) in enumerate([("L", 500), ("R", 980)] if LAND else [("L", 130), ("R", 465)]):
        sd = sc[key]
        t = lead + cue(vo, sd["cue"], 0.1 if j == 0 else 0.55)
        ls = fit([sd["label"]], 280, 44)
        items = []
        for m, (sign, text) in enumerate(sd["items"]):
            yy = 330 + m * 120
            col = {"+": (YEL, f'<path d="M14 27 L23 36 L39 18" fill="none" stroke="{NAVY}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'),
                   "-": (NAVY, f'<path d="M17 17 L35 35 M35 17 L17 35" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/>'),
                   "o": (NAVY, f'<circle cx="26" cy="26" r="7" fill="{CREAM}"/>')}[sign]
            badge_svg = f'<svg viewBox="0 0 52 52" width="52" height="52"><circle cx="26" cy="26" r="24" fill="{col[0]}"/>{col[1]}</svg>'
            items.append(f'<div id="{sid}-{key}i{m}" style="position:absolute;left:{30 if LAND else 18}px;top:{yy}px;width:{cw - 35}px;"><div style="position:absolute;left:0;top:0;">{badge_svg}</div>'
                         f'<div style="position:absolute;left:66px;top:4px;width:{cw - 103}px;font-weight:700;font-size:{34 if LAND else 30}px;line-height:1.18;color:{NAVY};">{escape(text)}</div></div>')
            js.append(f'tl.fromTo("#{sid}-{key}i{m}", {{ x: 30, opacity: 0 }}, {{ x: 0, opacity: 1, duration: 0.3, ease: "power3.out" }}, {t + 0.35 + m * 0.3:.2f});')
        html.append(f"""    <div id="{sid}-{key}" style="position:absolute;left:{x}px;top:{110 if LAND else 310}px;width:{cw}px;height:760px;border-radius:28px;background:{CREAM};--ink:{NAVY};--acc:{YEL};--paper:#ffffff;">
      <div style="position:absolute;left:0;top:28px;width:{cw}px;text-align:center;font-weight:900;font-size:{ls}px;line-height:1;color:{NAVY};">{escape(sd['label'])}</div>
      <div class="ic" style="position:absolute;left:{(cw - 200) // 2}px;top:92px;width:200px;height:200px;">{icons.svg(sd['icon'], f'{sid}{key}')}</div>
      {''.join(items)}
    </div>""")
        js.insert(0, f'tl.fromTo("#{sid}-{key}", {{ y: 120, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.4, ease: "power4.out" }}, {t:.2f});')
        sfx.append(("pop", t, 1.3))
    return theme, base_css(), "\n".join(html), "\n    ".join(js), sfx


def s_cta(sid, sc, vo, lead, cue):
    theme = "navy"
    ask = sc["ask"]
    size = fit(ask, 720, 76, 0.62)
    lines = "".join(f'<div style="color:{YEL if j == len(ask) - 1 else CREAM};">{escape(l)}</div>' for j, l in enumerate(ask))
    tk = lead + cue(vo, "komen", 0.35)
    wi = [i for i, (w, s) in enumerate(vo["words"]) if norm(w).startswith("komen")]
    tw = lead + vo["words"][wi[0] + 1][1] if wi and wi[0] + 1 < len(vo["words"]) else tk + 0.4
    word = sc["word"]; t_end = tw + 0.07 * len(word)
    html = f"""    <div id="{sid}-q" style="position:absolute;left:130px;top:{Y(330)}px;font-weight:900;font-size:{size}px;line-height:1.08;">{lines}</div>
    <div id="{sid}-box" style="position:absolute;left:130px;top:{Y(700)}px;width:650px;height:120px;border-radius:60px;background:{CREAM};">
      <div style="position:absolute;left:22px;top:22px;width:76px;height:76px;border-radius:38px;background:{YEL};"></div>
      <div id="{sid}-ph" style="position:absolute;left:124px;top:38px;color:rgba(9,25,54,0.45);font-weight:600;font-size:40px;line-height:1;">Tambah komen...</div>
      <div id="{sid}-typed" style="position:absolute;left:124px;top:34px;color:{NAVY};font-weight:900;font-size:48px;line-height:1;letter-spacing:0.04em;"></div>
      <div id="{sid}-send" style="position:absolute;right:16px;top:16px;width:88px;height:88px;border-radius:44px;background:rgba(9,25,54,0.14);"><svg style="position:absolute;left:22px;top:22px" width="44" height="44" viewBox="0 0 44 44"><path d="M6 22 L38 6 L28 38 L22 24 Z" fill="{NAVY}"/></svg></div>
    </div>
    <div id="{sid}-reply" style="position:absolute;left:230px;top:{Y(860)}px;padding:22px 30px;border-radius:34px 34px 34px 8px;background:{YEL};color:{NAVY};font-weight:900;font-size:44px;line-height:1;white-space:nowrap;">{escape(sc['reply'])}</div>"""
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
    if LAND:  # fill the right half with the happy customer
        h_html, _ = hero(sid, "confident", theme, 0, 0)
        html += "\n    " + h_html
        js += "\n    " + hero_js(sid, "h", 0.3, vo["dur"])
    return theme, base_css(), html, js, sfx


def scene_file(sid, theme, css, html, js, first, cap_css, cap_html, cap_js):
    th = THEME[theme]
    stripes = ""
    wipe = ""
    if not first:
        s2 = CREAM if theme != "cream" else NAVY
        sw = 3600 if LAND else 2400
        stripes = (f'    <div style="position:absolute;left:-660px;top:{-1200 if LAND else -240}px;width:{sw}px;height:{sw}px;transform:rotate(22deg);pointer-events:none;z-index:9;">'
                   f'<div id="{sid}-sa" style="position:absolute;left:-200px;top:0;width:170px;height:{sw}px;background:{YEL};"></div>'
                   f'<div id="{sid}-sb" style="position:absolute;left:-400px;top:0;width:120px;height:{sw}px;background:{s2};"></div></div>')
        wipe = (f'tl.fromTo("#root", {{ clipPath: "polygon(0% 0%, -30% 0%, -70% 100%, 0% 100%)" }}, {{ clipPath: "polygon(0% 0%, 150% 0%, 110% 100%, 0% 100%)", duration: 0.5, ease: "power2.inOut" }}, 0);\n    '
                f'tl.fromTo("#{sid}-sa", {{ x: 0 }}, {{ x: {sw + 300}, duration: 0.5, ease: "power2.inOut" }}, 0);\n    '
                f'tl.fromTo("#{sid}-sb", {{ x: 0 }}, {{ x: {sw + 300}, duration: 0.55, ease: "power2.inOut" }}, 0);\n    ')
    return f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; background: {th['bg']}; color: {th['text']}; font-family: "Montserrat", sans-serif; overflow: hidden; {th['vars']} }}
{css}
{cap_css}
  </style>
  <div id="root" data-composition-id="{sid}" data-width="{WH()[0]}" data-height="{WH()[1]}">
{html}
{cap_html}
{stripes}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    {wipe}{js}
    {cap_js}
    window.__timelines["{sid}"] = tl;
  </script>
</template>
"""
