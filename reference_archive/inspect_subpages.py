import os
import re

for fname in os.listdir('scraped_pages'):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join('scraped_pages', fname)
    with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    print(f"\n==========================================")
    print(f"PAGE: {fname}")
    print(f"==========================================")
    
    # Title
    t_m = re.search(r'<title>(.*?)</title>', html, re.I)
    print("Title:", t_m.group(1).strip() if t_m else '')

    # Headings
    headings = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.I | re.DOTALL)
    print("Headings count:", len(headings))
    for tag, h in headings[:15]:
        clean = re.sub(r'<[^>]+>', '', h).strip()
        clean = ' '.join(clean.split())
        if clean:
            print(f"  [{tag}] {clean[:90]}")

    # Images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    print(f"Images count: {len(imgs)}")
    for img in imgs[:5]:
        print(f"  img: {img}")
