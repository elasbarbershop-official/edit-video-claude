"""Business / story scenes for "Di Sebalik Kerusi Barber": stickman shop, revenue-vs-profit chart,
RM100 cost split, clipper-to-dashboard morph and the follow CTA. Works in 9:16 and 16:9 (style2.LAND).
Every scene returns (theme, css, html, js, sfx) like style2."""
from html import escape

import icons
import style2 as S2
from stickman import stickman, chair

NAVY, YEL, CREAM = S2.NAVY, S2.YEL, S2.CREAM
INK = {"navy": CREAM, "cream": NAVY, "yellow": NAVY}


def region(top_portrait):
    """Visual area: portrait = under the title in the safe column; landscape = right half."""
    if S2.LAND:
        return 1000, 150, 820, 760
    return 130, top_portrait, 750, 1060 - top_portrait


def box(id_, svg, x, y, w, h, extra=""):
    return f'<div id="{id_}" style="position:absolute;left:{x:.0f}px;top:{y:.0f}px;width:{w:.0f}px;height:{h:.0f}px;{extra}">{svg}</div>'


SVGFIT = "    #root .fit svg { width: 100%; height: 100%; display: block; }"


def colour_title(sid, lines, top, size, theme, hl):
    th = S2.THEME[theme]; out = []
    for j, l in enumerate(lines):
        y = S2.Y(top) + j * size * 1.04
        col = f"color:{YEL};" if (j in hl and theme == "navy") else (th["hl_css"] if j in hl else f"color:{th['text']};")
        out.append(f'    <div id="{sid}-t{j}" class="ttl" style="top:{y:.0f}px;font-size:{size}px;{col}">{escape(l)}</div>')
    return "\n".join(out), S2.Y(top) + len(lines) * size * 1.04


def title_in(sid, n, at=0.25, step=0.12):
    return "".join(f'tl.fromTo("#{sid}-t{j}", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.32, ease: "power3.inOut" }}, {at + j * step:.2f});\n    ' for j in range(n))


def wallet_svg():
    return (f'<svg viewBox="0 0 220 170" xmlns="http://www.w3.org/2000/svg" overflow="visible">'
            f'<rect x="10" y="40" width="200" height="120" rx="18" fill="{YEL}" stroke="{NAVY}" stroke-width="8"/>'
            f'<path d="M10 70 L210 70" stroke="{NAVY}" stroke-width="8"/>'
            f'<rect x="150" y="88" width="60" height="44" rx="10" fill="{CREAM}" stroke="{NAVY}" stroke-width="8"/><circle cx="170" cy="110" r="7" fill="{NAVY}"/>'
            f'<path d="M40 40 Q40 10 70 14 L150 30" stroke="{NAVY}" stroke-width="8" fill="none" stroke-linecap="round"/>'
            f'<text x="34" y="132" font-family="Montserrat" font-weight="900" font-size="38" fill="{NAVY}">RM0</text></svg>')


def dashboard_svg(sid):
    bars = "".join(f'<rect id="{sid}-db{i}" x="{40 + i * 34}" y="{170 - h}" width="22" height="{h}" rx="4" fill="{YEL}"/>' for i, h in enumerate((40, 62, 54, 86, 108)))
    return (f'<svg viewBox="0 0 320 230" xmlns="http://www.w3.org/2000/svg" overflow="visible">'
            f'<rect x="6" y="6" width="308" height="218" rx="22" fill="{NAVY}"/>'
            f'<rect x="26" y="24" width="120" height="12" rx="6" fill="{CREAM}" opacity="0.8"/>{bars}'
            f'<path d="M30 180 L210 180" stroke="{CREAM}" stroke-width="4" opacity="0.5"/>'
            f'<circle cx="262" cy="92" r="38" fill="{CREAM}"/><path d="M262 92 L262 54 A38 38 0 0 1 297 106 Z" fill="{YEL}"/>'
            f'<path id="{sid}-dl" d="M226 190 L250 168 L270 176 L298 142" stroke="{YEL}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')


