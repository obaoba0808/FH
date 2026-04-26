# Google Search Console 接入教學

歐巴傳播網站適用的 GSC 接入步驟，幫助追蹤搜尋流量與外鏈成效。

---

## 步驟 1：建立 GSC 資源

1. 前往 [Google Search Console](https://search.google.com/search-console)
2. 點擊「新增資源」
3. 輸入網址：`https://obaoba0808.github.io/FH/`
4. 選擇驗證方式（推薦 HTML 檔案驗證）

## 步驟 2：驗證網站所有權

### 方法 A：HTML 檔案驗證（推薦）

下載驗證 HTML 檔案，放置到 `FH-website/` 目錄後 commit 推送：

```html
<!-- 檔案名：google1234567890abc.html -->
google-site-verification: google1234567890abc.html
```

GitHub Pages 部署後，點擊 GSC 中的「驗證」即可。

### 方法 B：DNS 驗證

若無法上傳 HTML 檔案，可在 DNS 設定中加入 TXT 紀錄：
- 主機：`@` 或 `obaoba0808.github.io`
- 類型：`TXT`
- 值：`google-site-verification=google1234567890abc`

## 步驟 3：提交 sitemap

1. GSC 右側選單 →「sitemap」
2. 輸入：`sitemap.xml`
3. 點擊「提交」

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

## 步驟 5：優化搜尋呈現 (SEO)

### 提升 CTR 技巧
- 確認每個頁面有獨特的 `<title>` 與 `<meta description>`
- 使用結構化資料 (Schema.org) 讓搜尋引擎顯示更多資訊
- 歐巴傳播網站已加入 Article + FAQPage Schema

### 監控關鍵詞
- GSC 「搜尋成效」報告可看到使用者用哪些詞找到你
- 重点关注長尾關鍵詞：
  - 「叫傳播安全嗎」
  - 「傳播小姐打工」
  - 「台北傳播多少錢」

---

## 常見問題

### Q：GSC 需要多久才會有數據？
A：通常 24-48 小時後才會開始顯示搜尋數據。新網站可能需要一週。

### Q：成人內容網站可以使用 GSC 嗎？
A：Google 對成人內容有特殊政策。若網站包含成人內容，需確保：
- 不包含未成年內容
- 不包含非法內容
- 符合 Google 色情政策

### Q：為什麼某些頁面沒有被索引？
A：檢查以下項目：
1. robots.txt 是否允許爬蟲
2. 頁面是否有 canonical 指向正確網址
3. 頁面是否有 `<meta name="robots" content="noindex">`

---

## 後續行動

1. **設定 GSC**（需要 GitHub 帳號登入）
2. **每週查看數據**：追蹤關鍵詞排名變化
3. **分析外鏈**：哪些論壇/網站正在引用歐巴傳播
4. **優化內容**：根據 GSC 數據調整頁面標題與描述