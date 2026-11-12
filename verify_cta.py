with open('compare-girls.html', 'r', encoding='utf-8') as f:
    c = f.read()

checks = ['平均30分鐘到府', 'LINE 預約，享保障', '98%', '打槍換人', '選擇歐巴傳播', 'LINE_click']
for kw in checks:
    status = '+' if kw in c else '-'
    print(f'[{status}] {kw}')

old_copy = ['LINE 快速預約', 'LINE 諮詢']
for kw in old_copy:
    status = 'STILL' if kw in c else 'REMOVED'
    print(f'[{status}] old: {kw}')
