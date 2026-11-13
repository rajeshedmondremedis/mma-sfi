import re

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# Let's search for rules that set background or color on main container elements
blocks = re.findall(r'(\.elementor-element-[a-f0-9]+[^{]*)\{([^}]+)\}', css)

# Map of major IDs in page.html
# e.g., about, services, etc.
with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

for sel, body in blocks:
    if 'background' in body or 'color:' in body:
        # let's see what this selector targets
        # filter interesting ones
        if any(prop in body for prop in ['background-color', 'background:', 'color:']):
            # let's clean up body
            props = [p.strip() for p in body.split(';') if any(k in p for k in ['background', 'color', 'border', 'box-shadow'])]
            if props:
                print(f"{sel.strip()[:60]} => {props[:3]}")
