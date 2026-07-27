"""
GEO Phase 3 — 實體一致性 & sameAs
全站 3 頁：移除所有現有 Organization JSON-LD，注入超集模板。
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent

ORG_JSONLD = (
    '{"@context":"https://schema.org","@type":"Organization","name":"歐巴傳播 OPPA ENT.",'
    '"alternateName":"歐巴傳播","url":"https://obaoba.online/",'
    '"logo":"https://obaoba.online/android-chrome-512x512.png",'
    '"image":"https://obaoba.online/og-image.jpg",'
    '"description":"歐巴傳播是台北的頂級傳播（外出陪伴）服務公司，提供 KTV 派對、汽車旅館派對、商務飯局、一對一陪伴與私人派對等公關到府服務，服務範圍涵蓋大台北地區。",'
    '"areaServed":[{"@type":"City","name":"台北市"},{"@type":"City","name":"新北市"}],'
    '"priceRange":"NT$1,200-3,500","foundingDate":"2022",'
    '"contactPoint":{"@type":"ContactPoint","telephone":"+886926656666","contactType":"預約專線","availableLanguage":["Chinese"],"hoursAvailable":"24/7"},'
    '"address":{"@type":"PostalAddress","addressLocality":"台北市","addressRegion":"台灣","addressCountry":"TW"},'
    '"sameAs":["https://line.me/ti/p/~938nzmjr"]}'
)
ORG_TAG = f'<script type="application/ld+json">\n{ORG_JSONLD}\n</script>'

def remove_org_scripts(html: str) -> str:
    """Remove any ld+json script block whose content starts with '{' and contains '@type":"Organization'"."""
    def replacer(m):
        content = m.group(1)
        stripped = content.strip()
        if stripped.startswith('{') and '"@type":"Organization"' in stripped:
            return ''  # remove it
        return m.group(0)
    pattern = re.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', re.DOTALL)
    return pattern.sub(replacer, html)

def inject_before_head(html: str) -> str:
    return html.replace('</head>', ORG_TAG + '\n</head>', 1)

def verify(html: str) -> dict[str, bool]:
    return {
        'sameAs':     '"sameAs"' in html,
        'newAs_TC':   '"新北市"' in html,
        'cleanTel':   '+886926656666' in html,
        'noDash':     '+886-926-656-666' not in html,
        'twenty47':   '"24/7"' in html,
        'priceRange': '"priceRange"' in html,
        'founding':   '"foundingDate"' in html,
        'altName':    '"alternateName"' in html,
        'orgOnce':    html.count('"@type":"Organization"') == 1,
    }

PAGES = ['index.html', 'about-oppa.html', 'faq-all-in-one.html']

def main():
    for page in PAGES:
        fpath = ROOT / page
        if not fpath.exists():
            print(f'[--] {page}: NOT FOUND')
            continue
        html = fpath.read_text('utf-8')
        html = remove_org_scripts(html)
        html = inject_before_head(html)
        fpath.write_text(html, 'utf-8')

    print('\n--- Verification ---')
    for page in PAGES:
        fpath = ROOT / page
        if not fpath.exists():
            continue
        html = fpath.read_text('utf-8')
        v = verify(html)
        all_ok = all(v.values())
        print(('[OK]' if all_ok else '[FAIL]') + ' ' + page)
        for k, val in v.items():
            print('    ' + ('[OK]' if val else '[!!]') + ' ' + k)

if __name__ == '__main__':
    main()
