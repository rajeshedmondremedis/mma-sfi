import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Let's find all containers with data-id
containers = re.findall(r'<div[^>]*class="([^"]*elementor-element-([a-f0-9]+)[^"]*e-con-(?:boxed|full)[^"]*)"[^>]*data-id="([^"]+)"[\s\S]*?(?=<div[^>]*class="[^"]*e-con-|$)', html)

for full_cls, cid, did in containers[:35]:
    # find heading in this snippet
    # find in css
    pattern = rf'\.elementor-element-{cid}[^{{]*\{{([^}}]+)\}}'
    matches = re.findall(pattern, css)
    styles = []
    for m in matches:
        for p in m.split(';'):
            p = p.strip()
            if any(k in p for k in ['background', 'color', 'border']):
                styles.append(p)
    print(f"Container {cid} (did={did}): {styles}")
