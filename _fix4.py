import re, datetime
today = datetime.date.today().isoformat()

pg = open('pricing-guide-2026.html', encoding='utf-8').read()

# 1. 開場行情摘要（p class="mb-0"）
pg = re.sub(
    r'年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元\+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！',
    '年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！',
    pg
)

# 2. 普通級 H3 (with 全形括號)
pg = pg.replace('<h3>1. 普通級：2500-3500元（入門首選）</h3>', '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>')

# 3. 精選級 H3
pg = pg.replace('<h3>2. 精選級：3500-5000元（市場主流）</h3>', '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>')

# 4. VIP H3
pg = pg.replace('<h3>3. VIP：4000-6000元/小時</h3>', '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>')

# 5. 頂級 H3 (both variations)
pg = pg.replace('<h3>3. 頂級：5000-8000元以上（尊榮享受）</h3>', '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>')

# 6. FAQ JSON-LD 行情
pg = pg.replace(
    '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"',
    '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'
)

# 7. 飯局妹 FAQ
pg = pg.replace('>飯局妹的收費行情大概在<strong>3000-10000元</strong>之間', '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間')

# 8. 飯局表 3000-10000
pg = pg.replace('>3000-10000元<', '>NT$4,000-8,000元<')

# 9. 普通級描述段落
pg = pg.replace('<p>普通級是很多第一次接觸傳播服務的人的首選', '<p>基礎公關是很多第一次接觸傳播服務的人的首選')
pg = pg.replace('<p>普通級的傳播妹，外型條件中等，但親和力通常不錯', '<p>基礎公關，外型條件中等，但親和力通常不錯')

# 10. 精選級描述段落
pg = pg.replace('<p>精選級是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的傳播妹通常是：', '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：')
pg = pg.replace('<p>精選級的傳播小姐服務品質穩定', '<p>標準公關服務品質穩定')

# 11. dateModified
pg = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', pg)

open('pricing-guide-2026.html', 'w', encoding='utf-8').write(pg)

# Verify
pg2 = open('pricing-guide-2026.html', encoding='utf-8').read()
print('=== Verification ===')
for p in ['普通級', '精選級', '2500-3500元', '3500-5000元', '5000-8000元']:
    idx = pg2.find(p)
    if idx >= 0:
        ctx = pg2[max(0,idx-20):idx+60]
        print('STILL FOUND:', p, ':', repr(ctx))
    else:
        print('CLEAN:', p)
print()
print('=== New patterns ===')
for p in ['基礎公關', '標準公關', 'VIP 公關', '頂級公關', '2,400/2小時', '3,600/2小時', '4,000/2小時', '5,000+/2小時']:
    idx = pg2.find(p)
    print('  ' + p + ':', 'FOUND' if idx >= 0 else 'NOT FOUND')
