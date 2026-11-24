// Deterministic hair-tress drawing. Every mode yields the same number of points,
// so GSAP can tween a path's "d" attribute between modes (attr: { d }).
(function () {
  const P = 24;
  function rnd(i, k) { const x = Math.sin(i * 127.1 + k * 311.7) * 43758.5453; return x - Math.floor(x); }
  function d(o, i, mode, ph) {
    const c = (o.n - 1) / 2, pts = [];
    for (let k = 0; k < P; k++) {
      const t = k / (P - 1);
      let off = 0;
      if (mode === "frizz") off = (i - c) * o.gap * 0.95 * t * t + (rnd(i, k) * 2 - 1) * (4 + 30 * t);
      else if (mode === "smooth") off = Math.sin(t * Math.PI * 1.3 + (ph || 0) + i * 0.06) * 18 * t - (i - c) * o.gap * 0.1 * t;
      else if (mode === "regrow") off = t < 0.22 ? (rnd(i, k) * 2 - 1) * 12 * (1 - t / 0.22) + (i - c) * 3 * (1 - t / 0.22) : 0;
      pts.push((o.x0 + i * o.gap + off).toFixed(1) + "," + (o.y0 + t * o.len).toFixed(1));
    }
    return "M" + pts.join(" L");
  }
  function build(svg, o) {
    const NS = "http://www.w3.org/2000/svg", paths = [];
    for (let i = 0; i < o.n; i++) {
      const p = document.createElementNS(NS, "path");
      p.setAttribute("d", d(o, i, o.mode || "frizz", 0));
      p.setAttribute("fill", "none");
      p.setAttribute("stroke", o.color || "#1e140f");
      p.setAttribute("stroke-width", o.width || 11);
      p.setAttribute("stroke-linecap", "round");
      p.setAttribute("stroke-linejoin", "round");
      svg.appendChild(p);
      paths.push(p);
    }
    const clip = document.createElementNS(NS, "rect");
    const w = (o.n - 1) * o.gap + 50;
    clip.setAttribute("x", o.x0 - 25); clip.setAttribute("y", o.y0 - 34);
    clip.setAttribute("width", w); clip.setAttribute("height", 48);
    clip.setAttribute("rx", 14); clip.setAttribute("fill", o.clip || "#ffba00");
    svg.appendChild(clip);
    return {
      paths,
      d: (i, mode, ph) => d(o, i, mode, ph),
      // Tween every strand to a mode on timeline tl at time at.
      to(tl, mode, at, dur, ease, ph) {
        paths.forEach((p, i) => tl.to(p, { attr: { d: d(o, i, mode, ph) }, duration: dur, ease: ease || "power3.inOut" }, at));
      },
      // Sway: smooth mode with phase moving; deterministic function of timeline time.
      sway(tl, at, dur, cycles) {
        const st = { ph: 0 };
        tl.fromTo(st, { ph: 0 }, { ph: Math.PI * 2 * (cycles || 1), duration: dur, ease: "none", immediateRender: false,
          onUpdate: () => paths.forEach((p, i) => p.setAttribute("d", d(o, i, "smooth", st.ph))) }, at);
      },
    };
  }
  window.Hair = { build };
})();
