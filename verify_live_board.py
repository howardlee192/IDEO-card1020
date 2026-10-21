# -*- coding: utf-8 -*-
import json
import re
import html

with open(r"C:/Users/Admin/.gemini/antigravity/brain/95ae7192-ee66-4f3e-9f15-97fd27cf6cee/.system_generated/steps/439/output.txt", "r", encoding="utf-8") as f:
    data = json.load(f)

svg = data.get("svg", "")

frames = re.findall(r'<g [^>]*data-miro-id="(\d+)"[^>]*data-frame="([^"]+)"', svg)
print(f"=== Found {len(frames)} Frames ===")
for fid, ftitle in frames:
    print(f"\nFrame {fid}: {ftitle}")
    # find group substring for this frame
    g_match = re.search(r'<g [^>]*data-miro-id="' + fid + r'"[^>]*>(.*?)</g>', svg, re.DOTALL)
    if not g_match:
        print("  Could not extract frame group body")
        continue
    g_body = g_match.group(1)
    stickies = re.findall(r'<rect [^>]*data-miro-id="(\d+)"[^>]*data-type="sticky"[^>]*data-content="([^"]+)"[^>]*data-color="([^"]+)"', g_body)
    print(f"  Sticky count: {len(stickies)}")
    for sid, cnt, col in stickies:
        decoded = html.unescape(cnt)
        title_m = re.search(r'<b>(.*?)</b>', decoded)
        title = title_m.group(1) if title_m else "NO TITLE"
        has_how = "<b>HOW:</b>" in decoded
        has_why = "<b>WHY:</b>" in decoded
        has_ex = "<b>案例:</b>" in decoded
        has_fluff = any(k in decoded for k in ["問句:", "交付:", "提示:"])
        status = "OK" if (has_how and has_why and has_ex and not has_fluff) else "FAIL"
        print(f"    [{status}] ID {sid} ({col}): {title}")
        if status != "OK":
            print(f"       -> HOW: {has_how}, WHY: {has_why}, 案例: {has_ex}, FLUFF: {has_fluff}")