# ------------------------------------------------------------------ scenes
def s_shop(sid, sc, vo, lead, series, cue):
    theme = "navy"
    size = S2.fit(sc["lines"], 860 if S2.LAND else 750, 100 if S2.LAND else 96)
    t_html, bottom = colour_title(sid, sc["lines"], 360, size, theme, sc["hl"])
    rx, ry, rw, rh = region(int(bottom) + 50)
    k = rw / 820
    st_w, st_h = 170 * k, 255 * k
    floor_y = ry + (330 if not S2.LAND else 520) * (k if not S2.LAND else 1)
    stations = []
    for i in range(3):
        x0 = rx + i * 275 * k
        stations.append(box(f"{sid}-ch{i}", chair(INK[theme], YEL), x0 + 95 * k, floor_y - st_h, st_w, st_h, "")
                        + box(f"{sid}-cu{i}", stickman("sit", "#8fa0c2", YEL, cape=True), x0 + 95 * k, floor_y - st_h - 6 * k, st_w, st_h)
                        + box(f"{sid}-ba{i}", stickman("barber", CREAM, YEL, prop="clipper"), x0 - 5 * k, floor_y - st_h, st_w, st_h))
    shop = (f'<div id="{sid}-shop" style="position:absolute;left:0;top:0;width:100%;height:100%;transform-origin:{rx + rw / 2:.0f}px {floor_y - st_h / 2:.0f}px;">'
            + "".join(stations)
            + f'<div style="position:absolute;left:{rx - 20:.0f}px;top:{floor_y:.0f}px;width:{rw + 40:.0f}px;height:8px;border-radius:4px;background:{CREAM};opacity:0.35;"></div>'
            + f'<div id="{sid}-full" style="position:absolute;left:{rx:.0f}px;top:{floor_y + 34:.0f}px;padding:12px 22px;border-radius:30px;background:{YEL};color:{NAVY};font-weight:900;font-size:34px;line-height:1;">PELANGGAN HARI INI: <span id="{sid}-n">0</span></div>'
            + "</div>")
    ow, oh = 300 * (1 if S2.LAND else 0.9), 450 * (1 if S2.LAND else 0.9)
    oy = ry + (40 if S2.LAND else 10)
    owner = box(f"{sid}-own", stickman("worried", CREAM, YEL, prop="sweat"), rx + (60 if S2.LAND else 20), oy, ow, oh, "opacity:0;transform-origin:50% 100%;")
    wal = box(f"{sid}-wal", wallet_svg(), rx + (420 if S2.LAND else 380), oy + oh * 0.45, 300, 232, "opacity:0;transform-origin:50% 50%;")
    html = S2.chip(sid, series, theme) + "\n" + t_html + "\n    " + shop + "\n    " + owner + "\n    " + wal
    t_full = lead + cue(vo, "penuh", 0.35)
    t_shut = lead + cue(vo, "tutup", 0.8)
    js = (title_in(sid, len(sc["lines"]), 0.05, 0.08)
          + "".join(f'tl.fromTo("#{sid}-ba{i}", {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {0.25 + i * 0.12:.2f});\n    '
                    f'tl.fromTo(["#{sid}-cu{i}", "#{sid}-ch{i}"], {{ y: 40, opacity: 0 }}, {{ y: 0, opacity: 1, duration: 0.35, ease: "back.out(1.8)" }}, {0.32 + i * 0.12:.2f});\n    '
                    f'tl.fromTo("#{sid}-ba{i}", {{ rotation: -3 }}, {{ rotation: 3, duration: 0.4, ease: "sine.inOut", repeat: {int((t_shut - 0.5) / 0.4)}, yoyo: true, transformOrigin: "50% 100%" }}, 0.6);\n    '
                    for i in range(3))
          + f'tl.fromTo("#{sid}-full", {{ scale: 0.5, opacity: 0, transformOrigin: "0% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2)" }}, {t_full:.2f});\n    '
          + f'const cnt{sid} = {{ v: 0 }}; tl.fromTo(cnt{sid}, {{ v: 0 }}, {{ v: 36, duration: 1.4, ease: "power2.out", immediateRender: false, onUpdate: () => {{ document.querySelector("#{sid}-n").textContent = Math.round(cnt{sid}.v); }} }}, {t_full:.2f});\n    '
          + f'tl.set("#{sid}-n", {{ textContent: "0" }}, 0);\n    '
          # dramatic camera push into the shop, then it dims and the worried owner + empty wallet take over
          + f'tl.to("#{sid}-shop", {{ scale: 1.5, opacity: 0.12, duration: 0.6, ease: "power3.in" }}, {t_shut - 0.35:.2f});\n    '
          + f'tl.fromTo("#{sid}-own", {{ opacity: 0, y: 60, scale: 0.9 }}, {{ opacity: 1, y: 0, scale: 1, duration: 0.4, ease: "back.out(1.6)" }}, {t_shut + 0.1:.2f});\n    '
          + f'tl.fromTo("#{sid}-own", {{ x: -4 }}, {{ x: 4, duration: 0.08, repeat: 7, yoyo: true, ease: "none", immediateRender: false }}, {t_shut + 0.5:.2f});\n    '
          + f'tl.fromTo("#{sid}-wal", {{ opacity: 0, scale: 0.4, rotation: -12 }}, {{ opacity: 1, scale: 1, rotation: 0, duration: 0.4, ease: "back.out(2.2)" }}, {t_shut + 0.35:.2f});')
    sfx = [("impact-bass-1", 0.0, 0.45), ("pop", t_full, 1.2), ("whoosh-cinematic", max(0, t_shut - 0.6), 0.5, 1.2, 1.8), ("impact-bass-1", t_shut + 0.1, 0.5)]
    return theme, S2.base_css() + "\n" + SVGFIT, html, js, sfx


