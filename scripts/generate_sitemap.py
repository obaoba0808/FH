#!/usr/bin/env python3
"""
OBAOBA sitemap 產生器
自動掃描所有 HTML 頁面並產生 sitemap.xml
"""

import glob
import os
from datetime import datetime

SITE_DIR = 'C:/tmp/obaoba_marketing/FH'
os.chdir(SITE_DIR)

# 排除的頁面
EXCLUDE = {
    'b1xb689gu3wgchds0j20dytklnhzda.html',  # FB 驗證檔
}

# 優先級設定
PRIORITY = {
    '': '1.0',           # 首頁
    'news.html': '0.9',
    'faq-all-in-one.html': '0.9',
    'pricing-guide-2026.html': '0.9',
    'safety-guide-2026.html': '0.9',
    'privacy-policy.html': '0.3',
    'terms-of-service.html': '0.3',
}

pages = sorted(glob.glob('*.html'))
pages = [p for p in pages if p not in EXCLUDE]

today = datetime.now().strftime('%Y-%m-%d')

lines = ['<?xml version="1.0" encoding="UTF-8"?>']
lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
lines.append('  <!-- 首頁 -->')
lines.append('  <url>')
lines.append('    <loc>https://obaoba.online/</loc>')
lines.append(f'    <lastmod>{today}</lastmod>')
lines.append('    <changefreq>weekly</changefreq>')
lines.append('    <priority>1.0</priority>')
lines.append('  </url>')

for p in pages:
    if p == 'index.html':
        continue  # 首頁已用根網址
    priority = PRIORITY.get(p, '0.7')
    lines.append('  <url>')
    lines.append(f'    <loc>https://obaoba.online/{p}</loc>')
    lines.append(f'    <lastmod>{today}</lastmod>')
    lines.append('    <changefreq>monthly</changefreq>')
    lines.append(f'    <priority>{priority}</priority>')
    lines.append('  </url>')

lines.append('</urlset>')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')

print(f'✅ sitemap.xml 已更新：{len(pages)} 個頁面')
print(f'日期：{today}')
