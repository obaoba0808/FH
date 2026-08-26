# _dump_pos.py — Dump exact bytes at key positions
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

def D(label, pos, n):
    if 0 <= pos < len(raw):
        chunk = raw[pos:pos+n]
        log.append('%s @%d (hex): %s' % (label, pos, chunk.hex(' ')))
        log.append('%s @%d (decoded): %s' % (label, pos, chunk.decode('utf-8', errors='replace')))
    else:
        log.append('%s @%d: OUT OF RANGE (size=%d)' % (label, pos, len(raw)))

D('H3-3 VIP', 29515, 70)
D('H3-4  頂級', 30195, 70)
D('H3-5 after', 30790, 70)

# Search for ALL occurrences of "3. " followed by single CJK in H3 context
import re
for m in re.finditer(b'<h3>[0-9]+\\. ', raw):
    ctx = raw[m.start():m.start()+60]
    log.append('H3 number @%d: %s' % (m.start(), ctx.decode('utf-8', errors='replace')))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_dump_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
