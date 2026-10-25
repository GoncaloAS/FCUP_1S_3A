"""Gera os PDFs das fichas 5/6 e do trabalho prático de Redes (texto copiado do Moodle)."""
import re, sys, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Preformatted, Image,
                                Table, TableStyle, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

FD = "/opt/anaconda3/pkgs/matplotlib-base-3.8.4-py312h4479663_2/lib/python3.12/site-packages/matplotlib/mpl-data/fonts/ttf/"
for n, f in [("DejaVuSans", "DejaVuSans.ttf"), ("DejaVuSans-Bold", "DejaVuSans-Bold.ttf"),
             ("DejaVuSans-Oblique", "DejaVuSans-Oblique.ttf"), ("DejaVuSans-BoldOblique", "DejaVuSans-BoldOblique.ttf"),
             ("DejaVuSansMono", "DejaVuSansMono.ttf"), ("DejaVuSansMono-Bold", "DejaVuSansMono-Bold.ttf")]:
    pdfmetrics.registerFont(TTFont(n, FD + f))
addMapping("DejaVuSans", 0, 0, "DejaVuSans"); addMapping("DejaVuSans", 1, 0, "DejaVuSans-Bold")
addMapping("DejaVuSans", 0, 1, "DejaVuSans-Oblique"); addMapping("DejaVuSans", 1, 1, "DejaVuSans-BoldOblique")
addMapping("DejaVuSansMono", 0, 0, "DejaVuSansMono"); addMapping("DejaVuSansMono", 1, 0, "DejaVuSansMono-Bold")
addMapping("DejaVuSansMono", 0, 1, "DejaVuSansMono"); addMapping("DejaVuSansMono", 1, 1, "DejaVuSansMono-Bold")

S = {
    "title": ParagraphStyle("t", fontName="DejaVuSans-Bold", fontSize=15, leading=19, alignment=TA_CENTER, spaceAfter=2),
    "sub": ParagraphStyle("s", fontName="DejaVuSans-Oblique", fontSize=8.5, leading=11, alignment=TA_CENTER,
                          textColor=colors.grey, spaceAfter=12),
    "h2": ParagraphStyle("h2", fontName="DejaVuSans-Bold", fontSize=12, leading=15, spaceBefore=10, spaceAfter=4),
    "h3": ParagraphStyle("h3", fontName="DejaVuSans-Bold", fontSize=10.5, leading=13, spaceBefore=7, spaceAfter=3),
    "p": ParagraphStyle("p", fontName="DejaVuSans", fontSize=9.5, leading=13, spaceAfter=5),
    "n": ParagraphStyle("n", fontName="DejaVuSans", fontSize=9.5, leading=13, spaceBefore=6, spaceAfter=4,
                        leftIndent=14, firstLineIndent=-14),
    "a": ParagraphStyle("a", fontName="DejaVuSans", fontSize=9.5, leading=13, spaceAfter=3,
                        leftIndent=34, firstLineIndent=-16),
    "b": ParagraphStyle("b", fontName="DejaVuSans", fontSize=9.5, leading=13, spaceAfter=2,
                        leftIndent=26, firstLineIndent=-10),
    "cap": ParagraphStyle("c", fontName="DejaVuSans", fontSize=8.5, leading=11, alignment=TA_CENTER, spaceAfter=6),
    "code": ParagraphStyle("code", fontName="DejaVuSansMono", fontSize=7.6, leading=9.4, leftIndent=8,
                           backColor=colors.Color(.95, .95, .95), borderPadding=5, spaceBefore=4, spaceAfter=8),
    "cell": ParagraphStyle("cell", fontName="DejaVuSans", fontSize=7.8, leading=9.6),
    "cellb": ParagraphStyle("cellb", fontName="DejaVuSans-Bold", fontSize=7.8, leading=9.6),
}


def inl(t):
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"`([^`]+)`", r'<font face="DejaVuSansMono" size="8.8">\1</font>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"\^(.+?)\^", r"<super>\1</super>", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<link href="\2" color="#1a4f9c">\1</link>', t)
    return t


def build(path, title, sub, blocks):
    out = [Paragraph(inl(title), S["title"]), Paragraph(inl(sub), S["sub"])]
    for b in blocks:
        k = b[0]
        if k in ("p", "h2", "h3", "cap"):
            out.append(Paragraph(inl(b[1]), S[k]))
        elif k == "n":
            out.append(Paragraph(f"<b>{b[1]}</b>&nbsp;&nbsp;" + inl(b[2]), S["n"]))
        elif k == "a":
            out.append(Paragraph(f"{b[1]}&nbsp;&nbsp;" + inl(b[2]), S["a"]))
        elif k == "b":
            out.append(Paragraph("•&nbsp;&nbsp;" + inl(b[1]), S["b"]))
        elif k == "code":
            out.append(Preformatted(b[1].strip("\n"), S["code"]))
        elif k == "img":
            img = Image(b[1]); w = b[2] * cm
            img.drawHeight = img.imageHeight * w / img.imageWidth; img.drawWidth = w
            out.append(KeepTogether([Spacer(1, 4), img, Spacer(1, 3), Paragraph(inl(b[3]), S["cap"])]))
        elif k == "table":
            rows, widths = b[1], b[2]
            data = [[Paragraph(inl(c), S["cellb" if i == 0 else "cell"]) for c in r] for i, r in enumerate(rows)]
            t = Table(data, colWidths=[w * cm for w in widths], repeatRows=1)
            t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), .4, colors.grey),
                                   ("BACKGROUND", (0, 0), (-1, 0), colors.Color(.9, .9, .9)),
                                   ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                   ("TOPPADDING", (0, 0), (-1, -1), 2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3)]))
            out += [Spacer(1, 3), t, Spacer(1, 6)]
        elif k == "sp":
            out.append(Spacer(1, b[1]))
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm, topMargin=1.8 * cm,
                            bottomMargin=1.8 * cm, title=title, author="Moodle FCUP — CC3002 Redes de Comunicação")
    doc.build(out)
    print("ok", path)


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(__file__))
    import conteudo
    for path, title, sub, blocks in conteudo.DOCS:
        build(path, title, sub, blocks)
