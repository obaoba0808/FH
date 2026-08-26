# _rebuild_vip.py — Rebuild missing H3-3 VIP tag and renumber H3-4
fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()

log = []
def L(msg):
    log.append(msg)

L('File size: %d' % len(raw))

# ================================================================
# 1. Fix H3-4 numbering: "4. 頂級" -> "3. 頂級"
# ================================================================
# From scan: H3-4 at byte 30195 = <h3>4. 頂級...NT$5,000+...
old_h3_4_num = b'<h3>4. \xe9\xa0\x82\xe7\xb4\x9a'  # <h3>4. 頂級
new_h3_4_num = '<h3>3. \xe9\xa0\x82\xe7\xb4\x9a'.encode('utf-8')

if old_h3_4_num in raw:
    raw = raw.replace(old_h3_4_num, new_h3_4_num, 1)
    L('OK: Renumbered H3-4 (4.->3.)')
else:
    L('MISS: H3-4 renumber')

# ================================================================
# 2. Insert new H3-3 VIP between H3-2 and H3-4
# ================================================================
# New VIP H3 tag
new_h3_vip = (
    b'<h3>2. VIP \xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9a'
    b'NT$4,000/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88'
    b'\xe2\x88\x88NT$2,000/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'
)

# Find insertion point: after H3-2 content, before H3-4 section
# H3-2 content ends around byte 29433 (its closing </h3>)
# Look for the </h3> that marks end of H3-2 (around byte 29496)
h3_2_close = b'\x85\xac\xe9\x97\x9c\xef\xbc\x9aNT$3,600/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x89\x88NT$1,800/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'
pos = raw.find(h3_2_close)
L('H3-2 close at: %d' % pos)

if pos >= 0:
    # Insert new H3 after this closing tag
    # Find the next newline after </h3>
    insert_after = pos + len(h3_2_close)
    # Skip whitespace to a clean point
    skip = 0
    while insert_after < len(raw) and raw[insert_after:insert_after+1] in (b'\r', b'\n', b' ', b'\t'):
        insert_after += 1
        skip += 1
    L('Skipped %d whitespace bytes' % skip)
    
    L('Inserting new H3 at byte %d' % insert_after)
    L('Context before: %s' % repr(raw[insert_after-10:insert_after+20]))
    
    # Find the next <h3> (H3-4)
    next_h3 = raw.find(b'<h3>', insert_after)
    L('Next <h3> at byte %d' % next_h3)
    
    # Build the VIP section content
    vip_content = (
        b'\n\n\n            <p>VIP \xe5\x85\xac\xe9\x97\xb4\xe6\x98\xaf\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82'
        b'\xb3\xe6\x92\xad\xe5\xb8\x82\xe5\xa0\xb4\xe7\x9a\x84<strong>\xe9\xab\x98\xe9\x9a\x90'
        b'\xe6\xb6\x88\xe8\xb2\xbb\xe5\x8d\x80\xe9\x96\x93</strong>\xef\xbc\x8c\xe9\x80\xb2\xe5'
        b'\x85\xa5\xe9\x80\x99\xe5\x80\x8b\xe5\x83\xb9\xe4\xbd\x8d\xe7\x9a\x84\xe4\xba\xba\xe9'
        b'\x80\xb1\xe5\xb8\xb8\xe6\x9c\x83\xe6\x9b\xb4\xe9\xab\x98\xe7\x9a\x84\xe8\xa6\x81\xe6\xb1'
        b'\x82\xe3\x80\x82</p>\n\n\n            <ul>\n\n\n                <li>\xe5\xa4\x96\xe5\x9e\x8b\xe4\xb8\xad\xe4\xb8\x8a\xe6\xb0\xb4\xe6\xba\x96\xef'
        b'\xbc\x8c\xe5\xa4\x96\xe8\xa1\x8c\xe5\x8f\xaf\xe6\x89\xbf</li>\n\n\n                <li>\xe5\xae\xb6\xe5\xba\xad\xe6\x99\x82\xe6\x9c\x83\xe5\x85\xa8\xe5\x93\x81\xe4\xb8'
        b'\xbb\xe8\xa6\x81\xe6\x89\xbf\xe8\xb2\xbb</li>\n\n\n                <li>\xe6\x9c\x83\xe8\x80\x81\xe6\x9a\x8c\xe4\xb8\x8a\xe7\x9a\x84\xe6\x9c\x8d\xe5\x8b'
        b'\x99\xe7\xa6\x8f\xe5\x88\xa9</li>\n\n\n            </ul>\n\n\n            <p>VIP \xe5\x85\xac\xe9\x97\xb4\xe9\x80\xb2\xe5\x85\xa5\xe6\x96\x87\xe5\x8c\x96\xe5\x9c'
        b'\xb0\xe7\x90\x83\xe6\x9c\x83\xe4\xb8\x80\xe5\xae\x9a\xe5\xb9\xb4\xe8\xb3\x87\xe5\x8f\x8a'
        b'\xe4\xb8\x8a\xe6\xb5\xb7\xe7\x9a\x84\xe4\xba\xba\xe5\xa3\xab\xe7\x94\x9f\xe6\xb6\xaf\xe3\x80'
        b'\x82\xe5\xa6\x82\xe6\x9e\x9c\xe4\xbd\xa0\xe6\x9c\x89\xe8\x87\xaa\xe5\xb7\xa5\xe8\xb3\x87'
        b'\xe6\xba\x90\xe5\x8f\x8a\xe5\xb8\x82\xe5\xa0\xb4\xe4\xba\xa4\xe9\x9b\x9c\xef\xbc\x8c'
        b'\xe9\x80\xb2\xe5\x85\xa5 VIP \xe5\x85\xac\xe9\x97\xb4\xe6\x98\xaf\xe5\xbe\x88\xe5\xa5\xbd'
        b'\xe7\x9a\x84\xe9\x81\xb8\xe6\x93\x8a\xe3\x80\x82</p>'
    )
    
    # Insert H3 + content before next <h3>
    if next_h3 > insert_after:
        before_next = raw[insert_after:next_h3]
        L('Content between insert point and next H3 (%d bytes):' % len(before_next))
        L(repr(before_next[:100]))
        
        raw = raw[:insert_after] + new_h3_vip + vip_content + raw[insert_after:]
        L('OK: Inserted H3-3 VIP + content')
    else:
        L('WARN: Could not find next H3')
else:
    L('MISS: H3-2 close not found')

# ================================================================
# 3. dateModified
# ================================================================
import re, datetime
today = datetime.date.today().isoformat()
new_dm = ('"dateModified": "%s"' % today).encode('utf-8')
raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
L('dateModified: %d' % n)

# ================================================================
# 4. Write
# ================================================================
with open(fp, 'wb') as f:
    f.write(raw)
L('File written (%d bytes)' % len(raw))

# ================================================================
# 5. Verify
# ================================================================
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
for m in re.finditer(b'<h3.*?</h3>', raw, flags=re.DOTALL):
    decoded = m.group().decode('utf-8', errors='replace')
    L('[%d len=%d] %s' % (m.start(), len(m.group()), decoded[:100]))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_rebuild_vip_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log))
print('Done')
