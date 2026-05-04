# ═══════════════════════════════════════════════════════
#  PHASE 5 — PORTFOLIO PDF CASE STUDY
#  Retail Stock-Out Reduction — BA Portfolio Project
# ═══════════════════════════════════════════════════════

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table,
    TableStyle, HRFlowable, PageBreak
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

W, H = A4

# ── COLOURS ──────────────────────────────────────────
NAVY   = colors.HexColor("#1E2761")
ICE    = colors.HexColor("#CADCFC")
ACCENT = colors.HexColor("#4FC3F7")
RED    = colors.HexColor("#E74C3C")
AMBER  = colors.HexColor("#F39C12")
GREEN  = colors.HexColor("#27AE60")
MUTED  = colors.HexColor("#8A9BBF")
DARK   = colors.HexColor("#12193D")
WHITE  = colors.white
LIGHT  = colors.HexColor("#F4F7FF")

# ── STYLES ───────────────────────────────────────────
def S(name, **kw):
    return ParagraphStyle(name, **kw)

styles = {
    "h1": S("h1", fontSize=26, textColor=NAVY, fontName="Helvetica-Bold",
             spaceAfter=6, leading=32),
    "h2": S("h2", fontSize=15, textColor=NAVY, fontName="Helvetica-Bold",
             spaceBefore=18, spaceAfter=6, leading=20),
    "h3": S("h3", fontSize=11, textColor=ACCENT, fontName="Helvetica-Bold",
             spaceBefore=10, spaceAfter=4, leading=15),
    "body": S("body", fontSize=10, textColor=colors.HexColor("#2d2d2d"),
              fontName="Helvetica", leading=16, spaceAfter=6),
    "small": S("small", fontSize=8.5, textColor=MUTED,
               fontName="Helvetica", leading=13),
    "label": S("label", fontSize=8, textColor=WHITE, fontName="Helvetica-Bold",
               alignment=TA_CENTER),
    "kpi_val": S("kpi_val", fontSize=22, textColor=NAVY, fontName="Helvetica-Bold",
                 alignment=TA_CENTER, leading=26),
    "kpi_lbl": S("kpi_lbl", fontSize=8, textColor=MUTED, fontName="Helvetica",
                 alignment=TA_CENTER, leading=11),
    "finding": S("finding", fontSize=9.5, textColor=colors.HexColor("#1a1a2e"),
                 fontName="Helvetica", leading=15, leftIndent=10),
    "tag": S("tag", fontSize=8, textColor=WHITE, fontName="Helvetica-Bold",
             alignment=TA_CENTER),
    "footer": S("footer", fontSize=8, textColor=MUTED, fontName="Helvetica",
                alignment=TA_CENTER),
    "subtitle": S("subtitle", fontSize=12, textColor=MUTED, fontName="Helvetica",
                  spaceAfter=4, leading=16),
    "code": S("code", fontSize=9, textColor=colors.HexColor("#2d2d2d"),
              fontName="Courier", leading=14, backColor=LIGHT,
              leftIndent=8, rightIndent=8),
}

# ── HELPERS ──────────────────────────────────────────
def HR(color=NAVY, thickness=1):
    return HRFlowable(width="100%", thickness=thickness,
                      color=color, spaceAfter=8, spaceBefore=4)

def section_tag(text, color=NAVY):
    data = [[Paragraph(text, styles["tag"])]]
    t = Table(data, colWidths=[40*mm], rowHeights=[7*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), color),
        ("ROUNDEDCORNERS", [4]),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

def kpi_row(items):
    # items = [(value, label, color), ...]
    cells = []
    for val, lbl, col in items:
        inner = [
            [Paragraph(val, styles["kpi_val"])],
            [Paragraph(lbl, styles["kpi_lbl"])],
        ]
        t = Table(inner, colWidths=[38*mm], rowHeights=[12*mm, 8*mm])
        t.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), LIGHT),
            ("LINEBELOW", (0,0), (-1,0), 2.5, col),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
            ("TOPPADDING", (0,0), (-1,-1), 4),
            ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ]))
        cells.append(t)

    row = Table([cells], colWidths=[40*mm]*len(items))
    row.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
    ]))
    return row

def finding_box(text, color=NAVY):
    data = [[Paragraph(text, styles["finding"])]]
    t = Table(data, colWidths=[160*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT),
        ("LINEBEFORE", (0,0), (0,-1), 3, color),
        ("TOPPADDING", (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING", (0,0), (-1,-1), 14),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
    ]))
    return t

