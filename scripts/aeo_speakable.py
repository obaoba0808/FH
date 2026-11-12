#!/usr/bin/env python3
"""
AEO speakable schema 注入器
為頁面加上 Google AI Overviews / 語音搜尋適用的 speakable 標示
"""
import re
import json
import glob
import os

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 優先頁面（SEO 重點）
PRIORITY = [
    'index.html', 'pricing-guide-2026.html', 'how_much.html', 'safety-guide-2026.html',
    'faq-all-in-one.html', 'about-oppa.html', 'booking-guide.html', 'first-time-2026.html',
    'newbie-guide-2026.html', 'tipping-guide-2026.html', 'venue-guide-2026.html',
    'motel_safe.html', 'KTV_party.html', 'legality-guide.html', 'taipei_agency_guide.html',
]


def build_speakable(url):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": url,
        "speakable": {
            "@type": "SpeakableSpecification",
            "cssSelector": [
                "h1",
                ".aeo-answer",
                ".quick-answer",
                ".glass-panel p",
                "article p"
            ]
        }
    }


def has_speakable(html):
    return '"speakable"' in html or '"SpeakableSpecification"' in html


def main():
    files = sorted(glob.glob(os.path.join(SITE_DIR, '*.html')))
    done, skipped = 0, 0
    for f in files:
        bname = os.path.basename(f)
        if bname == 'b1xb689gu3wgchds0j20dytklnhzda.html':
            continue
        # 只處理優先頁面 + 有 aeo-answer 的頁面
        with open(f, encoding='utf-8') as fh:
            html = fh.read()
        if has_speakable(html):
            skipped += 1
            continue
        if bname not in PRIORITY and 'aeo-answer' not in html:
            continue

        url = f"https://obaoba.online/{bname}"
        schema = build_speakable(url)
        script = (
            '\n    <!-- AEO Speakable (AI Overviews / Voice) -->\n'
            f'    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n'
        )
        html = html.replace('</body>', script + '</body>')
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(html)
        done += 1

    print(f'✅ 已加上 speakable: {done} 頁')
    print(f'⏭️  已有跳過: {skipped} 頁')


if __name__ == '__main__':
    main()
