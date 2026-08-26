# _clean_fix.py — UTF-8 source, replacements via bytes/hex to avoid encoding issues
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
LOG = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_clean_fix_log.txt'
today = datetime.date.today().isoformat()

def h(hexstr):
    return bytes.fromhex(hexstr.replace(' ', ''))

def rep(raw, old_h, new_text, label):
    old_b = h(old_h)
    new_b = new_text.encode('utf-8')
    if old_b in raw:
        raw = raw.replace(old_b, new_b, 1)
        return raw, True, 'OK: ' + label
    return raw, False, 'MISS: ' + label

log = []

with open(fp, 'rb') as f:
    raw = f.read()

log.append('File size: %d' % len(raw))

# ==============================================================
# 1. HERO <p> block — find exact bytes, build exact replacement
# ==============================================================
idx_p = raw.find(b'2500-3500')
log.append('2500-3500 at: %d' % idx_p)

# Find <p class="mb-0"> that precedes this
mb0 = raw.rfind(b'<p class="mb-0">', 0, idx_p)
pclose = raw.find(b'</p>', mb0)
old_hero = raw[mb0:pclose+5]
log.append('old_hero (%d bytes): %s' % (len(old_hero), repr(old_hero.decode('utf-8', errors='replace'))))

# Build new hero HTML (ASCII-only hex construction)
new_hero = (
    b'<p class="mb-0">2026'
    b'\xe5\xb9\xb4\xe5\x8f\xb0\xe5\x8c\x97'  # 年台北
    b'\xe5\x82\xb3\xe6\x92\xad'               # 傳播
    b'\xe8\xa1\x8c\xe6\x83\x85'               # 行情
    b'\xe3\x80\x90'                            # 【
    b'\xe5\x9f\xba\xe7\xa4\x8e'               # 基礎
    b'\xe7\xb4\x9a'                            # 級
    b'\xe3\x80\x91'                            # 】
    b' <strong>NT$2,400/2'
    b'\xe5\xb0\x8f\xe6\x99\x82'               # 小時
    b'</strong>'
    b'\xe3\x80\x81'                            # 、
    b'\xe6\xa8\x99\xe6\xba\x96'               # 標準
    b'\xe7\xb4\x9a'                            # 級
    b' <strong>NT$3,600/2'
    b'\xe5\xb0\x8f\xe6\x99\x82'               # 小時
    b'</strong>'
    b'\xe3\x80\x81'                            # 、
    b'<strong>VIP</strong>'
    b' <strong>NT$4,000/2'
    b'\xe5\xb0\x8f\xe6\x99\x82'               # 小時
    b'</strong>'
    b'\xe3\x80\x81'                            # 、
    b'<strong>\xe9\xa0\x82\xe7\xb4\x9a</strong>'  # 頂級
    b' <strong>NT$5,000+/2'
    b'\xe5\xb0\x8f\xe6\x99\x82'               # 小時
    b'</strong>'
    b'\xe3\x80\x82'                            # 。
    b'\xe4\xbd\x8e\xe6\x96\xbc\xe9\x80\x99\xe5\x80\x8b'   # 低於這個
    b'\xe8\xa1\x8c\xe6\x83\x85'               # 行情
    b'\xe5\xa4\xaa\xe5\xa4\x9a'               # 太多
    b'\xe8\xa6\x81\xe5\xb0\x8f\xe5\xbf\x83'   # 要小心
    b'\xe6\x9c\x89\xe9\xac\xbc'               # 有鬼
    b'\xef\xbc\x8c'                            # ，
    b'\xe9\xab\x98\xe6\x96\xbc\xe5\xa4\xaa'   # 高於太
    b'\xe5\xa4\x9a\xe5\x8f\xaf\xe8\x83\xbd'  # 多可能
    b'\xe6\x98\xaf\xe8\xa2\xab'                # 是被
    b'\xe5\xbd\x93\xe7\x9b\x86\xe5\xad\x90'   # 當盤子
    b'\xef\xbc\x81'                            # ！
    b'</p>'
)

