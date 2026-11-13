import re

with open('hero_dump.txt', 'r', encoding='utf-8', errors='ignore') as f:
    hero = f.read()

# Let's find all images
imgs = re.findall(r'<img[^>]+>', hero)
print(f"Total images in hero: {len(imgs)}")
for img in imgs:
    src = re.search(r'src=["\']([^"\']+)["\']', img)
    alt = re.search(r'alt=["\']([^"\']*)["\']', img)
    print(f"  src: {src.group(1) if src else ''} | alt: {alt.group(1) if alt else ''}")

# Let's find any text or links or widgets
widgets = re.findall(r'data-widget_type="([^"]+)"', hero)
print("Hero widgets:", set(widgets))
