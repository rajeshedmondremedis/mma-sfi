import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

for cid in ['587d4413', '249aabf', '19be1a00', '2ec5c1a', '24865c3']:
    pos = html.find(cid)
    if pos != -1:
        snippet = html[pos:pos+1500]
        # remove tags to see text
        clean = re.sub(r'<[^>]+>', ' ', snippet)
        print(f"=== Container {cid} ===")
        print(' '.join(clean.split()[:40]))
