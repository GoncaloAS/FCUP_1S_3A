#!/usr/bin/env python3
"""Gera o site único de soluções, SOLUCOES.html (na raiz do repositório).

Junta numa só página as soluções de todas as disciplinas, cada uma a partir
da sua fonte <Disciplina>/.fonte/SOLUCOES_<Disciplina>.md, com um separador
por disciplina. Corre sozinho (python3 _shared/template/build_solucoes.py)
ou no fim do build.sh. Reconstrói sempre todas as disciplinas, para o site
nunca ficar com uma disciplina desatualizada.
"""
import html
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "_shared/template"
SAIDA = ROOT / "SOLUCOES.html"


def nome_da_disciplina(md: Path, pasta: str) -> str:
    """'Lógica Computacional --- Soluções ...' -> 'Lógica Computacional'."""
    m = re.search(r'^title:\s*"?(.*?)\s*(---|—|")', md.read_text(), re.M)
    return m.group(1).strip() if m and m.group(1).strip() else pasta


def fragmento(md: Path, pasta: str, nome: str, cor: int) -> str:
    cmd = [
        "pandoc", str(md), "-f", "markdown",
        "--template", str(TEMPLATE / "solucoes-disciplina.html"),
        "--lua-filter", str(TEMPLATE / "fitch.lua"),
        "--lua-filter", str(TEMPLATE / "solucoes.lua"),
        "--lua-filter", str(TEMPLATE / "auto-align.lua"),
        "--math-method=mathml", "--section-divs",
        "--embed-resources", "--standalone",
        "--syntax-highlighting=tango",
        f"--id-prefix={pasta}-",
        f"--resource-path={md.parent.parent}",
        "-M", f"disciplina={pasta}",
        "-M", f"nome={nome}",
        "-M", f"cor={cor}",
    ]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"Erro a gerar as soluções de {pasta}:\n{r.stderr}")
    if r.stderr.strip():
        print(r.stderr.strip(), file=sys.stderr)
    return r.stdout


def main() -> None:
    fontes = sorted(ROOT.glob("*/.fonte/SOLUCOES_*.md"),
                    key=lambda p: p.parent.parent.name.lower())
    if not fontes:
        sys.exit("Não há nenhum .fonte/SOLUCOES_*.md")
    separadores, seccoes = [], []
    for i, md in enumerate(fontes):
        pasta = md.parent.parent.name
        nome = nome_da_disciplina(md, pasta)
        seccoes.append(fragmento(md, pasta, nome, i % 6))
        separadores.append(
            f'<button type="button" role="tab" class="separador" data-cor="{i % 6}" '
            f'data-alvo="{pasta}" aria-selected="false">{html.escape(nome)}</button>')
    pagina = (TEMPLATE / "solucoes.html").read_text()
    pagina = pagina.replace("<!--SEPARADORES-->", "\n".join(separadores))
    pagina = pagina.replace("<!--DISCIPLINAS-->", "\n".join(seccoes))
    SAIDA.write_text(pagina)
    print(f"Gerado: {SAIDA} ({len(fontes)} disciplinas)")


if __name__ == "__main__":
    main()
