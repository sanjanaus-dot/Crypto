# Alternative Level 1 program
# Accept five lines, process the file and display the result.

with open("input.txt", "w") as file:
    for i in range(5):
        text = input("Enter line " + str(i + 1) + ": ")
        file.write(text + "\n")

with open("input.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()
alphabetic = 0
digits = 0
spaces = 0
special = 0

for char in content:
    if char.isalpha():
        alphabetic += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    elif char != "\n":
        special += 1

print("Number of lines:", len(lines))
print("Number of words:", len(words))
print("Alphabetic characters:", alphabetic)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

with open("processed.txt", "w") as file:
    file.write(content.upper())

print("\nProcessed contents:")
with open("processed.txt", "r") as file:
    print(file.read())
