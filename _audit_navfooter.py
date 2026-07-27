import sys, glob, os
sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob('*.html'))
print(f'{len(files)} files')

for f in files:
    html = open(f,encoding='utf-8').read()
    i = html.find('<nav ')
    if i < 0:
        print(f'{f}: NO NAV')
        continue
    nav_section = html[i:html.find('</nav>',i)+6]
    
    has_dropdown = '情報特搜' in nav_section
    has_phone = '0926-656666' in nav_section
    has_pricing = 'how_much.html' in nav_section
    has_faq = 'faq-all-in-one' in nav_section
    has_pricing_anchor = '#pricing' in nav_section
    
    # footer check
    j = html.rfind('<footer')
    if j >= 0:
        footer_end = html.find('</footer>', j)
        footer = html[j:footer_end+9]
        footer_links = footer.count('<a href=')
    else:
        footer_links = 0
    
    print(f'{f}: nav_drop={has_dropdown} phone={has_phone} pricing_url={has_pricing} faq_url={has_faq} pricing_hash={has_pricing_anchor} footer_links={footer_links}')
