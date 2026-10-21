# -*- coding: utf-8 -*-
import os
import html
from update_all_cards import cards_03, cards_04, cards_05

output_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020"

xs = [700, 4500, 8300, 12100, 15900]
ys = [1200, 5600]

def make_sticky_content(c):
    return (
        f"<b>{c['title']}</b><br/>"
        f"<i>{c['cat']}</i><br/><br/>"
        f"<b>HOW:</b> {c['how']}<br/><br/>"
        f"<b>WHY:</b> {c['why']}<br/><br/>"
        f"<b>案例:</b> {c['example']}"
    )

# --- Frame 03 (Storyboard) ---
stb_delete_ids = [
    "3458764687915609886", "3458764687915609887", "3458764687915609889", "3458764687915609890", "3458764687915609891",
    "3458764687915609892", "3458764687915609893", "3458764687915609894", "3458764687915609895", "3458764687915609896"
]
f03_lines = ['<svg>']
for did in stb_delete_ids:
    f03_lines.append(f'<rect data-miro-id="{did}" data-deleted="true" />')
f03_lines.append('<g data-miro-id="3458764687915609874" data-frame="03. 分鏡 Storyboard（10張）" transform="translate(9000, -205000)">')
f03_lines.append('<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#f0f5fd" data-title="03. 分鏡 Storyboard（10張）" />')
f03_lines.append('<text data-miro-id="3458764687915609885" x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#0c5db9">03. 分鏡 Storyboard · 鏡頭語言與動態腳本</text>')
for idx, c in enumerate(cards_03):
    x = xs[idx % 5]
    y = ys[idx // 5]
    content = make_sticky_content(c)
    esc = html.escape(content, quote=True)
    f03_lines.append(f'<rect id="stb_{idx+1:02d}" data-type="sticky" x="{x}" y="{y}" width="3400" height="3800" data-color="cyan" data-content="{esc}" />')
f03_lines.append('</g>')
f03_lines.append('</svg>')
with open(os.path.join(output_dir, "frame_03_update.svg"), "w", encoding="utf-8") as f:
    f.write("\n".join(f03_lines))

# --- Frame 04 (Animation) ---
ani_delete_ids = [
    "3458764687915673858", "3458764687915673859", "3458764687915673860", "3458764687915673861", "3458764687915673862",
    "3458764687915673863", "3458764687915673864", "3458764687915673865", "3458764687915673866", "3458764687915673867"
]
f04_lines = ['<svg>']
for did in ani_delete_ids:
    f04_lines.append(f'<rect data-miro-id="{did}" data-deleted="true" />')
f04_lines.append('<g data-miro-id="3458764687915673843" data-frame="04. 動畫 Animation（10張）" transform="translate(-35000, -192000)">')
f04_lines.append('<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#eaf9ef" data-title="04. 動畫 Animation（10張）" />')
f04_lines.append('<text data-miro-id="3458764687915673857" x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#087532">04. 動畫 Animation · 律動法則與動態表演</text>')
for idx, c in enumerate(cards_04):
    x = xs[idx % 5]
    y = ys[idx // 5]
    content = make_sticky_content(c)
    esc = html.escape(content, quote=True)
    f04_lines.append(f'<rect id="ani_{idx+1:02d}" data-type="sticky" x="{x}" y="{y}" width="3400" height="3800" data-color="green" data-content="{esc}" />')
f04_lines.append('</g>')
f04_lines.append('</svg>')
with open(os.path.join(output_dir, "frame_04_update.svg"), "w", encoding="utf-8") as f:
    f.write("\n".join(f04_lines))

# --- Frame 05 (VFX & Comp) ---
vfx_delete_ids = [
    "3458764687915734495", "3458764687915734496", "3458764687915734497", "3458764687915734498", "3458764687915734500",
    "3458764687915734501", "3458764687915734502", "3458764687915734503", "3458764687915734504", "3458764687915734505"
]
f05_lines = ['<svg>']
for did in vfx_delete_ids:
    f05_lines.append(f'<rect data-miro-id="{did}" data-deleted="true" />')
f05_lines.append('<g data-miro-id="3458764687915734479" data-frame="05. 特效與合成 VFX &amp; Comp（10張）" transform="translate(-13000, -192000)">')
f05_lines.append('<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#f4f2fd" data-title="05. 特效與合成 VFX &amp; Comp（10張）" />')
f05_lines.append('<text data-miro-id="3458764687915734492" x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#6028c5">05. 特效與合成 VFX &amp; Comp · 氛圍渲染與最終母帶</text>')
for idx, c in enumerate(cards_05):
    x = xs[idx % 5]
    y = ys[idx // 5]
    content = make_sticky_content(c)
    esc = html.escape(content, quote=True)
    f05_lines.append(f'<rect id="vfx_{idx+1:02d}" data-type="sticky" x="{x}" y="{y}" width="3400" height="3800" data-color="violet" data-content="{esc}" />')
f05_lines.append('</g>')
f05_lines.append('</svg>')
with open(os.path.join(output_dir, "frame_05_update.svg"), "w", encoding="utf-8") as f:
    f.write("\n".join(f05_lines))

# --- Frame 06 (Rule Card) ---
rule_delete_ids = ["3458764687915734824", "3458764687915734825", "3458764687915734826"]
f06_lines = ['<svg>']
for did in rule_delete_ids:
    f06_lines.append(f'<rect data-miro-id="{did}" data-deleted="true" />')
f06_lines.append('<g data-miro-id="3458764687915734815" data-frame="06. 核心規則卡 Rule Card（5人團隊）" transform="translate(9000, -192000)">')
f06_lines.append('<rect data-type="frame" x="0" y="0" width="20000" height="10500" fill="#fff5ed" data-title="06. 核心規則卡 Rule Card（5人團隊）" />')
f06_lines.append('<text data-miro-id="3458764687915734823" x="700" y="700" font-family="noto_sans" font-size="400" font-weight="bold" fill="#bb4d00">06. 核心規則 Rule · 5人團隊多工兼任矩陣與秒級決策律</text>')

rules_data = [
    {
        "id": "rule_01",
        "title": "RULE-01. 5人團隊多工兼任角色矩陣",
        "cat": "<b>[Learn]</b> · 全局協同",
        "how": "成員 A 主導編導與剪輯聲音；成員 B 主導概念與背景；成員 C 主導分鏡與原畫；成員 D 主導動畫執行與中割；成員 E 主導特效合成與母帶 QC。",
        "why": "5 人小組不准有純指揮官，全員皆兵、主責一道工序並兼任下游，產能最大化。",
        "example": "分鏡師畫完立刻接手關鍵原畫，避免交接解釋成本，作畫進度直接提前 1 週。",
        "x": 700, "y": 1977, "w": 5600, "h": 7500, "color": "orange"
    },
    {
        "id": "rule_02",
        "title": "RULE-02. IDEO 卡牌三階調用機制",
        "cat": "<b>[Try]</b> · 敏捷排障",
        "how": "每日立會抽 1 張當前卡作為產出標準；任何環節卡關超 1 天立刻亮紅燈強制按卡執行；驗收依交付標的點交。",
        "why": "用客觀工具卡代替主觀爭論，把溝通與扯皮成本降到最低。",
        "example": "概念設計卡關 2 天，全員亮出「情緒板過濾卡」強制砍到剩 20 張參考圖，當天下午順利定案。",
        "x": 7000, "y": 1977, "w": 5600, "h": 7500, "color": "yellow"
    },
    {
        "id": "rule_03",
        "title": "RULE-03. 爭端終結三秒律",
        "cat": "<b>[Ask]</b> · 秒級定案",
        "how": "故事時長爭議由成員 A（編導）一票否決；畫風審美由成員 B（概念）一票定奪；產能超時由成員 C/D/E（製作組）一票拒絕。",
        "why": "告別無休止的民主投票與空耗會議，賦予各領域負責人絕對裁決權。",
        "example": "會議爭論結局要不要死人超過 1 小時，編導行使一票否決權 3 秒定案，團隊立刻散會開工。",
        "x": 13300, "y": 1977, "w": 5600, "h": 7500, "color": "orange"
    }
]

for r in rules_data:
    content = make_sticky_content(r)
    esc = html.escape(content, quote=True)
    f06_lines.append(f'<rect id="{r["id"]}" data-type="sticky" x="{r["x"]}" y="{r["y"]}" width="{r["w"]}" height="{r["h"]}" data-color="{r["color"]}" data-content="{esc}" />')

f06_lines.append('</g>')
f06_lines.append('</svg>')
with open(os.path.join(output_dir, "frame_06_update.svg"), "w", encoding="utf-8") as f:
    f.write("\n".join(f06_lines))

print("All frame update SVGs (03, 04, 05, 06) built successfully!")
