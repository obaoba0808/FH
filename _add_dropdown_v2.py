import glob, re, sys

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'

# New pages to add to dropdown: (filename, display text)
NEW = [
    ('beginners-checklist.html', '新手必看 12 項檢查清單'),
    ('2026-pricing-table.html', '2026 收費行情表（計算機）'),
    ('private-party-guide.html', '私人派對攻略'),
]

# Insertion anchors: existing page + display text (partial match), insert AFTER it
# All anchors must exist in ALL dropdowns (verified: how_much/KTV_party/motel_safe/first_time_called/business-guide/recruitment = 32/32)
ANCHORS = {
    'beginners-checklist.html': ('first_time_called.html', '第一次叫傳播'),
    '2026-pricing-table.html': ('how_much.html', '透明收費'),
    'private-party-guide.html': ('KTV_party.html', 'KTV派對'),
}

def build_link_a(fname, text):
    # Type A: full URL
    return ('                            <a href="https://obaoba.online/' + fname + '" class="px-4 py-3.5 text-sm text-gray-200 hover:text-white hover:bg-white/10 rounded-xl transition-colors border-b border-white/5 leading-relaxed flex items-start gap-2">\n'
            '                                <span class="text-neonPink mt-0.5">\u2726</span> ' + text + '\n'
            '                            </a>')

def build_link_b(fname, text):
    # Type B: relative path (new style pages)
    return ('<a href="' + fname + '" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">' + text + '</a>')

def find_anchor_block(content, anchor_file, anchor_text):
    """Find the full <a ...>...</a> block for the anchor page (Type A or B)."""
    # Type A: full URL
    for url in [f'https://obaoba.online/{anchor_file}', anchor_file]:
        pat = re.compile(r'<a href="' + re.escape(url) + r'"[^>]*>(.*?)</a>', re.S)
        for m in pat.finditer(content):
            block = m.group(0)
            if anchor_text in m.group(1) or anchor_text in block:
                return m
    return None

updated = []
for fpath in sorted(glob.glob(ROOT + '/*.html')):
    fname = fpath.replace(ROOT + '\\', '')
    if 'google' in fname or fname in [n for n, _ in NEW]:
        continue
    content = open(fpath, encoding='utf-8').read()
    orig = content
    added = []

    for new_file, new_text in NEW:
        if new_file in content:
            continue  # already present
        anchor_file, anchor_text = ANCHORS[new_file]
        m = find_anchor_block(content, anchor_file, anchor_text)
        if not m:
            continue
        # Determine format: Type A if the anchor uses full URL
        is_type_a = ('https://obaoba.online/' + anchor_file) in m.group(0)
        link = build_link_a(new_file, new_text) if is_type_a else build_link_b(new_file, new_text)
        # Insert after anchor block, preserving newline structure
        end = m.end()
        if content[end:end+1] == '\n':
            insert_pos = end + 1
        else:
            insert_pos = end
        content = content[:insert_pos] + link + '\n' + content[insert_pos:]
        added.append(new_file)

    if added:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        updated.append((fname, added))

for fname, added in updated:
    print(f'UPDATED {fname}: {added}')
print(f'\nTotal updated: {len(updated)} / {len(glob.glob(ROOT + "/*.html")) - 1} pages')
