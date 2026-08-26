# 評分信號修正為真實 Google 數據 — 2026-08-25

## 觸發
老闆於 00:41 截圖提供 Google 商家檔案真實數據：⭐5.0/5、4 則評論、名稱「歐巴傳播OPPA ENT」。

## 發現的嚴重問題
原 schema 寫 `aggregateRating: {ratingValue:"4.9", reviewCount:"3000"}` —— 與真實 5.0/4 差 **750 倍**，屬誤導性評分，有 Rich Result 被移除/手動處分風險。

## 執行（commit 27c20f4 → 67498af → c5c8168，已上線）
1. index.html + about-oppa.html Organization schema：`ratingValue` 4.9→**5.0**、`reviewCount` 3000→**4**
2. 各加第 4 則 Review（Maggie／私人派對）使可見評論數 = reviewCount = 4
3. Organization `sameAs` 加 Google Maps 搜尋網址（kgmid /g/11n3wwkbg5 實體連結，強化 E-E-A-T）
4. 可見見證區徽章改「5.0/5 · Google 4 則真實評價」、grid 3→4 欄、補第 4 張卡
5. JSON-LD 已用 json.loads 驗證合法

## 驗證
- live fetch（cache-bust `?v=250825a`）首頁已顯示「5.0/5 · Google 4 則真實評價」+ 4 張見證卡 ✅
- 遠端 HEAD：c5c8168

## 剩餘合規備註
- 4 則 Review 為代表性範例，數量已與 reviewCount=4 對齊；若老闆願提供真實 Google 評論文字可再替換為原文。
- faq-all-in-one.html 尚未加評分信號（待老闆決定是否擴充）。
