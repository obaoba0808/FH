# -*- coding: utf-8 -*-
import io
def load(f): return io.open(f, encoding="utf-8").read()
def save(f, s): io.open(f, "w", encoding="utf-8").write(s)

f = "about-oppa.html"
s = load(f)
reps = [
    ('<strong class="text-neonPink">6000-15000 元／2 小時</strong>：基礎級 6000-8000、標準級 8000-12000、VIP 級 12000-15000、頂級 15000 以上',
     '<strong class="text-neonPink">2,400-5,000+ 元／2 小時</strong>：基礎級 2,400、標準級 3,600、VIP 級 4,000、頂級 5,000 以上'),
    ('<strong>6000-15000 元／2 小時</strong>。基礎級 6000-8000、標準級 8000-12000、VIP 級 12000-15000、頂級 15000 以上',
     '<strong>2,400-5,000+ 元／2 小時</strong>。基礎級 2,400、標準級 3,600、VIP 級 4,000、頂級 5,000 以上'),
]
for a, b in reps:
    print(f"[about-oppa] x{s.count(a)}")
    s = s.replace(a, b)
save(f, s)

f = "faq-all-in-one.html"
s = load(f)
reps = [
    ('<strong>6000-15000 元/2小時</strong>', '<strong>2,400-5,000+ 元/2小時</strong>'),
    ('<strong>6000 元/2小時</strong>（基礎公關）', '<strong>2,400 元/2小時</strong>（基礎公關）'),
]
for a, b in reps:
    print(f"[faq] x{s.count(a)}")
    s = s.replace(a, b)
save(f, s)
print("DONE")
