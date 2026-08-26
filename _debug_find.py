with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html', encoding='utf-8') as f:
    pg = f.read()
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_debug_out.txt', 'w', encoding='utf-8') as out:
    out.write('len: ' + str(len(pg)) + '\n')
    idx = pg.find('普通級')
    out.write('普通級 at: ' + str(idx) + '\n')
    if idx >= 0:
        out.write('context: ' + repr(pg[idx-10:idx+80]) + '\n')
    else:
        out.write('NOT FOUND\n')
    # Check char codes
    out.write('\nFirst 50 chars: ' + repr(pg[:50]) + '\n')
    # Check bytes
    raw = open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html', 'rb').read()
    out.write('\nRaw bytes len: ' + str(len(raw)) + '\n')
    pat_utf8 = '普通級'.encode('utf-8')
    out.write('普通級 UTF-8 bytes: ' + repr(pat_utf8) + '\n')
    pos_utf8 = raw.find(pat_utf8)
    out.write('Found in raw bytes at: ' + str(pos_utf8) + '\n')
