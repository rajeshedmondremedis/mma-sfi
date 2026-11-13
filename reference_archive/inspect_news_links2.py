with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
pos = html.find('In the News')
sub = html[pos:pos+15000]

for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', sub, re.DOTALL):
    href = m.group(1)
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    if text:
        print(f"{text} -> {href}")
