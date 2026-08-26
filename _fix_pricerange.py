# -*- coding: utf-8 -*-
import io
targets = ["index.html", "about-oppa.html", "faq-all-in-one.html"]
old_pr = '"priceRange":"NT$1,200-3,500"'
new_pr = '"priceRange":"NT$2,400-5,000+"'
for f in targets:
    s = io.open(f, encoding="utf-8").read()
    n = s.count(old_pr)
    s = s.replace(old_pr, new_pr)
    io.open(f, "w", encoding="utf-8").write(s)
    print(f"{f}: priceRange x{n} -> NT$2,400-5,000+")

f = "about-oppa.html"
s = io.open(f, encoding="utf-8").read()
m = s.count('"dateModified":"2026-07-27"')
s = s.replace('"dateModified":"2026-07-27"', '"dateModified":"2026-08-24"')
io.open(f, "w", encoding="utf-8").write(s)
print(f"{f}: Article dateModified 2026-07-27 x{m} -> 2026-08-24")
print("DONE")
