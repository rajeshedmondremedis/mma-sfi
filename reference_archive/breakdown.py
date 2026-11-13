import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's write a script that breaks down the page into clean sections
# We'll save each section's title, text, images, and button links into a readable file
with open('sections_breakdown.txt', 'w', encoding='utf-8') as out:
    # Let's inspect the counters
    out.write("=== COUNTERS / STATS ===\n")
    counters = re.findall(r'<div[^>]*class="[^"]*counter[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
    for c in re.findall(r'(?:Training Hours|Student Success Rate|Certified Instructors)[\s\S]{1,500}?(?:odometer|counter-number)[\s\S]{1,200}?</div>', html):
        out.write(c + "\n---\n")

    # Let's inspect the entire body from pos 49000 to pos 140000
    sub = html[49000:145000]
    out.write("\n=== HEADINGS AND THEIR SURROUNDING TEXT ===\n")
    for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>', sub, re.DOTALL | re.IGNORECASE):
        tag = m.group(1)
        h_text = re.sub(r'<[^>]+>', '', m.group(2)).strip()
        # Find subsequent paragraph or text
        pos = m.end()
        next_chunk = sub[pos:pos+800]
        p_m = re.findall(r'<p[^>]*>(.*?)</p>', next_chunk, re.DOTALL | re.IGNORECASE)
        imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', next_chunk, re.IGNORECASE)
        links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', next_chunk, re.DOTALL | re.IGNORECASE)

        out.write(f"\n[{tag.upper()}] {h_text}\n")
        if p_m:
            for p in p_m[:3]:
                out.write(f"  P: {re.sub(r'<[^>]+>', '', p).strip()}\n")
        if imgs:
            out.write(f"  IMGS: {imgs[:3]}\n")
        if links:
            cleaned_links = [(l[0], re.sub(r'<[^>]+>', '', l[1]).strip()) for l in links if l[0] != '#']
            if cleaned_links:
                out.write(f"  LINKS: {cleaned_links[:3]}\n")

print("Wrote sections_breakdown.txt")
