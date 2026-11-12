#!/usr/bin/env python3
"""
AEO 快速答案注入器
為每個頁面在 hero 區後加入「快速答案」區塊
- 從現有 FAQ schema 抽取第一個 Q&A
- 產生 HTML 區塊 + Answer schema
"""
import re
import json
import glob
import os

SITE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 自訂答案（針對最重要的頁面，提供最佳化答案）
CUSTOM_ANSWERS = {
    'index.html': '歐巴傳播是台北專業傳播公司，提供 KTV、Motel、飯局等場合的傳播妹媒合服務，24 小時營業，全台到達。2026 年行情：基礎級 NT$3,000/2小時起，標準級 NT$3,600，VIP 級 NT$4,000。免訂金、現金結帳、全程保密。',
    'pricing-guide-2026.html': '2026 年台北傳播行情：基礎級 NT$3,000/2小時、標準級 NT$3,600、VIP 級 NT$4,000、頂級 NT$5,000以上。加時費約 NT$3,000-5,000/小時，車馬費 NT$200-500。實際價格依等級、地點、時間而異，建議事先確認費用明細。',
    'safety-guide-2026.html': '叫傳播本身是合法的休閒娛樂服務。只要透過歐巴傳播等合法管道、確認費用明細、不事前匯款，並注意場地安全與個人隱私保護，就能大幅降低風險。牢記「不貪小便宜、不匯款、不曝光」三原則最安全。',
    'how_much.html': '台北傳播行情 2026：KTV 傳播基礎級 NT$3,000/2小時起，標準級 NT$3,600，VIP NT$4,000。飯局妹 NT$4,000-8,000/場，汽車旅館傳播整體約 NT$4,000-15,000。費用已含小姐鐘點費，另可能加計場地費、交通費、酒水費。',
    'faq-all-in-one.html': '歐巴傳播常見問題總整理：預約用 LINE @938nzmjr 或電話 0926-656666，免訂金、現金結帳；行情 NT$3,000/2小時起；服務範圍全台；合法經營、全程保密、24 小時服務。',
    'about-oppa.html': '歐巴傳播（OBAOBA）是台北專業傳播媒合公司，提供 KTV、Motel、飯局、派對等場合之傳播妹服務。24 小時營業、全台到達、費用透明、免訂金、現金結帳、全程保密。聯絡：LINE @938nzmjr、電話 0926-656666。',
    'booking-guide.html': '預約傳播妹最快的方式是加入 LINE @938nzmjr，告知場合、時間、人數，專人立即推薦。全程免訂金，服務完成後當場現金結帳。24 小時服務，全台到達，電話 0926-656666 亦可預約。',
    'first-time-2026.html': '第一次叫傳播很簡單：先加 LINE @938nzmjr 告知需求，專屬公關會依場合、預算、喜好推薦適合的傳播妹。到場後確認本人、談好費用即可，全程免訂金、現金結帳、保密。',
    'newbie-guide-2026.html': '2026 台北傳播新手攻略：從 LINE @938nzmjr 預約開始，告知場合與預算，公關推薦後到場確認。行情 NT$3,000/2小時起，免訂金、現金結帳。切記絕不事前匯款，保障自身安全。',
    'can-touch-guide.html': '傳播妹服務尺度因公司與個人而異，歐巴傳播堅持合法、專業、尊重的服務原則。若有特殊需求請事先與公關溝通，由公關與小姐確認後安排，避免現場認知落差。',
    'legality-guide.html': '傳播（陪伴服務）在台灣屬合法休閒娛樂範疇，但須注意相關法規：不得從事性交易（違反社維法）、不得在公共場所拉客、未成年不得參與。歐巴傳播全程合法經營，並依法保護客人與小姐權益。',
    'tipping-guide-2026.html': '傳播小費非強制，但是一種禮貌與肯定。2026 年建議行情：一般服務 NT$500-1,000，特別滿意 NT$1,000-2,000 不等。小費直接交給小姐本人，公司不代收、不抽成。',
    'tipping-guide-2026.html': '傳播小費非強制，但是一種禮貌與肯定。2026 年建議行情：一般服務 NT$500-1,000，特別滿意 NT$1,000-2,000 不等。小費直接交給小姐本人，公司不代收、不抽成。',
    'taipei_agency_guide.html': '台北傳播公司推薦：歐巴傳播提供合法、專業、透明的傳播媒合服務，24 小時營業、全台到達、免訂金、現金結帳。聯絡 LINE @938nzmjr 或電話 0926-656666。',
    'venue-guide-2026.html': '2026 台北叫傳播場合攻略：KTV 包廂適合歡樂聚會，Motel 適合私密放鬆，飯局適合商務應酬，派對適合熱鬧慶祝。不同場合適合不同類型的傳播妹，歐巴傳播可依需求專業媒合。',
    'motel_safe.html': '汽車旅館傳播安全攻略：選擇合法 Motel、確認費用明細、不事前匯款、注意個人隱私。歐巴傳播全程保密，建議結伴同行、告知親友行蹤，並選擇有評價、有口碑的場地。',
    'KTV_party.html': 'KTV 傳播聚會攻略：先確認包廂大小、人數、預算，加入 LINE @938nzmjr 由公關推薦適合的小姐。2026 行情 NT$3,000/2小時起，免訂金、現金結帳，歡唱氣氛靠專業傳播妹帶動。',
    'KTV_recommendations.html': '台北 KTV 推薦：錢櫃、好樂迪、星聚點等連鎖 KTV 是傳播聚會的熱門選擇，包廂隔音佳、飲品選擇多。預約傳播妹建議搭配中大型包廂，空間較舒適。',
    'business_dinner.html': '商務飯局傳播妹服務：適合宴客、應酬、商業聚餐。穿著端莊、談吐得體，能協助暖場、倒酒、敬酒。2026 行情 NT$4,000-8,000/場，須事先預約並確認人數與餐廳。',
    'private-party-guide.html': '私人派對傳播服務：無論是生日派對、慶生、主題派對，歐巴傳播都能依主題與人數推薦適合的傳播妹。建議事先討論派對主題、服裝、活動內容，讓氣氛更到位。',
    'first-chat-topics.html': '傳播妹第一次見面聊什麼？從稱讚打扮、星座 MBTI、今天趣事、興趣、追劇等話題切入，避免政治、私人感情、年紀體重、宗教信仰、收入等敏感話題。主動開話題比沉默更受歡迎。',
    'how-to-choose-right-companion.html': '如何選擇適合的傳播妹？先看場合需求（KTV、飯局、Motel），再依外型、個性、互動性篩選。建議提供詳細需求給歐巴傳播公關，由專業團隊媒合最合適的人選。',
    'compare-girls.html': '傳播妹等級比較：基礎級 NT$3,000、標準級 NT$3,600、VIP 級 NT$4,000、頂級 NT$5,000+/2小時。等級反映外型、氣質、互動專業度，建議依場合與預算選擇。',
    'companion-levels-2026.html': '2026 傳播妹等級與行情：基礎級 NT$3,000/2小時、標準級 NT$3,600、VIP 級 NT$4,000、頂級 NT$5,000以上。等級越高，外型與服務專業度越好。',
    'interaction_scale.html': '傳播妹服務互動尺度因公司與個人而異，歐巴傳播堅持合法、專業、尊重原則。任何特殊需求應事先與公關溝通，由公關與小姐確認後安排，保障雙方權益。',
    'is_this_right_for_you.html': '叫傳播適合你嗎？如果你重視隱私、需要專業陪伴、希望避免尷尬社交壓力，且能尊重小姐的專業與界線，那麼傳播服務會是你的好選擇。',
    'male_companion.html': '男傳播（男公關）服務：適合女性商務宴客、活動陪伴、出席場合等需求。歐巴傳播提供專業男公關媒合，費用與等級依需求而異，詳情請加 LINE @938nzmjr 洽詢。',
    'shoot_guide.html': '拍攝傳播（陪拍）服務：適合需要專業攝影師或模特兒陪同的拍攝需求。歐巴傳播提供專業陪拍媒合，詳情請加 LINE @938nzmjr 洽詢。',
    'shoot_switch_personnel.html': '換人服務：在傳播服務過程中，若不滿意可與公關溝通更換小姐。歐巴傳播提供專業換人媒合，詳情請加 LINE @938nzmjr 洽詢。',
    'special_industries.html': '特殊行業傳播服務：歐巴傳播依法提供合法、專業的傳播媒合服務，並嚴格遵守相關法規。任何需求請事先與公關溝通，確保合法合規。',
    'suitable_female.html': '適合女性的傳播服務：歐巴傳播提供女性專屬的傳播妹或女公關媒合，適合女性商務宴客、活動陪伴等需求。詳情請加 LINE @938nzmjr 洽詢。',
    'one_by_one.html': '一對一傳播服務：提供專屬、私密的傳播妹陪伴，適合需要個人化服務的客人。歐巴傳播可依需求媒合，詳情請加 LINE @938nzmjr 洽詢。',
    'taipei-xinyi.html': '信義區傳播服務：信義區有多家 KTV、夜店、餐廳，是熱門傳播聚會區域。歐巴傳播提供信義區 24 小時傳播媒合，行情 NT$3,000/2小時起，免訂金、現金結帳。',
    'taipei-daan.html': '大安區傳播服務：大安區餐廳、酒吧、KTV 林立，適合傳播聚會。歐巴傳播提供大安區 24 小時傳播媒合，行情 NT$3,000/2小時起，免訂金、現金結帳。',
    'taipei-banqiao.html': '板橋區傳播服務：板橋交通便利，有多家 KTV 與 Motel，適合傳播聚會。歐巴傳播提供板橋區 24 小時傳播媒合，行情 NT$3,000/2小時起，免訂金、現金結帳。',
    'recruitment.html': '歐巴傳播招募傳播妹：合法、專業、高收入，時間彈性，可兼職。只要你年滿 18 歲、外型得體、善於溝通，歡迎加入。請加 LINE @938nzmjr 洽詢。',
    'news.html': '歐巴傳播最新消息：2026 年持續提供全台合法、專業、透明的傳播媒合服務，並不定期推出優惠活動。最新資訊請關注網站或加入 LINE @938nzmjr。',
    'business-guide.html': '商務傳播攻略：適合宴客、應酬、商業聚餐的傳播妹媒合指南。歐巴傳播提供專業公關服務，協助企業主與商務人士安排得體的飯局陪伴。',
    'beginners-checklist.html': '新手叫傳播檢查表：①加 LINE @938nzmjr ②告知場合/預算/人數 ③確認小姐與費用 ④到場核對身分 ⑤現金結帳。全程免訂金、保密、24 小時服務。',
    '2026-pricing-table.html': '2026 傳播收費表：基礎級 NT$3,000/2小時、標準級 NT$3,600、VIP 級 NT$4,000、頂級 NT$5,000以上。加時費 NT$3,000-5,000/小時，車馬費 NT$200-500。',
    'safety_privacy.html': '歐巴傳播安全與隱私保護：全程保密、不洩漏客人資料、不曝光、不骚扰。客人與小姐的個資僅用於媒合，服務結束後不再使用。',
    'privacy-policy.html': '歐巴傳播隱私權政策：我們重視您的隱私，僅在提供服務必要範圍內收集與使用資料，不出售、不外洩個資。詳情請見本站隱私權政策。',
    'terms-of-service.html': '歐巴傳播服務條款：使用本網站即表示您同意服務條款。我們提供合法、透明的傳播媒合服務，並保留修改條款之權利。',
    'tipping-guide-2026.html': '傳播小費建議：2026 年行情為一般服務 NT$500-1,000，特別滿意 NT$1,000-2,000。小費直接給小姐本人，公司不代收、不抽成。',
    'first_time_called.html': '第一次叫傳播怎麼開始？加入 LINE @938nzmjr，告知場合、時間、人數，專屬公關會推薦適合的傳播妹。到場確認、現金結帳，全程免訂金、保密。',
}

