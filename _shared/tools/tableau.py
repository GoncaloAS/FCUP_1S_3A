#!/usr/bin/env python3
"""Tableaux semânticos e refutações por resolução: verificação e desenho.

Blocos no Markdown (desenhados pelo filtro _shared/template/tableau.lua):

  ```{.tableau seq="(p -> q) -> (~q -> ~p)"}
  ~((p -> q) -> (~q -> ~p))
  p -> q                ; 1
  ~(~q -> ~p)           ; 1
  ~q                    ; 3
  ~~p                   ; 3
  p                     ; 5
  [
  ~p                    ; 2
  x                     ; 6, 7
  |
  q                     ; 2
  x                     ; 4, 9
  ]
  ```

  - Os nós numeram-se pela ordem do texto. As linhas sem ";" no início são a
    raiz (o conjunto {phi1, ..., phin}); "; j" diz o nó expandido (a regra,
    alfa, beta, ~~, ~F, ~T, deduz-se da fórmula de j).
  - "[" abre uma ramificação (regra beta), "|" passa ao ramo seguinte e "]"
    fecha. Depois de "]" o ramo acabou.
  - "x ; i, k" fecha o ramo: os nós i e k são psi e ~psi (ou um deles é F).
  - Nos atributos seq/de o pandoc come as barras: escreve-se /\\\\ e \\\\/
    (duas barras) em vez de /\\ e \\/.
  - seq="phi": a raiz tem de ser ~phi (dedução por tableau de phi).
    Classe .aberto: o tableau pode ter ramos abertos (não exige "x").

  ```{.resolucao de="((p -> q) /\\\\ (q -> r)) -> ~(~r /\\\\ p)"}
  {~p, q}
  {~q, r}
  {~r}
  {p}
  {q}                   ; 1, 4
  {r}                   ; 2, 5
  F                     ; 3, 6
  ```

  - Linhas sem ";" são as cláusulas do conjunto; "; i, k" diz que a linha é
    a resolvente das cláusulas i e k. A última linha tem de ser F ({}).
  - de="phi": o conjunto de cláusulas tem de ser equivalente a ~phi
    (refutação = dedução por resolução de phi).

Uso:
  tableau.py check <ficheiros.md>     verifica todos os blocos
  tableau.py dot tableau|resolucao [seq|de] < bloco   -> graphviz (stdout);
                                       erros vão para stderr como AVISO
"""
import itertools
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fitch_check import parse  # noqa: E402

NEG = "~"
FALSO, VERD = ("at", "F"), ("at", "T")


def neg(f):
    return ("~", f)


# ------------------------------------------------------------ escrita
GREGAS = {"phi": "φ", "psi": "ψ", "delta": "δ", "gamma": "γ", "theta": "θ",
          "alpha": "α", "beta": "β", "sigma": "σ"}
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
PREC = {"<->": 1, "->": 2, "\\/": 3, "/\\": 4}
SIMB = {"<->": "↔", "->": "→", "\\/": "∨", "/\\": "∧"}


def atomo(a):
    m = re.match(r"([A-Za-z]+)(\d*)$", a)
    w, d = m.group(1), m.group(2)
    if w == "T":
        return "V"
    return GREGAS.get(w, w) + d.translate(SUB)


def uni(f, pai=None, lado=None):
    """Fórmula em Unicode, com os parêntesis mínimos."""
    if f[0] == "at":
        return atomo(f[1])
    if f[0] == "~":
        return "¬" + uni(f[1], "~")
    op = f[0]
    s = f"{uni(f[1], op, 'e')} {SIMB[op]} {uni(f[2], op, 'd')}"
    if pai is None:
        return s
    if pai == "~" or PREC[op] < PREC[pai]:
        return f"({s})"
    if PREC[op] == PREC[pai] and (op != pai or op in ("->", "<->")
                                   or lado == "d"):
        return f"({s})"
    return s


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ------------------------------------------------------------ tableaux
def componentes(f):
    """('alfa', [a1, a2]) | ('beta', [b1, b2]) | ('uno', [g]) | None."""
    if f[0] == "/\\":
        return "alfa", [f[1], f[2]]
    if f[0] == "\\/":
        return "beta", [f[1], f[2]]
    if f[0] == "->":
        return "beta", [neg(f[1]), f[2]]
    if f[0] == "~":
        g = f[1]
        if g[0] == "~":
            return "uno", [g[1]]
        if g == FALSO:
            return "uno", [VERD]
        if g == VERD:
            return "uno", [FALSO]
        if g[0] == "/\\":
            return "beta", [neg(g[1]), neg(g[2])]
        if g[0] == "\\/":
            return "alfa", [neg(g[1]), neg(g[2])]
        if g[0] == "->":
            return "alfa", [g[1], neg(g[2])]
    return None


