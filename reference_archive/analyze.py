import re
from html.parser import HTMLParser

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Extract title
title_m = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
print('Title:', title_m.group(1).strip() if title_m else 'None')

# Extract meta description
desc_m = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
print('Description:', desc_m.group(1).strip() if desc_m else 'None')

# Find stylesheets
print('\n--- CSS Links ---')
for m in re.finditer(r'<link[^>]*rel=["\']stylesheet["\'][^>]*href=["\']([^"\']*)["\']', html, re.IGNORECASE):
    print(m.group(1))

# Find scripts
print('\n--- JS Scripts ---')
for m in re.finditer(r'<script[^>]*src=["\']([^"\']*)["\']', html, re.IGNORECASE):
    print(m.group(1))

# Find headings
print('\n--- Headings ---')
for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.IGNORECASE | re.DOTALL):
    tag = m.group(1)
    text = re.sub(r'<[^>]+>', ' ', m.group(2))
    text = ' '.join(text.split())
    if text:
        print(f'<{tag}>: {text}')

# Find images
print('\n--- Images (sample) ---')
for i, m in enumerate(re.finditer(r'<img[^>]+>', html, re.IGNORECASE)):
    if i < 30:
        tag = m.group(0)
        src_m = re.search(r'src=["\']([^"\']+)["\']', tag)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', tag)
        print(f"Img: alt='{alt_m.group(1) if alt_m else ''}' src='{src_m.group(1) if src_m else ''}'")

# Look at overall body structure or classes
print('\n--- Body class ---')
body_m = re.search(r'<body[^>]*class=["\']([^"\']*)["\']', html, re.IGNORECASE)
print('Body class:', body_m.group(1) if body_m else 'None')
