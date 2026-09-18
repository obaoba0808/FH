import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# All image references
all_images = re.findall(r'(images/[^\'"\s)]+)', content)
print('=== All image references ===')
for img in sorted(set(all_images)):
    print(' ', img)

print('')
print('Total unique images:', len(set(all_images)))

# Check for picture/source tags
picture_tags = re.findall(r'<picture[^>]*>.*?</picture>', content, re.DOTALL)
print('')
print('Picture tags:', len(picture_tags))

# Check for srcset
srcset = re.findall(r'srcset="([^"]*)"', content)
print('Srcset attributes:', len(srcset))

# Check CSS background images
bg_images = re.findall(r'background-image:\s*url\(["\']?([^"\')]+)', content)
print('')
print('CSS background images:')
for bg in sorted(set(bg_images)):
    print(' ', bg)
