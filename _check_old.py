import sys, codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, errors='replace')

html = open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html', encoding='utf-8').read()
print('File length:', len(html))

for p in ['普通級', '精選級', '2500-3500', '3500-5000', '5000-8000', '2500-3500元', '3500-5000元', '5000-8000元']:
    idx = html.find(p)
    if idx >= 0:
        print('FOUND: ' + p + ' at ' + str(idx) + ': ' + repr(html[idx-5:idx+60]))
    else:
        print('NOT FOUND: ' + p)

# Also check all occurrences
print('\n--- All pricing mentions ---')
for idx in range(len(html)):
    pass

import re
for m in re.finditer(r'[\d,]+-[\d,]+元', html):
    ctx = html[max(0,m.start()-20):m.end()+20]
    if 'animation' not in ctx.lower() and 'anime' not in ctx.lower() and 'random' not in ctx.lower():
        print(repr(ctx))