def s_chart(sid, sc, vo, lead, theme, cue):
    size = S2.fit(sc["title"], 860 if S2.LAND else 750, 96 if S2.LAND else 88)
    t_html, bottom = colour_title(sid, sc["title"], 340, size, theme, [len(sc["title"]) - 1])
    rx, ry, rw, rh = region(int(bottom) + 60)
    ch = min(rh - 20, 520 if S2.LAND else 440)
    cw = (rw - 60) / 2
    ink = INK[theme]
    t1 = lead + cue(vo, "jualan", 0.2)
    t2 = lead + cue(vo, "keuntungan", 0.4)
    t3 = lead + cue(vo, "berbeza", 0.8)
    parts, js = [], []
    for side, (label, arrow, hs, fill, t) in enumerate([("JUALAN", "▲", (30, 45, 62, 80, 100), ink, t1),
                                                         ("UNTUNG", "▼", (100, 78, 55, 36, 18), YEL, t2)]):
        x0 = rx + side * (cw + 60)
        bw = (cw - 40) / 5 - 14
        bars = "".join(f'<div id="{sid}-b{side}{i}" style="position:absolute;left:{20 + i * (bw + 14):.0f}px;bottom:70px;width:{bw:.0f}px;height:{(ch - 170) * h / 100:.0f}px;border-radius:10px 10px 0 0;background:{fill};{"border:6px solid " + NAVY + ";box-sizing:border-box;" if fill == YEL else ""}transform-origin:50% 100%;"></div>' for i, h in enumerate(hs))
        parts.append(f'<div id="{sid}-k{side}" style="position:absolute;left:{x0:.0f}px;top:{ry:.0f}px;width:{cw:.0f}px;height:{ch:.0f}px;border-radius:26px;background:{"rgba(9,25,54,0.06)" if theme != "navy" else "rgba(250,248,242,0.08)"};">'
                     f'<div style="position:absolute;left:20px;top:22px;font-weight:900;font-size:{44 if not S2.LAND else 48}px;line-height:1;color:{ink};">{label} <span style="color:{YEL if theme == "navy" else NAVY};">{arrow}</span></div>'
                     f'{bars}<div style="position:absolute;left:16px;right:16px;bottom:62px;height:6px;border-radius:3px;background:{ink};opacity:0.5;"></div></div>')
        js.append(f'tl.fromTo("#{sid}-k{side}", {{ opacity: 0, y: 50 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power3.out" }}, {t - 0.15:.2f});')
        js.append(f'tl.fromTo({[f"#{sid}-b{side}{i}" for i in range(5)]}, {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.45, ease: "back.out(1.4)", stagger: 0.09 }}, {t + 0.1:.2f});')
    ne = f'<div id="{sid}-ne" style="position:absolute;left:{rx + rw / 2 - 60:.0f}px;top:{ry + ch / 2 - 70:.0f}px;width:120px;height:120px;border-radius:60px;background:{YEL if theme != "yellow" else NAVY};color:{NAVY if theme != "yellow" else YEL};font-weight:900;font-size:84px;line-height:116px;text-align:center;box-shadow:0 8px 0 rgba(9,25,54,0.25);">≠</div>'
    js.append(f'tl.fromTo("#{sid}-ne", {{ scale: 0, rotation: -40 }}, {{ scale: 1, rotation: 0, duration: 0.35, ease: "back.out(2.5)" }}, {t3:.2f});')
    html = t_html + "\n    " + "".join(parts) + "\n    " + ne
    if S2.LAND:  # the owner watches the charts from the left column
        pass
    js_all = title_in(sid, len(sc["title"])) + "\n    ".join(js)
    sfx = [("pop", t1, 1.2), ("pop", t2, 1.2), ("click", t3, 1.3)]
    return theme, S2.base_css() + "\n" + SVGFIT, html, js_all, sfx


