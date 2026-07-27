from pathlib import Path

html = Path('index.html').read_text('utf-8')

# Simple searches
print('Index of "@type":"Organization":', html.find('"@type":"Organization"'))
print('Index of @type Organization:', html.find('@type":"Organization"'))
print('Index of Organization:', html.find('Organization'))

# Check what the actual raw text looks like around position 254
print('\nChars around position 254:')
for i in range(248, 270):
    c = html[i]
    print(f'  [{i}] U+{ord(c):04X} = {repr(c)}')

# Check if the file has any BOM or unusual encoding
print('\nFirst 10 chars:')
for i in range(min(10, len(html))):
    c = html[i]
    print(f'  [{i}] U+{ord(c):04X} = {repr(c)}')
