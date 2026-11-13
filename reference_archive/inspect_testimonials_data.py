import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

test_pos = html.find('elementskit-testimonial')
test_chunk = html[test_pos:test_pos+15000]

imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', test_chunk)
print("Testimonial images:", imgs)

names = re.findall(r'<h[3-5][^>]*class="[^"]*elementskit-profile-name[^"]*"[^>]*>(.*?)</h[3-5]>', test_chunk)
print("Testimonial names:", names)

desigs = re.findall(r'<span[^>]*class="[^"]*elementskit-profile-desg[^"]*"[^>]*>(.*?)</span>', test_chunk)
print("Testimonial designations:", desigs)
