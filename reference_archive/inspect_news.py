import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

news_pos = html.find('In the News')
cta_pos = html.find('SHAPING THE FUTURE OF INDIAN MMA')
news_html = html[news_pos:cta_pos]

with open('news_cards.txt', 'w', encoding='utf-8') as out:
    # Find all articles / containers
    cards = re.findall(r'<div class="elementor-element elementor-element-[a-f0-9]+ e-con-full e-flex[^"]* e-con e-child".*?<!-- \.elementor-element -->', news_html, re.DOTALL)
    for i, c in enumerate(cards):
        out.write(f"\n--- NEWS CARD {i+1} ---\n")
        title = re.search(r'<h4[^>]*>(.*?)</h4>', c)
        p = re.search(r'<p[^>]*>(.*?)</p>', c)
        img = re.search(r'src=["\']([^"\']+)["\']', c)
        btn = re.search(r'<a[^>]+class="[^"]*elementor-button[^"]*"[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', c)
        out.write(f"Title: {re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else ''}\n")
        out.write(f"Img: {img.group(1) if img else ''}\n")
        out.write(f"Excerpt: {re.sub(r'<[^>]+>', '', p.group(1)).strip() if p else ''}\n")
        out.write(f"Button: {re.sub(r'<[^>]+>', '', btn.group(2)).strip() if btn else ''} -> {btn.group(1) if btn else ''}\n")

print("Wrote news_cards.txt")
