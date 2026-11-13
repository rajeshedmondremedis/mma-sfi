import re

with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's find every data-widget_type in order
pos = 0
widgets = []
for m in re.finditer(r'data-widget_type="([^"]+)"', html):
    start = m.start()
    w_type = m.group(1)
    # grab the next 1500 chars
    chunk = html[start:start+1500]
    # find closing tag of widget container if possible
    text = re.sub(r'<script.*?</script>', '', chunk, flags=re.DOTALL)
    text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = ' '.join(text.split())
    # find images
    imgs = re.findall(r'src=["\']([^"\']+)["\']', chunk)
    widgets.append((w_type, text[:160], imgs[:2]))

print(f"Total widgets: {len(widgets)}")
with open('original_widgets_flow.txt', 'w', encoding='utf-8') as out:
    for i, (w, t, imgs) in enumerate(widgets):
        out.write(f"\n[{i+1}] {w}\n")
        out.write(f"  TEXT: {t}\n")
        if imgs:
            out.write(f"  IMGS: {imgs}\n")

print("Wrote original_widgets_flow.txt")
