#!/usr/bin/env python3
"""
generate_report_pdf.py
Recreates the audit report as a professional A4 PDF from scratch.

This is NOT an HTML-to-PDF conversion. It regenerates the entire report
using the same audit data, with a layout optimized for print/PDF.

Usage:
    python generate_report_pdf.py input.json [output.pdf]

Dependencies:
    pip install reportlab

Input: JSON file with audit data (same format as generate_report_html.py)
Output: Professional A4 PDF with Copy House branding
"""

import json
import sys
import math
from datetime import datetime
from pathlib import Path

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm, cm
    from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
        PageBreak, KeepTogether, HRFlowable, Image
    )
    from reportlab.graphics.shapes import Drawing, Circle, Line, Polygon, String, Group
    from reportlab.graphics.charts.spider import SpiderChart
    from reportlab.graphics import renderPDF
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
except ImportError:
    print("Erreur : reportlab non installe.")
    print("Installation : pip install reportlab")
    sys.exit(1)


# --- BRAND COLORS ---
PRIMARY = colors.HexColor("#FF6B35")
BG_DARK = colors.HexColor("#0a0a0f")
TEXT_MAIN = colors.HexColor("#1a1a1a")
TEXT_MUTED = colors.HexColor("#666666")
TEXT_HEADING = colors.HexColor("#000000")
GREEN = colors.HexColor("#22c55e")
LIME = colors.HexColor("#84cc16")
YELLOW = colors.HexColor("#eab308")
ORANGE = colors.HexColor("#f97316")
RED = colors.HexColor("#ef4444")
BORDER_LIGHT = colors.HexColor("#e0e0e0")
BG_LIGHT = colors.HexColor("#f8f8f8")
WHITE = colors.white

GRADE_COLORS = {"A": GREEN, "B": LIME, "C": YELLOW, "D": ORANGE, "F": RED}


def grade_for(score):
    if score >= 90: return "A"
    if score >= 75: return "B"
    if score >= 60: return "C"
    if score >= 40: return "D"
    return "F"


def grade_color(grade):
    return GRADE_COLORS.get(grade, TEXT_MUTED)


# --- STYLES ---
def build_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        fontSize=24,
        leading=30,
        textColor=TEXT_HEADING,
        spaceAfter=6,
        fontName="Helvetica-Bold",
    ))

    styles.add(ParagraphStyle(
        "SectionTitle",
        parent=styles["Heading1"],
        fontSize=18,
        leading=24,
        textColor=TEXT_HEADING,
        spaceBefore=20,
        spaceAfter=10,
        fontName="Helvetica-Bold",
        borderWidth=0,
        borderPadding=0,
    ))

    styles.add(ParagraphStyle(
        "SubsectionTitle",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=TEXT_HEADING,
        spaceBefore=14,
        spaceAfter=6,
        fontName="Helvetica-Bold",
    ))

    styles.add(ParagraphStyle(
        "BodyText2",
        parent=styles["Normal"],
        fontSize=10,
        leading=15,
        textColor=TEXT_MAIN,
        spaceAfter=6,
    ))

    styles.add(ParagraphStyle(
        "MutedText",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        textColor=TEXT_MUTED,
        spaceAfter=4,
    ))

    styles.add(ParagraphStyle(
        "MetaInfo",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=TEXT_MUTED,
    ))

    styles.add(ParagraphStyle(
        "FooterText",
        parent=styles["Normal"],
        fontSize=8,
        leading=10,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER,
    ))

    styles.add(ParagraphStyle(
        "ScoreBig",
        parent=styles["Normal"],
        fontSize=48,
        leading=52,
        textColor=PRIMARY,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    ))

    styles.add(ParagraphStyle(
        "GradeLabel",
        parent=styles["Normal"],
        fontSize=14,
        leading=18,
        alignment=TA_CENTER,
        fontName="Helvetica-Bold",
    ))

    styles.add(ParagraphStyle(
        "RewriteBefore",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=TEXT_MUTED,
        backColor=colors.HexColor("#fff5f5"),
        borderWidth=0.5,
        borderColor=colors.HexColor("#fecaca"),
        borderPadding=8,
    ))

    styles.add(ParagraphStyle(
        "RewriteAfter",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        textColor=TEXT_MAIN,
        backColor=colors.HexColor("#f0fdf4"),
        borderWidth=0.5,
        borderColor=colors.HexColor("#bbf7d0"),
        borderPadding=8,
    ))

    return styles


