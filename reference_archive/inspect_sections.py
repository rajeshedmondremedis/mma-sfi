import re

with open('page.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Let's extract:
# 1. Top bar / Header info
# 2. Hero Section
# 3. Stats / Counters
# 4. About Us / Who We Are / Vision & Mission / Core Objectives
# 5. President's Message
# 6. Affiliations (FIMA, GAMMA, AMMA) with certificates / logos
# 7. Our Services (Precision Punches, Mastery Unleashed, Integrity, etc.)
# 8. News & Updates (Articles / Blog posts)
# 9. Shaping the Future of Indian MMA (banner / CTA)
# 10. Our Trainers / Warriors (Jason Mamoa, Lisa Rodriguez, etc.)
# 11. Testimonials (Epic Journeys, Real Results)
# 12. Footer

# Let's write a script to search for sections by heading or content
sections_to_find = [
    "Training Hours", "Student Success Rate", "Certified Instructors",
    "Who We Are", "Vision", "Mission", "Core Objectives", "President's Message",
    "Affiliations", "FIMA", "GAMMA", "AMMA",
    "Our Services", "Precision Punches", "Mastery Unleashed",
    "In the News", "SHAPING THE FUTURE OF INDIAN MMA",
    "Meet the Warriors", "Epic Journeys", "Our Address"
]

for s in sections_to_find:
    pos = html.find(s)
    print(f"Heading '{s}': pos={pos}")
    if pos != -1:
        snippet = html[max(0, pos-200):min(len(html), pos+600)]
        # clean html
        clean = re.sub(r'<[^>]+>', ' ', snippet)
        clean = ' '.join(clean.split())
        print(f"   Context: {clean[:200]}...")
