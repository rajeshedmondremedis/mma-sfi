import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Check all local image sources in index.html
imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
print(f"Total img src attributes in index.html: {len(imgs)}")

missing = []
for src in imgs:
    if not src.startswith('http') and not src.startswith('//') and not src.startswith('data:'):
        # Local file
        if not os.path.exists(src):
            missing.append(src)
        else:
            print(f"OK: {src} ({os.path.getsize(src)} bytes)")

if missing:
    print("\nWARNING - Missing local files:", missing)
else:
    print("\nAll local image references in index.html exist and are valid!")

# Check style.css images
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css_imgs = re.findall(r'url\(["\']?([^"\'\)]+)["\']?\)', css)
print(f"\nCSS url() references: {css_imgs}")
for c_url in css_imgs:
    resolved = os.path.normpath(os.path.join('assets/css', c_url))
    if not os.path.exists(resolved):
        print(f"WARNING - Missing CSS file: {c_url} -> {resolved}")
    else:
        print(f"OK CSS asset: {c_url} -> {resolved} ({os.path.getsize(resolved)} bytes)")
