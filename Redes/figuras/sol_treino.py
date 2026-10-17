#!/usr/bin/env python3
"""Figuras das soluções dos exercícios de treino de diagramas (C2.7 e C2.8), em SVG sem dependências.

  sol_c27_http_msc.svg   MSC de HTTP não persistente: HTML + 2 imagens, uma conexão TCP por objeto
  sol_c28_dns.svg        setas DNS de www.publico.pt: (a) local iterativo, (b) tudo recursivo

Uso: python3 Redes/figuras/sol_treino.py   (escreve ao lado deste ficheiro)
"""
from pathlib import Path

AQUI = Path(__file__).resolve().parent
FONTE = "font-family:Helvetica,Arial,sans-serif"
LARANJA = "#f58518"


def svg(w, h, corpo):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">\n'
            f'<defs><marker id="seta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#222"/></marker></defs>\n'
            f'<rect width="{w}" height="{h}" fill="#fff"/>\n{corpo}</svg>\n')


def texto(x, y, t, tam=11, ancora="middle", peso="normal", cor="#222"):
    # contorno branco por baixo: o rótulo lê-se mesmo por cima de uma linha
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{tam}" text-anchor="{ancora}" font-weight="{peso}" '
            f'fill="{cor}" stroke="#fff" stroke-width="3" paint-order="stroke" style="{FONTE}">{t}</text>\n')


def seta(x1, y1, x2, y2, rotulo="", lado=0, tam=10):
    s = (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#222" stroke-width="1.3" '
         f'marker-end="url(#seta)"/>\n')
    if rotulo:
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        s += texto(xm, ym - 4 + lado, rotulo, tam)
    return s


# ─────────────── C2.7: HTTP não persistente, 1 HTML (20 ms) + 2 imagens (40 ms), RTT = 40 ms ───────────────
def msc_http():
    E = 3.0            # px por ms
    y0, xc, xs = 50, 120, 330
    rtt, meio = 40, 20
    objetos = [("index.html", 20), ("img1", 40), ("img2", 40)]
    c = texto(xc, 30, "cliente", 12, peso="bold") + texto(xs, 30, "servidor", 12, peso="bold")
    total = sum(2 * rtt + t for _, t in objetos)
    yf = y0 + total * E + 20
    c += f'<line x1="{xc}" y1="{y0}" x2="{xc}" y2="{yf}" stroke="#222" stroke-width="2"/>\n'
    c += f'<line x1="{xs}" y1="{y0}" x2="{xs}" y2="{yf}" stroke="#222" stroke-width="2"/>\n'
    t0 = 0
    for nome, tr in objetos:
        y = lambda t: y0 + t * E
        # abrir a conexão (1 RTT), depois o pedido vai com o último ACK
        c += seta(xc, y(t0), xs, y(t0 + meio), "SYN")
        c += seta(xs, y(t0 + meio), xc, y(t0 + rtt), "SYN-ACK")
        c += seta(xc, y(t0 + rtt), xs, y(t0 + rtt + meio), f"ACK + GET {nome}")
        # resposta: faixa = tempo de transmissão
        a, b = t0 + rtt + meio, t0 + rtt + meio + tr
        c += (f'<polygon points="{xs},{y(a):.1f} {xs},{y(b):.1f} {xc},{y(b + meio):.1f} {xc},{y(a + meio):.1f}" '
              f'fill="{LARANJA}" fill-opacity="0.45" stroke="{LARANJA}"/>\n')
        c += texto((xc + xs) / 2, (y(a) + y(b + meio)) / 2 + 4, f"{nome} ({tr} ms)", 10)
        fim = t0 + 2 * rtt + tr
        # chaveta à esquerda com o custo do objeto
        c += f'<line x1="{xc - 14}" y1="{y(t0):.1f}" x2="{xc - 14}" y2="{y(fim):.1f}" stroke="#555" stroke-width="1"/>\n'
        c += f'<line x1="{xc - 18}" y1="{y(t0):.1f}" x2="{xc - 10}" y2="{y(t0):.1f}" stroke="#555"/>\n'
        c += f'<line x1="{xc - 18}" y1="{y(fim):.1f}" x2="{xc - 10}" y2="{y(fim):.1f}" stroke="#555"/>\n'
        c += texto(xc - 22, (y(t0) + y(fim)) / 2 - 2, f"2 RTT + {tr}", 10, "end")
        c += texto(xc - 22, (y(t0) + y(fim)) / 2 + 11, f"= {2 * rtt + tr} ms", 10, "end")
        c += texto(xs + 8, y(fim) + 4, f"{fim} ms", 10, "start", cor="#555")
        t0 = fim
    c += texto((xc + xs) / 2, yf + 4, f"total: {total} ms (6 RTT + 100 ms)", 11, peso="bold")
    return svg(430, int(yf + 16), c)


# ─────────────── C2.8: www.publico.pt, caches vazias ───────────────
def dns():
    nomes = ["cliente", "servidor\nlocal", "raiz", "TLD pt", "autoridade\npublico.pt"]
    xs = [45, 155, 265, 375, 485]
    paineis = [
        ("(a) local recursivo para o cliente, iterativo para fora", [
            (0, 1, "1 A www.publico.pt?"), (1, 2, "2 a mesma pergunta"), (2, 1, "3 NS de pt"),
            (1, 3, "4 a mesma pergunta"), (3, 1, "5 NS de publico.pt"), (1, 4, "6 a mesma pergunta"),
            (4, 1, "7 A = IP"), (1, 0, "8 A = IP")]),
        ("(b) tudo recursivo (não se usa)", [
            (0, 1, "1 A www.publico.pt?"), (1, 2, "2"), (2, 3, "3"), (3, 4, "4"),
            (4, 3, "5 A = IP"), (3, 2, "6 A = IP"), (2, 1, "7 A = IP"), (1, 0, "8 A = IP")]),
    ]
    c, y = "", 10
    passo = 26
    for titulo, msgs in paineis:
        c += texto(10, y + 14, titulo, 12, "start", "bold")
        y += 30
        for x, n in zip(xs, nomes):
            for k, linha in enumerate(n.split("\n")):
                c += texto(x, y + 10 + 12 * k, linha, 10, peso="bold")
        y += 30
        topo, fundo = y, y + passo * len(msgs) + 6
        for x in xs:
            c += f'<line x1="{x}" y1="{topo}" x2="{x}" y2="{fundo}" stroke="#222" stroke-width="2"/>\n'
        for i, (a, b, r) in enumerate(msgs):
            ya = topo + 8 + passo * i
            c += seta(xs[a], ya, xs[b], ya + passo - 8, r, tam=9)
        y = fundo + 20
    return svg(540, int(y), c)


(AQUI / "sol_c27_http_msc.svg").write_text(msc_http())
(AQUI / "sol_c28_dns.svg").write_text(dns())
print("sol_c27_http_msc.svg, sol_c28_dns.svg")
