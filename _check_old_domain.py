import re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
for fname in ['index.html', 'how_much.html', 'news.html']:
    c = open(ROOT + '/' + fname, encoding='utf-8').read()
    print(f'\n=== {fname} ===')
    for m in re.finditer(r'[^\s"\']*obaoba0808\.github\.io[^\s"\']*', c):
        ctx = c[max(0, m.start()-60):m.end()+60].replace('\n', ' ')
        print(' ', ctx)
