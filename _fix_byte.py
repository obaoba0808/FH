# _fix_byte.py — Byte-level replacement
with open('pricing-guide-2026.html', 'rb') as f:
    raw = f.read()

# The actual old bytes around 普通級
old_bytes = (
    b'<p class="mb-0">2026\xe5\xb9\xb4\xe5\x8f\xb0\xe5\x8c\x97\xe5\x82\'
    b'\xb3\xe6\x92\xad\xe8\xa1\x8c\xe6\x83\x85\xef\xbc\x9a\xe6\x99\xae'
    b'\xe9\x80\x9a\xe7\xb4\x9a <strong>2500-3500\xe5\x85\x83</strong>'
    b'\xef\xbc\x8c\xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a <strong>3500-5000'
    b'\xe5\x85\x83</strong>\xef\xbc\x8c<strong>\xe9\xa1\x96\xe7\xb4\x9a'
    b'</strong> <strong>5000-8000\xe5\x85\x83+</strong>\xe3\x80\x82\xe4\xbd'
    b'\x8e\xe6\x96\xbc\xe9\x80\x99\xe5\x80\x8b\xe8\xa1\x8c\xe6\x83\x85'
    b'\xe5\xa4\xaa\xe5\xa4\x9a\xe8\xa6\x81\xe5\xb0\x8f\xe5\xbf\x83\xe6'
    b'\x9c\x89\xe9\xac\xbc\xef\xbc\x8c\xe9\xab\x98\xe6\x96\xbc\xe5\xa4'
    b'\xaa\xe5\xa4\x9a\xe5\x8f\xaf\xe8\x83\xbd\xe6\x98\xaf\xe8\xa2\xab'
    b'\xe7\x95\xb6\xe7\x9b\x86\xe5\xad\x90\xef\xbc\x81</p>'
)

new_str = (
    '<p class="mb-0">2026年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！</p>'
)

idx = raw.find(old_bytes)
print('old_bytes found at:', idx)
if idx >= 0:
    new_bytes = new_str.encode('utf-8')
    raw = raw.replace(old_bytes, new_bytes)
    print('Replaced!')
else:
    print('old_bytes NOT found — let us search what is at the rough position')
    # try to find it at rough position
    rough = raw.find(b'2500-3500\xe5\x85\x83')
    print('rough find 2500-3500 at:', rough)
    if rough >= 0:
        print(repr(raw[rough-100:rough+200]))

# Now fix H3 tags - find the section around line 370 (after the price summary)
# The issue: H3 tags have fullwidth parentheses (（...）) vs (...
# Let's check
h3_old1 = b'<h3>1. \xe6\x99\xae\xe9\x80\x9a\xe7\xb4\x9a\xef\xbc\x9a2500-3500\xe5\x85\x83\xef\xbc\x88\xe5\x85\xa5\xe9\x96\x80\xe9\xa6\x96\xe9\x81\xb9\xef\xbc\x89</h3>'
h3_idx = raw.find(h3_old1)
print('H3 普通級 found at:', h3_idx)
if h3_idx < 0:
    # try without parentheses
    h3_rough = raw.find(b'2500-3500\xe5\x85\x83\xef\xbc\x88')
    print('H3 2500 rough at:', h3_rough)
    if h3_rough >= 0:
        print(repr(raw[h3_rough-20:h3_rough+100]))

# H3 精選級
h3_old2 = b'<h3>2. \xe7\xb2\xbe\xe9\x81\xb8\xe7\xb4\x9a\xef\xbc\x9a3500-5000\xe5\x85\x83\xef\xbc\x88\xe5\xb8\x82\xe5\xa0\xb4\xe4\xb8\xbb\xe6\xb5\x81\xef\xbc\x89</h3>'
h3_idx2 = raw.find(h3_old2)
print('H3 精選級 found at:', h3_idx2)

# H3 VIP
h3_vip = b'<h3>3. VIP\xef\xbc\x9a4000-6000\xe5\x85\x83/\xe5\xb0\x8f\xe6\x99\x82</h3>'
h3_vip_idx = raw.find(h3_vip)
print('H3 VIP found at:', h3_vip_idx)
if h3_vip_idx < 0:
    # try different encoding
    vip_rough = raw.find(b'4000-6000')
    print('VIP rough at:', vip_rough)
    if vip_rough >= 0:
        print(repr(raw[vip_rough-50:vip_rough+80]))

# H3 頂級
h3_top = b'<h3>3. \xe9\xa1\x96\xe7\xb4\x9a\xef\xbc\x9a5000-8000\xe5\x85\x83\xe4\xbb\x8a\xe4\xb8\x8a\xef\xbc\x88\xe5\xb0\x8a\xe5\u5b81\xe4\xba\xab\xe4\xba\xab\xe5\x8f\x97\xef\xbc\x89</h3>'
h3_top_idx = raw.find(h3_top)
print('H3 頂級 found at:', h3_top_idx)

with open('pricing-guide-2026.html', 'wb') as f:
    f.write(raw)
