import urllib.request
BASE = 'https://obaoba.online/'
CL = 'ykmbmbct7c'
GA = 'G-534539378'
targets = ['', 'taipei-daan.html', 'taipei-xinyi.html', 'taipei-banqiao.html']
ok = fail = 0
for p in targets:
    url = BASE + p
    label = p if p else '(home)'
    req = urllib.request.Request(url, headers={'User-Agent': 'OBAOBA-QA/1.0', 'Cache-Control': 'no-cache'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            c = r.read().decode('utf-8', 'replace')
            cl = 'OK' if CL in c else 'MISSING'
            ga = 'OK' if GA in c else 'MISSING'
            line = '{:<26} HTTP={} len={:<7} Clarity={:<8} GA4={}'.format(label, r.status, len(c), cl, ga)
            if cl == 'OK' and ga == 'OK' and r.status == 200:
                ok += 1
            else:
                fail += 1
            print(line)
    except Exception as e:
        fail += 1
        print('{}: ERROR {}'.format(label, e))
print('-' * 60)
print('PASS {} | FAIL {}'.format(ok, fail))
