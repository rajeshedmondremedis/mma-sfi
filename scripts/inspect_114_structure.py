import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's find each main section in page.html and look at its classes and inline styles
# In page.html:
# Header: id=104
# Content: id=114
# Footer: id=105

# Let's extract the HTML for id 114
m = re.search(r'data-elementor-id="114"[\s\S]*?data-elementor-id="105"', html)
if m:
    content_html = m.group(0)
    print("Found content container 114. Length:", len(content_html))
    
    # Let's find top-level sections inside 114
    # Find all direct <section> or <div class="... elementor-top-section ..."> or <div class="... e-con-boxed ...">
    top_sections = re.findall(r'<div[^>]*class="([^"]*e-con-boxed[^"]*)"[^>]*data-id="([^"]+)"', content_html)
    print("Boxed containers:", len(top_sections))
    for cls, did in top_sections:
        print("  Container ID:", did)
