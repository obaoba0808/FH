fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

# Find all H3 tags
import re
log.append('=== ALL H3 TAGS ===')
for m in re.finditer(rb'<h3>[^<]+</h3>', raw):
    log.append('H3 [%d]: %s' % (m.start(), m.group().decode('utf-8', errors='replace')))

# Find VIP in the file
log.append('\n=== VIP occurrences ===')
vip_idx = raw.find(b'VIP')
while vip_idx >= 0:
    ctx = raw[max(0,vip_idx-30):vip_idx+60]
    log.append('VIP at %d: %s' % (vip_idx, repr(ctx.decode('utf-8', errors='replace'))))
    log.append('  Hex: %s' % ctx.hex(' '))
    vip_idx = raw.find(b'VIP', vip_idx + 1)

# VIP followed by 公關
vip_gong = raw.find(b'VIP \xe5\x85\xac\xe9\x97\xb4')
log.append('\nVIP 公關 at: %s' % vip_gong)

# Check around byte 422 (from earlier)
log.append('\n=== Context around byte 422 ===')
log.append(repr(raw[400:550].decode('utf-8', errors='replace')))
log.append('Hex: %s' % raw[400:550].hex(' '))

# VIP followed by price
for m in re.finditer(rb'VIP[^<]{0,20}NT\$', raw):
    log.append('VIP+NT$ at %d: %s' % (m.start(), repr(m.group().decode('utf-8', errors='replace'))))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_find_vip_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
