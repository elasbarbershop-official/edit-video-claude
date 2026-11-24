#!/usr/bin/env bash
# Check, render and loudness-normalise siri projects.
# usage: siri/tools/finish.sh [slug-prefix ...]   (no args = every project in siri/)
set -uo pipefail
export HYPERFRAMES_BROWSER_PATH=${HYPERFRAMES_BROWSER_PATH:-/opt/pw-browsers/chromium-1243/chrome-linux64/chrome}
cd "$(dirname "$0")/.."
mkdir -p renders
for d in [0-9][0-9]-*/; do
  slug=${d%/}
  if [ $# -gt 0 ]; then ok=0; for p in "$@"; do [[ $slug == $p* ]] && ok=1; done; [ $ok = 1 ] || continue; fi
  (
    cd "$slug"
    npx hyperframes check --json > check.json 2>/dev/null
    python3 - <<'EOF'
import json
d = json.load(open("check.json"))
bad = [f"{k}:{f.get('severity')}:{f.get('code')}:{(f.get('message') or '')[:120]}"
       for k, v in d.items() if isinstance(v, dict) and "findings" in v
       for f in v["findings"] if f.get("severity") in ("error", "warning")]
open("check-summary.txt", "w").write(f"ok={d.get('ok')}\n" + "\n".join(bad) + "\n")
EOF
    npx hyperframes render -q delivery -o raw.mp4 > render.log 2>&1 &&
    ffmpeg -nostdin -v error -y -i raw.mp4 -c:v copy -af "loudnorm=I=-15:TP=-1.5:LRA=11" -ar 48000 -c:a aac -b:a 192k \
      -movflags +faststart "../renders/$slug.mp4" && rm -f raw.mp4 && echo "rendered $slug" || echo "FAILED $slug"
  )
done
