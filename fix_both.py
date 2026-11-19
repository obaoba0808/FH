# -*- coding: utf-8 -*-
import re

def fix_file(filepath):
    with open(filepath, encoding='utf-8') as f:
        src = f.read()

    new_sections = '''
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

    # Pattern: insert new_sections AFTER </main> (inside <main>), BEFORE the comment block
    # Use a unique anchor: the comment block after </main>
    after_main = '</main>\n    <!-- ========================================== -->\n    <!-- 以上區塊為每篇文章需要替換的內容 -->\n    <!-- ========================================== -->'
    before_cta = '\n    <!-- Global CTA -->'

    if after_main in src:
        # Split at the insertion point
        parts = src.split(after_main, 1)
        # parts[0] = everything up to and including </main>+comment block
        # parts[1] = Global CTA + rest
        # We want new_sections to be INSIDE <main>, so insert after </main>
        # But before the comment block: so new_sections goes right after </main>
        # The correct anchor is: </main> followed by the comment block
        # We want to insert new_sections between </main> and the comment block
        # So: parts[0] ends with </main>\n, then we add new_sections, then comment block, then before_cta
        
        # Actually let's split differently: use </main> as the split point
        main_close = '</main>'
        idx_main = src.find(main_close)
        idx_after = idx_main + len(main_close)
        # Insert new_sections after </main> and before the comment block
        new_src = src[:idx_after] + '\n' + new_sections + src[idx_after:]
        print(f"Inserted new sections after </main> in {filepath}")
    else:
        print(f"WARNING: after_main anchor not found in {filepath}")
        print("Trying alternative approach...")
        # Alternative: insert before the comment block (which is after </main>)
        alt = '    <!-- 以上區塊為每篇文章需要替換的內容 -->'
        if alt in src:
            idx = src.find(alt)
            new_src = src[:idx] + new_sections + src[idx:]
            print(f"Inserted before comment block in {filepath}")
        else:
            print(f"ERROR: cannot find insertion point in {filepath}")
            return

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_src)
    
    # Verify
    with open(filepath, encoding='utf-8') as f:
        c = f.read()
    m = re.search(r'<main[^>]*>(.*?)<\/main>', c, re.DOTALL)
    body = m.group(1) if m else ''
    h2 = c.count('<h2>')
    faq = c.count('<details class="mb-4')
    date_ok = '"dateModified": "2026-07-15"' in c
    cn = sum(1 for ch in body if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
    print(f"  H2={h2}, FAQ={faq}, dateModified={date_ok}, Chinese chars={cn}")

# Fix special_industries.html
special_path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html'
fix_file(special_path)

# Fix how_much.html
how_path = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\how_much.html'
fix_file(how_path)
