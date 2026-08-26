# -*- coding: utf-8 -*-
import io, re
s = io.open("dist/output.css", encoding="utf-8").read()
print("glass-panel defined:", (".glass-panel{" in s))
m = re.search(r"\.glass-panel\{[^}]*\}", s)
print("glass-panel rule:", (m.group(0)[:140] if m else "NOT FOUND"))
m2 = re.search(r"\.text-glow\{[^}]*\}", s)
print("text-glow rule:", (m2.group(0)[:140] if m2 else "NOT FOUND"))
m3 = re.search(r"\.text-textWhite\{[^}]*\}", s)
print("text-textWhite rule:", (m3.group(0)[:140] if m3 else "NOT FOUND"))
