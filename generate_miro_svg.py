# -*- coding: utf-8 -*-
import os
import re
import html
import json

repo_dir = r"C:\Users\Admin\.gemini\antigravity\scratch\IDEO-card1020"

def parse_01_directing():
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
        category = ""
        how = ""
        why = ""
        example = ""
        for l in lines:
            if "頂部分類" in l:
                category = l.replace("* **頂部分類**：", "").strip()
            elif "HOW" in l:
                how = l.replace("* **HOW**：", "").strip()
            elif "WHY" in l:
                why = l.replace("* **WHY**：", "").strip()
            elif "案例" in l or "EXAMPLE" in l:
                example = re.sub(r"^\*\s*\*\*(案例|EXAMPLE)\*\*：\s*", "", l).strip()
        
        cards.append({
            "title": title,
            "category": category,
            "how": how,
            "why": why,
            "example": example
        })
    return cards

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
        category = ""
        question = ""
        how = []
        why = ""
        deliverable = ""
        tip = ""
        
        mode = None
        for l in lines:
            if "正面分類" in l:
                category = l.replace("* **正面分類**：", "").strip()
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
            elif mode == "how" and (l.startswith("1.") or l.startswith("2.") or l.startswith("3.") or l.startswith("*")):
                clean_how = re.sub(r"^\d+\.\s*", "", l)
                clean_how = re.sub(r"^\*\s*", "", clean_how)
                how.append(clean_how)
            elif mode == "why" and not why:
                why = l.strip()
            elif mode == "deliverable" and not deliverable:
                deliverable = l.strip()
            elif mode == "tip" and not tip:
                tip = l.strip()
        
        cards.append({
            "title": title,
            "category": category,
            "question": question,
            "how": " ".join(how),
            "why": why,
            "deliverable": deliverable,
            "tip": tip
        })
    return cards

directing = parse_01_directing()
print(f"Directing: {len(directing)} cards")

concept = parse_standard_spec("02_Concept.md")
print(f"Concept: {len(concept)} cards")

storyboard = parse_standard_spec("03_Storyboard.md")
print(f"Storyboard: {len(storyboard)} cards")

animation = parse_standard_spec("04_Animation.md")
print(f"Animation: {len(animation)} cards")

vfx_all = parse_standard_spec("05_VFX_Comp_Rules.md")
print(f"VFX & Rules: {len(vfx_all)} cards")
