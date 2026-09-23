"""批次替換 Meta Pixel ID 佔位符 -> 實際 ID
格式確認：佔位符出現 2 次（init + noscript img）
"""
import os, sys, re

PIXEL_ID = "1377320045457011"
PLACEHOLDER = "META_PIXEL_ID"

files = [
    "about-oppa.html",
    "business-guide.html",
    "faq-all-in-one.html",
    "first_time_called.html",
    "how_much.html",
    "index.html",
    "KTV_recommendations.html",
    "motel_safe.html",
    "pricing-guide-2026.html",
    "safety_privacy.html",
]

print("=" * 70)
print(f"替換 Meta Pixel ID: {PLACEHOLDER} -> {PIXEL_ID}")
print("=" * 70)

total_replaced = 0
for fn in files:
    if not os.path.exists(fn):
        print(f"SKIP   {fn} (不存在)")
        continue
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    count = content.count(PLACEHOLDER)
    if count == 0:
        print(f"WARN   {fn} 無佔位符")
        continue
    new = content.replace(PLACEHOLDER, PIXEL_ID)
    # 驗證：替換後不應再有佔位符，且 ID 出現次數 = 原佔位符次數
    assert PLACEHOLDER not in new, f"{fn}: 仍有殘留"
    new_count = new.count(PIXEL_ID)
    if new_count != count:
        print(f"FAIL   {fn} ID次數不符 {new_count} != {count}")
        continue
    with open(fn, "w", encoding="utf-8", newline="") as f:
        f.write(new)
    total_replaced += count
    print(f"OK     {fn:<30} 替換 {count} 處")

print("-" * 70)
print(f"總替換處數: {total_replaced}")
