# _fix_final.py — Byte-level replacement for pricing-guide-2026.html
import datetime
today = datetime.date.today().isoformat()

with open('pricing-guide-2026.html', 'rb') as f:
    raw = f.read()

html = raw.decode('utf-8', errors='replace')

# Check current state
print('普通級 occurrences:', html.count('普通級'))
print('精選級 occurrences:', html.count('精選級'))
print('2500-3500元 occurrences:', html.count('2500-3500元'))
print('3500-5000元 occurrences:', html.count('3500-5000元'))
print('5000-8000元 occurrences:', html.count('5000-8000元'))

# === REPLACEMENTS ===

# 1. Hero 行情摘要 (p class="mb-0")
old1 = '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
new1 = '年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
html = html.replace(old1, new1, 1)

# 2. 普通級 H3
old2 = '<h3>1. 普通級：2500-3500元（入門首選）</h3>'
new2 = '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>'
html = html.replace(old2, new2)

# 3. 精選級 H3
old3 = '<h3>2. 精選級：3500-5000元（市場主流）</h3>'
new3 = '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>'
html = html.replace(old3, new3)

# 4. VIP H3
old4 = '<h3>3. VIP：4000-6000元/小時</h3>'
new4 = '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>'
html = html.replace(old4, new4)

# 5. 頂級 H3
old5 = '<h3>3. 頂級：5000-8000元以上（尊榮享受）</h3>'
new5 = '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>'
html = html.replace(old5, new5)

# 6. FAQ JSON-LD
old6 = '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"'
new6 = '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'
html = html.replace(old6, new6)

# 7. 飯局妹 FAQ
old7 = '>飯局妹的收費行情大概在<strong>3000-10000元</strong>之間'
new7 = '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間'
html = html.replace(old7, new7)

# 8. 飯局表 3000-10000元
old8 = '>3000-10000元<'
new8 = '>NT$4,000-8,000元<'
html = html.replace(old8, new8)

# 9. 普通級描述段落
html = html.replace('<p>普通級是很多第一次接觸傳播服務的人的首選', '<p>基礎公關是很多第一次接觸傳播服務的人的首選')
html = html.replace('<p>普通級的傳播妹，外型條件中等，但親和力通常不錯', '<p>基礎公關，外型條件中等，但親和力通常不錯')

# 10. 精選級描述段落
html = html.replace('<p>精選級是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的傳播妹通常是：', '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：')
html = html.replace('<p>精選級的傳播小姐服務品質穩定', '<p>標準公關服務品質穩定')

# 11. dateModified
import re
html = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', html)

# Write back
with open('pricing-guide-2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('\nAfter replacement:')
print('普通級 occurrences:', html.count('普通級'))
print('精選級 occurrences:', html.count('精選級'))
print('2500-3500元 occurrences:', html.count('2500-3500元'))
print('3500-5000元 occurrences:', html.count('3500-5000元'))
print('5000-8000元 occurrences:', html.count('5000-8000元'))
print()
print('基礎公關 occurrences:', html.count('基礎公關'))
print('標準公關 occurrences:', html.count('標準公關'))
print('VIP 公關 occurrences:', html.count('VIP 公關'))
print('頂級公關 occurrences:', html.count('頂級公關'))
print('2,400/2小時 occurrences:', html.count('2,400/2小時'))
print('3,600/2小時 occurrences:', html.count('3,600/2小時'))
print('4,000/2小時 occurrences:', html.count('4,000/2小時'))
print('5,000+/2小時 occurrences:', html.count('5,000+/2小時'))
