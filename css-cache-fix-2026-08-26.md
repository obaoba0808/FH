# CSS 快取截斷修復記錄（2026-08-26）

## 問題現象
用戶回報 `https://obaoba.online/2026-pricing-table.html` 「連結無法點、像一張紙」（樣式完全失效）。

## 根因（兩層 Cloudflare 快取問題）
1. **CSS 被 CF 快取截斷**：`dist/output.css?v=250825a` 在部署空窗期被 CF 回應並快取成 6989 bytes 的「截斷版」（實際檔案 30KB）。全站 33+ 頁引用此 CSS → 全部樣式失效。
2. **404 快取**：更名/改版本後，新 URL 在 GitHub Pages 尚未部署完成時被 CF 首次請求，CF 快取了 404（cf-cache-status: HIT 的 404）。

## 關鍵診斷學習
- `Content-Length: 6989` 不必然是截斷！Cloudflare 對 text/css 預設 gzip 壓縮，30KB CSS 壓縮後約 6989 bytes。
- **判斷真偽的方法**：用 PowerShell `Invoke-WebRequest`（自動解壓）抓 body 看實際長度；或用 `curl -sI` 看有無 `Content-Encoding: gzip`。
- `cf-cache-status: MISS` = 向 origin 現抓；`HIT` = 用邊緣快取（含 404 快取）。

## 修復動作
1. 全站 CSS 版本 `?v=250825a` → `?v=250826a`（commit `cccd3d9`）—— 繞過截斷 CSS。
2. CSS 檔案更名 `dist/output.css` → `dist/main.css`，全站 HTML 同步（commit `4f0b899`）。
3. 發現 `?v=1` 被 CF 快取成 404 → 升級 `?v=1` → `?v=2`（commit `7338506`）。
4. 最終 `dist/main.css?v=2` 驗證：解壓 30,496 bytes、`.glass-panel`/`.btn-neon` 全在、200 OK。

## 已確認正常
- 全站 35 個 HTML 引用 `dist/main.css?v=2`，0 處舊 `output.css`。
- 乾淨 URL `dist/main.css` 與 `?v=2` 皆 200 完整。

## 用戶端動作（必要）
硬刷新 `Ctrl+Shift+R` / `Cmd+Shift+R` 清除瀏覽器對舊 HTML+截斷 CSS 的快取。Server 端已 100% 正常。

## SOP（未來每次改 CSS/JS 必做）
- 改 `dist/main.css` 後，全站 HTML 的引用版本參數遞增（`?v=2` → `?v=3` ...），逼 CF 重新抓檔。
- 腳本範本：`_bust_css.py`（正則替換 `dist/main.css\?v=N` → `?v=N+1`）。
- 注意 PowerShell inline Python 引號被吃 → 一律用腳本檔；f-string 內不可含反斜線。
- git push 需 `git -c http.version=HTTP/1.1 push origin main`（SSL workaround）。

## 環境限制（再次確認）
- **無 Cloudflare 後台權限**：無 CF API token、wrangler 未登入、無 .cloudflared 目錄。無法手動 Purge Cache 或修改 Cache-Control 規則。
- 只能靠「換 URL / 加版本參數」讓 CF 重新向 origin 抓檔。
