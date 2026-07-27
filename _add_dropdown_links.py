import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# 4 missing pages with link text
MISSING = [
    ('booking-guide.html',  '預約流程完整攻略！傳播小姐預約步驟詳解'),
    ('legality-guide.html', '傳播妹合法嗎？2026台灣八大行業合法性全解析'),
    ('compare-girls.html',  '傳播妹 vs 酒店小姐超完整比較！7大面向一次看懂'),
    ('business-guide.html', '商務公關推薦攻略！飯局妹和傳播妹的選擇指南'),
]

# Insertion anchors: insert each missing page AFTER the </a> of the anchor page
ANCHORS = ['how_much.html', 'safety_privacy.html', 'special_industries.html', 'tipping-guide-2026.html']

def build_link_html(filename, link_text, domain_prefix):
    """Build a single dropdown link line (inline format, consistent with the codebase)."""
    if domain_prefix:
        href = f'https://obaoba.online/{filename}'
    else:
        href = filename
    return f'''                            <a href="{href}" class="px-4 py-3.5 text-sm text-gray-200 hover:text-white hover:bg-white/10 rounded-xl transition-colors border-b border-white/5 leading-relaxed flex items-start gap-2">
                                <span class="text-neonPink mt-0.5">✦</span> {link_text}
                            </a>'''

def find_dropdown_block(html):
    """Find the <div class="p-2 flex flex-col"> inside the dropdown."""
    marker = '<div class="p-2 flex flex-col">'
    start = html.find(marker)
    if start < 0:
        return None, 0, 0
    # Find the closing </div> — the one that closes this div
    # Count nesting: open parens
    open_count = 0
    i = start + len(marker)
    while i < len(html):
        if html[i:i+5] == '<div ' or html[i:i+4] == '<div>':
            open_count += 1
        elif html[i:i+6] == '</div>':
            if open_count == 0:
                return marker, start, i + 6
            open_count -= 1
        i += 1
    return marker, start, len(html)

def has_link_in_block(block, filename):
    """Check if a link already exists in the dropdown block."""
    return filename in block

def insert_after_anchor(block, anchor_file, new_html):
    """Insert new_html after the </a> of the anchor page link."""
    # Find the anchor link's closing </a>
    # Search for href="(domain?)anchor_file" ... </a>
    # Use a regex that matches both full URL and relative
    pattern = rf'href="(?:https://obaoba\.online/)?{re.escape(anchor_file)}"'
    m = re.search(pattern, block)
    if not m:
        print(f'    [WARN] anchor {anchor_file} not found!')
        return block
    # Find the </a> closing this anchor
    after_href = m.end()
    close = block.find('</a>', after_href)
    if close < 0:
        print(f'    [WARN] </a> not found for {anchor_file}')
        return block
    # Insert new_html after the </a> (add newline)
    return block[:close+5] + '\n' + new_html + '\n' + block[close+5:]

import glob

files = glob.glob('*.html')
files.sort()
print(f'Scanning {len(files)} HTML files...\n')

total_added = 0
total_files_modified = 0

for fname in files:
    html = open(fname, 'r', encoding='utf-8').read()
    
    marker, start, end = find_dropdown_block(html)
    if marker is None:
        continue  # no dropdown in this file
    
    block = html[start:end]
    
    # Detect URL pattern: does the existing dropdown use full URLs?
    has_full_url = 'https://obaoba.online/' in block
    
    modified = False
    for i, (page_file, page_text) in enumerate(MISSING):
        if page_file == fname:
            # Don't link to self
            print(f'{fname}: SKIP {page_file} (self-link)')
            continue
        if has_link_in_block(block, page_file):
            print(f'{fname}: already has {page_file}')
            continue
        
        anchor = ANCHORS[i]
        new_link = build_link_html(page_file, page_text, has_full_url)
        new_block = insert_after_anchor(block, anchor, new_link)
        if new_block == block:
            print(f'{fname}: FAILED to insert {page_file} after {anchor}')
        else:
            block = new_block
            modified = True
            total_added += 1
            print(f'{fname}: + {page_file} (after {anchor})')
    
    if modified:
        new_html = html[:start] + block + html[end:]
        open(fname, 'w', encoding='utf-8').write(new_html)
        total_files_modified += 1

print(f'\nDone. Modified {total_files_modified} files, added {total_added} links.')
