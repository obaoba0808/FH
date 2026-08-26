# -*- coding: utf-8 -*-
# _fix_final2.py — Clean bytes replacement using str.encode()
import re, datetime

PATH = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
LOG = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_final2_log.txt'
today = datetime.date.today().isoformat()

log = []

def L(msg):
    log.append(str(msg))

with open(PATH, 'rb') as f:
    raw = f.read()

L('File size: %d' % len(raw))

# Helper: replace bytes by string patterns
def rep_bytes(raw, old_str, new_str, label):
    old_b = old_str.encode('utf-8')
    new_b = new_str.encode('utf-8')
    if old_b in raw:
        raw = raw.replace(old_b, new_b, 1)
        L('OK: %s' % label)
        return raw, True
    else:
        L('MISS: %s' % label)
        return raw, False

# ===== REPLACEMENTS =====
changes = 0

# 1. Hero <p> block
raw, ok = rep_bytes(raw,
    '<p class="mb-0">2026年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！</p>',
    '<p class="mb-0">2026年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！</p>',
    'Hero <p>行情摘要')
if ok: changes += 1

# 2. H3 普通級
raw, ok = rep_bytes(raw,
    '<h3>1. 普通級：2500-3500元（入門首選）</h3>',
    '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>',
    'H3 普通級')
if ok: changes += 1

# 3. H3 精選級
raw, ok = rep_bytes(raw,
    '<h3>2. 精選級：3500-5000元（市場主流）</h3>',
    '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>',
    'H3 精選級')
if ok: changes += 1

# 4. H3 VIP
raw, ok = rep_bytes(raw,
    '<h3>3. VIP：4000-6000元/小時</h3>',
    '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>',
    'H3 VIP')
if ok: changes += 1

# 5. H3 頂級
raw, ok = rep_bytes(raw,
    '<h3>3. 頂級：5000-8000元以上（尊榮享受）</h3>',
    '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>',
    'H3 頂級')
if ok: changes += 1

# 6. FAQ JSON-LD
raw, ok = rep_bytes(raw,
    '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"',
    '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"',
    'FAQ JSON-LD')
if ok: changes += 1

# 7. 飯局妹 FAQ
raw, ok = rep_bytes(raw,
    '>飯局妹的收費行情大概在<strong>3000-10000元</strong>之間',
    '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間',
    '飯局妹 FAQ')
if ok: changes += 1

# 8. 飯局表 3000-10000
raw, ok = rep_bytes(raw,
    '>3000-10000元<',
    '>NT$4,000-8,000元<',
    '飯局表 3000-10000')
if ok: changes += 1

# 9. 普通級段落描述1
raw, ok = rep_bytes(raw,
    '<p>普通級是很多第一次接觸傳播服務的人的首選',
    '<p>基礎公關是很多第一次接觸傳播服務的人的首選',
    '普通級 段落1')
if ok: changes += 1

# 10. 普通級段落描述2
raw, ok = rep_bytes(raw,
    '<p>普通級的傳播妹，外型條件中等，但親和力通常不錯',
    '<p>基礎公關，外型條件中等，但親和力通常不錯',
    '普通級 段落2')
if ok: changes += 1

# 11. 精選級段落1
raw, ok = rep_bytes(raw,
    '<p>精選級是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的傳播妹通常是：',
    '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：',
    '精選級 段落1')
if ok: changes += 1

# 12. 精選級段落2
raw, ok = rep_bytes(raw,
    '<p>精選級的傳播小姐服務品質穩定',
    '<p>標準公關服務品質穩定',
    '精選級 段落2')
if ok: changes += 1

# 13. dateModified
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
L('dateModified: %d' % n)
if n: changes += 1

# Write
with open(PATH, 'wb') as f:
    f.write(raw)
L('Written. Total changes: %d' % changes)

# Final verification
html = raw.decode('utf-8', errors='replace')
L('')
L('=== FINAL ===')
for p in ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
          '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
          '2500-3500元', '3500-5000元', '5000-8000元']:
    L('%s: %d' % (p, html.count(p)))

with open(LOG, 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Log written to _fix_final2_log.txt')
