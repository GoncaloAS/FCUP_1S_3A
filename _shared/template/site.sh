#!/bin/bash
# Gera o site (_site/) e abre-o em http://localhost:8000 para ver antes do push.
# Uso: _shared/template/site.sh [porta]
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
PORTA="${1:-8000}"
python3 "$ROOT/_shared/site/build_site.py"
echo "Site em http://localhost:$PORTA (Ctrl+C para parar)"
python3 -m http.server "$PORTA" -d "$ROOT/_site"
