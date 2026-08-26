fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\how_much.html'
with open(fp, 'rb') as f:
    raw = f.read()
html = raw.decode('utf-8', errors='replace')
lines = []
lines.append('Size: %d' % len(raw))
lines.append('普通級: %d' % html.count('普通級'))
lines.append('基礎公關: %d' % html.count('基礎公關'))
lines.append('精選級: %d' % html.count('精選級'))
lines.append('標準公關: %d' % html.count('標準公關'))
lines.append('2,400: %d' % html.count('2,400'))
lines.append('3,600: %d' % html.count('3,600'))
lines.append('4,000: %d' % html.count('4,000'))
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_check_hm2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('done')
