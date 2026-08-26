# -*- coding: utf-8 -*-
# _fix_main.py — Complete pricing update with log file output
import re, datetime, os

PATH = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
LOG = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_main_log.txt'
today = datetime.date.today().isoformat()

log_lines = []

def L(msg):
    log_lines.append(str(msg))

with open(PATH, 'rb') as f:
    raw = f.read()

L('File size: %d bytes' % len(raw))

# ======== STEP 1: Find pricing section ========
idx_price = raw.find(b'2500-3500')
L('2500-3500 at byte: %d' % idx_price)

if idx_price < 0:
    L('ERROR: pricing not found!')
else:
    # Extract region for analysis
    region = raw[max(0, idx_price-700):idx_price+100]
    # Write region to file
    with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_pricing_region.bin', 'wb') as f:
        f.write(region)
    L('Wrote region to _pricing_region.bin (%d bytes)' % len(region))

    # ======== STEP 2: Extract exact old <p class="mb-0"> block ========
    mb0 = raw.rfind(b'<p class="mb-0">', 0, idx_price)
    p_close = raw.find(b'</p>', mb0)
    old_hero = raw[mb0:p_close+5]
    L('old_hero length: %d' % len(old_hero))
    L('old_hero decoded: %s' % repr(old_hero.decode('utf-8', errors='replace')))

    # ======== STEP 3: Build new hero <p> block ========
    new_price_html = (
        '2026年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，'
        '標準級 <strong>NT$3,600/2小時</strong>，'
        '<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，'
        '<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。'
        '低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
    )
    new_hero = b'<p class="mb-0">' + new_price_html.encode('utf-8') + b'</p>'
    L('new_hero decoded: %s' % repr(new_hero.decode('utf-8', errors='replace')))

    # ======== STEP 4: Replace ========
    if old_hero == new_hero:
        L('Hero: ALREADY UP TO DATE')
    else:
        raw = raw.replace(old_hero, new_hero, 1)
        L('Hero: REPLACED (%d -> %d bytes)' % (len(old_hero), len(new_hero)))

    # ======== STEP 5: H3 tags ========
    h3_replacements = [
        (b'<h3>1. \xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xef\xbc\x9a2500-3500\xe5\x85\x83\xef\xbc\x88\xe5\x85\xa5\xe9\x96\x80\xe9\xa6\x96\xe9\x81\xb9\xef\xbc\x89</h3>',
         b'<h3>1. \xe5\x9f\xba\xe7\xa4\x8e\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$2,400/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$1,200/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>',
         'H3 普通級'),
        (b'<h3>2. \xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xef\xbc\x9a3500-5000\xe5\x85\x83\xef\xbc\x88\xe5\xb8\x82\xe5\xa0\xb4\xe4\xb8\xbb\xe6\xb5\x81\xef\xbc\x89</h3>',
         b'<h3>2. \xe6\xa8\x99\xe6\xba\x96\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$3,600/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$1,800/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>',
         'H3 精選級'),
        (b'<h3>3. VIP\xef\xbc\x9a4000-6000\xe5\x85\x83/\xe5\xb0\x8f\xe6\x99\x82</h3>',
         b'<h3>3. VIP \xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$4,000/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$2,000/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>',
         'H3 VIP'),
        (b'<h3>3. \xe9\xa1\x96\xe7\xb4\x9a\xef\xbc\x9a5000-8000\xe5\x85\x83\xe4\xbb\x8a\xe4\xb8\x8a\xef\xbc\x88\xe5\xb0\x8a\xe5\x8b\x81\xe4\xba\xab\xe4\xba\xab\xe5\x8f\x97\xef\xbc\x89</h3>',
         b'<h3>4. \xe9\xa0\x82\xe7\xb4\x9a\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$5,000+/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$2,500+/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>',
         'H3 頂級'),
    ]

    for old_b, new_b, label in h3_replacements:
        if old_b in raw:
            raw = raw.replace(old_b, new_b, 1)
            L('%s: REPLACED' % label)
        else:
            L('%s: NOT FOUND (searching by context)' % label)
            # Search nearby bytes
            search_str = old_b[:20]
            pos = raw.find(search_str)
            if pos >= 0:
                L('  H3 candidate at byte %d: %s' % (pos, repr(raw[pos:pos+len(old_b)].decode('utf-8', errors='replace'))))
            else:
                L('  H3 candidate NOT found at all')

    # ======== STEP 6: FAQ JSON-LD ========
    faq_old = b'"\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad\xe6\x94\xb6\xe8\xb2\xbb\xe8\xa1\x8c\xe6\x83\x85\xef\xbc\x9a\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\xb4\x843500-3500'
    # Search for the actual text
    faq_search = raw.find(b'\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\xb4\x84')  # 普通級約
    if faq_search > 0:
        # Get text around this area
        faq_text_start = raw.rfind(b'"text": "', 0, faq_search)
        if faq_text_start > 0:
            faq_text_end = raw.find(b'"', faq_text_start + 10)
            old_faq_text = raw[faq_text_start:faq_text_end+1]
            L('FAQ text field: %s' % repr(old_faq_text.decode('utf-8', errors='replace')))
            
            new_faq_text = (
                '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'
            ).encode('utf-8')
            raw = raw.replace(old_faq_text, new_faq_text, 1)
            L('FAQ JSON-LD: REPLACED')
        else:
            L('FAQ text field: NOT FOUND')
    else:
        L('普通級約: NOT FOUND in raw')

    # ======== STEP 7: 飯局妹 FAQ ========
    old_banquet = b'>3000-10000\xe5\x85\x83</strong>\xe4\xb9\x8b\xe9\x96\x93'
    new_banquet = b'>NT$4,000-8,000元</strong>之間'
    if old_banquet in raw:
        raw = raw.replace(old_banquet, new_banquet, 1)
        L('飯局妹 FAQ: REPLACED')
    else:
        L('飯局妹 FAQ: NOT FOUND')
        # Find it with context
        pos = raw.find(b'3000-10000')
        if pos > 0:
            L('  Found 3000-10000 at byte %d: %s' % (pos, repr(raw[pos-50:pos+60].decode('utf-8', errors='replace'))))

    # ======== STEP 8: 飯局表 3000-10000 ========
    old_table = b'>3000-10000\xe5\x85\x83<'
    new_table = b'>NT$4,000-8,000元<'
    if old_table in raw:
        raw = raw.replace(old_table, new_table, 1)
        L('飯局表: REPLACED')
    else:
        L('飯局表: NOT FOUND')
        pos = raw.find(b'>3000-10000')
        if pos > 0:
            L('  Found >3000-10000 at byte %d: %s' % (pos, repr(raw[pos-30:pos+40].decode('utf-8', errors='replace'))))

    # ======== STEP 9: Paragraph replacements ========
    # Find paragraphs by searching for 2500-3500 then looking backwards
    para_old1 = b'<p>\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe6\x98\xaf'  # <p>普通級是
    para_new1 = b'<p>\xe5\x9f\xba\xe7\xa4\x8e\xe5\x85\xac\xe9\x97\xb4\xe6\x98\xaf'
    if para_old1 in raw:
        raw = raw.replace(para_old1, para_new1, 1)
        L('段落1: REPLACED')
    else:
        L('段落1: NOT FOUND')

    # <p>普通級的傳播妹
    para_old2 = b'<p>\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\x9a\x84\xe5\x82\xb3\xe6\x92\xad\xe5\xa6\xb9'
    para_new2 = b'<p>\xe5\x9f\xba\xe7\xa4\x8e\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x8c'
    if para_old2 in raw:
        raw = raw.replace(para_old2, para_new2, 1)
        L('段落2: REPLACED')
    else:
        L('段落2: NOT FOUND')

    # 精選級主流
    para_old3 = b'\xe4\xb8\xbb\xe6\xb5\x81\xe6\xb6\x88\xe8\xb2\xbb\xe5\x8d\x80\xe9\x96\x93</strong>\xe3\x80\x82\xe9\x80\x99\xe5\x80\x8b\xe5\x83\xb9\xe4\xbd\x8d\xe7\x9a\x84\xe5\x82\xb3\xe6\x92\xad\xe5\xa6\xb9\xe9\x80\x9a'
    para_new3 = b'\xe4\xb8\xbb\xe6\xb5\x81\xe6\xb6\x88\xe8\xb2\xbb\xe5\x8d\x80\xe9\x96\x93</strong>\xe3\x80\x82\xe9\x80\x99\xe5\x80\x8b\xe5\x83\xb9\xe4\xbd\x8d\xe7\x9a\x84\xe5\x85\xac\xe9\x97\xb4\xe9\x80\x9a'
    if para_old3 in raw:
        raw = raw.replace(para_old3, para_new3, 1)
        L('段落3: REPLACED')
    else:
        L('段落3: NOT FOUND')

    # 精選級傳播小姐
    para_old4 = b'\xe5\x82\xb3\xe6\x92\xad\xe5\xb0\x8f\xe5\xa7\x90\xe6\x9c\x8d\xe5\x8b\x99\xe5\x93\x81\xe8\xb3\xaa\xe7\xa9\xa9\xe5\xae\x9a'
    para_new4 = b'\xe5\x85\xac\xe9\x97\xb4\xe6\x9c\x8d\xe5\x8b\x99\xe5\x93\x81\xe8\xb3\xaa\xe7\xa9\xa9\xe5\xAE\x9a'
    if para_old4 in raw:
        raw = raw.replace(para_old4, para_new4, 1)
        L('段落4: REPLACED')
    else:
        L('段落4: NOT FOUND')

    # ======== STEP 10: dateModified ========
    new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
    raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
    L('dateModified: %d replaced' % n)

    # ======== Write ========
    with open(PATH, 'wb') as f:
        f.write(raw)
    L('File written.')

    # ======== Final verification ========
    html = raw.decode('utf-8', errors='replace')
    L('')
    L('=== FINAL COUNTS ===')
    for p in ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
              '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
              '2500-3500元', '3500-5000元', '5000-8000元']:
        L('%s: %d' % (p, html.count(p)))

# Write log
with open(LOG, 'w', encoding='utf-8') as f:
    f.write('\n'.join(log_lines))
print('DONE - log written')
