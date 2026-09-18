import re
import os

# Page info mapping
PAGE_INFO = {
    'news.html': ('情報特搜站｜傳播業最新動態｜歐巴傳播', 'https://obaoba.online/news.html'),
    'first-chat-topics.html': ('第一次叫傳播聊什麼？話題攻略｜歐巴傳播', 'https://obaoba.online/first-chat-topics.html'),
    'venue-guide-2026.html': ('2026台北傳播場所推薦指南｜歐巴傳播', 'https://obaoba.online/venue-guide-2026.html'),
    'newbie-guide-2026.html': ('2026傳播新手入門完整指南｜歐巴傳播', 'https://obaoba.online/newbie-guide-2026.html'),
    'how_much.html': ('叫傳播多少錢？2026最新行情｜歐巴傳播', 'https://obaoba.online/how_much.html'),
    'safety_privacy.html': ('傳播安全與隱私完整指南｜歐巴傳播', 'https://obaoba.online/safety_privacy.html'),
    'recruitment.html': ('傳播妹徵才｜加入歐巴傳播｜歐巴傳播', 'https://obaoba.online/recruitment.html'),
    'KTV_recommendations.html': ('台北KTV推薦｜傳播派對最佳場所｜歐巴傳播', 'https://obaoba.online/KTV_recommendations.html'),
    'shoot_switch_personnel.html': ('打槍換人完全攻略｜歐巴傳播', 'https://obaoba.online/shoot_switch_personnel.html'),
    'one_by_one.html': ('一個人叫傳播可以嗎？｜歐巴傳播', 'https://obaoba.online/one_by_one.html'),
    'special_industries.html': ('特殊行業叫傳播指南｜歐巴傳播', 'https://obaoba.online/special_industries.html'),
    'suitable_female.html': ('如何選擇適合的傳播妹？｜歐巴傳播', 'https://obaoba.online/suitable_female.html'),
    'motel_safe.html': ('汽車旅館叫傳播安全指南｜歐巴傳播', 'https://obaoba.online/motel_safe.html'),
    'KTV_party.html': ('KTV派對玩法攻略｜歐巴傳播', 'https://obaoba.online/KTV_party.html'),
    'interaction_scale.html': ('傳播互動尺度說明｜歐巴傳播', 'https://obaoba.online/interaction_scale.html'),
    'first_time_called.html': ('第一次叫傳播？新手必看完整攻略｜歐巴傳播', 'https://obaoba.online/first_time_called.html'),
    'business_dinner.html': ('商務飯局傳播攻略｜歐巴傳播', 'https://obaoba.online/business_dinner.html'),
    'is_this_right_for_you.html': ('叫傳播適合我嗎？｜歐巴傳播', 'https://obaoba.online/is_this_right_for_you.html'),
    'shoot_guide.html': ('打槍換人完全攻略｜歐巴傳播', 'https://obaoba.online/shoot_guide.html'),
    'can-touch-guide.html': ('傳播互動尺度說明｜歐巴傳播', 'https://obaoba.online/can-touch-guide.html'),
    'companion-levels-2026.html': ('2026傳播公關等級與價格對照｜歐巴傳播', 'https://obaoba.online/companion-levels-2026.html'),
    'male_companion.html': ('男公關服務｜歐巴傳播', 'https://obaoba.online/male_companion.html'),
    'taipei_agency_guide.html': ('台北傳播公司推薦指南｜歐巴傳播', 'https://obaoba.online/taipei_agency_guide.html'),
    'first-time-2026.html': ('2026第一次叫傳播完整攻略｜歐巴傳播', 'https://obaoba.online/first-time-2026.html'),
    'tipping-guide-2026.html': ('2026傳播小費指南｜歐巴傳播', 'https://obaoba.online/tipping-guide-2026.html'),
    'safety-guide-2026.html': ('2026傳播安全指南｜歐巴傳播', 'https://obaoba.online/safety-guide-2026.html'),
    'how-to-choose-right-companion.html': ('如何選擇適合的傳播妹？｜歐巴傳播', 'https://obaoba.online/how-to-choose-right-companion.html'),
    'compare-girls.html': ('傳播妹 vs 酒店小姐比較｜歐巴傳播', 'https://obaoba.online/compare-girls.html'),
    'business-guide.html': ('商務公關推薦攻略｜歐巴傳播', 'https://obaoba.online/business-guide.html'),
    'legality-guide.html': ('叫傳播合法嗎？法律指南｜歐巴傳播', 'https://obaoba.online/legality-guide.html'),
    'booking-guide.html': ('傳播預約流程完整攻略｜歐巴傳播', 'https://obaoba.online/booking-guide.html'),
    'pricing-guide-2026.html': ('2026傳播價格完整指南｜歐巴傳播', 'https://obaoba.online/pricing-guide-2026.html'),
    'faq-all-in-one.html': ('傳播常見問題FAQ｜歐巴傳播', 'https://obaoba.online/faq-all-in-one.html'),
    'about-oppa.html': ('關於歐巴傳播｜台北頂級傳播公司｜歐巴傳播', 'https://obaoba.online/about-oppa.html'),
    'beginners-checklist.html': ('傳播新手檢查清單｜歐巴傳播', 'https://obaoba.online/beginners-checklist.html'),
    '2026-pricing-table.html': ('2026傳播價格對照表｜歐巴傳播', 'https://obaoba.online/2026-pricing-table.html'),
    'private-party-guide.html': ('私人派對傳播攻略｜歐巴傳播', 'https://obaoba.online/private-party-guide.html'),
}

