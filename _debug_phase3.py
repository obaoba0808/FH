"""Quick debug of _geo_phase3.py logic on about-oppa.html"""
import re
from pathlib import Path

ROOT = Path('.')

html = (ROOT / 'about-oppa.html').read_text('utf-8')
print(f'File size: {len(html)} chars')

# Find all ld+json scripts
pattern = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.DOTALL)
scripts = list(pattern.finditer(html))
print(f'\nFound {len(scripts)} ld+json scripts:')
for i, m in enumerate(scripts):
    content = m.group(1).strip()[:80]
    tags = []
    if '"Organization"' in content: tags.append('Org')
    if '"Article"' in content: tags.append('Article')
    if '"WebSite"' in content: tags.append('WebSite')
    if '"FAQPage"' in content: tags.append('FAQPage')
    print(f'  [{i}] {", ".join(tags) if tags else "other"}: {content}...')

# Check current state of about-oppa.html
print(f'\n--- Current about-oppa.html state ---')
print(f'  has sameAs: {"sameAs" in html}')
print(f'  has 新北市: {"新北市" in html}')
print(f'  has priceRange: {"priceRange" in html}')
print(f'  org count: {html.count(chr(34)+"@type"+chr(34)+":"+chr(34)+"Organization"+chr(34))}')
