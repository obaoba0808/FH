"""
最終版：清除所有殘留的舊 LINE 按鈕
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'google1798bed44632c997.html']

NEW_BTN = (
    '<a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer" '
    'class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#06C755] hover:bg-[#05a546] '
    'text-white font-bold text-sm transition-all shadow-[0_0_20px_rgba(6,199,85,0.3)] hover:scale-[1.03]" '
    'onclick="gtag(\'event\', \'LINE_click\', {\'event_category\': \'CTA\', \'event_label\': \'nav_btn\'});">'
    '<iconify-icon icon="bi:line" class="text-lg"></iconify-icon>'
    '加 LINE 預約'
    '</a>'
)

total = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # 找所有含 LINE 快速預約 的 <a> 連結標籤（跨行）
    # 匹配從 <a href="line.me" 到 </a> 含 "LINE 快速預約"
    p = r'<a href="https://line\.me[^"]*"[^>]*>.*?LINE 快速預約.*?</a>'
    
    count = 0
    while True:
        new_content = re.sub(p, NEW_BTN, content, flags=re.DOTALL)
        if new_content == content:
            break
        content = new_content
        count += 1
    
    if count > 0:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'[CLEANED x{count}] {fname}')
        total += 1

print(f'\nDone: {total} files cleaned')
