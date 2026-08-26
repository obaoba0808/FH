import urllib.request, os, sys

IMGDIR = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/images'
os.makedirs(IMGDIR, exist_ok=True)

images = [
    ('hero-beginners-checklist.webp', 'https://images.unsplash.com/photo-1607082348824-0a96f2a4b9da?w=1536&q=85&fm=webp'),
    ('hero-pricing-table.webp',       'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1536&q=85&fm=webp'),
    ('hero-private-party.webp',       'https://images.unsplash.com/photo-1530103862676-de8c9debad1d?w=1536&q=85&fm=webp'),
]

for fname, url in images:
    out = os.path.join(IMGDIR, fname)
    if os.path.exists(out):
        print(f'SKIP: {fname}')
        continue
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        with open(out, 'wb') as f:
            f.write(data)
        print(f'OK: {fname} ({len(data)//1024}KB)')
    except Exception as e:
        print(f'FAIL {fname}: {e}', file=sys.stderr)