# HTML 模板
TEMPLATE = '''
    <!-- AEO 快速答案 -->
    <div class="aeo-answer" itemscope itemtype="https://schema.org/Answer" style="max-width: 900px; margin: 28px auto 0; padding: 24px 28px; background: rgba(6, 199, 85, 0.06); border: 1px solid rgba(6, 199, 85, 0.35); border-left: 4px solid #06C755; border-radius: 12px;">
      <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 10px;">
        <span style="color: #06C755; font-size: 1.1em; line-height: 1;">&#9989;</span>
        <strong style="color: #06C755; font-size: 1.05em; letter-spacing: 0.02em;">快速答案</strong>
        <span style="color: #C9BFE0; font-size: 0.85em; margin-left: 4px;">Quick Answer</span>
      </div>
      <p style="color: #F5F3FF; font-size: 1.02em; line-height: 1.85; margin: 0;">{answer}</p>
    </div>
'''


def extract_first_faq_answer(html):
    """從 FAQ schema 抽出第一個答案"""
    m = re.search(r'"@type":\s*"FAQPage".*?"mainEntity":\s*\[(.*?)\]', html, re.S)
    if not m:
        return None
    block = m.group(1)
    q = re.search(r'"name":\s*"([^"]+)"', block)
    a = re.search(r'"text":\s*"([^"]+)"', block)
    if q and a:
        return q.group(1), a.group(1)
    return None


