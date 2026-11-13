with open('page_extracted.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
# Print first 150 lines
for l in lines[:150]:
    print(l, end='')
