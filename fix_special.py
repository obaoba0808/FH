# -*- coding: utf-8 -*-
import re

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    src = f.read()

# The marker that uniquely identifies the end of article content
# Pattern: closing comment block + optional blank lines + Global CTA
# Use a regex to find the insertion point after the article's last content
old_end = re.compile(
    r'(<img[^>]*>)\s*(</main>)',
    re.DOTALL
).search(src)

# Simpler approach: find <!-- Global CTA --> and go backwards to find end of </main> block
cta_idx = src.find('    <!-- Global CTA -->')
print('Global CTA at:', cta_idx)

# Find the </main> tag before this
main_close_idx = src.rfind('</main>', 0, cta_idx)
print('</main> at:', main_close_idx)
print('Between </main> and Global CTA:')
print(repr(src[main_close_idx:cta_idx]))
