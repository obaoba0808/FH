import sys, glob, re
sys.stdout.reconfigure(encoding='utf-8')

idx = open('index.html', 'r', encoding='utf-8').read()

# ── Extract reference nav ──
nav_start = idx.index('<!-- Navbar')
nav_end   = idx.index('</nav>', nav_start) + 6
ref_nav = idx[nav_start:nav_end]

# ── Extract reference footer + scripts + </html> ──
f_start = idx.index('<footer')
f_end   = idx.index('</html>', f_start) + 7
ref_footer_scripts = idx[f_start:f_end]

# ── Extract body-opening divs (noise-overlay, bg-canvas, lens-flare) ──
body_tag_end = idx.index('>', idx.index('<body')) + 1
nl_after_body = idx.index('\n', body_tag_end) + 1
ref_body_divs = idx[nl_after_body:nav_start].strip()

print(f'ref_nav: {len(ref_nav)} bytes')
print(f'ref_footer+scripts: {len(ref_footer_scripts)} bytes')
print(f'ref_body_divs: {len(ref_body_divs)} bytes')

# ── Process all HTML files ──
files = sorted(glob.glob('*.html'))
count = 0

for fname in files:
    base = fname.lower().replace('.html','')
    if 'google' in base:
        print(f'{fname}: SKIP (google verification)')
        continue
    if fname == 'index.html':
        print(f'{fname}: SKIP (reference)')
        continue
    
    html = open(fname, 'r', encoding='utf-8').read()
    original = html
    
    changes = []
    
    # ── Step 1: Inject body divs if missing ──
    if 'noise-overlay' not in html:
        # Find <body ...> tag
        bm = re.search(r'<body[^>]*>', html)
        if bm:
            inject_pos = bm.end()
            # Insert after the body tag's newline
            next_nl = html.index('\n', inject_pos) + 1 if '\n' in html[inject_pos:] else inject_pos
            html = html[:next_nl] + ref_body_divs + '\n\n' + html[next_nl:]
            changes.append('body_divs')
    
    # ── Step 2: Replace nav ──
    # Find nav by matching known patterns
    nav_patterns = [
        '<nav class="fixed w-full z-50 top-0',
        '<nav class="fixed w-full top-0 z-50',
        '<nav class="fixed top-0 w-full z-50',
    ]
    nav_i = -1
    for p in nav_patterns:
        nav_i = html.find(p)
        if nav_i >= 0:
            break
    
    if nav_i >= 0:
        nav_close = html.index('</nav>', nav_i) + 6
        html = html[:nav_i] + ref_nav + '\n\n' + html[nav_close:]
        changes.append('nav')
    
    # ── Step 3: Replace footer + scripts ──
    f_i = html.find('<footer')
    if f_i >= 0:
        html = html[:f_i] + ref_footer_scripts
        changes.append('footer')
    
    if changes:
        open(fname, 'w', encoding='utf-8').write(html)
        count += 1
        print(f'{fname}: {" + ".join(changes)}')
    else:
        print(f'{fname}: no changes')

print(f'\nDone. Modified {count} files.')
