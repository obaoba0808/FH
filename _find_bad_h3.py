# _find_bad_h3.py — Find and fix the VIP H3 closing tag
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []

def L(msg):
    log.append(msg)

L('File size: %d' % len(raw))

# Find all h3 closing tags and their contexts
import re

L('\n=== All h3> occurrences ===')
for m in re.finditer(b'h3>', raw):
    # Get 50 bytes before and 5 after
    ctx = raw[max(0,m.start()-50):m.start()+5]
    L('%d: %s' % (m.start(), repr(ctx)))

L('\n=== All H3 tags (DOTALL) ===')
for m in re.finditer(b'<h3>.*?</h3>', raw, flags=re.DOTALL):
    decoded = m.group().decode('utf-8', errors='replace')
    L('[%d len=%d] %s' % (m.start(), len(m.group()), decoded[:100]))

# Check if VIP H3 exists in the file at all
vip_pos = raw.find(b'VIP')
L('\nVIP positions: %d total' % raw.count(b'VIP'))

# The VIP H3 should be between bytes 30195 and 33467
# From earlier hex analysis, H3 at 30195 = 4. 頂級...
# So where is the 3. VIP? Maybe it was removed entirely.
# Let me check if 3. VIP exists
old_vip = raw.find(b'3. VIP')
L('3. VIP found at: %s' % old_vip)

# Check for <h3>3. (the VIP number)
h3_3 = raw.find(b'<h3>3. ')
L('<h3>3. found at: %s' % h3_3)
if h3_3 > 0:
    ctx = raw[h3_3:h3_3+80]
    L('Context: %s' % repr(ctx.decode('utf-8', errors='replace')))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_find_bad_h3_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
