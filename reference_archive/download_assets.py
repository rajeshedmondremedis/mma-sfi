import re
import os
import urllib.request

os.makedirs('assets/images', exist_ok=True)

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

with open('post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

all_imgs = set(re.findall(r'https?://[^\s"\'\)]+\.(?:png|jpe?g|webp|gif|svg)', html + css))
print(f"Found {len(all_imgs)} distinct images/assets")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

saved_map = {}
for url in sorted(all_imgs):
    # filter only mma-sfi.org or relevant assets
    if 'mma-sfi.org' not in url and 'unwwind.com' not in url:
        continue
    base_name = os.path.basename(url.split('?')[0])
    local_path = os.path.join('assets', 'images', base_name)
    print(f"Downloading {base_name} ...")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp, open(local_path, 'wb') as f:
            f.write(resp.read())
        saved_map[url] = f"assets/images/{base_name}"
        print(f"  OK: {local_path} ({os.path.getsize(local_path)} bytes)")
    except Exception as e:
        print(f"  FAILED {url}: {e}")

print(f"\nSuccessfully downloaded {len(saved_map)} images.")
