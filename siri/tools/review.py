"""Snapshot each scene of each siri project (late in the scene, when everything is on screen)
and tile them: one row per video. usage: python3 review.py out.jpg slug-prefix ..."""
import os, re, subprocess, sys
from PIL import Image, ImageDraw

SIRI = "/home/user/edit-video-claude/siri"
env = dict(os.environ, HYPERFRAMES_BROWSER_PATH="/opt/pw-browsers/chromium-1243/chrome-linux64/chrome")
out, prefixes = sys.argv[1], sys.argv[2:]
rows = []
for slug in sorted(os.listdir(SIRI)):
    if not re.match(r"\d\d-", slug) or (prefixes and not any(slug.startswith(p) for p in prefixes)):
        continue
    idx = open(f"{SIRI}/{slug}/index.html").read()
    hosts = re.findall(r'id="(s\d+)" data-composition-id="s\d+" data-composition-src="[^"]+" data-start="([\d.]+)" data-duration="([\d.]+)"', idx)
    outro = float(re.search(r'elas-outro.html" data-start="([\d.]+)"', idx).group(1))
    times = [float(s) + float(d) - 0.75 for _, s, d in hosts] + [outro + 3.0]
    times[0] = 0.05
    r = subprocess.run(["npx", "hyperframes", "snapshot", "--at", ",".join(f"{t:.2f}" for t in times)],
                       cwd=f"{SIRI}/{slug}", env=env, capture_output=True, text=True)
    frames = sorted(set(re.findall(r"(/\S+/frame-\d+-at-[\d.]+s\.png)", r.stdout)), key=lambda p: int(re.search(r"frame-(\d+)", p).group(1)))
    rows.append((slug, frames[: len(times)]))
W = 216; H = 384
cols = max(len(f) for _, f in rows)
sheet = Image.new("RGB", (cols * W + 10, len(rows) * (H + 30)), "#222")
d = ImageDraw.Draw(sheet)
for y, (slug, frames) in enumerate(rows):
    d.text((6, y * (H + 30) + 6), slug, fill="#fff")
    for x, f in enumerate(frames):
        sheet.paste(Image.open(f).convert("RGB").resize((W, H)), (x * W + 5, y * (H + 30) + 26))
sheet.save(out, quality=80)
print(out, [(s, len(f)) for s, f in rows])