# --- RADAR CHART DRAWING ---
def draw_radar(categories, width=220, height=220):
    d = Drawing(width, height)
    cx, cy = width / 2, height / 2
    r = min(cx, cy) - 30
    n = len(categories)
    if n < 3:
        return d

    for level in [0.25, 0.5, 0.75, 1.0]:
        points = []
        for i in range(n):
            angle = (2 * math.pi * i / n) - math.pi / 2
            points.extend([
                cx + r * level * math.cos(angle),
                cy + r * level * math.sin(angle)
            ])
        poly = Polygon(points)
        poly.fillColor = None
        poly.strokeColor = BORDER_LIGHT
        poly.strokeWidth = 0.5
        d.add(poly)

    for i in range(n):
        angle = (2 * math.pi * i / n) - math.pi / 2
        x2 = cx + r * math.cos(angle)
        y2 = cy + r * math.sin(angle)
        line = Line(cx, cy, x2, y2)
        line.strokeColor = BORDER_LIGHT
        line.strokeWidth = 0.5
        d.add(line)

        lx = cx + (r + 18) * math.cos(angle)
        ly = cy + (r + 18) * math.sin(angle)
        label = String(lx, ly, categories[i]["name"])
        label.fontSize = 7
        label.fillColor = TEXT_MUTED
        label.textAnchor = "middle"
        d.add(label)

    data_points = []
    for i in range(n):
        angle = (2 * math.pi * i / n) - math.pi / 2
        val = (categories[i].get("score", 0)) / 100
        data_points.extend([
            cx + r * val * math.cos(angle),
            cy + r * val * math.sin(angle)
        ])
    data_poly = Polygon(data_points)
    data_poly.fillColor = colors.Color(1, 0.42, 0.21, alpha=0.2)
    data_poly.strokeColor = PRIMARY
    data_poly.strokeWidth = 1.5
    d.add(data_poly)

    for i in range(0, len(data_points), 2):
        dot = Circle(data_points[i], data_points[i + 1], 3)
        dot.fillColor = PRIMARY
        dot.strokeColor = None
        d.add(dot)

    return d


# --- GAUGE DRAWING ---
def draw_gauge(score, size=50):
    d = Drawing(size, size)
    cx, cy = size / 2, size / 2
    r = size / 2 - 5
    grade = grade_for(score)
    color = grade_color(grade)

    bg_circle = Circle(cx, cy, r)
    bg_circle.fillColor = None
    bg_circle.strokeColor = BORDER_LIGHT
    bg_circle.strokeWidth = 4
    d.add(bg_circle)

    if score > 0:
        from reportlab.graphics.shapes import ArcPath, Wedge
        start_angle = 90
        extent = -3.6 * score

        wedge = Wedge(cx, cy, r, start_angle, start_angle + extent,
                      radius1=r - 2, yradius1=r - 2)
        wedge.fillColor = None
        wedge.strokeColor = color
        wedge.strokeWidth = 4
        d.add(wedge)

    label = String(cx, cy - 3, str(score))
    label.fontSize = 12
    label.fontName = "Helvetica-Bold"
    label.fillColor = color
    label.textAnchor = "middle"
    d.add(label)

    return d


# --- TABLE HELPERS ---
def severity_text(sev):
    return sev.upper() if sev else ""


def result_color(result):
    return {"PASS": GREEN, "WARNING": YELLOW, "FAIL": RED}.get(result, TEXT_MUTED)


