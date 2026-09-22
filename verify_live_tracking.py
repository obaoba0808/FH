"""線上追蹤碼全站驗證 - 掃描 41 頁確認 Clarity + GA4 生效"""
import re, json, urllib.request, concurrent.futures, sys

BASE = "https://obaoba.online/"
CLARITY = "ykmbmbct7c"
GA4 = "G-534539378"

def fetch(path):
    url = BASE + path
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (compatible; OBAOBA-QA/1.0)",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read().decode("utf-8", errors="replace")
            return path, r.status, len(raw), (CLARITY in raw), (GA4 in raw), None
    except Exception as e:
        return path, 0, 0, False, False, str(e)

def main():
    # 讀取本地 sitemap 取得頁面清單
    try:
        with open("sitemap.xml", encoding="utf-8") as f:
            sm = f.read()
        paths = re.findall(r"<loc>([^<]+)</loc>", sm)
        paths = [p.replace("https://obaoba.online/", "").strip() for p in paths]
        paths = [p for p in paths if p and not p.startswith("http")]
    except Exception as e:
        print("sitemap 讀取失敗:", e)
        sys.exit(1)

    print(f"sitemap 頁面數: {len(paths)}")
    print("-" * 78)

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for r in ex.map(fetch, paths):
            results.append(r)

    ok = fail = 0
    fails = []
    for path, status, ln, cl, ga, err in results:
        if err:
            print(f"ERROR  {path:<34} {err[:40]}")
            fail += 1
            fails.append((path, "ERROR"))
        elif status == 200 and cl and ga:
            ok += 1
        else:
            parts = []
            if status != 200: parts.append(f"HTTP={status}")
            if not cl: parts.append("Clarity=MISSING")
            if not ga: parts.append("GA4=MISSING")
            print(f"FAIL   {path:<34} {' '.join(parts)}")
            fail += 1
            fails.append((path, " ".join(parts)))

    print("-" * 78)
    print(f"總計 {len(paths)} 頁 | PASS {ok} | FAIL {fail}")

    report = {
        "total": len(paths), "pass": ok, "fail": fail,
        "clarity_id": CLARITY, "ga4_id": GA4,
        "failures": [{"path": p, "reason": r} for p, r in fails],
    }
    with open("verify_live_report.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print("報告已寫入 verify_live_report.json")
    return 0 if fail == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
