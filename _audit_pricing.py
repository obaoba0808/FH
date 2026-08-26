# _audit_pricing.py — Final audit: check all old/new price strings
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()
html = raw.decode('utf-8', errors='replace')

log = []

def C(label, count):
    log.append('%s: %d' % (label, count))

log.append('=== AUDIT ===')
log.append('File size: %d bytes' % len(raw))

# New pricing
C('基礎公關', html.count('基礎公關'))
C('標準公關', html.count('標準公關'))
C('VIP 公關', html.count('VIP 公關'))
C('頂級公關', html.count('頂級公關'))
C('2,400/2小時', html.count('2,400/2小時'))
C('3,600/2小時', html.count('3,600/2小時'))
C('4,000/2小時', html.count('4,000/2小時'))
C('5,000+/2小時', html.count('5,000+/2小時'))

# Old pricing (should be 0)
C('普通級', html.count('普通級'))
C('精選級', html.count('精選級'))
C('2500-3500元', html.count('2500-3500元'))
C('3500-5000元', html.count('3500-5000元'))
C('5000-8000元', html.count('5000-8000元'))

# Old FAQ JSON-LD text
C('普通級約', html.count('普通級約'))
C('2500-3500', html.count('2500-3500'))
C('3500-5000', html.count('3500-5000'))

# Search for the old FAQ JSON-LD pattern in bytes
old_faq_pattern = b'\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad\xe6\x94\xb6\xe8\xb2\xbb'  # 台北傳播收費
faql_pos = raw.find(old_faq_pattern)
log.append('台北傳播收費 at: %s' % faql_pos)
if faql_pos > 0:
    ctx = raw[faql_pos:faql_pos+100]
    log.append('Context: %s' % repr(ctx.decode('utf-8', errors='replace')))

# Search for all "text": " patterns in JSON-LD
import re
for m in re.finditer(rb'"text": "[^"]{10,}"', raw):
    text = m.group()
    if len(text) > 20:  # Only real text fields
        decoded = text.decode('utf-8', errors='replace')
        if any(c >= '\u4e00' for c in decoded):  # Contains Chinese
            log.append('\nJSON-LD text field:')
            log.append(decoded[:200])

# H3 pricing section
log.append('\n=== H3 pricing tags ===')
for m in re.finditer(rb'<h3>[^<]*\xef\xbc\x9a[^<]*</h3>', raw):  # H3 containing fullwidth colon
    decoded = m.group().decode('utf-8', errors='replace')
    log.append(decoded)

# Hero <p> text
hero_start = raw.find(b'<p class="mb-0">')
hero_end = raw.find(b'</p>', hero_start)
if hero_start > 0:
    hero_p = raw[hero_start:hero_end+4]
    log.append('\nHero <p>:')
    log.append(hero_p.decode('utf-8', errors='replace'))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_audit_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))

print('Done')
