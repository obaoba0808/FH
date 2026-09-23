"""全站 head 結構驗證 v2
修正 v1 誤判：
- GA4 'G-xxxx' 在正常載入器會出現 2 次（?id= 與 config），故計數邏輯改為
  檢查「是否含 gtag/js?id= 載入器」與「是否含 gtag('config',ID)」，各需恰好 1 次。
- Meta Pixel 只要求 init 恰好 1 次（noscript 也算同一段，不重複 init）。
"""
import os, glob, re

BOM = b"\xef\xbb\xbf"
CLARITY = "ykmbmbct7c"
GA4 = "G-534539378"
PIXEL = "1377320045457011"

LOADER_P = re.compile(r"fbq\('init',\s*'%s'\)" % PIXEL)
NOSCRIPT_P = re.compile(r"facebook\.com/tr\?id=%s" % PIXEL)
GA4_LOADER = re.compile(r"gtag/js\?id=%s" % GA4)
GA4_CONFIG = re.compile(r"gtag\('config',\s*'%s'\)" % GA4)
CLARITY_RE = re.compile(r"clarity.*?%s" % CLARITY, re.I | re.S)

files = sorted(glob.glob("*.html"))
print(f"{'檔案':<34} {'Clar':<5} {'GA4ld':<6} {'GA4cfg':<7} {'PxInit':<7} {'PxNs':<5} {'BOM':<4} 判定")
print("-" * 92)

ok = 0
fails = []
for fn in files:
    with open(fn, "rb") as f:
        raw = f.read()
    has_bom = raw.startswith(BOM)
    txt = raw.decode("utf-8-sig" if has_bom else "utf-8", errors="replace")

    clar = 1 if CLARITY in txt else 0
    ga4ld = len(GA4_LOADER.findall(txt))
    ga4cfg = len(GA4_CONFIG.findall(txt))
    pxinit = len(LOADER_P.findall(txt))
    pxns = len(NOSCRIPT_P.findall(txt))

    passed = (clar == 1 and ga4ld == 1 and ga4cfg == 1
              and pxinit == 1 and pxns == 1 and not has_bom)
    if passed:
        ok += 1
        mark = "PASS"
    else:
        fails.append(fn)
        mark = "FAIL"
    print(f"{fn:<34} {clar:<5} {ga4ld:<6} {ga4cfg:<7} {pxinit:<7} {pxns:<5} "
          f"{'Y' if has_bom else 'N':<4} {mark}")

print("-" * 92)
print(f"總計 {len(files)} 頁 | PASS {ok} | FAIL {len(fails)}")
if fails:
    print("失敗頁面:")
    for f in fails:
        print("  -", f)
