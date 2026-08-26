# _scan_hex2.py — Use \xNN escapes (ASCII-only, always safe)
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

# Corrupt closing: </strong>】/h3>
corrupt = b'\x3c\x2fstrong\x3e\xe3\x80\x91\x2fh3\x3e'
log.append('Corrupt %d: %s' % (raw.count(corrupt), repr(corrupt)))

# Correct closing: </strong>】</h3>
correct = b'\x3c\x2fstrong\x3e\xe3\x80\x91\x3c\x2fh3\x3e'
log.append('Correct %d' % raw.count(correct))

pos = raw.find(corrupt)
log.append('Corrupt at: %s' % pos)
if pos >= 0:
    ctx = raw[pos-60:pos+120]
    log.append('Context: %s' % repr(ctx.decode('utf-8', errors='replace')))
    log.append('Hex: %s' % ctx.hex(' '))

# Replace corrupt with correct
if pos >= 0:
    n = raw.count(corrupt)
    raw = raw.replace(corrupt, correct)
    log.append('Replaced %d' % n)

# Also find standalone </h3> with stray chars
log.append('\n=== All </h3> in H3 context ===')
import re
for m in re.finditer(b'</h3>', raw):
    ctx = raw[max(0,m.start()-15):m.start()+5]
    log.append('</h3> at %d: ...%s' % (m.start(), repr(ctx.decode('utf-8', errors='replace'))))

# Write
with open(fp, 'wb') as f:
    f.write(raw)
log.append('Written')

html = raw.decode('utf-8', errors='replace')
log.append('\n=== H3 TAGS ===')
for m in re.finditer(b'<h3.*?</h3>', raw, flags=re.DOTALL):
    log.append('[%d] %s' % (m.start(), m.group().decode('utf-8', errors='replace')[:80]))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_scan_hex2_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
