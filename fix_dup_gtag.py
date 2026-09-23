"""移除 3 頁 PageView 追蹤區塊內重複的 gtag config（頁內 JS 冗餘宣告）
保留頁內自訂事件（如 updateCalc / scroll 追蹤），僅移除重複的
  function gtag(){...}gtag('js',new Date());gtag('config','G-534539378');
這種整段重宣告。
"""
import re

files = ['2026-pricing-table.html', 'beginners-checklist.html', 'private-party-guide.html']

# 比對頁內重複宣告：從 "window.dataLayer" 或 "=window.dataLayer||[];" 起到 config 結束
PAT = re.compile(
    r"(?:\w+\s*=\s*)?window\.dataLayer\s*\|\|\s*\[\s*\]\s*;\s*"
    r"function\s+gtag\s*\(\s*\)\s*\{\s*dataLayer\.push\(arguments\)\s*\}\s*"
    r"gtag\(\s*'js'\s*,\s*new\s+Date\(\)\s*\)\s*;\s*"
    r"gtag\(\s*'config'\s*,\s*'G-534539378'\s*\)\s*;\s*"
)

for fn in files:
    t = open(fn, encoding='utf-8').read()
    m = PAT.search(t)
    if not m:
        print(f'MISS  {fn} 找不到可移除區塊')
        continue
    snip = t[m.start():m.end()]
    new = t[:m.start()] + t[m.end():]
    # 驗證：config 應剩 1 次，loader 仍 1 次
    cfg = len(re.findall(r"gtag\('config',\s*'G-534539378'\)", new))
    ldr = len(re.findall(r'gtag/js\?id=G-534539378', new))
    if cfg != 1 or ldr != 1:
        print(f'ABORT {fn} 驗證失敗 cfg={cfg} ldr={ldr}')
        continue
    with open(fn, 'w', encoding='utf-8', newline='') as f:
        f.write(new)
    print(f'OK    {fn}  移除 {len(snip)} 字元  (cfg={cfg}, ldr={ldr})')
    print(f'      移除內容: {snip[:110]!r}...')
