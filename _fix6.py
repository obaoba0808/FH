# _fix6.py — Pricing update using confirmed exact strings
import re, datetime, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('pricing-guide-2026.html', 'r', encoding='utf-8') as f:
    html = f.read()

today = datetime.date.today().isoformat()
changes = 0

# 1. Hero 行情摘要 (exact confirmed)
OLD1 = '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
NEW1 = '年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
if OLD1 in html:
    html = html.replace(OLD1, NEW1, 1)
    changes += 1

# 2. H3 普通級
OLD2 = '<h3>1. 普通級：2500-3500元（入門首選）</h3>'
NEW2 = '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>'
if OLD2 in html:
    html = html.replace(OLD2, NEW2)
    changes += 1

# 3. H3 精選級
OLD3 = '<h3>2. 精選級：3500-5000元（市場主流）</h3>'
NEW3 = '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>'
if OLD3 in html:
    html = html.replace(OLD3, NEW3)
    changes += 1

# 4. H3 VIP
OLD4 = '<h3>3. VIP：4000-6000元/小時</h3>'
NEW4 = '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>'
if OLD4 in html:
    html = html.replace(OLD4, NEW4)
    changes += 1

# 5. H3 頂級
OLD5 = '<h3>3. 頂級：5000-8000元以上（尊榮享受）</h3>'
NEW5 = '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>'
if OLD5 in html:
    html = html.replace(OLD5, NEW5)
    changes += 1

# 6. FAQ JSON-LD
OLD6 = '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"'
NEW6 = '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'
if OLD6 in html:
    html = html.replace(OLD6, NEW6)
    changes += 1

# 7. 飯局妹 FAQ
OLD7 = '>飯局妹的收費行情大概在<strong>3000-10000元</strong>之間'
NEW7 = '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間'
if OLD7 in html:
    html = html.replace(OLD7, NEW7)
    changes += 1

# 8. 飯局表 3000-10000
OLD8 = '>3000-10000元<'
NEW8 = '>NT$4,000-8,000元<'
if OLD8 in html:
    html = html.replace(OLD8, NEW8)
    changes += 1

# 9. 普通級段落
OLD9 = '<p>普通級是很多第一次接觸傳播服務的人的首選'
NEW9 = '<p>基礎公關是很多第一次接觸傳播服務的人的首選'
if OLD9 in html:
    html = html.replace(OLD9, NEW9)
    changes += 1

# 10. 普通級 描述
OLD10 = '<p>普通級的傳播妹，外型條件中等，但親和力通常不錯'
NEW10 = '<p>基礎公關，外型條件中等，但親和力通常不錯'
if OLD10 in html:
    html = html.replace(OLD10, NEW10)
    changes += 1

# 11. 精選級段落1
OLD11 = '<p>精選級是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的傳播妹通常是：'
NEW11 = '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：'
if OLD11 in html:
    html = html.replace(OLD11, NEW11)
    changes += 1

# 12. 精選級段落2
OLD12 = '<p>精選級的傳播小姐服務品質穩定'
NEW12 = '<p>標準公關服務品質穩定'
if OLD12 in html:
    html = html.replace(OLD12, NEW12)
    changes += 1

# 13. dateModified
html = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', html)
changes += 1

with open('pricing-guide-2026.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Report
with open('pricing-guide-2026.html', 'r', encoding='utf-8') as f:
    pg = f.read()

with open('_fix_report.txt', 'w', encoding='utf-8') as out:
    out.write(f'Changes made: {changes}\n')
    out.write(f'普通級: {pg.count("普通級")}\n')
    out.write(f'精選級: {pg.count("精選級")}\n')
    out.write(f'2500-3500元: {pg.count("2500-3500元")}\n')
    out.write(f'3500-5000元: {pg.count("3500-5000元")}\n')
    out.write(f'5000-8000元: {pg.count("5000-8000元")}\n')
    out.write(f'基礎公關: {pg.count("基礎公關")}\n')
    out.write(f'標準公關: {pg.count("標準公關")}\n')
    out.write(f'VIP 公關: {pg.count("VIP 公關")}\n')
    out.write(f'頂級公關: {pg.count("頂級公關")}\n')
