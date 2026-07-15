# -*- coding: utf-8 -*-
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    c = f.read()

# Find </main>
idx_main = c.find('</main>')
print('</main> at:', idx_main)
print(repr(c[idx_main:idx_main+200]))
