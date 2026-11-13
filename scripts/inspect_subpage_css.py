import re

for page in ['about-us.html', 'team.html', 'events.html', 'contact-us.html']:
    path = f'reference_archive/scraped_pages/{page}'
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()
    # find linked css
    css_files = re.findall(r'href=["\']([^"\']+\.css[^"\']*)["\']', html)
    post_css = [c for c in css_files if 'post-' in c]
    print(f"{page} uses post css:", post_css)
