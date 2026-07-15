# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    path = f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}'
    with open(path, encoding='utf-8') as f:
        src = f.read()
    
    print(f'=== {fname} ===')
    print(f'File len: {len(src)}')
    
    # Find ALL <main and </main>
    pos = 0
    count = 0
    while True:
        m_tag = src.find('<main', pos)
        c_tag = src.find('</main>', pos)
        if m_tag == -1 and c_tag == -1:
            break
        if m_tag != -1 and (c_tag == -1 or m_tag < c_tag):
            print(f'  <main at: {m_tag}')
            pos = m_tag + 1
        elif c_tag != -1:
            print(f'  </main at: {c_tag}')
            pos = c_tag + 1
        count += 1
        if count > 10:
            print('  ... (too many)')
            break
    print()
