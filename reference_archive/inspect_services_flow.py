with open('original_widgets_flow.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect widgets 35 to 55
lines = text.split('\n[')
for l in lines:
    if any(f'[{i}]' in '[' + l for i in range(35, 55)):
        print('[' + l)
