import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'

# Pages + which links they need
NEEDS = {
    'index.html':          ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html'],
    'how_much.html':      ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html'],
    'pricing-guide-2026.html': ['beginners-checklist.html', 'private-party-guide.html'],
    'about-oppa.html':    ['beginners-checklist.html', '2026-pricing-table.html'],
    'first_time_called.html': ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html'],
    'motel_safe.html':    ['beginners-checklist.html', 'private-party-guide.html'],
    'KTV_party.html':     ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html'],
    'faq-all-in-one.html': ['beginners-checklist.html', 'private-party-guide.html'],
    'business_dinner.html': ['2026-pricing-table.html', 'private-party-guide.html'],
}

LINK_TEXT = {
    'beginners-checklist.html': '新手必看 12 項檢查清單',
    '2026-pricing-table.html': '2026 收費行情表（計算機）',
    'private-party-guide.html': '私人派對攻略',
}

for fname, needed in sorted(NEEDS.items()):
    fpath = ROOT + '/' + fname
    content = open(fpath, encoding='utf-8').read()
    original = content
    inserted = []

    for new_page in needed:
        # Skip if already present
        if new_page in content:
            continue
        link_html = f'<a href="{new_page}" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">{LINK_TEXT[new_page]}</a>'
        # Insert before </div>\n                </div>\n            </div>\n        </div>
        # Pattern: find the closing of the dropdown div (before the nav links at bottom)
        # Best anchor: before <a href="about-oppa.html" or before <a href="news.html"
        for anchor in ['about-oppa.html', 'news.html']:
            pattern = r'(\n\s*<a href="[^"]*' + re.escape(anchor) + r'"[^>]*>[^<]*</a>\n\s*</div>\n\s*</div>)'
            m = re.search(pattern, content)
            if m:
                content = content[:m.start()] + '\n                    ' + link_html + m.group(1) + content[m.end():]
                inserted.append(new_page)
                break

    if inserted:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'UPDATED {fname}: added {inserted}')
    else:
        print(f'SKIP   {fname}: no changes needed')
