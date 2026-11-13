import os
import re

files = [
    'team.html', 'about-us.html', 'anti-doping.html', 'safeguarding.html',
    'news.html', 'events.html', 'event-sanctioning.html', 'members-state.html', 'contact-us.html'
]

with open('full_subpages_content.txt', 'w', encoding='utf-8') as out:
    for fname in files:
        fpath = os.path.join('scraped_pages', fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            html = f.read()
        
        out.write(f"\n{'='*50}\nFILE: {fname}\n{'='*50}\n")
        
        # remove scripts and styles
        clean = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL | re.I)
        clean = re.sub(r'<style.*?</style>', '', clean, flags=re.DOTALL | re.I)
        
        # find content between header and footer
        # Header is usually data-elementor-id="104", Footer is data-elementor-id="105"
        h_end = clean.find('data-elementor-id="104"')
        if h_end != -1:
            clean = clean[clean.find('>', h_end)+1:]
        
        f_start = clean.find('data-elementor-id="105"')
        if f_start != -1:
            clean = clean[:f_start]
        
        # print tags and text
        for m in re.finditer(r'<(h[1-6]|p|li|span|a)[^>]*>(.*?)</\1>|<img[^>]+>', clean, re.DOTALL | re.I):
            s = m.group(0)
            if s.startswith('<img'):
                src = re.search(r'src=["\']([^"\']+)["\']', s)
                out.write(f"IMG: {src.group(1) if src else ''}\n")
            else:
                tag = m.group(1)
                text = re.sub(r'<[^>]+>', ' ', m.group(2)).strip()
                text = ' '.join(text.split())
                if len(text) > 1 and not text.startswith('{') and not text.startswith('/*'):
                    out.write(f"[{tag.upper()}] {text}\n")

print("Wrote full_subpages_content.txt")
