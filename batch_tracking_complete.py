#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次補齊追蹤碼至全部 HTML 頁面
- Clarity (ykmbmbct7c)
- GA4 (G-534539378)
以 </head> 前插入方式處理，避免重複。
"""
import os
import re
import glob

WS = os.path.dirname(os.path.abspath(__file__))

CLARITY_ID = "ykmbmbct7c"
GA4_ID = "G-534539378"

CLARITY_SNIPPET = f'''<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){{
        c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    }})(window, document, "clarity", "script", "{CLARITY_ID}");
</script>
'''

GA4_SNIPPET = f'''<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA4_ID}');
</script>
'''


def insert_before_head_close(html: str, snippet: str) -> str:
    """Insert snippet immediately before </head> (case-insensitive)."""
    m = re.search(r'</head\s*>', html, re.IGNORECASE)
    if not m:
        return html
    idx = m.start()
    return html[:idx] + snippet + html[idx:]


def main():
    files = sorted(glob.glob(os.path.join(WS, "*.html")))
    clarity_added, ga4_added, skipped = [], [], []

    for fp in files:
        name = os.path.basename(fp)
        with open(fp, "r", encoding="utf-8", errors="replace") as f:
            html = f.read()

        original = html
        changed = []

        if CLARITY_ID not in html:
            html = insert_before_head_close(html, CLARITY_SNIPPET)
            changed.append("clarity")

        if GA4_ID not in html:
            html = insert_before_head_close(html, GA4_SNIPPET)
            changed.append("ga4")

        if html != original:
            with open(fp, "w", encoding="utf-8", newline="") as f:
                f.write(html)
            if "clarity" in changed:
                clarity_added.append(name)
            if "ga4" in changed:
                ga4_added.append(name)
            print(f"[OK] {name}: +{','.join(changed)}")
        else:
            skipped.append(name)

    print()
    print(f"Total files scanned : {len(files)}")
    print(f"Clarity added       : {len(clarity_added)}")
    print(f"GA4 added           : {len(ga4_added)}")
    print(f"Already complete    : {len(skipped)}")

    # Verification pass
    print()
    print("=== VERIFY ===")
    c_ok = g_ok = 0
    for fp in files:
        with open(fp, "r", encoding="utf-8", errors="replace") as f:
            html = f.read()
        if CLARITY_ID in html:
            c_ok += 1
        if GA4_ID in html:
            g_ok += 1
    print(f"Clarity present: {c_ok}/{len(files)}")
    print(f"GA4 present    : {g_ok}/{len(files)}")


if __name__ == "__main__":
    main()
