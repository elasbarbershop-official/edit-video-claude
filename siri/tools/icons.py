"""Elas brand icon set: flat line icons, viewBox 0 0 200 200.
Colours come from CSS variables on the parent: --ink (lines), --acc (yellow accent), --paper (fills)."""

S = 'fill="none" stroke="var(--ink)" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"'
SI = 'stroke="var(--ink)" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"'
A = 'fill="var(--acc)"'
P = 'fill="var(--paper)"'
INK = 'fill="var(--ink)"'


def face(shape, beard=False):
    shapes = {
        "oval": "M100 30 C145 30 158 70 156 105 C154 145 130 172 100 172 C70 172 46 145 44 105 C42 70 55 30 100 30 Z",
        "round": "M100 32 C148 32 160 68 160 100 C160 140 135 170 100 170 C65 170 40 140 40 100 C40 68 52 32 100 32 Z",
        "square": "M52 40 L148 40 Q156 40 156 50 L156 140 Q156 168 128 168 L72 168 Q44 168 44 140 L44 50 Q44 40 52 40 Z",
        "heart": "M46 52 Q48 32 100 32 Q152 32 154 52 Q158 98 128 142 Q112 168 100 170 Q88 168 72 142 Q42 98 46 52 Z",
        "long": "M100 18 C138 18 146 52 146 96 C146 150 128 182 100 182 C72 182 54 150 54 96 C54 52 62 18 100 18 Z",
    }
    d = shapes[shape]
    out = f'<path d="{d}" {P} {SI}/>'
    out += f'<circle cx="80" cy="96" r="6" {INK}/><circle cx="120" cy="96" r="6" {INK}/>'
    if beard:
        bd = {
            "round": "M62 118 Q70 150 100 176 Q130 150 138 118 Q120 138 100 138 Q80 138 62 118 Z",
            "square": "M48 112 Q50 166 100 170 Q150 166 152 112 Q128 140 100 140 Q72 140 48 112 Z",
            "long": "M58 110 Q60 150 100 160 Q140 150 142 110 Q122 132 100 132 Q78 132 58 110 Z",
            "heart": "M74 120 Q80 168 100 178 Q120 168 126 120 Q112 136 100 136 Q88 136 74 120 Z",
            "oval": "M52 116 Q58 166 100 174 Q142 166 148 116 Q124 140 100 140 Q76 140 52 116 Z",
        }[shape]
        out += f'<path d="{bd}" {INK}/>'
        out += f'<path d="M84 124 Q100 116 116 124" fill="none" stroke="var(--paper)" stroke-width="7" stroke-linecap="round"/>'
    else:
        out += f'<path d="M84 132 Q100 142 116 132" {S}/>'
    return out


def head(hair):
    # front view head with a hairstyle shape on top
    base = (f'<ellipse cx="40" cy="108" rx="10" ry="16" {P} {SI}/><ellipse cx="160" cy="108" rx="10" ry="16" {P} {SI}/>'
            f'<path d="M100 44 C140 44 152 76 150 108 C148 146 128 172 100 172 C72 172 52 146 50 108 C48 76 60 44 100 44 Z" {P} {SI}/>'
            f'<circle cx="82" cy="110" r="5" {INK}/><circle cx="118" cy="110" r="5" {INK}/><path d="M88 140 Q100 148 112 140" {S}/>')
    hairs = {
        "crop": "M50 92 Q48 40 100 34 Q152 40 150 92 Q140 80 128 82 L120 70 L110 82 L98 70 L88 84 L76 74 L66 86 Q56 84 50 92 Z",
        "quiff": "M50 94 Q46 50 84 36 Q120 10 156 34 Q170 50 150 70 Q150 82 150 94 Q138 70 100 74 Q66 74 50 94 Z",
        "sidepart": "M50 98 Q46 42 100 36 Q154 40 150 98 Q146 76 132 70 L76 72 Q60 76 50 98 Z M76 72 L74 44",
        "crew": "M52 90 Q52 46 100 42 Q148 46 148 90 Q130 76 100 76 Q70 76 52 90 Z",
        "fringe": "M48 104 Q42 44 100 34 Q158 44 152 104 Q144 88 136 96 L126 84 L114 98 L102 84 L90 98 L78 86 L66 98 Q58 92 48 104 Z",
        "long": "M44 140 Q30 40 100 32 Q170 40 156 140 Q150 110 148 92 Q130 70 100 72 Q70 70 52 92 Q50 110 44 140 Z",
        "thin": None,
    }
    h = hairs[hair]
    if hair == "thin":
        strands = "".join(f'<path d="M{x} 60 Q{x+4} 40 {x+8} 34" {S}/>' for x in range(62, 140, 13))
        return base + strands
    parts = h.split(" M")
    out = base + f'<path d="{parts[0]}" {INK}/>'
    if len(parts) > 1:
        out += f'<path d="M{parts[1]}" fill="none" stroke="var(--paper)" stroke-width="6" stroke-linecap="round"/>'
    return out


