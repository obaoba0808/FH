import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 新連結（相對路徑版本，適用於新頁面）
NEW_LINKS_REL = [
    '<a href="compare-girls.html" class="hover:text-neonPink transition-colors">傳播妹vs酒店</a>',
    '<a href="business-guide.html" class="hover:text-neonPink transition-colors">商務公關</a>',
    '<a href="legality-guide.html" class="hover:text-neonPink transition-colors">合法性解析</a>',
    '<a href="booking-guide.html" class="hover:text-neonPink transition-colors">預約流程</a>',
]

# 新連結（完整 URL 版本，適用於舊頁面）
BASE_URL = "https://obaoba0808.github.io/FH/"
NEW_LINKS_ABS = [
    f'<a href="{BASE_URL}compare-girls.html" class="hover:text-neonPink transition-colors">傳播妹vs酒店</a>',
    f'<a href="{BASE_URL}business-guide.html" class="hover:text-neonPink transition-colors">商務公關</a>',
    f'<a href="{BASE_URL}legality-guide.html" class="hover:text-neonPink transition-colors">合法性解析</a>',
    f'<a href="{BASE_URL}booking-guide.html" class="hover:text-neonPink transition-colors">預約流程</a>',
]

pages_to_update = [
    'how_much.html', 'safety_privacy.html', 'recruitment.html',
    'first_time_called.html', 'first-time-2026.html',
    'KTV_party.html', 'one_by_one.html', 'KTV_recommendations.html',
    'business_dinner.html', 'motel_safe.html', 'shoot_guide.html',
    'is_this_right_for_you.html', 'shoot_switch_personnel.html',
    'special_industries.html', 'suitable_female.html',
    'interaction_scale.html', 'can-touch-guide.html',
    'companion-levels-2026.html', 'male_companion.html',
    'taipei_agency_guide.html', 'news.html', 'tipping-guide-2026.html',
    'index.html'
]

count = 0
for fname in pages_to_update:
    if not os.path.exists(fname):
        continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 檢查是否已有這些連結
    if ('compare-girls.html' in content and 
        'business-guide.html' in content and
        'legality-guide.html' in content and
        'booking-guide.html' in content):
        print(f'[OK] {fname}')
        continue
    
    # 判斷是相對路徑還是完整 URL
    uses_abs = 'https://obaoba0808.github.io/FH/' in content
    new_links = NEW_LINKS_ABS if uses_abs else NEW_LINKS_REL
    insert_str = '\n            '.join(new_links)
    
    new_content = None
    
    # 嘗試多個錨點
    anchors = [
        ('taipei_agency_guide', BASE_URL + 'taipei_agency_guide.html'),
        ('taipei_agency_guide', 'taipei_agency_guide.html'),
        ('tipping-guide-2026', BASE_URL + 'tipping-guide-2026.html'),
        ('tipping-guide-2026', 'tipping-guide-2026.html'),
        ('companion-levels-2026', BASE_URL + 'companion-levels-2026.html'),
        ('companion-levels-2026', 'companion-levels-2026.html'),
        ('加入我們', BASE_URL + 'recruitment.html'),
        ('recruitment.html', BASE_URL + 'recruitment.html'),
    ]
    
    for label, anchor_url in anchors:
        pattern = rf'(<a href="{re.escape(anchor_url)}"[^<]*</a>)'
        replacement = insert_str + r'\n            \1'
        temp = re.sub(pattern, replacement, content)
        if temp != content:
            new_content = temp
            print(f'[ADD] {fname} -> {label}')
            break
    
    if new_content:
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
    else:
        print(f'[SKIP] {fname}: no anchor found')

print(f'\nDone: {count} files updated')
