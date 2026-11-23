"""Figuras dos capítulos 3 e 4 (matplotlib). Correr a partir de Redes/:
uv run -q --with matplotlib python -I figuras/src/transporte.py"""
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10})
OUT = "figuras/"
AZ, VM, CZ = "#1f4e9c", "#b3261e", "#555555"


def msc(ax, titulo, xs, xr, tmax, eventos, notas_e=(), notas_r=(), pos=0.22):
    """eventos: (t0, t1, rótulo, de_emissor, perdido, cor)"""
    ax.set_xlim(-0.2, 1.2); ax.set_ylim(tmax + 0.3, -0.9); ax.axis("off")
    for x, n in ((xs, "emissor"), (xr, "receptor")):
        ax.plot([x, x], [-0.3, tmax], color="black", lw=1.2)
        ax.text(x, -0.55, n, ha="center", fontsize=10, weight="bold")
    ax.set_title(titulo, fontsize=10.5, weight="bold")
    for t0, t1, lab, de_e, perdido, cor in eventos:
        a, b = (xs, xr) if de_e else (xr, xs)
        if perdido:
            fim = a + (b - a) * 0.55; tf = t0 + (t1 - t0) * 0.55
            ax.annotate("", xy=(fim, tf), xytext=(a, t0),
                        arrowprops=dict(arrowstyle="-", color=cor, lw=1.3))
            ax.text(fim, tf, "✕", color=VM, ha="center", va="center", fontsize=13, weight="bold")
        else:
            ax.annotate("", xy=(b, t1), xytext=(a, t0),
                        arrowprops=dict(arrowstyle="-|>", color=cor, lw=1.3, mutation_scale=10))
        xm = a + (b - a) * pos; tm = t0 + (t1 - t0) * pos
        ax.text(xm, tm - 0.12, lab, color=cor, fontsize=9, ha="center", va="bottom",
                bbox=dict(fc="white", ec="none", pad=0.4))
    for t, txt in notas_e:
        ax.text(xs - 0.04, t, txt, ha="right", va="center", fontsize=8.5, color=CZ)
    for t, txt in notas_r:
        ax.text(xr + 0.04, t, txt, ha="left", va="center", fontsize=8.5, color=CZ)


def gbn_sr():
    D = 2.0  # tempo de viagem
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 6.2))
    # Go-Back-N, N = 4 (slide 52)
    ev = [(0, D, "pkt0", 1, 0, AZ), (0.5, 0.5 + D, "pkt1", 1, 0, AZ), (1, 1 + D, "pkt2", 1, 1, AZ),
          (1.5, 1.5 + D, "pkt3", 1, 0, AZ),
          (D, 2 * D, "ACK0", 0, 0, CZ), (2.5, 4.5, "ACK1", 0, 0, CZ), (3.5, 5.5, "ACK1", 0, 0, CZ),
          (4, 6, "pkt4", 1, 0, AZ), (4.5, 6.5, "pkt5", 1, 0, AZ),
          (6, 8, "ACK1", 0, 0, CZ), (6.5, 8.5, "ACK1", 0, 0, CZ),
          (7, 9, "pkt2", 1, 0, VM), (7.5, 9.5, "pkt3", 1, 0, VM), (8, 10, "pkt4", 1, 0, VM), (8.5, 10.5, "pkt5", 1, 0, VM),
          (9, 11, "ACK2", 0, 0, CZ), (9.5, 11.5, "ACK3", 0, 0, CZ)]
    msc(axs[0], "Go-Back-N (N = 4): perde-se o pkt2", 0.15, 0.85, 12, ev,
        notas_e=[(4, "ACK0 → envia pkt4"), (4.5, "ACK1 → envia pkt5"), (7, "timeout: reenvia\n2, 3, 4 e 5")],
        notas_r=[(3.5, "pkt3 fora de ordem:\ndescarta, ACK1"), (6, "pkt4: descarta, ACK1"), (6.5, "pkt5: descarta, ACK1"),
                 (9, "entrega 2, ACK2"), (9.5, "entrega 3, ACK3 …")])
    ev = [(0, D, "pkt0", 1, 0, AZ), (0.5, 0.5 + D, "pkt1", 1, 0, AZ), (1, 1 + D, "pkt2", 1, 1, AZ),
          (1.5, 1.5 + D, "pkt3", 1, 0, AZ),
          (D, 2 * D, "ACK0", 0, 0, CZ), (2.5, 4.5, "ACK1", 0, 0, CZ), (3.5, 5.5, "ACK3", 0, 0, CZ),
          (4, 6, "pkt4", 1, 0, AZ), (4.5, 6.5, "pkt5", 1, 0, AZ),
          (6, 8, "ACK4", 0, 0, CZ), (6.5, 8.5, "ACK5", 0, 0, CZ),
          (7, 9, "pkt2", 1, 0, VM), (9, 11, "ACK2", 0, 0, CZ)]
    msc(axs[1], "Selective Repeat (N = 4): perde-se o pkt2", 0.15, 0.85, 12, ev,
        notas_e=[(4, "ACK0 → envia pkt4"), (4.5, "ACK1 → envia pkt5"), (5.5, "ACK3: marca o 3,\njanela não avança"),
                 (7, "timeout do pkt2:\nreenvia só o 2"), (11, "ACK2: janela → 6")],
        notas_r=[(3.5, "pkt3 → buffer, ACK3"), (6, "pkt4 → buffer, ACK4"), (6.5, "pkt5 → buffer, ACK5"),
                 (9, "entrega 2, 3, 4, 5\nACK2")])
    fig.tight_layout(); fig.savefig(OUT + "gbn_sr.pdf", bbox_inches="tight"); plt.close(fig)


