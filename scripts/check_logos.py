import os, re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
    
    header_logo = re.findall(r'class="site-logo"[^>]*>[\s\S]*?<\/a>', content)
    footer_logo = re.findall(r'class="footer-logo"[^>]*>[\s\S]*?<\/div>', content)
    
    hl = header_logo[0].strip().replace('\n', ' ') if header_logo else 'NONE'
    fl = footer_logo[0].strip().replace('\n', ' ') if footer_logo else 'NONE'
    print(f"{f}:")
    print(f"  Header logo: {hl[:100]}")
    print(f"  Footer logo: {fl[:100]}")
