# _fix_numbers.py — Fix H3 numbering: VIP=3., 頂級=4.
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
today = datetime.date.today().isoformat()

with open(fp, 'rb') as f:
    raw = f.read()

log = []

# Fix: <h3>2. VIP -> <h3>3. VIP
old1 = b'<h3>2. VIP'
new1 = '<h3>3. VIP'.encode('utf-8')
if old1 in raw:
    raw = raw.replace(old1, new1, 1)
    log.append('OK: 2. VIP -> 3. VIP')
else:
    log.append('MISS: 2. VIP')

# Fix: <h3>3. 頂級 -> <h3>4. 頂級  
old2 = b'<h3>3. \xe9\xa0\x82'
new2 = '<h3>4. \xe9\xa0\x82'.encode('utf-8')
if old2 in raw:
    raw = raw.replace(old2, new2, 1)
    log.append('OK: 3. 頂級 -> 4. 頂級')
else:
    log.append('MISS: 3. 頂級')

# dateModified
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
log.append('dateModified: %d' % n)

with open(fp, 'wb') as f:
    f.write(raw)
log.append('Written (%d bytes)' % len(raw))

html = raw.decode('utf-8', errors='replace')
log.append('')
log.append('=== FINAL ===')
log.append('普通級: %d' % html.count('普通級'))
log.append('精選級: %d' % html.count('精選級'))
log.append('基礎公關: %d' % html.count('基礎公關'))
log.append('標準公關: %d' % html.count('標準公關'))
log.append('VIP 公關: %d' % html.count('VIP 公關'))
log.append('頂級公關: %d' % html.count('頂級公關'))
log.append('2,400/2小時: %d' % html.count('2,400/2小時'))
log.append('3,600/2小時: %d' % html.count('3,600/2小時'))
log.append('4,000/2小時: %d' % html.count('4,000/2小時'))
log.append('5,000+/2小時: %d' % html.count('5,000+/2小時'))

log.append('')
log.append('=== H3 TAGS ===')
for m in re.finditer(b'<h3.*?</h3>', raw, flags=re.DOTALL):
    decoded = m.group().decode('utf-8', errors='replace')
    log.append('[%d len=%d] %s' % (m.start(), len(m.group()), decoded[:100]))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_numbers_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
