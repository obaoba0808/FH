import requests
import os

images_dir = r'C:\Users\FH01\.qclaw\workspaces\main-workspace\FH-website\images'
os.makedirs(images_dir, exist_ok=True)

# Unsplash fallback - 台北夜景氛圍
url_hero = 'https://images.unsplash.com/photo-1470004914212-05527e49370b?q=80&w=1920&auto=format&fit=crop'
r1 = requests.get(url_hero, timeout=60)
hero_path = os.path.join(images_dir, 'hero-pricing-2026.jpg')
with open(hero_path, 'wb') as f:
    f.write(r1.content)
print('HERO size:', len(r1.content), 'bytes')
with open(hero_path, 'rb') as f:
    h = f.read(2)
    print('HERO valid JPEG:', h == b'\xff\xd8')

# Unsplash fallback - 酒吧氛圍美女
url_content = 'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?q=80&w=1200&auto=format&fit=crop'
r2 = requests.get(url_content, timeout=60)
content_path = os.path.join(images_dir, 'content-pricing-2026.jpg')
with open(content_path, 'wb') as f:
    f.write(r2.content)
print('Content size:', len(r2.content), 'bytes')
with open(content_path, 'rb') as f:
    h = f.read(2)
    print('Content valid JPEG:', h == b'\xff\xd8')

print('Done!')
