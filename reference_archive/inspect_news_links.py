with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
pos = html.find('In the News')
sub = html[pos:pos+12000]

# find all h4 titles and their links
for m in re.finditer(r'<h4[^>]*>(.*?)</h4>', sub):
    print("News title:", re.sub(r'<[^>]+>', '', m.group(1)).strip())

# find all buttons/links
for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', sub):
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    if text and text != 'X':
        print(f"  Link: {text} -> {m.group(1)}")
