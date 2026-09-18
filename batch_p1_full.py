import re
import os
from datetime import datetime

# Phase 1: Technical SEO optimization for ALL pages
# Apply to all HTML files in the website directory

PAGES_INFO = {
    'index.html': ('傳播妹｜台北傳播公司｜KTV歡唱、派對首選｜歐巴傳播', 'https://obaoba.online/'),
    'news.html': ('情報特搜站｜傳播業最新資訊｜歐巴傳播', 'https://obaoba.online/news.html'),
    'first-chat-topics.html': ('第一次聊天話題｜傳播互動技巧｜歐巴傳播', 'https://obaoba.online/first-chat-topics.html'),
    'venue-guide-2026.html': ('2026場地選擇指南｜KTV、Motel、飯店推薦｜歐巴傳播', 'https://obaoba.online/venue-guide-2026.html'),
    'newbie-guide-2026.html': ('2026新手完整攻略｜第一次叫傳播必看｜歐巴傳播', 'https://obaoba.online/newbie-guide-2026.html'),
    'how_much.html': ('叫傳播多少錢？2026最新行情｜歐巴傳播', 'https://obaoba.online/how_much.html'),
    'safety_privacy.html': ('安全與隱私｜歐巴傳播保障機制｜歐巴傳播', 'https://obaoba.online/safety_privacy.html'),
    'recruitment.html': ('公關招募｜加入歐巴傳播｜歐巴傳播', 'https://obaoba.online/recruitment.html'),
    'KTV_recommendations.html': ('台北KTV推薦｜傳播派對最佳場所｜歐巴傳播', 'https://obaoba.online/KTV_recommendations.html'),
    'shoot_switch_personnel.html': ('打槍換人機制｜歐巴傳播服務保障｜歐巴傳播', 'https://obaoba.online/shoot_switch_personnel.html'),
    'one_by_one.html': ('一對一陪伴服務｜專屬公關體驗｜歐巴傳播', 'https://obaoba.online/one_by_one.html'),
    'special_industries.html': ('特殊行業服務｜歐巴傳播專業外派｜歐巴傳播', 'https://obaoba.online/special_industries.html'),
    'suitable_female.html': ('適合女性的服務｜歐巴傳播多元選擇｜歐巴傳播', 'https://obaoba.online/suitable_female.html'),
    'motel_safe.html': ('汽車旅館安全指南｜歐巴傳播｜歐巴傳播', 'https://obaoba.online/motel_safe.html'),
    'KTV_party.html': ('KTV派對攻略｜歐巴傳播歡唱指南｜歐巴傳播', 'https://obaoba.online/KTV_party.html'),
    'interaction_scale.html': ('互動尺度說明｜歐巴傳播服務規範｜歐巴傳播', 'https://obaoba.online/interaction_scale.html'),
    'first_time_called.html': ('第一次叫傳播？新手必看完整攻略｜歐巴傳播', 'https://obaoba.online/first_time_called.html'),
    'business_dinner.html': ('商務飯局公關｜歐巴傳播專業招待｜歐巴傳播', 'https://obaoba.online/business_dinner.html'),
    'is_this_right_for_you.html': ('這適合你嗎？｜歐巴傳播服務評估｜歐巴傳播', 'https://obaoba.online/is_this_right_for_you.html'),
    'shoot_guide.html': ('打槍機制完整說明｜歐巴傳播｜歐巴傳播', 'https://obaoba.online/shoot_guide.html'),
    'can-touch-guide.html': ('互動界線指南｜歐巴傳播服務規範｜歐巴傳播', 'https://obaoba.online/can-touch-guide.html'),
    'companion-levels-2026.html': ('2026公關等級說明｜歐巴傳播分級制度｜歐巴傳播', 'https://obaoba.online/companion-levels-2026.html'),
    'male_companion.html': ('男公關服務｜歐巴傳播多元選擇｜歐巴傳播', 'https://obaoba.online/male_companion.html'),
    'taipei_agency_guide.html': ('台北傳播公司指南｜如何選擇優質業者｜歐巴傳播', 'https://obaoba.online/taipei_agency_guide.html'),
    'first-time-2026.html': ('2026新手入門｜第一次叫傳播完整流程｜歐巴傳播', 'https://obaoba.online/first-time-2026.html'),
    'tipping-guide-2026.html': ('2026小費指南｜歐巴傳播禮儀說明｜歐巴傳播', 'https://obaoba.online/tipping-guide-2026.html'),
    'safety-guide-2026.html': ('2026安全指南｜叫傳播注意事項｜歐巴傳播', 'https://obaoba.online/safety-guide-2026.html'),
    'how-to-choose-right-companion.html': ('如何選擇適合的公關｜歐巴傳播選人指南｜歐巴傳播', 'https://obaoba.online/how-to-choose-right-companion.html'),
    'compare-girls.html': ('公關類型比較｜歐巴傳播選擇指南｜歐巴傳播', 'https://obaoba.online/compare-girls.html'),
    'business-guide.html': ('商務公關推薦攻略｜歐巴傳播', 'https://obaoba.online/business-guide.html'),
    'legality-guide.html': ('合法性說明｜歐巴傳播合規服務｜歐巴傳播', 'https://obaoba.online/legality-guide.html'),
    'booking-guide.html': ('預約流程指南｜歐巴傳播訂位教學｜歐巴傳播', 'https://obaoba.online/booking-guide.html'),
    'pricing-guide-2026.html': ('2026價格完整指南｜歐巴傳播收費說明｜歐巴傳播', 'https://obaoba.online/pricing-guide-2026.html'),
    'faq-all-in-one.html': ('常見問題36題｜叫傳播FAQ完整解析｜歐巴傳播', 'https://obaoba.online/faq-all-in-one.html'),
    'about-oppa.html': ('關於歐巴傳播｜台北頂級傳播公司｜歐巴傳播', 'https://obaoba.online/about-oppa.html'),
    'beginners-checklist.html': ('新手檢查清單｜第一次叫傳播準備｜歐巴傳播', 'https://obaoba.online/beginners-checklist.html'),
    '2026-pricing-table.html': ('2026價格表｜歐巴傳播收費一覽｜歐巴傳播', 'https://obaoba.online/2026-pricing-table.html'),
    'private-party-guide.html': ('私人派對攻略｜歐巴傳播聚會指南｜歐巴傳播', 'https://obaoba.online/private-party-guide.html'),
}

