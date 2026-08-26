import re, glob, os

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'

REPLACEMENTS = [
    # 1. 絕不在 JSON-LD 裡替換（schema name 用 OPPA ENT.）
    # 2. Nav logo: "FH 歐巴傳播" → "歐巴傳播"
    (r'<a href="index\.html" class="logo">FH 歐巴傳播</a>', '<a href="index.html" class="logo">歐巴傳播</a>'),
    (r'<a href="index\.html" class="logo">歐巴傳播 OPPA ENT\.</a>', '<a href="index.html" class="logo">歐巴傳播</a>'),
    (r'<a href="index\.html" class="logo">歐巴傳播</a>', '<a href="index.html" class="logo">歐巴傳播</a>'),
    # 3. 文字中的 "歐巴傳播 OPPA ENT." → "歐巴傳播"（但避開 JSON-LD）
    #    策略：只在 </body> 之前處理，或者用更精確匹配
    # 4. Footer 中的 OPPA ENT.
    (r'歐巴傳播 OPPA ENT\.', '歐巴傳播'),
    # 5. Footer "© 2024-2026 FH 歐巴傳播" → "© 2024-2026 歐巴傳播"
    (r'© \d{4}-\d{4} FH 歐巴傳播', lambda m: f'© {m.group()[:4]}-{m.group()[-4:]} 歐巴傳播'),
    # 6. Nav 其他 "FH 歐巴傳播" 出現
    (r'FH 歐巴傳播', '歐巴傳播'),
]

stats = {}
for f in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    s = open(f, encoding='utf-8').read()
    orig = s
    changed = False

    # 分割出 JSON-LD block，不動它
    parts = re.split(r'(<script type="application/ld\+json">.*?</script>)', s, flags=re.S)
    new_parts = []
    for i, part in enumerate(parts):
        if i % 2 == 1:  # JSON-LD block
            new_parts.append(part)
        else:
            t = part
            # Nav logo: class="logo" 之後的文字
            t = re.sub(r'(<a href="index\.html" class="logo">)[^<]*?(</a>)', r'\1歐巴傳播\2', t)
            # Footer OPPA ENT (© 行)
            t = re.sub(r'© (\d{4})-(\d{4}) FH 歐巴傳播', r'© \1-\2 歐巴傳播', t)
            # 純文字 "歐巴傳播 OPPA ENT." → "歐巴傳播"
            t = re.sub(r'歐巴傳播 OPPA ENT\.', '歐巴傳播', t)
            # 其他 "FH 歐巴傳播" → "歐巴傳播"
            t = re.sub(r'FH 歐巴傳播', '歐巴傳播', t)
            if t != part:
                changed = True
            new_parts.append(t)

    if changed:
        s = ''.join(new_parts)
        open(f, 'w', encoding='utf-8').write(s)
        stats[os.path.basename(f)] = True
        print('UPDATED:', os.path.basename(f))

print(f'\nTotal: {len(stats)} files changed')
