import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]
print(f"Total HTML pages found: {len(html_files)}")

all_ok = True
for f in html_files:
    with open(f, 'r', encoding='utf-8') as page:
        content = page.read()
    
    # Check images
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', content)
    missing_imgs = []
    for src in imgs:
        if not src.startswith('http') and not src.startswith('//') and not src.startswith('data:'):
            if not os.path.exists(src):
                missing_imgs.append(src)
    
    # Check internal page links
    links = re.findall(r'<a[^>]+href=["\']([^"\']+\.html)["\']', content)
    missing_links = []
    for link in links:
        if not os.path.exists(link):
            missing_links.append(link)

    print(f"\nPAGE: {f}")
    print(f"  Images checked: {len(imgs)} (Missing: {len(missing_imgs)})")
    if missing_imgs:
        all_ok = False
        print(f"    Missing images: {missing_imgs}")
    print(f"  Internal links checked: {len(links)} (Missing: {len(missing_links)})")
    if missing_links:
        all_ok = False
        print(f"    Missing links: {missing_links}")

if all_ok:
    print("\nALL PAGES VERIFIED SUCCESSFULLY! No missing images or broken links.")
else:
    print("\nSome issues found. Check output above.")
