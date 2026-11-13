import re

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css114 = f.read()

# Let's inspect all rules with background-color
rules = re.findall(r'(\.[^{]+)\{([^}]*background[^}]*)\}', css114)
print(f"Total background rules in post-114.css: {len(rules)}")
for sel, body in rules:
    print("SELECTOR:", sel[:80])
    # extract background or background-color
    bgs = re.findall(r'background(?:-color)?:\s*([^;]+);', body)
    colors = re.findall(r'color:\s*([^;]+);', body)
    print("  BGs:", bgs)
    if colors:
        print("  Colors:", colors)
    print("-" * 30)

with open('reference_archive/post-104.css', 'r', encoding='utf-8', errors='ignore') as f:
    css104 = f.read()

print("\n=== HEADER CSS (post-104.css) ===")
rules104 = re.findall(r'(\.[^{]+)\{([^}]*background[^}]*)\}', css104)
for sel, body in rules104:
    print("SELECTOR:", sel[:80])
    bgs = re.findall(r'background(?:-color)?:\s*([^;]+);', body)
    print("  BGs:", bgs)

