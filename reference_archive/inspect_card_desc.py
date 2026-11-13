import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

serv_pos = html.find('Our Services')
news_pos = html.find('In the News')
serv_html = html[serv_pos:news_pos]

for box in re.finditer(r'<div class="elementor-image-box-wrapper">(.*?)</div>\s*</div>\s*</div>', serv_html, re.DOTALL):
    chunk = box.group(1)
    title = re.search(r'<h4[^>]*>(.*?)</h4>', chunk)
    desc = re.search(r'<p[^>]*>(.*?)</p>', chunk)
    img = re.search(r'src=["\']([^"\']+)["\']', chunk)
    print("CARD:")
    print("  Img:", img.group(1) if img else '')
    print("  Title:", re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else '')
    print("  Desc:", re.sub(r'<[^>]+>', '', desc.group(1)).strip() if desc else 'NO DESC')
