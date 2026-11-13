import os
import re
import urllib.request

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
os.makedirs('assets/images', exist_ok=True)

all_urls = set()
for fname in os.listdir('scraped_pages'):
    if not fname.endswith('.html'):
        continue
    with open(os.path.join('scraped_pages', fname), 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    found = re.findall(r'https?://[^\s"\'\)]+\.(?:png|jpe?g|webp|gif|svg)', html)
    for u in found:
        if 'mma-sfi.org' in u:
            all_urls.add(u)

print(f"Total distinct URLs to check: {len(all_urls)}")
for u in sorted(all_urls):
    bname = os.path.basename(u.split('?')[0])
    lpath = os.path.join('assets', 'images', bname)
    if os.path.exists(lpath) and os.path.getsize(lpath) > 0:
        continue
    print(f"Downloading {bname}...")
    try:
        req = urllib.request.Request(u, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as resp, open(lpath, 'wb') as f:
            f.write(resp.read())
        print(f"  OK: {bname} ({os.path.getsize(lpath)} bytes)")
    except Exception as e:
        print(f"  Error {bname}: {e}")

print("Done downloading subpage assets.")
