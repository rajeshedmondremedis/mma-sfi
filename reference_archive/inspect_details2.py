import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("--- COUNTERS ---")
for m in re.finditer(r'<div[^>]*class="[^"]*counter[^"]*"[^>]*>.*?</div>\s*</div>\s*</div>', html, re.DOTALL):
    chunk = m.group(0)
    print(chunk[:300])
    print("="*40)

# Let's search for numbers near Training Hours
th_pos = html.find('Training Hours')
print("Near Training Hours:\n", html[th_pos-200:th_pos+300])

rate_pos = html.find('Student Success Rate')
print("Near Student Success Rate:\n", html[rate_pos-200:rate_pos+300])

cert_pos = html.find('Certified Instructors')
print("Near Certified Instructors:\n", html[cert_pos-200:cert_pos+300])

print("\n--- TESTIMONIALS ---")
test_pos = html.find('Epic Journeys')
print("Near Testimonials:\n", html[test_pos:test_pos+3000])

print("\n--- FOOTER ---")
footer_pos = html.find('data-elementor-id="105"')
if footer_pos != -1:
    print(html[footer_pos:footer_pos+3000])
