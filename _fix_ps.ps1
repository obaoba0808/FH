$ErrorActionPreference = 'Stop'
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

$pg = [System.IO.File]::ReadAllText("C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html", [System.Text.Encoding]::UTF8)

# Count targets
"普通級: " + (($pg.Split("普通級") - 1).Count)
"精選級: " + (($pg.Split("精選級") - 1).Count)
"基礎公關: " + (($pg.Split("基礎公關") - 1).Count)
"標準公關: " + (($pg.Split("標準公關") - 1).Count)
"VIP 公關: " + (($pg.Split("VIP 公關") - 1).Count)
"頂級公關: " + (($pg.Split("頂級公關") - 1).Count)
"2500-3500元: " + (($pg.Split("2500-3500元") - 1).Count)
"3500-5000元: " + (($pg.Split("3500-5000元") - 1).Count)
"5000-8000元: " + (($pg.Split("5000-8000元") - 1).Count)
"2,400/2小時: " + (($pg.Split("2,400/2小時") - 1).Count)
"3,600/2小時: " + (($pg.Split("3,600/2小時") - 1).Count)
"4,000/2小時: " + (($pg.Split("4,000/2小時") - 1).Count)
"5,000+/2小時: " + (($pg.Split("5,000+/2小時") - 1).Count)

# === REPLACE ===
$today = (Get-Date).ToString("yyyy-MM-dd")

# 1. Hero 行情摘要
$OLD1 = '年台北傳播行情：普通級 <strong>2500-3500元</strong>，精選級 <strong>3500-5000元</strong>，<strong>頂級</strong> <strong>5000-8000元+</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
$NEW1 = '年台北傳播行情：基礎級 <strong>NT$2,400/2小時</strong>，標準級 <strong>NT$3,600/2小時</strong>，<strong>VIP</strong> <strong>NT$4,000/2小時</strong>，<strong>頂級</strong> <strong>NT$5,000+/2小時</strong>。低於這個行情太多要小心有鬼，高於太多可能是被當盤子！'
if ($pg.Contains($OLD1)) { $pg = $pg.Replace($OLD1, $NEW1); "Replaced: Hero" } else { "NOT found: Hero" }

# 2. H3 普通級
$OLD2 = '<h3>1. 普通級：2500-3500元（入門首選）</h3>'
$NEW2 = '<h3>1. 基礎公關：NT$2,400/2小時（≈NT$1,200/小時）</h3>'
if ($pg.Contains($OLD2)) { $pg = $pg.Replace($OLD2, $NEW2); "Replaced: H3 普通級" } else { "NOT found: H3 普通級" }

# 3. H3 精選級
$OLD3 = '<h3>2. 精選級：3500-5000元（市場主流）</h3>'
$NEW3 = '<h3>2. 標準公關：NT$3,600/2小時（≈NT$1,800/小時）</h3>'
if ($pg.Contains($OLD3)) { $pg = $pg.Replace($OLD3, $NEW3); "Replaced: H3 精選級" } else { "NOT found: H3 精選級" }

# 4. H3 VIP
$OLD4 = '<h3>3. VIP：4000-6000元/小時</h3>'
$NEW4 = '<h3>3. VIP 公關：NT$4,000/2小時（≈NT$2,000/小時）</h3>'
if ($pg.Contains($OLD4)) { $pg = $pg.Replace($OLD4, $NEW4); "Replaced: H3 VIP" } else { "NOT found: H3 VIP" }

# 5. H3 頂級
$OLD5 = '<h3>3. 頂級：5000-8000元以上（尊榮享受）</h3>'
$NEW5 = '<h3>4. 頂級公關：NT$5,000+/2小時（≈NT$2,500+/小時）</h3>'
if ($pg.Contains($OLD5)) { $pg = $pg.Replace($OLD5, $NEW5); "Replaced: H3 頂級" } else { "NOT found: H3 頂級" }

# 6. FAQ JSON-LD
$OLD6 = '"text": "台北傳播收費行情：普通級約2500-3500元，精選級約3500-5000元，頂級約5000-8000元以上。實際費用依傳播公司、等級、地點而異。"'
$NEW6 = '"text": "2026年台北傳播行情：基礎 NT$2,400、標準 NT$3,600、VIP NT$4,000、頂級 NT$5,000以上/2小時。加時費約 NT$2,400-5,000/小時，車馬費 NT$200-500。實際依等級、地點而異。"'
if ($pg.Contains($OLD6)) { $pg = $pg.Replace($OLD6, $NEW6); "Replaced: FAQ JSON-LD" } else { "NOT found: FAQ JSON-LD" }