def parse_tableau(text):
    """Devolve a lista de nós {n, f, just, pai, ramo_ini} (árvore)."""
    nos = []
    pilha = []          # por ramificação aberta: [nó onde ramifica, filhos]
    atual = None        # último nó do ramo corrente
    novo_ramo = False
    for raw in text.splitlines():
        s = raw.strip()
        if not s:
            continue
        if s == "[":
            pilha.append(atual)
            novo_ramo = True
            continue
        if s == "|":
            atual = pilha[-1]
            novo_ramo = True
            continue
        if s == "]":
            pilha.pop()
            atual = None    # nada pode continuar depois de "]"
            continue
        f_txt, _, j = s.partition(";")
        f_txt, j = f_txt.strip(), j.strip()
        n = len(nos) + 1
        if atual is None and nos:
            raise ValueError(f"nó {n}: depois de ']' o ramo já acabou")
        no = {"n": n, "txt": f_txt, "pai": atual, "ramo_ini": novo_ramo,
              "just": [int(x) for x in re.findall(r"\d+", j)]}
        no["f"] = None if f_txt == "x" else parse(f_txt)
        nos.append(no)
        atual = n
        novo_ramo = False
    if pilha:
        raise ValueError("falta ']'")
    return nos


def ramo(nos, n):
    """Números dos nós do ramo de n (da raiz até n, inclusive)."""
    out = []
    while n is not None:
        out.append(n)
        n = nos[n - 1]["pai"]
    return out[::-1]


def check_tableau(nos, seq=None, aberto=False):
    erros = []
    if not nos:
        return ["tableau vazio"]
    raiz = [no for no in nos if not no["just"] and no["f"] is not None]
    if seq is not None:
        if len(raiz) != 1 or raiz[0]["f"] != neg(parse(seq)):
            erros.append(f"a raiz tem de ser ¬({uni(parse(seq))})")
    filhos = {}
    for no in nos:
        filhos.setdefault(no["pai"], []).append(no["n"])
    for no in nos:
        n, js = no["n"], no["just"]
        r = ramo(nos, no["pai"]) if no["pai"] else []
        if no["f"] is None:          # fecho
            if len(js) != 2 or not all(j in r for j in js):
                erros.append(f"nó {n} (×): cita dois nós do próprio ramo")
                continue
            a, b = nos[js[0] - 1]["f"], nos[js[1] - 1]["f"]
            if not (a == neg(b) or b == neg(a)):
                erros.append(f"nó {n} (×): {uni(a)} e {uni(b)} não são ψ e ¬ψ")
            continue
        if not js:
            if any(nos[k - 1]["just"] for k in r):
                erros.append(f"nó {n}: falta a justificação")
            continue
        j = js[0]
        if j not in r:
            erros.append(f"nó {n}: o nó {j} não está no seu ramo")
            continue
        c = componentes(nos[j - 1]["f"])
        if c is None:
            erros.append(f"nó {n}: o nó {j} é um literal, não se expande")
            continue
        tipo, comps = c
        if tipo == "beta":
            irmaos = filhos[no["pai"]]
            ok = (no["ramo_ini"] and len(irmaos) == 2
                  and [nos[k - 1]["f"] for k in irmaos] == comps
                  and all(nos[k - 1]["just"] == [j] for k in irmaos))
            if not ok:
                erros.append(f"nó {n}: β de {j} tem de abrir dois ramos com "
                             f"{uni(comps[0])} | {uni(comps[1])}")
        elif no["f"] not in comps:
            erros.append(f"nó {n}: {uni(no['f'])} não é componente do nó {j}")
        elif no["ramo_ini"]:
            erros.append(f"nó {n}: a regra {tipo} não ramifica")
    folhas = [no for no in nos if no["n"] not in filhos]
    for fl in folhas:
        r = ramo(nos, fl["n"])
        for k in r:
            c = componentes(nos[k - 1]["f"]) if nos[k - 1]["f"] else None
            if c and c[0] == "alfa":
                usados = [nos[m - 1]["f"] for m in r if nos[m - 1]["just"] == [k]
                          and nos[m - 1]["f"] is not None]
                if usados and not all(x in usados for x in c[1]):
                    erros.append(f"ramo do nó {fl['n']}: a regra α de {k} "
                                 "acrescenta os dois componentes")
        if not aberto and fl["f"] is not None:
            erros.append(f"ramo do nó {fl['n']} não está fechado (falta 'x')")
    return sorted(set(erros), key=erros.index)


