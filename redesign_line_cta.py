"""
歐巴傳播 LINE CTA 重新設計系統
目標：提升轉換率，讓更多人加 LINE

設計原則：
1. 統一設計語言（最強的 LINE 按鈕）
2. 差異化文案（依頁面類型）
3. 加入信任狀（數字、徽章）
4. 加入緊迫感（30分鐘、24小時）
5. 多處曝光（Hero + 中間 + Footer 前）
"""

import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

BASE_URL = "https://obaoba0808.github.io/FH/"

# ============================================================
# CTA 模板（6 種變體）
# ============================================================

# 模板1：首頁 / 速度型（最大按鈕，加入 LINE 官方徽章）
CTA_HERO = '''
<!-- LINE CTA Section -->
<section class="py-16 px-6 relative z-10">
    <div class="max-w-4xl mx-auto">
        <div class="glass-panel rounded-3xl p-8 md:p-10 border border-[#06C755]/30 relative overflow-hidden">
            <!-- 背景光暈 -->
            <div class="absolute -top-20 -right-20 w-60 h-60 bg-[#06C755]/10 rounded-full blur-3xl"></div>
            <div class="absolute -bottom-20 -left-20 w-60 h-60 bg-[#06C755]/5 rounded-full blur-3xl"></div>

            <div class="relative z-10 text-center">
                <!-- 信任徽章 -->
                <div class="flex flex-wrap justify-center gap-3 mb-6">
                    <span class="px-3 py-1 rounded-full bg-[#06C755]/20 text-[#06C755] text-xs font-bold border border-[#06C755]/30">
                        <iconify-icon icon="ph:clock-countdown-fill" class="inline align-middle mr-1"></iconify-icon>平均30分鐘到府
                    </span>
                    <span class="px-3 py-1 rounded-full bg-electricPurple/20 text-electricPurple text-xs font-bold border border-electricPurple/30">
                        <iconify-icon icon="ph:shield-check-fill" class="inline align-middle mr-1"></iconify-icon>隱私100%保密
                    </span>
                    <span class="px-3 py-1 rounded-full bg-neonPink/20 text-neonPink text-xs font-bold border border-neonPink/30">
                        <iconify-icon icon="ph:users-three-fill" class="inline align-middle mr-1"></iconify-icon>已服務3,000+客戶
                    </span>
                </div>

                <h3 class="text-2xl md:text-3xl font-black mb-3 text-textWhite">
                    想要今晚安排？<span class="text-[#06C755]">LINE 最快</span>
                </h3>
                <p class="text-gray-400 mb-8 text-sm md:text-base">
                    說出你的需求 → 專人確認 → 30分鐘內到府。全程隱私，不留紀錄。
                </p>

                <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
                   class="inline-flex items-center gap-3 px-10 py-5 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-xl md:text-2xl transition-all shadow-[0_0_40px_rgba(6,199,85,0.4)] hover:shadow-[0_0_60px_rgba(6,199,85,0.6)] hover:scale-[1.03] active:scale-[0.98]"
                   onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'hero_section'});">
                    <iconify-icon icon="bi:line" class="text-3xl"></iconify-icon>
                    立即加 LINE 預約
                </a>

                <p class="mt-4 text-xs text-gray-500">
                    或致電 <a href="tel:+886926656666" onclick="gtag('event', 'phone_click', {'event_category': 'CTA', 'event_label': 'hero_section'});" class="text-gray-400 hover:text-white underline underline-offset-2">0926-656666</a> · 24小時服務
                </p>
            </div>
        </div>
    </div>
</section>
'''

