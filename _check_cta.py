html=open('index.html',encoding='utf-8').read()
checks=[
    ('Green badge','border-[#06C755]/30' in html and '24小時預約中' in html),
    ('Primary LINE large','hero_primary' in html),
    ('Trust badges','平均30分鐘到府' in html),
    ('Sticky bar','translate-y-full' in html),
    ('Sticky JS','IntersectionObserver' in html),
    ('Sticky bar gtag','sticky_bar' in html),
]
for n,ok in checks:
    print(f'  [{"OK" if ok else "FAIL"}] {n}')
