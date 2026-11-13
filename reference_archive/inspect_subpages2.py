import os
import re

def print_page_details(fname):
    print(f"\n==================== {fname} ====================")
    with open(os.path.join('scraped_pages', fname), 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Find the main body
    body_m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if not body_m:
        body_m = re.search(r'data-elementor-type="wp-page"[^>]*>(.*?)</div>\s*</div>\s*<!-- \.entry-content -->', html, re.DOTALL)
    
    text = body_m.group(1) if body_m else html
    
    # print all headings and paragraphs
    items = re.findall(r'<(h[1-6]|p|li|a)[^>]*>(.*?)</\1>', text, re.DOTALL | re.I)
    for tag, content in items:
        cleaned = re.sub(r'<[^>]+>', '', content).strip()
        cleaned = ' '.join(cleaned.split())
        if len(cleaned) > 2 and not cleaned.startswith('{') and not cleaned.startswith('/*') and 'Primary Menu' not in cleaned:
            if tag in ['h1', 'h2', 'h3', 'h4']:
                print(f"[{tag.upper()}] {cleaned}")
            elif tag in ['p', 'li'] and len(cleaned) > 20:
                print(f"   {cleaned[:140]}...")

print_page_details('team.html')
print_page_details('about-us.html')
print_page_details('anti-doping.html')
print_page_details('safeguarding.html')
