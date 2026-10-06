import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('=== P1 Verification ===')
print('')

# 1. Google Fonts optimization
if 'onload="this.onload=null;this.rel=' in content:
    print('[P1-1] Google Fonts async load: OK')
else:
    print('[P1-1] Google Fonts async load: MISSING')

if '<noscript><link href="https://fonts.googleapis.com' in content:
    print('[P1-1] Noscript fallback: OK')
else:
    print('[P1-1] Noscript fallback: MISSING')

# 2. Image fetchpriority
if 'fetchpriority="low"' in content:
    print('[P1-3] Image fetchpriority=low: OK')
else:
    print('[P1-3] Image fetchpriority=low: MISSING')

# 3. Internal links (HTML sitemap)
if 'aria-label="網站導覽"' in content:
    print('[P1-4] HTML Sitemap nav: OK')
else:
    print('[P1-4] HTML Sitemap nav: MISSING')

# 4. Schema @graph
if '@graph' in content:
    print('[P1-5] Schema @graph: OK')
else:
    print('[P1-5] Schema @graph: MISSING')

# 5. Service Schema
if 'serviceType' in content:
    print('[P1-5] Service Schema: OK')
else:
    print('[P1-5] Service Schema: MISSING')

# 6. WebPage Schema
if 'WebPage' in content:
    print('[P1-5] WebPage Schema: OK')
else:
    print('[P1-5] WebPage Schema: MISSING')

# Count schema types
schema_types = re.findall(r'"@type": "([^"]+)"', content)
print('')
print('Schema types found:', ', '.join(schema_types))

# Check for duplicate H1
h1_count = len(re.findall(r'<h1[>\s]', content))
print('')
print('H1 count:', h1_count)

# Check title
title = re.search(r'<title>([^<]+)</title>', content)
if title:
    print('Title:', title.group(1))
