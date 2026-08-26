# _fix5.py — Hard reset pricing sections in pricing-guide-2026.html
with open('pricing-guide-2026.html', 'rb') as f:
    raw = f.read()
html = raw.decode('utf-8')

idx = html.find('\u666a\u901a\u7d1a')  # 普通級
print('普通級 at byte-utf8 pos:', idx)
print(repr(html[idx-5:idx+100]))
