# _fix_vip.py — Fix remaining issues after _hex_fix2.py
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
today = datetime.date.today().isoformat()

with open(fp, 'rb') as f:
    raw = f.read()

log = []

def L(msg):
    log.append(msg)

L('File size: %d' % len(raw))

# ===== VIP H3 =====
# Try different byte patterns for the VIP H3
vip_patterns = [
    b'<h3>3. VIP\xef\xbc\x9a4000-6000\xe5\x85\x83/\xe5\xb0\x8f\xe6\x99\x82</h3>',
    b'<h3>3. VIP\xef\xbc\x9a 4000-6000\xe5\x85\x83/\xe5\xb0\x8f\xe6\x99\x82</h3>',
    b'<h3>3. VIP</h3>',
]
new_vip = '<h3>3. VIP \xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$4,000/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$2,000/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'.encode('utf-8')

for pat in vip_patterns:
    L('Searching for VIP pattern: %s' % repr(pat))
    if pat in raw:
        raw = raw.replace(pat, new_vip, 1)
        L('OK: VIP H3 replaced (pattern: %s)' % repr(pat))
        break
else:
    # Search for VIP in H3 context
    vip_idx = raw.find(b'VIP')
    L('VIP found at byte: %s' % vip_idx)
    if vip_idx > 0:
        ctx = raw[max(0, vip_idx-20):vip_idx+100]
        L('VIP context: %s' % repr(ctx))
        # Try to find the full H3 tag
        h3_start = raw.rfind(b'<h3>', 0, vip_idx)
        h3_end = raw.find(b'</h3>', vip_idx)
        if h3_end > h3_start:
            full_h3 = raw[h3_start:h3_end+5]
            L('Full H3 tag: %s' % full_h3.decode('utf-8', errors='replace'))
            # Check if it contains old pricing
            if b'4000' in full_h3 or b'6000' in full_h3:
                raw = raw.replace(full_h3, new_vip, 1)
                L('OK: VIP H3 replaced (by context)')

# ===== 頂級 (top tier) remaining mentions =====
# Count current 頂級 mentions
html = raw.decode('utf-8', errors='replace')
dd_count = html.count('\xe9\xa0\x82\xe7\xb4\x9a')  # 頂級
L('Current 頂級 count: %d' % dd_count)

# Find all occurrences of 頂級 in H3 tags
L('\nSearching for remaining 頂級 H3 tags:')
for m in re.finditer(rb'<h3>[^<]*\xe9\xa0\x82[^<]*</h3>', raw):
    L('  H3: ' + m.group().decode('utf-8', errors='replace'))

# ===== dateModified =====
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
L('dateModified: %d' % n)

# ===== Write =====
with open(fp, 'wb') as f:
    f.write(raw)
L('File written.')

# ===== Final counts =====
html2 = raw.decode('utf-8', errors='replace')
L('')
L('=== FINAL ===')
strings = ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
           '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
           '2500-3500元', '3500-5000元', '5000-8000元']
for s in strings:
    L('%s: %d' % (s, html2.count(s)))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_vip_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))

print('Done')
