"""Elas 2D character: faceless front-view bust with swappable face shape, hairstyle,
side length (clipper guard 0-4 or fade low/mid/high) and beard. viewBox 0 0 600 760."""

HEAD = {
    "oval": "M300 120 C390 120 420 200 418 300 C416 400 380 500 300 540 C220 500 184 400 182 300 C180 200 210 120 300 120 Z",
    "round": "M300 125 C400 125 430 210 430 320 C430 430 380 520 300 532 C220 520 170 430 170 320 C170 210 200 125 300 125 Z",
    "square": "M300 120 C395 120 422 180 422 260 L422 420 Q420 500 360 530 L240 530 Q180 500 178 420 L178 260 C178 180 205 120 300 120 Z",
    "heart": "M300 120 C402 120 430 200 426 290 C422 380 380 470 300 544 C220 470 178 380 174 290 C170 200 198 120 300 120 Z",
    "long": "M300 98 C386 98 406 180 405 290 C404 420 372 524 300 566 C228 524 196 420 195 290 C194 180 214 98 300 98 Z",
}
HALF = {"oval": 118, "round": 130, "square": 122, "heart": 126, "long": 105}
CHIN = {"oval": 540, "round": 532, "square": 530, "heart": 544, "long": 566}

HAIR = {
    "crop": "M175 250 Q170 120 300 95 Q430 120 425 250 Q410 215 382 224 L360 200 L336 224 L310 198 L285 226 L260 200 L238 224 Q200 212 175 250 Z",
    "quiff": "M178 240 Q170 130 260 92 Q330 46 420 88 Q462 118 426 170 Q426 205 424 240 Q400 180 300 186 Q215 186 178 240 Z",
    "sidepart": "M178 256 Q168 120 300 100 Q432 112 424 256 Q414 200 380 186 L252 186 Q202 196 178 256 Z",
    "crew": "M184 232 Q186 122 300 112 Q414 122 416 232 Q380 196 300 197 Q220 196 184 232 Z",
    "fringe": "M172 272 Q160 115 300 95 Q440 115 428 272 Q414 242 396 256 L372 230 L346 260 L320 232 L294 260 L268 232 L244 260 L218 238 Q195 252 172 272 Z",
    "long": "M166 392 Q138 108 300 90 Q462 108 434 392 Q424 300 420 252 Q380 192 300 194 Q220 192 180 252 Q176 300 166 392 Z",
    "messy": "M176 248 Q160 130 240 100 L250 74 L282 96 L300 66 L322 94 L356 72 L362 104 Q440 126 424 248 Q408 206 370 214 L350 190 L322 214 L298 186 L272 214 L248 192 L226 218 Q196 214 176 248 Z",
    "buzz": "M186 236 Q188 126 300 116 Q412 126 414 236 Q380 206 300 206 Q220 206 186 236 Z",
}

BEARD = {
    "full": "M{l} 392 Q{l2} 510 300 {c} Q{r2} 510 {r} 392 Q{r3} 450 300 452 Q{l3} 450 {l} 392 Z",
    "chin": "M{lc} 450 Q{lc2} 520 300 {c} Q{rc2} 520 {rc} 450 Q300 470 {lc} 450 Z",
}


def _side(level, uid, hw=118):
    """Fill for the sides (above the ears). level 0-4 clipper guard, or 'low'/'mid'/'high' fade."""
    if isinstance(level, int):
        op = [0.12, 0.35, 0.55, 0.78, 0.95][level]
        f = f'fill="#1a110c" opacity="{op}"'
        return _bands(hw, f), ""
    stop = {"low": 0.72, "mid": 0.42, "high": 0.12}[level]
    g = f"sd-{uid}"
    defs = (f'<linearGradient id="{g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a110c" stop-opacity="0.95"/>'
            f'<stop offset="{stop:.2f}" stop-color="#1a110c" stop-opacity="0.8"/><stop offset="{min(1, stop + 0.18):.2f}" stop-color="#1a110c" stop-opacity="0.05"/>'
            f'<stop offset="1" stop-color="#1a110c" stop-opacity="0"/></linearGradient>')
    return _bands(hw, f'fill="url(#{g})"'), defs


def _bands(hw, fill):
    # temple/side bands just inside the head outline, from the crown down to the ear
    l, r = 300 - hw - 20, 300 + hw - 62
    return (f'<path d="M{l} 175 L{l + 84} 175 Q{l + 72} 260 {l + 64} 350 L{l} 350 Z" {fill}/>'
            f'<path d="M{r + 82} 175 L{r - 2} 175 Q{r + 10} 260 {r + 18} 350 L{r + 82} 350 Z" {fill}/>')


