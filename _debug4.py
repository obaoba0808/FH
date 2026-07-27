from pathlib import Path

html = Path('index.html').read_text('utf-8')
print('File length:', len(html))

# Test raw bytes
s1 = '"@type":"Organization"'
s2 = '@type":"Organization"'
s3 = 'Organization'
print('s1 in html:', s1 in html)
print('s2 in html:', s2 in html)
print('s3 in html:', s3 in html)

# Try bytes
b1 = s1.encode('utf-8')
print('s1 bytes:', b1)
print('html.encode utf-8:', html.encode('utf-8')[:500])