# 模板2：比較頁 / 信任型（差異化 Why Choose Us）
CTA_CHOOSE_US = '''
<!-- 為什麼選擇歐巴傳播 -->
<section class="py-16 px-6 relative z-10">
    <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-3xl md:text-4xl font-black mb-3">
            為什麼選擇<span class="text-gradient">歐巴傳播</span>？
        </h2>
        <p class="text-gray-400 mb-10">4個讓客戶回頭的理由</p>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
            <div class="glass-panel rounded-2xl p-6 text-center hover:border-[#06C755]/50 transition-colors">
                <iconify-icon icon="ph:clock-countdown-fill" class="text-4xl text-[#06C755] mb-3"></iconify-icon>
                <div class="text-2xl font-black text-textWhite">30分鐘</div>
                <div class="text-xs text-gray-400 mt-1">快速到府調度</div>
            </div>
            <div class="glass-panel rounded-2xl p-6 text-center hover:border-[#06C755]/50 transition-colors">
                <iconify-icon icon="ph:shield-check-fill" class="text-4xl text-electricPurple mb-3"></iconify-icon>
                <div class="text-2xl font-black text-textWhite">100%</div>
                <div class="text-xs text-gray-400 mt-1">隱私保密保障</div>
            </div>
            <div class="glass-panel rounded-2xl p-6 text-center hover:border-[#06C755]/50 transition-colors">
                <iconify-icon icon="ph:arrows-clockwise-fill" class="text-4xl text-neonPink mb-3"></iconify-icon>
                <div class="text-2xl font-black text-textWhite">打槍換人</div>
                <div class="text-xs text-gray-400 mt-1">不滿意免費換</div>
            </div>
            <div class="glass-panel rounded-2xl p-6 text-center hover:border-[#06C755]/50 transition-colors">
                <iconify-icon icon="ph:star-fill" class="text-4xl text-yellow-400 mb-3"></iconify-icon>
                <div class="text-2xl font-black text-textWhite">98%</div>
                <div class="text-xs text-gray-400 mt-1">客戶滿意回頭</div>
            </div>
        </div>

        <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
           class="inline-flex items-center gap-3 px-10 py-5 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-xl transition-all shadow-[0_0_30px_rgba(6,199,85,0.4)] hover:scale-[1.03]"
           onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'choose_us'});">
            <iconify-icon icon="bi:line" class="text-2xl"></iconify-icon>
            用 LINE 預約，享保障
        </a>
    </div>
</section>
'''

# 模板3：新手向 / 隱私型（降低初次接觸門檻）
CTA_FIRST_TIMER = '''
<!-- 新手專區：LINE 匿名諮詢 -->
<section class="py-16 px-6 relative z-10">
    <div class="max-w-3xl mx-auto">
        <div class="glass-panel rounded-3xl p-8 md:p-10 border border-electricPurple/30 text-center">
            <div class="w-16 h-16 rounded-full bg-electricPurple/20 flex items-center justify-center mx-auto mb-6">
                <iconify-icon icon="ph:user-circle-question-fill" class="text-4xl text-electricPurple"></iconify-icon>
            </div>
            <h3 class="text-2xl md:text-3xl font-black mb-3">
                第一次叫傳播？<br><span class="text-electricPurple">LINE 先問，不尷尬</span>
            </h3>
            <p class="text-gray-400 mb-8 text-sm md:text-base">
                可以先化名詢問行程、收費、注意事項。<br>
                專人回覆，不需要當場決定。
            </p>
            <div class="flex flex-col sm:flex-row gap-4 justify-center">
                <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
                   class="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-lg transition-all shadow-[0_0_25px_rgba(6,199,85,0.3)] hover:scale-[1.02]"
                   onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'first_timer'});">
                    <iconify-icon icon="bi:line" class="text-xl"></iconify-icon>
                    LINE 匿名諮詢（免費）
                </a>
                <a href="tel:+886926656666"
                   class="inline-flex items-center justify-center gap-2 px-8 py-4 rounded-2xl border border-white/20 hover:bg-white/10 text-white font-bold text-lg transition-colors"
                   onclick="gtag('event', 'phone_click', {'event_category': 'CTA', 'event_label': 'first_timer'});">
                    <iconify-icon icon="ph:phone-fill" class="text-neonPink text-xl"></iconify-icon>
                    致電 0926-656666
                </a>
            </div>
            <p class="mt-4 text-xs text-gray-500 flex items-center justify-center gap-1">
                <iconify-icon icon="ph:lock-simple-fill" class="text-xs"></iconify-icon>
                所有對話絕對保密，不留存任何紀錄
            </p>
        </div>
    </div>
</section>
'''

