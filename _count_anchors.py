import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'

# Count how many pages have each candidate anchor in their dropdown
candidates = [
    'how_much.html', 'KTV_party.html', 'motel_safe.html', 'first_time_called.html',
    'business-guide.html', 'faq-all-in-one.html', 'about-oppa.html', 'news.html',
    'shoot_guide.html', 'recruitment.html',
]

counts = {c: 0 for c in candidates}
total = 0
for fpath in glob.glob(ROOT + '/*.html'):
    fname = fpath.replace(ROOT + '\\', '')
    if 'google' in fname or fname in ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html']:
        continue
    content = open(fpath, encoding='utf-8').read()
    m = re.search(r'情報特搜站', content)
    if not m:
        continue
    total += 1
    dropdown = content[m.start():m.start()+9000]
    for c in candidates:
        if c in dropdown:
            counts[c] += 1

print(f'Pages with dropdown: {total}')
for c, n in sorted(counts.items(), key=lambda x: -x[1]):
    print(f'  {c}: {n} pages')