def two_col(left_items, right_items, lw=85*mm, rw=78*mm):
    data = [[left_items, right_items]]
    t = Table(data, colWidths=[lw, rw])
    t.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    return t

# ── HEADER / FOOTER ──────────────────────────────────
def on_page(canvas, doc):
    canvas.saveState()
    # Header bar
    canvas.setFillColor(NAVY)
    canvas.rect(0, H - 14*mm, W, 14*mm, fill=1, stroke=0)
    canvas.setFillColor(ACCENT)
    canvas.rect(0, H - 14*mm, 4*mm, 14*mm, fill=1, stroke=0)
    canvas.setFillColor(WHITE)
    canvas.setFont("Helvetica-Bold", 8)
    canvas.drawString(12*mm, H - 9*mm, "RETAIL STOCK-OUT REDUCTION  |  BA PORTFOLIO CASE STUDY")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(ICE)
    canvas.drawRightString(W - 12*mm, H - 9*mm, f"Page {doc.page}")
    # Footer
    canvas.setFillColor(DARK)
    canvas.rect(0, 0, W, 10*mm, fill=1, stroke=0)
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7)
    canvas.drawCentredString(W/2, 3.5*mm,
        "BanothDeepak  |  github.com/BanothDeepak/retail-stockout-ba-project  |  May 2026")
    canvas.restoreState()

# ── BUILD DOCUMENT ────────────────────────────────────
doc = SimpleDocTemplate(
    "/home/claude/Phase5_BA_CaseStudy.pdf",
    pagesize=A4,
    topMargin=22*mm, bottomMargin=18*mm,
    leftMargin=18*mm, rightMargin=18*mm,
)

story = []

# ════════════════════════════════════════════════════
#  PAGE 1 — COVER
# ════════════════════════════════════════════════════
story.append(Spacer(1, 20*mm))
story.append(Paragraph("BA Portfolio Project", styles["subtitle"]))
story.append(Paragraph("Retail Stock-Out Reduction", styles["h1"]))
story.append(HR(ACCENT, 2))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "A Business Analyst case study using a real retail inventory dataset to identify "
    "stock-out risks, forecast inaccuracies, promotion inefficiencies, and pricing gaps "
    "across 5 stores and 20 products.",
    styles["body"]
))
story.append(Spacer(1, 10))

# KPI row
story.append(kpi_row([
    ("73,100", "Dataset Rows", NAVY),
    ("5",      "Stores",       ACCENT),
    ("20",     "Products",     GREEN),
    ("5",      "Deliverables", AMBER),
]))
story.append(Spacer(1, 14))

# Project metadata table
meta = [
    ["Project",   "Retail Stock-Out Reduction"],
    ["Analyst",   "BanothDeepak"],
    ["Dataset",   "Retail Store Inventory Forecasting (Kaggle)"],
    ["Tools",     "Python · pandas · matplotlib · VS Code · GitHub"],
    ["Phases",    "Requirements → Data Analysis → Dashboard → Portfolio"],
    ["Date",      "May 2026"],
]
meta_t = Table(meta, colWidths=[38*mm, 122*mm])
meta_t.setStyle(TableStyle([
    ("FONTNAME",  (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTNAME",  (1,0), (1,-1), "Helvetica"),
    ("FONTSIZE",  (0,0), (-1,-1), 9.5),
    ("TEXTCOLOR", (0,0), (0,-1), NAVY),
    ("TEXTCOLOR", (1,0), (1,-1), colors.HexColor("#2d2d2d")),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [LIGHT, WHITE]),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ("LINEBELOW", (0,-1), (-1,-1), 0.5, ICE),
]))
story.append(meta_t)
story.append(PageBreak())

# ════════════════════════════════════════════════════
#  PAGE 2 — PROBLEM & APPROACH
# ════════════════════════════════════════════════════
story.append(Paragraph("1. Business Problem", styles["h2"]))
story.append(HR())
story.append(Paragraph(
    "A retail chain operating 5 stores across multiple regions is experiencing simultaneous "
    "stock-out and overstock situations. The initial assumption was that this was a "
    "category-specific issue — but analysis reveals a systemic replenishment model failure "
    "affecting all 5 categories equally.",
    styles["body"]
))
story.append(Spacer(1, 6))
story.append(finding_box(
    "<b>Key Finding:</b> Every category sits at ~33% low-stock AND ~37% overstock "
    "simultaneously — a replenishment model failure, not a product problem.",
    RED
))
story.append(Spacer(1, 10))

story.append(Paragraph("2. Analytical Approach", styles["h2"]))
story.append(HR())

phases = [
    ("Phase 1", "Project Scoping", "Defined project title, scope, and business context for the retail inventory domain."),
    ("Phase 2", "Requirements Gathering", "Built a Data Dictionary (15 columns), 5 User Stories with acceptance criteria, and a 9-section BRD."),
    ("Phase 3", "Data Analysis", "Python scripts (pandas + matplotlib) covering all 5 user stories. Outputs: CSVs, PNGs, Excel."),
    ("Phase 4", "Dashboard & Deck", "8-slide PowerPoint deck + interactive HTML dashboard with 7 tabs and native charts."),
    ("Phase 5", "Portfolio Packaging", "PDF case study, LinkedIn post, Notion template, and GitHub push."),
]
phase_data = [["Phase", "Name", "Output"]] + [[p, n, d] for p, n, d in phases]
phase_t = Table(phase_data, colWidths=[22*mm, 44*mm, 94*mm])
phase_t.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), NAVY),
    ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",      (0,0), (-1,-1), 9),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT, WHITE]),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 7),
    ("RIGHTPADDING",  (0,0), (-1,-1), 7),
    ("TEXTCOLOR",     (0,1), (0,-1), NAVY),
    ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
    ("GRID",          (0,0), (-1,-1), 0.3, ICE),
]))
story.append(phase_t)
story.append(PageBreak())

