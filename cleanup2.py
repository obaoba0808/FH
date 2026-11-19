# -*- coding: utf-8 -*-
"""
Final cleanup: remove duplicates, keep correct content, update metadata.
Both files currently have:
  - correct first 9 H2 sections inside <main>
  - extra duplicate H2 sections outside </main>
  - Wrong dateModified and JSON-LD
Goal: Remove duplicates outside </main>, update metadata, keep correct 9 H2.
"""
import re

def fix_file(path, new_sections_to_add, faq_ld_replacement, check_marker):
    with open(path, encoding='utf-8') as f:
        src = f.read()

    # Step 1: Find <main>...</main>
    m = re.search(r'<main[^>]*>(.*?)</main>', src, re.DOTALL)
    if not m:
        print(f"ERROR: no <main> in {path}")
        return

    body = m.group(1)
    body_h2 = body.count('<h2>')
    print(f"{path.split('/')[-1]}: body has {body_h2} H2")

    # Step 2: Check if new sections already added (四-section inside body)
    already_has_new = check_marker in body
    print(f"  Already has new sections: {already_has_new}")

    # Step 3: Trim body to first 9 H2 if needed
    h2_positions = [(m2.start(),) for m2 in re.finditer(r'<h2>', body)]
    if len(h2_positions) >= 9:
        # Trim to first 9 H2 sections
        correct_body = body[:h2_positions[8][0]]
        print(f"  Trimmed body to first 9 H2, {len(correct_body)} chars")
    else:
        correct_body = body

    # Step 4: Build final article body
    if already_has_new:
        final_body = correct_body  # already has new sections, don't re-add
        print(f"  Skipping new sections (already present)")
    else:
        final_body = correct_body + '\n' + new_sections_to_add
        print(f"  Added new sections, final body {len(final_body)} chars")

    # Step 5: Find Global CTA section
    cta_marker = '<section class="py-12 px-6 relative z-10 max-w-4xl mx-auto mb-12">'
    cta_pos = src.find(cta_marker)
    if cta_pos == -1:
        print(f"ERROR: Global CTA not found in {path}")
        return

    # Step 6: Reconstruct file
    before_main = src[:m.start()]
    after_cta = src[cta_pos:]

    # Build new <main> block
    new_main_block = f'\n        <main class="relative z-10 max-w-3xl mx-auto px-6 py-16 article-content">\n{final_body}\n    </main>\n'

    new_src = before_main + new_main_block + after_cta

    # Step 7: Update dateModified
    new_src = re.sub(r'"dateModified":\s*"[^"]*"', '"dateModified": "2026-07-15"', new_src)
    print(f"  dateModified updated")

    # Step 8: Update FAQ JSON-LD
    if faq_ld_replacement:
        # Try multiline first
        old_pattern, new_pattern = faq_ld_replacement
        if old_pattern in new_src:
            new_src = new_src.replace(old_pattern, new_pattern)
            print(f"  FAQ JSON-LD updated (multiline)")
        else:
            # Try compact (no spaces/newlines)
            compact_old = re.sub(r'\s+', '', old_pattern)
            compact_new = re.sub(r'\s+', '', new_pattern)
            if compact_old in new_src:
                new_src = new_src.replace(compact_old, compact_new)
                print(f"  FAQ JSON-LD updated (compact)")
            else:
                # Use regex to find and replace FAQPage block
                faq_match = re.search(
                    r'("@type":\s*"FAQPage".*?"mainEntity":\s*\[.*?\]\s*\})',
                    new_src, re.DOTALL
                )
                if faq_match:
                    new_src = new_src.replace(faq_match.group(0), new_pattern)
                    print(f"  FAQ JSON-LD updated (regex)")
                else:
                    print(f"  FAQ JSON-LD: old pattern not found!")

    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_src)

    # Verify
    with open(path, encoding='utf-8') as f:
        c = f.read()
    m2 = re.search(r'<main[^>]*>(.*?)</main>', c, re.DOTALL)
    body2 = m2.group(1) if m2 else ''
    h2 = c.count('<h2>')
    faq = c.count('<details class="mb-4')
    date_ok = '"dateModified": "2026-07-15"' in c
    faq_q = c.count('"@type": "Question"')
    cn = sum(1 for ch in body2 if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
    name = path.split('/')[-1]
    print(f'\n=== {name} ===')
    print(f'  H2 sections     : {h2} (need 9+)')
    print(f'  FAQ HTML items  : {faq} (need 6+)')
    print(f'  FAQ JSON-LD Q   : {faq_q} (need 6+)')
    print(f'  dateModified ok : {date_ok}')
    print(f'  Chinese chars   : {cn} (need 1500+)\n')


# ─── HOW_MUCH.HTML ──────────────────────────────────────────────
SEC_NEW_HOWMUCH = '''
        <h2>四、影響收費的關鍵變數：時段、地點、包廂人數</h2>
        <p>影響傳播收費的變數比表面數字複雜得多，首要因素是<b>預約時段</b>。週五與週六晚上的需求最旺，工資自然水漲船高；反觀平日週一至週四的下午茶場或平日晚間，許多公司會祭出折扣或促銷方案，平均可比週末便宜 NT$200 至 NT$500 不等。若時間弹性較大，刻意避開高峰時段是省錢的第一步。</p>
        <p>第二項關鍵變數是<b>地點</b>。台北市精華地帶如大安區、信義區的錢櫃或高級汽車旅館，因地點偏遠或消費水準高，司機與公關的車馬費可能稍高；而中正、內湖、士林等區域因交通便利性佳，收費相對平實。此外，偏遠縣市如新北的淡水或桃園，原則上需要負擔來回車資，費用比市區高出 NT$300 至 NT$800，預約前應先向公司確認。</p>
        <p>第三項則是<b>包廂人數組合</b>。兩人包廂的單價最高，因為一位公關必須專責服務您一人；四人以上包廂平均每人分攤的費用會明顯降低。若您打算揪團開趴，事先湊足人數不僅能炒熱氣氛，更能實質降低每人負擔。以保三等級為例，兩人場 NT$1,800/小時攤下來比四人場 NT$1,500/小時每人 NT$375 還貴。</p>

        <h2>五、公關、保三、VIP 三級詳細比較表</h2>
        <p>以下是業界最常被拿來比較的三個等級，從行情價到適合場合一次說明清楚，幫助您在預約前做出最佳判斷。</p>
        <div class="overflow-x-auto mb-6">
            <table class="w-full text-sm text-left border-collapse">
                <thead>
                    <tr class="border-b border-white/20 text-neonPink">
                        <th class="py-3 px-4 font-bold">等級</th>
                        <th class="py-3 px-4 font-bold">行情價（NT$/小時）</th>
                        <th class="py-3 px-4 font-bold">身高要求</th>
                        <th class="py-3 px-4 font-bold">顏值門檻</th>
                        <th class="py-3 px-4 font-bold">適合場合</th>
                        <th class="py-3 px-4 font-bold">服務態度</th>
                    </tr>
                </thead>
                <tbody class="text-gray-300">
                    <tr class="border-b border-white/10">
                        <td class="py-3 px-4 font-bold text-white">公關</td>
                        <td class="py-3 px-4">NT$1,200 – 1,400</td>
                        <td class="py-3 px-4">不限</td>
                        <td class="py-3 px-4">普通活潑</td>
                        <td class="py-3 px-4">KTV 歡唱、同學聚會</td>
                        <td class="py-3 px-4">主動熱情、帶動氣氛</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-3 px-4 font-bold text-white">保三</td>
                        <td class="py-3 px-4">NT$1,500 – 1,800</td>
                        <td class="py-3 px-4">160 cm 以上</td>
                        <td class="py-3 px-4">中上顏值、身材勻稱</td>
                        <td class="py-3 px-4">商務飯局、公司聚餐</td>
                        <td class="py-3 px-4">得體有禮、應對成熟</td>
                    </tr>
                    <tr class="border-b border-white/10">
                        <td class="py-3 px-4 font-bold text-white">VIP</td>
                        <td class="py-3 px-4">NT$2,000 – 2,500+</td>
                        <td class="py-3 px-4">163 cm 以上</td>
                        <td class="py-3 px-4">高顏值、網紅等級</td>
                        <td class="py-3 px-4">重要應酬、VIP 派對</td>
                        <td class="py-3 px-4">優雅細膩、話題豐富</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <p>值得注意的是，各公司的分級標準略有差異，部分公司會以「保二、保四」等更細緻的階級區分，建議預約前直接向歐巴傳播的 LINE 窗口詢問當日有空班的實際人選與報價。</p>

        <h2>六、為什麼歐巴傳播堅持透明定價？</h2>
        <p>市面上許多不良傳播公司慣用「低價吸客」的套路，先以 NT$800 行情價誘使客人下訂，抵達現場後才層層加碼：開桌費 NT$500、經紀費 NT$300、清潔費 NT$200，最終結算金額往往是報價的兩倍有餘。這種手法在業界俗稱「<strong>刺客行銷</strong>」，重傷消費者對整個行業的信任。</p>
        <p>歐巴傳播從創立之初便確立「<strong>透明報價、絕不事後加價</strong>」的核心原則。所有收費項目在預約確認階段便完整告知，包含鐘點費、車馬費（若有的話）與場地需求說明，客人同意後才派班。營造一個「<strong>消費前清楚，消費後安心</strong>」的交易環境，是我們對每一位客戶的基本承諾。</p>
        <p>此外，歐巴傳播更提供「<strong>看過滿意才計時</strong>」的保障機制：公關抵達現場後，消費者有權利先「看檯」，若長相、氣質不符合期待，可直接禮貌請對方離開並要求更換，<strong>此階段完全免費</strong>。這項制度杜絕了「照騙」的問題，也讓消費者在決策前擁有完整的知情權與主導權。</p>

        <h2>七、傳統八大行業 vs 傳播妹：價格結構差在哪？</h2>
        <p>要理解傳播的價格CP值，必須先搞懂傳統八大行業的收費套路。八大行業泛指酒店、特種行業等，其中最常被拿來比較的是<b>酒店（俗稱「店」）</b>的收費結構。酒店的計費方式極為複雜，以下逐一拆解：</p>
        <ul>
            <li><strong>框費（坐檯費）：</strong> 小姐到包廂坐下就開始計算，通常每 10-15 分鐘為一節，一節 NT$500 至 NT$1,000 不等，消費兩個小時等於 8-12 節，金額輕易破萬。</li>
            <li><strong>包廂費：</strong> 依包廂大小從 NT$1,500 到 NT$6,000 不等，且多為四小時起跳。</li>
            <li><strong>酒水費：</strong> 酒店的酒水價格是市價的 3-5 倍，一瓶普通威士忌市價 NT$1,200，在酒店包廂可能叫價 NT$4,000。</li>
            <li><strong>少爺小費、幹部抽成：</strong> 每次結帳另有各式名目的服務費。</li>
        </ul>
        <p>簡單來說，在酒店消費一場四小時的局，<strong>帳單金額輕鬆落在 NT$20,000 至 NT$40,000</strong>，還要加上小姐的「出場費」。相比之下，傳播以「鐘點費 × 人數」的簡潔模式，兩位公關四小時的費用大約 NT$9,600 至 NT$14,400，<strong>省下的費用足以再開一場續攤</strong>。傳播之所以CP值高，是因為去除了酒店層層剝削的中間環節，讓消費者直接與公關互動。</p>

        <h2>八、2026 年行情趨勢：通膨與市場現況</h2>
        <p>2026 年受到基本工資持續調漲、油價居高等因素影響，傳播行情也出現了微幅變化。根據業界觀察，台北都會區的公關時薪平均較 2025 年上漲約 5% 至 8%，主因是基本工資從 2025 年的 NT$285/小時提升至 2026 年的 NT$300/小時，連帶墊高了人力成本。</p>
        <p>具體來說，<strong>公關等級從 NT$1,200 調整至 NT$1,250 – 1,400</strong>；<strong>保三等級從 NT$1,500 – 1,800 調整至 NT$1,600 – 1,900</strong>；<strong>VIP 等級則從 NT$2,000 調整至 NT$2,100 – 2,500</strong>。即便如此，與傳統酒店相比，傳播的整體花費仍然低了 40% 至 60%，CP 值優勢依然明顯。</p>
        <p>值得注意的是，2026 年市場上出現了許多「低價傳播」的平台或 LINE 群組，打著 NT$600 – 800/小時的不可思議價格招攬客人。這類型服務的風險極高，可能是無照個體戶、或藉機從事非法交易，不僅沒有「打槍換人」的保障，一旦發生糾紛也求助無門。選擇像歐巴傳播這樣有固定公司制度與客服窗口的正規業者，才是長遠安心之道。</p>

        <h2>九、預算有限？NT$1,500 以內的高 CP 值玩法</h2>
        <p>即便預算在 NT$1,500 以內，依然有辦法玩得盡興又不委屈。以下提供三個實用策略，幫助小資族或只是想偶爾放鬆的客人，把每一分錢都花在刀口上。</p>
        <ul>
            <li><strong>策略一：平日離峰時段預約。</strong> 週一至週四的下午 14:00 – 18:00 是最划算的離峰時段，許多公司針對此時段提供 NT$1,000 – 1,200 的優惠價，相當於原價的 8 折。提前一至兩天預約，通常能鎖定更好的班底。</li>
            <li><strong>策略二：揪團平攤費用。</strong> 四人包廂點兩位公關，平均每人負擔 NT$750/小時，若再配合離峰時段，總預算可控制在 NT$2,400 以內（兩小時計），比獨自去一趟錢櫃加小費還划得來。</li>
            <li><strong>策略三：直接參加公司舉辦的主題派對。</strong> 歐巴傳播不時推出「雙人特惠組」或「派對套裝」，含一位公關兩小時服務加基本場地優惠，總價 NT$2,800 起，比個別預約實惠許多。詳情請追蹤歐巴傳播的 LINE 官方帳號獲取第一手優惠資訊。</li>
        </ul>
        <p>總結來說，傳播收費雖然看似有階級之分，但只要掌握時段、人數與預約時機三大要素，即便預算有限，也能享有高質感的外派陪伴服務。重點是找到值得信任的公司，並在預約前把所有費用確認清楚，避免成為冤大頭。</p>

        <h2>常見問題 FAQ</h2>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q1：叫傳播一小時大約多少錢？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>公關等級約 NT$1,200 – 1,400/小時，保三等級約 NT$1,500 – 1,900/小時，VIP 等級 NT$2,000 以上。實際價格以預約當下有空班的女孩與公司報價為準。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q2：車馬費怎麼算？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>市區（台北市、新北市核心區）一般不收車馬費；跨縣市或偏遠地區可能酌收 NT$300 – NT$800，預約時會先告知，不會到場才追加。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q3：不滿意可以打槍換人嗎？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>可以。在公關坐下確認服務前，若長相或氣質不符合期待，可直接要求更換，不收取任何費用。這是正規傳播公司保障消費者權益的基本機制。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q4：傳播跟酒店的價格差多少？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>一場四小時的酒店聚會，帳單輕鬆落在 NT$20,000 – 40,000（含框費、包廂費、酒水費等）。傳播同樣四小時、兩位公關的費用約 NT$9,600 – 14,400，節省幅度達 40% – 60%。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q5：有沒有隱藏費用或加價項目？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>正規公司如歐巴傳播，預約時完整告知所有費用項目（鐘點費與車馬費），絕無開桌費、經紀費、清潔費等隱藏項目。建議選擇透明報價的正規公司，避免落入低價陷阱。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q6：2026 年行情是否有變動？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>受基本工資調漲影響，2026 年行情較 2025 年微幅上漲約 5% – 8%。即便如此，傳播整體費用仍比傳統酒店低了近一半，是目前台北夜生活CP值最高的選擇。</p>
            </div>
        </details>

'''

FAQ_LD_HOWMUCH_OLD = '{"@type":"FAQPage","@id":"https://obaoba0808.github.io/FH/how_much.html#faq","mainEntity":[{"@type":"Question","name":"叫傳播多少錢？","acceptedAnswer":{"@type":"Answer","text":"在台北正統傳播公司，行情約為每小時 NT$1,200 至 NT$2,500 不等，取決於等級（公關、保三、VIP）。歐巴傳播主打透明定價、絕不事後加價。"}}]}'
FAQ_LD_HOWMUCH_NEW = '{"@type":"FAQPage","@id":"https://obaoba0808.github.io/FH/how_much.html#faq","mainEntity":[{"@type":"Question","name":"叫傳播多少錢？","acceptedAnswer":{"@type":"Answer","text":"公關等級約 NT$1,200 – 1,400/小時，保三等級約 NT$1,500 – 1,900/小時，VIP 等級 NT$2,000 以上。實際價格以預約當下有空班的女孩與公司報價為準。"}},{"@type":"Question","name":"車馬費怎麼算？","acceptedAnswer":{"@type":"Answer","text":"市區（台北市、新北市核心區）一般不收車馬費；跨縣市或偏遠地區可能酌收 NT$300 – NT$800，預約時會先告知，不會到場才追加。"}},{"@type":"Question","name":"不滿意可以打槍換人嗎？","acceptedAnswer":{"@type":"Answer","text":"可以。在公關坐下確認服務前，若長相或氣質不符合期待，可直接要求更換，不收取任何費用。這是正規傳播公司保障消費者權益的基本機制。"}},{"@type":"Question","name":"傳播跟酒店的價格差多少？","acceptedAnswer":{"@type":"Answer","text":"一場四小時的酒店聚會，帳單輕鬆落在 NT$20,000 – 40,000（含框費、包廂費、酒水費等）。傳播同樣四小時、兩位公關的費用約 NT$9,600 – 14,400，節省幅度達 40% – 60%。"}},{"@type":"Question","name":"有沒有隱藏費用或加價項目？","acceptedAnswer":{"@type":"Answer","text":"正規公司如歐巴傳播，預約時完整告知所有費用項目（鐘點費與車馬費），絕無開桌費、經紀費、清潔費等隱藏項目。建議選擇透明報價的正規公司，避免落入低價陷阱。"}},{"@type":"Question","name":"2026 年行情是否有變動？","acceptedAnswer":{"@type":"Answer","text":"受基本工資調漲影響，2026 年行情較 2025 年微幅上漲約 5% – 8%。即便如此，傳播整體費用仍比傳統酒店低了近一半，是目前台北夜生活CP值最高的選擇。"}}]}'

fix_file(
    r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\how_much.html',
    new_sections_to_add=SEC_NEW_HOWMUCH,
    faq_ld_replacement=(FAQ_LD_HOWMUCH_OLD, FAQ_LD_HOWMUCH_NEW),
    check_marker='四、影響收費的關鍵變數：時段、地點、包廂人數'
)


# ─── SPECIAL_INDUSTRIES.HTML ────────────────────────────────────
SEC_NEW_SPECIAL = '''
        <h2>四、酒店與傳播的核心差異：場地與機動性</h2>
        <p>酒店與傳播最根本的差異，在於<b>「誰決定地點」</b>。在酒店消費，您必須親自前往店家，無論是台北東區的制服店、禮服店還是便服店，地點由店家決定，營業時間也受到限制——通常凌晨兩點後便打烊，想續攤也無處可去。更糟的是，幹部與少爺時不時進包廂推銷酒水，打斷聚會節奏，令人不勝其擾。</p>
        <p>傳播則完全打破這個限制。當您致電或加 LINE 預約，告知希望的地點——無論是錢櫃、好樂迪、商務會所，還是離市區有一段距離的陽明山私廚，<strong>公關小姐會依照您的安排前往</strong>。您可以選在自己熟悉的場地，掌控聚會的節奏與氣氛，不用擔心被不相關的人打擾。這種「<strong>外送到府</strong>」的概念，正是傳播相較於酒店最大的核心優勢。</p>
        <p>此外，酒店的包廂大小與等級掛鉤，想要升級大包廂往往需要加價；而傳播的人數組合完全自由——兩人小酌、三人閒聊、十人以上開趴，都能在同一套計費模式下靈活安排。這種高度的彈性，讓傳播的使用場景遠比酒店寬廣許多。</p>

        <h2>五、什麼是「傳播」？與酒店、公關公司的本質區別</h2>
        <p>「傳播」這個詞在業界的全稱是「傳播公司」或「傳播經紀」，本質上是一種<strong>人力派遣型態的陪伴服務</strong>。公司旗下簽約一定數量的公關小姐（俗稱「妹妹」），當客人有陪伴需求時，公司負責調配人力的派遣與媒合，並從中收取服務費或抽成。</p>
        <p>很多人容易把傳播與「公關公司」搞混。公關公司的定義更廣，泛指從事公關活動、活動策劃或商務陪同的正規企業；而傳播在台灣的語境下，多半指的是<strong>以派遣女性陪伴服務為核心業務</strong>的公司，服務場景以夜生活娛樂為主，涵蓋KTV、派對、飯局等場合。</p>
        <p>傳播與酒店的差異更明顯：酒店屬於「定點接待」模式，女孩在店內等待客人上門，工作環境固定且高壓；傳播則是「外送服務」模式，女孩根據每次預約的指示前往不同地點，工作節奏更彈性、自主性更高。兩者雖然都隸屬八大行業的廣義範疇，但在商業模式、收費結構與工作體驗上，差異相當巨大。</p>

        <h2>六、公關、保三、模特：傳播妹的三個等級詳解</h2>
        <p>許多初次接觸傳播的客人，常對「公關、保三、模特」這些名詞感到困惑。以下詳細說明這三個等級的篩選標準、工作內容與適合場景，幫助您對號入座，找到最適合自己的陪伴人選。</p>
        <ul>
            <li><strong>公關（普級）：</strong> 篩選標準以活潑好聊、帶動氣氛為主，顏值與身材無嚴格門檻。適合預算有限、純粹想找人唱歌聊天的場合，如同學聚會、生日派對、單純續攤等。收費 NT$1,200/小時起，是最高 CP 值的選擇。</li>
            <li><strong>保三（中級）：</strong> 須通過一定的顏值與身材初選，通常要求身高 160cm 以上、五官端正、體態勻稱。適合商務應酬、公司聚餐或需要「撐場面」的正式場合，不僅能陪伴，更能展現一定的社交禮儀與應對能力。收費 NT$1,500 – 1,800/小時。</li>
            <li><strong>VIP模特（高級）：</strong> 嚴格篩選，外型亮眼程度相當於網紅或演藝等級，氣質談吐兼備，能在高端社交場合自然融入。適合重要的商務飯局、VIP 派對或私人招待所等需要「門面」的場合。收費 NT$2,000/小時以上，部分頂級人選可達 NT$3,000/小時。</li>
        </ul>
        <p>值得一提的是，歐巴傳播對於每一位簽約公關都有基本的身分核查與背景確認，確保不會有未成年或是非自願從事工作者。這是正規公司對社會責任的基本把關，也是客人選擇傳播服務時應優先考量的安全指標。</p>

        <h2>七、八大行業女生的入行考量：為什麼選擇傳播而非酒店？</h2>
        <p>從女性工作者的角度來看，傳播與酒店兩條路的差異，直接影響她們的生活品質與長期發展。以下從五個實際層面分析，為什麼越來越多女孩在入行八大行業時，優先考慮傳播而非傳統酒店。</p>
        <p><strong>第一，時間彈性。</strong> 酒店工作通常需要「打卡制」，從晚間八點待到凌晨兩點是基本款，中途離場常受到限制或扣薪。傳播則是預約制，女孩可以根據自己的時間安排接受或婉拒訂單，適合有正職工作或在校就讀、需要兼職收入的人。</p>
        <p><strong>第二，無酒精壓力。</strong> 酒店生態中，推銷酒水是核心業績來源，女孩往往被要求陪同大量飲酒，長期下來對健康造成傷害。傳播的工作內容以陪伴聊天、帶動氣氛為主，沒有硬性的酒水推銷壓力，烈酒往往是「喝或不喝由自己決定」。</p>
        <p><strong>第三，場地自主。</strong> 酒店的包廂空間封閉，高壓的消費文化容易讓女孩陷入情緒疲乏。傳播的工作地點多樣（KTV、餐廳、汽車旅館），且女孩可以事先了解客人的背景與需求，有心理準備的情況下赴約，心理負擔相對較輕。</p>
        <p><strong>第四，收入結構透明。</strong> 酒店的薪水受到幹部、經紀、公司多層抽成，實際到手的金額往往只有帳面的一小部分。傳播的收費結構相對透明，鐘點費直接與服務時間掛鉤，女孩對於自己的收入有更清晰的掌握。</p>
        <p><strong>第五，沒有「困在店裡」的壓力。</strong> 酒店環境中，女孩若遇到不愉快的客人或狀況，往往需要透過幹部或公司協調，處境被動；傳播的女孩到場服務後，若感到不舒服，可以選擇婉拒後續服務並離開，主導權在自己手上。</p>

        <h2>八、歐巴傳播的定位：介於酒店與正當娛樂之間</h2>
        <p>歐巴傳播的服務定位，刻意與傳統八大行業保持距離，同時也與一般社交平台有所區隔。我們把自己定義為「<strong>介於酒店與正當娛樂之間的頂級外派陪伴服務</strong>」，這個定位體現在以下三個核心原則：</p>
        <ul>
            <li><strong>透明定價，杜絕刺客消費：</strong> 從第一通電話或第一封 LINE 訊息開始，所有費用項目便完整告知消費者，絕無到場後層層追加的戲碼。</li>
            <li><strong>看過滿意才計時，保障雙方：</strong> 公關抵達後，消費者有權利先「看檯」確認，不滿意可立即更換。這項制度不只保護消費者，也間接篩選了真正有服務意願的工作者。</li>
            <li><strong>一對一客服，負責到底：</strong> 每位消費者從預約到服務結束，全程配有專屬客服窗口，任何問題都能即時獲得回應，而非像酒店消費般結帳後就「人去樓空」。</li>
        </ul>
        <p>我們相信，優質的陪伴服務不需要高昂的包廂費與酒水費來襯托。一個愉快的夜晚，取決於對的人、對的氣氛、對的場所，而非華麗卻昂貴的場面。這就是歐巴傳播的存在價值。</p>

        <h2>九、常見迷思破解：傳播真的是八大行業嗎？</h2>
        <p>許多人聽到「傳播」二字，第一直覺反應是「八大行業」「特種行業」，下意識地將其與非法交易畫上等號。這個刻板印象，來自於早期市場混亂時期的歷史包袱。事實上，傳播的法律定性長期處於<strong>灰色地帶</strong>，具體解析如下：</p>
        <p><strong>迷思一：傳播等於性交易。</strong> 這是最大的誤解。正規傳播公司的核心服務是「陪同陪伴」，涵蓋唱歌、聊天、飯局、派對等社交場合的陪伴。服務內容以情感互動為主，絕非以性交易為目的。若有業者以此為號召，那是個別業者的違法行為，不代表整個行業。</p>
        <p><strong>迷思二：傳播是合法的八大行業。</strong> 嚴格來說，傳播並非政府核發特種行業許可證的業種類別。它不像酒店有特定的業種登記（如視聽歌唱、特定娛樂），而是掛靠在「陪伴服務」「公關服務」的廣義框架下營運。這也是為什麼傳播長期存在法律灰色空間——<strong>不違法，但也不受明確法律保障</strong>。</p>
        <p><strong>迷思三：叫傳播會被抓？</strong> 消費者單純叫一位公關到 KTV 唱歌聊天，完全屬於正常社交行為，不構成違法。只有當消費內容涉及性交易或非法活動時，才會觸犯法律。選擇正規公司、正常消費，消費者與工作者雙方皆受到法律保障。</p>
        <p>面對這個灰色地帶，歐巴傳播的策略是：<strong>提供優質陪伴服務、杜絕任何非法暗示、公開透明收費</strong>，用制度與口碑建立品牌信譽，而非依賴擦邊球或灰色地帶存活。這是我們對自身定位的堅持，也是對每一位消費者與工作者的責任。</p>

        <h2>常見問題 FAQ</h2>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q1：什麼是「傳播」？跟酒店有何不同？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>傳播是指傳播公司派遣公關小姐到客人指定的地點（如KTV、汽車旅館、私人會所）提供陪伴服務，採鐘點計費，無包廂費與酒水低消；酒店則需要客人到店消費，有高昂包廂費與酒水費，且受限於店家營業時間。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q2：公關、保三、模特三個等級有何差異？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>公關等級適合一般聚會，活潑大方，收費 NT$1,200/小時起；保三等級顏值與身材較高，適合商務場合，收費 NT$1,500/小時起；VIP模特等級為網紅或高顏值，適合重要應酬，收費 NT$2,000/小時以上。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q3：女生入行八大行業，為什麼優先選擇傳播而非酒店？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>傳播的工作時間更彈性，可兼顧正職或學業；地點由客人指定，女孩不需長期待在高壓的酒店環境；酒精壓力較小，不必被強迫推銷或陪同大量飲酒的飯局；收入以時計，不受幹部抽成剝削。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q4：傳播是否屬於八大行業？法律上如何定義？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>傳播的定位處於法律灰色地帶。正規傳播公司的業務本質是「陪同陪伴服務」，而非性交易，但市場上確實存在打著傳播名號實則從事非法交易的業者。選擇有固定公司制度與客服窗口的正規傳播，是保障雙方權益的關鍵。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q5：歐巴傳播和其他傳播公司有什麼不同？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>歐巴傳播定位為「介於酒店與正當娛樂之間的頂級外派陪伴服務」，提供透明定價、看過滿意才計時的保障，並配有一對一客服窗口。無隱藏費用、無事後加價，是我們對消費者的核心承諾。</p>
            </div>
        </details>
        <details class="mb-4 border border-white/10 rounded-xl overflow-hidden">
            <summary class="px-6 py-4 cursor-pointer font-bold text-white hover:bg-white/5 transition-colors">Q6：叫傳播適合哪些場合？</summary>
            <div class="px-6 py-4 text-gray-300 border-t border-white/10">
                <p>傳播的機動性極高，適合幾乎所有需要女性陪伴的社交場合：KTV歡唱、公司聚餐後續攤、商務飯局撐場面、私人派對、汽車旅館聚會、一對一約會等。場所由您決定，時間由您掌控，遠比酒店更有彈性。</p>
            </div>
        </details>

'''

# For special_industries.html, we need to replace the entire JSON-LD script
SPECIAL_SCHEMA_OLD = '<script type="application/ld+json>\n{\n  "@context": "https://schema.org", "@type": "NewsArticle",\n  "headline": "八大行業大解密：酒店與傳播到底差在哪？",\n  "image": ["https://ibb.co/5hVhkRwL"]\n}\n</script>'
SPECIAL_SCHEMA_NEW ='''<script type="application/ld+json>
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "@id": "https://obaoba0808.github.io/FH/special_industries.html#article",
      "headline": "八大行業大解密：酒店與傳播到底差在哪？",
      "description": "酒店與傳播公司有什麼不同？從消費模式、場地限制到客群分析，帶你了解為何越來越多玩家轉而選擇機動性更高的「叫傳播」。",
      "datePublished": "2024-01-01",
      "dateModified": "2026-07-15",
      "author": {"@type": "Organization", "name": "歐巴傳播"},
      "publisher": {
        "@type": "Organization",
        "name": "歐巴傳播",
        "logo": {"@type": "ImageObject", "url": "https://obaoba0808.github.io/FH/images/android-chrome-512x512.png"}
      }
    },
    {
      "@type": "FAQPage",
      "@id": "https://obaoba0808.github.io/FH/special_industries.html#faq",
      "mainEntity": [
        {"@type": "Question", "name": "什麼是「傳播」？跟酒店有何不同？", "acceptedAnswer": {"@type": "Answer", "text": "傳播是指傳播公司派遣公關小姐到客人指定的地點（如KTV、汽車旅館、私人會所）提供陪伴服務，採鐘點計費，無包廂費與酒水低消；酒店則需要客人到店消費，有高昂包廂費與酒水費，且受限於店家營業時間。"}},
        {"@type": "Question", "name": "公關、保三、模特三個等級有何差異？", "acceptedAnswer": {"@type": "Answer", "text": "公關等級適合一般聚會，活潑大方，收費 NT$1,200/小時起；保三等級顏值與身材較高，適合商務場合，收費 NT$1,500/小時起；VIP模特等級為網紅或高顏值，適合重要應酬，收費 NT$2,000/小時以上。"}},
        {"@type": "Question", "name": "女生入行八大行業，為什麼優先選擇傳播而非酒店？", "acceptedAnswer": {"@type": "Answer", "text": "傳播的工作時間更彈性，可兼顧正職或學業；地點由客人指定，女孩不需長期待在高壓的酒店環境；酒精壓力較小，不必被強迫推銷或陪同大量飲酒的飯局；收入以時計，不受幹部抽成剝削。"}},
        {"@type": "Question", "name": "傳播是否屬於八大行業？法律上如何定義？", "acceptedAnswer": {"@type": "Answer", "text": "傳播的定位處於法律灰色地帶。正規傳播公司的業務本質是「陪同陪伴服務」，而非性交易，但市場上確實存在打著傳播名號實則從事非法交易的業者。選擇有固定公司制度與客服窗口的正規傳播，是保障雙方權益的關鍵。"}},
        {"@type": "Question", "name": "歐巴傳播和其他傳播公司有什麼不同？", "acceptedAnswer": {"@type": "Answer", "text": "歐巴傳播定位為「介於酒店與正當娛樂之間的頂級外派陪伴服務」，提供透明定價、看過滿意才計時的保障，並配有一對一客服窗口。無隱藏費用、無事後加價，是我們對消費者的核心承諾。"}},
        {"@type": "Question", "name": "叫傳播適合哪些場合？", "acceptedAnswer": {"@type": "Answer", "text": "傳播的機動性極高，適合幾乎所有需要女性陪伴的社交場合：KTV歡唱、公司聚餐後續攤、商務飯局撐場面、私人派對、汽車旅館聚會、一對一約會等。場所由您決定，時間由您掌控，遠比酒店更有彈性。"}}
      ]
    }
  ]
}
</script>'''

# special_industries.html: just fix the body (don't need FAQ JSON-LD replacement since it's a new schema)
path_special = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html'
with open(path_special, encoding='utf-8') as f:
    src = f.read()

m = re.search(r'<main[^>]*>(.*?)</main>', src, re.DOTALL)
body = m.group(1)
body_h2 = body.count('<h2>')
print(f"special_industries.html: body has {body_h2} H2")
already_has_new = '四、酒店與傳播的核心差異：場地與機動性' in body
print(f"  Already has new sections: {already_has_new}")

h2_positions = [(m2.start(),) for m2 in re.finditer(r'<h2>', body)]
if len(h2_positions) >= 9:
    correct_body = body[:h2_positions[8][0]]
    print(f"  Trimmed to first 9 H2, {len(correct_body)} chars")
else:
    correct_body = body

if already_has_new:
    final_body = correct_body
    print(f"  Skipping new sections (already present)")
else:
    final_body = correct_body + '\n' + SEC_NEW_SPECIAL
    print(f"  Added new sections, final {len(final_body)} chars")

cta_marker = '<section class="py-12 px-6 relative z-10 max-w-4xl mx-auto mb-12">'
cta_pos = src.find(cta_marker)
before_main = src[:m.start()]
after_cta = src[cta_pos:]

new_main_block = f'\n    <main class="relative z-10 max-w-3xl mx-auto px-6 py-16 article-content">\n{final_body}\n</main>\n'
new_src = before_main + new_main_block + after_cta

# Update schema
if SPECIAL_SCHEMA_OLD in new_src:
    new_src = new_src.replace(SPECIAL_SCHEMA_OLD, SPECIAL_SCHEMA_NEW)
    print("  Schema updated")
else:
    # Try compact version
    compact_old = re.sub(r'\s+', '', SPECIAL_SCHEMA_OLD)
    compact_new = re.sub(r'\s+', '', SPECIAL_SCHEMA_NEW)
    if compact_old in new_src:
        new_src = new_src.replace(compact_old, compact_new)
        print("  Schema updated (compact)")
    else:
        print("  Schema: old pattern not found!")
        # Try regex
        old_pat = re.compile(r'<script type="application/ld\+json>.*?</script>', re.DOTALL)
        new_src = old_pat.sub(SPECIAL_SCHEMA_NEW, new_src)
        print("  Schema updated (regex)")

with open(path_special, 'w', encoding='utf-8') as f:
    f.write(new_src)
print(f"special_industries.html written, {len(new_src)} chars")

# Verify special
with open(path_special, encoding='utf-8') as f:
    c = f.read()
m2 = re.search(r'<main[^>]*>(.*?)</main>', c, re.DOTALL)
body2 = m2.group(1) if m2 else ''
h2 = c.count('<h2>')
faq = c.count('<details class="mb-4')
date_ok = '"dateModified": "2026-07-15"' in c
faq_q = c.count('"@type": "Question"')
cn = sum(1 for ch in body2 if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
print(f'\n=== special_industries.html ===')
print(f'  H2 sections     : {h2} (need 9+)')
print(f'  FAQ HTML items  : {faq} (need 6+)')
print(f'  FAQ JSON-LD Q   : {faq_q} (need 6+)')
print(f'  dateModified ok : {date_ok}')
print(f'  Chinese chars   : {cn} (need 1500+)')
