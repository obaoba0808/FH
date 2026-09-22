# OBAOBA.online 自動化部署說明

## 部署流程

本專案使用 GitHub Actions 自動部署至 https://obaoba.online/

### 觸發條件

- **自動**: 推送 `main` 分支且變更 `website/` 目錄內檔案
- **手動**: 在 GitHub Actions 頁面點擊 "Run workflow"

### 部署目標

- **Repo**: `obaoba0808/FH`
- **網址**: https://obaoba.online/
- **CDN**: GitHub Pages (全球 CDN)

### 所需 Secrets

請在 GitHub repo 設定以下 Secrets：

| Secret | 說明 | 取得方式 |
|--------|------|----------|
| `FH_DEPLOY_TOKEN` | GitHub Personal Access Token | Settings → Developer settings → Personal access tokens |

### 設定步驟

1. 前往 https://github.com/obaoba0808/obaoba.online/settings/secrets/actions
2. 點擊 "New repository secret"
3. Name: `FH_DEPLOY_TOKEN`
4. Secret: 貼上 GitHub Personal Access Token
5. 點擊 "Add secret"

### 手動部署

```bash
# 本地推送觸發部署
git add .
git commit -m "更新網站內容"
git push origin main
```

### 檢查部署狀態

- GitHub Actions: https://github.com/obaoba0808/obaoba.online/actions
- 網站狀態: https://obaoba.online/
- Pages 構建: https://github.com/obaoba0808/FH/deployments

### 回滾

如需回滾至上一版本：

```bash
git revert HEAD
git push origin main
```

## 自動化排程

| 排程 | 時間 | 任務 |
|------|------|------|
| Daily SEO Check | 每日 08:00 (UTC+8) | 技術健康檢查 |
| Weekly Report | 每週一 09:00 (UTC+8) | 優化進度報告 |
