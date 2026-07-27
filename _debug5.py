import subprocess

# Read raw git content
result = subprocess.run(
    ['git', 'cat-file', '-p', 'HEAD:index.html'],
    capture_output=True, cwd='.',
    text=False  # raw bytes
)
git_content = result.stdout
print('Git content length:', len(git_content))

# Search for Organization
idx = git_content.find(b'Organization')
print('Organization index:', idx)
if idx >= 0:
    print('Found at:', idx)
    start = max(0, idx - 50)
    print('Context:', git_content[start:idx+100])
else:
    print('NOT FOUND in git content')
    # Check what the raw bytes look like around the JSON-LD area
    print('Last 200 bytes:', git_content[-200:])

# Also check the working directory file
from pathlib import Path
wd_content = Path('index.html').read_bytes()
idx2 = wd_content.find(b'Organization')
print('\nWorking dir Organization index:', idx2)
if idx2 >= 0:
    start = max(0, idx2 - 50)
    print('Context:', wd_content[start:idx2+100])
