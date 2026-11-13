import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's extract clean structured sections:
with open('page_extracted.txt', 'w', encoding='utf-8') as out:
    # 1. Header (template 104)
    out.write("=================== HEADER ===================\n")
    h_start = html.find('data-elementor-id="104"')
    h_end = html.find('data-elementor-id="114"')
    if h_start != -1 and h_end != -1:
        header_html = html[h_start:h_end]
        for line in re.findall(r'<[^>]+>|[^<]+', header_html):
            line = line.strip()
            if line and not line.startswith('<'):
                out.write(f"TEXT: {line}\n")
            elif line.startswith('<img'):
                out.write(f"IMG: {line}\n")
            elif line.startswith('<a ') and 'href=' in line:
                out.write(f"LINK: {line}\n")
            elif 'fa-' in line or 'icon' in line:
                out.write(f"ICON/CLASS: {line[:120]}\n")

    # 2. Page Content (template 114)
    out.write("\n=================== PAGE BODY ===================\n")
    p_start = html.find('data-elementor-id="114"')
    p_end = html.find('data-elementor-id="105"')
    if p_start != -1:
        page_html = html[p_start:p_end] if p_end != -1 else html[p_start:]
        for line in re.findall(r'<[^>]+>|[^<]+', page_html):
            line = line.strip()
            if line and not line.startswith('<') and not line.startswith('{') and not line.startswith('/*'):
                out.write(f"TEXT: {line}\n")
            elif line.startswith('<img'):
                out.write(f"IMG: {line}\n")
            elif line.startswith('<a ') and 'href=' in line:
                out.write(f"LINK: {line}\n")
            elif any(k in line for k in ['counter-number', 'data-duration', 'data-to-value', 'odometer']):
                out.write(f"COUNTER: {line}\n")

    # 3. Footer (template 105)
    out.write("\n=================== FOOTER ===================\n")
    if p_end != -1:
        footer_html = html[p_end:]
        for line in re.findall(r'<[^>]+>|[^<]+', footer_html):
            line = line.strip()
            if line and not line.startswith('<') and not line.startswith('{') and not line.startswith('/*'):
                out.write(f"TEXT: {line}\n")
            elif line.startswith('<img'):
                out.write(f"IMG: {line}\n")
            elif line.startswith('<a ') and 'href=' in line:
                out.write(f"LINK: {line}\n")

print("Wrote page_extracted.txt")
