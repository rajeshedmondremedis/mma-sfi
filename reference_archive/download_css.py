import urllib.request
import re

css_urls = [
    'https://mma-sfi.org/wp-content/uploads/elementor/css/post-8.css',
    'https://mma-sfi.org/wp-content/uploads/elementor/css/post-104.css',
    'https://mma-sfi.org/wp-content/uploads/elementor/css/post-114.css',
    'https://mma-sfi.org/wp-content/uploads/elementor/css/post-105.css',
    'https://mma-sfi.org/wp-content/uploads/premium-addons-elementor/pafe-114.css'
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for url in css_urls:
    fname = url.split('/')[-1].split('?')[0]
    print(f"Downloading {fname}...")
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp, open(fname, 'wb') as f:
            f.write(resp.read())
        print(f"Saved {fname}")
    except Exception as e:
        print(f"Error {url}: {e}")
