import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('SHAPING THE FUTURE OF INDIAN MMA')
print(html[pos-500:pos+800])
