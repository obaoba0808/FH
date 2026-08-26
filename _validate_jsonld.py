import re, json, glob, os

ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
pat = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)

bad = 0
tel_pages = 0
for f in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    s = open(f, encoding='utf-8').read()
    for i, m in enumerate(pat.finditer(s)):
        try:
            d = json.loads(m.group(1))
        except Exception as e:
            bad += 1
            print('BAD JSON', os.path.basename(f), i, e)
            continue
        # check for telephone anywhere
    # count pages whose any Organization has telephone
    has_tel = False
    for m in pat.finditer(s):
        try:
            d = json.loads(m.group(1))
        except: 
            continue
        txt = json.dumps(d, ensure_ascii=False)
        if '"telephone"' in txt:
            has_tel = True
    if has_tel:
        tel_pages += 1

print('Pages with telephone in schema:', tel_pages)

# show index sameAs
s = open(os.path.join(ROOT,'index.html'), encoding='utf-8').read()
for m in pat.finditer(s):
    d = json.loads(m.group(1))
    def walk(o):
        if isinstance(o, dict):
            if o.get('@type') == 'Organization' or (isinstance(o.get('@type'),list) and 'Organization' in o.get('@type')):
                if 'sameAs' in o:
                    print('INDEX sameAs:', o['sameAs'])
            for v in o.values(): walk(v)
        elif isinstance(o, list):
            for v in o: walk(v)
    walk(d)
