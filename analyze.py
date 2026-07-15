# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        c = f.read()
    
    print(f'=== {fname} ===')
    print(f'File len: {len(c)}')
    
    # Find <main>...</main>
    m = re.search(r'<main([^>]*)>(.*?)</main>', c, re.DOTALL)
    if m:
        body = m.group(2)
        h2_in_main = body.count('<h2>')
        cn_in_main = sum(1 for ch in body if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
        print(f'  Inside <main>: {len(body)} chars, H2={h2_in_main}, CN={cn_in_main}')
        print(f'  Has 四-section in main: {"四、" in body}')
        print(f'  Has FAQ in main: {"<details" in body}')
    
    # What's outside </main>
    after_main = c[m.end():] if m else c
    h2_outside = after_main.count('<h2>')
    print(f'  Outside </main>: {len(after_main)} chars, H2={h2_outside}')
    print()
