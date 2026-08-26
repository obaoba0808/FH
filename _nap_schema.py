import re, json, glob, os

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
TEL = '+886926656666'
SAMEAS = ['https://line.me/ti/p/~938nzmjr',
          'https://www.google.com/maps/search/?api=1&query=%E6%AD%90%E5%B7%B4%E5%82%B3%E6%92%AD']

def augment(obj):
    if isinstance(obj, dict):
        if 'Organization' in obj.get('@type', []) if isinstance(obj.get('@type'), list) else obj.get('@type') == 'Organization':
            if 'telephone' not in obj:
                obj['telephone'] = TEL
            if 'sameAs' not in obj:
                obj['sameAs'] = SAMEAS
        for k, v in list(obj.items()):
            augment(v)
    elif isinstance(obj, list):
        for v in obj:
            augment(v)

pat = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
total_changes = 0
for f in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    s = open(f, encoding='utf-8').read()
    new = []
    file_changed = False
    for m in pat.finditer(s):
        raw = m.group(1)
        try:
            d = json.loads(raw)
        except Exception:
            new.append(raw)
            continue
        before = json.dumps(d, ensure_ascii=False)
        augment(d)
        after = json.dumps(d, ensure_ascii=False)
        if before != after:
            file_changed = True
            total_changes += 1
        new.append(after)
    if file_changed:
        # reassemble
        out = []
        last = 0
        for m, repl in zip(pat.finditer(s), new):
            out.append(s[last:m.start(1)])
            out.append(repl)
            last = m.end(1)
        out.append(s[last:])
        open(f, 'w', encoding='utf-8').write(''.join(out))
        print(os.path.basename(f), 'updated')
print('TOTAL files with schema augmented:', total_changes)