# 模板4：預約流程頁（便利型）
CTA_BOOKING = '''
<!-- 預約最簡便：LINE -->
<section class="py-16 px-6 relative z-10">
    <div class="max-w-3xl mx-auto">
        <div class="glass-panel rounded-3xl p-8 md:p-10 border border-[#06C755]/30">
            <h3 class="text-2xl font-black text-center mb-2">
                <span class="text-[#06C755]">LINE</span> 預約 3 步驟
            </h3>
            <p class="text-gray-400 text-center text-sm mb-8">說需求 → 等確認 → 到府服務</p>

            <div class="grid grid-cols-3 gap-4 mb-8">
                <div class="text-center">
                    <div class="w-12 h-12 rounded-full bg-[#06C755]/20 text-[#06C755] font-black text-xl flex items-center justify-center mx-auto mb-2">1</div>
                    <div class="text-sm font-bold text-textWhite">LINE 說需求</div>
                    <div class="text-xs text-gray-400 mt-1">時間、地點、人數</div>
                </div>
                <div class="text-center">
                    <div class="w-12 h-12 rounded-full bg-electricPurple/20 text-electricPurple font-black text-xl flex items-center justify-center mx-auto mb-2">2</div>
                    <div class="text-sm font-bold text-textWhite">專人回覆</div>
                    <div class="text-xs text-gray-400 mt-1">5分鐘內確認</div>
                </div>
                <div class="text-center">
                    <div class="w-12 h-12 rounded-full bg-neonPink/20 text-neonPink font-black text-xl flex items-center justify-center mx-auto mb-2">3</div>
                    <div class="text-sm font-bold text-textWhite">到府安排</div>
                    <div class="text-xs text-gray-400 mt-1">平均30分鐘</div>
                </div>
            </div>

            <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
               class="block w-full py-5 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-xl text-center transition-all shadow-[0_0_30px_rgba(6,199,85,0.4)] hover:scale-[1.02]"
               onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'booking'});">
                <iconify-icon icon="bi:line" class="inline align-middle mr-2 text-2xl"></iconify-icon>
                立刻用 LINE 預約
            </a>
        </div>
    </div>
</section>
'''

# 模板5：飯局 / 商務型（場面、保密）
CTA_BUSINESS = '''
<!-- 商務預約：LINE -->
<section class="py-16 px-6 relative z-10">
    <div class="max-w-4xl mx-auto">
        <div class="glass-panel rounded-3xl p-8 md:p-10 border border-electricPurple/30">
            <div class="text-center mb-8">
                <h3 class="text-2xl md:text-3xl font-black mb-2">
                    商務場合・場面不失禮
                </h3>
                <p class="text-gray-400 text-sm">
                    尾牙、春酒、客戶接待、飯局 · 公關氣質出眾，保密機制完善
                </p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-8">
                <div class="flex items-center gap-3 p-4 rounded-xl bg-white/5">
                    <iconify-icon icon="ph:graduation-cap-fill" class="text-2xl text-electricPurple"></iconify-icon>
                    <div><div class="font-bold text-sm text-textWhite">氣質出眾</div><div class="text-xs text-gray-400">大學學歷以上公關可選</div></div>
                </div>
                <div class="flex items-center gap-3 p-4 rounded-xl bg-white/5">
                    <iconify-icon icon="ph:briefcase-fill" class="text-2xl text-electricPurple"></iconify-icon>
                    <div><div class="font-bold text-sm text-textWhite">場面應對得體</div><div class="text-xs text-gray-400">商務禮儀、敬酒、話題</div></div>
                </div>
                <div class="flex items-center gap-3 p-4 rounded-xl bg-white/5">
                    <iconify-icon icon="ph:lock-fill" class="text-2xl text-electricPurple"></iconify-icon>
                    <div><div class="font-bold text-sm text-textWhite">絕對保密</div><div class="text-xs text-gray-400">不留存任何個人資料</div></div>
                </div>
                <div class="flex items-center gap-3 p-4 rounded-xl bg-white/5">
                    <iconify-icon icon="ph:clock-fill" class="text-2xl text-electricPurple"></iconify-icon>
                    <div><div class="font-bold text-sm text-textWhite">24小時</div><div class="text-xs text-gray-400">緊急需求也能安排</div></div>
                </div>
            </div>
            <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
               class="block w-full py-5 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-xl text-center transition-all shadow-[0_0_30px_rgba(6,199,85,0.4)] hover:scale-[1.02]"
               onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'business'});">
                <iconify-icon icon="bi:line" class="inline align-middle mr-2 text-2xl"></iconify-icon>
                LINE 商務預約（指名制）
            </a>
        </div>
    </div>
</section>
'''

