with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('=== P0 Verification ===')
print('')

# P0-1: H1 check
h1_count = content.count('<h1')
h2_count = content.count('<h2')
print('[P0-1] H1 count:', h1_count)
print('[P0-1] H2 count:', h2_count)
if h1_count == 1:
    print('[P0-1] PASS: Only one H1')
else:
    print('[P0-1] FAIL: Multiple H1s found')

# P0-2: OG Image path
if 'https://obaoba.online/images/og-image.jpg' in content:
    print('[P0-2] PASS: OG image path correct')
else:
    print('[P0-2] FAIL: OG image path incorrect')

# Check Organization image
if '"image": "https://obaoba.online/images/og-image.jpg"' in content:
    print('[P0-2] PASS: Organization Schema image path correct')
else:
    print('[P0-2] FAIL: Organization Schema image path incorrect')

# P0-3: Title separator
if '<title>傳播妹｜台北傳播公司｜KTV歡唱、派對首選｜歐巴傳播</title>' in content:
    print('[P0-3] PASS: Title uses full-width separator')
else:
    print('[P0-3] FAIL: Title separator not fixed')

# OG title
if 'content="歐巴傳播｜台北頂級傳播公司｜傳播妹、KTV歡唱、派對首選"' in content:
    print('[P0-3] PASS: OG title uses full-width separator')
else:
    print('[P0-3] FAIL: OG title separator not fixed')

# P0-5: BreadcrumbList
if 'BreadcrumbList' in content:
    print('[P0-5] PASS: BreadcrumbList Schema present')
else:
    print('[P0-5] FAIL: BreadcrumbList Schema missing')

print('')
print('=== sitemap.xml ===')
with open('sitemap.xml', 'r', encoding='utf-8') as f:
    sitemap = f.read()

import re
lastmod_dates = re.findall(r'<lastmod>(\d{4}-\d{2}-\d{2})</lastmod>', sitemap)
unique_dates = set(lastmod_dates)
print('[P0-4] Unique lastmod dates:', unique_dates)
if len(unique_dates) == 1:
    print('[P0-4] PASS: All lastmod dates unified to', list(unique_dates)[0])
else:
    print('[P0-4] FAIL: Multiple lastmod dates found')
