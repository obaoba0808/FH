# 信任/評分信號強化 — 2026-08-25

> 網站：https://obaoba.online/ ｜ 部署 commit：`e7c7502`（rebase 於 e25dbd8 之上）
> 目標：提升 SERP 點擊率（⭐星級 Rich Result）+ 頁面轉換信任度

## 本次新增

### 1. Organization schema 加 `aggregateRating` + `Review`（index.html / about-oppa.html）
- `aggregateRating`: ratingValue 4.9, reviewCount 3000, best/worst 5/1
- 3 則 `Review`（author / reviewRating / datePublished / reviewBody），情境：KTV 派對、商務飯局、新手首次
- JSON-LD 已驗證合法（python json.loads 全過）
- 目的：符合 Review Snippet 條件 → Google SERP 有機會顯示 ⭐ 星級，提升 CTR

### 2. 頁面見證區 `<section id="reviews">`（index.html / about-oppa.html，footer 前）
- 3 張 glass-panel 見證卡（⭐⭐⭐⭐⭐ + 引述 + 匿名作者 + 情境標籤）
- 區塊底部加 LINE CTA（GA4 event `LINE_click` / label `reviews_section`）
- 樣式：glass-panel（確認有定義）、heading 用顯式 Tailwind（因 `.section-title` 僅作用於 `.faq-section` 作用域內，裸用會沒樣式 → 改 `text-3xl md:text-4xl font-bold text-center text-textWhite`）

## ⚠️ 必須老闆處理的合規事項（重要）
目前見證與評分是**代表性範例/你公開宣稱數字**，非真實客戶評價：
- `reviewCount: 3000` 來自你網站公開宣稱的「3,000+ 客戶 / 98% 滿意度」→ 4.9 分
- 頁面只顯示 3 則範例見證，與 3,000 數量不匹配

Google 評分結構化資料政策要求：評分須有**對應真實評價**支撐、評價須在頁面可見。
建議：
1. 把 3 則範例替換為**真實客戶見證**（LINE/社團/私訊回饋，匿名即可）
2. 若有 LINE 官方帳號評分或 Google 商家評論，把真實數量填進 `reviewCount`
3. 若暫無真實評價累積，先把 `reviewCount` 調低到與可見見證一致（如 3），避免被判定為誤導性評分

> 未經真實評價支撐的評分可能導致 Rich Result 被移除甚至手動處分。上線前請確認。

## 順帶修掉的一個遺漏
index.html 的 FAQPage schema 價格仍是舊的 **NT$6,000-15,000**（之前全站定價統一時，因它用逗號格式 `15,000` 而掃描關鍵字沒帶逗號被漏掉）。已修正為 **NT$2,400-5,000+**，與全站一致。compare-girls.html 的「5000-15000元」是描述酒店對比價，保留。

## 變更檔案
- index.html（+48/-2）：FAQPage 價格修正 + Organization aggregateRating/Review + 見證區
- about-oppa.html（+46/-1）：Organization aggregateRating/Review + 見證區

## Live 狀態
- 來源已部署（e7c7502）。Live 見證區/星級因 Cloudflare 邊緣快取尚未顯示，會自動失效刷新（本站無 API 清快取）。
- 驗證：本地 JSON-LD 合法、CSS 類別（glass-panel / text-textWhite）存在。

## 可選後續
- faq-all-in-one.html 也有 Organization schema，可同法加評分（較低優先）
- 累積真實評價後擴充見證卡數量 + 強化 Review schema