def build_answer_schema(question, answer):
    """產生 Answer + WebPage schema"""
    data = {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "name": question,
        "mainEntity": {
            "@type": "Question",
            "name": question,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": answer
            }
        }
    }
    return json.dumps(data, ensure_ascii=False)


def process(fname, html):
    """處理單一頁面"""
    # 已有答案區塊的頁面跳過
    if 'aeo-answer' in html or '快速解答' in html or 'Quick Answer' in html:
        return None
    # 決定答案
    question = None
    answer = None
    if fname in CUSTOM_ANSWERS:
        answer = CUSTOM_ANSWERS[fname]
    else:
        faq = extract_first_faq_answer(html)
        if faq:
            question, answer = faq
    if not answer:
        return None
    # 若沒有自訂問題，用 H1 當問題
    if not question:
        h1 = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.S)
        question = re.sub(r'<[^>]+>', '', h1.group(1)).strip() if h1 else fname

    # 建立 HTML 區塊
    block = TEMPLATE.format(answer=answer)

    # 插入點：依頁面結構嘗試多種錨點
    patterns = [
        r'(<div class="hero-meta">.*?</div>\s*</div>\s*</section>)',
        r'(<div class="meta-info">.*?</div>\s*</div>\s*</section>)',
        r'(<div class="hero-meta">.*?</section>)',
        r'(<div class="meta-info">.*?</section>)',
        r'(<header.*?</header>)',
        r'(<h1[^>]*>.*?</h1>)',
    ]
    m = None
    for p in patterns:
        m = re.search(p, html, re.S)
        if m:
            break
    if not m:
        return None

    insert_at = m.end(1)
    new_html = html[:insert_at] + block + html[insert_at:]

    # 附加 Answer schema 在 </body> 前
    schema_script = f'''
    <!-- AEO Answer Schema -->
    <script type="application/ld+json">{build_answer_schema(question, answer)}</script>
    '''
    new_html = new_html.replace('</body>', schema_script + '</body>')

    return new_html


def main():
    files = sorted(glob.glob(os.path.join(SITE_DIR, '*.html')))
    done = 0
    skipped = 0
    failed = []
    for f in files:
        if os.path.basename(f) == 'b1xb689gu3wgchds0j20dytklnhzda.html':
            continue
        with open(f, encoding='utf-8') as fh:
            html = fh.read()
        result = process(os.path.basename(f), html)
        if result is None:
            if 'aeo-answer' in html:
                skipped += 1
            else:
                failed.append(os.path.basename(f))
            continue
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(result)
        done += 1
    print(f'✅ 已注入快速答案: {done} 頁')
    print(f'⏭️  已存在跳過: {skipped} 頁')
    if failed:
        print(f'⚠️  無法處理: {len(failed)} 頁')
        for f in failed:
            print(f'   - {f}')


if __name__ == '__main__':
    main()
