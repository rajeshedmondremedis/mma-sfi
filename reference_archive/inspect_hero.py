import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's inspect everything between header and Training Hours
p_start = html.find('data-elementor-id="114"')
th_pos = html.find('Training Hours')
hero_html = html[p_start:th_pos]

with open('hero_dump.txt', 'w', encoding='utf-8') as out:
    out.write(hero_html)

# Let's also check background images in CSS or inline style
bg_imgs = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', hero_html)
print("Background images in hero HTML:", bg_imgs)

# Let's check post-114.css for background images
with open('post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css_114 = f.read()

css_bg = re.findall(r'url\([\'"]?([^\'")]+)[\'"]?\)', css_114)
print("Background images in post-114.css:", set(css_bg))

# Let's find all text in hero_html
text_in_hero = []
for m in re.finditer(r'>([^<]+)<', hero_html):
    t = m.group(1).strip()
    if t and not t.startswith('{') and not t.startswith('/*'):
        text_in_hero.append(t)
print("Hero text chunks:", text_in_hero)
