import re

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
c = open(ROOT + '/index.html', encoding='utf-8').read()

# Find the dropdown div
m = re.search(r'情報特搜站', c)
if m:
    snippet = c[m.start()-50:m.start()+4000]
    for i, line in enumerate(snippet.split('\n')):
        print(i, repr(line[:120]))
