import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'

# All 3 new pages to insert
NEW_LINKS = [
    ('<a href="beginners-checklist.html"', '新手必看 12 項檢查清單'),
    ('<a href="2026-pricing-table.html"', '2026 收費行情表（計算機）'),
    ('<a href="private-party-guide.html"', '私人派對攻略'),
]

def get_link(href, text):
    return f'<a href="{href}" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">{text}</a>'

def add_links_to_file(fpath):
    content = open(fpath, encoding='utf-8').read()
    original = content

    # Find the dropdown <div> that contains 、情報特搜站 nav items
    # Look for the closing </div> right before </div></div> at the nav end
    # We'll insert after the last existing <a href=...> in the dropdown

    for new_href, new_text in NEW_LINKS:
        full_link = get_link(new_href, new_text)
        # Skip if already present
        if new_href in content:
            continue
        # Find a good insertion point - after recruitment.html or similar
        markers = [
            ('recruitment.html', '加入我們'),
            ('faq-all-in-one.html', '常見問題'),
            ('about-oppa.html', '關於歐巴'),
            ('news.html', '最新消息'),
        ]
        for marker_href, marker_text in markers:
            pattern = r'(<a href="[^"]*' + re.escape(marker_href) + r'"[^>]*>' + re.escape(marker_text) + r'</a>)'
            m = re.search(pattern, content)
            if m:
                # Insert after this line
                end_pos = m.end()
                # Find the newline after this </a>
                rest = content[end_pos:]
                nl_match = re.match(r'(</a>)(.*)$', rest, re.S)
                if nl_match:
                    insert_after = m.end() + len(nl_match.group(1))
                    content = content[:insert_after] + '\n                    ' + full_link + content[insert_after:]
                    break

    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('UPDATED:', fpath.replace(ROOT, ''))

# Fix the key pages that are missing links
key_pages = ['index.html', 'how_much.html', 'pricing-guide-2026.html',
             'about-oppa.html', 'first_time_called.html', 'motel_safe.html',
             'KTV_party.html', 'faq-all-in-one.html']

for p in key_pages:
    add_links_to_file(ROOT + '/' + p)