def s_split(sid, sc, vo, lead, theme, cue):
    th = S2.THEME[theme]; ink = th["text"]
    size = S2.fit(sc["title"], 860 if S2.LAND else 750, 88 if S2.LAND else 80)
    t_html, bottom = colour_title(sid, sc["title"], 330, size, theme, [len(sc["title"]) - 1])
    x, w = 130, (860 if S2.LAND else 750)
    y_cnt = bottom + 24
    y_bar = y_cnt + 170
    y_rows = y_bar + 120
    base_rm = sc.get("base", 100)
    seg, rows, js, sfx = [], [], [], []
    off = 0; prev = -1.0; remain = base_rm
    js.append(f'const rm{sid} = {{ v: {base_rm} }}; const rmEl{sid} = document.querySelector("#{sid}-rm");')
    js.append(f'tl.set("#{sid}-rm", {{ textContent: "RM{base_rm}" }}, 0);')
    for i, (label, amt) in enumerate(sc["costs"]):
        raw = cue(vo, label.split()[0], (i + 1) / (len(sc["costs"]) + 2), prev); prev = raw
        t = lead + raw
        sw = w * amt / base_rm
        shade = ["#ffffff", "#e9e6dc", "#ffffff", "#e9e6dc", "#ffffff", "#e9e6dc"][i % 6] if theme == "navy" else [NAVY, "#24365e"][i % 2]
        tc = NAVY if theme == "navy" else CREAM
        seg.append(f'<div id="{sid}-s{i}" style="position:absolute;left:{x + off:.0f}px;top:{y_bar:.0f}px;width:{sw:.0f}px;height:88px;background:{shade};border-right:4px solid {th["bg"]};box-sizing:border-box;'
                   f'color:{tc};font-weight:900;font-size:24px;line-height:88px;text-align:center;overflow:hidden;white-space:nowrap;">{amt}</div>')
        col, rr = i % 2, i // 2
        rows.append(f'<div id="{sid}-r{i}" style="position:absolute;left:{x + col * (w / 2):.0f}px;top:{y_rows + rr * 66:.0f}px;width:{w / 2 - 20:.0f}px;font-weight:800;font-size:{36 if S2.LAND else 30}px;line-height:1.2;color:{ink};white-space:nowrap;">'
                    f'<span style="display:inline-block;width:18px;height:18px;border-radius:9px;background:{YEL};margin-right:12px;vertical-align:4px;"></span>{escape(label)} <b style="color:{YEL if theme == "navy" else NAVY};">RM{amt}</b></div>')
        js.append(f'tl.fromTo("#{sid}-s{i}", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.3, ease: "power3.out" }}, {t:.2f});')
        js.append(f'tl.fromTo("#{sid}-r{i}", {{ opacity: 0, x: -24 }}, {{ opacity: 1, x: 0, duration: 0.25, ease: "power3.out" }}, {t:.2f});')
        js.append(f'tl.fromTo(rm{sid}, {{ v: {remain} }}, {{ v: {remain - amt}, duration: 0.35, ease: "power2.out", immediateRender: false, onUpdate: () => {{ rmEl{sid}.textContent = "RM" + Math.round(rm{sid}.v); }} }}, {t:.2f});')
        sfx.append(("click", t, 1.1))
        off += sw; remain -= amt
    t_end = lead + cue(vo, "keuntungan", 0.9, prev)
    base = f'<div id="{sid}-base" style="position:absolute;left:{x}px;top:{y_bar:.0f}px;width:{w}px;height:88px;border-radius:14px;background:{YEL};overflow:hidden;"></div>'
    keep = (f'<div id="{sid}-keep" style="position:absolute;left:{x + w - 150:.0f}px;top:{y_bar - 64:.0f}px;padding:8px 14px;border-radius:12px;background:{YEL};color:{NAVY};font-weight:900;font-size:28px;line-height:1;white-space:nowrap;">UNTUNG</div>')
    cnt = (f'<div style="position:absolute;left:{x}px;top:{y_cnt:.0f}px;width:{w}px;font-weight:700;font-size:{30 if S2.LAND else 26}px;line-height:1.1;color:{ink};opacity:0.8;">{escape(sc.get("lead_text", "Daripada setiap RM100 jualan, baki untuk anda:"))}</div>'
           f'<div id="{sid}-rm" style="position:absolute;left:{x}px;top:{y_cnt + 40:.0f}px;font-weight:900;font-size:110px;line-height:1;color:{YEL if theme == "navy" else NAVY};">RM{base_rm}</div>')
    note = f'<div style="position:absolute;left:{x}px;top:{y_rows + 3 * 66 + 6:.0f}px;width:{w}px;font-weight:600;font-size:24px;line-height:1.2;color:{ink};opacity:0.7;">*Contoh ilustrasi sahaja, bukan angka sebenar Ela&#39;s Barbershop.</div>'
    js.append(f'tl.fromTo("#{sid}-keep", {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "back.out(2)" }}, {t_end:.2f});')
    js.append(f'tl.fromTo("#{sid}-rm", {{ scale: 1 }}, {{ scale: 1.12, duration: 0.18, ease: "power2.out", yoyo: true, repeat: 1, transformOrigin: "0% 50%", immediateRender: false }}, {t_end:.2f});')
    sfx.append(("pop", t_end, 1.3))
    html = t_html + "\n    " + cnt + base + "".join(seg) + keep + "".join(rows) + note
    if S2.LAND:
        html += "\n    " + box(f"{sid}-own", stickman("worried", CREAM if theme == "navy" else NAVY, YEL, prop="sweat"), 1290, 220, 420, 630, "")
        js.append(f'tl.fromTo("#{sid}-own", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "back.out(1.6)" }}, 0.3);')
    return theme, S2.base_css() + "\n" + SVGFIT, html, title_in(sid, len(sc["title"])) + "\n    ".join(js), sfx