def optimize_page(filepath):
    filename = os.path.basename(filepath)
    if filename not in PAGE_INFO:
        return False, ['Unknown page']
    
    page_name, page_url = PAGE_INFO[filename]
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # P1-3: Add fetchpriority="low" to lazy-loaded images
    lazy_imgs = re.findall(r'<img[^>]*loading="lazy"[^>]*>', content)
    lazy_count = 0
    for img in lazy_imgs:
        if 'fetchpriority' not in img:
            new_img = img.replace('loading="lazy"', 'loading="lazy" fetchpriority="low"')
            content = content.replace(img, new_img, 1)
            lazy_count += 1
    if lazy_count > 0:
        changes.append(f'P1-3: fetchpriority=low on {lazy_count} lazy image(s)')
    
    # P1-5: Add WebPage Schema if missing (and page has some schema)
    has_schema = 'application/ld+json' in content
    has_webpage = 'WebPage' in content
    if has_schema and not has_webpage:
        webPage_schema = f'''<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "@id": "{page_url}#webpage", "url": "{page_url}", "name": "{page_name}", "inLanguage": "zh-TW", "isPartOf": {{"@id": "https://obaoba.online/#website"}}, "about": {{"@id": "https://obaoba.online/#organization"}}}}</script>'''
        # Insert after the first schema script
        first_schema_end = content.find('</script>', content.find('application/ld+json')) + 9
        content = content[:first_schema_end] + '\n    ' + webPage_schema + content[first_schema_end:]
        changes.append('P1-5: WebPage Schema added')
    elif not has_schema:
        # Add basic WebPage schema if no schema at all
        webPage_schema = f'''<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "@id": "{page_url}#webpage", "url": "{page_url}", "name": "{page_name}", "inLanguage": "zh-TW", "isPartOf": {{"@id": "https://obaoba.online/#website"}}, "about": {{"@id": "https://obaoba.online/#organization"}}}}</script>'''
        # Insert before </head>
        head_end = content.find('</head>')
        if head_end > 0:
            content = content[:head_end] + '    ' + webPage_schema + '\n' + content[head_end:]
            changes.append('P1-5: WebPage Schema added (no existing schema)')
    
    # P1-6: Verify single H1
    h1_count = len(re.findall(r'<h1[>\s]', content))
    if h1_count == 1:
        changes.append('P1-6: Single H1 verified')
    elif h1_count > 1:
        changes.append(f'WARNING: {h1_count} H1 tags')
    else:
        changes.append('WARNING: No H1 tag')
    
    # Write if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    else:
        return False, changes

# Process all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html']
modified_count = 0
results = []

for filepath in sorted(html_files):
    changed, changes = optimize_page(filepath)
    status = 'MODIFIED' if changed else 'NO CHANGE'
    if changed:
        modified_count += 1
    results.append((filepath, status, changes))

# Print results
for filepath, status, changes in results:
    print(f'[{status}] {filepath}')
    for change in changes:
        print(f'  - {change}')

print(f'\nTotal: {modified_count}/{len(html_files)} files modified')
