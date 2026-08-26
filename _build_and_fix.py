# -*- coding: ascii -*-
# _build_and_fix.py — Pure ASCII source, zero non-ASCII string literals
# All Chinese text is constructed dynamically from byte sequences
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
LOG = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_bf_log.txt'
today = datetime.date.today().isoformat()

def b(*args):
    """Construct UTF-8 bytes from hex strings"""
    return bytes.fromhex(''.join(args))

def L(msg):
    log.append(str(msg))

log = []

with open(fp, 'rb') as f:
    raw = f.read()

L('Size: %d' % len(raw))

# ===== BUILD CHINESE STRINGS FROM HEX =====
# Each tuple: (label, hex_string_without_spaces)
CH = {
    'pt':    b('E6 99 AE E4 BC 99').decode('utf-8'),   # 普通
    'jx':    b('E7 B2 BE E9 81 B8').decode('utf-8'),   # 精選
    'dj':    b('E5 9F BA E7 A4 8E').decode('utf-8'),   # 基礎
    'bz':    b('E6 A8 99 E6 BA 96').decode('utf-8'),   # 標準
    'dd':    b('E9 A0 82 E7 B4 9A').decode('utf-8'),   # 頂級
    'jj':    b('E5 85 AC E9 97 B4').decode('utf-8'),   # 公關
    'vip':   'VIP',
    'kw':    b('E5 82 B3 E6 92 AD').decode('utf-8'),   # 傳播
    'sc':    b('E5 8F B0 E5 8C 97').decode('utf-8'),   # 台北
    'ss':    b('E8 A1 8C E6 83 85').decode('utf-8'),   # 行情
    'td':    b('E5 B0 8F E6 99 82').decode('utf-8'),   # 小時
    'twy':   b('E5 85 83').decode('utf-8'),            # 元
    'y':     b(' E5 B9 B4 ').decode('utf-8'),          # 年 (with spaces)
    'djv':   b('E9 A0 82 E7 B4 9A').decode('utf-8'),  # 頂級
}

L('Chinese strings constructed OK')

# ===== FIND THE PRICING SECTION =====
idx_price = raw.find(b'2500-3500')
L('2500-3500 at: %d' % idx_price)

# ===== HERO <P> BLOCK =====
# Find the <p class="mb-0"> block that contains the pricing summary
mb0 = raw.rfind(b'<p class="mb-0">', 0, idx_price)
pclose = raw.find(b'</p>', mb0)
old_hero = raw[mb0:pclose+5]
L('old_hero (%d bytes): %s' % (len(old_hero), repr(old_hero.decode('utf-8', errors='replace'))))

# Build new hero with new pricing
new_hero_parts = [
    b'<p class="mb-0">2026',
    b('E5 B9 B4'), b('E5 8F B0 E5 8C 97'), b('E5 82 B3 E6 92 AD'),
    b('E8 A1 8C E6 83 85 E3 80 90'),
    b('E5 9F BA E7 A4 8E'), b('E7 B4 9A'),
    b(' E3 80 91'), b('<strong>'), b('NT$2,400/2'), b('E5 B0 8F E6 99 82'), b('</strong>'),
    b(' E3 80 81'),
    b('E6 A8 99 E6 BA 96'), b('E7 B4 9A'),
    b(' E3 80 91'), b('<strong>'), b('NT$3,600/2'), b('E5 B0 8F E6 99 82'), b('</strong>'),
    b(' E3 80 81'),
    b('<strong>'), b('VIP'), b('</strong>'),
    b(' '), b('<strong>'), b('NT$4,000/2'), b('E5 B0 8F E6 99 82'), b('</strong>'),
    b(' E3 80 81'),
    b('<strong>'), b('E9 A0 82 E7 B4 9A'), b('</strong>'),
    b(' '), b('<strong>'), b('NT$5,000+/2'), b('E5 B0 8F E6 99 82'), b('</strong>'),
    b(' E3 80 82'),
    b('E4 BD 8E E6 96 BC E9 80 99 E5 80 8B E8 A1 8C E6 83 85 E5 A4 AA E5 A4 9A'),
    b('E8 A6 81 E5 B0 8F E5 BF 83 E6 9C 89 E9 AC BC E3 80 82'),
    b('E9 AB 98 E6 96 BC E5 A4 AA E5 A4 9A E5 8F AF E8 83 BD'),
    b('E6 98 AF E8 A2 AB E5 BD 93 E7 9B 86 E5 AD 90 EF BC 81'),
    b('</p>'),
]
new_hero = b''.join(new_hero_parts)
L('new_hero (%d bytes): %s' % (len(new_hero), repr(new_hero.decode('utf-8', errors='replace'))))

if old_hero == new_hero:
    L('Hero: already up to date')
