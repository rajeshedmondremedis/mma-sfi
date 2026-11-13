import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Let's find all parent containers: e-parent
parents = re.findall(r'<div[^>]*class="([^"]*e-parent[^"]*)"[^>]*data-id="([^"]+)"', html)
print(f"Total e-parent containers: {len(parents)}")

for full_cls, cid in parents:
    # find snippet
    pos = html.find(f'data-id="{cid}"')
    snippet = html[pos:pos+1200]
    # find headings in snippet
    headings = re.findall(r'<h[1-6][^>]*>(.*?)</h[1-6]>', snippet)
    clean_h = [re.sub(r'<[^>]+>', '', h).strip() for h in headings]
    
    # find css rules for cid
    pattern = rf'\.elementor-element-{cid}(?::not\([^\)]+\)|::before)?\s*\{{([^}}]+)\}}'
    matches = re.findall(pattern, css)
    bgs = []
    for m in matches:
        bgs.extend(re.findall(r'background(?:-color)?:\s*([^;]+);', m))
    
    is_hidden = 'elementor-hidden-desktop' in full_cls
    print(f"Parent {cid} | Hidden={is_hidden} | Headings={clean_h[:3]} | BGs={bgs}")
