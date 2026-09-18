import re
from datetime import datetime

# ========== P0-1: H1 修復 ==========
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 修復 H1: 將 <br> 改為 H1 + H2
old_h1 = '<h1 class="text-5xl md:text-7xl font-black mb-6 leading-tight tracking-tight">\n                <span class="text-gradient">台北傳播公司推薦</span> <br>\n                歐巴傳播 — 頂級VIP專屬體驗\n            </h1>'

new_h1 = '<h1 class="text-5xl md:text-7xl font-black mb-2 leading-tight tracking-tight">\n                <span class="text-gradient">台北傳播公司推薦</span>\n            </h1>\n            <h2 class="text-3xl md:text-5xl font-bold mb-6 leading-tight tracking-tight text-white">\n                歐巴傳播 — 頂級VIP專屬體驗\n            </h2>'

if old_h1 in content:
    content = content.replace(old_h1, new_h1)
    print('[P0-1] H1 fixed: split into H1 + H2')
else:
    print('[P0-1] WARNING: H1 pattern not found')

# ========== P0-2: OG Image 路徑統一 (Organization Schema) ==========
old_org_image = '"image": "https://obaoba.online/og-image.jpg"'
new_org_image = '"image": "https://obaoba.online/images/og-image.jpg"'
if old_org_image in content:
    content = content.replace(old_org_image, new_org_image)
    print('[P0-2] Organization Schema image path fixed')
else:
    print('[P0-2] WARNING: Organization image path not found')

# ========== P0-3: Title 分隔符格式 ==========
old_title = '<title>傳播妹 | 台北傳播公司 | KTV歡唱、派對首選 |歐巴傳播</title>'
new_title = '<title>傳播妹｜台北傳播公司｜KTV歡唱、派對首選｜歐巴傳播</title>'
if old_title in content:
    content = content.replace(old_title, new_title)
    print('[P0-3] Title separator fixed')
else:
    print('[P0-3] WARNING: Title pattern not found')

# Also fix OG title
old_og_title = '<meta property="og:title" content="歐巴傳播 | 台北頂級傳播公司 | 傳播妹、KTV歡唱、派對首選">'
new_og_title = '<meta property="og:title" content="歐巴傳播｜台北頂級傳播公司｜傳播妹、KTV歡唱、派對首選">'
if old_og_title in content:
    content = content.replace(old_og_title, new_og_title)
    print('[P0-3] OG title separator fixed')

# Fix Twitter title
old_tw_title = '<meta name="twitter:title" content="傳播妹 | 台北傳播公司 |歐巴傳播">'
new_tw_title = '<meta name="twitter:title" content="傳播妹｜台北傳播公司｜歐巴傳播">'
if old_tw_title in content:
    content = content.replace(old_tw_title, new_tw_title)
    print('[P0-3] Twitter title separator fixed')

# ========== P0-5: 新增 BreadcrumbList Schema ==========
breadcrumb_schema = '\n    <!-- BreadcrumbList Schema -->\n    <script type="application/ld+json">{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "首頁", "item": "https://obaoba.online/"}]}</script>'

last_schema_end = content.rfind('</script>\n    </head>')
if last_schema_end != -1:
    insert_pos = last_schema_end + len('</script>')
    content = content[:insert_pos] + breadcrumb_schema + content[insert_pos:]
    print('[P0-5] BreadcrumbList Schema added')
else:
    print('[P0-5] WARNING: Could not find insertion point')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('')
print('index.html modifications complete!')
print('File size: ' + str(len(content)) + ' bytes')

# ========== P0-4: sitemap lastmod 更新 ==========
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

today = datetime.now().strftime('%Y-%m-%d')
# Replace all lastmod dates with today
sitemap_new = re.sub(r'<lastmod>\d{4}-\d{2}-\d{2}</lastmod>', f'<lastmod>{today}</lastmod>', sitemap)

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_new)

print('')
print('[P0-4] sitemap.xml lastmod updated to ' + today)
print('File size: ' + str(len(sitemap_new)) + ' bytes')
