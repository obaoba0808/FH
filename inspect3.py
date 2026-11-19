# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        c = f.read()
    
    print(f'=== {fname} ===')
    print(f'File len: {len(c)}')
    
    # Find <main>...</main>
    m = re.search(r'<main[^>]*>(.*?)</main>', c, re.DOTALL)
    if m:
        body = m.group(1)
        print(f'Main body: {len(body)} chars')
        h2_positions = [(mm.start(), mm.group(0)) for mm in re.finditer(r'<h2>', body)]
        print(f'H2 count: {len(h2_positions)}')
        for i, (pos, tag) in enumerate(h2_positions):
            snippet = body[pos:pos+60].replace('\n', ' ')
            print(f'  H2[{i}] at {pos}: {snippet}')
        
        # Check for FAQ details
        faq_pos = body.find('<details')
        print(f'FAQ details at: {faq_pos}')
        if faq_pos >= 0:
            snippet = body[faq_pos:faq_pos+100].replace('\n', ' ')
            print(f'  {snippet}')
        
        # Check last 200 chars
        print(f'Last 200 chars of body:')
        print(repr(body[-200:]))
    else:
        print('No <main> found!')
    print()
