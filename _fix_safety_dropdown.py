import re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
fpath = ROOT + '/safety-guide-2026.html'
c = open(fpath, encoding='utf-8').read()
orig = c

# Add 2026-pricing-table.html after pricing-guide-2026.html (2026傳播收費行情)
if '2026-pricing-table.html' not in c:
    pat = re.compile(r'(<a href="pricing-guide-2026.html"[^>]*>[^<]*2026傳播收費行情[^<]*</a>)')
    m = pat.search(c)
    if m:
        link = '<a href="2026-pricing-table.html" class="dropdown-link">2026 收費行情表（計算機）</a>'
        c = c[:m.end()] + '\n' + link + c[m.end():]
        print('Added pricing-table link')

# Add private-party-guide.html after beginners-checklist.html (新手必看 12 項檢查清單)
if 'private-party-guide.html' not in c:
    pat2 = re.compile(r'(<a href="beginners-checklist.html"[^>]*>[^<]*新手必看 12 項檢查清單[^<]*</a>)')
    m2 = pat2.search(c)
    if m2:
        link2 = '<a href="private-party-guide.html" class="dropdown-link">私人派對攻略</a>'
        c = c[:m2.end()] + '\n' + link2 + c[m2.end():]
        print('Added private-party link')

if c != orig:
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(c)
    print('safety-guide-2026.html updated')
else:
    print('No changes')
