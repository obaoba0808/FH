# -*- coding: utf-8 -*-
import re

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    src = f.read()

# ── 1) Build new article sections ───────────────────────────────
new_sections = '''
        <h2>四、酒店與傳播的核心差異：場地與機動性</h2>
        <p>影響傳播收費的變數比表面數字複雜得多，首要因素是<b>預約時段</b>。週五與週六晚上的需求最旺，工資自然水漲船高；反觀平日週一至週四的下午茶場或平日晚間，許多公司會祭出折扣或促銷方案，平均可比週末便宜 NT$200 至 NT$500 不等。若時間弹性較大，刻意避開高峰時段是省錢的第一步。</p>
        <p>第二項關鍵變數是<b>地點</b>。台北市精華地帶如大安區、信義區的錢櫃或高級汽車旅館，因地點偏遠或消費水準高，司機與公關的車馬費可能稍高；而中正、內湖、士林等區域因交通便利性佳，收費相對平實。此外，偏遠縣市如新北的淡水或桃園，原則上需要負擔來回車資，費用比市區高出 NT$300 至 NT$800，預約前應先向公司確認。</p>
        <p>第三項則是<b>包廂人數組合</b>。兩人包廂的單價最高，因為一位公關必須專責服務您一人；四人以上包廂平均每人分攤的費用會明顯降低。若您打算揪團開趴，事先湊足人數不僅能炒熱氣氛，更能實質降低每人負擔。以保三等級為例，兩人場 NT$1,800/小時攤下來比四人場 NT$1,500/小時每人 NT$375 還貴。</p>

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

# ── 2) Fix insertion: use regex to insert AFTER </main>, BEFORE comment block ──
# Pattern: </main> followed by the comment block, then Global CTA
# We want to insert new_sections BETWEEN </main> and the comment block
# The comment block starts with: "    <!-- ========================================== -->"
# So we insert new_sections right after </main> and before that

comment_block_start = '    <!-- ========================================== -->\n    <!-- 以上區塊為每篇文章需要替換的內容 -->'
insert_after = '</main>\n'

if insert_after in src:
    src = src.replace(insert_after, insert_after + new_sections, 1)
    print("Insertion OK")
else:
    print("ERROR: insert_after not found!")

with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', 'w', encoding='utf-8') as f:
    f.write(src)

# ── Verification ──
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    c = f.read()

m = re.search(r'<main[^>]*>(.*?)<\/main>', c, re.DOTALL)
body = m.group(1) if m else ''
h2 = c.count('<h2>')
faq = c.count('<details class="mb-4')
date_ok = '"dateModified": "2026-07-15"' in c
faq_q = c.count('"@type": "Question"')
cn = sum(1 for ch in body if '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf')
print('=== special_industries.html ===')
print('  H2:', h2, '| FAQ:', faq, '| JSON-LD Q:', faq_q, '| dateModified:', date_ok)
print('  Chinese chars:', cn)
