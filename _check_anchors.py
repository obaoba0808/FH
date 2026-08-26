import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
targets = ['pricing-guide-2026.html', 'business_dinner.html', 'how_much.html', 'first_time_called.html']

for fpath in sorted(glob.glob(ROOT + '/*.html'))[:5]:
    fname = fpath.replace(ROOT + '\\', '')
    content = open(fpath, encoding='utf-8').read()
    # Only check within dropdown area (情報特搜站)
    m = re.search(r'情報特搜站', content)
    if not m:
        continue
    dropdown = content[m.start():m.start()+8000]
    found = [t for t in targets if t in dropdown]
    print(f'{fname}: in-dropdown={found}')
