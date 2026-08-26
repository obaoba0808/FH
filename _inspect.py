with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html', 'rb') as f:
    raw = f.read()

html = raw.decode('utf-8', errors='replace')
idx = html.find('普通級')
print('普通級 at:', idx)
print('Context (60 chars):', repr(html[idx-10:idx+80]))

# Find the exact bytes of the surrounding context
old_str = '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
idx2 = html.find(old_str)
print('old_str found:', idx2)

# Show raw bytes around 普通級
pat_utf8 = '普通級'.encode('utf-8')
pos_utf8 = raw.find(pat_utf8)
print('\nRaw byte pos:', pos_utf8)
print('Raw bytes around (pos-50 to pos+50):', repr(raw[pos_utf8-50:pos_utf8+50]))

# Also check with byte replacement
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_old_str_bytes.txt', 'wb') as out:
    out.write(raw[pos_utf8-200:pos_utf8+200])
print('\nDumped 400 bytes to _old_str_bytes.txt')
