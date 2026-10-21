# -*- coding: utf-8 -*-
import html
import json
from update_all_cards import cards_02

delete_ids = [
    "3458764687915609099",
    "3458764687915609100",
    "3458764687915609101",
    "3458764687915609102",
    "3458764687915609104",
    "3458764687915609105",
    "3458764687915609106",
    "3458764687915609107",
    "3458764687915609108"
]

xs = [700, 4500, 8300, 12100, 15900]
ys = [1200, 5600]

lines = ['<svg>']
# Delete old stickies
for did in delete_ids:
    lines.append(f'<rect data-miro-id="{did}" data-deleted="true" />')

# Frame 02
lines.append('<g data-miro-id="3458764687915609085" data-frame="02. 概念設計 Concept（10張）" transform="translate(-13000, -205000)">')
lines.append('<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#fff0f0" data-title="02. 概念設計 Concept（10張）" />')
lines.append('<text data-miro-id="3458764687915609096" x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#bd0a0a">02. 概念設計 Concept · 視覺世界觀與風格資產</text>')

for idx, c in enumerate(cards_02):
    x = xs[idx % 5]
    y = ys[idx // 5]
    # Exact 01 format
    # <b>Title</b><br/><i>Category</i><br/><br/><b>HOW:</b> ...<br/><br/><b>WHY:</b> ...<br/><br/><b>案例:</b> ...
    content = (
        f"<b>{c['title']}</b><br/>"
        f"<i>{c['cat']}</i><br/><br/>"
        f"<b>HOW:</b> {c['how']}<br/><br/>"
        f"<b>WHY:</b> {c['why']}<br/><br/>"
        f"<b>案例:</b> {c['example']}"
    )
    content_escaped = html.escape(content, quote=True)
    lines.append(f'<rect id="con_{idx+1:02d}" data-type="sticky" x="{x}" y="{y}" width="3400" height="3800" data-color="light_pink" data-content="{content_escaped}" />')

lines.append('</g>')
lines.append('</svg>')

svg_str = "\n".join(lines)
out_path = r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020\frame_02_update.svg"
with open(out_path, "w", encoding="utf-8") as f:
    f.write(svg_str)

print("Saved frame_02_update.svg, length:", len(svg_str))
