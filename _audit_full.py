# -*- coding: utf-8 -*-
import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(BASE, "*.html")))
# exclude google verification file
files = [f for f in files if not os.path.basename(f).startswith("google")]

def read(f):
    with open(f, encoding="utf-8", errors="replace") as fh:
        return fh.read()

print(f"{'FILE':<38} {'canon':<5} {'hl':<4} {'og:img':<6} {'fav':<5} {'@type':<22} {'ext-noop':<9} {'imgNoAlt':<8} {'titleLen'}")
print("-"*120)
rows=[]
for f in files:
    h = read(f)
    name = os.path.basename(f)
    canonical = "Y" if re.search(r'<link rel="canonical"', h) else "N"
    hl = "Y" if ('hreflang="zh-Hant"' in h and 'hreflang="x-default"' in h) else ("P" if 'hreflang' in h else "N")
    ogimg = "Y" if 'og:image' in h else "N"
    fav = "PNG" if re.search(r'<link rel="icon"[^>]*\.png', h) else ("svg" if 'data:image/svg+xml' in h else "NONE")
    types = re.findall(r'"@type"\s*:\s*"([^"]+)"', h)
    # external links without rel noopener
    ext = re.findall(r'<a[^>]+href="(https?://[^"]+)"', h)
    ext_noop = 0
    for m in re.finditer(r'<a\s+[^>]*href="https?://[^"]+"[^>]*>', h):
        tag = m.group(0)
        if 'rel=' not in tag or 'noopener' not in tag:
            ext_noop += 1
    # images without alt
    imgs = re.findall(r'<img\s+[^>]*>', h)
    noalt = 0
    for im in imgs:
        if 'alt=' not in im:
            noalt += 1
        else:
            am = re.search(r'alt="([^"]*)"', im)
            if am and am.group(1).strip()=="":
                noalt += 1  # empty alt counts as present (ok for decorative) - count separately maybe
    # title length
    tm = re.search(r'<title>([^<]*)</title>', h)
    tlen = len(tm.group(1)) if tm else 0
    tset = "/".join(sorted(set(types)))
    rows.append((name,canonical,hl,ogimg,fav,tset,ext_noop,noalt,tlen))
    print(f"{name:<38} {canonical:<5} {hl:<4} {ogimg:<6} {fav:<5} {tset:<22} {ext_noop:<9} {noalt:<8} {tlen}")

print("\n=== SUMMARY ===")
nc = sum(1 for r in rows if r[1]=="N")
nh = sum(1 for r in rows if r[2]!="Y")
no = sum(1 for r in rows if r[6]>0)
print(f"Missing canonical: {nc}")
print(f"Missing full hreflang(zh-Hant+x-default): {nh}")
print(f"Files with external links lacking rel=noopener: {no}")
for r in rows:
    if r[6]>0:
        print(f"   {r[0]}: {r[6]} external links no noopener")
