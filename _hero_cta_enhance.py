import sys
sys.stdout.reconfigure(encoding='utf-8')

html = open('index.html', 'r', encoding='utf-8').read()

# ── 1. Hero badge: pink → green ──────────────────────────────────────────────
old_badge = '''            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-panel mb-6 border-electricPurple/30">
                <span class="w-2 h-2 rounded-full bg-neonPink animate-pulse"></span>
                <span class="text-xs text-violetBlue tracking-widest font-bold uppercase">Taipei Premium Entertainment | 98% 客戶滿意度</span>
            </div>'''

new_badge = '''            <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-panel mb-6 border-[#06C755]/30">
                <span class="w-2 h-2 rounded-full bg-[#06C755] animate-pulse shadow-[0_0_8px_#06C755]"></span>
                <span class="text-xs text-[#06C755] tracking-widest font-bold uppercase">24小時預約中</span>
                <span class="text-gray-500">|</span>
                <span class="text-xs text-violetBlue tracking-widest font-bold uppercase">平均30分鐘到府</span>
            </div>'''

html = html.replace(old_badge, new_badge, 1)

# ── 2. CTA buttons: swap primary/secondary, enhance LINE ────────────────────
old_cta = '''            <div class="flex flex-col sm:flex-row gap-4 justify-center items-center">
                <!-- 這裡被替換為 台北傳播情報站 -->
                <a href="https://obaoba.online/news.html" class="btn-neon px-10 py-4 rounded-full font-bold text-lg flex items-center gap-2 group w-full sm:w-auto justify-center">
                    <iconify-icon icon="ph:newspaper-clipping-fill" class="group-hover:animate-bounce"></iconify-icon>
                    台北傳播情報站
                </a>
                <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer" class="px-10 py-4 rounded-full font-bold text-lg glass-panel hover:bg-white/5 transition-colors flex items-center gap-2 text-[#06C755] border-[#06C755]/30 w-full sm:w-auto justify-center" onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'LINE'});">
                    <iconify-icon icon="bi:line" class="text-2xl"></iconify-icon>
                    加 LINE 預約
                </a>
            </div>'''

new_cta = '''            <!--  primary CTA: LINE (glowing green) -->
            <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
               class="inline-flex items-center gap-3 px-12 py-5 rounded-2xl bg-[#06C755] hover:bg-[#05a546] text-white font-black text-xl md:text-2xl transition-all shadow-[0_0_40px_rgba(6,199,85,0.5)] hover:shadow-[0_0_60px_rgba(6,199,85,0.7)] hover:scale-[1.03] active:scale-[0.98] mb-4"
               onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'hero_primary'});">
                <iconify-icon icon="bi:line" class="text-3xl"></iconify-icon>
                加 LINE 預約
            </a>
            <!-- secondary CTA: news -->
            <a href="https://obaoba.online/news.html"
               class="inline-flex items-center gap-2 px-8 py-3 rounded-full font-bold text-base transition-all text-gray-300 border border-white/20 hover:border-white/40 hover:bg-white/5 hover:text-white mb-8">
                <iconify-icon icon="ph:newspaper-clipping-fill"></iconify-icon>
                台北傳播情報站
            </a>
            <!-- Trust badges -->
            <div class="flex flex-wrap justify-center gap-3 mt-2">
                <span class="px-3 py-1 rounded-full bg-[#06C755]/15 text-[#06C755] text-xs font-bold border border-[#06C755]/30">
                    <iconify-icon icon="ph:clock-countdown-fill" class="inline align-middle mr-1"></iconify-icon>平均30分鐘到府
                </span>
                <span class="px-3 py-1 rounded-full bg-electricPurple/15 text-electricPurple text-xs font-bold border border-electricPurple/30">
                    <iconify-icon icon="ph:shield-check-fill" class="inline align-middle mr-1"></iconify-icon>見面後再付款
                </span>
                <span class="px-3 py-1 rounded-full bg-neonPink/15 text-neonPink text-xs font-bold border border-neonPink/30">
                    <iconify-icon icon="ph:users-three-fill" class="inline align-middle mr-1"></iconify-icon>已服務3,000+客戶
                </span>
            </div>'''

html = html.replace(old_cta, new_cta, 1)

# ── 3. Sticky bottom bar (after hero section closes) ─────────────────────────
old_hero_close = '''        </div>
    </section>

    <!-- Bento Grid'''

new_sticky = '''        </div>
    </section>

    <!-- Sticky Bottom CTA Bar -->
    <div id="sticky-bar" class="fixed bottom-0 left-0 right-0 z-[100] translate-y-full transition-transform duration-500 ease-out">
        <div class="bg-midnight/95 backdrop-blur-2xl border-t border-white/15 shadow-[0_-4px_40px_rgba(0,0,0,0.8)] px-4 py-3">
            <div class="max-w-5xl mx-auto flex items-center justify-between gap-3">
                <div class="flex items-center gap-2 min-w-0">
                    <span class="w-2 h-2 rounded-full bg-[#06C755] animate-pulse shadow-[0_0_6px_#06C755] flex-shrink-0"></span>
                    <span class="text-xs text-gray-300 font-medium truncate">今晚安排？LINE 最快</span>
                </div>
                <div class="flex items-center gap-2 flex-shrink-0">
                    <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
                       class="flex items-center gap-1.5 px-4 py-2 rounded-full bg-[#06C755] hover:bg-[#05a546] text-white font-bold text-sm transition-all shadow-[0_0_20px_rgba(6,199,85,0.4)]"
                       onclick="gtag('event', 'LINE_click', {'event_category': 'CTA', 'event_label': 'sticky_bar'});">
                        <iconify-icon icon="bi:line" class="text-base"></iconify-icon>
                        <span class="hidden sm:inline">加 LINE</span>
                        <span class="sm:hidden">LINE</span>
                    </a>
                    <a href="tel:+886926656666"
                       class="flex items-center gap-1.5 px-3 py-2 rounded-full border border-white/20 text-white/80 font-medium text-sm hover:bg-white/10 transition-colors"
                       onclick="gtag('event', 'phone_click', {'event_category': 'CTA', 'event_label': 'sticky_bar'});">
                        <iconify-icon icon="ph:phone-fill" class="text-neonPink text-sm"></iconify-icon>
                        <span class="hidden sm:inline">0926-656666</span>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <script>
    (function() {
        var bar = document.getElementById('sticky-bar');
        if (!bar) return;
        var hero = document.querySelector('section');
        if (!hero) return;

        var sentinel = document.createElement('div');
        sentinel.style.cssText = 'position:absolute;top:' + (hero.offsetTop + hero.offsetHeight - 120) + 'px;width:1px;height:1px;';
        document.body.appendChild(sentinel);

        var obs = new IntersectionObserver(function(entries) {
            entries.forEach(function(e) {
                if (e.target === sentinel) {
                    if (e.intersectionRatio === 0) {
                        bar.style.transform = 'translateY(0)';
                    } else {
                        bar.style.transform = 'translateY(100%)';
                    }
                }
            });
        }, {threshold: [0, 1]});

        obs.observe(sentinel);
    })();
    </script>

    <!-- Bento Grid'''

html = html.replace(old_hero_close, new_sticky, 1)

open('index.html', 'w', encoding='utf-8').write(html)
print('Done. Changes applied.')
print('  - Hero badge: pink → green 24/7')
print('  - Primary CTA: LINE (glowing green, large)')
print('  - Secondary CTA: news (ghost style)')
print('  - Trust badges: 3 badges below CTA')
print('  - Sticky bar: appears after scrolling past hero')
