import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's inspect all Elementor widgets/sections
sections = re.findall(r'<section[^>]*>(.*?)</section>', html, re.DOTALL)
print(f"Total <section> tags: {len(sections)}")

# Let's inspect elementor containers / sections
# In modern elementor or classic:
e_containers = re.findall(r'class="[^"]*(?:elementor-section|elementor-container|e-con)[^"]*"', html)
print(f"Total elementor containers/sections: {len(e_containers)}")

# Let's extract full text blocks to understand all the content on the page
clean_text = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
clean_text = re.sub(r'<style.*?</style>', '', clean_text, flags=re.DOTALL | re.IGNORECASE)

# Let's print the top bar, header, hero, and every major section
with open('extracted_structure.txt', 'w', encoding='utf-8') as out:
    # Let's write all text snippets with their tags
    for tag in ['header', 'nav', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'span']:
        for m in re.finditer(rf'<{tag}[^>]*>(.*?)</{tag}>', clean_text, re.DOTALL | re.IGNORECASE):
            inner = re.sub(r'<[^>]+>', ' ', m.group(1))
            inner = ' '.join(inner.split())
            if len(inner) > 2:
                out.write(f"[{tag.upper()}] {inner}\n")

print("Wrote extracted_structure.txt")
