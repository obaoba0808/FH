#!/usr/bin/env python3
"""
AEO Answer Schema 補強器
為「已有快速解答區塊、但缺獨立 Answer schema」的頁面補上
WebPage + Question + Answer 結構化資料
"""
import re
import json
import glob
import os

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_answer_block(html):
    """從頁面找出快速解答區塊的問題與答案"""
    # 模式 1：AI 快速解答懶人包（含 <strong>問題</strong>答案）
    m = re.search(
        r'(?:快速解答|Quick Answer|aeo-answer).*?<p[^>]*>(.*?)</p>',
        html, re.S
    )
    if not m:
        return None
    inner = m.group(1)
    inner_clean = re.sub(r'<[^>]+>', '', inner).strip()
    inner_clean = re.sub(r'\s+', ' ', inner_clean)

    # 抽出 <strong> 內的問題
    sm = re.search(r'<strong>(.*?)</strong>', inner, re.S)
    if sm:
        question = re.sub(r'<[^>]+>', '', sm.group(1)).strip()
        answer = inner_clean[len(question):].strip()
        # 去掉答案開頭可能的分隔符
        answer = re.sub(r'^[：:,\s]+', '', answer)
    else:
        # 沒有 strong，用第一人稱問句猜
        qm = re.search(r'^([^？?。]{4,40}[？?])', inner_clean)
        if qm:
            question = qm.group(1)
            answer = inner_clean[len(question):].strip()
        else:
            question = None
            answer = inner_clean

    if not answer or len(answer) < 20:
        return None
    # 答案太短時，改用 FAQ 第一個答案
    if len(answer) < 60:
        faq = re.search(
            r'"@type":\s*"FAQPage".*?"mainEntity":\s*\[(.*?)\]', html, re.S
        )
        if faq:
            fq = re.search(r'"name":\s*"([^"]+)"', faq.group(1))
            fa = re.search(r'"text":\s*"([^"]+)"', faq.group(1))
            if fq and fa and len(fa.group(1)) > len(answer):
                question = fq.group(1)
                answer = fa.group(1)
    return question, answer


def build_schema(question, answer, fname):
    """產生 WebPage + Question + Answer schema"""
    h1 = None
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": question or fname,
        "description": answer[:200],
        "mainEntity": {
            "@type": "Question",
            "name": question or fname,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer
            }
        }
    }


def has_standalone_answer(html):
    """檢查是否已有獨立 Answer schema"""
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try:
            d = json.loads(m.group(1))
            t = d.get('@type')
            if t == 'Answer':
                return True
            me = d.get('mainEntity')
            if isinstance(me, dict) and me.get('@type') == 'Question':
                return True
            if isinstance(d.get('@graph'), list):
                for n in d['@graph']:
                    if n.get('@type') == 'Answer':
                        return True
        except Exception:
            pass
    return False


def add_microdata(html):
    """為解答區塊加上 itemscope/itemtype（若還沒有）"""
    if 'itemscope itemtype="https://schema.org/Answer"' in html:
        return html
    # 找到快速解答區塊的 <p>，加上 itemprop
    def repl(m):
        block = m.group(0)
        if 'itemprop' in block:
            return block
        # 在 <p ...> 加 itemprop="text"
        block = re.sub(r'<p([^>]*)>', r'<p\1 itemprop="text">', block, count=1)
        return block
    html = re.sub(
        r'(?:快速解答|Quick Answer|aeo-answer).*?</div>',
        repl, html, count=1, flags=re.S
    )
    return html


def process(fname, html):
    if has_standalone_answer(html):
        return None, 'skip'
    found = find_answer_block(html)
    if not found:
        return None, 'no-answer'
    question, answer = found
    schema = build_schema(question, answer, fname)
    script = (
        '\n    <!-- AEO Answer Schema (auto) -->\n'
        f'    <script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>\n'
    )
    new_html = html.replace('</body>', script + '</body>')
    return new_html, 'ok'


def main():
    files = sorted(glob.glob(os.path.join(SITE_DIR, '*.html')))
    done, skipped, failed = 0, 0, []
    for f in files:
        if os.path.basename(f) == 'b1xb689gu3wgchds0j20dytklnhzda.html':
            continue
        with open(f, encoding='utf-8') as fh:
            html = fh.read()
        result, status = process(os.path.basename(f), html)
        if status == 'skip':
            skipped += 1
            continue
        if result is None:
            failed.append(os.path.basename(f))
            continue
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(result)
        done += 1
    print(f'✅ 已補上 Answer schema: {done} 頁')
    print(f'⏭️  原有跳過: {skipped} 頁')
    if failed:
        print(f'⚠️  找不到解答區: {len(failed)} 頁')
        for f in failed:
            print(f'   - {f}')


if __name__ == '__main__':
    main()
