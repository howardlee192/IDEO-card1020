# -*- coding: utf-8 -*-
import os
import re
import html
import json
import urllib.parse

repo_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020"

def clean_html(text):
    text = re.sub(r"\*\*|\*", "", text)
    return text.strip()

def build_directing_svg():
    path = os.path.join(repo_dir, "01_Directing.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    cards = []
    sections = re.split(r"\n###\s+", text)
    for sec in sections[1:]:
        lines = [l.strip() for l in sec.split("\n") if l.strip()]
        if not lines:
            continue
        title = lines[0]
        cat, how, why, ex = "", "", "", ""
        for l in lines:
            if "頂部分類" in l:
                cat = l.replace("* **頂部分類**：", "").strip()
            elif "HOW" in l:
                how = l.replace("* **HOW**：", "").strip()
            elif "WHY" in l:
                why = l.replace("* **WHY**：", "").strip()
            elif "案例" in l or "EXAMPLE" in l:
                ex = re.sub(r"^\*\s*\*\*(案例|EXAMPLE)\*\*：\s*", "", l).strip()
        cards.append((title, cat, how, why, ex))

    svg_parts = [
        '<svg>',
        '<g data-frame="01. 編導 Directing（10張）" transform="translate(-35000, -205000)">',
        '<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#fffbed" data-title="01. 編導 Directing（10張）" />',
        '<text x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#af7e04">01. 編導 Directing · 前期企劃與敘事結構</text>'
    ]

    col_xs = [700, 4500, 8300, 12100, 15900]
    row_ys = [1200, 5600]

    for i, (title, cat, how, why, ex) in enumerate(cards[:10]):
        c = i % 5
        r = i // 5
        x = col_xs[c]
        y = row_ys[r]
        
        # Build formatted sticky content
        content = (
            f"<b>{clean_html(title)}</b><br/>"
            f"<i>{clean_html(cat)}</i><br/><br/>"
            f"<b>HOW:</b> {clean_html(how)}<br/><br/>"
            f"<b>WHY:</b> {clean_html(why)}<br/><br/>"
            f"<b>案例:</b> {clean_html(ex)}"
        )
        escaped_content = html.escape(content, quote=True)
        svg_parts.append(
            f'<rect id="dir_{i+1:02d}" data-type="sticky" x="{x}" y="{y}" width="3400" height="3800" '
            f'data-color="yellow" data-content="{escaped_content}" />'
        )

    svg_parts.append('</g>')
    svg_parts.append('</svg>')
    return "".join(svg_parts)

if __name__ == "__main__":
    svg = build_directing_svg()
    print("SVG generated, length:", len(svg))
    with open(r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020\frame_01.svg", "w", encoding="utf-8") as f:
        f.write(svg)