def make_checks_table(checks, styles):
    header = [
        Paragraph("<b>#</b>", styles["MutedText"]),
        Paragraph("<b>Check</b>", styles["MutedText"]),
        Paragraph("<b>Sev.</b>", styles["MutedText"]),
        Paragraph("<b>Resultat</b>", styles["MutedText"]),
        Paragraph("<b>Commentaire</b>", styles["MutedText"]),
    ]
    data = [header]

    for i, c in enumerate(checks):
        res_color = result_color(c.get("result", ""))
        data.append([
            Paragraph(str(i + 1), styles["MutedText"]),
            Paragraph(c.get("title", ""), styles["BodyText2"]),
            Paragraph(f"<font color='#{TEXT_MUTED.hexval()[2:]}'>{c.get('severity', '')}</font>", styles["MutedText"]),
            Paragraph(f"<font color='#{res_color.hexval()[2:]}'><b>{c.get('result', '')}</b></font>", styles["BodyText2"]),
            Paragraph(c.get("comment", ""), styles["MutedText"]),
        ])

    col_widths = [25, 140, 55, 55, 200]
    t = Table(data, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ]))
    return t


def make_action_table(actions, priority_label, styles):
    elements = []
    elements.append(Paragraph(f"<b>Priorite {priority_label}</b>", styles["SubsectionTitle"]))

    header = [
        Paragraph("<b>#</b>", styles["MutedText"]),
        Paragraph("<b>Action</b>", styles["MutedText"]),
        Paragraph("<b>Categorie</b>", styles["MutedText"]),
        Paragraph("<b>Effort</b>", styles["MutedText"]),
        Paragraph("<b>Impact</b>", styles["MutedText"]),
    ]
    data = [header]
    for i, a in enumerate(actions):
        data.append([
            Paragraph(str(i + 1), styles["MutedText"]),
            Paragraph(a.get("action", ""), styles["BodyText2"]),
            Paragraph(a.get("category", ""), styles["MutedText"]),
            Paragraph(a.get("effort", ""), styles["MutedText"]),
            Paragraph(a.get("impact", ""), styles["MutedText"]),
        ])

    t = Table(data, colWidths=[25, 200, 90, 70, 70], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    elements.append(t)
    elements.append(Spacer(1, 10))
    return elements


# --- HEADER / FOOTER CALLBACKS ---
def make_header_footer(data):
    company = data.get("company", "Entreprise")
    score = data.get("score", 0)
    grade = grade_for(score)

    def header_footer(canvas, doc):
        canvas.saveState()

        # Header line
        canvas.setStrokeColor(PRIMARY)
        canvas.setLineWidth(2)
        canvas.line(20 * mm, A4[1] - 15 * mm, A4[0] - 20 * mm, A4[1] - 15 * mm)

        canvas.setFont("Helvetica-Bold", 9)
        canvas.setFillColor(TEXT_HEADING)
        canvas.drawString(20 * mm, A4[1] - 13 * mm, f"Copy House — Audit Marketing : {company}")

        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(TEXT_MUTED)
        canvas.drawRightString(A4[0] - 20 * mm, A4[1] - 13 * mm, f"Score : {score}/100 ({grade})")

        # Footer
        canvas.setStrokeColor(BORDER_LIGHT)
        canvas.setLineWidth(0.5)
        canvas.line(20 * mm, 15 * mm, A4[0] - 20 * mm, 15 * mm)

        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(TEXT_MUTED)
        canvas.drawString(20 * mm, 10 * mm, "Copy House — copyhouse.fr/communaute")
        canvas.drawRightString(A4[0] - 20 * mm, 10 * mm, f"Page {doc.page}")

        canvas.restoreState()

    return header_footer


# --- SCORE SUMMARY TABLE ---
def make_score_summary(categories, styles):
    header = [
        Paragraph("<b>Categorie</b>", styles["MutedText"]),
        Paragraph("<b>Score</b>", styles["MutedText"]),
        Paragraph("<b>Grade</b>", styles["MutedText"]),
    ]
    data = [header]
    for cat in categories:
        s = cat.get("score", 0)
        g = grade_for(s)
        gc = grade_color(g)
        data.append([
            Paragraph(cat.get("name", ""), styles["BodyText2"]),
            Paragraph(f"<font color='#{gc.hexval()[2:]}'><b>{s}/100</b></font>", styles["BodyText2"]),
            Paragraph(f"<font color='#{gc.hexval()[2:]}'><b>{g}</b></font>", styles["BodyText2"]),
        ])

    t = Table(data, colWidths=[250, 80, 60], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BG_LIGHT),
        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ]))
    return t


