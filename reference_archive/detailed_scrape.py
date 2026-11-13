import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's see the header / top-bar
# Look for phone, email, social links, menu items
print("--- CONTACT INFO & TOPBAR ---")
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', html)
print("Emails found:", set(emails))
phones = re.findall(r'\+?\d[\d\s-]{8,}\d', html)
print("Phones (sample):", set(phones[:10]))

# Navigation menu links
print("\n--- MENU LINKS ---")
nav_links = re.findall(r'<li[^>]*class="[^"]*menu-item[^"]*"[^>]*>\s*<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', html, re.DOTALL)
for href, text in nav_links:
    clean_t = re.sub(r'<[^>]+>', '', text).strip()
    print(f"  {clean_t} -> {href}")

# Find all e-con-inner or top-level e-con
print("\n--- TOP-LEVEL CONTAINERS ---")
# Let's inspect the main elementor page content
# The elementor wrapper is usually <div class="elementor elementor-114 ...">
main_match = re.search(r'<div class="elementor elementor-114[^"]*"[^>]*>(.*?)</div>\s*<!-- \.elementor -->', html, re.DOTALL)
if not main_match:
    main_match = re.search(r'<div data-elementor-type="wp-page" data-elementor-id="114"[^>]*>(.*?)</div>\s*</div>\s*<!-- \.entry-content -->', html, re.DOTALL)

# Let's search for header template and footer template
header_match = re.search(r'data-elementor-id="104"[^>]*>(.*?)<!-- \.elementor-104 -->', html, re.DOTALL)
footer_match = re.search(r'data-elementor-id="105"[^>]*>(.*?)<!-- \.elementor-105 -->', html, re.DOTALL)

print("Header template found:", bool(header_match))
print("Footer template found:", bool(footer_match))

# Let's inspect the sections in order!
