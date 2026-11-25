"""Premium stickman for the business / story styles. viewBox 0 0 200 300, faceless.
Colours: ink (body), acc (accent: apron / tie / props). Thick rounded strokes so it reads at phone size."""

POSES = {
    # shoulder (100,104), hip (100,186); each limb: (elbow/knee, hand/foot)
    "stand":   dict(la=((72, 146), (66, 190)), ra=((128, 146), (134, 190)), ll=((86, 236), (78, 286)), rl=((114, 236), (122, 286))),
    "worried": dict(la=((52, 86), (80, 40)), ra=((148, 86), (120, 40)), ll=((86, 236), (74, 286)), rl=((114, 236), (126, 286))),
    "barber":  dict(la=((70, 148), (70, 194)), ra=((146, 128), (184, 104)), ll=((88, 236), (80, 286)), rl=((114, 236), (124, 286))),
    "sit":     dict(la=((76, 146), (110, 172)), ra=((124, 146), (140, 172)), ll=((150, 196), (150, 270)), rl=((160, 200), (164, 270))),
    "point":   dict(la=((72, 146), (68, 190)), ra=((146, 84), (186, 52)), ll=((86, 236), (78, 286)), rl=((114, 236), (122, 286))),
    "happy":   dict(la=((54, 70), (40, 30)), ra=((146, 70), (160, 30)), ll=((84, 236), (70, 286)), rl=((116, 236), (130, 286))),
    "walk":    dict(la=((80, 146), (100, 186)), ra=((122, 146), (108, 186)), ll=((112, 232), (130, 286)), rl=((92, 236), (74, 284))),
}


def stickman(pose="stand", ink="#091936", acc="#ffba00", prop=None, cape=False, tie=False):
    p = POSES[pose]
    sw = 'stroke-width="15" stroke-linecap="round" stroke-linejoin="round" fill="none"'
    sitting = pose == "sit"
    hip = (100, 186)
    limbs = "".join(f'<path d="M{a[0]} {a[1]} L{e[0]} {e[1]} L{h[0]} {h[1]}" stroke="{ink}" {sw}/>'
                    for a, (e, h) in [((100, 104), p["la"]), ((100, 104), p["ra"])])
    legs = "".join(f'<path d="M{hip[0]} {hip[1]} L{k[0]} {k[1]} L{f[0]} {f[1]}" stroke="{ink}" {sw}/>' for k, f in (p["ll"], p["rl"]))
    body = f'<path d="M100 90 L100 186" stroke="{ink}" {sw}/>'
    head = f'<circle cx="100" cy="52" r="32" fill="{ink}"/><path d="M78 40 Q100 20 124 38" stroke="{acc}" stroke-width="6" fill="none" stroke-linecap="round" opacity="0.9"/>'
    extra = ""
    if tie:
        extra += f'<path d="M100 98 L92 112 L100 150 L108 112 Z" fill="{acc}"/>'
    if cape:
        extra += f'<path d="M58 100 L142 100 L170 200 L30 200 Z" fill="{acc}" opacity="0.95"/>'
    if prop == "clipper":
        h = p["ra"][1]
        extra += f'<g transform="translate({h[0] - 10} {h[1] - 26}) rotate(-30 10 26)"><rect x="0" y="0" width="22" height="46" rx="6" fill="{acc}"/><rect x="-3" y="-8" width="28" height="12" rx="3" fill="{ink}"/></g>'
    if prop == "sweat":
        extra += f'<path d="M150 30 C142 44 142 52 150 56 C158 52 158 44 150 30 Z" fill="{acc}"/>'
    order = (legs + body + extra + limbs + head) if cape else (legs + body + limbs + extra + head)
    if sitting:
        order = legs + body + limbs + extra + head
    return f'<svg viewBox="0 0 200 300" xmlns="http://www.w3.org/2000/svg" overflow="visible">{order}</svg>'


def chair(ink="#091936", acc="#ffba00"):
    """Barber chair seen from the side, same 200x300 box as the stickman (customer sits at hip 100,186)."""
    return (f'<svg viewBox="0 0 200 300" xmlns="http://www.w3.org/2000/svg" overflow="visible">'
            f'<path d="M60 96 L66 196 L168 196" stroke="{acc}" stroke-width="18" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="M110 200 L110 268 M70 284 L150 284" stroke="{ink}" stroke-width="12" stroke-linecap="round"/></svg>')
