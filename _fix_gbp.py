import io

old = 'https://www.google.com/maps/search/?api=1&query=%E6%AD%90%E5%B7%B4%E5%82%B3%E6%92%AD&query_place_id=/g/11n3wwkbg5'
new = 'https://www.google.com/maps/search/?api=1&query=%E6%AD%90%E5%B7%B4%E5%82%B3%E6%92%AD'

for f in ['index.html', 'about-oppa.html']:
    p = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website/' + f
    s = io.open(p, encoding='utf-8').read()
    n = s.count(old)
    s = s.replace(old, new)
    io.open(p, 'w', encoding='utf-8').write(s)
    print(f, 'replaced', n)
