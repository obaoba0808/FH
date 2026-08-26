import re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
NEW = [
    ('beginners-checklist.html', '新手必看 12 項檢查清單'),
    ('2026-pricing-table.html', '2026 收費行情表（計算機）'),
    ('private-party-guide.html', '私人派對攻略'),
]
ANCHORS = {
    'beginners-checklist.html': ('first_time_called.html', '第一次叫傳播'),
    '2026-pricing-table.html': ('how_much.html', '透明收費'),
    'private-party-guide.html': ('KTV_party.html', 'KTV派對'),
}

def build_link_b(fname, text):
    return ('<a href="' + fname + '" class="block px-4 py-2.5 hover:bg-white/5 hover:text-[#FF2DAF] transition-colors text-sm">' + text + '</a>')

for fname in ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html']:
    fpath = ROOT + '/' + fname
    c = open(fpath, encoding='utf-8').read()
    orig = c
    added = []
    for new_file, new_text in NEW:
        if new_file == fname:
            continue  # skip self-link
        if new_file in c:
            continue
        anchor_file, anchor_text = ANCHORS[new_file]
        # This page's dropdown is Type B (relative)
        pat = re.compile(r'<a href="' + re.escape(anchor_file) + r'"[^>]*>(.*?)</a>', re.S)
        m = None
        for mm in pat.finditer(c):
            if anchor_text in mm.group(1) or anchor_text in mm.group(0):
                m = mm
                break
        if not m:
            print(f'{fname}: anchor {anchor_file} not found for {new_file}')
            continue
        link = build_link_b(new_file, new_text)
        end = m.end()
        if c[end:end+1] == '\n':
            insert_pos = end + 1
        else:
            insert_pos = end
        c = c[:insert_pos] + link + '\n' + c[insert_pos:]
        added.append(new_file)
    if added:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f'{fname}: added {added}')
    else:
        print(f'{fname}: no changes')
