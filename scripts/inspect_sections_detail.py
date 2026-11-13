import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

def get_css_props(elem_id):
    pattern = rf'\.elementor-element-{elem_id}(?::not\([^\)]+\)|::before)?\s*\{{([^}}]+)\}}'
    matches = re.findall(pattern, css)
    props = []
    for m in matches:
        for line in m.split(';'):
            line = line.strip()
            if any(k in line for k in ['background', 'color', 'border']):
                props.append(line)
    return props

# Find all direct elementor-top-section or elementor-element with data-element_type="container" or "section"
containers = re.findall(r'<div[^>]*class="[^"]*elementor-element-([a-f0-9]+)[^"]*elementor-top-(?:section|container|column)[^"]*"[^>]*data-id="([^"]+)"[^>]*>', html)

if not containers:
    # try broader match
    containers = re.findall(r'data-id="([a-f0-9]+)"[^>]*data-element_type="(?:container|section)"', html)
    print(f"Found {len(containers)} containers")
    for cid in containers[:25]:
        props = get_css_props(cid)
        print(f"Container {cid}: {props}")
else:
    for cid, did in containers:
        props = get_css_props(cid)
        print(f"Container {cid}: {props}")
