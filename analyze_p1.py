import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print('=== P1 Technical Analysis ===')
print('')

# 1. Image analysis
images = re.findall(r'<img[^>]*>', content)
print('[Images] Total img tags:', len(images))

webp_count = sum(1 for img in images if '.webp' in img.lower())
jpg_count = sum(1 for img in images if '.jpg' in img.lower() or '.jpeg' in img.lower())
png_count = sum(1 for img in images if '.png' in img.lower())
print('  WebP:', webp_count)
print('  JPG:', jpg_count)
print('  PNG:', png_count)

# Check lazy loading
lazy_count = sum(1 for img in images if 'loading="lazy"' in img or "loading='lazy'" in img)
print('  With lazy loading:', lazy_count)

# Check alt text
no_alt = [img for img in images if 'alt=' not in img]
print('  Without alt text:', len(no_alt))
if no_alt:
    print('  Examples:', no_alt[:2])

# 2. Script analysis (render blocking)
scripts = re.findall(r'<script[^>]*>', content)
print('')
print('[Scripts] Total script tags:', len(scripts))
scripts_without_defer_async = [s for s in scripts if 'defer' not in s and 'async' not in s and 'type="application/ld+json"' not in s]
print('  Without defer/async:', len(scripts_without_defer_async))
for s in scripts_without_defer_async[:3]:
    print('   ', s)

# 3. CSS analysis
css_links = re.findall(r'<link[^>]*rel="stylesheet"[^>]*>', content)
print('')
print('[CSS] Stylesheet links:', len(css_links))
for css in css_links:
    print('  ', css[:100])

# 4. External resources
external_js = re.findall(r'src="(https?://[^"]+)"', content)
print('')
print('[External JS] Count:', len(external_js))
for js in external_js[:5]:
    print('  ', js)

# 5. Preconnect hints
preconnect = re.findall(r'<link[^>]*rel="preconnect"[^>]*>', content)
print('')
print('[Preconnect] Count:', len(preconnect))
for p in preconnect:
    print('  ', p)

# 6. Font loading
fonts = re.findall(r'<link[^>]*fonts\.googleapis\.com[^>]*>', content)
print('')
print('[Google Fonts] Count:', len(fonts))
for f in fonts:
    print('  ', f[:120])

# 7. Check for dns-prefetch
dns_prefetch = re.findall(r'<link[^>]*rel="dns-prefetch"[^>]*>', content)
print('')
print('[DNS Prefetch] Count:', len(dns_prefetch))

# 8. Hero image check
hero_img = re.findall(r'src="images/hero[^"]*"', content)
print('')
print('[Hero Images]:', hero_img)

# 9. Check for preload hints
preload = re.findall(r'<link[^>]*rel="preload"[^>]*>', content)
print('')
print('[Preload] Count:', len(preload))
for p in preload:
    print('  ', p[:120])
