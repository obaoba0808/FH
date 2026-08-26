import re, json, glob, os
ROOT = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
pat = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)
sets = {}
for f in sorted(glob.glob(os.path.join(ROOT, '*.html'))):
    s = open(f, encoding='utf-8').read()
    vals = set()
    for m in pat.finditer(s):
        try: d = json.loads(m.group(1))
        except: continue
        def walk(o):
            if isinstance(o, dict):
                if (o.get('@type')=='Organization' or (isinstance(o.get('@type'),list) and 'Organization' in o.get('@type'))) and 'sameAs' in o:
                    vals.add(tuple(o['sameAs']))
                for v in o.values(): walk(v)
            elif isinstance(o, list):
                for v in o: walk(v)
        walk(d)
    sets[os.path.basename(f)] = vals
# distinct sameAs tuples
distinct = {}
for f, vals in sets.items():
    for v in vals:
        distinct.setdefault(v, []).append(f)
print('Distinct sameAs sets:', len(distinct))
for v, files in distinct.items():
    print(' *', v, '->', len(files), 'pages')
