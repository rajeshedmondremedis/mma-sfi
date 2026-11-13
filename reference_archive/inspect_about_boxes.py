with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
pos = html.find('Vision')
boxes = re.findall(r'<div[^>]*class="[^"]*elementor-widget-icon-box[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>', html[pos-200:pos+5000], re.DOTALL)
print(f"Total icon boxes found: {len(boxes)}")
for i, b in enumerate(boxes):
    title = re.search(r'<h[1-6][^>]*class="[^"]*elementor-icon-box-title[^"]*"[^>]*>(.*?)</h[1-6]>', b)
    desc = re.search(r'<p[^>]*class="[^"]*elementor-icon-box-description[^"]*"[^>]*>(.*?)</p>', b)
    svg = re.search(r'<svg[^>]*>.*?</svg>', b, re.DOTALL)
    print(f"\nBOX {i+1}:")
    print("  Title:", re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else '')
    print("  Desc:", re.sub(r'<[^>]+>', '', desc.group(1)).strip() if desc else '')
    print("  Has SVG:", bool(svg))
