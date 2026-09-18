import urllib.request
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

pages = [
    "news.html", "first-chat-topics.html", "venue-guide-2026.html", "newbie-guide-2026.html",
    "safety_privacy.html", "recruitment.html", "shoot_switch_personnel.html", "one_by_one.html",
    "special_industries.html", "suitable_female.html", "KTV_party.html", "interaction_scale.html",
    "business_dinner.html", "is_this_right_for_you.html", "shoot_guide.html", "can-touch-guide.html",
    "companion-levels-2026.html", "male_companion.html", "taipei_agency_guide.html", "first-time-2026.html",
    "tipping-guide-2026.html", "safety-guide-2026.html", "how-to-choose-right-companion.html",
    "compare-girls.html", "legality-guide.html", "booking-guide.html", "pricing-guide-2026.html",
    "faq-all-in-one.html", "about-oppa.html", "beginners-checklist.html", "2026-pricing-table.html",
    "private-party-guide.html"
]

def download(page):
    url = f"https://obaoba.online/{page}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read()
            with open(page, 'wb') as f:
                f.write(content)
            return (page, len(content), "OK")
    except Exception as e:
        return (page, 0, str(e))

results = []
with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(download, p): p for p in pages}
    for future in as_completed(futures):
        results.append(future.result())

for page, size, status in sorted(results):
    if status == "OK":
        print(f"OK  {page:40s}  {size:6d} bytes")
    else:
        print(f"ERR {page:40s}  {status}")

ok_count = sum(1 for r in results if r[2] == "OK")
print(f"\nTotal: {ok_count}/{len(pages)} downloaded successfully")
