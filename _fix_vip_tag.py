# _fix_vip_tag.py — Fix H3 VIP using exact bytes from hex analysis
import re, datetime

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
today = datetime.date.today().isoformat()

with open(fp, 'rb') as f:
    raw = f.read()

log = []
def L(msg):
    log.append(msg)

L('File size: %d' % len(raw))

# The H3 VIP tag has the format:
# <h3>【<strong>VIP</strong>】 <strong>NT$4,000/2小時</strong>】/h3>
# The "】/h3>" comes from a BAD closing tag that spans H3 tags
# We need to find and fix this malformed closing

# Search for the bad pattern: </strong>】/h3>
bad_close = b'</strong>\xe3\x80\x91/h3>'
if bad_close in raw:
    L('Found bad close at: %d' % raw.find(bad_close))
    # Count occurrences
    cnt = raw.count(bad_close)
    L('Count: %d' % cnt)
    # Fix: remove the stray 】/h3> and close properly
    # Actually the issue is the tag says </h3> but has stray characters
    # Pattern: ...NT$4,000/2小時</strong>】/h3>  
    # Should be: ...NT$4,000/2小時</strong>】</h3>
    fixed_close = b'</strong>\xe3\x80\x91</h3>'
    raw = raw.replace(bad_close, fixed_close)
    L('Fixed %d occurrences' % cnt)
else:
    L('Bad close not found')

# Also check for VIP line that has "】<strong>NT$" pattern followed by bad close
# Search: VIP...NT$4,000...】/h3>
# The old (broken) H3 structure: <h3>【<strong>VIP</strong>】 <strong>NT$4,000/2小時</strong>】</h3>
# But it appears as: <h3>【<strong>VIP</strong>】 <strong>NT$4,000/2小時</strong>】/h3>
old_vip_h3 = (
    b'<h3>\xe3\x80\x90<strong>VIP</strong>\xe3\x80\x91 '
    b'<strong>NT$4,000/2\xe5\xb0\x8f\xe6\x99\x82</strong>'
    b'\xe3\x80\x91/h3>'
)
new_vip_h3 = (
    b'<h3>\xe3\x80\x90<strong>VIP</strong>\xe3\x80\x91 '
    b'<strong>NT$4,000/2\xe5\xb0\x8f\xe6\x99\x82</strong>'
    b'\xe3\x80\x91</h3>'
)

if old_vip_h3 in raw:
    raw = raw.replace(old_vip_h3, new_vip_h3)
    L('OK: VIP H3 fixed (old pattern)')
else:
    L('Old VIP H3 pattern not found')

# Also try the same pattern without leading <h3>
old_vip_inner = (
    b'\xe3\x80\x90<strong>VIP</strong>\xe3\x80\x91 '
    b'<strong>NT$4,000/2\xe5\xb0\x8f\xe6\x99\x82</strong>'
    b'\xe3\x80\x91/h3>'
)
new_vip_inner = (
    b'\xe3\x80\x90<strong>VIP</strong>\xe3\x80\x91 '
    b'<strong>NT$4,000/2\xe5\xb0\x8f\xe6\x99\x82</strong>'
    b'\xe3\x80\x91</h3>'
)
if old_vip_inner in raw:
    raw = raw.replace(old_vip_inner, new_vip_inner)
    L('OK: VIP inner fixed')
else:
    L('Old VIP inner pattern not found')

# Try to find ANY occurrence of VIP followed by NT$4,000 in H3 context
idx = raw.find(b'VIP</strong>')
while idx >= 0:
    ctx = raw[max(0,idx-5):idx+100]
    if b'/h3>' in ctx or b'</h3>' in ctx:
        L('VIP in H3 context at %d: %s' % (idx, repr(ctx.decode('utf-8', errors='replace'))))
    idx = raw.find(b'VIP</strong>', idx+1)

# dateModified
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
L('dateModified: %d' % n)

# Write
with open(fp, 'wb') as f:
    f.write(raw)
L('File written.')

# Final
html = raw.decode('utf-8', errors='replace')
L('')
L('=== FINAL ===')
L('普通級: %d' % html.count('普通級'))
L('精選級: %d' % html.count('精選級'))
L('基礎公關: %d' % html.count('基礎公關'))
L('標準公關: %d' % html.count('標準公關'))
L('VIP 公關: %d' % html.count('VIP 公關'))
L('頂級公關: %d' % html.count('頂級公關'))
L('2,400/2小時: %d' % html.count('2,400/2小時'))
L('3,600/2小時: %d' % html.count('3,600/2小時'))
L('4,000/2小時: %d' % html.count('4,000/2小時'))
L('5,000+/2小時: %d' % html.count('5,000+/2小時'))

L('')
L('=== H3 TAGS ===')
for m in re.finditer(rb'<h3>.*?</h3>', raw):
    L('[%d] %s' % (m.start(), m.group().decode('utf-8', errors='replace')))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_fix_vip_tag_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