log.append('new_hero (%d bytes): %s' % (len(new_hero), repr(new_hero.decode('utf-8', errors='replace'))))

if old_hero == new_hero:
    log.append('Hero: ALREADY UP TO DATE')
else:
    raw = raw.replace(old_hero, new_hero, 1)
    log.append('Hero: REPLACED')

# ==============================================================
# 2. H3 TAGS — find via regex, print them, then replace
# ==============================================================
log.append('\n=== H3 Tags ===')
for m in re.finditer(rb'<h3>[^<]+</h3>', raw):
    tag = m.group().decode('utf-8', errors='replace')
    log.append('Found: ' + tag)

# H3 replacements using confirmed bytes
raw, ok, msg = rep(raw,
    '3c68333e312e20e699aee9809ae7b49aefbc9a323530302d33353030e58583efbc8830e585a5e9996e0e581b9efbc893c2f68333e',
    '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>',
    'H3 普通級')
log.append(msg)

raw, ok, msg = rep(raw,
    '3c68333e322e20e7b2bee981b8e7b49aefbc9a33353030e58583efbc88e5b882e5a0b4e4b8bbe6b581efbc893c2f68333e',
    '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>',
    'H3 精選級')
log.append(msg)

raw, ok, msg = rep(raw,
    '3c68333e332e20564950efbc9a34303030e58583e2f4b08fe6b99f3e3c2f68333e',
    '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>',
    'H3 VIP')
log.append(msg)

# H3 頂級 (was numbered as 3.)
raw, ok, msg = rep(raw,
    '3c68333e332e20e9a196e7b49aefbc9a35303030e58583e4bb8ae4b88aefbc88e5b08ae5b081e4ba86e4ba86e58f97efbc893c2f68333e',
    '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>',
    'H3 頂級')
log.append(msg)

# ==============================================================
# 3. FAQ JSON-LD
# ==============================================================
log.append('\n=== FAQ JSON-LD ===')
pt约 = b'\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\xb4\x84'  # 普通級約
faql_idx = raw.find(pt约)
log.append('普通級約 at: %s' % faql_idx)

if faql_idx > 0:
    # Find the "text": " field that precedes this
    text_start = raw.rfind(b'"text": "', 0, faql_idx + 200)
    if text_start >= 0:
        text_end = raw.find(b'"', text_start + 10)
        old_text_field = raw[text_start:text_end + 1]
        log.append('Old FAQ text: ' + repr(old_text_field.decode('utf-8', errors='replace')))
        new_faq_text = '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'.encode('utf-8')
        raw = raw.replace(old_text_field, new_faq_text, 1)
        log.append('OK: FAQ JSON-LD')
    else:
        log.append('FAQ text field: not found')
else:
    log.append('普通級約: not found')

# ==============================================================
# 4. 飯局妹 FAQ
# ==============================================================
raw, ok, msg = rep(raw,
    '3e33303030e58583e4b8 80e58583efbc88330e58583e4b88aefbc893c2f68333e',  # has space issue
    '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間',
    '飯局妹 FAQ')
# Actually search for the exact bytes
old_bq = b'>3000-10000\xe5\x85\x83</strong>\xe4\xb9\x8b\xe9\x96\x93'
new_bq = '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間'.encode('utf-8')
if old_bq in raw:
    raw = raw.replace(old_bq, new_bq, 1)
    log.append('OK: 飯局妹 FAQ')
else:
    log.append('MISS: 飯局妹 FAQ')

# ==============================================================
# 5. 飯局表 3000-10000
# ==============================================================
old_tq = b'>3000-10000\xe5\x85\x83<'
new_tq = b'>NT$4,000-8,000元<'
if old_tq in raw:
    raw = raw.replace(old_tq, new_tq, 1)
    log.append('OK: 飯局表')
else:
    log.append('MISS: 飯局表')

# ==============================================================
# 6. Paragraph replacements (using bytes search)
# ==============================================================
log.append('\n=== Paragraphs ===')

