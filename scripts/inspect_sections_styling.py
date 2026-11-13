import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

# find all elementor-element-xxxxxxx
elem_ids = set(re.findall(r'elementor-element-([a-f0-9]+)', html))
print(f"Total elementor elements in page.html: {len(elem_ids)}")

# Let's find background colors and font colors in post-114.css
rules = re.findall(r'(\.elementor-114\s+[^\{]+)\{([^\}]+)\}', css)
print(f"Total rules in post-114.css: {len(rules)}")

# Let's find all color properties and their values
colors_used = set(re.findall(r'(?<!background-)color:\s*([^;]+);', css))
bgs_used = set(re.findall(r'background(?:-color)?:\s*([^;]+);', css))

print("Colors used in post-114.css:")
for c in sorted(colors_used):
    print("  ", c)

print("\nBackgrounds used in post-114.css:")
for b in sorted(bgs_used):
    print("  ", b)
