"""PreToolUse(Bash): regras de git que a memória não chega para garantir.
- Há sessões em paralelo nesta árvore: nada de `git add -A` / `git add .` (adiciona por caminho).
- Os commits do Gonçalo não levam Co-Authored-By do Claude.
- O repositório é público: nada de forçar (`git add -f`) os ficheiros pessoais do .gitignore."""
import json, re, sys

cmd = json.load(sys.stdin).get("tool_input", {}).get("command", "")
# só conta o que é mesmo comando (não texto dentro de aspas ou de um heredoc de mensagem)
codigo = re.sub(r"'[^']*'|\"[^\"]*\"", "", cmd.split("<<")[0])
if re.search(r"(^|[;&|]\s*)git\s+add\s+(-A|--all|\.(\s|$))", codigo):
    print("Bloqueado: há outras sessões a trabalhar nesta árvore. Adiciona só os teus ficheiros, por caminho "
          "(`git add <ficheiros>`), e confirma o `git status` antes do commit.", file=sys.stderr)
    sys.exit(2)
if re.search(r"(^|[;&|]\s*)git\s+add\b[^;&|]*\s(-f|--force)\b", codigo) and \
        re.search(r"INFO_|AGENDA|Feedback_|registo\.json", codigo):
    print("Bloqueado: INFO, AGENDA e feedback são pessoais e o repositório é público. Vão só cifrados "
          "no _shared/site/pessoal.enc (pessoal.py).", file=sys.stderr)
    sys.exit(2)
if re.search(r"(^|[;&|]\s*)git\s+commit", codigo) and re.search(r"Co-Authored-By:\s*Claude", cmd, re.I):
    print("Bloqueado: os commits do Gonçalo não levam Co-Authored-By do Claude. Tira essa linha.", file=sys.stderr)
    sys.exit(2)
