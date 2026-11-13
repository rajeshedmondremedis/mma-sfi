import urllib.request
import os

pages = {
    'about-us': 'https://mma-sfi.org/about-us/',
    'news': 'https://mma-sfi.org/news/',
    'events': 'https://mma-sfi.org/events/',
    'event-sanctioning': 'https://mma-sfi.org/event-sanctioning/',
    'anti-doping': 'https://mma-sfi.org/anti-doping-policy-mma-sfi/',
    'safeguarding': 'https://mma-sfi.org/safeguarding/',
    'members-state': 'https://mma-sfi.org/members-state/',
    'team': 'https://mma-sfi.org/team/',
    'contact-us': 'https://mma-sfi.org/contact-us/'
}

os.makedirs('scraped_pages', exist_ok=True)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

for name, url in pages.items():
    print(f"Fetching {name} from {url}...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            filepath = os.path.join('scraped_pages', f"{name}.html")
            with open(filepath, 'wb') as f:
                f.write(content)
            print(f"  Saved {name}.html ({len(content)} bytes)")
    except Exception as e:
        print(f"  Error {name}: {e}")

print("Done fetching pages.")
