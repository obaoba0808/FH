# _fix_v5.py — Read file as bytes, print hex of known strings for debugging
PATH = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'

with open(PATH, 'rb') as f:
    raw = f.read()

# Find the exact byte range for the pricing content section
# Known content (confirmed by Python's repr):
# '26年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-'
# Let's find "2500-3500" bytes in raw

# ASCII bytes
idx = raw.find(b'2500-3500')
print(f'2500-3500 at byte pos: {idx}')
if idx >= 0:
    print(f'Context (40 bytes before to 100 after): {repr(raw[max(0,idx-40):idx+100])}')
    # Print hex
    segment = raw[max(0,idx-40):idx+100]
    print('HEX:', segment.hex(' '))

# Also search for '普通級' UTF-8 bytes
pt_utf8 = '普通級'.encode('utf-8')
idx2 = raw.find(pt_utf8)
print(f'\n普通級 UTF-8 bytes at: {idx2}')
if idx2 >= 0:
    print(f'Context: {repr(raw[idx2-20:idx2+60])}')
    segment2 = raw[idx2-20:idx2+60]
    print('HEX:', segment2.hex(' '))

# Write the segment before '2500-3500' to a separate file
if idx >= 0:
    # find the <p class="mb-0"> before this
    chunk = raw[max(0,idx-500):idx+200]
    with open('_debug_chunk.bin', 'wb') as f:
        f.write(chunk)
    print(f'\nWrote 700-byte debug chunk to _debug_chunk.bin')
    print(f'Chunk length: {len(chunk)}')
