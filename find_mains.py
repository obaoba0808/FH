# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        c = f.read()
    
    print(f'=== {fname} ===')
    # Find all </main> positions
    pos = 0
    idx = c.find('</main>', pos)
    while idx != -1:
        # Show context
        snippet = c[max(0,idx-30):idx+50].replace('\n', '\\n')
        print(f'  </main> at {idx}: ...{snippet}...')
        pos = idx + 1
        idx = c.find('</main>', pos)
    print()
