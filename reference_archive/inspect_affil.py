import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

affil_pos = html.find('Affiliations')
services_pos = html.find('Our Services')

affil_html = html[affil_pos-200:services_pos]

for m in re.finditer(r'<img[^>]+>', affil_html):
    print("Affil Img:", m.group(0))

for m in re.finditer(r'<(h[1-6]|p)[^>]*>(.*?)</\1>', affil_html, re.DOTALL):
    tag = m.group(1)
    text = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
    text = ' '.join(text.split())
    print(f"[{tag}] {text}")
