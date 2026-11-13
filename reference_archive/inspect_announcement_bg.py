with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('d26badd')
print(html[pos-300:pos+200])

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
# find background for parent of d26badd
parent_id = re.search(r'elementor-element-([a-f0-9]+)[^>]*>\s*<div[^>]*>\s*<div[^>]*elementor-element-d26badd', html)
if parent_id:
    p_id = parent_id.group(1)
    print("Parent ID:", p_id)
    p_css = re.findall(rf'\.{p_id}[^{{]*\{{([^}}]+)\}}', css)
    print("Parent CSS:", p_css)
