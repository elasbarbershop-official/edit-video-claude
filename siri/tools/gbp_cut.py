"""Make <=30 s cuts for Google Business Profile (Google rejects videos longer than 30 s).

Keeps whole scenes from the start (cut on a scene boundary, so no sentence is chopped) and then joins the
locked logo outro with a short crossfade. Output: siri/renders/gbp/<slug>-30s.mp4
usage: python3 siri/tools/gbp_cut.py [slug-prefix ...]
"""
import os, re, subprocess, sys

SIRI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX, OUTRO, XF = 29.5, 4.2, 0.3


def dur(f):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f]))


def cut(slug):
    src = f"{SIRI}/renders/{slug}.mp4"
    idx = open(f"{SIRI}/{slug}/index.html").read()
    starts = [float(x) for x in re.findall(r'data-composition-src="compositions/s\d+\.html" data-start="([\d.]+)"', idx)]
    o = float(re.search(r'compositions/elas-outro\.html" data-start="([\d.]+)"', idx).group(1))
    os.makedirs(f"{SIRI}/renders/gbp", exist_ok=True)
    out = f"{SIRI}/renders/gbp/{slug}-30s.mp4"
    total = dur(src)
    if total <= 30:
        subprocess.run(["cp", src, out], check=True); return out, total
    # last scene boundary that leaves room for the outro (scene start minus a beat before its wipe)
    cands = [s for s in starts[2:] if s + OUTRO - XF <= MAX]
    c = (max(cands) if cands else MAX - OUTRO + XF) + 0.15
    tail = total - o
    fc = (f"[0:v]trim=0:{c:.2f},setpts=PTS-STARTPTS[a];[0:v]trim={o:.2f}:{total:.2f},setpts=PTS-STARTPTS[b];"
          f"[a][b]xfade=transition=fade:duration={XF}:offset={c - XF:.2f},format=yuv420p[v];"
          f"[0:a]atrim=0:{c:.2f},asetpts=PTS-STARTPTS[x];[0:a]atrim={o:.2f}:{total:.2f},asetpts=PTS-STARTPTS[y];"
          f"[x][y]acrossfade=d={XF}[au]")
    subprocess.run(["ffmpeg", "-nostdin", "-v", "error", "-y", "-i", src, "-filter_complex", fc, "-map", "[v]", "-map", "[au]",
                    "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-r", "30", "-c:a", "aac", "-b:a", "192k",
                    "-movflags", "+faststart", out], check=True)
    return out, c + tail - XF


if __name__ == "__main__":
    want = sys.argv[1:]
    for d in sorted(os.listdir(f"{SIRI}/renders")):
        if not d.endswith(".mp4"):
            continue
        slug = d[:-4]
        if want and not any(slug.startswith(w) for w in want):
            continue
        if not os.path.exists(f"{SIRI}/{slug}/index.html"):
            continue
        out, ln = cut(slug)
        print(f"{slug}: {dur(out):.1f}s", flush=True)