# 模板6：求職者 / 安全型
CTA_RECRUIT = '''
<!-- 求職專區：LINE 匿名詢問 -->
<section class="py-16 px-6 relative z-10">
    <div class="max-w-3xl mx-auto">
        <div class="glass-panel rounded-3xl p-8 md:p-10 border border-neonPink/30 text-center">
            <div class="w-16 h-16 rounded-full bg-neonPink/20 flex items-center justify-center mx-auto mb-6">
                <iconify-icon icon="ph:hand-waving-fill" class="text-4xl text-neonPink"></iconify-icon>
            </div>
            <h3 class="text-2xl md:text-3xl font-black mb-3">
                想了解？<span class="text-neonPink">LINE 匿名詢問</span>
            </h3>
            <p class="text-gray-400 mb-8 text-sm">
                任何關於工作內容、收入、彈性、安全的問題，<br>都可以先化名詢問，不留個資。
            </p>
            <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
               class="inline-flex items-center gap-3 px-10 py-5 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-xl transition-all shadow-[0_0_30px_rgba(6,199,85,0.4)] hover:scale-[1.03]"
               onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'recruit'});">
                <iconify-icon icon="bi:line" class="text-2xl"></iconify-icon>
                LINE 匿名詢問
            </a>
            <p class="mt-4 text-xs text-gray-500">
                或致電 <a href="tel:+886926656666" onclick="gtag('event', 'phone_click', {'event_category': 'CTA', 'event_label': 'recruit'});" class="text-gray-400 hover:text-white underline">0926-656666</a> · 我們會耐心解答
            </p>
        </div>
    </div>
</section>
'''

# 頁面 → CTA 模板對照
PAGE_CTA_MAP = {
    'index.html': CTA_HERO,
    'first_time_called.html': CTA_FIRST_TIMER,
    'first-time-2026.html': CTA_FIRST_TIMER,
    'compare-girls.html': CTA_CHOOSE_US,
    'booking-guide.html': CTA_BOOKING,
    'business-guide.html': CTA_BUSINESS,
    'business_dinner.html': CTA_BUSINESS,
    'recruitment.html': CTA_RECRUIT,
    'is_this_right_for_you.html': CTA_RECRUIT,
    'how_much.html': CTA_CHOOSE_US,
    'KTV_party.html': CTA_HERO,
    'KTV_recommendations.html': CTA_HERO,
    'motel_safe.html': CTA_HERO,
    'one_by_one.html': CTA_FIRST_TIMER,
    'shoot_guide.html': CTA_CHOOSE_US,
    'safety_privacy.html': CTA_FIRST_TIMER,
    'companion-levels-2026.html': CTA_CHOOSE_US,
    'legality-guide.html': CTA_FIRST_TIMER,
    'can-touch-guide.html': CTA_FIRST_TIMER,
    'interaction_scale.html': CTA_FIRST_TIMER,
    'special_industries.html': CTA_FIRST_TIMER,
    'suitable_female.html': CTA_CHOOSE_US,
    'taipei_agency_guide.html': CTA_CHOOSE_US,
    'male_companion.html': CTA_CHOOSE_US,
    'shoot_switch_personnel.html': CTA_CHOOSE_US,
    'tipping-guide-2026.html': CTA_HERO,
    'news.html': CTA_HERO,
}

def replace_cta_in_file(filepath, cta_html):
    """在 footer 前插入新的 CTA 區塊，同時移除舊的 LINE CTA"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 移除舊的 LINE CTA section（如果有）
    # 匹配從 <!-- LINE CTA 或 相關 section 到底部
    old_cta_patterns = [
        # 匹配「LINE 快速預約」類似的 section
        r'<!-- LINE.*?-->\s*<section[^>]*>.*?</section>',
        # 匹配 FAQ 後面的舊 CTA
        r'<!-- LINE.*?CTA.*?-->.*?</section>',
    ]
    for p in old_cta_patterns:
        content = re.sub(p, '', content, flags=re.DOTALL)

    # 找 footer 位置，在 footer 前插入新 CTA
    footer_match = re.search(r'(<footer[^>]*>)', content)
    if footer_match:
        insert_pos = footer_match.start()
        content = content[:insert_pos] + '\n' + cta_html + '\n' + content[insert_pos:]
    else:
        # 找不到 footer，就在 </body> 前插入
        content = re.sub(r'(</body>)', cta_html + r'\n\1', content)

    # 確保 LINE onclick 追蹤存在（更新為更詳細的 label）
    # (這已在模板中處理)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    updated = 0
    skipped = 0
    for fname, cta in PAGE_CTA_MAP.items():
        if not os.path.exists(fname) or fname == 'google1798bed44632c997.html':
            skipped += 1
            continue
        changed = replace_cta_in_file(fname, cta)
        if changed:
            print(f'[REDESIGN] {fname}')
            updated += 1
        else:
            print(f'[SKIP] {fname}: no changes')
            skipped += 1

    print(f'\n完成：{updated} 頁重新設計 LINE CTA，{skipped} 頁跳過')

if __name__ == '__main__':
    main()
