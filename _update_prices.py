# _update_prices.py — 更新 how_much.html 和 pricing-guide-2026.html 收費行情
import re

# ── how_much.html ──────────────────────────────────────
hm = open('how_much.html', encoding='utf-8').read()

# 1. Meta descriptions (og:description 也跟著)
hm = hm.replace(
    '了解台北傳播妹收費行情：公關 NT$1,200/小時、保三 NT$1,500-1,800/小時、VIP NT$2,000-2,500/小時，含鐘點費計算方式與打槍換人保障制度詳細說明。',
    '了解台北傳播妹收費行情：基礎 NT$2,400/2小時、標準 NT$3,600/2小時、VIP NT$4,000/2小時、頂級 NT$5,000+/2小時，含收費項目說明與打槍換人保障制度。'
)
hm = hm.replace(
    '拒絕當冤大頭！全面解析公關、保三、VIP等級計費標準。',
    '拒絕當冤大頭！2026年行情：基礎 NT$2,400起，標準 NT$3,600，頂級 NT$5,000以上。'
)

# 2. 開場引導段落 (第219行附近)
hm = hm.replace(
    '行情約為每小時 NT$1,200 至 NT$2,500 不等，取決於等級（公關、保三、VIP）',
    '行情約為每2小時 NT$2,400 至 NT$5,000 以上不等，取決於等級（基礎、標準、VIP、頂級）'
)

# 3. 第二段行情說明
hm = hm.replace(
    '行情價約 <strong>NT$1,200-1,500/小時</strong>（一般公關等級），保三等級約 NT$1,500-2,000/小時，VIP 等級 NT$2,000-2,500/小時',
    '行情價約 <strong>NT$2,400/2小時</strong>（基礎公關），標準公關約 NT$3,600/2小時，VIP 等級 NT$4,000/2小時，頂級 NT$5,000+/2小時'
)
hm = hm.replace(
    '台北傳播妹（傳播小姐）的行情價約 <strong>NT$2,400-3,000/2小時</strong>',
    '台北傳播妹（傳播小姐）的行情價約 <strong>NT$2,400/2小時</strong>'
)

# 4. 等級列表 (226-228行)
hm = hm.replace(
    '<li><strong>公關等級：</strong> 約 NT$1,200/小時。適合一般 KTV 歡唱帶動氣氛，活潑大方。</li>',
    '<li><strong>基礎公關：</strong> NT$2,400/2小時，約 NT$1,200/小時。適合一般 KTV 歡唱帶動氣氛，活潑大方。</li>'
)
hm = hm.replace(
    '<li><strong>保三等級：</strong> 約 NT$1,500 - 1,800/小時。顏值與身材經過嚴選，適合商務應酬或派對撐場面。</li>',
    '<li><strong>標準公關：</strong> NT$3,600/2小時，約 NT$1,800/小時。顏值與身材經過嚴選，適合商務應酬或派對撐場面。</li>'
)
hm = hm.replace(
    '<li><strong>VIP 模特等級：</strong> NT$2,000 以上/小時。擁有極高顏值或網紅等級，帶出門絕對有面子。</li>',
    '<li><strong>VIP 公關：</strong> NT$4,000/2小時，約 NT$2,000/小時。擁有極高顏值或網紅等級，帶出門絕對有面子。</li>'
)
# 補頂級
hm = hm.replace(
    '<li><strong>VIP 公關：</strong> NT$4,000/2小時，約 NT$2,000/小時。擁有極高顏值或網紅等級，帶出門絕對有面子。</li>',
    '<li><strong>VIP 公關：</strong> NT$4,000/2小時，約 NT$2,000/小時。擁有極高顏值或網紅等級，帶出門絕對有面子。</li>\n                        <li><strong>頂級公關：</strong> NT$5,000+/2小時，約 NT$2,500+/小時。業界最高規格，模特兒或藝人等級，適合重要商務場合。</li>'
)

# 5. 隱藏費用段落 (241行)
hm = hm.replace(
    '依等級每小時 NT$1,200-2,500',
    '依等級每2小時 NT$2,400-5,000+'
)

# 6. 段落比價 (258行)
hm = hm.replace(
    '<strong>公關（General）</strong>NT$1,200-1,400/小時，適合 KTV 歡唱帶動氣氛；<strong>保三</strong>NT$1,500-1,800/小時，顏值',
    '<strong>基礎公關</strong>NT$2,400/2小時，適合 KTV 歡唱帶動氣氛；<strong>標準公關</strong>NT$3,600/2小時，顏值'
)
hm = hm.replace(
    '；<strong>VIP 等級</strong>NT$2,000-2,500/小時，模特兒等級、適合商務場合',
    '；<strong>VIP 公關</strong>NT$4,000/2小時；<strong>頂級公關</strong>NT$5,000+/2小時，模特兒等級、適合商務場合'
)

# 7. 比較表格 (274, 282, 290行)
hm = hm.replace(
    '<td class="py-3 px-4">NT$1,200 – 1,400</td>',
    '<td class="py-3 px-4">NT$2,400 / 2小時（≈NT$1,200/小時）</td>'
)
hm = hm.replace(
    '<td class="py-3 px-4">NT$1,500 – 1,800</td>',
    '<td class="py-3 px-4">NT$3,600 / 2小時（≈NT$1,800/小時）</td>'
)
hm = hm.replace(
    '<td class="py-3 px-4">NT$2,000 – 2,500+</td>',
    '<td class="py-3 px-4">NT$4,000+ / 2小時（≈NT$2,000+/小時）</td>'
)
# 頂級 row
old_tr_vip = '<tr>\n                        <td class="py-3 px-4"><strong>VIP 等級</strong></td>\n                        <td class="py-3 px-4">NT$2,000 – 2,500+</td>'
new_tr_vip = '<tr>\n                        <td class="py-3 px-4"><strong>VIP 公關</strong></td>\n                        <td class="py-3 px-4">NT$4,000+ / 2小時（≈NT$2,000+/小時）</td>\n                    </tr>\n                    <tr>\n                        <td class="py-3 px-4"><strong>頂級公關</strong></td>\n                        <td class="py-3 px-4">NT$5,000+ / 2小時（≈NT$2,500+/小時）</td>'
hm = hm.replace(old_tr_vip, new_tr_vip)

