#!/usr/bin/env python3
"""
generate_report_html.py
Generates the branded HTML audit report from a JSON data file.

Usage:
    python generate_report_html.py input.json [output.html]

Input: JSON file with audit data (scores, findings, rewrites, etc.)
Output: Self-contained HTML report file (dark-mode, Copy House branded)

The script reads the report template from templates/report.html,
injects the audit data as a JS object, and writes the final HTML.
"""

import json
import sys
import os
from datetime import datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).parent
TEMPLATE_PATH = SCRIPT_DIR.parent / "templates" / "report.html"


def load_template():
    if not TEMPLATE_PATH.exists():
        print(f"Erreur : template introuvable a {TEMPLATE_PATH}")
        sys.exit(1)
    return TEMPLATE_PATH.read_text(encoding="utf-8")


def load_audit_data(json_path):
    path = Path(json_path)
    if not path.exists():
        print(f"Erreur : fichier JSON introuvable : {json_path}")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def validate_data(data):
    """Minimal validation of required fields."""
    required = ["company", "score", "categories", "sections"]
    missing = [k for k in required if k not in data]
    if missing:
        print(f"Attention : champs manquants dans le JSON : {', '.join(missing)}")
        for k in missing:
            if k == "company":
                data[k] = "Entreprise"
            elif k == "score":
                data[k] = 0
            elif k in ("categories", "sections"):
                data[k] = []

    if "date" not in data:
        data["date"] = datetime.now().strftime("%d/%m/%Y")

    if "grade" not in data:
        s = data.get("score", 0)
        if s >= 90:
            data["grade"] = "A"
        elif s >= 75:
            data["grade"] = "B"
        elif s >= 60:
            data["grade"] = "C"
        elif s >= 40:
            data["grade"] = "D"
        else:
            data["grade"] = "F"

    return data


def inject_data(template_html, data):
    """Replace the JS data placeholder with actual audit data."""
    data_js = json.dumps(data, ensure_ascii=False, indent=2)

    injection = f"const AUDIT_DATA = {data_js};"
    modified = template_html.replace(
        "const AUDIT_DATA = window.__AUDIT_DATA__ || null;",
        injection
    )

    if "{{COMPANY}}" in modified:
        modified = modified.replace("{{COMPANY}}", data.get("company", "Entreprise"))

    return modified


def generate_output_path(data, output_arg=None):
    if output_arg:
        return Path(output_arg)

    company = data.get("company", "audit")
    safe_name = "".join(c if c.isalnum() or c in "-_ " else "" for c in company)
    safe_name = safe_name.strip().replace(" ", "-").lower()
    date_str = datetime.now().strftime("%Y%m%d")
    return Path(f"audit-{safe_name}-{date_str}.html")


def main():
    if len(sys.argv) < 2:
        print("Usage : python generate_report_html.py input.json [output.html]")
        print("")
        print("  input.json   Donnees d'audit (scores, findings, rewrites)")
        print("  output.html  Chemin de sortie (optionnel, genere automatiquement)")
        sys.exit(1)

    json_path = sys.argv[1]
    output_arg = sys.argv[2] if len(sys.argv) > 2 else None

    template = load_template()
    data = load_audit_data(json_path)
    data = validate_data(data)

    html = inject_data(template, data)
    output_path = generate_output_path(data, output_arg)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html, encoding="utf-8")

    print(f"Rapport genere : {output_path}")
    print(f"  Entreprise : {data.get('company')}")
    print(f"  Score : {data.get('score')}/100 ({data.get('grade')})")
    print(f"  Sections : {len(data.get('sections', []))}")
    print(f"  Categories : {len(data.get('categories', []))}")

    return str(output_path)


if __name__ == "__main__":
    main()
