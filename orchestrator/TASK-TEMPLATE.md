# OBAOBA Task Template

## 標準任務格式

所有 Agent 輸出必須使用以下格式：

```markdown
---

## TASK_ID
[部門]-[YYYYMMDD]-[編號]

## OBJECTIVE
[一句話說明這個任務的目標]

## INPUT
- 網站: https://obaoba.online/
- 目標客群: [描述]
- 競爭者: [列表]
- 其他輸入: [描述]

## RESEARCH
[研究過程與發現]

## ACTION
[採取的行動]

## OUTPUT
[具體輸出內容]

## METRICS
- [指標 1]: [數值]
- [指標 2]: [數值]

## EVIDENCE
- [證據 1]: [來源]
- [證據 2]: [來源]

## STATUS
[DRAFT | IN_REVIEW | QA | APPROVED | PUBLISHED | ARCHIVED]

## NEXT_ACTION
[下一步行動與負責 Agent]

---
```

## 狀態說明

| 狀態 | 說明 |
|------|------|
| DRAFT | 草稿階段 |
| IN_REVIEW | 審核中 |
| QA | 品質檢查 |
| APPROVED | 已批准 |
| PUBLISHED | 已發布 |
| ARCHIVED | 已歸檔 |

## 範例

```markdown
---

## TASK_ID
SEO-20260923-001

## OBJECTIVE
找出 OBAOBA 新增 SEO 流量機會

## INPUT
- 網站: https://obaoba.online/
- 目標客群: 台北地區尋找傳播服務的男性客戶
- 競爭者: [競爭網站列表]

## RESEARCH
[研究內容...]

## ACTION
建立「大安區傳播推薦」文章

## OUTPUT
[文章內容...]

## METRICS
- 預估月搜尋量: 1,200
- 競爭度: 中
- 預估排名時間: 3 個月

## EVIDENCE
- Google Keyword Planner 數據
- SERP 分析結果

## STATUS
READY_FOR_QA

## NEXT_ACTION
Content Writer Agent 撰寫文章

---
```
