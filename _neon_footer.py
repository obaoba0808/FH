import glob

NEON_FOOTER = """<!-- Footer -->
<footer class="relative mt-20 overflow-hidden">
    <!-- Neon top border -->
    <div class="h-px bg-gradient-to-r from-transparent via-[#7B2CFF] via-[#FF2DAF] to-transparent shadow-[0_0_20px_rgba(255,45,175,0.5)]"></div>
    
    <div class="bg-gradient-to-b from-[#0D0616] to-[#07030f] py-16 relative">
        <!-- Ambient glow left -->
        <div class="absolute top-0 left-1/4 w-96 h-40 bg-[#7B2CFF]/5 rounded-full blur-3xl pointer-events-none"></div>
        <!-- Ambient glow right -->
        <div class="absolute bottom-0 right-1/4 w-80 h-32 bg-[#FF2DAF]/5 rounded-full blur-3xl pointer-events-none"></div>
        
        <div class="max-w-7xl mx-auto px-6 relative z-10">
            <!-- Main 4-column grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 mb-12">
                
                <!-- Column 1: Brand -->
                <div class="glass-panel rounded-2xl p-6 border border-white/10 relative overflow-hidden group">
                    <!-- Glow corner -->
                    <div class="absolute -top-4 -right-4 w-20 h-20 bg-[#FF2DAF]/10 rounded-full blur-xl group-hover:bg-[#FF2DAF]/20 transition-all duration-500"></div>
                    
                    <div class="flex items-center gap-2 mb-4">
                        <iconify-icon icon="mdi:crown" class="text-neonPink text-3xl drop-shadow-[0_0_10px_rgba(255,45,175,0.8)] group-hover:scale-110 transition-transform"></iconify-icon>
                        <span class="font-display text-xl tracking-widest font-bold text-white">歐巴傳播</span>
                    </div>
                    <p class="text-gray-400 text-sm leading-relaxed mb-5">台北夜生活娛樂服務領導品牌。傳播妹、飯局妹、派對陪伴，正派經營，價格透明。</p>
                    
                    <!-- LINE CTA -->
                    <a href="https://line.me/R/ti/p/@938nzmjr" target="_blank" rel="noopener noreferrer"
                       class="flex items-center justify-center gap-2 w-full py-3 rounded-xl bg-[#06C755] hover:bg-[#05a546] text-white font-bold text-sm transition-all shadow-[0_0_15px_rgba(6,199,85,0.3)] hover:shadow-[0_0_25px_rgba(6,199,85,0.5)] hover:scale-[1.02] active:scale-[0.98] mb-3">
                        <iconify-icon icon="bi:line" class="text-xl"></iconify-icon> 加 LINE 預約
                    </a>
                    
                    <div class="space-y-2">
                        <p class="text-sm text-gray-400 flex items-center gap-2">
                            <iconify-icon icon="ph:phone-fill" class="text-neonPink"></iconify-icon>
                            <a href="tel:+886926656666" class="hover:text-neonPink transition-colors">0926-656-666</a>
                        </p>
                        <p class="text-sm text-gray-400 flex items-center gap-2">
                            <iconify-icon icon="ph:clock-fill" class="text-electricPurple"></iconify-icon>
                            24小時服務
                        </p>
                    </div>
                </div>
                
                <!-- Column 2: 新手指南 -->
                <div class="glass-panel rounded-2xl p-6 border border-white/10 relative overflow-hidden group">
                    <div class="absolute -top-4 -right-4 w-20 h-20 bg-[#7B2CFF]/10 rounded-full blur-xl group-hover:bg-[#7B2CFF]/20 transition-all duration-500"></div>
                    <div class="flex items-center gap-2 mb-5">
                        <div class="w-8 h-px bg-gradient-to-r from-[#7B2CFF] to-transparent"></div>
                        <h4 class="font-bold text-white tracking-wide">新手指南</h4>
                    </div>
                    <ul class="space-y-3 text-sm">
                        <li><a href="first_time_called.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-electricPurple text-xs">&#9656;</span> 第一次叫傳播？新手必看</a></li>
                        <li><a href="compare-girls.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-electricPurple text-xs">&#9656;</span> 傳播妹 vs 酒店小姐</a></li>
                        <li><a href="booking-guide.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-electricPurple text-xs">&#9656;</span> 預約流程完整攻略</a></li>
                        <li><a href="how_much.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-electricPurple text-xs">&#9656;</span> 2026 收費行情大公開</a></li>
                        <li><a href="business-guide.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-electricPurple text-xs">&#9656;</span> 商務公關推薦攻略</a></li>
                        <li><a href="legality-guide.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-electricPurple text-xs">&#9656;</span> 傳播妹合法嗎？</a></li>
                    </ul>
                </div>
                
                <!-- Column 3: 場合攻略 -->
                <div class="glass-panel rounded-2xl p-6 border border-white/10 relative overflow-hidden group">
                    <div class="absolute -top-4 -right-4 w-20 h-20 bg-[#06C755]/8 rounded-full blur-xl group-hover:bg-[#06C755]/15 transition-all duration-500"></div>
                    <div class="flex items-center gap-2 mb-5">
                        <div class="w-8 h-px bg-gradient-to-r from-[#06C755] to-transparent"></div>
                        <h4 class="font-bold text-white tracking-wide">場合攻略</h4>
                    </div>
                    <ul class="space-y-3 text-sm">
                        <li><a href="KTV_recommendations.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-[#06C755] text-xs">&#9656;</span> 台北 KTV 場所推薦</a></li>
                        <li><a href="motel_safe.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-[#06C755] text-xs">&#9656;</span> Motel 安全指南</a></li>
                        <li><a href="business_dinner.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-[#06C755] text-xs">&#9656;</span> 飯局妹場合攻略</a></li>
                        <li><a href="one_by_one.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-[#06C755] text-xs">&#9656;</span> 單身客專屬玩法</a></li>
                        <li><a href="KTV_party.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-[#06C755] text-xs">&#9656;</span> KTV 派對玩法</a></li>
                    </ul>
                </div>
                
                <!-- Column 4: 服務與安全 -->
                <div class="glass-panel rounded-2xl p-6 border border-white/10 relative overflow-hidden group">
                    <div class="absolute -top-4 -right-4 w-20 h-20 bg-[#FF2DAF]/8 rounded-full blur-xl group-hover:bg-[#FF2DAF]/15 transition-all duration-500"></div>
                    <div class="flex items-center gap-2 mb-5">
                        <div class="w-8 h-px bg-gradient-to-r from-[#FF2DAF] to-transparent"></div>
                        <h4 class="font-bold text-white tracking-wide">服務與安全</h4>
                    </div>
                    <ul class="space-y-3 text-sm">
                        <li><a href="safety_privacy.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-neonPink text-xs">&#9656;</span> 安全與隱私完整指南</a></li>
                        <li><a href="can-touch-guide.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-neonPink text-xs">&#9656;</span> 互動尺度說明</a></li>
                        <li><a href="shoot_guide.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-neonPink text-xs">&#9656;</span> 打槍換人完全攻略</a></li>
                        <li><a href="companion-levels-2026.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-neonPink text-xs">&#9656;</span> 公關等級與價格對照</a></li>
                        <li><a href="faq-all-in-one.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-neonPink text-xs">&#9656;</span> 常見問題 FAQ</a></li>
                        <li><a href="about-oppa.html" class="flex items-center gap-2 text-gray-400 hover:text-white hover:translate-x-1 transition-all duration-200"><span class="text-neonPink text-xs">&#9656;</span> 關於歐巴傳播</a></li>
                    </ul>
                </div>
                
            </div>
            
            <!-- Bottom bar -->
            <div class="border-t border-white/10 pt-8">
                <!-- Related sites -->
                <div class="flex flex-wrap justify-center gap-x-3 gap-y-1 mb-5 text-sm">
                    <span class="text-gray-500">相關網站：</span>
                    <a href="https://obaoba0808.github.io/Yulin-Design/" class="hover:text-neonPink transition-colors" rel="noopener">侑霖室內設計</a>
                    <span class="text-gray-600">&#x30FB;</span>
                    <a href="https://obaoba0808.github.io/Sweet-Burst-Fruits/" class="hover:text-neonPink transition-colors" rel="noopener">爆甜水果行</a>
                    <span class="text-gray-600">&#x30FB;</span>
                    <a href="https://golightly.fun/" class="hover:text-neonPink transition-colors" rel="noopener">均在路上</a>
                </div>
                
                <div class="flex flex-wrap justify-center items-center gap-x-4 gap-y-2 text-xs text-gray-500">
                    <p><span class="text-neonPink">&copy;</span> 2024-2026 <span class="text-white font-semibold">歐巴傳播</span> All Rights Reserved</p>
                    <span class="hidden sm:inline text-gray-600">&#124;</span>
                    <p>本站內容僅供參考，不涉及任何非法服務</p>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Neon bottom glow -->
    <div class="h-px bg-gradient-to-r from-transparent via-[#FF2DAF] via-[#7B2CFF] to-transparent shadow-[0_0_15px_rgba(123,44,255,0.4)]"></div>
</footer>
"""

def replace_footer(html):
    fi = html.find('<footer')
    if fi < 0:
        return html, False
    fe = html.index('</footer>', fi) + 9
    return html[:fi] + NEON_FOOTER + '\n\n\n' + html[fe:], True

files = sorted(glob.glob('*.html'))
count = 0

for fname in files:
    if 'google' in fname.lower():
        print(fname + ': SKIP')
        continue
    html = open(fname, 'r', encoding='utf-8').read()
    new_html, ok = replace_footer(html)
    if ok:
        open(fname, 'w', encoding='utf-8').write(new_html)
        count += 1
        print(fname + ': OK')
    else:
        print(fname + ': no footer found')

print('\nDone. ' + str(count) + ' files updated.')
