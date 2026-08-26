# _fix_h3_num.py — Fix H3-4 numbering by finding <h3>3. {bad_utf8}頂
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
today = datetime.date.today().isoformat()

with open(fp, 'rb') as f:
    raw = f.read()

log = []

# The H3-4 has corrupt UTF-8 bytes for 頂: c3 a9 c2 a0 c2 82 c3 a7 c2 b4 c2 9a
# followed by the valid 級 bytes: e5 85 ac e9 97 9c
corrupt = b'\xc3\xa9\xc2\xa0\xc2\x82\xc3\xa7\xc2\xb4\xc2\x9a'
valid = b'\xe9\xa0\x82'  # 頂 in proper UTF-8

# Find all occurrences of this corrupt pattern
pos = 0
while True:
    idx = raw.find(corrupt, pos)
    if idx < 0:
        break
    # Check if it's in H3 context
    before = raw[max(0,idx-30):idx]
    after = raw[idx:idx+20]
    log.append('Corrupt at %d: ...%s|%s' % (idx, before[-20:], after[:15]))
    pos = idx + 1

# Replace ALL corrupt 頂 with valid UTF-8 頂
n_replace = raw.count(corrupt)
log.append('Replace count: %d' % n_replace)

if n_replace > 0:
    raw = raw.replace(corrupt, valid)
    log.append('Replaced corrupt with valid')

# Now fix: the H3-4 <h3>3. 頂級 should be <h3>4. 頂級
# Find H3 with "3. " followed by the valid 頂
# Pattern in bytes: <h3>3. {valid_頂}...
old_h3 = b'<h3>3. \xe9\xa0\x82'  # <h3>3. 頂
new_h3 = b'<h3>4. \xe9\xa0\x82'  # <h3>4. 頂
if old_h3 in raw:
    raw = raw.replace(old_h3, new_h3, 1)
    log.append('OK: H3-4 renumbered (3.->4.)')
else:
    log.append('MISS: <h3>3. 頂 pattern')

# dateModified
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
log.append('dateModified: %d' % n)

with open(fp, 'wb') as f:
    f.write(raw)
log.append('Written (%d bytes)' % len(raw))

html = raw.decode('utf-8', errors='replace')
log.append('')
log.append('=== H3 TAGS ===')
for m in re.finditer(b'<h3.*?</h3>', raw, flags=re.DOTALL):
    decoded = m.group().decode('utf-8', errors='replace')
    log.append('[%d len=%d] %s' % (m.start(), len(m.group()), decoded[:100]))

log.append('')
log.append('=== COUNTS ===')
for s in ['基礎公關', '標準公關', 'VIP', '頂級', '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時']:
    log.append('%s: %d' % (s, html.count(s)))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_h3_num_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
