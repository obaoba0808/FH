# -*- coding: utf-8 -*-
import os, re, glob
BASE = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(BASE, "*.html")))
files = [f for f in files if not os.path.basename(f).startswith("google")]

atag = re.compile(r'<a\b[^>]*>', re.DOTALL)
hrefre = re.compile(r'href="(https?://[^"]+)"')
svgfav = re.compile(r'<link rel="icon" type="image/svg\+xml" href="data:image/svg\+xml,[^"]*">')
PNG_FAV = ('<link rel="apple-touch-icon" sizes="180x180" href="images/apple-touch-icon.png">\n'
           '    <link rel="icon" type="image/png" sizes="32x32" href="images/favicon-32x32.png">\n'
           '    <link rel="icon" type="image/png" sizes="16x16" href="images/favicon-16x16.png">\n'
           '    <link rel="manifest" href="site.webmanifest">')

def fix_tag(m):
    tag = m.group(0)
    hm = hrefre.search(tag)
    if not hm:
        return tag
    url = hm.group(1)
    if "obaoba.online" in url:
        return tag
    if "rel=" in tag and "noopener" in tag:
        return tag
    if "rel=" in tag:
        tag = re.sub(r'(rel="[^"]*)(")', r'\1 noreferrer\2', tag, count=1)
    else:
        tag = tag.rstrip(">") + ' rel="noopener noreferrer">'
    return tag

changed = []
for f in files:
    s = open(f, encoding="utf-8", errors="replace").read()
    s2 = atag.sub(fix_tag, s)
    s2, nsvg = svgfav.subn(PNG_FAV, s2)
    if s2 != s:
        open(f, "w", encoding="utf-8").write(s2)
        changed.append((os.path.basename(f), nsvg))

for name, nsvg in changed:
    print(f"updated {name} (svg-favicon replaced: {nsvg})")
print(f"\nTotal files changed: {len(changed)}")
