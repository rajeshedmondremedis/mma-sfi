with open('reference_archive/post-114.css', 'r', encoding='utf-8', errors='ignore') as f:
    css = f.read()

import re
# Find d26badd (the announcement)
pos = css.find('d26badd')
if pos != -1:
    print("d26badd CSS:\n", css[pos-100:pos+500])

# Find 249aabf (parent of about us)
pos2 = css.find('249aabf')
if pos2 != -1:
    print("249aabf CSS:\n", css[pos2-100:pos2+500])
