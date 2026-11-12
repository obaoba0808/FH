# -*- coding: utf-8 -*-
import re

path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\how_much.html'
with open(path, encoding='utf-8') as f:
    c = f.read()

print(f'File len: {len(c)}')

# Find first <main
idx_main = c.find('<main')
print(f'First <main at: {idx_main}')
print(repr(c[idx_main:idx_main+100]))

# Find all </main>
pos = 0
while True:
    idx = c.find('</main>', pos)
    if idx == -1:
        break
    print(f'</main> at: {idx}')
    print(repr(c[max(0,idx-50):idx+20]))
    pos = idx + 1

# Try regex match
m = re.search(r'<main[^>]*>(.*?)</main>', c, re.DOTALL)
if m:
    body = m.group(1)
    print(f'Regex matched: body len={len(body)}, H2={body.count("<h2>")}')
else:
    print('Regex NO MATCH!')

# Try simple string split
parts = c.split('</main>')
print(f'Split by </main>: {len(parts)} parts')
for i, p in enumerate(parts[:3]):
    print(f'  Part {i}: {len(p)} chars, last 50: {repr(p[-50:])}')
