# _verify_fix.py — Read file as UTF-8, search for patterns, write exact bytes
# This script uses ONLY ASCII string literals + dynamic str() construction
# to avoid any source file encoding issues.
import os

fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'

with open(fp, 'rb') as f:
    raw = f.read()

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_verify_out.txt', 'w', encoding='utf-8') as out:
    out.write('File size: %d bytes\n' % len(raw))
    
    # Search for '2500-3500' bytes
    idx = raw.find(b'2500-3500')
    out.write('2500-3500 at: %d\n' % idx)
    if idx >= 0:
        out.write('Context: %s\n' % repr(raw[max(0,idx-40):idx+80]))
    
    # Search for '普通級' by UTF-8 bytes (constructed from ord)
    pt = chr(0x666E) + chr(0x901A) + chr(0x7D1A)  # 普通級
    pt_bytes = pt.encode('utf-8')
    idx2 = raw.find(pt_bytes)
    out.write('普通級 at: %d (UTF-8 bytes: %s)\n' % (idx2, pt_bytes.hex()))
    
    # Search for '精選級'
    jx = chr(0x7CBE) + chr(0x9078) + chr(0x7D1A)
    jx_bytes = jx.encode('utf-8')
    idx3 = raw.find(jx_bytes)
    out.write('精選級 at: %d\n' % idx3)
    
    # Show the full <p class="mb-0"> block
    if idx >= 0:
        mb0 = raw.rfind(b'<p class="mb-0">', 0, idx)
        pclose = raw.find(b'</p>', mb0)
        block = raw[mb0:pclose+5]
        out.write('\n<p> block (byte %d-%d):\n' % (mb0, pclose+5))
        out.write('Decoded: %s\n' % block.decode('utf-8', errors='replace'))
        out.write('Hex: %s\n' % block.hex(' '))
    
    # Search for all H3 tags
    import re
    for m in re.finditer(rb'<h3>[^<]+</h3>', raw):
        tag = m.group()
        out.write('H3: %s\n' % tag.decode('utf-8', errors='replace'))
    
    # Show the FAQ JSON-LD text field
    pt2 = chr(0x53D1) + chr(0x5EC3) + chr(0+0x6536) + chr(0x8CBB) + chr(0x696D) + chr(0x696E)
    pt2_b = pt2.encode('utf-8')
    idx4 = raw.find(pt2_b)
    if idx4 > 0:
        out.write('\nFAQ text region at: %d\n' % idx4)
        text_start = raw.rfind(b'"text": "', 0, idx4+50)
        if text_start >= 0:
            text_end = raw.find(b'"', text_start + 10)
            text_block = raw[text_start:text_end+1]
            out.write('FAQ text: %s\n' % text_block.decode('utf-8', errors='replace'))

print('Done. Check _verify_out.txt')
