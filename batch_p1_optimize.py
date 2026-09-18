import re
import os

# P1 optimizations to apply to each page
def optimize_page(filepath, page_name, page_url):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # P1-1: Google Fonts async loading (if present)
    if 'fonts.googleapis.com' in content and 'onload=' not in content:
        content = re.sub(
            r'<link href="(https://fonts\.googleapis\.com/[^"]+)" rel="stylesheet">',
            r'<link rel="preload" href="\1" as="style" onload="this.onload=null;this.rel=\'stylesheet\'">\n    <noscript><link href="\1" rel="stylesheet"></noscript>',
            content
        )
        changes.append('P1-1: Google Fonts async load')
    
    # P1-3: Add fetchpriority="low" to non-hero images with loading="lazy"
    # Find img tags with loading="lazy" but without fetchpriority
    lazy_imgs = re.findall(r'<img[^>]*loading="lazy"[^>]*>', content)
    for img in lazy_imgs:
        if 'fetchpriority' not in img:
            new_img = img.replace('loading="lazy"', 'loading="lazy" fetchpriority="low"')
            content = content.replace(img, new_img, 1)
            changes.append('P1-3: fetchpriority=low on lazy image')
    
    # P1-4: Add HTML Sitemap nav before copyright (if not present)
    if 'aria-label="網站導覽"' not in content and '©' in content:
        # Find the copyright line and add sitemap before it
        content = re.sub(
            r'(<p[^>]*>.*?©.*?)</p>',
            r'<nav aria-label="網站導覽" class="mb-4"><div class="flex flex-wrap justify-center gap-x-3 gap-y-1 text-xs"><a href="index.html" class="text-gray-400 hover:text-white transition-colors">首頁</a><span class="text-gray-600">·</span><a href="how_much.html" class="text-gray-400 hover:text-white transition-colors">收費行情</a><span class="text-gray-600">·</span><a href="first_time_called.html" class="text-gray-400 hover:text-white transition-colors">新手指南</a><span class="text-gray-600">·</span><a href="KTV_recommendations.html" class="text-gray-400 hover:text-white transition-colors">KTV推薦</a><span class="text-gray-600">·</span><a href="motel_safe.html" class="text-gray-400 hover:text-white transition-colors">Motel指南</a><span class="text-gray-600">·</span><a href="safety_privacy.html" class="text-gray-400 hover:text-white transition-colors">安全隱私</a><span class="text-gray-600">·</span><a href="faq-all-in-one.html" class="text-gray-400 hover:text-white transition-colors">常見問題</a><span class="text-gray-600">·</span><a href="about-oppa.html" class="text-gray-400 hover:text-white transition-colors">關於我們</a></div></nav>\1</p>',
            content
        )
        changes.append('P1-4: HTML Sitemap nav')
    
    # P1-5: Convert separate schemas to @graph (if multiple ld+json scripts)
    schema_scripts = re.findall(r'<script type="application/ld\+json">(.*?)</script>', content, re.DOTALL)
    if len(schema_scripts) > 1 and '@graph' not in content:
        # This is complex - for now, just add WebPage schema if missing
        if 'WebPage' not in content:
            # Add WebPage schema after the first schema
            webPage_schema = f'''<script type="application/ld+json">{{"@context": "https://schema.org", "@type": "WebPage", "@id": "{page_url}#webpage", "url": "{page_url}", "name": "{page_name}", "inLanguage": "zh-TW", "isPartOf": {{"@id": "https://obaoba.online/#website"}}, "about": {{"@id": "https://obaoba.online/#organization"}}}}</script>'''
            # Insert after the first schema script
            first_schema_end = content.find('</script>', content.find('application/ld+json')) + 9
            content = content[:first_schema_end] + '\n    ' + webPage_schema + content[first_schema_end:]
            changes.append('P1-5: WebPage Schema added')
    
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
pages = [
    ('how_much.html', '叫傳播多少錢？2026最新行情｜歐巴傳播', 'https://obaoba.online/how_much.html'),
    ('first_time_called.html', '第一次叫傳播？新手必看完整攻略｜歐巴傳播', 'https://obaoba.online/first_time_called.html'),
    ('KTV_recommendations.html', '台北KTV推薦｜傳播派對最佳場所｜歐巴傳播', 'https://obaoba.online/KTV_recommendations.html'),
    ('motel_safe.html', '汽車旅館叫傳播安全指南｜歐巴傳播', 'https://obaoba.online/motel_safe.html'),
    ('business-guide.html', '商務公關推薦攻略｜歐巴傳播', 'https://obaoba.online/business-guide.html'),
]

for filename, page_name, page_url in pages:
    if os.path.exists(filename):
        changed, changes = optimize_page(filename, page_name, page_url)
        status = 'MODIFIED' if changed else 'NO CHANGE'
        print(f'[{status}] {filename}')
        for change in changes:
            print(f'  - {change}')
        print('')
    else:
        print(f'[MISSING] {filename}')
