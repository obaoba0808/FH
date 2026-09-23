"""把既有 gtag-only 的 CTA onclick 升級為 GA4 + Meta Pixel 雙軌"""
import glob, re

PAT = re.compile(r"""onclick="(gtag\('event',\s*'([A-Za-z_]+)'[^"]*?\))""")


def suffix(ev):
    return "if(typeof fbq!=='undefined'){fbq('trackCustom','%s');}" % ev


total = 0
changed = []

for fn in sorted(glob.glob("*.html")):
    t = open(fn, encoding="utf-8").read()
    cnt = [0]

    def repl(m):
        full, ev = m.group(1), m.group(2)
        if "fbq" in full:
            return m.group(0)
        cnt[0] += 1
        return 'onclick="%s;%s"' % (full, suffix(ev))

    new = PAT.sub(repl, t)
    if new != t:
        with open(fn, "w", encoding="utf-8", newline="") as f:
            f.write(new)
        changed.append((fn, cnt[0]))
        total += cnt[0]

print(f"更新 {len(changed)} 檔，共 {total} 個 onclick 升級為雙軌")
for fn, c in changed:
    print(f"  {fn:<34} {c}")
