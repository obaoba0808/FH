import os, glob

root_relative = {
    '/FH/index.html': '/',
    '/FH/faq-all-in-one.html': '/faq-all-in-one.html',
    '/FH/first_time_called.html': '/first_time_called.html',
    '/FH/news.html': '/news.html',
}

abs_old = 'https://obaoba0808.github.io/FH/'
abs_new = 'https://obaoba.online/'

files = sorted(glob.glob('*.html'))
for f in files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    orig = content
    for old, new in root_relative.items():
        content = content.replace(old, new)
    if f == 'pricing-guide-2026.html':
        content = content.replace(abs_old, abs_new)
    if content != orig:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(content)
        print('Updated:', f)
print('--- done ---')
