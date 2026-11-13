with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re

pos = html.find('Who We Are')
print("Who We Are context:")
# let's find the parent container
sub = html[pos-400:pos+3500]
# find e-con-inner and children
for m in re.finditer(r'<div class="elementor-element elementor-element-([a-f0-9]+)[^"]* e-con e-child"', sub):
    print("Child container:", m.group(0)[:120])
