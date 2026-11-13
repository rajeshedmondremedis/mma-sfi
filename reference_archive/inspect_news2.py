import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

news_pos = html.find('In the News')
cta_pos = html.find('SHAPING THE FUTURE OF INDIAN MMA')
news_html = html[news_pos:cta_pos]

# Let's see all h4, img, p, a in news_html
for m in re.finditer(r'<h4[^>]*>(.*?)</h4>', news_html, re.DOTALL):
    print("H4:", re.sub(r'<[^>]+>', '', m.group(1)).strip())

for m in re.finditer(r'<img[^>]+src=["\']([^"\']+)["\']', news_html):
    print("IMG:", m.group(1))

for m in re.finditer(r'<p[^>]*>(.*?)</p>', news_html, re.DOTALL):
    print("P:", re.sub(r'<[^>]+>', '', m.group(1)).strip())
