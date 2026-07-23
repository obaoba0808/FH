"""
深度清理所有舊 LINE 按鈕：精準匹配 + 完全替換
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'google1798bed44632c997.html']

# 新的 LINE 按鈕（統一設計）
NEW_BTN = (
    '<a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer" '
    'class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-[#06C755] hover:bg-[#05a546] '
    'text-white font-bold text-sm transition-all shadow-[0_0_20px_rgba(6,199,85,0.3)] hover:scale-[1.03]" '
    'onclick="gtag(\'event\', \'LINE_click\', {\'event_category\': \'CTA\', \'event_label\': \'nav_btn\'});">'
    '<iconify-icon icon="bi:line" class="text-lg"></iconify-icon>'
    '加 LINE 預約'
    '</a>'
)

# 新的 LINE 大按鈕（用於 mid-content inline CTAs）
NEW_BTN_LARGE = (
    '<a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer" '
    'class="inline-flex items-center gap-2 px-8 py-4 rounded-2xl bg-[#06C755] hover:bg-[#05a546] '
    'text-white font-black text-lg transition-all shadow-[0_0_25px_rgba(6,199,85,0.4)] hover:scale-[1.03]" '
    'onclick="gtag(\'event\', \'LINE_click\', {\'event_category\': \'CTA\', \'event_label\': \'inline_cta\'});">'
    '<iconify-icon icon="bi:line" class="text-xl"></iconify-icon>'
    '加 LINE 預約'
    '</a>'
)

total_updated = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content

    # Pattern 1: 包含 SVG checkmark 的舊 LINE 按鈕（header nav 最常見）
    # 整個 <a> 標籤含 SVG + "LINE 快速預約"
    p1 = r'<a href="https://line\.me[^"]*"[^>]*>\s*<svg[^>]*>[^<]*</svg>\s*LINE[^<]*</a>'
    new_content = re.sub(p1, NEW_BTN, content)
    if new_content != content:
        content = new_content
        print(f'[SVG-BTN] {fname}')

    # Pattern 2: 包含 iconify-icon 的舊 LINE 按鈕
    p2 = r'<a href="https://line\.me[^"]*"[^>]*>\s*<iconify-icon[^>]*>[^<]*</iconify-icon>\s*LINE[^<]*</a>'
    new_content = re.sub(p2, NEW_BTN, content)
    if new_content != content:
        content = new_content
        print(f'[ICONIFY-BTN] {fname}')

    # Pattern 3: 純文字舊 LINE 按鈕（無 SVG/iconify，純文字）
    p3 = r'<a href="https://line\.me[^"]*"[^>]*>\s*LINE[^<]*</a>'
    new_content = re.sub(p3, NEW_BTN, content)
    if new_content != content:
        content = new_content
        print(f'[TEXT-BTN] {fname}')

    # 清理殘留的舊按鈕 class（已部分替換但殘留舊 class）
    # 把 hover:bg-green-600 改成 hover:bg-[#05a546] 等
    content = content.replace('hover:bg-green-600', 'hover:bg-[#05a546]')
    content = content.replace('bg-green-500', 'bg-[#06C755]')

    # 統一 URL：ti/p/@938nzmjr 改為 R/ti/p/@938nzmjr（LINE 官方推薦）
    content = content.replace('https://line.me/ti/p/@938nzmjr"', 'https://line.me/R/ti/p/@938nzmjr"')

    # 替換按鈕文字
    content = content.replace('>LINE 快速預約<', '>加 LINE 預約<')
    content = content.replace('>LINE 立即預約<', '>LINE 立即預約<')
    content = content.replace('>LINE 免費諮詢<', '>LINE 免費諮詢<')
    content = content.replace('>LINE 諮詢<', '>LINE 諮詢<')

    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        total_updated += 1
        print(f'  -> Saved: {fname}')

print(f'\nLINE buttons fully cleaned: {total_updated} files')
