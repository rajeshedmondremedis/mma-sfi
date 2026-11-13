import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Look for data-elementor-type or data-elementor-id
ids = re.findall(r'data-elementor-type="([^"]*)"\s+data-elementor-id="([^"]*)"', html)
print("Elementor sections:", ids)

# Look for all <header> and <footer> tags or classes
headers = re.findall(r'<header[^>]*>.*?</header>', html, re.DOTALL)
print(f"Header tags count: {len(headers)}")

footers = re.findall(r'<footer[^>]*>.*?</footer>', html, re.DOTALL)
print(f"Footer tags count: {len(footers)}")

# Let's inspect CSS files: post-8.css, post-114.css, post-104.css, post-105.css
# Let's download the key CSS files to check colors, fonts, styles!
