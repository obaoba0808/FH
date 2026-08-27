# Dropdown 垃圾文字修復 - 2026-08-26 18:35

## 問題描述
用戶回報下拉選單出現亂碼 `flex flex-col">`。

## 根因
先前修復腳本 (`_fix_dropdown_html.py`) 僅處理 `<div class="p-2"` 缺閉合引號問題，未發現另一個問題：
- 錯誤模式：`</a> flex flex-col">`
- 位置：在每個 dropdown 第一個 anchor (`</a>`) 之後
- 影響：30 個頁面

## 修復
- 腳本：`_fix_dropdown_garbage.py`（正則替換 `</a>\s+flex flex-col">` → `</a>`）
- 修復頁數：30/37 頁（7 頁無 dropdown 或已正確）
- Commit：`48943c7`（2026-08-26 18:35）
- Push：✅ 成功

## 驗證
- Live URL: https://obaoba.online/index.html
- 強制刷新（Cache-Control: no-cache）後確認：✅ 已無 `</a> flex flex-col">` 模式
- Content Length: 71,004 bytes（與舊版 71,020 bytes 差 16 bytes = 移除 16 chars × 1 occurrence）

## 後續
- 用戶瀏覽器可能仍有快取 → 建議強制刷新（Ctrl/Cmd+Shift+R）
- Cloudflare 邊緣快取預設 8 天 TTL → 部分節點可能仍吐舊版
