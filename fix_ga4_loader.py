#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
補上缺少的 GA4 gtag.js 載入器（3 頁）
這些頁面已有 gtag('config', ...) 守衛與事件追蹤，但缺 library loader。
"""
import os
import re

WS = os.path.dirname(os.path.abspath(__file__))
GA4_ID = "G-534539378"

TARGETS = [
    "2026-pricing-table.html",
    "beginners-checklist.html",
    "private-party-guide.html",
]

LOADER = f'''<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}');
</script>
'''


def main():
    for name in TARGETS:
        fp = os.path.join(WS, name)
        with open(fp, "r", encoding="utf-8", errors="replace") as f:
            html = f.read()

        if f"gtag/js?id={GA4_ID}" in html:
            print(f"[SKIP] {name}: loader 已存在")
            continue

        m = re.search(r'</head\s*>', html, re.IGNORECASE)
        if not m:
            print(f"[FAIL] {name}: 找不到 </head>")
            continue

        html = html[:m.start()] + LOADER + html[m.start():]
        with open(fp, "w", encoding="utf-8", newline="") as f:
            f.write(html)
        print(f"[OK] {name}: 已補上 GA4 loader")

    # Verify
    print()
    print("=== VERIFY ===")
    files = [f for f in os.listdir(WS) if f.endswith(".html")]
    c_ok = g_ok = 0
    for f in files:
        with open(os.path.join(WS, f), "r", encoding="utf-8", errors="replace") as fh:
            html = fh.read()
        if "ykmbmbct7c" in html:
            c_ok += 1
        if f"gtag/js?id={GA4_ID}" in html:
            g_ok += 1
    print(f"Total HTML       : {len(files)}")
    print(f"Clarity present  : {c_ok}/{len(files)}")
    print(f"GA4 loader present: {g_ok}/{len(files)}")


if __name__ == "__main__":
    main()
