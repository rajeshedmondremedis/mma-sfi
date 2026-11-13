import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('India Shines in MMA at the 3rd Asian Youth Games')
print(html[pos-300:pos+800])
