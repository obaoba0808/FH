fp = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(fp, 'rb') as f:
    raw = f.read()
html = raw.decode('utf-8', errors='replace')

lines = []
lines.append('File size: %d bytes' % len(raw))
lines.append('普通級: %d' % html.count('普通級'))
lines.append('精選級: %d' % html.count('精選級'))
lines.append('基礎公關: %d' % html.count('基礎公關'))
lines.append('標準公關: %d' % html.count('標準公關'))
lines.append('VIP 公關: %d' % html.count('VIP 公關'))
lines.append('頂級公關: %d' % html.count('頂級公關'))
lines.append('2,400: %d' % html.count('2,400'))
lines.append('3,600: %d' % html.count('3,600'))
lines.append('4,000: %d' % html.count('4,000'))
lines.append('5,000: %d' % html.count('5,000'))
lines.append('2500-3500: %d' % html.count('2500-3500'))
lines.append('3500-5000: %d' % html.count('3500-5000'))
lines.append('5000-8000: %d' % html.count('5000-8000'))
lines.append('2500: %d' % html.count('2500'))
lines.append('3000-5000: %d' % html.count('3000-5000'))
lines.append('5000-15000: %d' % html.count('5000-15000'))
lines.append('8000-20000: %d' % html.count('8000-20000'))
lines.append('3000-10000: %d' % html.count('3000-10000'))

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\_verify_final_log.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('VERIFIED')
