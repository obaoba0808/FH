"""對全站尚未安裝 Meta Pixel 的頁面，補上完整 Pixel 程式碼
插入點：</head> 之前
"""
import glob, os, re

PIXEL_ID = "1377320045457011"

PIXEL_BLOCK = """    <!-- Meta Pixel Code -->
    <script>
    !function(f,b,e,v,n,t,s)
    {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
    n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;
    t.src=v;s=b.getElementsByTagName(e)[0];
    s.parentNode.insertBefore(t,s)}(window, document,'script',
    'https://connect.facebook.net/en_US/fbevents.js');
    fbq('init', '%s');
    fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
    src="https://www.facebook.com/tr?id=%s&ev=PageView&noscript=1"
    /></noscript>
    <!-- End Meta Pixel Code -->
""" % (PIXEL_ID, PIXEL_ID)

files = sorted(glob.glob("*.html"))
installed, skipped, errors = [], [], []

for fn in files:
    txt = open(fn, encoding="utf-8").read()
    if "fbevents.js" in txt or "fbq('init'" in txt:
        skipped.append(fn)
        continue
    if "</head>" not in txt:
        errors.append((fn, "無 </head>"))
        continue
    new = txt.replace("</head>", PIXEL_BLOCK + "</head>", 1)
    if new.count("fbq('init', '%s')" % PIXEL_ID) != 1:
        errors.append((fn, "init 次數異常"))
        continue
    with open(fn, "w", encoding="utf-8", newline="") as f:
        f.write(new)
    installed.append(fn)

print(f"新安裝: {len(installed)} 頁")
for f in installed:
    print("  +", f)
print(f"\n已存在略過: {len(skipped)} 頁")
for f in skipped:
    print("  =", f)
if errors:
    print(f"\n錯誤: {len(errors)}")
    for f, e in errors:
        print(f"  ! {f}: {e}")
