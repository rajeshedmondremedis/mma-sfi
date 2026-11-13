import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]
print("Checking HTML files for inline styles:", files)

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    # find style attributes
    styles = re.findall(r'style="([^"]*)"', content)
    inline_bgs = [s for s in styles if 'background' in s or 'color' in s]
    if inline_bgs:
        print(f"\n{f} has {len(inline_bgs)} inline color/bg styles:")
        for s in inline_bgs[:5]:
            print("  ", s)
