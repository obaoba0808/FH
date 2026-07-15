# -*- coding: utf-8 -*-
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    c = f.read()
print('File length:', len(c))
print('Has Global CTA:', 'Global CTA' in c)
print('Has how_much:', 'how_much' in c)
print('Has dateModified 2026:', '2026' in c)

# Find Global CTA
idx = c.find('Global CTA')
if idx >= 0:
    print('Around Global CTA:')
    print(repr(c[idx-100:idx+30]))
