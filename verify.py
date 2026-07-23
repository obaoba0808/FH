with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

if "LINE_click" in c:
    print('[OK] LINE tracking: enabled')
else:
    print('[ERROR] LINE tracking: missing')

for p in ['compare-girls.html', 'business-guide.html', 'legality-guide.html', 'booking-guide.html']:
    if p in c:
        print(f'[OK] {p} in footer')
    else:
        print(f'[ERROR] {p} missing')

if 'ZhbG-nkaGf9TEhMItLV21s5Vku7ipxhZaVHHZShcdi4' in c:
    print('[OK] GSC verification tag: present')