def stop_wait():
    fig, axs = plt.subplots(1, 2, figsize=(9.5, 4.2))
    for ax, n, tit in ((axs[0], 1, "Stop-and-wait: 1 pacote por RTT + L/R"),
                       (axs[1], 3, "Pipelining: 3 pacotes por RTT + L/R")):
        ax.set_xlim(-0.6, 1.6); ax.set_ylim(7.6, -0.8); ax.axis("off")
        ax.set_title(tit, fontsize=10.5, weight="bold")
        for x, nm in ((0, "emissor"), (1, "receptor")):
            ax.plot([x, x], [-0.2, 7.2], color="black", lw=1.2); ax.text(x, -0.45, nm, ha="center", weight="bold")
        LR, P = 0.5, 3.0
        for i in range(n):
            a = i * LR
            ax.fill([0, 1, 1, 0], [a, a + P, a + P + LR, a + LR], color=AZ, alpha=0.35, lw=0)
        ack_t = P + LR
        ax.annotate("", xy=(0, ack_t + P), xytext=(1, P + LR), arrowprops=dict(arrowstyle="-|>", color=CZ))
        ax.text(0.5, P + LR + P / 2 - 0.35, "ACK", color=CZ, ha="center")
        ax.annotate("", xy=(-0.1, 0), xytext=(-0.1, LR * n), arrowprops=dict(arrowstyle="<->", lw=0.8))
        ax.text(-0.15, LR * n / 2, f"{n}·L/R" if n > 1 else "L/R", ha="right", va="center", fontsize=9)
        ax.annotate("", xy=(-0.42, 0), xytext=(-0.42, P * 2 + LR), arrowprops=dict(arrowstyle="<->", lw=0.8))
        ax.text(-0.47, P + LR / 2, "RTT + L/R", ha="right", va="center", fontsize=9, rotation=90)
        ax.text(0.5, 7.35, rf"$U = \dfrac{{{n if n > 1 else ''}L/R}}{{RTT + L/R}}$", ha="center", fontsize=11)
    fig.tight_layout(); fig.savefig(OUT + "stop_wait_pipelining.pdf", bbox_inches="tight"); plt.close(fig)


