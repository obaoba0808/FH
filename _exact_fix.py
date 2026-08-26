# -*- coding: utf-8 -*-
# _exact_fix.py — Read exact bytes from file around pricing section
# Then build replacement from those exact bytes
import re, datetime

PATH = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
today = datetime.date.today().isoformat()

with open(PATH, 'rb') as f:
    raw = f.read()

# Find the pricing section by searching for '2500-3500' bytes
idx_pricing = raw.find(b'2500-3500')
log = []
log.append(f'File size: {len(raw)}')
log.append(f'2500-3500 at byte: {idx_pricing}')

if idx_pricing < 0:
    log.append('ERROR: 2500-3500 not found!')
else:
    # Get 500 bytes around pricing section (before it, to capture the <p> tag)
    start = max(0, idx_pricing - 600)
    end = min(len(raw), idx_pricing + 300)
    section = raw[start:end]
    log.append(f'Section (byte {start} to {end}):')
    log.append(f'Hex: {section.hex(" ")}')
    
    # Read 1000 bytes from start of section for analysis
    with open('_pricing_section.bin', 'wb') as f:
        f.write(section)
    log.append(f'Wrote {len(section)} bytes to _pricing_section.bin')

    # ===== BUILD EXACT OLD/NEW =====

    # The exact old <p class="mb-0"> block
    # We know: the block starts with <p class="mb-0"> and contains 2500-3500/3500-5000/5000-8000
    # Let's find the exact start by searching backwards from idx_pricing
    mb0_pos = raw.rfind(b'<p class="mb-0">', 0, idx_pricing)
    log.append(f'<p class="mb-0"> at byte: {mb0_pos}')
    
    # Find the </p> after that
    p_end_pos = raw.find(b'</p>', mb0_pos)
    log.append(f'</p> at byte: {p_end_pos}')
    
    old_hero_p = raw[mb0_pos:p_end_pos + 5]  # include </p>
    log.append(f'old_hero_p length: {len(old_hero_p)}')
    log.append(f'old_hero_p hex: {old_hero_p.hex(" ")}')
    log.append(f'old_hero_p decoded: {old_hero_p.decode("utf-8", errors="replace")}')

    # Build new hero <p> block — same structure, new prices
    # The new content
    new_price_text = (
        '2026年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，'
        '標準級 <strong>NT$3,600/2小時</strong>，'
        '<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，'
        '<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。'
        '低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
    )
    new_hero_p = b'<p class="mb-0">' + new_price_text.encode('utf-8') + b'</p>'
    log.append(f'new_hero_p decoded: {new_hero_p.decode("utf-8", errors="replace")}')

    # Replace
    if old_hero_p == new_hero_p:
        log.append('Hero already up to date')
    else:
        raw = raw.replace(old_hero_p, new_hero_p, 1)
        log.append(f'Replaced hero <p> ({len(old_hero_p)} -> {len(new_hero_p)})')

    # ===== H3 TAGS =====
    # Find H3 tags in the file
    h3_pattern = rb'<h3>[^<]+</h3>'
    for m in re.finditer(h3_pattern, raw):
        tag = m.group()
        log.append(f'H3: {tag.decode("utf-8", errors="replace")}')

    # Specific H3 replacements using exact bytes
    replacements = [
        # (old_bytes, new_text, label)
        (b'<h3>1. \xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xef\xbc\x9a2500-3500\xe5\x85\x83\xef\xbc\x88\xe5\x85\xa5\xe9\x96\x80\xe9\xa6\x96\xe9\x81\xb9\xef\xbc\x89</h3>',
         '1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）', 'H3 普通級'),
        (b'<h3>2. \xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xef\xbc\x9a3500-5000\xe5\x85\x83\xef\xbc\x88\xe5\xb8\x82\xe5\xa0\xb4\xe4\xb8\xbb\xe6\xb5\x81\xef\xbc\x89</h3>',
         '2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）', 'H3 精選級'),
        (b'<h3>3. VIP\xef\xbc\x9a4000-6000\xe5\x85\x83/\xe5\xb0\x8f\xe6\x99\x82</h3>',
         '3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）', 'H3 VIP'),
        (b'<h3>3. \xe9\xa1\x96\xe7\xb4\x9a\xef\xbc\x9a5000-8000\xe5\x85\x83\xe4\xbb\x8a\xe4\xb8\x8a\xef\xbc\x88\xe5\xb0\x8a\xe5\x8b\x81\xe4\xba\xab\xe4\xba\xab\xe5\x8f\x97\xef\xbc\x89</h3>',
         '4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）', 'H3 頂級'),
    ]

    for old_b, new_text, label in replacements:
        if old_b in raw:
            new_b = ('<h3>' + new_text + '</h3>').encode('utf-8')
            raw = raw.replace(old_b, new_b, 1)
            log.append(f'OK: {label}')
        else:
            log.append(f'MISS: {label}')

    # FAQ JSON-LD (search for the "普通級約" pattern in bytes)
    pt约 = '約'.encode('utf-8')  # \xe7\xb4\x84
    # Search for 2500-3500\xe5\x85\x83 in the FAQ JSON-LD section
    faql_idx = raw.find(b'\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\xb4\x84')  # 普通級約
    if faql_idx > 0:
        # Get surrounding context
        faql_ctx = raw[max(0,faql_idx-50):faql_idx+200]
        log.append(f'FAQ JSON-LD region hex: {faql_ctx.hex(" ")}')
        # Try to find exact old FAQ JSON-LD bytes
        old_faq_b = raw[faql_idx-30:faql_idx+250]
        log.append(f'FAQ region decoded: {old_faq_b.decode("utf-8", errors="replace")}')
        # Build new FAQ text
        new_faq_text = ('2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、'
                        'VIP NT$4,000、頂級 NT$5,000以上/2小時。'
                        '加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。'
                        '實際依等級、地點而異。')
        new_faq_b = ('"text": "' + new_faq_text + '"').encode('utf-8')
        old_faq_search = raw.find(b'"text": "\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad')
        if old_faq_search >= 0:
            # Find the end of this "text" field
            end_search = raw.find(b'"', old_faq_search + 10)
            if end_search > old_faq_search:
                old_text_field = raw[old_faq_search:end_search+1]
                log.append(f'Old FAQ text field: {old_text_field.decode("utf-8", errors="replace")}')
                raw = raw.replace(old_text_field, new_faq_b, 1)
                log.append('OK: FAQ JSON-LD')
    else:
        log.append('普通級約 not found in raw bytes')

    # 飯局妹 FAQ
    old_banquet = b'>\xe9\xa3\xaf\xe5\xb1\x80\xe5\xa6\xb9\xe7\x9a\x84\xe6\x94\xb6\xe8\xb2\xbb\xe8\xa1\x8c\xe6\x83\x85\xe5\xa4\xaa\xe7\xb0\x84\xe5\x9c\xa8<strong>3000-10000\xe5\x85\x83</strong>\xe4\xb9\x8b\xe9\x96\x93'
    new_banquet = b'>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間'
    if old_banquet in raw:
        raw = raw.replace(old_banquet, new_banquet, 1)
        log.append('OK: 飯局妹 FAQ')
    else:
        log.append('MISS: 飯局妹 FAQ')

    # 飯局表 3000-10000
    old_table = b'>3000-10000\xe5\x85\x83<'
    new_table = b'>NT$4,000-8,000元<'
    if old_table in raw:
        raw = raw.replace(old_table, new_table, 1)
        log.append('OK: 飯局表 3000-10000')
    else:
        log.append('MISS: 飯局表 3000-10000')

    # Paragraph replacements (普通級/精選級 in body text)
    para_replacements = [
        (b'<p>\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe6\x98\xaf\xe5\xbe\x88\xe5\xa4\x9a\xe7\xac\xac\xe4\xb8\x80\xe6\xac\xa1\xe6\x8e\xa5\xe8\xa7\x92\xe5\x82\xb3\xe6\x92\xad\xe6\x9c\x8d\xe5\x8b\x99\xe7\x9a\x84\xe4\xba\xba\xe7\x9a\x84\xe9\x80\x89',
         b'<p>\xe5\x9f\xba\xe7\xa4\x8e\xe5\x85\xac\xe9\x97\xb4\xe6\x98\xaf\xe5\xbe\x88\xe5\xa4\x9a\xe7\xac\xac\xe4\xb8\x80\xe6\xac\xa1\xe6\x8e\xa5\xe8\xa7\x92\xe5\x82\xb3\xe6\x92\xad\xe6\x9c\x8d\xe5\x8b\x99\xe7\x9a\x84\xe4\xba\xba\xe7\x9a\x84\xe9\x80\x89'),
        (b'<p>\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\x9a\x84\xe5\x82\xb3\xe6\x92\xad\xe5\xa6\xb9\xef\xbc\x8c\xe5\xa4\x96\xe5\x9e\x8b\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xb8\xad\xe7\xad\x89\xef\xbc\x8c\xe4\xbd\x86\xe8\xa6\xaa\xe5\x92\x8c\xe5\x8a\x9b\xe9\x80\x9a\xe5\xb8\xb8\xe4\xb8\x8d\xe9\x8c\xaf',
         b'<p>\xe5\x9f\xba\xe7\xa4\x8e\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x8c\xe5\xa4\x96\xe5\x9e\x8b\xe6\x9d\xa1\xe4\xbb\xb6\xe4\xb8\xad\xe7\xad\x89\xef\xbc\x8c\xe4\xbd\x86\xe8\xa6\xaa\xe5\x92\x8c\xe5\x8a\x9b\xe9\x80\x9a\xe5\xb8\xb8\xe4\xb8\x8d\xe9\x8c\xaf'),
        (b'<p>\xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xe6\x98\xaf\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad\xe5\xb8\x82\xe5\xa0\xb4\xe7\x9a\x84<strong>\xe4\xb8\xbb\xe6\xb5\x81\xe6\xb6\x88\xe8\xb2\xbb\xe5\x8d\x80\xe9\x96\x93</strong>',
         b'<p>\xe6\xa8\x99\xe6\xba\x96\xe5\x85\xac\xe9\x97\xb4\xe6\x98\xaf\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad\xe5\xb8\x82\xe5\xa0\xb4\xe7\x9a\x84<strong>\xe4\xb8\xbb\xe6\xb5\x81\xe6\xb6\x88\xe8\xb2\xbb\xe5\x8d\x80\xe9\x96\x93</strong>'),
        (b'<p>\xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xe7\x9a\x84\xe5\x82\xb3\xe6\x92\xad\xe5\xb0\x8f\xe5\xa7\x90\xe6\x9c\x8d\xe5\x8b\x99\xe5\x93\x81\xe8\xb3\xaa\xe7\xa9\xa9\xe5\xae\x9a',
         b'<p>\xe6\xa8\x99\xe6\xba\x96\xe5\x85\xac\xe9\x97\xb4\xe6\x9c\x8d\xe5\x8b\x99\xe5\x93\x81\xe8\xb3\xaa\xe7%A9%A9\xe5\xAE\x9A'),
    ]

    for old_b, new_b in para_replacements:
        if old_b in raw:
            raw = raw.replace(old_b, new_b, 1)
            log.append(f'OK: paragraph replacement ({len(old_b)} -> {len(new_b)})')
        else:
            log.append(f'MISS: paragraph ({old_b[:30].hex()})')

    # dateModified
    new_dm = f'"dateModified": "{today}"'.encode('utf-8')
    raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
    log.append(f'dateModified: {n} replaced')

    # Write back
    with open(PATH, 'wb') as f:
        f.write(raw)
    log.append('File written.')

    # Final verification
    html = raw.decode('utf-8', errors='replace')
    log.append('')
    log.append('=== FINAL COUNTS ===')
    for p in ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
              '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
              '2500-3500元', '3500-5000元', '5000-8000元']:
        log.append(f'{p}: {html.count(p)}')

# Write log
with open('_exact_fix_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Log written to _exact_fix_log.txt')
