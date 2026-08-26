import glob
ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
pages = ['index.html','how_much.html','first_time_called.html','pricing-guide-2026.html','business_dinner.html','about-oppa.html']
for f in pages:
    c = open(ROOT+'/'+f, encoding='utf-8').read()
    b = 'beginners-checklist' in c
    p = '2026-pricing-table' in c
    pp = 'private-party' in c
    print(f'{f}: beginners={b} pricing={p} party={pp}')