# Find the <p>普通級段落
p_pt_start = raw.find(b'\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe6\x98\xaf')  # 普通級是
if p_pt_start >= 0:
    p_open = raw.rfind(b'<p>', 0, p_pt_start)
    p_close = raw.find(b'</p>', p_pt_start)
    old_para = raw[p_open:p_close+4]
    log.append('普通級段落: ' + repr(old_para.decode('utf-8', errors='replace')))
    new_para = '<p>基礎公關是很多第一次接觸傳播服務的人的首選</p>'.encode('utf-8')
    raw = raw.replace(old_para, new_para, 1)
    log.append('OK: 段落 普通級是')
else:
    log.append('MISS: 段落 普通級是')

# 普通級的傳播妹
p_pt2 = raw.find(b'\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xe7\x9a\x84\xe5\x82\xb3\xe6\x92\xad\xe5\xa6\xb9')  # 普通級的傳播妹
if p_pt2 >= 0:
    p_open2 = raw.rfind(b'<p>', 0, p_pt2)
    p_close2 = raw.find(b'</p>', p_pt2)
    old_para2 = raw[p_open2:p_close2+4]
    log.append('普通級的段落: ' + repr(old_para2.decode('utf-8', errors='replace')))
    new_para2 = '<p>基礎公關，外型條件中等，但親和力通常不錯</p>'.encode('utf-8')
    raw = raw.replace(old_para2, new_para2, 1)
    log.append('OK: 段落 普通級的')
else:
    log.append('MISS: 段落 普通級的')

# 精選級主流消費區間
p_jx = raw.find(b'\xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xe6\x98\xaf\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad\xe5\xb8\x82\xe5\xa0\xb4\xe7\x9a\x84')  # 精選級是台北傳播市場的
if p_jx >= 0:
    p_open3 = raw.rfind(b'<p>', 0, p_jx)
    p_close3 = raw.find(b'</p>', p_jx)
    old_para3 = raw[p_open3:p_close3+4]
    log.append('精選級段落: ' + repr(old_para3.decode('utf-8', errors='replace')))
    new_para3 = '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：</p>'.encode('utf-8')
    raw = raw.replace(old_para3, new_para3, 1)
    log.append('OK: 段落 精選級主流')
else:
    log.append('MISS: 段落 精選級主流')

# 精選級的傳播小姐
p_jx2 = raw.find(b'\xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xe7\x9a\x84\xe5\x82\xb3\xe6\x92\xad\xe5\xb0\x8f\xe5\xa7\x90')  # 精選級的傳播小姐
if p_jx2 >= 0:
    p_open4 = raw.rfind(b'<p>', 0, p_jx2)
    p_close4 = raw.find(b'</p>', p_jx2)
    old_para4 = raw[p_open4:p_close4+4]
    log.append('精選級小姐段落: ' + repr(old_para4.decode('utf-8', errors='replace')))
    new_para4 = '<p>標準公關服務品質穩定，<strong>適合各種場合</strong>：慶生、公司聚會、朋友聯誼、商務應酬都可以撐場面。如果你不確定要選哪個等級，選標準公關就對了！</p>'.encode('utf-8')
    raw = raw.replace(old_para4, new_para4, 1)
    log.append('OK: 段落 精選級小姐')
else:
    log.append('MISS: 段落 精選級小姐')

# ==============================================================
# 7. dateModified
# ==============================================================
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
log.append('dateModified: %d' % n)

# ==============================================================
# 8. Write back
# ==============================================================
with open(fp, 'wb') as f:
    f.write(raw)
log.append('\nFile written.')

# ==============================================================
# 9. Final counts
# ==============================================================
html = raw.decode('utf-8', errors='replace')
log.append('')
log.append('=== FINAL COUNTS ===')
for p in ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
          '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
          '2500-3500元', '3500-5000元', '5000-8000元']:
    log.append('%s: %d' % (p, html.count(p)))

with open(LOG, 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))

print('Done. Check _clean_fix_log.txt')
