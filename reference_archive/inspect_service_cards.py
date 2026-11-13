import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

serv_pos = html.find('Our Services')
news_pos = html.find('In the News')
serv_html = html[serv_pos:news_pos]

cards = re.findall(r'<div[^>]*class="[^"]*elementor-widget-image-box[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>', serv_html, re.DOTALL)
print(f"Image boxes found: {len(cards)}")
for c in cards:
    print(c[:400])
    print("="*40)
