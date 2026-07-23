import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'google1798bed44632c997.html']

# 追蹤程式碼
LINE_ONCLICK = " onclick=\"gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'LINE'});\""
PHONE_ONCLICK = " onclick=\"gtag('event', 'phone_click', {'event_category': 'CTA', 'event_label': 'Phone'});\""

count = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 找出所有 LINE 連結並加入追蹤
    # 匹配 <a href="https://line.me/..." ...>
    line_pattern = r'(<a href="https://line\.me[^"]*"[^>]*)>'
    if 'line.me' in content:
        # 避免重複加入
        if "gtag('event', 'LINE_click'" not in content:
            content = re.sub(line_pattern, r'\1' + LINE_ONCLICK + '>', content)
            print(f'[LINE] {fname}')

    # 找出所有電話連結並加入追蹤
    phone_pattern = r'(<a href="tel:[^"]*"[^>]*)>'
    if 'tel:' in content:
        if "gtag('event', 'phone_click'" not in content:
            content = re.sub(phone_pattern, r'\1' + PHONE_ONCLICK + '>', content)
            print(f'[PHONE] {fname}')

    if content != original:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1

print(f'\nTracking added to {count} files')
