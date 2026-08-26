# _final_cleanup.py — Fix remaining old pricing in JSON-LD and H3 tags
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
today = datetime.date.today().isoformat()

with open(fp, 'rb') as f:
    raw = f.read()

log = []
def L(msg):
    log.append(msg)

L('File size: %d' % len(raw))

# ==============================================================
# 1. H3 VIP tag — find <h3>3. VIP</h3> and upgrade to 公關
# ==============================================================
# Search for H3 tag that contains "VIP" but not "NT$"
h3_vip_old = b'<h3>3. VIP</h3>'
h3_vip_new = '<h3>3. VIP \xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$4,000/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$2,000/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'.encode('utf-8')
if h3_vip_old in raw:
    raw = raw.replace(h3_vip_old, h3_vip_new, 1)
    L('OK: H3 VIP upgraded')
else:
    L('H3 3. VIP tag not found (may already be fixed or different format)')

# Also search for any H3 containing just "3. VIP" with extra text
for m in re.finditer(rb'<h3>3\. VIP[^<]*</h3>', raw):
    tag = m.group()
    if b'NT$' not in tag:
        new_tag = '<h3>3. VIP \xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT$4,000/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT$2,000/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'.encode('utf-8')
        raw = raw.replace(tag, new_tag, 1)
        L('OK: H3 VIP upgraded (found: %s)' % tag.decode('utf-8', errors='replace'))
        break
else:
    L('No H3 VIP tag needing upgrade')

# ==============================================================
# 2. JSON-LD text fields — fix old price references
# ==============================================================
L('\nFixing JSON-LD text fields:')

# Fix: "2500-5000元/2小時" -> "NT$2,400-5,000/2小時"
old1 = b'2500-5000\xe5\x85\x83/2\xe5\xb0\x8f\xe6\x99\x82'
new1 = 'NT$2,400-5,000/2\xe5\xb0\x8f\xe6\x99\x82'.encode('utf-8')
if old1 in raw:
    raw = raw.replace(old1, new1, 1)
    L('OK: 2500-5000元/2小時 -> NT$2,400-5,000/2小時')
else:
    L('MISS: 2500-5000元/2小時')

# Fix: "5000-8000元以上" in JSON-LD -> "NT$5,000元以上"
old2 = b'5000-8000\xe5\x85\x83\xe4\xbb\xa5\xe4\xb8\x8a'
new2 = 'NT$5,000\xe4\xbb\xa5\xe4\xb8\x8a'.encode('utf-8')
if old2 in raw:
    raw = raw.replace(old2, new2, 1)
    L('OK: 5000-8000元以上 -> NT$5,000元以上')
else:
    L('MISS: 5000-8000元以上')

# Fix: "5000-15000元" -> "NT$5,000-15,000元"
old3 = b'5000-15000\xe5\x85\x83'
new3 = 'NT$5,000-15,000\xe5\x85\x83'.encode('utf-8')
if old3 in raw:
    raw = raw.replace(old3, new3, 1)
    L('OK: 5000-15000元 -> NT$5,000-15,000元')
else:
    L('MISS: 5000-15000元')

# Fix: "1500-5000元" (tips) -> "NT$1,500-5,000元"
old4 = b'1500-5000\xe5\x85\x83'
new4 = 'NT$1,500-5,000\xe5\x85\x83'.encode('utf-8')
if old4 in raw:
    raw = raw.replace(old4, new4, 1)
    L('OK: 1500-5000元 -> NT$1,500-5,000元')
else:
    L('MISS: 1500-5000元')

# Fix: "2500-8000元" -> "NT$2,400-8,000元"  
old5 = b'2500-8000\xe5\x85\x83'
new5 = 'NT$2,400-8,000\xe5\x85\x83'.encode('utf-8')
if old5 in raw:
    raw = raw.replace(old5, new5, 1)
    L('OK: 2500-8000元 -> NT$2,400-8,000元')
else:
    L('MISS: 2500-8000元')

# Fix: "3000-5000元" -> "NT$3,600-5,000元"
old6 = b'3000-5000\xe5\x85\x83'
new6 = 'NT$3,600-5,000\xe5\x85\x83'.encode('utf-8')
if old6 in raw:
    raw = raw.replace(old6, new6, 1)
    L('OK: 3000-5000元 -> NT$3,600-5,000元')
else:
    L('MISS: 3000-5000元')

# Fix: "8000-20000元" -> "NT$8,000-20,000元"
old7 = b'8000-20000\xe5\x85\x83'
new7 = 'NT$8,000-20,000\xe5\x85\x83'.encode('utf-8')
if old7 in raw:
    raw = raw.replace(old7, new7, 1)
    L('OK: 8000-20000元 -> NT$8,000-20,000元')
else:
    L('MISS: 8000-20000元')

# Fix: standalone "5000-8000元" -> "NT$5,000-8,000元"
old8 = b'>5000-8000\xe5\x85\x83<'
new8 = b'>NT$5,000-8,000\xe5\x85\x83<'
if old8 in raw:
    raw = raw.replace(old8, new8, 1)
    L('OK: >5000-8000元< -> >NT$5,000-8,000元<')
else:
    L('MISS: >5000-8000元<')

# ==============================================================
# 3. dateModified
# ==============================================================
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
L('dateModified: %d' % n)

# ==============================================================
# 4. Write
# ==============================================================
with open(fp, 'wb') as f:
    f.write(raw)
L('File written.')

# ==============================================================
# 5. Final counts
# ==============================================================
html = raw.decode('utf-8', errors='replace')
L('')
L('=== FINAL ===')
strings = ['普通級', '精選級', '基礎公關', '標準公關', 'VIP 公關', '頂級公關',
           '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時',
           '2500-3500元', '3500-5000元', '5000-8000元', '2500-5000', '5000-15000']
for s in strings:
    L('%s: %d' % (s, html.count(s)))

# Show all H3 tags
L('')
L('=== H3 TAGS ===')
for m in re.finditer(rb'<h3>[^<]+</h3>', raw):
    L(m.group().decode('utf-8', errors='replace'))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_final_cleanup_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))

print('Done')
