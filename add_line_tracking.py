import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'google1798bed44632c997.html']

count = 0
for fname in html_files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 只處理還沒加追蹤的 LINE 連結
    if 'LINE 快速' in content or 'LINE 諮詢' in content or 'LINE 預約' in content:
        # LINE CTA 按鈕（有多個變體）
        patterns = [
            (r'(<a href="https://line\.me/ti/p/@938nzmjr"[^>]*>)', r'\1 onclick="gtag(\'event\', \'LINE_click\', {\'event_category\': \'CTA\', \'event_label\': \'footer_cta\'});"'),
            (r'(<a href="https://line\.me[^"]*"[^>]*class="[^"]*bg-green[^>]*>)', r'\1 onclick="gtag(\'event\', \'LINE_click\', {\'event_category\': \'CTA\', \'event_label\': \'green_button\'});"'),
        ]
        
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        
        if content != original:
            print(f'[TRACK] {fname}: LINE click tracking added')
            count += 1
    
    # 電話連結追蹤
    if '0926-656-666' in content or "tel:0926" in content:
        patterns = [
            (r'(<a href="tel:0926[^"]*"[^>]*>)', r'\1 onclick="gtag(\'event\', \'phone_click\', {\'event_category\': \'CTA\', \'event_label\': \'phone\'});"'),
        ]
        
        for pattern, replacement in patterns:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                content = new_content
                if fname not in [f[0] for f in []]:
                    print(f'[TRACK] {fname}: Phone tracking added')
                    count += 0.5

print(f'\nTracking added to files')
