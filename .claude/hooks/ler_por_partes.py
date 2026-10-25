"""PreToolUse(Read): impõe a regra "ler por partes" do CLAUDE.md.
- PDF: só com `pages` de 1 ou 2 páginas (cada página é uma imagem cara); o texto vem do cache.
- Texto com mais de 40 KB (RESUMOs, SOLUCOES, quiz): só com `limit` (≤ 400 linhas), depois de um grep.
`allow_large: true` deixa passar quando o Gonçalo pediu mesmo o ficheiro inteiro."""
import json, os, re, sys

ev = json.load(sys.stdin)
inp = ev.get("tool_input", {})
path = inp.get("file_path", "")
root = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR", "."))
if not os.path.realpath(path).startswith(root + os.sep) or inp.get("allow_large"):
    sys.exit(0)

if path.lower().endswith(".pdf"):
    pags = str(inp.get("pages", "")).strip()
    m = re.fullmatch(r"(\d+)(?:-(\d+))?", pags)
    if m and int(m.group(2) or m.group(1)) - int(m.group(1)) < 2:
        sys.exit(0)
    print("PDF bloqueado: cada página entra como imagem. Texto: o cache (.fonte/.cache, contexto.sh) "
          "ou `pdftotext -f N -l N`. Imagem: Read com pages:\"N\" (no máximo 2 páginas).", file=sys.stderr)
    sys.exit(2)

try:
    kb = os.path.getsize(path) // 1024
except OSError:
    sys.exit(0)
limit = inp.get("limit")
if kb > 40 and (not limit or int(limit) > 400):
    print(f"{os.path.relpath(path, root)} tem {kb} KB: lê por partes. Primeiro `grep -n` "
          "(ou `contexto.sh <D> --mapa termos`), depois Read com offset e limit ≤ 400.", file=sys.stderr)
    sys.exit(2)