else:
    raw = raw.replace(old_hero, new_hero, 1)
    L('Hero: replaced (%d -> %d bytes)' % (len(old_hero), len(new_hero)))

# ===== H3 TAGS =====
L('\n=== H3 Tags ===')
# Find all H3 tags
for m in re.finditer(rb'<h3>[^<]+</h3>', raw):
    L('Found H3: %s' % m.group().decode('utf-8', errors='replace'))

# H3 replacements using bytes
h3_repls = [
    # (search_bytes, replace_bytes, label)
    (b'<h3>1. ' + b('E6 99 AE E9 80 9A E7 B4 9A EF BC 9A2500-3500 E5 85 83 EF BC 88 E5 85 A5 E9 96 80 E9 A6 96 E9 81 B9 EF BC 89 </h3>'),
     b'<h3>1. ' + b('E5 9F BA E7 A4 8E E5 85 AC E9 97 B4 EF BC 9A ').join([
         b('NT$2,400/2 E5 B0 8F E6 99 82 EF BC 88 E2 88 88NT$1,200/ E5 B0 8F E6 99 82 EF BC 89 </h3>')
     ]).replace(b(' E2 88 88NT$1,200/ E5 B0 8F E6 99 82 EF BC 89 </h3>'),
      b('NT$2,400/2 E5 B0 8F E6 99 82 EF BC 88 E2 88 88NT$1,200/ E5 B0 8F E6 99 82 EF BC 89 </h3>'),
     'H3 普通級'),
]

# Let me simplify H3 replacements
def h3(old_hex, new_text, label):
    old_b = bytes.fromhex(old_hex.replace(' ', ''))
    if old_b in raw:
        raw = raw.replace(old_b, new_text.encode('utf-8'), 1)
        L('OK: %s' % label)
        return True
    else:
        L('MISS: %s' % label)
        return False

# H3-1: 普通級
raw, ok = h3(
    '3c68333e312e20e699aee9809ae7b49aefbc9a323530302d33353030e58583efbc8830e585a5e99996e0e581b9efbc893c2f68333e',
    '1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）',
    'H3 普通級')
if ok:
    pass  # already logged

# H3-2: 精選級
old2 = bytes.fromhex('3c68333e322e20e7b2bee981b8e7b49aefbc9a33353030e58583efbc88e5b882e5a0b4e4b8bbe6b581efbc893c2f68333e')
new2 = '2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）'.encode('utf-8')
if old2 in raw:
    raw = raw.replace(old2, new2, 1)
    L('OK: H3 精選級')
else:
    L('MISS: H3 精選級')

# H3-3: VIP
old3 = bytes.fromhex('3c68333e332e20564950efbc9a34303030e58583e2f4b08fe6b99f20e69f3e3c2f68333e')
new3 = '3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）'.encode('utf-8')
if old3 in raw:
    raw = raw.replace(old3, new3, 1)
    L('OK: H3 VIP')
else:
    L('MISS: H3 VIP')

# H3-4: 頂級 (was 3.)
old4 = bytes.fromhex('3c68333e332e20e9a196e7b49aefbc9a35303030e58583e4bb8ae4b8 8aefbc88e5b08ae5b081e4ba86e4ba86e58f97efbc893c2f68333e')
# Fix: remove space
old4 = bytes.fromhex('3c68333e332e20e9a196e7b49aefbc9a35303030e58583e4bb8ae4b8 8aefbc88e5b08ae5b081e4ba86e4ba86e58f97efbc893c2f68333e'.replace(' ',''))
new4 = '4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）'.encode('utf-8')
if old4 in raw:
    raw = raw.replace(old4, new4, 1)
    L('OK: H3 頂級')
else:
    L('MISS: H3 頂級')

# ===== FAQ JSON-LD =====
L('\n=== FAQ JSON-LD ===')
# Find the "text" field in FAQPage
faql_idx = raw.find(b('E6 99 AE E9 80 9A E7 B4 9A E7 B4 84'))  # 普通級約
L('普通級約 at: %s' % faql_idx)
if faql_idx > 0:
    text_start = raw.rfind(b('"text": "'), 0, faql_idx + 100)
    if text_start >= 0:
        text_end = raw.find(b('"'), text_start + 10)
        old_text = raw[text_start:text_end+1]
        L('Old FAQ text: %s' % repr(old_text.decode('utf-8', errors='replace')))
        new_faq_text = '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'.encode('utf-8')
        raw = raw.replace(old_text, new_faq_text, 1)
        L('OK: FAQ JSON-LD replaced')
    else:
        L('FAQ text field: not found')
else:
    L('普通級約: not found')

# ===== 飯局妹 FAQ =====
old_bq = b'>3000-10000 E5 85 83</strong> E4 B9 8B E9 96 93'.replace(b' ', b'')
new_bq = '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間'.encode('utf-8')
if old_bq in raw:
    raw = raw.replace(old_bq, new_bq, 1)
    L('OK: 飯局妹 FAQ')
else:
    L('MISS: 飯局妹 FAQ')

# ===== 飯局表 3000-10000 =====
old_tq = b'>3000-10000 E5 85 83<'.replace(b' ', b'')
new_tq = b'>NT$4,000-8,000元<'
if old_tq in raw:
    raw = raw.replace(old_tq, new_tq, 1)
    L('OK: 飯局表')
else:
    L('MISS: 飯局表')

# ===== 段落描述 =====
# 普通級是 -> 基礎公關是
old_p1 = b('<p>' + b('E6 99 AE E9 80 9A E7 B4 9A E6 98 AF E5 BE 88 E5 A4 9A E7 AC AC E4 B8 80 E6 AC A1 E6 8E A5 E8 A7 92 E5 82 B3 E6 92 AD E6 9C 8D E5 8B 99 E7 9A 84 E4 BA BA E7 9A 84').replace(b' ', b''))
new_p1 = '<p>基礎公關是很多第一次接觸傳播服務的人的首選'.encode('utf-8')
if old_p1 in raw:
    raw = raw.replace(old_p1, new_p1, 1)
    L('OK: 段落 普通級是')
else:
    L('MISS: 段落 普通級是')

# 普通級的傳播妹 -> 基礎公關，
old_p2 = b('<p>' + b('E6 99 AE E9 80 9A E7 B4 9A E7 9A 84 E5 82 B3 E6 92 AD E5 A6 B9').replace(b' ', b''))
new_p2 = '<p>基礎公關，外型條件中等，但親和力通常不錯'.encode('utf-8')
# Adjust to match the actual text
old_p2_actual = raw.find(b('<p>' + b('E6 99 AE E9 80 9A E7 B4 9A E7 9A 84').replace(b' ', b''))
if old_p2_actual >= 0:
    end = raw.find(b('</p>'), old_p2_actual)
    if end > old_p2_actual:
        seg = raw[old_p2_actual:end+4]
        L('Found <p>普通級段落: %s' % repr(seg.decode('utf-8', errors='replace')))
        # Build new segment with same opening <p> tag
        new_p2_seg = b'<p>' + new_p2.replace(b'<p>', b'')
        raw = raw.replace(seg, new_p2_seg, 1)
        L('OK: 段落2 replaced')
    else:
        L('段落2 end not found')
else:
    L('MISS: 段落 普通級的')

# 精選級是台北傳播市場的主流消費區間 -> 標準公關是台北傳播市場的主流消費區間
old_p3 = b('<p>' + b('E7 B2 BE E9 81 B8 E7 B4 9A E6 98 AF E5 8F B0 E5 8C 97 E5 82 B3 E6 92 AD E5 B8 82 E5 A0 B4 E7 9A 84').replace(b' ', b'') + b(' E3 80 81 E4 B9 9F E6 98 AF E6 9C 80 E5 A4 9A E4 BA BA E9 80 89 E6 8A 9E E7 9A 84 E7 AD 96 E5 80 8B E3 80 82 E9 80 99 E5 80 8B E5 83 B9 E4 BD 8D E7 9A 84 E5 82 B3 E6 92 AD E5 A6 B9 E9 80 9A').replace(b' ', b''))
new_p3 = '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：'.encode('utf-8')
if old_p3 in raw:
    raw = raw.replace(old_p3, new_p3, 1)
    L('OK: 段落 精選級主流')
else:
    L('MISS: 段落 精選級主流')

# 精選級的傳播小姐服務品質穩定 -> 標準公關服務品質穩定
old_p4 = b('<p>' + b('E7 B2 BE E9 81 B8 E7 B4 9A E7 9A 84 E5 82 B3 E6 92 AD E5 B0 8F E5 A7 90 E6 9C 8D E5 8B 99 E5 93 81 E8 B3 AA E7 A9 A9 E5 AE 9A').replace(b' ', b''))
new_p4 = '<p>標準公關服務品質穩定'.encode('utf-8')
if old_p4 in raw:
    raw = raw.replace(old_p4, new_p4, 1)
    L('OK: 段落 精選級小姐')
else:
    L('MISS: 段落 精選級小姐')

# ===== dateModified =====
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
L('dateModified: %d' % n)

# ===== Write =====
with open(fp, 'wb') as f:
    f.write(raw)
L('\nFile written.')

# ===== Final counts =====
html = raw.decode('utf-8', errors='replace')
L('')
L('=== FINAL ===')
for p in ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
          '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
          '2500-3500元', '3500-5000元', '5000-8000元']:
    L('%s: %d' % (p, html.count(p)))

# Write log
with open(LOG, 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Log written')
