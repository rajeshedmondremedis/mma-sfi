import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Counter values
counters = re.findall(r'<div[^>]*class="[^"]*rkit-counter[^"]*"[^>]*>.*?</div>\s*</div>', html, re.DOTALL)
print(f"Total rkit-counter found: {len(counters)}")
for i, c in enumerate(counters):
    print(f"Counter {i}:")
    print(c)
    print("-"*40)

# Testimonial slides
test_chunk = html[html.find('elementskit-testimonial'):html.find('elementskit-testimonial') + 15000]
slides = re.findall(r'<div class="swiper-slide">(.*?)</div>\s*</div>\s*</div>\s*</div>', test_chunk, re.DOTALL)
print(f"Total testimonial slides found: {len(slides)}")
for i, s in enumerate(slides):
    clean = re.sub(r'<[^>]+>', ' ', s)
    clean = ' '.join(clean.split())
    print(f"Slide {i}: {clean[:300]}")
