# _find_vip2.py — Scan all H3 tags with DOTALL mode
import re

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

log.append('=== ALL H3 TAGS (DOTALL) ===')
for m in re.finditer(rb'<h3>.*?</h3>', raw, flags=re.DOTALL):
    decoded = m.group().decode('utf-8', errors='replace')
    log.append('[%d] %s' % (m.start(), decoded))

log.append('\n=== H3 with VIP ===')
for m in re.finditer(rb'<h3>[^<]*VIP[^<]*</h3>', raw, flags=re.DOTALL):
    log.append('[%d] %s' % (m.start(), m.group().decode('utf-8', errors='replace')))

log.append('\n=== Context around VIP at 28156 ===')
ctx = raw[28000:30400]
log.append('Decoded: %s' % ctx.decode('utf-8', errors='replace'))
log.append('Hex: %s' % ctx.hex(' '))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_find_vip2_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
