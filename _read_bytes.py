# -*- coding: utf-8 -*-
# _read_bytes.py — Extract exact bytes around pricing section for analysis
PATH = r'C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html'

with open(PATH, 'rb') as f:
    raw = f.read()

# Search for '2500-3500' bytes
idx = raw.find(b'2500-3500')
print(f'2500-3500 at byte {idx}')

# Extract 800 bytes before to capture the full <p class="mb-0"> tag
chunk = raw[max(0,idx-800):idx+300]

# Write to file
with open('_pricing_chunk.bin', 'wb') as f:
    f.write(chunk)

print(f'Wrote {len(chunk)} bytes to _pricing_chunk.bin')
print(f'Starts at byte {max(0,idx-800)}, ends at byte {idx+300}')
