# _fix_v6.py — bytes-based replacement with explicit hex
PATH = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'
with open(PATH, 'rb') as f:
    raw = f.read()

with open('_v6_log.txt', 'w') as log:
    def log_write(msg):
        log.write(msg + '\n')

    log_write(f'File size: {len(raw)}')

    # Find 2500-3500
    idx = raw.find(b'2500-3500')
    log_write(f'2500-3500 at: {idx}')
    if idx >= 0:
        ctx = raw[max(0,idx-20):idx+120]
        log_write(f'Context: {repr(ctx)}')

    # Find 普通級 UTF-8
    pt = '普通級'.encode('utf-8')
    idx2 = raw.find(pt)
    log_write(f'普通級 at: {idx2}')

    # Find 2026
    idx3 = raw.find(b'2026')
    log_write(f'2026 at: {idx3}')
    if idx3 >= 0:
        log_write(f'Context: {repr(raw[idx3:idx3+50])}')

    # === Hero region ===
    # Byte range: 28000-29500 (rough estimate from debug)
    # The exact bytes we confirmed:
    # <p class="mb-0">2026\xe5\xb9\xb4...普通級 2500-3500元...精選級 3500-5000元...頂級 5000-8000元+...
    # Let's build the exact bytes of the old hero <p> tag

    # From the hex dump:
    # <p class="mb-0">2026\xe5\xb9\xb4\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3\xe6\x92\xad\xe8\xa1\x8c\xe6\x83\x85\xef\xbc\x9a\xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a <strong>2500-3500\xe5\x85\x83</strong>\xef\xbc\x8c\xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a <strong>3500-5000\xe5\x85\x83</strong>\xef\xbc\x8c<strong>\xe9\xa1\x96\xe7\xb4\x9a</strong> <strong>5000-8000\xe5\x85\x83+</strong>\xe3\x80\x82\xe4\xbd\x8e\xe6\x96\xbc\xe9\x80\x99\xe5\x80\x8b\xe8\xa1\x8c\xe6\x83\x85\xe5\xa4\xaa\xe5\xa4\x9a\xe8\xa6\x81\xe5\xb0\x8f\xe5\xbf\x83\xe6\x9c\x89\xe9\xac\xbc\xef\xbc\x8c\xe9\xab\x98\xe6\x96\xbc\xe5\xa4\xaa\xe5\xa4\x9a\xe5\x8f\xaf\xe8\x83\xbd\xe6\x98\xaf\xe8\xa2\xab\xe7\x95\xb6\xe7\x9b\x86\xe5\xad\x90\xef\xbc\x81</p>
    old_hero_p = (
        b'<p class="mb-0">2026\xe5\xb9\xb4\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3'
        b'\xe6\x92\xad\xe8\xa1\x8c\xe6\x83\x85\xef\xbc\x9a\xe6\x99\xae\xe9\x80\x9a'
        b'\xe7\xb4\x9a <strong>2500-3500\xe5\x85\x83</strong>\xef\xbc\x8c\xe7\xb2\xbe'
        b'\xe9\x81\xb8\xe7\xb4\x9a <strong>3500-5000\xe5\x85\x83</strong>\xef\xbc\x8c'
        b'<strong>\xe9\xa1\x96\xe7\xb4\x9a</strong> <strong>5000-8000\xe5\x85\x83+'
        b'</strong>\xe3\x80\x82\xe4\xbd\x8e\xe6\x96\xbc\xe9\x80\x99\xe5\x80\x8b\xe8\xa1\x8c'
        b'\xe6\x83\x85\xe5\xa4\xaa\xe5\xa4\x9a\xe8\xa6\x81\xe5\xb0\x8f\xe5\xbf\x83\xe6\x9c'
        b'\x89\xe9\xac\xbc\xef\xbc\x8c\xe9\xab\x98\xe6\x96\xbc\xe5\xa4\xaa\xe5\xa4\x9a'
        b'\xe5\x8f\xaf\xe8\x83\xbd\xe6\x98\xaf\xe8\xa2\xab\xe7\x95\xb6\xe7\x9b\x86\xe5'
        b'\xad\x90\xef\xbc\x81</p>'
    )

    new_hero_p = (
        b'<p class="mb-0">2026\xe5\xb9\xb4\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\xb3'
        b'\xe6\x92\xad\xe8\xa1\x8c\xe6\x83\x85\xef\xbc\x9a\xe5\x9f\xba\xe7\xa4\x8e'
        b'\xe7\xb4\x9a <strong>NT\$2,400/2\xe5\xb0\x8f\xe6\x99\x82</strong>\xef\xbc\x8c'
        b'\xe6\xa8\x99\xe6\xba\x96\xe7\xb4\x9a <strong>NT\$3,600/2\xe5\xb0\x8f\xe6\x99\x82'
        b'</strong>\xef\xbc\x8c<strong>VIP</strong> <strong>NT\$4,000/2\xe5\xb0\x8f\xe6\x99\x82'
        b'</strong>\xef\xbc\x8c<strong>\xe9\xa0\x82\xe7\xb4\x9a</strong> <strong>'
        b'NT\$5,000+/2\xe5\xb0\x8f\xe6\x99\x82</strong>\xe3\x80\x82\xe4\xbd\x8e\xe6\x96\xbc'
        b'\xe9\x80\x99\xe5\x80\x8b\xe8\xa1\x8c\xe6\x83\x85\xe5\xa4\xaa\xe5\xa4\x9a'
        b'\xe8\xa6\x81\xe5\xb0\x8f\xe5\xbf\x83\xe6\x9c\x89\xe9\xac\xbc\xef\xbc\x8c'
        b'\xe9\xab\x98\xe6\x96\xbc\xe5\xa4\xaa\xe5\xa4\x9a\xe5\x8f\xaf\xe8\x83\xbd'
        b'\xe6\x98\xaf\xe8\xa2\xab\xe7\x95\xb6\xe7\x9b\x86\xe5\xad\x90\xef\xbc\x81</p>'
    )

    pos = raw.find(old_hero_p)
    log_write(f'old_hero_p found at: {pos}')
    if pos >= 0:
        raw = raw.replace(old_hero_p, new_hero_p, 1)
        log_write('Replaced: Hero <p>')
        changes = 1
    else:
        log_write('old_hero_p NOT found - checking individual bytes')
        changes = 0

    # === H3 tags ===
    # From _v5 hex: the H3 tags are NOT in the same byte range as the Hero
    # Let's find them by searching for the known byte patterns

    # H3 普通級
    h3_old1 = b'<h3>1. \xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xef\xbc\x9a2500-3500\xe5\x85\x83\xef\xbc\x88\xe5\x85\xa5\xe9\x96\x80\xe9\xa6\x96\xe9\x81\xb9\xef\xbc\x89</h3>'
    h3_new1 = b'<h3>1. \xe5\x9f\xba\xe7\xa4\x8e\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT\$2,400/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT\$1,200/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'
    pos = raw.find(h3_old1)
    log_write(f'H3 普通級 at: {pos}')
    if pos >= 0:
        raw = raw.replace(h3_old1, h3_new1)
        log_write('Replaced: H3 普通級')
        changes += 1

    # H3 精選級
    h3_old2 = b'<h3>2. \xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xef\xbc\x9a3500-5000\xe5\x85\x83\xef\xbc\x88\xe5\xb8\x82\xe5\xa0\xb4\xe4\xb8\xbb\xe6\xb5\x81\xef\xbc\x89</h3>'
    h3_new2 = b'<h3>2. \xe6\xa8\x99\xe6\xba\x96\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT\$3,600/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT\$1,800/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'
    pos = raw.find(h3_old2)
    log_write(f'H3 精選級 at: {pos}')
    if pos >= 0:
        raw = raw.replace(h3_old2, h3_new2)
        log_write('Replaced: H3 精選級')
        changes += 1

    # H3 VIP
    h3_old3 = b'<h3>3. VIP\xef\xbc\x9a4000-6000\xe5\x85\x83/\xe5\xb0\x8f\xe6\x99\x82</h3>'
    h3_new3 = b'<h3>3. VIP \xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT\$4,000/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT\$2,000/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'
    pos = raw.find(h3_old3)
    log_write(f'H3 VIP at: {pos}')
    if pos >= 0:
        raw = raw.replace(h3_old3, h3_new3)
        log_write('Replaced: H3 VIP')
        changes += 1

    # H3 頂級 (3. 頂級)
    h3_old4 = b'<h3>3. \xe9\xa1\x96\xe7\xb4\x9a\xef\xbc\x9a5000-8000\xe5\x85\x83\xe4\xbb\x8a\xe4\xb8\x8a\xef\xbc\x88\xe5\xb0\x8a\xe5\x8b\x81\xe4\xba\xab\xe4\xba\xab\xe5\x8f\x97\xef\xbc\x89</h3>'
    h3_new4 = b'<h3>4. \xe9\xa0\x82\xe7\xb4\x9a\xe5\x85\xac\xe9\x97\xb4\xef\xbc\x9aNT\$5,000+/2\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x88\xe2\x88\x88NT\$2,500+/\xe5\xb0\x8f\xe6\x99\x82\xef\xbc\x89</h3>'
    pos = raw.find(h3_old4)
    log_write(f'H3 頂級 at: {pos}')
    if pos >= 0:
        raw = raw.replace(h3_old4, h3_new4)
        log_write('Replaced: H3 頂級')
        changes += 1

    # dateModified
    import re, datetime
    today = datetime.date.today().isoformat()
    new_dm = f'"dateModified": "{today}"'.encode('utf-8')
    raw, n = re.subn(rb'"dateModified": "[^"]+"', new_dm, raw)
    if n:
        log_write(f'Replaced dateModified ({n})')
        changes += 1

    # Write back
    with open(PATH, 'wb') as f:
        f.write(raw)
    log_write(f'\nTotal changes: {changes}')

    # Final verification
    html = raw.decode('utf-8', errors='replace')
    log_write(f'普通級: {html.count("普通級")}')
    log_write(f'精選級: {html.count("精選級")}')
    log_write(f'基礎公關: {html.count("基礎公關")}')
    log_write(f'標準公關: {html.count("標準公關")}')
    log_write(f'VIP 公關: {html.count("VIP 公關")}')
    log_write(f'頂級公關: {html.count("頂級公關")}')
    log_write(f'2,400/2小時: {html.count("2,400/2小時")}')
    log_write(f'3,600/2小時: {html.count("3,600/2小時")}')
    log_write(f'4,000/2小時: {html.count("4,000/2小時")}')
    log_write(f'5,000+/2小時: {html.count("5,000+/2小時")}')
    log_write(f'2500-3500: {html.count("2500-3500")}')
    log_write(f'3500-5000: {html.count("3500-5000")}')
    log_write(f'5000-8000: {html.count("5000-8000")}')
