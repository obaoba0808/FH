"""為 4 頁補上 CTA 事件追蹤（GA4 + Meta Pixel 雙軌）"""
import re

files = ["safety-guide-2026.html", "taipei-banqiao.html",
         "taipei-daan.html", "taipei-xinyi.html"]

LINE_ATTR = ("onclick=\"gtag('event','LINE_click',{'event_category':'CTA'});"
             "if(typeof fbq!=='undefined')fbq('trackCustom','LINE_click');\"")
TEL_ATTR = ("onclick=\"gtag('event','phone_click',{'event_category':'CTA'});"
            "if(typeof fbq!=='undefined')fbq('trackCustom','phone_click');\"")

for fn in files:
    t = open(fn, encoding="utf-8").read()
    orig = t

    def add_attr(tag, attr):
        if "onclick" in tag:
            return tag
        return tag[:-1].rstrip() + " " + attr + ">"

    # LINE
    matches = [m.group(0) for m in
               re.finditer(r'<a\b[^>]*href="https://line\.me/R/ti/p/@938nzmjr"[^>]*>', t)]
    n_line = 0
    for tag in matches:
        new_tag = add_attr(tag, LINE_ATTR)
        if new_tag != tag:
            t = t.replace(tag, new_tag, 1)
            n_line += 1

    # TEL
    matches = [m.group(0) for m in re.finditer(r'<a\b[^>]*href="tel:[^"]*"[^>]*>', t)]
    n_tel = 0
    for tag in matches:
        new_tag = add_attr(tag, TEL_ATTR)
        if new_tag != tag:
            t = t.replace(tag, new_tag, 1)
            n_tel += 1

    if t != orig:
        with open(fn, "w", encoding="utf-8", newline="") as f:
            f.write(t)
        print(f"OK    {fn:<28} LINE補={n_line}  tel補={n_tel}")
    else:
        print(f"SKIP  {fn:<28} 無變更")
