# Phase 2-1: 地理型長尾頁計畫

## 目標關鍵字

| 優先序 | 頁面 | 目標關鍵字 | 預估月搜尋量 |
|--------|------|-----------|-------------|
| 1 | `/taipei-daan.html` | 大安區傳播推薦、大安區叫傳播 | 800 |
| 2 | `/taipei-xinyi.html` | 信義區叫傳播、信義區傳播公司 | 750 |
| 3 | `/taipei-banqiao.html` | 板橋傳播公司、板橋叫傳播 | 600 |
| 4 | `/taipei-zhongxiao.html` | 忠孝東路傳播、東區叫傳播 | 500 |
| 5 | `/taipei-songshan.html` | 松山區傳播推薦 | 450 |
| 6 | `/taipei-zhonghe.html` | 中和傳播公司、永和叫傳播 | 400 |
| 7 | `/taipei-shilin.html` | 士林區傳播推薦 | 350 |
| 8 | `/taipei-beitou.html` | 北投叫傳播、北投傳播公司 | 300 |
| 9 | `/taipei-neihu.html` | 內湖傳播公司 | 250 |
| 10 | `/taipei-nangang.html` | 南港叫傳播 | 200 |

## 頁面結構範本

```html
<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <title>[區域]傳播推薦｜[區域特色]｜歐巴傳播</title>
    <meta name="description" content="[區域]傳播推薦，歐巴傳播提供[區域]到府服務，30分鐘內抵達。專業公關、價格透明，LINE：@938nzmjr 立即預約。">
    <!-- Schema: LocalBusiness + Service -->
</head>
<body>
    <h1>[區域]傳播推薦｜歐巴傳播 [區域]到府服務</h1>
    
    <section id="intro">
        <h2>為什麼選擇歐巴傳播的[區域]服務？</h2>
        <p>[區域特色描述，如：大安區是台北市中心，鄰近信義商圈...]</p>
    </section>
    
    <section id="coverage">
        <h2>[區域]服務範圍</h2>
        <ul>
            <li>[區域內熱門地點1，如：大安森林公園周邊]</li>
            <li>[區域內熱門地點2，如：東區商圈]</li>
            <li>[區域內熱門地點3，如：忠孝復興]</li>
        </ul>
    </section>
    
    <section id="pricing">
        <h2>[區域]傳播價格</h2>
        <p>基礎級 NT$3,000/2hr | 標準級 NT$3,600/2hr | VIP級 NT$4,000/2hr</p>
        <p>[區域]車馬費：通常免費或 NT$300-500</p>
    </section>
    
    <section id="cta">
        <h2>立即預約[區域]傳播</h2>
        <a href="https://line.me/R/ti/p/@938nzmjr">加 LINE 預約</a>
        <a href="tel:+886926656666">0926-656666</a>
    </section>
    
    <section id="faq">
        <h2>[區域]叫傳播常見問題</h2>
        <!-- FAQ Schema -->
    </section>
    
    <nav aria-label="相關區域">
        <a href="taipei-xinyi.html">信義區傳播</a>
        <a href="taipei-banqiao.html">板橋傳播</a>
        <!-- 其他區域連結 -->
    </nav>
</body>
</html>
```

## 內部連結策略

- 每個地理頁連結回首頁、how_much.html、faq-all-in-one.html
- 地理頁之間互相連結（相關區域）
- 連結至 about-oppa.html 建立信任

## Schema 結構

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "LocalBusiness",
      "name": "歐巴傳播 [區域]服務",
      "areaServed": {
        "@type": "City",
        "name": "[區域]"
      },
      "serviceType": "傳播服務"
    },
    {
      "@type": "Service",
      "serviceType": "[區域]傳播到府服務"
    }
  ]
}
```
