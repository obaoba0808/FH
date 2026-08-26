# -*- coding: utf-8 -*-
import os, re, glob
BASE = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(BASE, "*.html")))
files = [f for f in files if not os.path.basename(f).startswith("google")]
# match full <a ...> tag including newlines
atag = re.compile(r'<a\b[^>]*>', re.DOTALL)
hrefre = re.compile(r'href="(https?://[^"]+)"')
total_missing = 0
for f in files:
    s = open(f, encoding="utf-8", errors="replace").read()
    missing = []
    for m in atag.finditer(s):
        tag = m.group(0)
        hm = hrefre.search(tag)
        if not hm:
            continue
        url = hm.group(1)
        # skip same-domain obaoba.online (internal absolute)
        if "obaoba.online" in url:
            continue
        if 'rel=' not in tag or 'noopener' not in tag:
            missing.append(url)
    if missing:
        total_missing += len(missing)
        print(f"{os.path.basename(f)}: {len(missing)} missing noopener")
        for u in sorted(set(missing)):
            print(f"    {u}")
print(f"\nTOTAL external links missing rel=noopener (excluding obaoba.online): {total_missing}")
