# -*- coding: utf-8 -*-
with open(r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\special_industries.html', encoding='utf-8') as f:
    src = f.read()

print('File len:', len(src))

# Check the area around the comment block
idx = src.find('<!-- 以上區塊')
print('Comment block at:', idx)
print(repr(src[idx-50:idx+250]))

# Also check if new sections are in the file
if '四、酒店與傳播的核心差異' in src:
    print('New sections found!')
    idx2 = src.find('四、酒店與傳播的核心差異')
    print(repr(src[idx2-100:idx2+50]))
else:
    print('New sections NOT found')
