# _update_pricing2.py — pricing-guide-2026.html 深度清理舊行情
import re, datetime

pg = open('pricing-guide-2026.html', encoding='utf-8').read()
today = datetime.date.today().isoformat()

# 1. Article JSON-LD description
pg = pg.replace(
    '"description": "2026年台北傳播收費行情完整攻略！普通級、精選級、頂級費用一次看，KTV傳播、飯局妹、汽車旅館傳播行情全公開。",',
    '"description": "2026年台北傳播收費行情完整攻略！基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000+/2小時，KTV傳播、飯局妹、汽車旅館行情全公開。",'
)

# 2. FAQ JSON-LD 行情問答
pg = pg.replace(
    '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等等級、地點而異。"',
    '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異，建議事先詢問。"'
)

# 3. FAQ JSON-LD motel 問答 (場地費)
pg = pg.replace(
    '"text": "汽車旅館傳播費用較高，包含場地費加上小姐的服務費，整體消費約5000-12000元不等，視選擇的等級和服務內容而定。"',
    '"text": "汽車旅館傳播費用較高，小姐鐘點費 NT$2,400-5,000+/2小時，加上汽車旅館場地費 NT$1,500-5,000元，整體消費約 NT$4,000-15,000元，視等級與旅館選擇而定。"'
)

# 4. 開場行情摘要 (353行)
pg = pg.replace(
    '2026年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！',
    '2026年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，VIP <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
)

# 5. 普通級/精選級 H2 段落描述換掉
pg = pg.replace(
    '精選級是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。',
    '標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。'
)
pg = pg.replace(
    '精選級的傳播小姐服務品質穩定，<strong>適合各種場合</strong>：慶生、公司聚會、朋友聯誼、商務應酬都可以撐場面。如果你不確定要選哪個等級，選精選級就對了！',
    '標準公關服務品質穩定，<strong>適合各種場合</strong>：慶生、公司聚會、朋友聯誼、商務應酬都可以撐場面。如果你不確定要選哪個等級，選標準公關就對了！'
)

# 6. 比較表格: KTV/精緻/飯局 (行 405, 417, 423)
# 舊數字是舊制 per-person per-session range
# KTV傳播  2500-8000  →  2400-5000+
# 飯局妹   5000-12000 →  4000-8000
# 私人派對 4000-15000 →  3000-12000 (多人分攤)
pg = pg.replace('>2500-8000元<', '>NT$2,400-5,000+元<')
pg = pg.replace('>5000-12000元<', '>NT$4,000-12,000元<')
pg = pg.replace('>4000-15000元<', '>NT$3,000-15,000元<')

# 7. 飯局妹/汽車旅館 breakdown (437, 439, 464, 465)
# 飯局：2500-8000(舊)→3600-5000(新)
pg = pg.replace(
    '<li><strong>小姐服務費</strong>：根據等級，2500-8000元不等</li>',
    '<li><strong>小姐服務費</strong>：根據等級，NT$3,600-5,000元不等（2小時）</li>'
)
pg = pg.replace(
    '<li><strong>酒水費用</strong>：視消費量，1000-5000元不等</li>',
    '<li><strong>酒水費用</strong>：視消費量，NT$1,000-5,000元不等</li>'
)
# 汽車旅館：4000-10000(舊)→3600-5000(新)
pg = pg.replace(
    '<li><strong>小姐服務費</strong>：依等級，4000-10000元</li>',
    '<li><strong>小姐服務費</strong>：依等級，NT$3,600-5,000元（2小時）</li>'
)

# 8. FAQ Motel 答案 (523行)
pg = pg.replace(
    '汽車旅館傳播費用較高，包含小姐服務費加上汽車旅館場地費，整體消費約5000-12000元不等，視選擇的等級、汽車旅館等級和服務內容而定。',
    '汽車旅館傳播費用較高，小姐鐘點費 NT$2,400-5,000+/2小時，加上汽車旅館場地費 NT$1,500-5,000元，整體消費約 NT$4,000-15,000元，視等級與旅館等級而定。'
)

# 9. FAQ 飯局答案 (514行已處理，這裡補漏)
pg = pg.replace(
    'KTV傳播以2小時計費（NT$2,400起），飯局妹以場次計算（NT$4,000-8,000/場，含交通補貼）。兩者服務模式不同，收費標準也不同。',
    'KTV傳播以2小時計費（NT$2,400起），飯局妹以場次計算（NT$4,000-8,000/場，含交通補貼）。兩者服務模式不同，收費標準也不同，飯局妹通常有交通補貼。'
)

# 10. dateModified 更新
pg = re.sub(r'"dateModified": "\d{4}-\d{2}-\d{2}"', f'"dateModified": "{today}"', pg)

# 驗證：確認沒有殘留舊數字
old_patterns = ['普通級', '精選級', '2500-3500元', '3500-5000元', '5000-8000元', '普通級.*元']
hits = []
for p in old_patterns:
    for m in re.finditer(re.escape(p), pg):
        ctx = pg[max(0,m.start()-30):m.end()+30]
        if 'animation' not in ctx.lower():
            hits.append(f'  Line ~{pg[:m.start()].count(chr(10))+1}: ...{ctx}...')
if hits:
    print('WARNING - still found old patterns:')
    for h in hits[:10]:
        print(h)
else:
    print('pricing-guide-2026.html: OK (no old patterns found)')

open('pricing-guide-2026.html', 'w', encoding='utf-8').write(pg)