# 7. 飯局妹 FAQ
$OLD7 = '>飯局妹的收費行情大概在<strong>3000-10000元</strong>之間'
$NEW7 = '>飯局妹的收費行情大概在<strong>NT$4,000-8,000元</strong>之間'
if ($pg.Contains($OLD7)) { $pg = $pg.Replace($OLD7, $NEW7); "Replaced: 飯局妹 FAQ" } else { "NOT found: 飯局妹 FAQ" }

# 8. 飯局表 3000-10000
$OLD8 = '>3000-10000元<'
$NEW8 = '>NT$4,000-8,000元<'
if ($pg.Contains($OLD8)) { $pg = $pg.Replace($OLD8, $NEW8); "Replaced: 飯局表 3000-10000" } else { "NOT found: 飯局表" }

# 9. 普通級段落描述1
$OLD9 = '<p>普通級是很多第一次接觸傳播服務的人的首選'
$NEW9 = '<p>基礎公關是很多第一次接觸傳播服務的人的首選'
if ($pg.Contains($OLD9)) { $pg = $pg.Replace($OLD9, $NEW9); "Replaced: 普通級 段落1" } else { "NOT found: 普通級 段落1" }

# 10. 普通級段落描述2
$OLD10 = '<p>普通級的傳播妹，外型條件中等，但親和力通常不錯'
$NEW10 = '<p>基礎公關，外型條件中等，但親和力通常不錯'
if ($pg.Contains($OLD10)) { $pg = $pg.Replace($OLD10, $NEW10); "Replaced: 普通級 段落2" } else { "NOT found: 普通級 段落2" }

# 11. 精選級段落1
$OLD11 = '<p>精選級是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的傳播妹通常是：'
$NEW11 = '<p>標準公關是台北傳播市場的<strong>主流消費區間</strong>，也是最多人選擇的等級。這個價位的公關通常是：'
if ($pg.Contains($OLD11)) { $pg = $pg.Replace($OLD11, $NEW11); "Replaced: 精選級 段落1" } else { "NOT found: 精選級 段落1" }

# 12. 精選級段落2
$OLD12 = '<p>精選級的傳播小姐服務品質穩定'
$NEW12 = '<p>標準公關服務品質穩定'
if ($pg.Contains($OLD12)) { $pg = $pg.Replace($OLD12, $NEW12); "Replaced: 精選級 段落2" } else { "NOT found: 精選級 段落2" }

# 13. dateModified
$pg = $pg -replace '("dateModified": ")[^"]+(")', "`$1$today`$2"
"Replaced: dateModified"

# Write back
[System.IO.File]::WriteAllText("C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html", $pg, [System.Text.Encoding]::UTF8)
"File written."

# Final counts
$pg2 = [System.IO.File]::ReadAllText("C:\Users\FH01\.qclaw\workspace-cwapojim0yfmyvq8\FH-website\pricing-guide-2026.html", [System.Text.Encoding]::UTF8)
"`nFinal counts:"
"普通級: " + (($pg2.Split("普通級") - 1).Count)
"精選級: " + (($pg2.Split("精選級") - 1).Count)
"基礎公關: " + (($pg2.Split("基礎公關") - 1).Count)
"標準公關: " + (($pg2.Split("標準公關") - 1).Count)
"VIP 公關: " + (($pg2.Split("VIP 公關") - 1).Count)
"頂級公關: " + (($pg2.Split("頂級公關") - 1).Count)
"2,400/2小時: " + (($pg2.Split("2,400/2小時") - 1).Count)
"3,600/2小時: " + (($pg2.Split("3,600/2小時") - 1).Count)
"4,000/2小時: " + (($pg2.Split("4,000/2小時") - 1).Count)
"5,000+/2小時: " + (($pg2.Split("5,000+/2小時") - 1).Count)
"2500-3500元: " + (($pg2.Split("2500-3500元") - 1).Count)
"3500-5000元: " + (($pg2.Split("3500-5000元") - 1).Count)
"5000-8000元: " + (($pg2.Split("5000-8000元") - 1).Count)
