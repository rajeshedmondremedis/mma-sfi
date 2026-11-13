import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's inspect the entire container of the 3 stats
stat_pos = html.find('Training Hours')
print(html[stat_pos-500:stat_pos+2500])
