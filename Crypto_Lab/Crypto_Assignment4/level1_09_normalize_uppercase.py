# Convert alphabetic characters to uppercase

with open("cryptology.txt", "r") as infile:
    content = infile.read()

content = content.upper()

with open("normalized.txt", "w") as outfile:
    outfile.write(content)

print("Uppercase text saved in normalized.txt")
