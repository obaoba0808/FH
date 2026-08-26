import re, json

for f in ['index.html', 'about-oppa.html']:
    s = open(f, encoding='utf-8').read()
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S)
    print(f, 'blocks:', len(blocks))
    for i, b in enumerate(blocks):
        try:
            d = json.loads(b)
            ar = d.get('aggregateRating')
            rc = d.get('review')
            print('  block', i, 'type=', d.get('@type'),
                  'rating=', (ar.get('ratingValue') if ar else None),
                  'count=', (ar.get('reviewCount') if ar else None),
                  'reviews=', (len(rc) if rc else 0))
        except Exception as e:
            print('  block', i, 'JSON ERR', e)