# --- BUILD PDF ---
def build_pdf(data, output_path):
    styles = build_styles()
    elements = []

    company = data.get("company", "Entreprise")
    score = data.get("score", 0)
    grade = grade_for(score)
    gc = grade_color(grade)

    # === COVER / EXECUTIVE SUMMARY ===
    elements.append(Spacer(1, 30))
    elements.append(Paragraph(f"Audit Marketing : {company}", styles["ReportTitle"]))

    meta_parts = []
    if data.get("date"):
        meta_parts.append(f"<b>Date :</b> {data['date']}")
    if data.get("url"):
        meta_parts.append(f"<b>Site :</b> {data['url']}")
    if data.get("industry"):
        meta_parts.append(f"<b>Industrie :</b> {data['industry']}")
    if meta_parts:
        elements.append(Paragraph(" | ".join(meta_parts), styles["MetaInfo"]))

    elements.append(Spacer(1, 20))
    elements.append(Paragraph(str(score), styles["ScoreBig"]))

    grade_style = ParagraphStyle(
        "GradeDynamic", parent=styles["GradeLabel"], textColor=gc
    )
    elements.append(Paragraph(f"Grade {grade}", grade_style))
    elements.append(Spacer(1, 20))

    # Score summary table
    categories = data.get("categories", [])
    if categories:
        elements.append(make_score_summary(categories, styles))
        elements.append(Spacer(1, 16))

    # Radar chart
    if len(categories) >= 3:
        radar = draw_radar(categories)
        elements.append(KeepTogether([
            Paragraph("Vue d'ensemble", styles["SubsectionTitle"]),
            radar,
            Spacer(1, 10),
        ]))

    # Executive summary text
    sections = data.get("sections", [])
    exec_section = next((s for s in sections if "sum" in s.get("title", "").lower() or "ex" in s.get("title", "").lower()), None)
    if exec_section and exec_section.get("summary"):
        elements.append(Paragraph(exec_section["summary"], styles["BodyText2"]))

    elements.append(PageBreak())

    # === SECTIONS ===
    for section in sections:
        title = section.get("title", "Section")
        s_score = section.get("score")
        confidence = section.get("confidence", "")

        score_text = ""
        if s_score is not None:
            sg = grade_for(s_score)
            sgc = grade_color(sg)
            score_text = f" — <font color='#{sgc.hexval()[2:]}'>{s_score}/100 ({sg})</font>"

        conf_text = ""
        if confidence:
            conf_text = f" <font color='#{TEXT_MUTED.hexval()[2:]}'>[{confidence}]</font>"

        elements.append(Paragraph(f"{title}{score_text}{conf_text}", styles["SectionTitle"]))
        elements.append(HRFlowable(width="100%", thickness=1, color=BORDER_LIGHT, spaceAfter=10))

        # Summary
        if section.get("summary"):
            elements.append(Paragraph(section["summary"], styles["BodyText2"]))
            elements.append(Spacer(1, 6))

        # Checks table
        if section.get("checks"):
            elements.append(make_checks_table(section["checks"], styles))
            elements.append(Spacer(1, 10))

        # Findings
        if section.get("findings"):
            for f in section["findings"]:
                res = f.get("result", "")
                sev = f.get("severity", "")
                rc = result_color(res)
                finding_text = (
                    f"<font color='#{rc.hexval()[2:]}'><b>[{res}]</b></font> "
                    f"<b>{f.get('title', '')}</b>"
                    f" <font color='#{TEXT_MUTED.hexval()[2:]}'>[{sev}]</font>"
                )
                elements.append(Paragraph(finding_text, styles["BodyText2"]))
                if f.get("description"):
                    elements.append(Paragraph(f["description"], styles["MutedText"]))
                elements.append(Spacer(1, 4))

        # Subsections
        if section.get("subsections"):
            for sub in section["subsections"]:
                elements.append(Paragraph(sub.get("title", ""), styles["SubsectionTitle"]))
                if sub.get("content"):
                    elements.append(Paragraph(sub["content"], styles["BodyText2"]))
                if sub.get("checks"):
                    elements.append(make_checks_table(sub["checks"], styles))
                if sub.get("findings"):
                    for f in sub["findings"]:
                        res = f.get("result", "")
                        rc = result_color(res)
                        elements.append(Paragraph(
                            f"<font color='#{rc.hexval()[2:]}'><b>[{res}]</b></font> "
                            f"<b>{f.get('title', '')}</b>",
                            styles["BodyText2"]
                        ))
                        if f.get("description"):
                            elements.append(Paragraph(f["description"], styles["MutedText"]))

        # Rewrites
        if section.get("rewrites"):
            elements.append(Paragraph("<b>Rewrites proposes</b>", styles["SubsectionTitle"]))
            for rw in section["rewrites"]:
                label = rw.get("label", "Rewrite")
                elements.append(Paragraph(f"<font color='#{PRIMARY.hexval()[2:]}'><b>{label}</b></font>", styles["BodyText2"]))
                elements.append(Paragraph(f"<b>Avant :</b> <strike>{rw.get('before', '')}</strike>", styles["RewriteBefore"]))
                elements.append(Paragraph(f"<b>Apres :</b> {rw.get('after', '')}", styles["RewriteAfter"]))
                if rw.get("justification"):
                    elements.append(Paragraph(rw["justification"], styles["MutedText"]))
                elements.append(Spacer(1, 8))

        # Lead magnets
        if section.get("lead_magnets"):
            elements.append(Paragraph("<b>Propositions de Lead Magnets</b>", styles["SubsectionTitle"]))
            for m in section["lead_magnets"]:
                elements.append(Paragraph(
                    f"<font color='#{PRIMARY.hexval()[2:]}'><b>{m.get('type', '')} — "
                    f"Conv. estimee : {m.get('conversion', '?')}%</b></font>",
                    styles["MutedText"]
                ))
                elements.append(Paragraph(f"<b>{m.get('title', '')}</b>", styles["BodyText2"]))
                if m.get("why"):
                    elements.append(Paragraph(m["why"], styles["MutedText"]))
                if m.get("outline"):
                    for item in m["outline"]:
                        elements.append(Paragraph(f"  - {item}", styles["BodyText2"]))
                if m.get("headline"):
                    elements.append(Paragraph(
                        f"<b>Opt-in :</b> {m['headline']}",
                        styles["BodyText2"]
                    ))
                elements.append(Spacer(1, 8))

        # Calendar
        if section.get("calendar"):
            elements.append(Paragraph("<b>Calendrier de contenu</b>", styles["SubsectionTitle"]))
            for week in section["calendar"]:
                elements.append(Paragraph(week.get("title", ""), styles["SubsectionTitle"]))
                if week.get("days"):
                    cal_header = [
                        Paragraph("<b>Jour</b>", styles["MutedText"]),
                        Paragraph("<b>Plateforme</b>", styles["MutedText"]),
                        Paragraph("<b>Format</b>", styles["MutedText"]),
                        Paragraph("<b>Pilier</b>", styles["MutedText"]),
                        Paragraph("<b>Hook</b>", styles["MutedText"]),
                    ]
                    cal_data = [cal_header]
                    for d in week["days"]:
                        cal_data.append([
                            Paragraph(d.get("day", ""), styles["BodyText2"]),
                            Paragraph(d.get("platform", ""), styles["MutedText"]),
                            Paragraph(d.get("format", ""), styles["MutedText"]),
                            Paragraph(d.get("pillar", ""), styles["MutedText"]),
                            Paragraph(d.get("hook", ""), styles["MutedText"]),
                        ])
                    ct = Table(cal_data, colWidths=[55, 70, 65, 50, 210], repeatRows=1)
                    ct.setStyle(TableStyle([
                        ("BACKGROUND", (0, 0), (-1, 0), BG_LIGHT),
                        ("GRID", (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("TOPPADDING", (0, 0), (-1, -1), 3),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                        ("FONTSIZE", (0, 0), (-1, -1), 8),
                    ]))
                    elements.append(ct)
                    elements.append(Spacer(1, 6))

        # Action tables
        if section.get("actions"):
            acts = section["actions"]
            for key, label in [("critical", "Critique"), ("high", "Haute"), ("medium", "Moyenne"), ("low", "Basse")]:
                if acts.get(key):
                    elements.extend(make_action_table(acts[key], label, styles))

        # Quick wins
        if section.get("quick_wins"):
            elements.append(Paragraph("<b>Quick Wins</b>", styles["SubsectionTitle"]))
            for i, w in enumerate(section["quick_wins"]):
                elements.append(Paragraph(
                    f"<font color='#{PRIMARY.hexval()[2:]}'><b>{i + 1}.</b></font> "
                    f"<b>{w.get('title', '')}</b> — {w.get('description', '')} "
                    f"<font color='#{TEXT_MUTED.hexval()[2:]}'>[{w.get('time', '')} | {w.get('category', '')}]</font>",
                    styles["BodyText2"]
                ))

        # Strategic questions
        if section.get("questions"):
            elements.append(Paragraph("<b>Questions strategiques</b>", styles["SubsectionTitle"]))
            for q in section["questions"]:
                elements.append(Paragraph(
                    f"<i>{q.get('question', '')}</i>",
                    styles["BodyText2"]
                ))
                if q.get("context"):
                    elements.append(Paragraph(q["context"], styles["MutedText"]))
                elements.append(Spacer(1, 6))

        # Raw HTML content
        if section.get("content_html"):
            elements.append(Paragraph(section["content_html"], styles["BodyText2"]))

        elements.append(Spacer(1, 16))

    # === FOOTER ===
    elements.append(HRFlowable(width="100%", thickness=1, color=BORDER_LIGHT, spaceBefore=20, spaceAfter=10))
    elements.append(Paragraph(
        "Niveaux de confiance : Complet = toutes sources | Partiel = sources partielles | Limite = signaux minimaux",
        styles["FooterText"]
    ))
    elements.append(Spacer(1, 6))
    elements.append(Paragraph(
        "Construit par Copy House — copyhouse.fr/communaute — copyhouse.fr/newsletter",
        styles["FooterText"]
    ))

    # === BUILD DOC ===
    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=20 * mm,
        rightMargin=20 * mm,
        topMargin=22 * mm,
        bottomMargin=20 * mm,
        title=f"Audit Marketing — {company}",
        author="Copy House",
        subject="Rapport d'audit marketing",
    )

    doc.build(elements, onFirstPage=make_header_footer(data), onLaterPages=make_header_footer(data))
    return str(output_path)


# --- MAIN ---
def load_audit_data(json_path):
    path = Path(json_path)
    if not path.exists():
        print(f"Erreur : fichier JSON introuvable : {json_path}")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_data(data):
    if "date" not in data:
        data["date"] = datetime.now().strftime("%d/%m/%Y")
    if "company" not in data:
        data["company"] = "Entreprise"
    if "score" not in data:
        data["score"] = 0
    if "categories" not in data:
        data["categories"] = []
    if "sections" not in data:
        data["sections"] = []
    return data


def generate_output_path(data, output_arg=None):
    if output_arg:
        return Path(output_arg)
    company = data.get("company", "audit")
    safe_name = "".join(c if c.isalnum() or c in "-_ " else "" for c in company)
    safe_name = safe_name.strip().replace(" ", "-").lower()
    date_str = datetime.now().strftime("%Y%m%d")
    return Path(f"audit-{safe_name}-{date_str}.pdf")


def main():
    if len(sys.argv) < 2:
        print("Usage : python generate_report_pdf.py input.json [output.pdf]")
        print("")
        print("  input.json   Donnees d'audit (scores, findings, rewrites)")
        print("  output.pdf   Chemin de sortie (optionnel, genere automatiquement)")
        print("")
        print("Dependance : pip install reportlab")
        sys.exit(1)

    json_path = sys.argv[1]
    output_arg = sys.argv[2] if len(sys.argv) > 2 else None

    data = load_audit_data(json_path)
    data = validate_data(data)

    output_path = generate_output_path(data, output_arg)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    result = build_pdf(data, output_path)

    print(f"PDF genere : {result}")
    print(f"  Entreprise : {data.get('company')}")
    print(f"  Score : {data.get('score')}/100 ({grade_for(data.get('score', 0))})")
    print(f"  Sections : {len(data.get('sections', []))}")
    print(f"  Pages : A4, marges 20mm")


if __name__ == "__main__":
    main()
