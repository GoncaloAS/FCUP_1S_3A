#!/usr/bin/env python3
"""Verifica as deduções em notação de Fitch (blocos ```{.fitch}) de um .md.

Uso: python3 _shared/tools/fitch_check.py Logica/.fonte/*.md

Para cada bloco confirma que cada linha é uma premissa, uma hipótese de uma
sub-dedução, ou resulta das linhas que cita pela regra que diz, e que só cita
linhas ainda acessíveis (não de sub-deduções já fechadas). Se o bloco tiver
o atributo seq="premissas |- conclusão", confirma também as premissas e a
conclusão. Blocos com a classe .nocheck são ignorados. A sintaxe está
descrita em _shared/template/fitch.lua.

Regras derivadas aceites (só usar quando o enunciado o permite, e provando-as
à parte): MT, RA, TE, ~~I.
"""
import re
import sys

# ---------------------------------------------------------------- fórmulas
TOK = re.compile(r"\s*(<->|->|/\\|\\/|~|\(|\)|[A-Za-z]+\d*)")


def tokens(s):
    pos, out = 0, []
    s = s.strip()
    while pos < len(s):
        m = TOK.match(s, pos)
        if not m:
            raise ValueError(f"não percebo a fórmula '{s}' na posição {pos}")
        out.append(m.group(1))
        pos = m.end()
        while pos < len(s) and s[pos].isspace():
            pos += 1
    return out


def parse(s):
    t = tokens(s)
    i = 0

    def peek():
        return t[i] if i < len(t) else None

    def eat(x=None):
        nonlocal i
        tok = t[i]
        if x and tok != x:
            raise ValueError(f"esperava {x} em '{s}'")
        i += 1
        return tok

    def iff():
        a = imp()
        while peek() == "<->":
            eat()
            a = ("<->", a, imp())
        return a

    def imp():
        a = disj()
        if peek() == "->":
            eat()
            return ("->", a, imp())  # associa à direita
        return a

    def disj():
        a = conj()
        while peek() == "\\/":
            eat()
            a = ("\\/", a, conj())
        return a

    def conj():
        a = neg()
        while peek() == "/\\":
            eat()
            a = ("/\\", a, neg())
        return a

    def neg():
        if peek() == "~":
            eat()
            return ("~", neg())
        if peek() == "(":
            eat()
            a = iff()
            eat(")")
            return a
        return ("at", eat())

    f = iff()
    if i != len(t):
        raise ValueError(f"sobra texto na fórmula '{s}'")
    return f


def show(f):
    if f[0] == "at":
        return f[1]
    if f[0] == "~":
        return "~" + show(f[1])
    return f"({show(f[1])} {f[0]} {show(f[2])})"


FALSO = ("at", "F")

# ---------------------------------------------------------------- deduções


def parse_block(text):
    linhas = []
    for raw in text.splitlines():
        s = raw.rstrip()
        if not s.strip():
            continue
        m = re.match(r"^[|\s]*", s)
        barras = m.group(0)
        nivel = barras.count("|")
        resto = s[len(barras):]
        if resto.startswith("---"):
            linhas[-1]["sub"] = True
            continue
        nova = resto.startswith(">")
        if nova:
            resto = resto[1:]
        if ";" in resto:
            f, j = resto.split(";", 1)
        else:
            f, j = resto, ""
        linhas.append(dict(nivel=nivel, nova=nova, sub=nova,
                           f=parse(f), txt=f.strip(), just=j.strip()))
    return linhas


