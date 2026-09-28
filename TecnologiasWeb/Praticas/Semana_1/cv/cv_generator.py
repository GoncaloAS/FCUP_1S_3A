"""
CV generator — Gonçalo Alves de Sousa

Uso:
    python cv_generator.py            -> gera as duas variantes
    VARIANT="igaming" python ...      -> (ou edita VARIANTS em baixo)

Variantes:
    "igaming" -> versão Clever Advertising (inclui poker + projeto de analytics)
    "general" -> versão neutra (sem poker, projeto substituído)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

W, H = A4
ML = 18 * mm
MR = 18 * mm
MT = 14 * mm
MB = 12 * mm
CW = W - ML - MR

# Colors
DARK = HexColor("#1a1a1a")
MEDIUM = HexColor("#3d3d3d")
LIGHT = HexColor("#6b7280")
ACCENT = HexColor("#2563EB")
DIVIDER = HexColor("#D1D5DB")

FB = "Helvetica-Bold"
FR = "Helvetica"
FO = "Helvetica-Oblique"


# ---------------------------------------------------------------- primitives

def wrap_text(c, text, font, size, max_w):
    c.setFont(font, size)
    words = text.split()
    lines, cur = [], ""
    for w in words:
        test = cur + (" " if cur else "") + w
        if c.stringWidth(test, font, size) <= max_w:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def check_page(c, y, needed=6 * mm):
    """Quebra de página segura. Devolve o novo y."""
    if y - needed < MB:
        c.showPage()
        return H - MT
    return y


def draw_wrapped(c, x, y, text, font, size, color, max_w, leading=None):
    if leading is None:
        leading = size * 1.48
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_text(c, text, font, size, max_w):
        y = check_page(c, y, leading)
        c.setFont(font, size)
        c.setFillColor(color)
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullet(c, x, y, text, max_w, leading=None):
    sz = 8
    if leading is None:
        leading = sz * 1.28
    indent = 4 * mm
    y = check_page(c, y, leading * 2)
    c.setFillColor(ACCENT)
    c.circle(x + 1.2 * mm, y - 0.3 * mm, 0.7 * mm, fill=1, stroke=0)
    return draw_wrapped(c, x + indent, y, text, FR, sz, MEDIUM, max_w - indent, leading)


def divider(c, y):
    c.setStrokeColor(DIVIDER)
    c.setLineWidth(0.4)
    c.line(ML, y, W - MR, y)


def underlined_heading(c, x, y, title):
    c.setFont(FB, 9)
    c.setFillColor(ACCENT)
    t = title.upper()
    c.drawString(x, y, t)
    tw = c.stringWidth(t, FB, 9)
    c.setStrokeColor(ACCENT)
    c.setLineWidth(1)
    c.line(x, y - 2.5 * mm, x + tw, y - 2.5 * mm)
    return y - 7 * mm


def section_title(c, y, title):
    y = check_page(c, y, 14 * mm)
    return underlined_heading(c, ML, y, title)


def job_header(c, y, title, date_str):
    y = check_page(c, y, 12 * mm)
    c.setFont(FB, 10.5)
    c.setFillColor(DARK)
    c.drawString(ML, y, title)
    c.setFont(FR, 8)
    c.setFillColor(LIGHT)
    c.drawRightString(W - MR, y, date_str)
    return y - 4.5 * mm


def job_sub(c, y, company, details, link=None):
    c.setFont(FR, 8.5)
    c.setFillColor(MEDIUM)
    c.drawString(ML, y, company)
    cw = c.stringWidth(company + "  ", FR, 8.5)
    c.setFont(FO, 8)
    c.setFillColor(ACCENT if link else LIGHT)
    c.drawString(ML + cw, y, details)
    if link:
        dw = c.stringWidth(details, FO, 8)
        c.linkURL(link, (ML + cw, y - 1.5 * mm, ML + cw + dw, y + 2.5 * mm), relative=0)
    return y - 5.5 * mm


def bullets(c, y, items):
    for b in items:
        y = draw_bullet(c, ML + 1 * mm, y, b, CW - 2 * mm)
        y -= 0.4 * mm
    return y - 1.6 * mm


# ---------------------------------------------------------------- content

HEADLINE = "Python & Django  ·  Async Data Pipelines  ·  Open Source — DjangoCon Europe / PyCon Portugal"

CONTACT_ITEMS = [
    ("+351 965 109 144", "tel:+351965109144"),
    ("gsag.sousa@icloud.com", "mailto:gsag.sousa@icloud.com"),
    ("linkedin.com/in/gonçalo-sousa-profile",
     "https://www.linkedin.com/in/gon%C3%A7alo-sousa-profile/"),
    ("github.com/GoncaloAS", "https://github.com/GoncaloAS"),
    ("Porto, Portugal", None),
]

EXPERIENCE = [
    {
        "title": "Software Engineer",
        "date": "Dec 2025 – Present",
        "company": "Universidade do Porto",
        "details": "Contract · Hybrid · Porto, Portugal",
        "bullets": [
            "Merging three Django/Wagtail products (faculty sites, university portal, central-services sites) into one codebase; an environment-based config layer in Python and Docker picks product, templates, styling and business rules at startup, so one codebase serves every university unit.",
            "Moving the codebase to current Django and Wagtail LTS releases one version at a time, each step gated by pinned dependencies, admin smoke tests on all three products, a test suite grown from 21 to 38 tests and a content comparison.",
            "Rewrote the course import from the university's information system as an async httpx client with rate limiting (~11,000 requests per run); turned courses from CMS pages into a plain model, clearing 4,074 orphaned pages.",
        ],
    },
    {
        "title": "Full Stack Developer",
        "date": "Jul 2023 – Dec 2025",
        "company": "Ad Evolutio",
        "details": "Part-time · Hybrid · Porto, Portugal",
        "bullets": [
            "Migrated 50%+ of the client portfolio off end-of-life Django versions onto a supported LTS release, closing known vulnerabilities and cutting upgrade debt.",
            "Built and maintained full-stack applications with Django, Wagtail and PostgreSQL across multiple client projects, from data modelling and REST API design to responsive frontend delivery.",
        ],
    },
    {
        "title": "Lead Developer & Staff, Conference Websites",
        "date": "2023 – Present",
        "company": "DjangoCon Europe & PyCon Portugal",
        "details": "Open Source · Volunteer",
        "bullets": [
            "Led development of the official Django-powered site for DjangoCon Europe 2025 (Dublin), after working as a developer on the 2024 (Vigo) site; 300+ attendees each.",
            "Built and maintained PyCon Portugal sites for 2025 (Cascais), 2024 (Braga) and 2023 (Coimbra) as part of the core organising team.",
        ],
    },
]

ASYQUOTE = {
    "title": "AsyQuote, Construction SaaS Platform",
    "date": "2023–2024 · Grade 20/20",
    "company": "Final Year Project · Colégio Internato dos Carvalhos",
    "details": "github.com/GoncaloAS/AsyQuote",
    "link": "https://github.com/GoncaloAS/AsyQuote",
    "bullets": [
        "Quoting SaaS in Django and Wagtail for small construction firms: quotes as a tree of chapters, services and priced lines with cost and margin per line; print-ready Excel export with live formulas.",
        "Async scraper (asyncio, aiohttp) for the supplier price catalogue: pages in batches of ten, retries with exponential backoff; ~40,000 products with pages and images in about 15 minutes. In 2026 added an RFC 9309 robots.txt matcher and Crawl-delay support.",
        "Accounts: mandatory email verification, reCAPTCHA, Argon2 hashing, Django's password validators (incl. 20,000 common passwords) and reset links that expire after 2 minutes.",
    ],
}

LANGS = [
    ("Portuguese", "Native"),
    ("English", "C1"),
    ("French", "C1"),
    ("Spanish", "A2"),
]

SKILLS = [
    ("Languages", "Python, JavaScript, C, C#, SQL"),
    ("Frameworks", "Django, Wagtail, HTMX, Bootstrap"),
    ("Infrastructure", "PostgreSQL, Docker, Git, Linux, CI/CD"),
    ("Practices", "REST APIs, asyncio, Web Scraping, Data Modelling"),
]

INTERESTS_IGAMING = (
    "Online poker — long-term winning cash-game player: 568k hands since Jan 2025, +4.2 bb/100 overall "
    "from NL5 to NL100 (before rakeback); 11.8 bb/100 over 51k hands at NL100, the current stake. "
    "Weekly group and fortnightly 1:1 coaching with the Polarize Poker professional team; solver study "
    "in GTO Wizard."
)


# ---------------------------------------------------------------- render

def create_cv(variant="igaming", path=None):
    if path is None:
        path = f"cv_{variant}.pdf"
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle("Gonçalo Alves de Sousa — CV")
    c.setAuthor("Gonçalo Alves de Sousa")

    y = H - MT

    # ===== HEADER =====
    c.setFont(FB, 22)
    c.setFillColor(DARK)
    c.drawString(ML, y, "Gonçalo Alves de Sousa")
    y -= 8 * mm

    y = draw_wrapped(c, ML, y, HEADLINE, FR, 9.5, MEDIUM, CW)
    y -= 2 * mm

    c.setFont(FR, 8)
    sep = "  ·  "
    cx = ML
    for i, (label, url) in enumerate(CONTACT_ITEMS):
        c.setFillColor(ACCENT if url else LIGHT)
        tw = c.stringWidth(label, FR, 8)
        c.drawString(cx, y, label)
        if url:
            c.linkURL(url, (cx, y - 1.5 * mm, cx + tw, y + 2.5 * mm), relative=0)
        cx += tw
        if i < len(CONTACT_ITEMS) - 1:
            c.setFillColor(LIGHT)
            c.drawString(cx, y, sep)
            cx += c.stringWidth(sep, FR, 8)
    y -= 5 * mm

    divider(c, y)
    y -= 4 * mm

    # ===== EXPERIENCE =====
    y = section_title(c, y, "Experience")
    for job in EXPERIENCE:
        y = job_header(c, y, job["title"], job["date"])
        y = job_sub(c, y, job["company"], job["details"])
        y = bullets(c, y, job["bullets"])

    divider(c, y)
    y -= 4 * mm

    # ===== PROJECTS =====
    y = section_title(c, y, "Projects")

    projects = [ASYQUOTE]

    for p in projects:
        y = job_header(c, y, p["title"], p["date"])
        c.setFont(FO, 8)
        c.setFillColor(LIGHT)
        c.drawString(ML, y, p["company"])
        if p.get("details"):
            sx = ML + c.stringWidth(p["company"] + "  ·  ", FO, 8)
            c.setFillColor(LIGHT)
            c.drawString(ML + c.stringWidth(p["company"], FO, 8), y, "  ·  ")
            c.setFillColor(ACCENT)
            c.drawString(sx, y, p["details"])
            dw = c.stringWidth(p["details"], FO, 8)
            if p.get("link"):
                c.linkURL(p["link"], (sx, y - 1.5 * mm, sx + dw, y + 2.5 * mm), relative=0)
        y -= 5 * mm
        y = bullets(c, y, p["bullets"])

    divider(c, y)
    y -= 4 * mm

    # ===== BEYOND WORK (igaming only) =====
    if variant == "igaming":
        y = section_title(c, y, "Beyond work")
        y = draw_wrapped(c, ML, y, INTERESTS_IGAMING, FR, 8, MEDIUM, CW, 3.6 * mm)
        y -= 1.5 * mm
        divider(c, y)
        y -= 4 * mm

    # ===== TWO COLUMNS =====
    y = check_page(c, y, 45 * mm)
    col1_x = ML
    col2_x = ML + CW * 0.54
    base_y = y

    # --- LEFT: Education ---
    y_l = underlined_heading(c, col1_x, base_y, "Education")

    c.setFont(FB, 9.5)
    c.setFillColor(DARK)
    c.drawString(col1_x, y_l, "BSc Computer Science")
    y_l -= 4 * mm
    c.setFont(FR, 8.5)
    c.setFillColor(MEDIUM)
    c.drawString(col1_x, y_l, "FCUP — Universidade do Porto")
    y_l -= 3.5 * mm
    c.setFont(FO, 7.5)
    c.setFillColor(LIGHT)
    c.drawString(col1_x, y_l, "Sep 2024 – Jul 2027 · Porto, Portugal")
    y_l -= 7 * mm

    c.setFont(FB, 9.5)
    c.setFillColor(DARK)
    c.drawString(col1_x, y_l, "High School Diploma — IT Track")
    y_l -= 4 * mm
    c.setFont(FR, 8.5)
    c.setFillColor(MEDIUM)
    c.drawString(col1_x, y_l, "Colégio Internato dos Carvalhos")
    y_l -= 3.5 * mm
    c.setFont(FO, 7.5)
    c.setFillColor(LIGHT)
    c.drawString(col1_x, y_l, "Sep 2022 – Jun 2024 · GPA 19/20")
    y_l -= 6 * mm

    y_l = underlined_heading(c, col1_x, y_l, "Languages")
    for lang, lvl in LANGS:
        c.setFont(FB, 8.5)
        c.setFillColor(DARK)
        c.drawString(col1_x, y_l, lang)
        c.setFont(FR, 8)
        c.setFillColor(LIGHT)
        c.drawString(col1_x + 27 * mm, y_l, lvl)
        y_l -= 4.5 * mm

    # --- RIGHT: Technical Skills ---
    y_r = underlined_heading(c, col2_x, base_y, "Technical Skills")
    col2_w = CW * 0.46
    for cat, items in SKILLS:
        c.setFont(FB, 8.5)
        c.setFillColor(DARK)
        c.drawString(col2_x, y_r, cat)
        y_r -= 3.5 * mm
        y_r = draw_wrapped(c, col2_x, y_r, items, FR, 7.8, MEDIUM, col2_w, 3.2 * mm)
        y_r -= 1.5 * mm

    y = min(y_l, y_r) - 2 * mm

    c.save()
    return path


if __name__ == "__main__":
    print(f"CV: {create_cv('igaming', 'cv.pdf')}")
    print(f"CV: {create_cv('general', 'cv_general.pdf')}")