# ════════════════════════════════════════════════════
#  PAGE 3 — USER STORIES & FINDINGS
# ════════════════════════════════════════════════════
story.append(Paragraph("3. User Stories & Key Findings", styles["h2"]))
story.append(HR())

us_data = [
    ["ID", "Persona", "Business Need", "Key Finding"],
    ["US-01", "Store Ops Manager",
     "Flag products where Inventory < Units Sold x 1.5",
     "~4,800 low-stock rows per category — systemic, not isolated"],
    ["US-02", "Supply Chain Planner",
     "Compare forecast vs actual by season & category",
     "MAE flat at 8.32-8.40 — zero seasonal weighting in model"],
    ["US-03", "Category Manager",
     "Compare inventory & sales on promo vs normal days",
     "137.8 vs 137.6 units — promotions deliver no uplift"],
    ["US-04", "Pricing Analyst",
     "Price gap vs competitor by region & category",
     "Groceries at -18.3% — exceeds 15% underpriced threshold"],
    ["US-05", "Operations Director",
     "% overstock & low-stock per store & region",
     "Consistent 38% overstock across all 5 stores"],
]
us_t = Table(us_data, colWidths=[14*mm, 32*mm, 54*mm, 60*mm])
us_t.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), NAVY),
    ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",      (0,0), (-1,-1), 8.5),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT, WHITE]),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 6),
    ("RIGHTPADDING",  (0,0), (-1,-1), 6),
    ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ("TEXTCOLOR",     (0,1), (0,-1), ACCENT),
    ("FONTNAME",      (0,1), (0,-1), "Helvetica-Bold"),
    ("GRID",          (0,0), (-1,-1), 0.3, ICE),
]))
story.append(us_t)
story.append(Spacer(1, 12))

story.append(Paragraph("4. Data Quality Observations", styles["h2"]))
story.append(HR())
story.append(Paragraph(
    "A key BA skill is flagging data anomalies during analysis. Two issues were identified and documented:",
    styles["body"]
))
story.append(Spacer(1, 4))
story.append(finding_box(
    "<b>DQ-01 Negative Demand Forecast values:</b> The Demand Forecast column contains negative values "
    "(min: -10.07). These were excluded from US-02 forecast accuracy analysis and flagged in the BRD "
    "as a data governance issue requiring upstream investigation.",
    AMBER
))
story.append(Spacer(1, 6))
story.append(finding_box(
    "<b>DQ-02 No Reorder Point column:</b> The dataset contains no explicit Reorder Point field. "
    "A derived threshold was calculated as Units Sold x 1.5 per US-01 acceptance criteria, "
    "documented in the Data Dictionary as a calculated field.",
    AMBER
))
story.append(PageBreak())

# ════════════════════════════════════════════════════
#  PAGE 4 — RECOMMENDATIONS & DELIVERABLES
# ════════════════════════════════════════════════════
story.append(Paragraph("5. Recommendations", styles["h2"]))
story.append(HR())

