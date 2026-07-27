import sys, glob
sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('*.html'))
skip = {'google1798bed44632c997.html', 'index.html'}
for f in files:
    base = f.lower()
    if base in skip or 'google' in base: continue
    html = open(f, encoding='utf-8').read()
    i = html.find('<footer')
    if i < 0: print(f'{f}: NO FOOTER'); continue
    try:
        e = html.index('</footer>', i) + 9
        footer = html[i:e]
    except:
        print(f'{f}: BAD FOOTER'); continue
    has_grid = 'grid-cols' in footer
    has_newbie = '新手指南' in footer
    has_scene = '場合攻略' in footer
    has_crown = 'mdi:crown' in footer
    print(f'{f}: grid={has_grid} 新手指南={has_newbie} 場合攻略={has_scene} crown={has_crown}')
