# -*- coding: utf-8 -*-
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    src = f.read()

# Check all variations of the marker
markers = [
    '</main>\n    <!-- ========================================== -->\n    <!-- 以上區塊為每篇文章需要替換的內容 -->\n    <!-- ========================================== -->\n\n    <!-- Global CTA -->',
    '</main>\n    <!-- ========================================== -->\n    <!-- 以上區塊為每篇文章需要替換的內容 -->\n    <!-- ========================================== -->\n\n<!-- Global CTA -->',
    '</main>\n    <!-- ========================================== -->\n    <!-- 以上區塊為每篇文章需要替換的內容 -->\n    <!-- ========================================== -->\n\n<!-- Global CTA -->',
    '<!-- 以上區塊為每篇文章需要替換的內容 -->\n    <!-- ========================================== -->\n\n    <!-- Global CTA -->',
]
for i, m in enumerate(markers):
    print(f'Marker {i}: found={m in src}')
    if m in src:
        idx = src.find(m)
        print(f'  at position {idx}')

# Also check what the end of the article content looks like
cta_idx = src.find('<!-- Global CTA -->')
if cta_idx < 0:
    cta_idx = src.find('    <!-- Global CTA -->')
print('\nFirst Global CTA at:', cta_idx)
if cta_idx >= 0:
    print(repr(src[cta_idx-5:cta_idx+50]))
