import sys, glob, os
sys.stdout.reconfigure(encoding='utf-8')

# ─── The new footer HTML (user-provided) ───
# Note: We need to adjust href paths based on page depth.
# index.html / about-oppa.html / news.html / faq-all-in-one.html → depth 0
# All others → depth 0 (they're all in root)
# Actually, checking: ALL pages are in root directory (no subdirs)
# So all hrefs can be direct like "first_time_called.html"

NEW_FOOTER = '''<!-- Footer -->
<footer class="bg-[#07030f] border-t border-white/10 py-16 mt-20">
<div class="max-w-7xl mx-auto px-6">
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10 mb-12">
<div>
<div class="flex items-center gap-2 mb-4">
<iconify-icon icon="mdi:crown" class="text-neonPink text-2xl"></iconify-icon>
<span class="font-display text-xl tracking-widest font-bold">歐巴傳播</span>
</div>
<p class="text-gray-400 text-sm leading-relaxed">台北夜生活娛樂服務領導品牌。傳播妹、飯局妹、派對陪伴，正派經營，價格透明。</p>
<div class="mt-4 space-y-2">
<p class="text-sm text-gray-400 flex items-center gap-2"><iconify-icon icon="ph:phone-fill" class="text-neonPink"></iconify-icon> 0926-656-666</p>
<p class="text-sm text-gray-400 flex items-center gap-2"><iconify-icon icon="bi:line" class="text-green-400"></iconify-icon> @938nzmjr</p>
</div>
</div>
<div>
<h4 class="font-bold text-white mb-4">新手指南</h4>
<ul class="space-y-2.5 text-sm text-gray-400">
<li><a href="first_time_called.html" class="hover:text-neonPink transition-colors">第一次叫傳播？新手必看</a></li>
<li><a href="compare-girls.html" class="hover:text-neonPink transition-colors">傳播妹 vs 酒店小姐</a></li>
<li><a href="booking-guide.html" class="hover:text-neonPink transition-colors">預約流程完整攻略</a></li>
<li><a href="how_much.html" class="hover:text-neonPink transition-colors">2026 收費行情大公開</a></li>
<li><a href="business-guide.html" class="hover:text-neonPink transition-colors">商務公關推薦攻略</a></li>
<li><a href="legality-guide.html" class="hover:text-neonPink transition-colors">傳播妹合法嗎？</a></li>
</ul>
</div>
<div>
<h4 class="font-bold text-white mb-4">場合攻略</h4>
<ul class="space-y-2.5 text-sm text-gray-400">
<li><a href="KTV_recommendations.html" class="hover:text-neonPink transition-colors">台北 KTV 場所推薦</a></li>
<li><a href="motel_safe.html" class="hover:text-neonPink transition-colors">Motel 安全指南</a></li>
<li><a href="business_dinner.html" class="hover:text-neonPink transition-colors">飯局妹場合攻略</a></li>
<li><a href="one_by_one.html" class="hover:text-neonPink transition-colors">單身客專屬玩法</a></li>
<li><a href="KTV_party.html" class="hover:text-neonPink transition-colors">KTV 派對玩法</a></li>
</ul>
</div>
<div>
<h4 class="font-bold text-white mb-4">服務與安全</h4>
<ul class="space-y-2.5 text-sm text-gray-400">
<li><a href="safety_privacy.html" class="hover:text-neonPink transition-colors">安全與隱私完整指南</a></li>
<li><a href="can-touch-guide.html" class="hover:text-neonPink transition-colors">互動尺度說明</a></li>
<li><a href="shoot_guide.html" class="hover:text-neonPink transition-colors">打槍換人完全攻略</a></li>
<li><a href="companion-levels-2026.html" class="hover:text-neonPink transition-colors">公關等級與價格對照</a></li>
<li><a href="faq-all-in-one.html" class="hover:text-neonPink transition-colors">常見問題 FAQ</a></li>
<li><a href="about-oppa.html" class="hover:text-neonPink transition-colors">關於歐巴傳播</a></li>
</ul>
</div>
</div>
<div class="border-t border-white/10 pt-8 text-center text-gray-500 text-sm">
<p class="text-xs text-gray-500 mb-3">相關網站：
<a href="https://obaoba0808.github.io/Yulin-Design/" class="hover:text-neonPink transition-colors" rel="noopener">侑霖室內設計</a> ・
<a href="https://obaoba0808.github.io/Sweet-Burst-Fruits/" class="hover:text-neonPink transition-colors" rel="noopener">爆甜水果行</a> ・
<a href="https://golightly.fun/" class="hover:text-neonPink transition-colors" rel="noopener">均在路上</a>
</p>
<p>&copy; 2024-2026 歐巴傳播 All Rights Reserved</p>
<p class="mt-2 text-xs">本站內容僅供參考，不涉及任何非法服務</p>
</div>
</div>
</footer>'''

def fix_hrefs(html, fname):
    """Fix relative hrefs: index.html/ about/ news/ faq pages use root paths."""
    # These pages are in root dir — same as NEW_FOOTER paths
    # But about-oppa/ news/ faq-all-in-one use /xxx.html links in nav
    # NEW_FOOTER uses relative paths like "about-oppa.html"
    # For those pages, we need to keep the relative paths working.
    # All pages are in same root dir, so no change needed.
    return html

def replace_footer(html, fname):
    """Replace footer section only (not scripts or </html>)."""
    fi = html.find('<footer')
    if fi < 0:
        print(f'{fname}: NO FOOTER to replace')
        return html
    
    # Find the end of footer
    fe = html.index('</footer>', fi) + 9
    
    # Check what's after footer: should be scripts + </html>
    after_footer = html[fe:].lstrip()
    has_scripts = after_footer.startswith('<!-- Scripts') or after_footer.startswith('<script>')
    has_html_close = '</html>' in after_footer
    
    if has_scripts and has_html_close:
        # Replace footer but keep scripts + </html>
        new_html = html[:fi] + NEW_FOOTER + '\n\n\n' + html[fe:]
    else:
        # Footer replacement includes closing tags
        new_html = html[:fi] + NEW_FOOTER + '\n\n\n' + html[fe:]
    
    return new_html

# ─── Apply to all pages ───
files = sorted(glob.glob('*.html'))
skip = {'google1798bed44632c997.html'}
count = 0

for fname in files:
    base = fname.lower()
    if base in skip or 'google' in base:
        print(f'{fname}: SKIP')
        continue
    
    html = open(fname, 'r', encoding='utf-8').read()
    original = html
    
    # Check if already has the new footer
    if '新手指南' in html and '場合攻略' in html:
        print(f'{fname}: ALREADY NEW footer, skipping')
        continue
    
    new_html = replace_footer(html, fname)
    
    if new_html != original:
        open(fname, 'w', encoding='utf-8').write(new_html)
        count += 1
        print(f'{fname}: UPDATED')
    else:
        print(f'{fname}: no change')

print(f'\nDone. Modified {count} files.')
