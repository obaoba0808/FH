# _fix_v3.py — Byte-level search then UTF-8 decode to verify, then replace
with open('pricing-guide-2026.html', 'rb') as f:
    raw = f.read()

html = raw.decode('utf-8', errors='replace')

# Helper: find byte position, then decode to UTF-8 for context
def show_utf8_context(haystack_raw, needle_utf8, label):
    pos = haystack_raw.find(needle_utf8.encode('utf-8'))
    if pos >= 0:
        ctx = haystack_raw[pos:pos+80].decode('utf-8', errors='replace')
        return pos, ctx
    return -1, None

# 1. Hero
needle = '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
pos, ctx = show_utf8_context(raw, needle, 'Hero')
print(f'Hero: pos={pos}')
if pos >= 0:
    print(f'  ctx: {repr(ctx)}')

# Check the exact character
idx = html.find('普通級')
print(f'普通級 in html at: {idx}')
if idx >= 0:
    print(f'  html ctx: {repr(html[idx-10:idx+60])}')

# Try using the exact bytes found by PowerShell
# PowerShell found: '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，頂級 <strong>5000-'
# In PowerShell this is UTF-16LE encoded string
# Let's just do the replacement by finding the byte position

# Find bytes of the whole hero line in raw
hero_start_b = html.index('年台北傳播行情：普通級')
hero_line_start = html.rfind('\n', 0, hero_start_b) + 1
hero_line_end = html.index('\n', hero_start_b)
hero_line = html[hero_line_start:hero_line_end]
print(f'\nHero line ({hero_line_start}-{hero_line_end}):')
print(repr(hero_line))

# Find the <p class="mb-0"> surrounding
p_start = html.rfind('<p class="mb-0">', 0, hero_line_start)
p_end = html.index('</p>', hero_line_end)
p_content = html[p_start:p_end+4]
print(f'\n<p> block ({p_start}-{p_end+4}):')
print(repr(p_content))
