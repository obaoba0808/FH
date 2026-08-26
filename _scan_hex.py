# _scan_hex.py — Find the exact corrupted H3 closing sequence
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

# Find the sequence: </strong> followed by </h3> or /h3>  
# Search for the CORRUPTED closing: </strong>】/h3>
# Hex: 3c 2f 73 74 72 6f 6e 67 3e e3 80 91 2f 68 33 3e
corrupt = b'\x3c\x2f\x73\x74\x72\x6f\x6e\x67\x3e\xe3\x80\x91\x2f\x68\x33\x3e'
pos = raw.find(corrupt)
log.append('Corrupt sequence at: %s' % pos)
if pos >= 0:
    # Show 200 bytes around it
    ctx = raw[pos-50:pos+150]
    log.append('Context (decoded): %s' % ctx.decode('utf-8', errors='replace'))
    log.append('Context (hex): %s' % ctx.hex(' '))

# Also find the CORRECT closing: </strong>】</h3>
# Hex: 3c 2f 73 74 72 6f 6e 67 3e e3 80 91 3c 2f 68 33 3e
correct = b'\x3c\x2f\x73\x74\x72\x6f\x6e\x67\x3e\xe3\x80\x91\x3c\x2f\x68\x33\x3e'
pos2 = raw.find(correct)
log.append('\nCorrect sequence at: %s' % pos2)
if pos2 >= 0:
    ctx2 = raw[pos2-50:pos2+50]
    log.append('Context (decoded): %s' % ctx2.decode('utf-8', errors='replace'))

# Find all occurrences of </h3> in the file
log.append('\n=== All </h3> positions ===')
import re
for m in re.finditer(b'</h3>', raw):
    ctx = raw[max(0,m.start()-20):m.start()+5]
    log.append('</h3> at %d: ...%s' % (m.start(), repr(ctx.decode('utf-8', errors='replace'))))

# Find any occurrence of 】/h3> 
log.append('\n=== All 】/h3> positions ===')
for m in re.finditer(b'\xe3\x80\x91\x2f\x68\x33\x3e', raw):
    ctx = raw[max(0,m.start()-30):m.start()+30]
    log.append('】/h3> at %d: %s' % (m.start(), repr(ctx.decode('utf-8', errors='replace'))))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_scan_hex_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