def handshake():
    fig, axs = plt.subplots(1, 2, figsize=(9.5, 4.4))
    ev = [(0, 1.5, "SYN, seq=x", 1, 0, AZ), (1.7, 3.2, "SYN+ACK\nseq=y, ack=x+1", 0, 0, VM),
          (3.4, 4.9, "ACK, ack=y+1\n(já pode levar dados)", 1, 0, AZ)]
    msc(axs[0], "Abrir: three-way handshake", 0.15, 0.85, 5.4, ev, pos=0.5,
        notas_e=[(0, "SYN_SENT"), (3.3, "ESTABLISHED")], notas_r=[(1.6, "SYN_RCVD"), (4.9, "ESTABLISHED")])
    axs[0].texts[0].set_text("cliente"); axs[0].texts[1].set_text("servidor")
    ev = [(0, 1.3, "FIN", 1, 0, AZ), (1.3, 2.6, "ACK", 0, 0, CZ), (3, 4.3, "FIN", 0, 0, VM), (4.3, 5.6, "ACK", 1, 0, AZ)]
    msc(axs[1], "Fechar: FIN/ACK em cada sentido", 0.15, 0.85, 6.6, ev, pos=0.5,
        notas_e=[(0, "close(): FIN_WAIT_1"), (2.6, "FIN_WAIT_2"), (4.3, "TIME_WAIT\n(espera 2×vida\ndum segmento)")],
        notas_r=[(1.3, "CLOSE_WAIT"), (3, "close(): LAST_ACK"), (5.6, "CLOSED")])
    axs[1].texts[0].set_text("cliente"); axs[1].texts[1].set_text("servidor")
    fig.tight_layout(); fig.savefig(OUT + "tcp_conexao.pdf", bbox_inches="tight"); plt.close(fig)


def reno(nome, janelas, limiares, notas, titulo=None, w=7.5, h=3.4, passo=2):
    fig, ax = plt.subplots(figsize=(w, h))
    r = list(range(1, len(janelas) + 1))
    ax.plot(r, janelas, "-o", color=AZ, ms=3.5, lw=1.4, label="CongWin")
    if limiares:
        ax.step(r, limiares, where="mid", color=VM, ls="--", lw=1, label="limiar")
        ax.legend(loc="upper left", fontsize=8.5, frameon=False)
    for x, y, t in notas:
        ax.annotate(t, xy=(x, y), xytext=(x + 0.4, y + 3), fontsize=8.5, color=CZ,
                    arrowprops=dict(arrowstyle="-", color=CZ, lw=0.6))
    ax.set_xlabel("ronda de transmissão (RTTs)"); ax.set_ylabel("janela (MSS)")
    ax.set_xticks(range(0, len(janelas) + 2, passo)); ax.grid(alpha=0.3)
    if titulo: ax.set_title(titulo, fontsize=10.5, weight="bold")
    fig.tight_layout(); fig.savefig(OUT + nome, bbox_inches="tight"); plt.close(fig)


if __name__ == "__main__":
    gbn_sr(); stop_wait(); handshake()
    # Ficha 7, ex. 4 (sem anotações: é o enunciado)
    f7 = [1, 2, 4, 8, 16, 32] + list(range(33, 43)) + list(range(21, 27)) + [1, 2, 4, 8]
    reno("reno_f7.pdf", f7, None, [], w=7.0, h=3.0)
    # Exame 2025/26, ex. 12: gráfico reconstruído (o original não se vê na foto); perdas em 8, 25 e 46
    ex25 = [2**i for i in range(8)] + list(range(64, 81)) + list(range(40, 61)) + [1, 2, 4, 8, 16] + list(range(30, 49))
    assert len(ex25) == 70
    reno("reno_exame25.pdf", ex25, None, [], w=7.5, h=3.4, passo=5)
    # Exemplo resolvido: limiar inicial 8, 3 ACKs dup. no fim da ronda 8, timeout no fim da ronda 11
    ex = [1, 2, 4, 8, 9, 10, 11, 12, 6, 7, 8, 1, 2, 4, 5, 6]
    lim = [8] * 8 + [6] * 3 + [4] * 5
    reno("reno_exemplo.pdf", ex, lim, [(8, 12, "3 ACKs dup."), (11, 8, "timeout")], w=7.0, h=3.0)