def dot_tableau(nos):
    out = ['graph T {', '  nodesep=0.25; ranksep=0.12; margin=0;',
           '  node [shape=plaintext, fontname="Charter", fontsize=13, '
           'height=0.22, margin="0.02,0.01"];',
           '  edge [color="#666666", penwidth=0.7];']
    for no in nos:
        n = no["n"]
        num = f'<font color="#888888" point-size="10">{n}</font>  '
        if no["f"] is None:
            i, k = (no["just"] + [0, 0])[:2]
            lab = (f'<font color="#b03030"><b>×</b></font>'
                   f'<font color="#888888" point-size="10"> ({i}, {k})</font>')
        else:
            j = f'<font color="#888888" point-size="10">  [{no["just"][0]}]</font>' \
                if no["just"] else ""
            lab = num + esc(uni(no["f"])) + j
        out.append(f'  n{n} [label=<{lab}>];')
        if no["pai"]:
            out.append(f'  n{no["pai"]} -- n{n};')
    out.append("}")
    return "\n".join(out)


# ------------------------------------------------------------ resolução
def lit(s):
    s = s.strip()
    return (False, s[1:].strip()) if s.startswith("~") else (True, s)


def lit_uni(l):
    return ("" if l[0] else "¬") + atomo(l[1])


def parse_resolucao(text):
    out = []
    for raw in text.splitlines():
        s = raw.strip()
        if not s:
            continue
        c, _, j = s.partition(";")
        c = c.strip()
        if c in ("F", "{}"):
            cl = frozenset()
        else:
            if not (c.startswith("{") and c.endswith("}")):
                raise ValueError(f"cláusula mal escrita: {c}")
            cl = frozenset(lit(x) for x in c[1:-1].split(",") if x.strip())
        out.append({"n": len(out) + 1, "c": cl, "txt": c,
                    "just": [int(x) for x in re.findall(r"\d+", j)]})
    return out


def resolventes(a, b):
    res = []
    for (s, p) in a:
        if (not s, p) in b:
            res.append((a - {(s, p)}) | (b - {(not s, p)}))
    return res


def avalia(f, v):
    t = f[0]
    if t == "at":
        return {"T": True, "F": False}.get(f[1], v.get(f[1]))
    if t == "~":
        return not avalia(f[1], v)
    a, b = avalia(f[1], v), avalia(f[2], v)
    return {"/\\": a and b, "\\/": a or b, "->": (not a) or b,
            "<->": a == b}[t]


def atomos(f, acc):
    if f[0] == "at":
        if f[1] not in ("T", "F"):
            acc.add(f[1])
    else:
        for g in f[1:]:
            atomos(g, acc)
    return acc


