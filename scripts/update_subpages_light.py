# Update about-us.html
with open('about-us.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<p style="color: #ffffff; font-weight: 500;">', '<p style="color: #222222; font-weight: 500;">')
text = text.replace('background-color: #06070a;', 'background-color: #f8f9fa;')
text = text.replace('<h4 style="font-size: 1.6rem; color: #fff;">', '<h4 style="font-size: 1.6rem; color: #111111;">')
text = text.replace('background: linear-gradient(180deg, #090a0d 0%, #000 100%); text-align: center;', 'background-color: #f8f9fa; border-top: 1px solid rgba(0,0,0,0.06); text-align: center;')
text = text.replace('<h2 style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 20px;">', '<h2 style="font-size: clamp(2.5rem, 5vw, 4rem); margin-bottom: 20px; color: #111111;">')

with open('about-us.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Update anti-doping.html
with open('anti-doping.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<p style="font-size: 1.25rem; font-style: italic; color: #ffffff; line-height: 1.8;">', '<p style="font-size: 1.25rem; font-style: italic; color: #111111; line-height: 1.8;">')

with open('anti-doping.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Update contact-us.html
with open('contact-us.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<h3 style="font-size: 2.2rem; color: #ffffff; margin-bottom: 8px;">', '<h3 style="font-size: 2.2rem; color: #111111; margin-bottom: 8px;">')

with open('contact-us.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Update event-sanctioning.html
with open('event-sanctioning.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<h4 style="font-size: 1.4rem; color: #fff; margin-bottom: 6px;">', '<h4 style="font-size: 1.4rem; color: #111111; margin-bottom: 6px;">')
text = text.replace('<h3 style="font-size: 2.2rem; color: #ffffff; margin-bottom: 12px;">', '<h3 style="font-size: 2.2rem; color: #111111; margin-bottom: 12px;">')

with open('event-sanctioning.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Update members-state.html
with open('members-state.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<h3 style="font-size: 1.8rem; color: #fff;">', '<h3 style="font-size: 1.8rem; color: #111111;">')
text = text.replace('<h4 style="font-size: 1.4rem; color: #fff;">', '<h4 style="font-size: 1.4rem; color: #111111;">')

with open('members-state.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Subpages inline styles successfully updated!")