def s_morph(sid, sc, vo, lead, cue):
    theme = "yellow"
    size = S2.fit(sc["title"], 860 if S2.LAND else 750, 96 if S2.LAND else 88)
    t_html, bottom = colour_title(sid, sc["title"], 330, size, theme, [len(sc["title"]) - 1])
    rx, ry, rw, rh = region(int(bottom) + 40)
    rh = min(rh, 700) if S2.LAND else min(rh, 1010 - ry - 80)
    cx, cy = rx + rw / 2, ry + rh / 2
    ic = rh * 0.75
    clip = box(f"{sid}-clip", icons.svg("clipper", sid + "cl"), cx - ic / 2, cy - ic / 2, ic, ic, f"--ink:{NAVY};--acc:{CREAM};--paper:#ffffff;")
    dw = min(rw * 0.62, rh * 1.0); dh = dw * 230 / 320
    dash = box(f"{sid}-dash", dashboard_svg(sid), cx - dw * 0.62, cy - dh / 2 - rh * 0.08, dw, dh, "opacity:0;")
    mw, mh = rh * 0.42, rh * 0.63
    man = box(f"{sid}-man", stickman("point", NAVY, CREAM, tie=True), cx + dw * 0.32, cy - mh / 2 + rh * 0.12, mw, mh, "opacity:0;")
    wk = "".join(box(f"{sid}-w{i}", stickman("stand", NAVY, CREAM), cx - dw * 0.62 + i * mw * 0.55, (min(cy + dh / 2 - rh * 0.02, 965 - mh * 0.5) if not S2.LAND else cy + dh / 2 - rh * 0.02), mw * 0.5, mh * 0.5, "opacity:0;") for i in range(3))
    t_cut = lead + cue(vo, "pandai", 0.35)
    t_biz = lead + cue(vo, "menguruskan", 0.7)
    t_sub = lead + cue(vo, "perniagaan", 0.85)
    badge_top = int(bottom + 60) if S2.LAND else 988
    html = t_html + "\n    " + clip + dash + man + wk + "\n" + S2.badge(sid, sc["sub"], theme, badge_top)
    js = (title_in(sid, len(sc["title"]))
          + f'tl.fromTo("#{sid}-clip", {{ scale: 0.6, opacity: 0, rotation: -20 }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.45, ease: "back.out(1.8)" }}, 0.3);\n    '
          + f'tl.fromTo("#{sid}-clip", {{ y: 0 }}, {{ y: -14, duration: 0.25, ease: "sine.inOut", yoyo: true, repeat: 3, immediateRender: false }}, {t_cut:.2f});\n    '
          + f'tl.to("#{sid}-clip", {{ scale: 0.2, rotation: 200, opacity: 0, duration: 0.4, ease: "power3.in" }}, {t_biz - 0.2:.2f});\n    '
          + f'tl.fromTo("#{sid}-dash", {{ scale: 0.3, opacity: 0, rotation: 12 }}, {{ scale: 1, opacity: 1, rotation: 0, duration: 0.45, ease: "back.out(1.6)" }}, {t_biz + 0.1:.2f});\n    '
          + f'tl.fromTo({[f"#{sid}-db{i}" for i in range(5)]}, {{ scaleY: 0, transformOrigin: "50% 100%" }}, {{ scaleY: 1, duration: 0.4, ease: "back.out(1.5)", stagger: 0.07 }}, {t_biz + 0.35:.2f});\n    '
          + f'tl.fromTo("#{sid}-dl", {{ strokeDasharray: 120, strokeDashoffset: 120 }}, {{ strokeDashoffset: 0, duration: 0.5, ease: "power2.out" }}, {t_biz + 0.6:.2f});\n    '
          + f'tl.fromTo("#{sid}-man", {{ opacity: 0, x: 40 }}, {{ opacity: 1, x: 0, duration: 0.35, ease: "power3.out" }}, {t_biz + 0.45:.2f});\n    '
          + f'tl.fromTo({[f"#{sid}-w{i}" for i in range(3)]}, {{ opacity: 0, y: 30 }}, {{ opacity: 1, y: 0, duration: 0.3, ease: "back.out(2)", stagger: 0.1 }}, {t_biz + 0.7:.2f});\n    '
          + f'tl.fromTo("#{sid}-bd", {{ scale: 0.5, opacity: 0 }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.2)" }}, {t_sub:.2f});')
    sfx = [("whoosh", t_biz - 0.25, 0.8, 0.57), ("sparkle", t_biz + 0.1, 0.4), ("click", t_sub, 1.1)]
    return theme, S2.base_css() + "\n" + SVGFIT, html, js, sfx


