import os, re, json, glob, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

root = 'C:/Users/FH01/.qclaw/workspace-cwapojim0yfmyvq8/FH-website'
htmls = sorted(glob.glob(os.path.join(root, '*.html')))
print('total html:', len(htmls))

# patterns
phone_patterns = {
    '0926656666 (no dash)': r'0926-?656-?666',
    '+886926656666': r'\+886926656666',
    '0926-656-666': r'0926-656-666',
}
name_vars = {
    '歐巴傳播 (plain)': '歐巴傳播',
    'OPPA ENT.': 'OPPA ENT',
    'OPPA ENT (no dot)': '歐巴傳播OPPA',
}
line_id = '@938nzmjr'

for f in htmls:
    s = open(f, encoding='utf-8').read()
    fn = os.path.basename(f)
    title_m = re.search(r'<title>(.*?)</title>', s, re.S)
    title = title_m.group(1).strip() if title_m else ''
    # schema blocks
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    schema_types = []
    schema_names = []
    schema_tel = []
    schema_addr = []
    for b in blocks:
        try:
            d = json.loads(b)
        except Exception:
            continue
        def walk(x):
            if isinstance(x, dict):
                if x.get('@type'):
                    t = x['@type']
                    schema_types.append(t if isinstance(t,str) else ','.join(t))
                    if 'name' in x: schema_names.append(str(x['name']))
                    if 'telephone' in x: schema_tel.append(str(x['telephone']))
                    if 'address' in x: schema_addr.append(str(x['address']))
                for v in x.values(): walk(v)
            elif isinstance(x, list):
                for v in x: walk(v)
        walk(d)
    # counts
    phone_hits = {k: len(re.findall(p, s)) for k,p in phone_patterns.items()}
    name_hits = {k: s.count(v) for k,v in name_vars.items()}
    line_hits = s.count(line_id)
    # footer NAP block?
    has_nap_block = '營業' in s or '服務時間' in s or '預約專線' in s
    print('='*70)
    print(fn, '| title:', title[:40])
    print('  phone:', phone_hits)
    print('  names:', name_hits)
    print('  line@:', line_hits, '| tel:link' , s.count('tel:+886926656666'))
    print('  schemaTypes:', schema_types)
    print('  schemaNames:', schema_names)
    print('  schemaTel:', schema_tel)