# HTML Sitemap navigation to add before copyright
HTML_SITEMAP = '''<nav aria-label="網站導覽" class="mb-4"><div class="flex flex-wrap justify-center gap-x-3 gap-y-1 text-xs"><a href="index.html" class="text-gray-400 hover:text-white transition-colors">首頁</a><span class="text-gray-600">·</span><a href="how_much.html" class="text-gray-400 hover:text-white transition-colors">收費行情</a><span class="text-gray-600">·</span><a href="first_time_called.html" class="text-gray-400 hover:text-white transition-colors">新手指南</a><span class="text-gray-600">·</span><a href="KTV_recommendations.html" class="text-gray-400 hover:text-white transition-colors">KTV推薦</a><span class="text-gray-600">·</span><a href="motel_safe.html" class="text-gray-400 hover:text-white transition-colors">Motel指南</a><span class="text-gray-600">·</span><a href="safety_privacy.html" class="text-gray-400 hover:text-white transition-colors">安全隱私</a><span class="text-gray-600">·</span><a href="faq-all-in-one.html" class="text-gray-400 hover:text-white transition-colors">常見問題</a><span class="text-gray-600">·</span><a href="about-oppa.html" class="text-gray-400 hover:text-white transition-colors">關於我們</a></div></nav>'''

def optimize_page(filepath, page_name, page_url):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # P1-1: Google Fonts async loading (if present and not already optimized)
    if 'fonts.googleapis.com' in content and 'onload=' not in content:
        content = re.sub(
            r'<link href="(https://fonts\.googleapis\.com/[^"]+)" rel="stylesheet">',
            r'<link rel="preload" href="\1" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n    <noscript><link href="\1" rel="stylesheet"></noscript>',
            content
        )
        changes.append('P1-1: Google Fonts async load')
    
    # P1-3: Add fetchpriority="low" to non-hero images with loading="lazy"
    lazy_imgs = re.findall(r'<img[^>]*loading="lazy"[^>]*>', content)
    lazy_count = 0
    for img in lazy_imgs:
        if 'fetchpriority' not in img:
            new_img = img.replace('loading="lazy"', 'loading="lazy" fetchpriority="low"')
            content = content.replace(img, new_img, 1)
            lazy_count += 1
    if lazy_count > 0:
        changes.append(f'P1-3: fetchpriority=low on {lazy_count} lazy images')
    
    # P1-4: Add HTML Sitemap nav before copyright (if not present)
    if 'aria-label="網站導覽"' not in content and '©' in content:
        content = re.sub(
            r'(<p[^>]*>.*?©.*?)</p>',
            HTML_SITEMAP + r'\1</p>',
            content
        )
        changes.append('P1-4: HTML Sitemap nav')
    
    # P1-5: Add WebPage Schema if missing (and not index.html which already has it)
    if 'WebPage' not in content and filepath != 'index.html':
        webpage_schema = f'''<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "@id": "{page_url}#webpage", "url": "{page_url}", "name": "{page_name}", "inLanguage": "zh-TW", "isPartOf": {{"@id": "https://obaoba.online/#website"}}, "about": {{"@id": "https://obaoba.online/#organization"}}}}</script>'''
        # Insert after the first schema script or before </head>
        if 'application/ld+json' in content:
            first_schema_end = content.find('</script>', content.find('application/ld+json')) + 9
            content = content[:first_schema_end] + '\n    ' + webpage_schema + content[first_schema_end:]
        else:
            head_end = content.find('</head>')
            if head_end != -1:
                content = content[:head_end] + '    ' + webpage_schema + '\n' + content[head_end:]
        changes.append('P1-5: WebPage Schema added')
    
    # P1-5: Add Article Schema for content pages (news, guide, etc.)
    if 'Article' not in content and any(x in filepath for x in ['news', 'guide', 'how-to', 'faq', 'checklist']):
        article_schema = f'''<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Article", "headline": "{page_name.split('｜')[0]}", "url": "{page_url}", "inLanguage": "zh-TW", "author": {{"@type": "Organization", "name": "歐巴傳播"}}, "publisher": {{"@id": "https://obaoba.online/#organization"}}, "datePublished": "2026-09-18", "dateModified": "2026-09-18"}}</script>'''
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + '    ' + article_schema + '\n' + content[head_end:]
            changes.append('P1-5: Article Schema added')
    
    # P1-6: Ensure single H1
    h1_count = len(re.findall(r'<h1[>\s]', content))
    if h1_count > 1:
        changes.append(f'WARNING: Multiple H1 tags ({h1_count})')
    elif h1_count == 0:
        changes.append('WARNING: No H1 tag')
    else:
        changes.append('P1-6: Single H1 verified')
    
    # Write if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    else:
        return False, changes

# Process all HTML files
total_modified = 0
total_files = 0

for filename, (page_name, page_url) in PAGES_INFO.items():
    if os.path.exists(filename):
        total_files += 1
        changed, changes = optimize_page(filename, page_name, page_url)
        status = 'MODIFIED' if changed else 'NO CHANGE'
        print(f'[{status}] {filename}')
        for change in changes:
            print(f'  - {change}')
        if changed:
            total_modified += 1
        print('')
    else:
        print(f'[MISSING] {filename}')

print('=' * 50)
print(f'Total files processed: {total_files}')
print(f'Total files modified: {total_modified}')
print(f'Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
