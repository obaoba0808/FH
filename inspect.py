# -*- coding: utf-8 -*-
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    src = f.read()

# Find Global CTA
cta_idx = src.find('<!-- Global CTA -->')
print('Global CTA at:', cta_idx)
print('Around it:')
print(repr(src[cta_idx-300:cta_idx+50]))
