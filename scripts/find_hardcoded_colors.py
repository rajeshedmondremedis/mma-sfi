import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

dark_colors = ['#000', '#06070a', '#080a0d', '#0d0f12', '#0f1217', '#11141a', '#0a0b0e', '#040507', '#050608', '#08090b', '#101318']

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    matches = []
    for idx, line in enumerate(lines, 1):
        if 'style=' in line:
            if '#fff' in line.lower() or any(c in line.lower() for c in dark_colors):
                matches.append((idx, line.strip()))
    if matches:
        print(f"=== {f} ({len(matches)} matches) ===")
        for line_num, l in matches[:10]:
            print(f"  Line {line_num}: {l}")
