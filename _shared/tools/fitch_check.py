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

1.ª ordem: AI AE EI EE =I =E. A caixa de ∀I/∃E abre com a variável nova,
"|> [v] ...", e o verificador confirma que v não ocorre antes (nas linhas
acessíveis) nem na conclusão, e que não há captura de variáveis. Sintaxe
completa no fitch.lua.
"""
import re
import sys

# ---------------------------------------------------------------- fórmulas
# Lógica de 1.ª ordem (Aula 14): "forall x phi", "exists x phi", termos
# f(x, a), predicados P(x, y), "t1 = t2", "t1 != t2" e substituição em
# sufixo "phi[v/x]" (aplicada logo ao ler). Letras gregas são metavariáveis;
# o atributo naolivre="psi:x" diz que x não ocorre livre em psi.
TOK = re.compile(r"\s*(<->|->|/\\|\\/|!=|=|~|\(|\)|\[|\]|/|,|[A-Za-z]+\d*)")
IDENT = re.compile(r"^[A-Za-z]+\d*$")
METAS = {"phi", "psi", "gamma", "theta", "delta", "alpha", "beta", "sigma"}
NAOLIVRE = {}


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


def V(n):
    return ("t", n, ())


def names_t(u):
    out = {u[1]}
    for a in u[2]:
        out |= names_t(a)
    return out


def terms_of(f):
    """Todos os termos (e subtermos) que aparecem em f."""
    out = set()

    def addt(u):
        out.add(u)
        for a in u[2]:
            addt(a)
    k = f[0]
    if k == "pred":
        for a in f[2]:
            addt(a)
    elif k == "=":
        addt(f[1]); addt(f[2])
    elif k == "~":
        out |= terms_of(f[1])
    elif k in ("A", "E"):
        out |= terms_of(f[2])
    elif k == "meta":
        for t, _ in f[2]:
            addt(t)
    elif k != "at":
        out |= terms_of(f[1]) | terms_of(f[2])
    return out


def names(f):
    """Todos os nomes (variáveis, constantes, funções) usados em termos de f."""
    out = set()
    for u in terms_of(f):
        out |= names_t(u)
    if f[0] in ("A", "E"):
        out.add(f[1])
    if f[0] in ("~", "A", "E"):
        out |= names(f[-1])
    elif f[0] in ("->", "<->", "/\\", "\\/"):
        out |= names(f[1]) | names(f[2])
    elif f[0] == "meta":
        out |= {x for _, x in f[2]}
    return out


def free_in(f, x):
    k = f[0]
    if k == "at":
        return False
    if k == "pred":
        return any(x in names_t(a) for a in f[2])
    if k == "=":
        return x in names_t(f[1]) or x in names_t(f[2])
    if k == "~":
        return free_in(f[1], x)
    if k in ("A", "E"):
        return f[1] != x and free_in(f[2], x)
    if k == "meta":
        return meta_livre(f[1], f[2], x)
    return free_in(f[1], x) or free_in(f[2], x)


def meta_livre(n, subs, x):
    if not subs:
        return x not in NAOLIVRE.get(n, set())
    t, y = subs[-1]
    ant = subs[:-1]
    if y == x:
        return x in names_t(t) and meta_livre(n, ant, y)
    return meta_livre(n, ant, x) or (x in names_t(t) and meta_livre(n, ant, y))


def tsub(u, x, t):
    if not u[2] and u[1] == x:
        return t
    return ("t", u[1], tuple(tsub(a, x, t) for a in u[2]))


def subst(f, x, t):
    """f[t/x]; erro se x não for substituível por t em f."""
    if t == V(x) or not free_in(f, x):
        return f
    k = f[0]
    if k == "pred":
        return ("pred", f[1], tuple(tsub(a, x, t) for a in f[2]))
    if k == "=":
        return ("=", tsub(f[1], x, t), tsub(f[2], x, t))
    if k == "~":
        return ("~", subst(f[1], x, t))
    if k in ("A", "E"):
        if f[1] in names_t(t):
            raise ValueError(f"{x} não é substituível por {show_t(t)}: {f[1]} ficaria ligada")
        return (k, f[1], subst(f[2], x, t))
    if k == "meta":
        return ("meta", f[1], f[2] + ((t, x),))
    return (k, subst(f[1], x, t), subst(f[2], x, t))


def inst(phi, x, g):
    """Há um termo t com phi[t/x] == g?"""
    for t in terms_of(g) | {V(x)}:
        try:
            if subst(phi, x, t) == g:
                return True
        except ValueError:
            pass
    return False


def rep(a, b, t1, t2):
    """b obtém-se de a trocando algumas ocorrências do termo t1 por t2."""
    if a == b:
        return True
    if a[0] == "t":
        if a == t1 and b == t2:
            return True
        return (b[0] == "t" and a[1] == b[1] and len(a[2]) == len(b[2])
                and all(rep(p, q, t1, t2) for p, q in zip(a[2], b[2])))
    if a[0] != b[0]:
        return False
    k = a[0]
    if k == "pred":
        return a[1] == b[1] and len(a[2]) == len(b[2]) and all(
            rep(p, q, t1, t2) for p, q in zip(a[2], b[2]))
    if k == "=":
        return rep(a[1], b[1], t1, t2) and rep(a[2], b[2], t1, t2)
    if k == "~":
        return rep(a[1], b[1], t1, t2)
    if k in ("A", "E"):
        return a[1] == b[1] and rep(a[2], b[2], t1, t2)
    if k == "meta":
        return a[1] == b[1] and len(a[2]) == len(b[2]) and all(
            y1 == y2 and rep(p, q, t1, t2) for (p, y1), (q, y2) in zip(a[2], b[2]))
    if k == "at":
        return False
    return rep(a[1], b[1], t1, t2) and rep(a[2], b[2], t1, t2)


def parse(s):
    t = tokens(s)
    i = 0

    def peek():
        return t[i] if i < len(t) else None

    def eat(x=None):
        nonlocal i
        if i >= len(t):
            raise ValueError(f"a fórmula '{s}' acaba cedo demais")
        tok = t[i]
        if x and tok != x:
            raise ValueError(f"esperava {x} em '{s}'")
        i += 1
        return tok

    def ident():
        n = eat()
        if not IDENT.match(n):
            raise ValueError(f"esperava um nome em '{s}' e vi '{n}'")
        return n

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

    def term():
        n = ident()
        args = []
        if peek() == "(":
            eat()
            args.append(term())
            while peek() == ",":
                eat()
                args.append(term())
            eat(")")
        return ("t", n, tuple(args))

    def postfix(a):
        while peek() == "[":
            eat()
            u = term()
            eat("/")
            x = ident()
            eat("]")
            a = subst(a, x, u)
        return a

    def neg():
        p = peek()
        if p == "~":
            eat()
            return ("~", neg())
        if p in ("forall", "exists"):
            eat()
            x = ident()
            return ("A" if p == "forall" else "E", x, neg())
        if p == "(":
            eat()
            a = iff()
            eat(")")
            return postfix(a)
        u = term()
        if peek() in ("=", "!="):
            op = eat()
            a = ("=", u, term())
            return ("~", a) if op == "!=" else a
        _, n, args = u
        if args:
            a = ("pred", n, args)
        elif re.sub(r"\d+$", "", n) in METAS:
            a = ("meta", n, ())
        else:
            a = ("at", n)
        return postfix(a)

    f = iff()
    if i != len(t):
        raise ValueError(f"sobra texto na fórmula '{s}'")
    return f


def show_t(u):
    return u[1] + (f"({', '.join(show_t(a) for a in u[2])})" if u[2] else "")


def show(f):
    k = f[0]
    if k == "at":
        return f[1]
    if k == "pred":
        return f"{f[1]}({', '.join(show_t(a) for a in f[2])})"
    if k == "=":
        return f"{show_t(f[1])} = {show_t(f[2])}"
    if k == "meta":
        return f[1] + "".join(f"[{show_t(t)}/{x}]" for t, x in f[2])
    if k == "~":
        return "~" + show(f[1])
    if k in ("A", "E"):
        return ("forall " if k == "A" else "exists ") + f[1] + " " + show(f[2])
    return f"({show(f[1])} {f[0]} {show(f[2])})"


FALSO = ("at", "F")

# ---------------------------------------------------------------- deduções


def parse_block(text):
    """Linhas da dedução. "|> [v]" sozinho (sem fórmula) abre a caixa da
    variável v na linha seguinte, que pode abrir mais caixas lá dentro."""
    linhas, pendentes = [], []
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
        var = None
        m = re.match(r"^\s*\[([A-Za-z]+\d*)\]\s*", f)
        if m:
            if not nova:
                raise ValueError(f"'{f.strip()}': a variável nova [v] só pode abrir uma sub-dedução")
            var, f = m.group(1), f[m.end():]
            if not f.strip() and not j.strip():
                pendentes.append((nivel, var))
                continue
        linhas.append(dict(nivel=nivel, nova=nova, sub=nova, var=var, abre=pendentes,
                           f=parse(f), txt=f.strip(), just=j.strip()))
        pendentes = []
    if pendentes:
        raise ValueError("[v] sozinho no fim da dedução")
    return linhas


def check(linhas):
    """Devolve lista de erros (vazia se a dedução está correta)."""
    erros = []
    n = len(linhas)
    # caixa = dict(ini, fim, nivel, var, hip); índices 1-based
    caixas = []
    pilha = []
    premissas_fim = 0
    for k, l in enumerate(linhas, 1):
        abre = [dict(ini=k, nivel=nv, var=v, hip=False) for nv, v in l["abre"]]
        if l["nova"]:
            abre.append(dict(ini=k, nivel=l["nivel"], var=l["var"], hip=not l["just"]))
        limite = abre[0]["nivel"] if abre else l["nivel"] + 1
        while pilha and (l["nivel"] < pilha[-1]["nivel"] or limite <= pilha[-1]["nivel"]):
            c = pilha.pop()
            c["fim"] = k - 1
            caixas.append(c)
        for c in abre:
            if c["nivel"] != (pilha[-1]["nivel"] + 1 if pilha else 1):
                erros.append(f"linha {k}: sub-dedução aberta ao nível errado")
            pilha.append(c)
        if pilha and l["nivel"] != pilha[-1]["nivel"]:
            erros.append(f"linha {k}: nível de indentação não bate certo")
        elif not pilha and l["nivel"] != 0:
            erros.append(f"linha {k}: linha indentada sem sub-dedução aberta")
    for c in pilha:
        c["fim"] = n
        caixas.append(c)
    if any(l["nivel"] for l in linhas[-1:]):
        erros.append("a última linha não está na dedução principal")
    # premissas = linhas iniciais de nível 0 até ao '---' (ou só as sem justificação)
    for k, l in enumerate(linhas, 1):
        if l["nivel"] == 0 and not l["just"] and not l["nova"]:
            premissas_fim = k
        else:
            break

    def caixas_de(k):
        return [c for c in caixas if c["ini"] <= k <= c["fim"]]

    def acessivel(a, k):
        # a linha a é acessível de k se a < k e toda a caixa que contém a contém k
        return 1 <= a < k and all(c["ini"] <= k <= c["fim"] for c in caixas_de(a))

    def caixa(rng, k):
        i, j = rng
        cs = [c for c in caixas if (c["ini"], c["fim"]) == (i, j)]
        if not cs:
            raise ValueError(f"{i}-{j} não é uma sub-dedução completa")
        c = cs[0]
        # tem de estar imediatamente dentro do contexto de k e já fechada
        if not j < k:
            raise ValueError(f"sub-dedução {i}-{j} ainda não fechou")
        fora = [d for d in caixas if d["nivel"] < c["nivel"] and d["ini"] <= i and d["fim"] >= j]
        if not all(d["ini"] <= k <= d["fim"] for d in fora):
            raise ValueError(f"sub-dedução {i}-{j} não é acessível")
        if linhas[k - 1]["nivel"] != c["nivel"] - 1:
            raise ValueError(f"sub-dedução {i}-{j} não está logo dentro desta linha")
        return (linhas[i - 1]["f"] if c["hip"] else None), linhas[j - 1]["f"], c

    def neg(f):
        return ("~", f)

    for k, l in enumerate(linhas, 1):
        f, j = l["f"], l["just"]
        if (l["nova"] and not (l["var"] and j)) or (k <= premissas_fim):
            if j:
                erros.append(f"linha {k}: hipótese/premissa não leva justificação")
            continue
        try:
            m = re.match(r"^(~~I|->I|->E|&I|&E|vI|vE|~I|~E|FI|FE|MT|RA|TE|AI|AE|EI|EE|=I|=E|R)\s*,?\s*(.*)$", j)
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
            elif regra == "AE":
                need(1, 0)
                q = L[0]
                ok = q[0] == "A" and inst(q[2], q[1], f)
            elif regra == "EI":
                need(1, 0)
                ok = f[0] == "E" and inst(f[2], f[1], L[0])
            elif regra in ("AI", "EE"):
                need(0, 1) if regra == "AI" else need(1, 1)
                hyp, ult, cx = C[0]
                ini, v = cx["ini"], cx["var"]
                if not v:
                    raise ValueError(f"a sub-dedução de {regra} tem de abrir com a variável nova: |> [v] ...")
                for a in range(1, ini):
                    if acessivel(a, ini) and v in names(linhas[a - 1]["f"]):
                        raise ValueError(f"{v} não é nova: já ocorre na linha {a}")
                if v in names(f):
                    raise ValueError(f"{v} não pode ocorrer na conclusão {show(f)}")
                tem_hip = cx["hip"]
                if regra == "AI":
                    if tem_hip:
                        raise ValueError("a sub-dedução de AI não tem hipótese (a 1.ª linha leva justificação)")
                    ok = f[0] == "A" and ult == subst(f[2], f[1], V(v))
                else:
                    q = L[0]
                    if v in names(q):
                        raise ValueError(f"{v} não é nova: ocorre em {show(q)}")
                    ok = (tem_hip and q[0] == "E" and hyp == subst(q[2], q[1], V(v))
                          and ult == f)
            elif regra == "=I":
                need(0, 0)
                ok = f[0] == "=" and f[1] == f[2]
            elif regra == "=E":
                need(2, 0)
                ok = any(e[0] == "=" and rep(o, f, e[1], e[2])
                         for e, o in ((L[0], L[1]), (L[1], L[0])))
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
            NAOLIVRE.clear()
            nl = re.search(r'naolivre="([^"]*)"', attrs)
            for item in (nl.group(1).split() if nl else []):
                meta, vs = item.split(":")
                NAOLIVRE[meta] = set(vs.split(","))
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
