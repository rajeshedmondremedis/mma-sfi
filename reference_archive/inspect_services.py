import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

serv_pos = html.find('Our Services')
news_pos = html.find('In the News')

serv_html = html[serv_pos-200:news_pos]

for m in re.finditer(r'<img[^>]+>', serv_html):
    print("Services Img:", m.group(0))

for m in re.finditer(r'<(h[1-6]|p|a)[^>]*>(.*?)</\1>', serv_html, re.DOTALL):
    tag = m.group(1)
    text = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
    text = ' '.join(text.split())
    if text:
        print(f"[{tag}] {text}")
