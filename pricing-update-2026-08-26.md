# 全站價格更新 - 2026-08-26

## 任務概述
用戶要求更正全網站收費標準，基礎級價格由 NT$2,400 調整為 NT$3,000。

## 新價格對照表

| 等級 | 2小時價格 | 加時/小時 |
|------|----------|----------|
| 基礎級 | NT$3,000 | NT$1,500 |
| 標準級 | NT$3,600 | NT$1,800 |
| VIP 級 | NT$4,000 | NT$2,000 |
| 頂級 | NT$5,000+ | NT$2,500+ |

## 更新範圍

### 主要頁面（8 個）
- 2026-pricing-table.html
- index.html
- about-oppa.html
- faq-all-in-one.html
- how_much.html
- pricing-guide-2026.html
- beginners-checklist.html
- private-party-guide.html

### 更新類型
1. **Meta 標籤**：description、og:description
2. **JSON-LD Schema**：Article description、FAQPage、priceRange
3. **可見文案**：價格卡片、表格、引導段落、FAQ answers
4. **JavaScript 計算機**：基礎價 2400→3000，加時費率 3000→1500
5. **每小時價格**：motel_safe.html（NT$1,200→NT$1,500）

### 排除項目
- 總預算範圍（如 NT$13,000-22,400）—— 這是加總結果，非單價
- VIP 每小時價格區間（NT$2,000-2,400 → NT$2,000）—— 改為固定價

## 驗證結果
- ✅ 全站無基礎級 2,400 殘留
- ✅ 新價格 3,000 已出現在 meta/schema/可見文案
- ✅ JavaScript 計算機邏輯正確

## Git Commit
- Commit: `b4c8f95`
- Message: "fix: 全站價格更新 - 基礎級 NT$2,400 → NT$3,000（2026-08-26 正式生效）"
- Push: 成功至 origin/main

## 後續事項
- [ ] 等待 Cloudflare 快取失效（HTML 600 秒、圖片/CSS 視版本參數）
- [ ] 用戶確認無痕視窗看到正確價格
- [ ] GSC 重新提交 sitemap（若索引頁面含舊價格）

---

**更新時間**：2026-08-26 18:03 GMT+8
**執行者**：QClaw SEO 專員
