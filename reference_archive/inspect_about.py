import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

about_pos = html.find('Who We Are')
affil_pos = html.find('Affiliations')

about_html = html[about_pos-300:affil_pos]

with open('about_dump.txt', 'w', encoding='utf-8') as out:
    out.write(about_html)

for m in re.finditer(r'<img[^>]+>', about_html):
    print("About Img:", m.group(0))

for m in re.finditer(r'<(h[1-6]|p)[^>]*>(.*?)</\1>', about_html, re.DOTALL):
    tag = m.group(1)
    text = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
    text = ' '.join(text.split())
    print(f"[{tag}] {text}")