def fade(level, uid):
    # side profile facing right: dark hair on top/back down to the fade line, then a soft fade to skin
    y = {"low": 128, "mid": 108, "high": 84}[level]
    g = f"fg-{uid}"
    clip = f"hc-{uid}"
    head_d = "M78 188 L80 162 Q50 146 46 108 Q42 50 92 30 Q140 16 160 56 Q166 74 164 92 L178 116 Q180 122 168 124 L168 136 Q170 142 164 144 L164 152 Q164 166 144 168 L120 168 L118 188 Z"
    return (f'<defs><linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="var(--ink)"/><stop offset="1" stop-color="var(--ink)" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="{clip}"><path d="{head_d}"/></clipPath></defs>'
            f'<path d="{head_d}" {P}/>'
            f'<g clip-path="url(#{clip})">'
            f'<path d="M20 {y} L20 0 L180 0 L180 50 Q150 40 140 54 Q124 64 118 {y - 4} Z" {INK}/>'
            f'<path d="M20 {y} L118 {y - 4} L118 {y + 46} L20 {y + 50} Z" fill="url(#{g})"/></g>'
            f'<path d="{head_d}" fill="none" {SI}/>'
            f'<path d="M84 110 Q74 112 74 124 Q74 138 86 140" fill="none" {SI}/>'
            f'<path d="M30 {y} L120 {y - 4}" stroke="var(--acc)" stroke-width="7" stroke-dasharray="12 9" stroke-linecap="round"/>')


