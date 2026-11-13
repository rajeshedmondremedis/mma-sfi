with open('full_subpages_content.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split('==================================================')
for sec in sections:
    if not sec.strip():
        continue
    lines = sec.strip().split('\n')
    header_line = lines[0]
    print(f"\n>>> {header_line}")
    # print first 20 non-img lines
    shown = 0
    for l in lines[1:]:
        if shown < 20:
            print(f"  {l}")
            shown += 1