def check(linhas):
    """Devolve lista de erros (vazia se a dedução está correta)."""
    erros = []
    n = len(linhas)
    # estrutura: cada linha pertence a uma caixa; caixa = (início, fim, nivel)
    caixas = []  # (ini, fim) de cada sub-dedução, índices 1-based
    pilha = []   # caixas abertas: [ini, nivel]
    premissas_fim = 0
    for k, l in enumerate(linhas, 1):
        while pilha and (l["nivel"] < pilha[-1][1] or (l["nova"] and l["nivel"] == pilha[-1][1])):
            ini, _ = pilha.pop()
            caixas.append((ini, k - 1))
        if l["nova"]:
            if l["nivel"] != (pilha[-1][1] + 1 if pilha else 1):
                erros.append(f"linha {k}: sub-dedução aberta ao nível errado")
            pilha.append([k, l["nivel"]])
        elif pilha and l["nivel"] != pilha[-1][1]:
            erros.append(f"linha {k}: nível de indentação não bate certo")
        elif not pilha and l["nivel"] != 0:
            erros.append(f"linha {k}: linha indentada sem sub-dedução aberta")
    for ini, _ in pilha:
        caixas.append((ini, n))
    if any(l["nivel"] for l in linhas[-1:]):
        erros.append("a última linha não está na dedução principal")
    # premissas = linhas iniciais de nível 0 até ao '---' (ou só as sem justificação)
    for k, l in enumerate(linhas, 1):
        if l["nivel"] == 0 and not l["just"] and not l["nova"]:
            premissas_fim = k
        else:
            break

    def caixas_de(k):
        return [c for c in caixas if c[0] <= k <= c[1]]

    def acessivel(a, k):
        # a linha a é acessível de k se a < k e toda a caixa que contém a contém k
        return 1 <= a < k and all(c[0] <= k <= c[1] for c in caixas_de(a))

    def caixa(rng, k):
        i, j = rng
        if (i, j) not in caixas:
            raise ValueError(f"{i}-{j} não é uma sub-dedução completa")
        # tem de estar imediatamente dentro do contexto de k e já fechada
        if not j < k:
            raise ValueError(f"sub-dedução {i}-{j} ainda não fechou")
        fora = [c for c in caixas if c[0] < i and c[1] >= j]
        if not all(c[0] <= k <= c[1] for c in fora):
            raise ValueError(f"sub-dedução {i}-{j} não é acessível")
        if linhas[k - 1]["nivel"] != linhas[i - 1]["nivel"] - 1:
            raise ValueError(f"sub-dedução {i}-{j} não está logo dentro desta linha")
        return linhas[i - 1]["f"], linhas[j - 1]["f"]

    def neg(f):
        return ("~", f)

    for k, l in enumerate(linhas, 1):
        f, j = l["f"], l["just"]
        if l["nova"] or (k <= premissas_fim):
            if j:
                erros.append(f"linha {k}: hipótese/premissa não leva justificação")
            continue
        try:
            m = re.match(r"^(~~I|->I|->E|&I|&E|vI|vE|~I|~E|FI|FE|R|MT|RA|TE)\s*,?\s*(.*)$", j)
            if not m:
                raise ValueError(f"regra desconhecida '{j}'")
            regra, args = m.group(1), [a.strip() for a in m.group(2).split(",") if a.strip()]
            linhas_ref, caixas_ref = [], []
            for a in args:
                if "-" in a:
                    i1, i2 = a.split("-")
                    caixas_ref.append(caixa((int(i1), int(i2)), k))
                else:
                    a = int(a)
                    if not acessivel(a, k):
                        raise ValueError(f"linha {a} não é acessível daqui")
                    linhas_ref.append(linhas[a - 1]["f"])
            L, C = linhas_ref, caixas_ref

            def need(nl, nc):
                if len(L) != nl or len(C) != nc:
                    raise ValueError(f"{regra} precisa de {nl} linha(s) e {nc} sub-dedução(ões)")

            ok = False
            if regra == "&I":
                need(2, 0)
                ok = f[0] == "/\\" and (f[1:] == (L[0], L[1]) or f[1:] == (L[1], L[0]))
            elif regra == "&E":
                need(1, 0)
                ok = L[0][0] == "/\\" and f in L[0][1:]
            elif regra == "vI":
                need(1, 0)
                ok = f[0] == "\\/" and L[0] in f[1:]
            elif regra == "vE":
                need(1, 2)
                d = L[0]
                ok = (d[0] == "\\/" and C[0][0] == d[1] and C[1][0] == d[2]
                      and C[0][1] == f and C[1][1] == f)
            elif regra == "~I":
                need(0, 1)
                ok = C[0][1] == FALSO and f == neg(C[0][0])
            elif regra == "~E":
                need(1, 0)
                ok = L[0] == neg(neg(f))
            elif regra == "FI":
                need(2, 0)
                ok = f == FALSO and (L[1] == neg(L[0]) or L[0] == neg(L[1]))
            elif regra == "FE":
                need(1, 0)
                ok = L[0] == FALSO
            elif regra == "->I":
                need(0, 1)
                ok = f == ("->", C[0][0], C[0][1])
            elif regra == "->E":
                need(2, 0)
                ok = L[1] == ("->", L[0], f) or L[0] == ("->", L[1], f)
            elif regra == "R":
                need(1, 0)
                ok = L[0] == f
            elif regra == "MT":
                need(2, 0)
                a, b = L
                ok = ((a[0] == "->" and b == neg(a[2]) and f == neg(a[1])) or
                      (b[0] == "->" and a == neg(b[2]) and f == neg(b[1])))
            elif regra == "RA":
                need(0, 1)
                ok = C[0][1] == FALSO and C[0][0] == neg(f)
            elif regra == "TE":
                need(0, 0)
                ok = f[0] == "\\/" and f[2] == neg(f[1])
            elif regra == "~~I":
                need(1, 0)
                ok = f == neg(neg(L[0]))
            if not ok:
                raise ValueError(f"{regra} não dá {show(f)} a partir do que cita")
        except (ValueError, IndexError) as e:
            erros.append(f"linha {k} ({l['txt']}; {j}): {e}")
    return erros, linhas[:premissas_fim], linhas[-1]["f"] if linhas else None


BLOCO = re.compile(r"^```\{([^}]*\.fitch[^}]*)\}\n(.*?)^```", re.M | re.S)


def main(paths):
    total = falhas = 0
    for p in paths:
        src = open(p, encoding="utf-8").read()
        for m in BLOCO.finditer(src):
            attrs, body = m.group(1), m.group(2)
            linha_md = src[:m.start()].count("\n") + 1
            if ".nocheck" in attrs:
                continue
            total += 1
            try:
                linhas = parse_block(body)
                erros, prem, concl = check(linhas)
                seq = re.search(r'seq="([^"]*)"', attrs)
                if seq:
                    esq, dir_ = seq.group(1).split("|-")
                    esperadas = [parse(x) for x in split_top(esq)]
                    if [l["f"] for l in prem] != esperadas:
                        erros.append("as premissas não são as do enunciado (seq=...)")
                    if concl != parse(dir_):
                        erros.append(f"a conclusão {show(concl)} não é a do enunciado")
            except ValueError as e:
                erros = [str(e)]
            if erros:
                falhas += 1
                print(f"{p}:{linha_md}: dedução ERRADA")
                for e in erros:
                    print("   ", e)
    print(f"{total} deduções verificadas, {falhas} com erros.")
    return 1 if falhas else 0


def split_top(s):
    """Parte 'a, b, c' por vírgulas fora de parênteses."""
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == "," and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return [x for x in out if x.strip()]


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
