from pathlib import Path
import re

pattern = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.DOTALL)
qt = '"'
org_tag = qt + "@type" + qt + ":" + qt + "Organization" + qt

for fname in ['index.html', 'about-oppa.html', 'faq-all-in-one.html']:
    f = Path(fname)
    if not f.exists():
        print(fname + ': NOT FOUND')
        continue
    html = f.read_text('utf-8')
    scripts = list(pattern.finditer(html))
    print('\n' + fname + ': ' + str(len(scripts)) + ' ld+json scripts')
    for i, m in enumerate(scripts):
        content = m.group(1).strip()[:100]
        tags = []
        for t in ['Organization', 'Article', 'WebSite', 'FAQPage', 'BreadcrumbList']:
            if qt + t + qt in content: tags.append(t)
        print('  [' + str(i) + '] ' + (', '.join(tags) if tags else 'other'))
    print('  orgCount: ' + str(html.count(org_tag)))
    print('  has sameAs: ' + str('sameAs' in html))
    print('  has 新北市: ' + str('新北市' in html))
