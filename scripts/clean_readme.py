with open('README.md', 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

print("README length:", len(text))
print("First 200 chars:\n", text[:200])

# Clean any null bytes or non-printable chars
cleaned = text.replace('\x00', '')
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(cleaned)

print("Cleaned README.md")
