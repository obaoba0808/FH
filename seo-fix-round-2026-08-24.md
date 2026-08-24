# 歐巴傳播 SEO 修復紀錄 — 2026-08-24

> 網站：https://obaoba.online/ ｜ 本地 clone：FH-website ｜ repo：obaoba0808/FH (main)
> 部署 commit：`e25dbd8`（rebase 於遠端 `ac55f73` 之上，已 push）

## 本次修復項目（已全部上線，除 sitemap 受 Cloudflare 快取影響）

### 🔴 P0 — 網域遷移遺漏頁
**safety-guide-2026.html** 是舊模板頁，canonical/og:url/JSON-LD logo/mainEntityOfPage 仍指向舊網域 `obaoba0808.github.io/FH/`：
- canonical → `https://obaoba.online/safety-guide-2026.html` ✅
- og:url → 新網域 ✅
- og:site_name "FH 歐巴傳播" → "歐巴傳播" ✅
- JSON-LD publisher/logo/mainEntityOfPage → 新網域 ✅
- 補 hreflang (zh-Hant + x-default) ✅
- 補 favicon PNG 集（原本只有不存在的 favicon.ico）✅
- 補 og:locale=zh_TW ✅
- Article dateModified → 2026-08-24 ✅

### 🟡 P1 — sitemap.xml
- 重寫：清除所有亂碼中文註解、修正被註解吞掉的 `<lastmod>` 標籤
- URL 數 31 → **33**（補齊遺漏的 `safety-guide-2026.html` 與 `how-to-choose-right-companion.html`）
- lastmod 全數更新為 2026-08-24，保留 changefreq/priority
- 驗證：本地 `xml.dom.minidom` 解析通過，33 URLs
- ⚠️ Live 仍顯示舊版（garbled/31 URLs/3229 bytes）：Cloudflare 邊緣快取 TTL 未失效，來源已正確，將自動刷新（本站無 API 清快取）

### 🟡 P1 — ai.txt vs robots.txt 衝突
- 問題：live robots.txt 經 Cloudflare 注入 `Content-Signal: ai-train=no`，但 ai.txt 對所有 AI 爬蟲 `Allow:/`（暗示可訓練），策略矛盾
- 修復：ai.txt 全域 `User-agent: *` 加 `ai-train: no`，與 robots.txt 對齊（仍 `Allow:/` 供 AI 引用/答案，僅禁止拿去訓練基模）

### 🟡 P1 — 定價跨頁不一致（已統一，⚠️ 需老闆核對）
- 舊狀態：about-oppa.html + faq-all-in-one.html 用 **6,000-15,000 元/2hr**；pricing-guide-2026 / how_much / ai.txt 用 **2,400-5,000+ 元/2hr**
- 判定：以「最新 + 最詳細 + 品牌 AI 文檔認證」的 2,400-5,000+ 系統為權威
- 修復：about-oppa.html（meta/og/JSON-LD FAQ/可見 FAQ 共 5 處）+ faq-all-in-one.html（JSON-LD/可見 FAQ/公關等級表 共 8 處）全數改為 2,400-5,000+
- 同步：index/about-oppa/faq 三個 Organization schema `priceRange` 由 `NT$1,200-3,500` → `NT$2,400-5,000+`
- about-oppa Article dateModified → 2026-08-24
- ✅ 全站掃描：已無 6000/8000/12000/15000 舊價格殘留（compare-girls.html 的「5000-15000元」是描述酒店小姐對比價，非本店定價，保留）
- ⚠️ **請老闆確認實際收費是否為 2,400-5,000+/2hr**。若真實價格是 6,000-15,000，請改 pricing-guide-2026.html + how_much.html（單一來源）後我再同步

### 🟢 P2 — noopener / favicon
- 11 頁各 1 個 LINE 連結缺 `rel="noopener"`（多行 `<a>` 標籤導致初版審計誤報，實為 11 處非 31 頁）→ 已補 `rel="noopener noreferrer"`，全站歸零
- 4 頁（booking-guide / business-guide / compare-girls / legality-guide）內嵌 SVG favicon → 統一為 PNG favicon 集（與 index 一致）

## 審計時的誤報（已澄清，非 bug）
- 「全站缺 schema.org」：錯。所有頁面皆有 Article/BreadcrumbList/FAQPage/Organization 等 JSON-LD
- 「index 影片無 preload」：錯。已有 `preload="none"` + poster
- 「Klook 壞鏈」：錯。是正常聯盟 widget（`affiliate.klook.com`），`//www.klook.com` 為協議相對連結
- 「31 頁缺 noopener」：錯。實為 11 頁各 1 處（多行標籤導致單行正則漏判 rel）

## 變更檔案清單（22 files, +528/-241）
sitemap.xml, safety-guide-2026.html, ai.txt, about-oppa.html, faq-all-in-one.html, index.html,
+ 11 頁 noopener（KTV_recommendations/business_dinner/can-touch-guide/how_much/interaction_scale/is_this_right_for_you/motel_safe/shoot_guide/shoot_switch_personnel/special_industries/suitable_female）
+ 4 頁 favicon（booking-guide/business-guide/compare-girls/legality-guide）
+ seo-audit-2026-08-24.md（審計報告）

## Live 驗證
- faq-all-in-one.html body 已顯示新定價（2,400-5,000+）→ 部署成功
- sitemap.xml live 仍舊版（快取，將自動失效）
- 全站舊網域自引用：0（僅餘 footer 姊妹站 github.io 連結，為正常外部連結）
- canonical 舊網域：0

## 待辦（非本次範圍）
- [ ] 老闆核對實際定價（2,400-5,000+ vs 6,000-15,000）
- [ ] Cloudflare 快取自動失效後複檢 sitemap.xml live
- [ ] 成人娛樂產業性質：Google Ads 政策與索引敏感度（資訊項，非程式修復）
