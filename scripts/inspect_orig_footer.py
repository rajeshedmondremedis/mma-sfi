import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# find footer tag or elementor-type="footer"
m = re.search(r'data-elementor-type="footer"[^>]*>([\s\S]*?)<\/div>\s*<\/div>\s*<\/div>', text)
if m:
    print("Found footer:")
    # print all images in footer
    imgs = re.findall(r'<img[^>]+src="([^">]+)"', m.group(0))
    print("Footer images:", imgs)
    # print text
    # remove tags
    clean_text = re.sub(r'<[^>]+>', ' ', m.group(0))
    print("Footer text snippet:", ' '.join(clean_text.split()[:80]))
else:
    print("Footer not found by regex")
