# _fix_h3_corrupt.py — Fix H3 closing tag using ALL hex escapes (ASCII-safe)
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

# CORRUPT closing: </strong>】/h3>
# Hex: 3c 2f 73 74 72 6f 6e 67 3e e3 80 91 2f 68 33 3e
corrupt = b'\x3c\x2f\x73\x74\x72\x6f\x6e\x67\x3e\xe3\x80\x91\x2f\x68\x33\x3e'
log.append('Corrupt count: %d' % raw.count(corrupt))

# CORRECT closing: </strong>】</h3>
# Hex: 3c 2f 73 74 72 6f 6e 67 3e e3 80 91 3c 2f 68 33 3e
correct = b'\x3c\x2f\x73\x74\x72\x6f\x6e\x67\x3e\xe3\x80\x91\x3c\x2f\x68\x33\x3e'
log.append('Correct count: %d' % raw.count(correct))

if corrupt in raw:
    raw = raw.replace(corrupt, correct)
    log.append('REPLACED corrupt with correct')
else:
    log.append('Corrupt not found')

# Write
with open(fp, 'wb') as f:
    f.write(raw)
log.append('Written')

html = raw.decode('utf-8', errors='replace')
log.append('\n=== H3 TAGS ===')
import re
for m in re.finditer(b'<h3.*?</h3>', raw, flags=re.DOTALL):
    log.append('[%d] %s' % (m.start(), m.group().decode('utf-8', errors='replace')[:100]))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_h3_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
