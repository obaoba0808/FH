import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
pages = []
for f in sorted(glob.glob(ROOT + '/*.html')):
    if 'google' in f: continue
    name = f.replace(ROOT+'\\','').replace('.html','')
    s = open(f, encoding='utf-8').read()
    m = re.search(r'<title>(.*?)</title>', s)
    title = m.group(1) if m else '?'
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', s, re.S)
    h2_count = len(h2s)
    details = re.findall(r'<details class="faq-item"', s)
    faq_count = len(details)
    words = len(re.sub(r'<[^>]+>','', s))
    pages.append({'name': name, 'title': title[:55], 'h2': h2_count, 'faq': faq_count, 'words': words})

print(f"{'WORDS':>5} | {'H2':>2} | {'FAQ':>3} | PAGE")
print('-'*80)
for p in sorted(pages, key=lambda x: x['words']):
    print(f"{p['words']:>5} | {p['h2']:>2} | {p['faq']:>3} | {p['name']}")
