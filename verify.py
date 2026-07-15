# -*- coding: utf-8 -*-
import re

for fname in ['how_much.html', 'special_industries.html']:
    with open(f'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/{fname}', encoding='utf-8') as f:
        c = f.read()

    m = re.search(r'<main[^>]*>(.*?)<\/main>', c, re.DOTALL)
    body = m.group(1) if m else ''
    h2 = c.count('<h2>')
    faq = c.count('<details class="mb-4')
    date_ok = '"dateModified": "2026-07-15"' in c
    cn = sum(1 for ch in body if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
    faq_q = c.count('"@type": "Question"')
    print(f'=== {fname} ===')
    print(f'  H2 sections  : {h2} (need 9+)')
    print(f'  FAQ items    : {faq} HTML / {faq_q} JSON-LD (need 6+)')
    print(f'  dateModified : {date_ok}')
    print(f'  Chinese chars: {cn} (need 1500+)')
    print()