def character(uid, face="oval", hair="crop", side="mid", beard=None, shirt="#1c2d55", thin=False):
    hd = HEAD[face]; hw = HALF[face]; ch = CHIN[face]
    sx = hw / 118.0
    side_fill, side_defs = _side(side, uid, hw) if side is not None else ("", "")
    ear_y = 312
    defs = f"""<defs>
  <radialGradient id="sk-{uid}" cx="0.45" cy="0.38" r="0.7"><stop offset="0" stop-color="#f3c7a3"/><stop offset="0.7" stop-color="#e0a882"/><stop offset="1" stop-color="#c88c66"/></radialGradient>
  <linearGradient id="hr-{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a271d"/><stop offset="1" stop-color="#140d09"/></linearGradient>
  <linearGradient id="nk-{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b9805c"/><stop offset="0.35" stop-color="#d39b75"/></linearGradient>
  <clipPath id="hc-{uid}"><path d="{hd}"/></clipPath>
  {side_defs}
</defs>"""
    body = (f'<path d="M50 760 Q62 648 196 612 L250 596 Q300 642 350 596 L404 612 Q538 648 550 760 Z" fill="{shirt}"/>'
            f'<path d="M250 596 Q300 642 350 596 L344 586 Q300 626 256 586 Z" fill="#000" opacity="0.18"/>'
            f'<path d="M258 {ch - 40} L256 600 Q300 640 344 600 L342 {ch - 40} Z" fill="url(#nk-{uid})"/>')
    ears = (f'<ellipse cx="{300 - hw - 4}" cy="{ear_y}" rx="24" ry="44" fill="#d9a07a"/><ellipse cx="{300 - hw}" cy="{ear_y}" rx="11" ry="26" fill="#b97f5b" opacity="0.6"/>'
            f'<ellipse cx="{300 + hw + 4}" cy="{ear_y}" rx="24" ry="44" fill="#d9a07a"/><ellipse cx="{300 + hw}" cy="{ear_y}" rx="11" ry="26" fill="#b97f5b" opacity="0.6"/>')
    head = (f'<path d="{hd}" fill="url(#sk-{uid})"/>'
            f'<g clip-path="url(#hc-{uid})">{side_fill}'
            f'<ellipse cx="300" cy="{ch + 10}" rx="{hw}" ry="60" fill="#8a5232" opacity="0.18"/>'
            f'<ellipse cx="{300 - hw * 0.62:.0f}" cy="380" rx="40" ry="70" fill="#b0704c" opacity="0.12"/><ellipse cx="{300 + hw * 0.62:.0f}" cy="380" rx="40" ry="70" fill="#b0704c" opacity="0.12"/></g>')
    hair_svg = ""
    if hair in HAIR:
        op = 0.55 if thin else 1
        hair_svg = (f'<g transform="translate(300 0) scale({sx:.3f} 1) translate(-300 0)" opacity="{op}">'
                    f'<path d="{HAIR[hair]}" fill="url(#hr-{uid})"/>'
                    + "".join(f'<path d="M{x} {130 + abs(x - 300) * 0.2:.0f} Q{x + 10} {170 + abs(x - 300) * 0.2:.0f} {x + 4} {205 + abs(x - 300) * 0.1:.0f}" stroke="#6b4a37" stroke-width="5" fill="none" stroke-linecap="round" opacity="0.45"/>' for x in range(222, 380, 26))
                    + "</g>")
        if hair == "sidepart":
            hair_svg += f'<path d="M252 188 Q246 140 262 108" stroke="#c48d68" stroke-width="5" fill="none" opacity="0.7" transform="translate(300 0) scale({sx:.3f} 1) translate(-300 0)"/>'
    beard_svg = ""
    if beard:
        l, r = 300 - hw + 6, 300 + hw - 6
        d = BEARD["full" if beard == "full" else "chin"].format(
            l=l, r=r, l2=l + 4, r2=r - 4, l3=l + 40, r3=r - 40, c=ch + 6,
            lc=300 - hw * 0.55, rc=300 + hw * 0.55, lc2=300 - hw * 0.5, rc2=300 + hw * 0.5)
        beard_svg = (f'<path d="{d}" fill="#1a110c" opacity="0.88"/>'
                     f'<path d="M262 418 Q300 404 338 418 Q300 430 262 418 Z" fill="#1a110c" opacity="0.88"/>')
    return f'<svg viewBox="0 0 600 760" xmlns="http://www.w3.org/2000/svg">{defs}{body}{ears}{head}{beard_svg}{hair_svg}</svg>'


# Map icon names used in specs onto character variants (None = keep the flat icon).
def from_icon(name):
    if name.startswith("face-"):
        parts = name.split("-")
        return dict(face=parts[1], hair="crop", side="mid", beard="full" if parts[-1] == "b" else None)
    if name.startswith("cut-"):
        h = name.split("-")[1]
        return dict(hair=h, side={"crew": "high", "crop": "mid", "quiff": "mid", "sidepart": "low", "fringe": "low", "long": 3}.get(h, "mid"))
    if name.startswith("fade-"):
        return dict(hair="crop", side=name.split("-")[1])
    if name == "beard":
        return dict(hair="sidepart", side="low", beard="full")
    if name == "hair-thin":
        return dict(hair="buzz", side=1, thin=True)
    if name in ("person", "confident"):
        return dict(hair="quiff", side="mid")
    return None
