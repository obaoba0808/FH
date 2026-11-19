# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        c = f.read()

    # Count ALL Chinese characters in the file
    all_cn = sum(1 for ch in c if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
    
    # Count inside <main> tag
    m = re.search(r'<main[^>]*>(.*?)</main>', c, re.DOTALL)
    body = m.group(1) if m else 'NOT FOUND'
    body_cn = sum(1 for ch in body if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
    
    print(f'=== {fname} ===')
    print(f'  Total Chinese chars in file: {all_cn}')
    print(f'  Chinese chars inside <main>: {body_cn}')
    print(f'  File len: {len(c)}')
    print()
