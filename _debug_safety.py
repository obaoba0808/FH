import re
ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
c = open(ROOT + '/safety-guide-2026.html', encoding='utf-8').read()
m = re.search(r'情報特搜站', c)
if m:
    snippet = c[m.start()-100:m.start()+2500]
    for i, line in enumerate(snippet.split('\n')):
        if 'href' in line:
            print(i, repr(line.strip()[:110]))
else:
    print('NO 情報特搜站 in safety-guide')
    # find nav links
    for m2 in re.finditer(r'<a href="([^"]+)"[^>]*>([^<]*)</a>', c):
        print('LINK:', m2.group(1), '|', m2.group(2)[:40])
