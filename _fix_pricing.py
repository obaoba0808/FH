# -*- coding: utf-8 -*-
import io

def load(f): return io.open(f, encoding="utf-8").read()
def save(f, s): io.open(f, "w", encoding="utf-8").write(s)

# ---- about-oppa.html ----
f = "about-oppa.html"
s = load(f)
reps = [
    ("鐘點費 6000-15000 元/2小時", "鐘點費 2,400-5,000+ 元/2小時"),
    ("約落在 6000-15000 元／2 小時。基礎級 6000-8000、標準級 8000-12000、VIP 級 12000-15000、頂級 15000 以上",
     "約落在 2,400-5,000+ 元／2 小時。基礎級 2,400、標準級 3,600、VIP 級 4,000、頂級 5,000 以上"),
]
for a, b in reps:
    c = s.count(a)
    s = s.replace(a, b)
    print(f"[about-oppa] '{a[:30]}...' x{c} -> replaced")
save(f, s)

# ---- faq-all-in-one.html ----
f = "faq-all-in-one.html"
s = load(f)
reps = [
    ("從基礎公關到VIP等級大約落在 6000-15000 元/2小時", "從基礎公關到VIP等級大約落在 2,400-5,000+ 元/2小時"),
    ("大約落在 6000-15000 元/2小時 的範圍", "大約落在 2,400-5,000+ 元/2小時 的範圍"),
    ("最低消費大約在 6000 元/2小時（基礎公關）", "最低消費大約在 2,400 元/2小時（基礎公關）"),
    ("新手第一次通常預算 6000-10000 元就能有很不錯的體驗", "新手第一次通常預算 2,400-3,600 元就能有很不錯的體驗"),
    ("6000-8000/2hr", "2,400/2hr"),
    ("8000-12000/2hr", "3,600/2hr"),
    ("12000-15000/2hr", "4,000/2hr"),
    ("15000+/2hr", "5,000+/2hr"),
]
for a, b in reps:
    c = s.count(a)
    s = s.replace(a, b)
    print(f"[faq] '{a}' x{c} -> replaced")
save(f, s)
print("DONE")
