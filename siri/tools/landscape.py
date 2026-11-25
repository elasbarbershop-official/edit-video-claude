"""Make a 16:9 (1920x1080) branded version of a finished 9:16 reel.

The portrait video sits in the centre; the left panel carries the series label and the hook title,
the right panel the Elas logo and the comment CTA. Audio is copied unchanged.

usage:
  python3 landscape.py siri [slug-prefix ...]          # siri videos (text taken from specs.py)
  python3 landscape.py one <in.mp4> <out.mp4> <series> <title lines | separated> <hl idx,..> <CTA WORD>
"""
import base64, os, subprocess, sys, tempfile
from html import escape

ROOT = "/home/user/edit-video-claude"
LOGO = f"{ROOT}/brand/elas-outro/assets/img/logo-parts/mask-all.png"
NAVY, YEL, CREAM = "#091936", "#ffba00", "#faf8f2"
VX, VW = 656, 608  # video slot




def panel_png(out_png, series, lines, hl, word):
    logo = base64.b64encode(open(f"{ROOT}/brand/logo/elas-logo.png", "rb").read()).decode()
    n = max(len(l) for l in lines)
    size = int(min(78, 500 / (0.78 * max(n, 1))))
    title = "".join(f'<div style="color:{YEL if i in hl else CREAM}">{escape(l)}</div>' for i, l in enumerate(lines))
    html = f"""<html><head><link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800;900&display=block" rel="stylesheet">
<style>body{{margin:0;width:1920px;height:1080px;background:{NAVY};font-family:Montserrat,sans-serif;overflow:hidden;position:relative}}
.chip{{position:absolute;left:96px;top:300px;background:{YEL};color:{NAVY};font-weight:900;font-size:26px;letter-spacing:.08em;padding:8px 14px}}
.title{{position:absolute;left:96px;top:356px;font-weight:900;font-size:{size}px;line-height:1.04;letter-spacing:-.01em}}
.sub{{position:absolute;left:96px;top:{356 + int(len(lines) * size * 1.04) + 34}px;color:{CREAM};opacity:.8;font-weight:700;font-size:28px}}
.frame{{position:absolute;left:{VX - 8}px;top:0;width:{VW + 16}px;height:1080px;background:{YEL}}}
.logo{{position:absolute;left:1340px;top:330px;width:480px}}
.cta{{position:absolute;left:1340px;top:640px;width:480px;text-align:center}}
.pill{{display:inline-block;background:{YEL};color:{NAVY};font-weight:900;font-size:34px;padding:14px 30px;border-radius:40px}}
.cta p{{color:{CREAM};font-weight:700;font-size:24px;margin:18px 0 0}}
.st{{position:absolute;width:60px;height:1600px;transform:rotate(22deg)}}</style></head><body>
<div class="st" style="left:-130px;top:800px;background:{YEL}"></div><div class="st" style="left:-50px;top:880px;background:{CREAM};width:34px"></div>
<div class="chip">{escape(series)}</div><div class="title">{title}</div><div class="sub">Tonton sampai habis &#8594;</div>
<div class="frame"></div>
<img class="logo" src="data:image/png;base64,{logo}">
<div class="cta"><div class="pill">KOMEN &quot;{escape(word)}&quot;</div><p>Tempah slot di Elas Barbershop</p></div>
</body></html>"""
    tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False)
    tmp.write(html); tmp.close()
    js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage({{viewport:{{width:1920,height:1080}}}});
await p.goto('file://{tmp.name}');await p.waitForTimeout(800);await p.screenshot({{path:'{out_png}'}});await b.close();}})()"""
    subprocess.run(["node", "-e", js], check=True)
    os.unlink(tmp.name)


def compose(src, out, png):
    os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-loop", "1", "-i", png, "-i", src, "-filter_complex",
                    f"[1:v]scale={VW}:1080:flags=lanczos[v];[0:v][v]overlay={VX}:0:shortest=1,format=yuv420p[o]",
                    "-map", "[o]", "-map", "1:a", "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-r", "30",
                    "-c:a", "copy", "-movflags", "+faststart", out], check=True)


def make(src, out, series, lines, hl, word):
    png = out[:-4] + "-panel.png"
    panel_png(png, series, lines, hl, word)
    compose(src, out, png)
    os.unlink(png)
    print("landscape", out, flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "siri":
        sys.path.insert(0, f"{ROOT}/siri")
        from specs import VIDEOS
        want = sys.argv[2:]
        for v in VIDEOS:
            if want and not any(v["slug"].startswith(w) for w in want):
                continue
            src = f"{ROOT}/siri/renders/{v['slug']}.mp4"
            if not os.path.exists(src):
                continue
            h, c = v["scenes"][0], v["scenes"][-1]
            make(src, f"{ROOT}/siri/renders/landscape/{v['slug']}-16x9.mp4", v["series"], h["lines"], h["hl"], c["word"])
    else:
        _, _, src, out, series, lines, hl, word = sys.argv
        make(src, out, series, lines.split("|"), [int(x) for x in hl.split(",") if x], word)
