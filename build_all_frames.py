# -*- coding: utf-8 -*-
import os
import re
import html

repo_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020"

def clean(text):
    text = re.sub(r"\*\*|\*", "", text)
    return text.strip()

def parse_standard_spec(filename):
    path = os.path.join(repo_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    cards = []
    sections = re.split(r"\n###\s+", text)
    for sec in sections[1:]:
        lines = [l.strip() for l in sec.split("\n") if l.strip()]
        if not lines:
            continue
        title = lines[0]
        cat, question, why, deliverable, tip = "", "", "", "", ""
        how = []
        mode = None
        for l in lines:
            if "正面分類" in l:
                cat = l.replace("* **正面分類**：", "").strip()
            elif "核心問句" in l:
                question = l.replace("* **核心問句**：", "").strip()
            elif "**How" in l:
                mode = "how"
            elif "**Why" in l:
                mode = "why"
                why = re.sub(r"^\*\s*\*\*Why[（(].*?[）)]\*\*：\s*", "", l).strip()
            elif "交付成果" in l:
                mode = "deliverable"
                deliverable = re.sub(r"^\*\s*\*\*交付成果\*\*：\s*", "", l).strip()
            elif "5人團隊提示" in l:
                mode = "tip"
                tip = re.sub(r"^\*\s*\*\*5人團隊提示\*\*：\s*", "", l).strip()
            elif mode == "how" and (re.match(r"^\d+\.", l) or l.startswith("*")):
                cl = re.sub(r"^\d+\.\s*", "", l)
                cl = re.sub(r"^\*\s*", "", cl)
                how.append(cl)
            elif mode == "why" and not why:
                why = l.strip()
            elif mode == "deliverable" and not deliverable:
                deliverable = l.strip()
            elif mode == "tip" and not tip:
                tip = l.strip()
        
        cards.append({
            "title": title,
            "category": cat,
            "question": question,
            "how": " ".join(how[:3]),
            "why": why,
            "deliverable": deliverable,
            "tip": tip
        })
    return cards

def generate_frame_svg(frame_title, header_subtitle, header_color, frame_fill, sticky_color, pos_x, pos_y, cards, prefix):
    col_xs = [700, 4500, 8300, 12100, 15900]
    row_ys = [1200, 5600]
    
    svg = [
        '<svg>',
        f'<g data-frame="{frame_title}" transform="translate({pos_x}, {pos_y})">',
        f'<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="{frame_fill}" data-title="{frame_title}" />',
        f'<text x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="{header_color}">{header_subtitle}</text>'
    ]
    
    for i, c in enumerate(cards[:10]):
        cx = col_xs[i % 5]
        cy = row_ys[i // 5]
        
        content = (
            f"<b>{clean(c['title'])}</b><br/>"
            f"<i>{clean(c['category'])}</i><br/><br/>"
            f"<b>問句:</b> {clean(c['question'])}<br/><br/>"
            f"<b>HOW:</b> {clean(c['how'])}<br/><br/>"
            f"<b>WHY:</b> {clean(c['why'])}<br/><br/>"
            f"<b>交付:</b> {clean(c['deliverable'])}<br/>"
            f"<b>提示:</b> {clean(c['tip'])}"
        )
        esc = html.escape(content, quote=True)
        svg.append(
            f'<rect id="{prefix}_{i+1:02d}" data-type="sticky" x="{cx}" y="{cy}" width="3400" height="3800" '
            f'data-color="{sticky_color}" data-content="{esc}" />'
        )
    
    svg.append('</g>')
    svg.append('</svg>')
    return "".join(svg)

# Concept
concept_cards = parse_standard_spec("02_Concept.md")
svg_02 = generate_frame_svg(
    "02. 概念設計 Concept（10張）",
    "02. 概念設計 Concept · 視覺世界觀與風格資產",
    "#bd0a0a", "#fff0f0", "light_pink",
    -13000, -205000,
    concept_cards, "con"
)
with open(os.path.join(repo_dir, "frame_02.svg"), "w", encoding="utf-8") as f:
    f.write(svg_02)

# Storyboard
storyboard_cards = parse_standard_spec("03_Storyboard.md")
svg_03 = generate_frame_svg(
    "03. 分鏡 Storyboard（10張）",
    "03. 分鏡 Storyboard · 鏡頭語言與動態腳本",
    "#305bab", "#f0f5fd", "cyan",
    9000, -205000,
    storyboard_cards, "stb"
)
with open(os.path.join(repo_dir, "frame_03.svg"), "w", encoding="utf-8") as f:
    f.write(svg_03)

# Animation
animation_cards = parse_standard_spec("04_Animation.md")
svg_04 = generate_frame_svg(
    "04. 動畫 Animation（10張）",
    "04. 動畫 Animation · 律動法則與動態表演",
    "#067429", "#eaf9ef", "green",
    -35000, -192000,
    animation_cards, "ani"
)
with open(os.path.join(repo_dir, "frame_04.svg"), "w", encoding="utf-8") as f:
    f.write(svg_04)

# VFX
vfx_all = parse_standard_spec("05_VFX_Comp_Rules.md")
vfx_cards = vfx_all[:10]
svg_05 = generate_frame_svg(
    "05. 特效與合成 VFX & Comp（10張）",
    "05. 特效與合成 VFX & Comp · 光影氛圍與母帶品質",
    "#6631d7", "#f4f2fd", "violet",
    -13000, -192000,
    vfx_cards, "vfx"
)
with open(os.path.join(repo_dir, "frame_05.svg"), "w", encoding="utf-8") as f:
    f.write(svg_05)

# Rule Card (Frame 6)
rule_card = vfx_all[10] if len(vfx_all) > 10 else None
svg_06_parts = [
    '<svg>',
    '<g data-frame="06. 核心規則卡 Rule Card（5人團隊）" transform="translate(9000, -192000)">',
    '<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#fff5ed" data-title="06. 核心規則卡 Rule Card（5人團隊）" />',
    '<text x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#9b4a08">06. 核心規則 Rule · 5人團隊多工兼任矩陣與秒級決策律</text>'
]

# We can put 3 big comprehensive stickies for Rule Card:
# Sticky 1: 5人兼任角色矩陣 (RACI)
raci_content = (
    "<b>【一、5人小團隊兼任角色矩陣】</b><br/>"
    "<i>核心規則 · 全局協同</i><br/><br/>"
    "<b>成員 A (主導):</b> 編導 (劇本/Picture Lock) ＋ 剪輯與聲音<br/><br/>"
    "<b>成員 B (主視覺):</b> 概念設計 (色彩/角色/場景) ＋ 背景繪製<br/><br/>"
    "<b>成員 C (動態核心):</b> 分鏡 / 動態腳本 (Animatic) ＋ 關鍵原畫<br/><br/>"
    "<b>成員 D (動態執行):</b> 動畫師 (原畫/中割/清線著色資產化)<br/><br/>"
    "<b>成員 E (後期基石):</b> 特效合成 (圖層管理/2D特效/全片調色母帶)"
)
raci_esc = html.escape(raci_content, quote=True)
svg_06_parts.append(
    f'<rect id="rule_01" data-type="sticky" x="700" y="1200" width="5800" height="8200" '
    f'data-color="orange" data-content="{raci_esc}" />'
)

# Sticky 2: 牌卡調用機制
process_content = (
    "<b>【二、IDEO 牌卡三階調用機制】</b><br/>"
    "<i>日常運作與卡關應對</i><br/><br/>"
    "<b>1. 每日 10 分鐘立會 (Standup):</b><br/>"
    "每位成員抽取當天負責職位的 1 張方法卡，作為今日交付的核心標準。<br/><br/>"
    "<b>2. 卡關紅燈召喚 (Blocker):</b><br/>"
    "當某環節延遲超過 1 天，當事人亮出該步驟卡牌，團隊停止發散爭論，嚴格執行卡牌上的 HOW 步驟與防坑提示。<br/><br/>"
    "<b>3. 交付驗收:</b><br/>"
    "依據各卡牌背面「交付成果 Deliverable」標準點交資產，不合格一律原路退件。"
)
process_esc = html.escape(process_content, quote=True)
svg_06_parts.append(
    f'<rect id="rule_02" data-type="sticky" x="7000" y="1200" width="5800" height="8200" '
    f'data-color="yellow" data-content="{process_esc}" />'
)

# Sticky 3: 爭端三秒裁決律
decision_content = (
    "<b>【三、爭議終結三秒律 (Tiebreaker)】</b><br/>"
    "<i>消除內耗 · 秒級定案</i><br/><br/>"
    "<b>故事與片長爭議:</b><br/>"
    "👉 <b>成員 A（編導）</b> 擁有一票否決權。<br/><br/>"
    "<b>畫風與視覺風格爭議:</b><br/>"
    "👉 <b>成員 B（概念設計）</b> 擁有一票定奪權。<br/><br/>"
    "<b>能不能如期做出來的產能爭議:</b><br/>"
    "👉 <b>成員 C/D（動畫）與 E（合成）</b> 擁有產能拒絕權。<br/><br/>"
    "<b>核心目的:</b> 告別學生組無休止開會，賦予小團隊軍隊般清晰的指揮鏈！"
)
decision_esc = html.escape(decision_content, quote=True)
svg_06_parts.append(
    f'<rect id="rule_03" data-type="sticky" x="13300" y="1200" width="5800" height="8200" '
    f'data-color="orange" data-content="{decision_esc}" />'
)

svg_06_parts.append('</g>')
svg_06_parts.append('</svg>')
svg_06 = "".join(svg_06_parts)
with open(os.path.join(repo_dir, "frame_06.svg"), "w", encoding="utf-8") as f:
    f.write(svg_06)

print("Generated frames 02, 03, 04, 05, 06 successfully!")
