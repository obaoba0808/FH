# _fix_v2.py — Simple string replacement using exact found strings
with open('pricing-guide-2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check what we found in _debug_find
# Context: '26年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-'
# The exact strings from the _debug_find output
OLD_HERO = '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
NEW_HERO = '年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'

if OLD_HERO in html:
    html = html.replace(OLD_HERO, NEW_HERO, 1)
    print('Hero replaced')
else:
    print('Hero NOT found, trying partial match')
    idx = html.find('2500-3500')
    print(f'2500-3500 at {idx}: {repr(html[max(0,idx-20):idx+60])}')

# H3 tags - let's find the actual text
import re
h3_matches = re.findall(r'<h3>[^<]+</h3>', html)
for m in h3_matches:
    print('H3:', repr(m))