ICONS = {
    "shower": f'<path d="M50 170 L50 60 Q50 30 82 30 L120 30" {S}/><path d="M100 52 Q120 30 150 52 Z" {A} {SI}/><path d="M104 52 L146 52" {S}/>'
              + "".join(f'<path d="M{x} 74 L{x-6} {94+i*6}" stroke="var(--acc)" stroke-width="8" stroke-linecap="round"/>' for i, x in enumerate([110, 125, 140]))
              + f'<circle cx="112" cy="128" r="6" {A}/><circle cx="132" cy="140" r="6" {A}/>',
    "steam": f'<path d="M100 172 C66 172 50 148 50 124 C50 96 100 50 100 50 C100 50 150 96 150 124 C150 148 134 172 100 172 Z" {A} {SI}/>'
             + "".join(f'<path d="M{x} 40 Q{x-10} 28 {x} 16 Q{x+10} 4 {x} -6" {S} transform="translate(0 6)"/>' for x in [70, 130]),
    "snow": "".join(f'<g transform="rotate({a} 100 100)"><path d="M100 26 L100 174" {S}/><path d="M86 42 L100 56 L114 42 M86 158 L100 144 L114 158" {S}/></g>' for a in (0, 60, 120))
            + f'<circle cx="100" cy="100" r="14" {A}/>',
    "thermo": f'<path d="M86 40 Q86 24 100 24 Q114 24 114 40 L114 118 Q132 128 132 148 Q132 176 100 176 Q68 176 68 148 Q68 128 86 118 Z" {P} {SI}/>'
              f'<circle cx="100" cy="148" r="18" {A}/><rect x="94" y="80" width="12" height="60" rx="6" {A}/>'
              + "".join(f'<path d="M124 {y} L142 {y}" {S}/>' for y in (50, 72, 94)),
    "drop": f'<path d="M100 176 C62 176 44 150 44 124 C44 90 100 24 100 24 C100 24 156 90 156 124 C156 150 138 176 100 176 Z" {A} {SI}/><path d="M76 128 Q78 148 96 154" fill="none" stroke="var(--paper)" stroke-width="8" stroke-linecap="round"/>',
    "oil": f'<path d="M36 150 Q36 60 100 60 Q164 60 164 150" {P} {SI}/>' + "".join(f'<path d="M{x} {y+30} C{x-12} {y+30} {x-16} {y+20} {x-16} {y+14} C{x-16} {y+2} {x} {y-14} {x} {y-14} C{x} {y-14} {x+16} {y+2} {x+16} {y+14} C{x+16} {y+20} {x+12} {y+30} {x} {y+30} Z" {A} {SI}/>' for x, y in [(70, 92), (112, 76), (140, 112)]),
    "dna": f'<path d="M70 20 C150 60 50 140 130 180" {S}/><path d="M130 20 C50 60 150 140 70 180" {S}/>' + "".join(f'<path d="M{78+abs(i-2)*4} {50+i*25} L{122-abs(i-2)*4} {50+i*25}" stroke="var(--acc)" stroke-width="8" stroke-linecap="round"/>' for i in range(5)),
    "sun": f'<circle cx="100" cy="100" r="38" {A} {SI}/>' + "".join(f'<path d="M100 22 L100 44" {S} transform="rotate({a} 100 100)"/>' for a in range(0, 360, 45)),
    "hand": f'<path d="M64 180 L56 112 Q54 98 66 98 Q76 98 78 110 L80 60 Q80 46 92 46 Q104 46 104 60 L104 40 Q104 26 116 26 Q128 26 128 40 L128 58 Q128 46 140 46 Q152 46 152 60 L152 132 Q152 168 128 180 Z" {P} {SI}/><circle cx="148" cy="30" r="10" {A}/>',
    "jar": f'<rect x="52" y="78" width="96" height="94" rx="18" {P} {SI}/><rect x="44" y="40" width="112" height="40" rx="12" {A} {SI}/><path d="M76 116 L124 116 M76 138 L110 138" {S}/>',
    "check": f'<circle cx="100" cy="100" r="74" {A} {SI}/><path d="M64 102 L90 128 L138 76" fill="none" stroke="var(--ink)" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>',
    "cross": f'<circle cx="100" cy="100" r="74" {A} {SI}/><path d="M70 70 L130 130 M130 70 L70 130" fill="none" stroke="var(--ink)" stroke-width="14" stroke-linecap="round"/>',
    "stress": f'<path d="M40 176 Q40 80 100 80 Q160 80 160 176" {P} {SI}/><circle cx="100" cy="120" r="0"/>'
              f'<path d="M84 18 L66 52 L92 52 L76 84" fill="none" stroke="var(--acc)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="M134 22 L120 46 L140 46 L128 70" fill="none" stroke="var(--acc)" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>'
              f'<path d="M78 136 Q90 128 100 136 Q110 144 122 136" {S}/>',
    "hairfall": f'<rect x="34" y="40" width="132" height="34" rx="10" {A} {SI}/>' + "".join(f'<path d="M{x} 74 L{x} 98" {S}/>' for x in range(50, 160, 16))
                + "".join(f'<path d="M{x} {y} q12 14 0 28 q-12 14 0 28" {S}/>' for x, y in [(66, 118), (106, 130), (146, 112)]),
    "calendar": f'<rect x="30" y="44" width="140" height="130" rx="16" {P} {SI}/><path d="M30 82 L170 82" {S}/><path d="M66 30 L66 58 M134 30 L134 58" {S}/>'
                + "".join(f'<rect x="{48+c*38}" y="{96+r*36}" width="26" height="24" rx="5" {A if (r, c) == (1, 1) else INK} />' for r in range(2) for c in range(3)),
    "sprout": f'<path d="M100 176 L100 90" {S}/><path d="M100 110 Q56 112 44 64 Q92 60 100 110 Z" {A} {SI}/><path d="M100 92 Q110 44 160 38 Q160 88 100 92 Z" {A} {SI}/><path d="M60 176 L140 176" {S}/>',
    "star": f'<path d="M100 22 L122 74 L178 78 L134 114 L148 170 L100 140 L52 170 L66 114 L22 78 L78 74 Z" {A} {SI}/>',
    "photo": f'<rect x="26" y="40" width="148" height="120" rx="14" {P} {SI}/><circle cx="136" cy="76" r="14" {A}/><path d="M36 150 L86 92 L120 132 L138 114 L166 150" {S}/>',
    "hair-texture": f'<path d="M50 30 L50 170" {S}/><path d="M100 30 Q120 58 100 86 Q80 114 100 142 Q116 160 100 172" {S}/><path d="M150 30 q-16 10 0 20 q16 10 0 20 q-16 10 0 20 q16 10 0 20 q-16 10 0 20 q16 10 0 20 q-16 10 0 20" {S}/><circle cx="100" cy="186" r="0"/>',
    "camera": f'<path d="M30 70 L66 70 L78 50 L122 50 L134 70 L170 70 Q178 70 178 80 L178 160 Q178 168 170 168 L30 168 Q22 168 22 160 L22 80 Q22 70 30 70 Z" {P} {SI}/><circle cx="100" cy="116" r="32" {A} {SI}/><circle cx="100" cy="116" r="12" {INK}/>',
    "ruler": f'<rect x="20" y="70" width="160" height="60" rx="10" {A} {SI}/>' + "".join(f'<path d="M{x} 70 L{x} {100 if i % 2 == 0 else 88}" {S}/>' for i, x in enumerate(range(40, 175, 16))),
    "chat": f'<path d="M24 40 Q24 28 36 28 L124 28 Q136 28 136 40 L136 92 Q136 104 124 104 L64 104 L40 124 L44 104 L36 104 Q24 104 24 92 Z" {A} {SI}/><path d="M80 120 L80 132 Q80 144 92 144 L140 144 L164 168 L160 144 L164 144 Q176 144 176 132 L176 84 Q176 72 164 72 L150 72" {S}/>'
            + "".join(f'<circle cx="{x}" cy="66" r="7" {INK}/>' for x in (56, 80, 104)),
    "clipper": f'<path d="M64 60 L136 60 L130 172 Q130 180 122 180 L78 180 Q70 180 70 172 Z" {P} {SI}/><rect x="56" y="24" width="88" height="36" rx="6" {A} {SI}/>'
               + "".join(f'<path d="M{x} 24 L{x} 12" {S}/>' for x in range(66, 140, 12)) + f'<rect x="88" y="94" width="24" height="44" rx="10" {INK}/>',
    "razor": f'<path d="M30 132 L120 42 Q140 30 150 44 Q156 56 144 66 L56 156 Z" {P} {SI}/><path d="M56 156 L84 184 Q92 190 100 182 L172 110 Q178 102 170 96 L144 70" {A} {SI}/><circle cx="144" cy="66" r="8" {INK}/>',
    "scissors": f'<circle cx="58" cy="146" r="26" {P} {SI}/><circle cx="142" cy="146" r="26" {P} {SI}/><path d="M74 124 L150 24" {S}/><path d="M126 124 L50 24" {S}/><circle cx="100" cy="92" r="9" {A}/>',
    "comb": f'<rect x="24" y="50" width="152" height="40" rx="12" {A} {SI}/>' + "".join(f'<path d="M{x} 90 L{x} {150 if x < 100 else 128}" {S}/>' for x in range(40, 170, 14)),
    "mirror": f'<ellipse cx="100" cy="86" rx="56" ry="68" {P} {SI}/><path d="M74 60 Q84 44 102 40" fill="none" stroke="var(--acc)" stroke-width="10" stroke-linecap="round"/><path d="M100 154 L100 176 M66 182 L134 182" {S}/>',
    "hairdryer": f'<path d="M30 60 Q30 36 56 36 L132 36 Q166 36 166 70 Q166 104 132 104 L56 104 Q30 104 30 80 Z" {P} {SI}/><path d="M96 104 L86 176 L118 176 L124 104" {A} {SI}/><circle cx="130" cy="70" r="16" {INK}/>'
                 + "".join(f'<path d="M20 {y} L4 {y}" stroke="var(--acc)" stroke-width="8" stroke-linecap="round"/>' for y in (54, 70, 86)),
    "confident": f'<circle cx="100" cy="66" r="34" {P} {SI}/><path d="M38 182 Q38 110 100 110 Q162 110 162 182" {P} {SI}/><path d="M154 24 L160 40 L176 42 L164 52 L168 68 L154 60 L140 68 L144 52 L132 42 L148 40 Z" {A}/>',
    "person": f'<circle cx="100" cy="66" r="36" {P} {SI}/><path d="M34 182 Q34 112 100 112 Q166 112 166 182" {A} {SI}/>',
    "clock": f'<circle cx="100" cy="104" r="72" {P} {SI}/><path d="M100 104 L100 62 M100 104 L130 120" {S}/><circle cx="100" cy="104" r="9" {A}/><path d="M76 20 L124 20" {S}/>',
    "thumb": f'<path d="M30 92 L60 92 L60 176 L30 176 Z" {A} {SI}/><path d="M60 98 L92 52 Q98 28 116 34 Q128 40 120 70 L112 92 L160 92 Q176 94 172 112 L158 166 Q154 176 142 176 L60 176" {P} {SI}/>',
    "sleep": f'<path d="M130 40 Q80 50 80 104 Q80 158 134 164 Q96 182 64 158 Q36 134 40 96 Q46 46 100 34 Q116 32 130 40 Z" {A} {SI}/><path d="M120 76 L150 76 L120 108 L150 108" {S}/><path d="M156 34 L174 34 L156 54 L174 54" {S}/>',
    "talk": f'<path d="M30 40 Q30 26 44 26 L156 26 Q170 26 170 40 L170 118 Q170 132 156 132 L84 132 L50 166 L56 132 L44 132 Q30 132 30 118 Z" {P} {SI}/>' + "".join(f'<circle cx="{x}" cy="80" r="11" {A}/>' for x in (68, 100, 132)),
    "tag": f'<path d="M100 26 L170 26 Q176 26 176 32 L176 102 L90 188 L14 112 Z" {A} {SI}/><circle cx="146" cy="56" r="12" {P} {SI}/><path d="M76 106 L118 106 M76 128 L104 128" {S}/>',
    "shop": f'<rect x="34" y="84" width="132" height="92" {P} {SI}/>' + "".join(f'<path d="M{24+i*38} 50 L{62+i*38} 50 L{62+i*38} 76 Q{43+i*38} 96 {24+i*38} 76 Z" {A if i % 2 == 0 else P} {SI}/>' for i in range(4))
            + f'<rect x="84" y="118" width="34" height="58" {INK}/><rect x="124" y="104" width="30" height="28" rx="4" {A}/>',
    "trophy": f'<path d="M60 30 L140 30 L136 86 Q132 120 100 124 Q68 120 64 86 Z" {A} {SI}/><path d="M60 46 Q28 46 34 76 Q40 96 66 98 M140 46 Q172 46 166 76 Q160 96 134 98" {S}/><path d="M100 124 L100 152 M66 176 L134 176 L126 152 L74 152 Z" {S}/>',
    "broom": f'<path d="M140 20 L94 108" {S}/><path d="M74 100 L118 120 L104 176 Q80 184 44 164 Z" {A} {SI}/><path d="M66 146 L58 170 M84 152 L80 178 M98 156 L98 180" {S}/>',
    "spray": f'<rect x="54" y="82" width="76" height="98" rx="16" {P} {SI}/><path d="M72 82 L72 52 L118 52 L118 82" {S}/><path d="M86 52 L86 36 L146 36 L146 52" {A} {SI}/>'
             + "".join(f'<circle cx="{166+i*6}" cy="{28+j*14}" r="5" {A}/>' for i in range(2) for j in range(3)) + f'<rect x="70" y="112" width="44" height="38" rx="6" {A}/>',
    "scalp": f'<path d="M30 160 Q30 50 100 50 Q170 50 170 160" {P} {SI}/>' + "".join(f'<path d="M{x} {y} l6 6 m0 -6 l-6 6" stroke="var(--acc)" stroke-width="7" stroke-linecap="round"/>' for x, y in [(64, 92), (96, 76), (130, 88), (80, 116), (118, 112), (146, 126)]),
    "beard": face("oval", beard=True),
    "hair-thin": head("thin"),
}
for s in ("oval", "round", "square", "heart", "long"):
    ICONS[f"face-{s}"] = face(s)
    ICONS[f"face-{s}-b"] = face(s, beard=True)
for h in ("crop", "quiff", "sidepart", "crew", "fringe", "long"):
    ICONS[f"cut-{h}"] = head(h)


def svg(name, uid, size=None):
    if name.startswith("fade-"):
        body = fade(name.split("-")[1], uid)
    else:
        body = ICONS[name]
    sz = f' width="{size}" height="{size}"' if size else ""
    return f'<svg viewBox="0 0 200 200"{sz} xmlns="http://www.w3.org/2000/svg" overflow="visible">{body}</svg>'