recs = [
    ("01", "Fix the Replenishment Model", RED,
     "Define dynamic reorder points using Inventory Level vs Units Sold x 1.5. "
     "The simultaneous 33% low-stock and 37% overstock across all categories confirms "
     "the formula is broken — not the products or stores."),
    ("02", "Introduce Seasonal Forecast Weighting", GREEN,
     "MAE of 8.32-8.40 is flat across all seasons — no seasonal adjustment exists. "
     "Prioritise Furniture (Autumn) and Toys (Winter) for model recalibration first."),
    ("03", "Conduct Promotion ROI Audit", AMBER,
     "Promotions run on 50% of all trading days yet deliver zero incremental demand "
     "(137.6 vs 137.8 avg units sold). Audit all promotion types before next cycle."),
    ("04", "Review Grocery Pricing Nationally", ACCENT,
     "Groceries average -18.3% below competitor price — exceeding the 15% alert threshold "
     "across all regions. A national pricing policy review is required to recover margin."),
]

for num, title, col, body in recs:
    rec_data = [[
        Paragraph(num, ParagraphStyle("rn", fontSize=14, textColor=WHITE,
                  fontName="Helvetica-Bold", alignment=TA_CENTER)),
        [Paragraph(title, ParagraphStyle("rt", fontSize=10, textColor=NAVY,
                   fontName="Helvetica-Bold", spaceAfter=3)),
         Paragraph(body, ParagraphStyle("rb", fontSize=9, textColor=colors.HexColor("#2d2d2d"),
                   fontName="Helvetica", leading=14))]
    ]]
    rec_t = Table(rec_data, colWidths=[14*mm, 146*mm])
    rec_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (0,-1), col),
        ("BACKGROUND",    (1,0), (1,-1), LIGHT),
        ("VALIGN",        (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]))
    story.append(rec_t)
    story.append(Spacer(1, 5))

story.append(Spacer(1, 8))
story.append(Paragraph("6. Portfolio Deliverables", styles["h2"]))
story.append(HR())

deliverables = [
    ["#", "Artefact", "Format", "Phase"],
    ["1", "Data Dictionary — 15 columns defined with business language", "Doc", "2"],
    ["2", "5 User Stories — with personas, outcomes & acceptance criteria", "Doc", "2"],
    ["3", "Business Requirements Document — 9 sections", "DOCX", "2"],
    ["4", "Phase 3 Python Analysis — all 5 user stories", "PY + CSV + PNG + XLSX", "3"],
    ["5", "Phase 4 PowerPoint Deck — 8 slides", "PPTX", "4"],
    ["6", "Phase 4 Interactive Dashboard — 7 tabs", "HTML", "4"],
    ["7", "Phase 5 PDF Case Study", "PDF", "5"],
    ["8", "GitHub Repository — full project history", "github.com", "All"],
]
del_t = Table(deliverables, colWidths=[8*mm, 94*mm, 44*mm, 14*mm])
del_t.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), NAVY),
    ("TEXTCOLOR",     (0,0), (-1,0), WHITE),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTNAME",      (0,1), (-1,-1), "Helvetica"),
    ("FONTSIZE",      (0,0), (-1,-1), 9),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [LIGHT, WHITE]),
    ("TOPPADDING",    (0,0), (-1,-1), 5),
    ("BOTTOMPADDING", (0,0), (-1,-1), 5),
    ("LEFTPADDING",   (0,0), (-1,-1), 7),
    ("RIGHTPADDING",  (0,0), (-1,-1), 7),
    ("TEXTCOLOR",     (0,1), (0,-1), MUTED),
    ("GRID",          (0,0), (-1,-1), 0.3, ICE),
    ("ALIGN",         (0,0), (0,-1), "CENTER"),
    ("ALIGN",         (3,0), (3,-1), "CENTER"),
]))
story.append(del_t)
story.append(Spacer(1, 10))

story.append(HR(ACCENT, 1.5))
story.append(Paragraph(
    "GitHub Repository: github.com/BanothDeepak/retail-stockout-ba-project",
    ParagraphStyle("link", fontSize=10, textColor=ACCENT, fontName="Helvetica-Bold",
                   alignment=TA_CENTER)
))

# ── BUILD ─────────────────────────────────────────────
doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
print("✅ Phase5_BA_CaseStudy.pdf saved!")
