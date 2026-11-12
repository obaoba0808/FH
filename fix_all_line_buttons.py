"""
修復所有舊 LINE 按鈕：header nav + mid-content inline CTAs
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'google1798bed44632c997.html']

total_updated = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # 替換所有舊 LINE 按鈕（小/中尺寸，非 CTA section 大按鈕）
    # 使用字串替換方式，精準匹配

    old_patterns = [
        # Pattern 1: bg-green-500 小按鈕（最常見舊版）
        'bg-green-500 text-white px-8 py-4 rounded-full font-bold text-lg',
        # Pattern 2: btn-neon LINE 按鈕
        'btn-neon px-8 py-3 rounded-full font-bold text-lg',
        # Pattern 3: 其他綠色 LINE 按鈕（mid-content）
        'bg-green-500 hover:bg-green-600 text-white font-bold text-lg',
    ]

    replacement = (
        'inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#06C755] hover:bg-[#05a546] '
        'text-white font-bold text-sm transition-all shadow-[0_0_20px_rgba(6,199,85,0.3)] '
        'hover:scale-[1.03]'
    )

    for pattern in old_patterns:
        # 找包含此 class 的整個 <a> 標籤
        # 簡化：直接替換 class 屬性
        p = r'(<a href="https://line\.me[^"]*"[^>]*class="[^"]*)' + re.escape(pattern) + r'([^>]*onclick="[^"]*LINE_click[^"]*"[^>]*>)'
        r_text = r'\g<1>' + replacement + r'\g<2>'
        new_content = re.sub(p, r_text, content)
        if new_content != content:
            content = new_content
            print(f'[CLASS] {fname}: updated button class')

    # 替換按鈕文字
    text_replacements = [
        ('>LINE 快速預約<', '>加 LINE 預約<'),
        ('>LINE 諮詢<', '>加 LINE 諮詢<'),
        ('>LINE 預約<', '>LINE 立即預約<'),
        ('>加 LINE 免費諮詢<', '>LINE 免費諮詢<'),
    ]
    for old_text, new_text in text_replacements:
        if old_text in content:
            content = content.replace(old_text, new_text)
            print(f'[TEXT] {fname}: "{old_text.strip("<>")}" -> "{new_text.strip("<>")}"')

    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        total_updated += 1

print(f'\nLINE buttons unified: {total_updated} files')
