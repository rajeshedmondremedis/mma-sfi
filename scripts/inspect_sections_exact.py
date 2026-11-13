import re

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

cids = ['56b282c', '54296030', '17e44004', '38a3be7', 'ec16965', '249aabf', '5a6cbe1', '19be1a00', '3fa26d4', '24865c3', '2ec5c1a', '7ea6de4f']

for cid in cids:
    # search css for cid
    print(f"=== CSS for {cid} ===")
    matches = re.findall(rf'(\.[^{{]*{cid}[^{{]*)\{{([^}}]+)\}}', css)
    for sel, body in matches:
        b = re.findall(r'background(?:-color)?:\s*([^;]+);', body)
        c = re.findall(r'(?<!background-)color:\s*([^;]+);', body)
        border = re.findall(r'border(?:-color)?:\s*([^;]+);', body)
        shadow = re.findall(r'box-shadow:\s*([^;]+);', body)
        print("  SEL:", sel.strip())
        if b: print("    BGs:", b)
        if c: print("    Colors:", c)
        if border: print("    Borders:", border)
        if shadow: print("    Shadows:", shadow)
