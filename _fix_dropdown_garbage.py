# -*- coding: utf-8 -*-
"""
Fix dropdown HTML garbage: '</a> flex flex-col">' -> '</a>'
"""
import re
import sys
from pathlib import Path
from io import TextIOWrapper

# Force UTF-8 stdout
sys.stdout = TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

repo = Path(r"C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website")
html_files = list(repo.glob("*.html"))

print(f"Found {len(html_files)} HTML files")

# Pattern: </a> followed by space + flex flex-col">
pattern = r'</a>\s+flex flex-col">'
replacement = '</a>'

fixed_count = 0
for f in html_files:
    content = f.read_text(encoding='utf-8')
    new_content = re.sub(pattern, replacement, content)
    if new_content != content:
        f.write_text(new_content, encoding='utf-8')
        matches = len(re.findall(pattern, content))
        print(f"  ✓ {f.name}: {matches} fixes")
        fixed_count += matches

print(f"\n✅ Total fixed: {fixed_count} occurrences")
