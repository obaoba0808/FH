import re, sys
sys.stdout.reconfigure(encoding='utf-8')
html = open('index.html', 'r', encoding='utf-8').read()

# Proper full-block regex
blocks = re.findall(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    html, re.DOTALL
)
print(f'JSON-LD blocks: {len(blocks)}')
for i, b in enumerate(blocks):
    b_stripped = b.strip()
    if b_stripped.startswith('{'):
        try:
            import json
            obj = json.loads(b_stripped)
            print(f'  [{i+1}] @type: {obj.get("@type", "unknown")}')
        except:
            print(f'  [{i+1}] (parse failed, startswith={{: {b_stripped[:80]})')
    else:
        print(f'  [{i+1}] (not JSON: {b_stripped[:60]})')

checks = {}
checks['org_once'] = html.count('"@type":"Organization"') == 1
checks['website_once'] = html.count('"@type":"WebSite"') == 1
checks['faqpage_once'] = html.count('"@type":"FAQPage"') == 1
checks['search_action'] = '"SearchAction"' in html
checks['same_as'] = '"sameAs"' in html
checks['no_dup_desc'] = '立即致電LINE預約。，立即致電LINE預約' not in html
checks['3_blocks'] = len(blocks) == 3
checks['org_is_first'] = blocks[0].strip().startswith('{') and '"Organization"' in blocks[0]

all_ok = all(checks.values())
for k, v in checks.items():
    print(('[OK] ' if v else '[FAIL] ') + k)
print()
print('All PASSED' if all_ok else 'Some FAILED')
