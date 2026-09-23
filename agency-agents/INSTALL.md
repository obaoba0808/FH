# Agency Agents 安裝指南

## 核心 Agents（OBAOBA 專用）

從 agency-agents 人才庫中，已篩選出 OBAOBA 所需的 30 個核心 Agents：

### HQ 層
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-CEO | strategy/nexus-strategy.md |

### Strategy Team
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-STRATEGIST | strategy/EXECUTIVE-BRIEF.md |
| OBAOBA-TREND-RESEARCHER | research/feedback-synthesizer.md |

### SEO Team
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-SEO-STRATEGIST | marketing/marketing-seo-specialist.md |
| OBAOBA-KEYWORD-RESEARCHER | marketing/marketing-agentic-search-optimizer.md |
| OBAOBA-SEO-AUDITOR | testing/testing-accessibility-auditor.md |
| OBAOBA-CONTENT-PLANNER | marketing/marketing-content-creator.md |

### Content Factory
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-CONTENT-STRATEGIST | marketing/marketing-content-creator.md |
| OBAOBA-CONTENT-WRITER | engineering/engineering-technical-writer.md |
| OBAOBA-CONTENT-EDITOR | testing/testing-reality-checker.md |

### Social Factory
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-SOCIAL-STRATEGIST | marketing/marketing-social-media-strategist.md |
| OBAOBA-IG | marketing/marketing-instagram-curator.md |
| OBAOBA-TIKTOK | marketing/marketing-tiktok-strategist.md |
| OBAOBA-YOUTUBE | marketing/marketing-video-optimization-specialist.md |

### Paid Media
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-PPC-STRATEGIST | paid-media/ppc-campaign-strategist.md |
| OBAOBA-AD-COPYWRITER | marketing/marketing-email-strategist.md |
| OBAOBA-AD-AUDITOR | testing/testing-evidence-collector.md |

### Sales Team
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-OFFER-STRATEGIST | sales/sales-offer-lead-gen-strategist.md |
| OBAOBA-LEAD-GENERATOR | sales/sales-outbound-strategist.md |
| OBAOBA-SALES-OUTREACH | sales/sales-account-strategist.md |

### Product Team
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-PRODUCT-STRATEGIST | product/product-manager.md |
| OBAOBA-OFFER-BUILDER | sales/sales-deal-strategist.md |

### Engineering Team
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-FRONTEND | engineering/engineering-frontend-developer.md |
| OBAOBA-UX | design/design-ux-architect.md |
| OBAOBA-UI | design/design-ui-designer.md |

### QA Team
| Agent | 來源檔案 |
|-------|----------|
| OBAOBA-BRAND-GUARDIAN | design/design-brand-guardian.md |
| OBAOBA-ANALYTICS | testing/testing-performance-benchmarker.md |
| OBAOBA-GROWTH-ANALYST | marketing/marketing-growth-hacker.md |
| OBAOBA-WORKFLOW-OPTIMIZER | testing/testing-workflow-optimizer.md |
| OBAOBA-REALITY-CHECKER | testing/testing-reality-checker.md |

## 安裝步驟

```bash
# 1. 複製所需 Agents
cp agency-agents-temp/marketing/marketing-seo-specialist.md agents/seo-strategist/
cp agency-agents-temp/marketing/marketing-content-creator.md agents/content-creator/
cp agency-agents-temp/engineering/engineering-frontend-developer.md agents/frontend/
# ... 依此類推

# 2. 轉換為 OpenClaw 格式
# 使用 scripts/convert-to-openclaw.py

# 3. 設定環境變數
export OBAOBA_AGENTS_PATH="./agents"
```

## OpenClaw 整合

每個 Agent 需要轉換為 OpenClaw 支援的格式：
- AGENTS.md（角色定義）
- SOUL.md（個性與語氣）
- 可選：MEMORY.md（記憶體）

轉換腳本：`scripts/convert-agency-to-openclaw.py`
