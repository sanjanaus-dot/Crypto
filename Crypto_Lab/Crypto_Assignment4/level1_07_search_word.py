# Search for a word in cryptology.txt

word = input("Enter a word to search: ")

with open("cryptology.txt", "r") as file:
    content = file.read()

if word.lower() in content.lower():
    print("Word found")
else:
    print("Word not found")
