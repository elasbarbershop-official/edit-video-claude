#!/usr/bin/env bash
# Copy the locked Elas Barbershop logo outro into a HyperFrames project.
# Usage: brand/install-outro.sh <project-dir>
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
dst="${1:?usage: install-outro.sh <project-dir>}"
mkdir -p "$dst/compositions" "$dst/assets/img/logo-parts" "$dst/assets/sfx"
cp "$here/elas-outro/compositions/elas-outro.html" "$dst/compositions/"
cp "$here/elas-outro/assets/img/logo-parts/"*.png "$dst/assets/img/logo-parts/"
cp -n "$here/elas-outro/assets/sfx/"* "$dst/assets/sfx/" 2>/dev/null || true
echo "Installed elas-outro into $dst. Mount it as the last scene (see the comment at the top of compositions/elas-outro.html)."