# 8. FAQ JSON-LD 更新
hm = hm.replace(
    '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"',
    '"text": "2026年台北傳播行情：基礎 NT$2,400/2小時、標準 NT$3,600/2小時、VIP NT$4,000/2小時、頂級 NT$5,000+/2小時。鐘點費+車馬費，無隱藏費用。"'
)

# 9. FAQ JSON-LD 飯局費用
hm = hm.replace(
    '"text": "飯局妹費用行情為每小時NT$2,000-3,000元，全程（3-5小時）約NT$8,000-12,000元。實際費用依公關等級與場合需求而異。',
    '"text": "飯局妹以場次計算，約 NT$4,000-8,000/場（2-4小時），含交通補貼。歐巴傳播提供商務場合專業公關，預約請洽 LINE。'
)

# 10. dateModified
import datetime
today = datetime.date.today().isoformat()
hm = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', hm)

open('how_much.html', 'w', encoding='utf-8').write(hm)
print('how_much.html: OK')


# ── pricing-guide-2026.html ──────────────────────────────
pg = open('pricing-guide-2026.html', encoding='utf-8').read()

# 1. Meta descriptions
pg = pg.replace(
    '2026年台北傳播收費行情完整攻略！普通級、精選級、頂級費用一次看，KTV傳播、飯局妹、汽車旅館傳播行情全公開。內行人教你如何選對服務不花冤枉錢！',
    '2026年台北傳播收費行情完整攻略！基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。KTV傳播、飯局妹、汽車旅館行情全公開，拒絕被當冤大頭！'
)
pg = pg.replace(
    '2026年台北傳播收費行情完整攻略！普通級、精選級、頂級費用一次看。',
    '2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。'
)

# 2. 開場白行情摘要 (353行)
pg = pg.replace(
    '2026年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>',
    '2026年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，VIP <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>'
)

# 3. 等級標題 (普通級/精選級/頂級 → 基礎/標準/VIP/頂級)
pg = pg.replace('<h3>1. 普通級：1500-2500元/小時</h3>', '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>')
pg = pg.replace('<h3>2. 精選級：2500-4000元/小時</h3>', '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>')
pg = pg.replace('<h3>3. VIP：4000-6000元/小時</h3>', '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>')
pg = pg.replace('<h3>3. 頂級：5000-8000元以上（尊榮享受）</h3>', '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>')

# 4. 頂級敘述段落 (384行)
pg = pg.replace(
    '頂級傳播妹可能是模特兒、網紅等級，或是業界資深的王牌小姐。她們<strong>懂得察言觀色',
    '頂級公關可能是模特兒、網紅等級，或是業界資深的王牌小姐。她們<strong>懂得察言觀色'
)

# 5. FAQ JSON-LD
pg = pg.replace(
    '"text": "2026年台北傳播行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"',
    '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時。實際費用依等級、地點而異。"'
)
pg = pg.replace(
    '"text": "KTV傳播以小時計費，飯局妹則以場次計算。KTV傳播適合包廂聚會，飯局妹適合商務餐敘，兩者服務模式不同，收費標準也不同。"',
    '"text": "KTV傳播以2小時計費（NT$2,400起），飯局妹以場次計算（NT$4,000-8,000/場）。KTV傳播適合包廂聚會，飯局妹適合商務餐敘，兩者服務模式不同，收費標準也不同。"'
)
pg = pg.replace(
    '"text": "選擇有透明收費標準的傳播公司，比較市場行情，避免價格過低或過高。優質傳播公司的收費會在合理區間內，並提供完善的服務保障。"',
    '"text": "選擇有透明收費標準的傳播公司，歐巴傳播基礎 NT$2,400/2小時起，標準 NT$3,600，頂級 NT$5,000+，鐘點費+車馬費，絕無隱藏費用，提供打槍換人保障。"'
)

# 6. 小費說明
pg = pg.replace(
    '<p>小費是<strong>看滿意度決定</strong>，不是強制的。參考標準：普通服務500-1000元，滿意服務1000-2000元，非常滿意2000-3000元以上。如果你真的很滿意，小費是對傳播小姐的肯定。</p>',
    '<p>小費是<strong>看滿意度決定</strong>，不是強制的。參考標準：普通服務 NT$500-1,000元，滿意服務 NT$1,000-2,000元，非常滿意 NT$2,000-3,000元以上。如果你真的很滿意，小費是對公關的肯定。</p>'
)

# 7. FAQ 答案文字 (505, 514行)
pg = pg.replace(
    '台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異，建議事先詢問清楚。',
    '2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。鐘點費+車馬費，無隱藏費用，建議事先詢問清楚。'
)
pg = pg.replace(
    'KTV傳播以小時計費，適合包廂聚會；飯局妹則以場次計算，適合商務餐敘。兩者服務模式不同，收費標準也不同。飯局妹通常會有交通補貼費用。',
    'KTV傳播以2小時計費（NT$2,400起），飯局妹以場次計算（NT$4,000-8,000/場，含交通補貼）。兩者服務模式不同，收費標準也不同。'
)

# 8. dateModified
pg = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', pg)

open('pricing-guide-2026.html', 'w', encoding='utf-8').write(pg)
print('pricing-guide-2026.html: OK')
print(f'Date updated to: {today}')
