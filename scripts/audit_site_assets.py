import os, re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Auditing {len(html_files)} HTML files...")

all_ok = True

for hf in html_files:
    with open(hf, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    for img in imgs:
        if img.startswith('http') or img.startswith('data:'):
            continue
        # check file existence
        # normalize path
        img_path = img.split('?')[0].split('#')[0]
        if not os.path.exists(img_path):
            print(f"[{hf}] MISSING IMAGE: {img_path}")
            all_ok = False
            
    # Check internal links
    links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\']', html)
    for l in links:
        if l.startswith('http') or l.startswith('mailto:') or l.startswith('tel:') or l.startswith('#'):
            continue
        link_path = l.split('?')[0].split('#')[0]
        if not os.path.exists(link_path):
            print(f"[{hf}] MISSING LINK TARGET: {link_path}")
            all_ok = False

if all_ok:
    print("SUCCESS: All images and internal link targets exist on disk across all 10 HTML pages!")
else:
    print("WARNING: Some assets or links are missing.")
