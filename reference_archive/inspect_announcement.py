with open('reference_archive/page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

pos = html.find('OFFICIAL ANNOUNCEMENT')
print(html[pos-300:pos+1500])
