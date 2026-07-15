# -*- coding: utf-8 -*-
for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        src = f.read()
    idx = src.find('</main>')
    print(f'=== {fname} ===')
    print(repr(src[idx:idx+200]))
    print()
