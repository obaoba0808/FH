"""
GEO Phase 4 — 首頁 index.html Schema 大修復 + Meta 清理
目標：
1. Organization JSON-LD — 修復 description 編碼亂碼
2. 補回 WebSite + SearchAction JSON-LD（啟用 Google Sitelinks 搜尋框）
3. 補回 FAQPage JSON-LD（6題）
4. 清理 meta description 重複文字
5. 統一 canonical 為根目錄（無尾斜線）
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent
PAGE = 'index.html'

# ── 1. Organization JSON-LD（修復 description 亂碼）───────────────────────────
ORG_JSONLD = (
    '{"@context":"https://schema.org","@type":"Organization",'
    '"name":"歐巴傳播 OPPA ENT.",'
    '"alternateName":"歐巴傳播",'
    '"url":"https://obaoba.online/",'
    '"logo":"https://obaoba.online/android-chrome-512x512.png",'
    '"image":"https://obaoba.online/og-image.jpg",'
    '"description":"歐巴傳播是台北的頂級傳播（外出陪伴）服務公司，提供 KTV 派對、汽車旅館派對、商務飯局、一對一陪伴與私人派對等公關到府服務，服務範圍涵蓋大台北地區。",'
    '"areaServed":[{"@type":"City","name":"台北市"},{"@type":"City","name":"新北市"}],'
    '"priceRange":"NT$1,200-3,500","foundingDate":"2022",'
    '"contactPoint":{"@type":"ContactPoint","telephone":"+886926656666","contactType":"預約專線","availableLanguage":["Chinese"],"hoursAvailable":"24/7"},'
    '"address":{"@type":"PostalAddress","addressLocality":"台北市","addressRegion":"台灣","addressCountry":"TW"},'
    '"sameAs":["https://line.me/ti/p/~938nzmjr"]}'
)

# ── 2. WebSite + SearchAction JSON-LD（啟用 Google 搜尋框）──────────────────
WEBSITE_JSONLD = (
    '{"@context":"https://schema.org","@type":"WebSite",'
    '"name":"歐巴傳播官方網站",'
    '"url":"https://obaoba.online/",'
    '"potentialAction":{"@type":"SearchAction",'
    '"target":"https://obaoba.online/?q={search_term_string}",'
    '"query-input":"required name=search_term_string"}}'
)

# ── 3. FAQPage JSON-LD（6題）────────────────────────────────────────────────
FAQPAGE_JSONLD = (
    '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['
    '{"@type":"Question","name":"歐巴傳播是什麼公司？",'
    '"acceptedAnswer":{"@type":"Answer","text":"歐巴傳播（OPPA ENT.）是台北的頂級傳播服務公司，主打公關外出到府陪伴模式：公關直接到您指定的餐廳、KTV、汽車旅館或飯店提供陪伴、互動與氣氛帶動服務。與傳統酒店不同，沒有店租與包廂費，帳單只有鐘點費加車馬費，價格比酒店便宜約 40-60%。"}},'
    '{"@type":"Question","name":"歐巴傳播提供哪些服務？",'
    '"acceptedAnswer":{"@type":"Answer","text":"主要服務包含：KTV 派對（包廂炒熱氣氛、點歌互動）；汽車旅館（Motel）派對；商務飯局（招待客戶、餐桌禮儀得體）；一對一陪伴（陪吃飯、陪逛街、純聊天）；私人派對（朋友聚會、生日、公司活動，可一次叫多位公關）。所有服務皆在法律允許範圍內、雙方同意下進行。"}},'
    '{"@type":"Question","name":"歐巴傳播價格大概多少？",'
    '"acceptedAnswer":{"@type":"Answer","text":"鐘點費依公關等級不同，約落在 NT$6,000-15,000 元／2 小時。基礎級 NT$6,000-8,000、標準級 NT$8,000-12,000、VIP 級 NT$12,000-15,000、頂級 NT$15,000 以上。加時每小時約 NT$3,000-5,000 元；大台北核心區車馬費通常免費或 NT$500-1,000 元。實際報價以當日檔期與等級為準，建議加 LINE（@938nzmjr）詢問。"}},'
    '{"@type":"Question","name":"怎麼預約歐巴傳播？",'
    '"acceptedAnswer":{"@type":"Answer","text":"兩種方式：LINE 預約（ID：@938nzmjr，24 小時線上回覆）或電話預約（0926-656666）。預約時告知聚會時間、地點、人數與想要的風格，公司會回傳 2-3 位公關照片供挑選，確認後派單，平均 30 分鐘到府。"}},'
    '{"@type":"Question","name":"叫傳播安全嗎？個資會不會外洩？",'
    '"acceptedAnswer":{"@type":"Answer","text":"找正規公司（如歐巴傳播）非常安全。個資保護措施包含：客戶資料加密儲存、不主動聯絡家人朋友、服務結束後不保留對話紀錄、不公開轉賣個資。公關皆通過身份查核，且採見面確認後再付款，不要求事先匯款大筆金額，有效防範詐騙。"}},'
    '{"@type":"Question","name":"不滿意可以換人嗎？",'
    '"acceptedAnswer":{"@type":"Answer","text":"可以，這是正規公司的基本保障。歐巴傳播的「打槍換人」機制：公關到場後可先確認外貌與氣質，若不滿意可立即免費更換（不限次數）；若連換幾位都不滿意，公司會無條件退款。預約時可要求提供「本人一週內實拍、未修圖」照片，從源頭避免照騙。"}}'
    ']}'
)

# ── 4. Meta description（清理重複文字）──────────────────────────────────────
META_DESC = (
    '歐巴傳播 OPPA ENT. 是台北頂級傳播公司，提供傳播妹桌面服務、KTV派對、'
    '公關陪伴與飯局妹外派服務。LINE：@938nzmjr 立即預約，30分鐘內到府安排。'
)

OG_DESC = (
    '歐巴傳播 OPPA ENT. 是台北頂級傳播公司，提供傳播妹桌面服務、KTV派對、'
    '公關陪伴與飯局妹外派服務。LINE：@938nzmjr 立即預約，30分鐘內到府安排。'
)


def remove_all_jsonld(html: str) -> str:
    """Remove ALL existing JSON-LD script blocks from <head>."""
    pattern = re.compile(
        r'\n?\s*<script[^>]+type=["\']application/ld\+json["\'][^>]*>.*?</script>',
        re.DOTALL
    )
    return pattern.sub('', html)


def inject_before_head_close(html: str) -> str:
    """Build and inject all three JSON-LD blocks before </head>."""
    combined = (
        f'\n    <!-- Schema: Organization + WebSite + FAQPage -->\n'
        f'    <script type="application/ld+json">\n{ORG_JSONLD}\n    </script>\n'
        f'    <script type="application/ld+json">\n{WEBSITE_JSONLD}\n    </script>\n'
        f'    <script type="application/ld+json">\n{FAQPAGE_JSONLD}\n    </script>\n'
    )
    return html.replace('</head>', combined + '</head>', 1)


def fix_meta_description(html: str) -> str:
    """Replace broken meta description with clean version."""
    # Fix <meta name="description">
    html = re.sub(
        r'<meta\s+name=["\']description["\']\s+content="[^"]*"[^>]*>',
        f'<meta name="description" content="{META_DESC}">',
        html
    )
    # Fix og:description
    html = re.sub(
        r'<meta\s+property=["\']og:description["\']\s+content="[^"]*"[^>]*>',
        f'<meta property="og:description" content="{OG_DESC}">',
        html
    )
    return html


def fix_canonical(html: str) -> str:
    """Ensure canonical is clean root URL."""
    html = re.sub(
        r'<link\s+rel=["\']canonical["\']\s+href="[^"]*"[^>]*>',
        '<link rel="canonical" href="https://obaoba.online/">',
        html
    )
    return html


def verify(html: str) -> dict:
    checks = {}
    checks['org_once'] = html.count('"@type":"Organization"') == 1
    checks['website_once'] = html.count('"@type":"WebSite"') == 1
    checks['faqpage_once'] = html.count('"@type":"FAQPage"') == 1
    checks['search_action'] = '"SearchAction"' in html
    checks['same_as'] = '"sameAs"' in html
    checks['no_garbled_desc'] = '甇' not in html and '單' not in html
    checks['no_dup_desc'] = '立即致電LINE預約。，立即致電LINE預約' not in html
    checks['canonical_clean'] = re.search(r'href="https://obaoba\.online/"\s*/?>', html) is not None
    checks['all_near_head'] = (
        html.index('"@type":"Organization"') < html.index('</head>') and
        html.index('"@type":"WebSite"') < html.index('</head>') and
        html.index('"@type":"FAQPage"') < html.index('</head>')
    )
    return checks


def main():
    fpath = ROOT / PAGE
    html = fpath.read_text('utf-8')
    original = html

    html = remove_all_jsonld(html)
    html = fix_meta_description(html)
    html = fix_canonical(html)
    html = inject_before_head_close(html)

    if html != original:
        fpath.write_text(html, 'utf-8')
        print('[OK] index.html updated')
    else:
        print('[--] index.html no change')

    # Verify
    html = fpath.read_text('utf-8')
    v = verify(html)
    print('\n--- Verification ---')
    all_ok = True
    for k, val in v.items():
        all_ok = all_ok and val
        print(('  [OK]' if val else '  [!!]') + ' ' + k)
    if all_ok:
        print('\nAll checks PASSED ✅')
    else:
        print('\nSome checks FAILED ❌')

    # Summary of JSON-LD scripts
    import re as re2
    pattern = re2.compile(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>')
    scripts = list(pattern.finditer(html))
    print(f'\nJSON-LD scripts: {len(scripts)}')
    for s in scripts:
        # Find what @type is in this script
        start = s.end()
        end_match = re2.search(r'</script>', html[start:])
        if end_match:
            content = html[start:start + end_match.start()]
            if '"Organization"' in content:
                print('  - Organization')
            elif '"WebSite"' in content:
                print('  - WebSite')
            elif '"FAQPage"' in content:
                print('  - FAQPage')
            elif '"BreadcrumbList"' in content:
                print('  - BreadcrumbList')
            else:
                print('  - Unknown')

if __name__ == '__main__':
    main()
