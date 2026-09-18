import re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

img_tags = re.findall(r'<img[^>]*>', content)
print('=== Image Analysis ===')
for i, img in enumerate(img_tags):
    src = re.search(r'src="([^"]+)"', img)
    loading = re.search(r'loading="([^"]+)"', img)
    alt = re.search(r'alt="([^"]+)"', img)
    fetchpriority = re.search(r'fetchpriority="([^"]+)"', img)
    
    src_val = src.group(1) if src else 'NO SRC'
    loading_val = loading.group(1) if loading else 'NO LOADING'
    alt_val = alt.group(1) if alt else 'NO ALT'
    fetch_val = fetchpriority.group(1) if fetchpriority else 'NO FETCHPRIORITY'
    
    print(str(i+1) + '. ' + src_val)
    print('   loading=' + loading_val + ', alt="' + alt_val + '", fetchpriority=' + fetch_val)
    print('')
