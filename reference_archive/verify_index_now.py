import os
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

imgs = re.findall(r'src=["\']([^"\']+)["\']', html)
missing_imgs = [s for s in imgs if not s.startswith('http') and not os.path.exists(s)]
print('Images check:', 'ALL OK' if not missing_imgs else f'MISSING: {missing_imgs}')

links = re.findall(r'href=["\']([^"\']+\.html)["\']', html)
missing_links = [l for l in links if not os.path.exists(l)]
print('Links check:', 'ALL OK' if not missing_links else f'MISSING: {missing_links}')
