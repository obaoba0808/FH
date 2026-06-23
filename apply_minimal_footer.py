# -*- coding: utf-8 -*-
"""
全站統一極簡 Footer：只要一行版權信息
"""
import os
import re

MINIMAL_FOOTER = '''<footer class="border-t border-white/10 mt-12 pt-8 pb-8 text-center text-sm text-gray-500">
    <p>&copy; 2024-2026 歐巴傳播 OPPA ENT. All rights reserved.</p>
</footer>'''

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'google1798bed44632c997.html']

updated = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<footer' not in content:
        print(f'⚠️  跳過（無 footer）: {fname}')
        continue

    # 找到 <footer ...> 到 </footer> 的範圍
    start = content.find('<footer')
    end = content.find('</footer>')
    if start == -1 or end == -1:
        print(f'⚠️  跳過（結構異常）: {fname}')
        continue

    end += len('</footer>')
    new_content = content[:start] + MINIMAL_FOOTER + '\n' + content[end:]

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(new_content)

    updated += 1
    print(f'✅ 已更新: {fname}')

print(f'\n完成！共更新 {updated} 個檔案')