def s_follow(sid, sc, vo, lead, series, handle, tagline, cue):
    theme = "navy"
    ask = sc["ask"]
    size = S2.fit(ask, 860 if S2.LAND else 750, 92 if S2.LAND else 84, 0.62)
    lines = "".join(f'<div style="color:{YEL if j == len(ask) - 1 else CREAM};">{escape(l)}</div>' for j, l in enumerate(ask))
    y_q = S2.Y(360)
    y_card = y_q + len(ask) * size * 1.08 + 50
    t_f = lead + cue(vo, "ikuti", 0.3)
    html = (S2.chip(sid, series, theme)
            + f'\n    <div id="{sid}-q" style="position:absolute;left:130px;top:{y_q:.0f}px;font-weight:900;font-size:{size}px;line-height:1.08;">{lines}</div>'
            + f'\n    <div id="{sid}-card" style="position:absolute;left:130px;top:{y_card:.0f}px;width:{750 if not S2.LAND else 860}px;height:190px;border-radius:30px;background:{CREAM};">'
            + f'<div style="position:absolute;left:20px;top:40px;width:190px;height:110px;border-radius:20px;background:{NAVY};"><img src="assets/img/elas-logo.png" alt="" style="position:absolute;left:14px;top:10px;width:162px;height:90px;object-fit:contain;"/></div>'
            + f'<div style="position:absolute;left:232px;top:30px;color:{NAVY};font-weight:900;font-size:{30 if not S2.LAND else 34}px;line-height:1;white-space:nowrap;">{escape(handle)}</div>'
            + f'<div style="position:absolute;left:232px;top:72px;color:rgba(9,25,54,0.65);font-weight:700;font-size:24px;line-height:1;white-space:nowrap;">{escape(sc.get("cardsub", "Ilmu barber setiap hari"))}</div>'
            + f'<div id="{sid}-btn" style="position:absolute;left:232px;top:112px;width:200px;height:58px;border-radius:29px;background:{YEL};color:{NAVY};font-weight:900;font-size:26px;line-height:58px;text-align:center;">'
            + f'<span id="{sid}-b1">IKUTI</span><span id="{sid}-b2" style="position:absolute;left:0;right:0;top:0;opacity:0;">✓ DIIKUTI</span></div></div>'
            + f'\n    <div id="{sid}-tag" style="position:absolute;left:130px;top:{y_card + 240:.0f}px;width:{750 if not S2.LAND else 860}px;color:{CREAM};font-weight:800;font-style:italic;font-size:40px;line-height:1.2;">{escape(tagline)}</div>')
    js = (f'tl.fromTo("#{sid}-chip", {{ scale: 0.4, opacity: 0, transformOrigin: "0% 50%" }}, {{ scale: 1, opacity: 1, duration: 0.3, ease: "back.out(2.4)" }}, 0.15);\n    '
          f'tl.fromTo("#{sid}-q", {{ clipPath: "inset(0% 100% 0% 0%)" }}, {{ clipPath: "inset(0% 0% 0% 0%)", duration: 0.4, ease: "power3.inOut" }}, 0.25);\n    '
          f'tl.fromTo("#{sid}-card", {{ opacity: 0, y: 40 }}, {{ opacity: 1, y: 0, duration: 0.35, ease: "power4.out" }}, {max(0.5, t_f - 0.5):.2f});\n    '
          f'tl.fromTo("#{sid}-btn", {{ scale: 1 }}, {{ scale: 0.86, duration: 0.08, ease: "power2.in", yoyo: true, repeat: 1, immediateRender: false }}, {t_f + 0.3:.2f});\n    '
          f'tl.to("#{sid}-btn", {{ backgroundColor: "{NAVY}", color: "{CREAM}", duration: 0.12, ease: "none" }}, {t_f + 0.38:.2f});\n    '
          f'tl.set("#{sid}-b1", {{ opacity: 0 }}, {t_f + 0.38:.2f}); tl.set("#{sid}-b2", {{ opacity: 1 }}, {t_f + 0.38:.2f});\n    '
          f'tl.fromTo("#{sid}-tag", {{ opacity: 0, y: 20 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }}, {t_f + 0.9:.2f});')
    sfx = [("click", t_f + 0.3, 1.3), ("sparkle", t_f + 0.9, 0.35)]
    if S2.LAND:
        html += "\n    " + box(f"{sid}-hap", stickman("happy", CREAM, YEL), 1340, 190, 440, 660, "")
        js += f'\n    tl.fromTo("#{sid}-hap", {{ opacity: 0, y: 60 }}, {{ opacity: 1, y: 0, duration: 0.45, ease: "back.out(1.6)" }}, 0.35);'
    return theme, S2.base_css() + "\n" + SVGFIT, html, js, sfx
