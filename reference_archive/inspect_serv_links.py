with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
pos = html.find('Our Services')
sub = html[pos:pos+4000]

for m in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', sub, re.DOTALL):
    href = m.group(1)
    text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
    print(f"Service link: '{text}' -> {href}")
