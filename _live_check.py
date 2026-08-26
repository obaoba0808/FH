import urllib.request, sys

pages = [
    'https://obaoba.online/beginners-checklist.html',
    'https://obaoba.online/2026-pricing-table.html',
    'https://obaoba.online/private-party-guide.html',
    'https://obaoba.online/sitemap.xml',
]
for url in pages:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as r:
            body = r.read().decode('utf-8', errors='replace')
            print(f'{r.status} {url} ({len(body)} bytes)')
            if 'sitemap' in url:
                print('  has beginners-checklist:', 'beginners-checklist' in body)
                print('  has pricing-table:', '2026-pricing-table' in body)
                print('  has private-party:', 'private-party-guide' in body)
    except Exception as e:
        print(f'ERR {url}: {e}')
