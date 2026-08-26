import glob

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
NEW = ['beginners-checklist.html', '2026-pricing-table.html', 'private-party-guide.html']

missing_report = []
for fpath in sorted(glob.glob(ROOT + '/*.html')):
    fname = fpath.replace(ROOT + '\\', '')
    if 'google' in fname or fname in NEW:
        continue
    content = open(fpath, encoding='utf-8').read()
    missing = [n for n in NEW if n not in content]
    if missing:
        missing_report.append((fname, missing))

for fname, missing in missing_report:
    print(f'{fname}: MISSING {missing}')
print(f'\nTotal pages missing links: {len(missing_report)}')
