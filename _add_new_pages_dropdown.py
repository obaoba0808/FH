import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'

# (new link, after_this_link_text)
INSERTIONS = [
    ('beginners-checklist.html', '第一次叫傳播'),
    ('2026-pricing-table.html', '2026價格行情表'),
    ('private-party-guide.html', '商務飯局'),
]

# Type A: full URLs, Type B: relative paths
# We'll try both and see which matches

html_files = [f for f in glob.glob(ROOT + '/*.html') 
               if 'google' not in f and 'beginners' not in f 
               and '2026-pricing-table' not in f and 'private-party' not in f]

updated = 0
skipped = 0

for fpath in sorted(html_files):
    fname = fpath.replace(ROOT+'\\','')
    content = open(fpath, encoding='utf-8').read()
    original = content
    any_change = False

    for new_page, anchor_text in INSERTIONS:
        # Find the dropdown block (contains  情報特搜站)
        # Look for the specific anchor by text
        patterns = [
            f'<a href="https://obaoba.online/{new_page}"',
            f'<a href="{new_page}"',
        ]
        if any(p in content for p in patterns):
            continue  # already present

        # Find the anchor that contains the marker text
        # Match <a href="..." ...>marker_text</a>
        escaped = re.escape(anchor_text)
        # Try full URL pattern first
        for marker_href in [
            f'https://obaoba.online/first_time_called.html',
            f'https://obaoba.online/pricing-guide-2026.html',
            f'https://obaoba.online/business_dinner.html',
        ]:
            marker_text_map = {
                'https://obaoba.online/first_time_called.html': '第一次叫傳播',
                'https://obaoba.online/pricing-guide-2026.html': '2026價格行情表',
                'https://obaoba.online/business_dinner.html': '商務飯局',
            }
            m_text = marker_text_map.get(marker_href, '')
            # Build regex to find the full <a ...>text</a> block
            pattern = r'(<a href="' + re.escape(marker_href) + r'"[^>]*>[^<]*' + re.escape(m_text) + r'[^<]*</a>)'
            m = re.search(pattern, content)
            if m:
                full_anchor = m.group(1)
                new_link_a = f'<a href="https://obaoba.online/{new_page}" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">{"新手必看 12 項檢查清單" if "beginners" in new_page else ("2026 收費行情表（計算機）" if "2026-pricing" in new_page else "私人派對攻略")}</a>'
                new_link_b = f'<a href="{new_page}" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">{"新手必看 12 項檢查清單" if "beginners" in new_page else ("2026 收費行情表（計算機）" if "2026-pricing" in new_page else "私人派對攻略")}</a>'
                # Try Type A
                if f'href="https://obaoba.online/{marker_href.split("/")[-1]}"' in content:
                    replacement = full_anchor + '\n                    ' + new_link_a
                else:
                    replacement = full_anchor + '\n                    ' + new_link_b
                content = content[:m.start()] + replacement + content[m.end():]
                any_change = True
                break

        if not any_change:
            # Try relative path
            rel_map = {
                'beginners': 'first_time_called.html',
                '2026-pricing-table': 'pricing-guide-2026.html',
                'private-party': 'business_dinner.html',
            }
            for k, v in rel_map.items():
                if k in new_page:
                    pattern = r'(<a href="' + re.escape(v) + r'"[^>]*>[^<]*</a>)'
                    m = re.search(pattern, content)
                    if m:
                        full_anchor = m.group(1)
                        link_text = {"beginners": "新手必看 12 項檢查清單", "2026-pricing-table": "2026 收費行情表（計算機）", "private-party": "私人派對攻略"}[k]
                        replacement = full_anchor + '\n                    ' + f'<a href="{new_page}" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">{link_text}</a>'
                        content = content[:m.start()] + replacement + content[m.end():]
                        any_change = True
                    break

    if any_change:
        with open(fpath, 'w', encoding='utf-8') as out:
            out.write(content)
        print(f'UPDATE: {fname}')
        updated += 1
    else:
        print(f'SKIP:   {fname}')
        skipped += 1

print(f'\nDone: {updated} updated, {skipped} skipped, {updated+skipped} total')
