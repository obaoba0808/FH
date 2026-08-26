import sys, os, re
sys.stdout.reconfigure(encoding='utf-8')

old_path = 'dist/output.css'
new_path = 'dist/main.css'
new_ref = new_path + '?v=1'

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
changed = 0
for fn in html_files:
    text = open(fn, encoding='utf-8').read()
    # Replace any reference to old css path (with or without version) -> new path
    new_text = re.sub(
        r'(dist/)output\.css(\?v=[^"\']*)?',
        lambda m: new_path + '?v=1',
        text
    )
    # Also handle the bare new path without version if any
    new_text = new_text.replace('dist/main.css', 'dist/main.css?v=1')
    if new_text != text:
        open(fn, 'w', encoding='utf-8').write(new_text)
        changed += 1
        print(f'Updated: {fn}')

print(f'\nTotal: {changed}/{len(html_files)} files changed')
