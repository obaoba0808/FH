import glob, re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
NEW = ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html']

all_pages = [f for f in glob.glob(ROOT + '/*.html') if 'google' not in f]
problems = []
for fpath in sorted(all_pages):
    fname = fpath.replace(ROOT + '\\', '')
    c = open(fpath, encoding='utf-8').read()
    for n in NEW:
        if n == fname:
            continue  # self-link skip
        if n not in c:
            problems.append(f'{fname}: missing {n}')

if problems:
    for p in problems:
        print('PROBLEM:', p)
else:
    print(f'ALL CLEAN: {len(all_pages)} pages, every page links to all 3 new pages (self-links skipped)')

# Also check no broken old-domain links remain in dropdowns
old_domain = 0
for fpath in all_pages:
    c = open(fpath, encoding='utf-8').read()
    if 'obaoba0808.github.io' in c:
        old_domain += 1
        print('OLD DOMAIN:', fpath.replace(ROOT + '\\', ''))
print(f'Pages with old-domain refs: {old_domain}')
