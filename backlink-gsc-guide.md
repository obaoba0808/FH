# Google Search Console 接入教學

歐巴傳播網站適用的 GSC 接入步驟，幫助追蹤搜尋流量與外鏈成效。

---

## ⚠️ 重要前提：子目錄部署

歐巴網站部署在 GitHub Pages 的 `/FH/` 子目錄：
- **網站根目錄**：`https://obaoba0808.github.io/FH/`
- **驗證檔放置位置**：`FH-website/googleXXXXX.html`（放在網站根目錄，會自動部署到 `/FH/` 路徑）

---

## 步驟 1：建立 GSC 資源

1. 前往 [Google Search Console](https://search.google.com/search-console)
2. 點擊「新增資源」
3. 輸入網址（**注意結尾斜線**）：`https://obaoba0808.github.io/FH/`
4. 選擇驗證方式（推薦 HTML 檔案驗證）

## 步驟 2：驗證網站所有權

### 方法 A：HTML 檔案驗證（推薦）

**流程：**

1. 在 GSC 新增資源時，選擇「HTML 檔案驗證」
2. Google 會提供一個 HTML 檔案，檔名例如：`google1234567890abc.html`
3. **把這個檔案放進 `FH-website/` 根目錄**（不是 `/FH/` 子目錄，GitHub Actions 會自動部署）
4. Commit 並推送至 GitHub
5. 等待 GitHub Pages 部署完成（約 2-3 分鐘）
6. 確認檔案可存取：`https://obaoba0808.github.io/FH/google1234567890abc.html`
7. 回 GSC 點擊「驗證」

**驗證連結格式（重要）：**
```
https://obaoba0808.github.io/FH/google1234567890abc.html
```
↑ 是 `/FH/` 路徑，不是根目錄

### 方法 B：DNS 驗證

若無法上傳 HTML 檔案，可在 DNS 設定中加入 TXT 紀錄：
- 主機：`@` 或 `obaoba0808.github.io`
- 類型：`TXT`
- 值：`google-site-verification=google1234567890abc`

### 方法 C：Google Analytics 驗證（最快）

如果 GA4 追蹤碼已正確安裝（測量 ID：`G-S7KQGHSD2R`），GSC 可直接用 GA4 驗證：
1. GSC → 新增資源 → 選擇「網域」類型
2. 輸入 `obaoba0808.github.io`（不帶 `/FH/`）
3. 選擇「Google Analytics」驗證方式
4. 因為 GA4 已全站部署，驗證通常幾分鐘內通過

## 步驟 3：提交 sitemap

GSC 驗證通過後：
1. GSC 右側選單 →「sitemap」
2. 輸入：`FH/sitemap.xml`（**含 FH/ 前綴**）
3. 點擊「提交」

> 注意：因為網站根目錄是 GitHub Pages 的 `obaoba0808.github.io`，而網站在 `/FH/` 子目錄，sitemap 路徑需含 `FH/` 前綴才正確。

## 步驟 4：追蹤重點數據

### 流量監控
- **點擊次數**：自然搜尋帶來的點擊
- **曝光次數**：網站在搜尋結果中被看見的次數
- **平均排名**：關鍵詞平均排名位置
- **點擊率 (CTR)**：曝光轉點擊的比例

### 外鏈監控
- 左側選單 →「連結」→「外部連結」
- 查看哪些網站正在連結到歐巴傳播
- 可看到錨文字 (anchor text) 分布

### 索引狀態
- 確認 Google 已索引哪些頁面
- 若發現未索引的頁面，檢查 robots.txt 或頁面 meta

## 步驟 5：關鍵詞監控重點

歐巴適用的重點追蹤關鍵詞（可直接在 GSC「搜尋成效」中新增這些詞）：

| 關鍵詞 | 類型 | 優先度 |
|--------|------|--------|
| 叫傳播安全嗎 | 長尾疑問詞 | ⭐⭐⭐ |
| 傳播小姐打工 | 求職者詞 | ⭐⭐⭐ |
| 台北傳播多少錢 | 價格詞 | ⭐⭐ |
| 汽車旅館叫傳播 | 場合詞 | ⭐⭐ |
| 飯局妹 | 場合詞 | ⭐⭐ |
| 傳播公司推薦 | 品牌詞 | ⭐⭐ |
| 歐巴傳播 | 品牌詞 | ⭐ |

## 步驟 6：如何根據 GSC 數據調整

### 發現高曝光、低點擊的頁面
→ 優化 meta description，加入更吸引人的描述

### 發現有排名但排名下滑
→ 更新內容、增加內鏈、爭取更多外鏈

### 發現新關鍵詞被看見
→ 在內容中自然融入該關鍵詞，強化該主題

---

## 常見問題

### Q：GSC 需要多久才會有數據？
A：通常 24-48 小時後才會開始顯示搜尋數據。新網站可能需要一週。

### Q：驗證檔已上傳但 GSC 顯示驗證失敗？
A：確認：
1. 檔案 URL 是否正確：`https://obaoba0808.github.io/FH/googleXXXXX.html`
2. GitHub Pages 是否已完成部署（檢查 Actions 頁面）
3. 等待 2-3 分鐘後再試

### Q：成人內容網站可以使用 GSC 嗎？
A：Google 對成人內容有特殊政策。若網站包含成人內容，需確保：
- 不包含未成年內容
- 不包含非法內容
- 符合 Google 色情政策
- 歐巴網站內容屬於成人娛樂，建議以「夜生活娛樂」關鍵詞為主

### Q：為什麼某些頁面沒有被索引？
A：檢查以下項目：
1. `robots.txt` 是否允許爬蟲（歐巴網站已正確設定）
2. 頁面是否有 canonical 指向正確網址（歐巴網站已設定）
3. 頁面是否有 `<meta name="robots" content="noindex">`（沒有的話忽略）

### Q：sitemap 提交 404？
A：路徑應為 `FH/sitemap.xml`，不是 `sitemap.xml`。歐巴網站的 sitemap 在 `/FH/sitemap.xml`。

---

## 後續行動

1. **今天**：設定 GSC（用 GA4 驗證最簡單）
2. **這週**：提交 sitemap（路徑 `FH/sitemap.xml`）
3. **每週**：查看搜尋成效，追蹤長尾關鍵詞排名
4. **每月**：分析外鏈變化，調整外鏈建設策略
5. **持續**：根據 GSC 數據優化頁面 meta 與內容

---

## 快速對照表

| 項目 | 值 |
|------|-----|
| GSC 資源 URL | `https://obaoba0808.github.io/FH/` |
| sitemap 路徑 | `FH/sitemap.xml` |
| GA4 測量 ID | `G-S7KQGHSD2R` |
| 驗證檔放置位置 | `FH-website/googleXXXXX.html` |
| 驗證檔最終 URL | `https://obaoba0808.github.io/FH/googleXXXXX.html` |
