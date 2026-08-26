import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
changed = 0
for fn in html_files:
    text = open(fn, encoding='utf-8').read()
    # Replace any existing version, or add after .css
    new_text = re.sub(
        r'(<link[^>]+href=["\'])(dist/output\.css)([^"\']*)(["\'/])',
        r'\1\2?v=250826a\3\4',
        text
    )
    if new_text != text:
        open(fn, 'w', encoding='utf-8').write(new_text)
        changed += 1
        print(f'Updated: {fn}')

print(f'\nTotal: {changed}/{len(html_files)} files changed')
