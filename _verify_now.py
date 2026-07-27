from pathlib import Path
import re

pattern = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.DOTALL)
qt = '"'
org_tag = qt + "@type" + qt + ":" + qt + "Organization" + qt

checks_map = {
    'sameAs': 'sameAs',
    'newAs_TC': qt + '新北市' + qt,
    'cleanTel': '+886926656666',
    'noDash': '+886-926-656-666',
    'twenty47': '"24/7"',
    'priceRange': '"priceRange"',
    'founding': '"foundingDate"',
    'altName': '"alternateName"' + qt + ':' + qt + '歐巴傳播',
}

for fname in ['index.html', 'about-oppa.html', 'faq-all-in-one.html']:
    f = Path(fname)
    if not f.exists():
        print('NOT FOUND: ' + fname)
        continue
    html = f.read_text('utf-8')
    scripts = list(pattern.finditer(html))
    org_count = html.count(org_tag)
    print('\n=== ' + fname + ' ===')
    print('  Scripts: ' + str(len(scripts)))
    print('  OrgCount: ' + str(org_count))
    for k, search in checks_map.items():
        found = search in html
        print('  ' + ('[OK]' if found else '[!!]') + ' ' + k + ': ' + str(found))