def check_resolucao(cls, de=None):
    erros = []
    for c in cls:
        if not c["just"]:
            continue
        if len(c["just"]) != 2 or not all(1 <= j < c["n"] for j in c["just"]):
            erros.append(f"linha {c['n']}: cita duas linhas anteriores")
            continue
        a, b = (cls[j - 1]["c"] for j in c["just"])
        if c["c"] not in resolventes(a, b):
            erros.append(f"linha {c['n']}: {c['txt']} não é resolvente das "
                         f"linhas {c['just'][0]} e {c['just'][1]}")
    if not cls or cls[-1]["c"]:
        erros.append("a última linha tem de ser F")
    if de is not None:
        phi = parse(de)
        prem = [c["c"] for c in cls if not c["just"]]
        ats = sorted(atomos(phi, set()) | {p for c in prem for _, p in c})
        for vals in itertools.product([True, False], repeat=len(ats)):
            v = dict(zip(ats, vals))
            sat = all(any(v[p] == s for s, p in c) for c in prem)
            if sat != (not avalia(phi, v)):
                erros.append("as cláusulas não são equivalentes a ¬φ "
                             f"(ex.: {v})")
                break
    return erros


def dot_resolucao(cls):
    usados, pilha = set(), [len(cls)]
    while pilha:
        n = pilha.pop()
        if n in usados:
            continue
        usados.add(n)
        pilha += cls[n - 1]["just"]
    out = ['digraph R {', '  nodesep=0.3; ranksep=0.3; margin=0;',
           '  node [shape=plaintext, fontname="Charter", fontsize=13, '
           'height=0.22, margin="0.02,0.01"];',
           '  edge [color="#666666", penwidth=0.7, arrowsize=0.5];']
    for c in cls:
        if c["n"] not in usados:
            continue
        num = f'<font color="#888888" point-size="10">{c["n"]}</font>  '
        if c["c"]:
            corpo = "{" + ", ".join(lit_uni(l) for l in sorted(
                c["c"], key=lambda l: (l[1], not l[0]))) + "}"
            lab = num + esc(corpo)
        else:
            lab = num + '<font color="#b03030"><b>F</b></font>'
        out.append(f'  c{c["n"]} [label=<{lab}>];')
        for j in c["just"]:
            out.append(f'  c{j} -> c{c["n"]};')
    out.append("}")
    return "\n".join(out)


# ------------------------------------------------------------ CLI
def processa(tipo, corpo, attr=None, aberto=False):
    if tipo == "tableau":
        nos = parse_tableau(corpo)
        return check_tableau(nos, attr, aberto), dot_tableau(nos)
    cls = parse_resolucao(corpo)
    return check_resolucao(cls, attr), dot_resolucao(cls)


BLOCO = re.compile(r"^```\{([^}]*\.(tableau|resolucao)[^}]*)\}\n(.*?)^```",
                   re.M | re.S)


def main(argv):
    if argv and argv[0] == "dot":
        tipo = argv[1]
        attr = argv[2] if len(argv) > 2 and argv[2] else None
        aberto = len(argv) > 3 and argv[3] == "aberto"
        corpo = sys.stdin.read()
        try:
            erros, dot = processa(tipo, corpo, attr, aberto)
        except ValueError as e:
            erros, dot = [str(e)], 'graph E { erro [label="erro"]; }'
        for e in erros:
            print(f"AVISO ({tipo} ERRADO, a começar em "
                  f"'{corpo.strip().splitlines()[0]}'): {e}", file=sys.stderr)
        print(dot)
        return 0
    paths = argv[1:] if argv and argv[0] == "check" else argv
    total = falhas = 0
    for p in paths:
        src = open(p, encoding="utf-8").read()
        for m in BLOCO.finditer(src):
            attrs, tipo, corpo = m.groups()
            total += 1
            a = re.search(r'(?:seq|de)="([^"]*)"', attrs)
            try:
                erros, _ = processa(tipo, corpo, a.group(1).replace("\\\\", "\\")
                                    if a else None, ".aberto" in attrs)
            except ValueError as e:
                erros = [str(e)]
            if erros:
                falhas += 1
                print(f"{p}:{src[:m.start()].count(chr(10)) + 1}: {tipo} ERRADO")
                for e in erros:
                    print("   ", e)
    print(f"{total} tableaux/resoluções verificados, {falhas} com erros.")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
