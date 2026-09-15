# Count lines, words and characters in cryptology.txt

with open("cryptology.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
characters = len(content)

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Number of characters:", characters)
