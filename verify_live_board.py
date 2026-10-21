# -*- coding: utf-8 -*-
import json
import re
import html
import sys

# Set stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

with open(r"C:/Users/Admin/.gemini/antigravity/brain/95ae7192-ee66-4f3e-9f15-97fd27cf6cee/.system_generated/steps/439/output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

# Also load updated step 451 for Frame 01
with open(r"C:/Users/Admin/.gemini/antigravity/brain/95ae7192-ee66-4f3e-9f15-97fd27cf6cee/.system_generated/steps/451/output.txt", "r", encoding="utf-8") as f:
    data_01 = json.load(f)

svg = data.get("svg", "")
svg_01 = data_01.get("svg", "")

frames = [
    ("3458764687915550337", "01. 編導 Directing（10張）", svg_01),
    ("3458764687915609085", "02. 概念設計 Concept（10張）", svg),
    ("3458764687915609874", "03. 分鏡 Storyboard（10張）", svg),
    ("3458764687915673843", "04. 動畫 Animation（10張）", svg),
    ("3458764687915734479", "05. 特效與合成 VFX & Comp（10張）", svg),
    ("3458764687915734815", "06. 核心規則卡 Rule Card（5人團隊）", svg),
]

print(f"=== Found {len(frames)} Frames ===")
total_ok = 0
total_stickies = 0

for fid, ftitle, src_svg in frames:
    print(f"\nFrame {fid}: {ftitle}")
    g_match = re.search(r'<g [^>]*data-miro-id="' + fid + r'"[^>]*>(.*?)</g>', src_svg, re.DOTALL)
    if not g_match:
        print("  Could not extract frame group body")
        continue
    g_body = g_match.group(1)
    stickies = re.findall(r'<rect [^>]*data-miro-id="(\d+)"[^>]*data-type="sticky"[^>]*data-content="([^"]+)"[^>]*data-color="([^"]+)"', g_body)
    print(f"  Sticky count: {len(stickies)}")
    for sid, cnt, col in stickies:
        total_stickies += 1
        decoded = html.unescape(cnt)
        title_m = re.search(r'<b>(.*?)</b>', decoded)
        title = title_m.group(1) if title_m else "NO TITLE"
        has_how = "<b>HOW:</b>" in decoded
        has_why = "<b>WHY:</b>" in decoded
        has_ex = "<b>案例:</b>" in decoded
        has_fluff = any(k in decoded for k in ["問句:", "交付:", "提示:"])
        status = "OK" if (has_how and has_why and has_ex and not has_fluff) else "FAIL"
        if status == "OK":
            total_ok += 1
        print(f"    [{status}] ID {sid} ({col}): {title}")
        if status != "OK":
            print(f"       -> HOW: {has_how}, WHY: {has_why}, 案例: {has_ex}, FLUFF: {has_fluff}")

print(f"\n==========================================")
print(f"Verification Summary: {total_ok}/{total_stickies} cards are 100% compliant with clean IDEO format!")

