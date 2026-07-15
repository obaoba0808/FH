# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        c = f.read()
    
    print(f'=== {fname} ===')
    print(f'  dateModified occurrences: {c.count("dateModified")}')
    idx = c.find('dateModified')
    if idx >= 0:
        print(f'  First dateModified: {repr(c[idx-20:idx+40])}')
    
    # Count all JSON-LD script blocks
    scripts = list(re.finditer(r'<script type="application/ld\+json">.*?</script>', c, re.DOTALL))
    print(f'  JSON-LD blocks: {len(scripts)}')
    for i, s in enumerate(scripts):
        snippet = c[s.start():s.start()+100].replace('\n', ' ')
        print(f'    Block {i}: {snippet}')
    print()
