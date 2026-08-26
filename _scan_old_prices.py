# _scan_old_prices.py — Find all old pricing bytes in JSON-LD
import re

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []
def L(msg):
    log.append(msg)

# Old price ranges to find (in bytes)
old_ranges = [
    b'2500-5000',
    b'5000-8000',
    b'5000-15000',
    b'3000-5000',
    b'2500-8000',
    b'4000-6000',
    b'8000-20000',
    b'5000-10000',
]

for rng in old_ranges:
    pos = 0
    while True:
        idx = raw.find(rng, pos)
        if idx < 0:
            break
        ctx = raw[max(0,idx-60):idx+60]
        ctx_decoded = ctx.decode('utf-8', errors='replace')
        L('Found %s at byte %d:' % (rng.decode('ascii', errors='replace'), idx))
        L('  Context: %s' % repr(ctx_decoded))
        L('  Hex: %s' % ctx.hex(' '))
        pos = idx + 1

# Also scan all JSON-LD "text": fields
L('\n=== All JSON-LD text fields ===')
for m in re.finditer(rb'"text": "[^"]{20,}"', raw):
    text = m.group()
    decoded = text.decode('utf-8', errors='replace')
    # Check for old price patterns
    has_old = any(rng in text for rng in old_ranges)
    if has_old:
        L('\nOLD TEXT FIELD (needs fix):')
        L(decoded)
        L('Hex: %s' % text.hex(' '))

L('\nDone')
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_scan_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
