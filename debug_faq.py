# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    path = f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}'
    with open(path, encoding='utf-8') as f:
        src = f.read()
    
    m = re.search(r'<main[^>]*>(.*?)</main>', src, re.DOTALL)
    body = m.group(1) if m else ''
    
    # Check for FAQ
    faq_markers = ['<h2>常見問題 FAQ</h2>', '<h2>常見問題</h2>', 'FAQ']
    for marker in faq_markers:
        pos = body.find(marker)
        print(f'{fname}: FAQ marker "{marker}" at: {pos}')
    
    # Show last 300 chars of body
    print(f'{fname} last 300 chars:')
    print(repr(body[-300:]))
    print()
