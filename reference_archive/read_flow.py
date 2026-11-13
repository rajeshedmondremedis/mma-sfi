with open('original_widgets_flow.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for l in lines:
    print(l, end='')
