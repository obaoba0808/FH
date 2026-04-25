# 歐巴傳播 — Google Analytics 4 接入指南

> 文件更新：2026-04-25
> 目標：將 Google Analytics 4 接入歐巴傳播網站，追蹤流量、頁面瀏覽、轉換事件

---

## 選項一：Google Analytics 4（推薦，無需網站備案）

Google Analytics 4（GA4）是最新一代分析工具，無需網站備案即可使用。

### Step 1：建立 GA4 資源

1. 前往 [Google Analytics](https://analytics.google.com/) 並使用 Google 帳號登入
2. 點擊「開始測量」
3. 填入以下資料：
   - 帳戶名稱：`歐巴傳播分析`
   - 屬性名稱：`obaoba0808.github.io/FH`
   - 時區：台北
   - 貨幣：美元（TWD）
4. 完成後進入「資料串流」→「新增串流」→「網站」
5. 填入：
   - 網站網址：`https://obaoba0808.github.io/FH/`
   - 串流名稱：`歐巴傳播官網`

### Step 2：複製追蹤程式碼

在串流設定頁面，複製以 `G-` 或 `GTM-` 開頭的**測量 ID**（格式：`G-XXXXXXXXXX`）。

### Step 3：將追蹤碼加入網站

打開 `index.html`，找到 `</head>` 標籤，在其**上方**插入以下程式碼（**將 `G-XXXXXXXXXX` 替換為你的測量 ID**）：

```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### Step 4：對所有子頁面重複

將同樣的程式碼片段加入每個 HTML 頁面的 `</head>` 上方：
- `how_much.html`、`news.html`、`first_time_called.html` 等
- **所有 18 個 HTML 頁面都需要加入**
- 測量 ID（`G-XXXXXXXXXX`）全站統一

### Step 5：驗證

1. 在 GA4「即時」報告中查看是否有流量
2. 安裝 [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/) Chrome 擴充功能
3. 訪問網站，檢查 DevTools Console 是否有 `gtag` 呼叫

---

## 選項二：Google Search Console（補充，網站管理）

GA4 追蹤用戶行為，Search Console 追蹤搜尋曝光。

1. 前往 [Search Console](https://search.google.com/search-console)
2. 驗證 `https://obaoba0808.github.io/FH/` 的擁有權
3. 驗證完成後可查看：
   - 哪些關鍵詞帶來流量
   - 點擊率（CTR）數據
   - 索引狀態與錯誤

---

## 建議追蹤事件（增強電子商務）

在 `</body>` 上方加入以下程式碼，可追蹤按鈕點擊事件：

```html
<script>
// 追蹤所有 CTA 按鈕點擊
document.querySelectorAll('.cta-btn, .neon-btn, a[href*="LINE"]').forEach(function(el) {
  el.addEventListener('click', function() {
    gtag('event', 'cta_click', {
      'event_category': 'engagement',
      'event_label': el.textContent.trim()
    });
  });
});
</script>
```

---

## GA4 關鍵報表

| 報表 | 用途 |
|------|------|
| 即時 | 當前在線人數 |
| 參與度 → 網頁 | 最受歡迎的文章頁面 |
| 流量開發 → 來源/媒介 | 訪客從哪裡來（搜尋/直接/社交） |
| 轉換 → 事件 | CTA 按鈕點擊次數 |
| 參與度 → 參與度區段 | 用戶在網站停留時間 |

---

## ⚠️ 隱私權注意事項

網站已有 `safety_privacy.html` 頁面說明隱私政策。建議在網站底部加入隱私權連結：

```html
<a href="safety_privacy.html" class="text-gray-500 hover:text-gray-300 text-sm">隱私權政策</a>
```

---

*本文件由 SEO 煉金師 AI 生成。如需協助接入，請提供 GA4 測量 ID（以 `G-` 開頭），我可代為更新所有 HTML 頁面。*
