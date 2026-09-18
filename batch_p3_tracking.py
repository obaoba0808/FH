import re
import os
from datetime import datetime

# Phase 3: Conversion & Tracking Optimization
# P3-2: Microsoft Clarity
# P3-3: Meta Pixel + Google Ads Remarketing

CLARITY_SCRIPT = '''<!-- Microsoft Clarity -->
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "CLARITY_ID");
</script>
'''

META_PIXEL_SCRIPT = '''<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'META_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=META_PIXEL_ID&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
'''

GOOGLE_ADS_REMARKETING_SCRIPT = '''<!-- Google Ads Remarketing -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-GOOGLE_ADS_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'AW-GOOGLE_ADS_ID');
</script>
'''

# CTA A/B Test Configuration (P3-1)
AB_TEST_SCRIPT = '''<!-- CTA A/B Testing -->
<script>
(function() {
    // Simple A/B test for CTA button text
    var variant = Math.random() < 0.5 ? 'A' : 'B';
    window.ctaVariant = variant;
    
    // Variant A: Original text
    // Variant B: Alternative text
    var ctaTexts = {
        'A': '加 LINE 預約',
        'B': '立即獲取今日班表'
    };
    
    // Store variant for analytics
    if (typeof gtag !== 'undefined') {
        gtag('event', 'ab_test_variant', {
            'event_category': 'cta_test',
            'event_label': variant,
            'value': 1
        });
    }
    
    // Apply variant text after DOM ready
    document.addEventListener('DOMContentLoaded', function() {
        var ctaButtons = document.querySelectorAll('[data-ab-test="cta"]');
        ctaButtons.forEach(function(btn) {
            btn.textContent = ctaTexts[variant];
        });
    });
})();
</script>
'''

# Voice Search FAQ Structured Data (P3-5)
VOICE_SEARCH_FAQ_SCHEMA = '''<script type="application/ld+json">{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "嘿 Siri，台北叫傳播推薦哪一家？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "歐巴傳播是台北頂級傳播公司，提供傳播妹桌面服務、KTV派對、公關娛樂與飯局妹外派服務。LINE：@938nzmjr 立即預約，30分鐘內到府安排。"
      }
    },
    {
      "@type": "Question",
      "name": "OK Google，叫傳播多少錢？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "叫傳播的價格依公關等級不同，約落在新台幣3,000到5,000元以上每2小時。基礎級3,000元、標準級3,600元、VIP級4,000元、頂級5,000元以上。加時每小時約1,500元以上。建議加LINE詢問當日行情。"
      }
    },
    {
      "@type": "Question",
      "name": "嘿 Siri，第一次叫傳播要注意什麼？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "第一次叫傳播建議選擇正規公司如歐巴傳播，注意事項包括：確認公司合法性、了解收費標準、保護個人隱私、事先溝通需求、選擇適合的公關等級。歐巴傳播提供打槍換人機制，不滿意可免費更換。"
      }
    }
  ]
}</script>
'''

def add_tracking_to_page(filepath, page_name):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    changes = []
    
    # Find </head> position
    head_end = content.find('</head>')
    if head_end == -1:
        changes.append('WARNING: No </head> tag found')
        return False, changes
    
    # P3-2: Add Microsoft Clarity (before </head>)
    if 'clarity.ms' not in content:
        content = content[:head_end] + CLARITY_SCRIPT + '\n' + content[head_end:]
        changes.append('P3-2: Microsoft Clarity script added')
    else:
        changes.append('P3-2: Microsoft Clarity already present')
    
    # P3-3: Add Meta Pixel (before </head>)
    if 'fbq' not in content:
        content = content[:head_end] + META_PIXEL_SCRIPT + '\n' + content[head_end:]
        changes.append('P3-3: Meta Pixel added')
    else:
        changes.append('P3-3: Meta Pixel already present')
    
    # P3-3: Add Google Ads Remarketing (before </head>)
    if 'AW-' not in content:
        content = content[:head_end] + GOOGLE_ADS_REMARKETING_SCRIPT + '\n' + content[head_end:]
        changes.append('P3-3: Google Ads Remarketing added')
    else:
        changes.append('P3-3: Google Ads Remarketing already present')
    
    # P3-1: Add A/B Test script (before </head>)
    if 'ctaVariant' not in content:
        content = content[:head_end] + AB_TEST_SCRIPT + '\n' + content[head_end:]
        changes.append('P3-1: CTA A/B Test script added')
    else:
        changes.append('P3-1: CTA A/B Test already present')
    
    # P3-5: Add Voice Search FAQ Schema (only for index.html and faq-all-in-one.html)
    if '嘿 Siri' not in content and filepath in ['index.html', 'faq-all-in-one.html']:
        content = content[:head_end] + VOICE_SEARCH_FAQ_SCHEMA + '\n' + content[head_end:]
        changes.append('P3-5: Voice Search FAQ Schema added')
    
    # Write if changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True, changes
    else:
        return False, changes

# Process key pages first (index + high-traffic pages)
KEY_PAGES = [
    'index.html',
    'how_much.html',
    'faq-all-in-one.html',
    'pricing-guide-2026.html',
    'about-oppa.html',
    'first_time_called.html',
    'KTV_recommendations.html',
    'motel_safe.html',
    'safety_privacy.html',
    'business-guide.html',
]

print('=' * 60)
print('Phase 3: Conversion & Tracking Optimization')
print(f'Timestamp: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
print('=' * 60)
print('')

total_modified = 0
for filename in KEY_PAGES:
    if os.path.exists(filename):
        changed, changes = add_tracking_to_page(filename, filename)
        status = 'MODIFIED' if changed else 'NO CHANGE'
        print(f'[{status}] {filename}')
        for change in changes:
            print(f'  - {change}')
        print('')
        if changed:
            total_modified += 1
    else:
        print(f'[MISSING] {filename}')

print('=' * 60)
print(f'Total pages processed: {len(KEY_PAGES)}')
print(f'Total pages modified: {total_modified}')
print('')
print('IMPORTANT: Replace placeholder IDs before deployment:')
print('  - CLARITY_ID: Get from https://clarity.microsoft.com')
print('  - META_PIXEL_ID: Get from Meta Events Manager')
print('  - AW-GOOGLE_ADS_ID: Get from Google Ads')
print('=' * 60)
