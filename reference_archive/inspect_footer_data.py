import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

footer_pos = html.find('data-elementor-id="105"')
footer_html = html[footer_pos:]

print("--- FOOTER HEADINGS ---")
for h in re.finditer(r'<h[1-6][^>]*>(.*?)</h[1-6]>', footer_html):
    print("Heading:", re.sub(r'<[^>]+>', '', h.group(1)).strip())

print("\n--- FOOTER PARAGRAPHS ---")
for p in re.finditer(r'<p[^>]*>(.*?)</p>', footer_html):
    print("P:", re.sub(r'<[^>]+>', '', p.group(1)).strip())

print("\n--- FOOTER LINKS ---")
for a in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', footer_html, re.DOTALL):
    text = re.sub(r'<[^>]+>', '', a.group(2)).strip()
    href = a.group(1)
    if text:
        print(f"  {text} -> {href}")
