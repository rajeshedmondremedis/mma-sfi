import re

with open('reference_archive/post-105.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# find all rules with background or color
rules = re.findall(r'(\.elementor-105\s+[^{]+)\{([^}]+)\}', css)
for sel, body in rules:
    bgs = re.findall(r'background(?:-color)?:\s*([^;]+);', body)
    colors = re.findall(r'(?<!background-)color:\s*([^;]+);', body)
    if bgs or colors:
        print(sel.strip()[:60])
        if bgs: print("  BGs:", bgs)
        if colors: print("  Colors:", colors)
