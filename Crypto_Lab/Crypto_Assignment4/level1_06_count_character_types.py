# Count uppercase, lowercase, digits, spaces and special characters

with open("cryptology_no.txt", "r") as file:
    content = file.read()

uppercase = 0
lowercase = 0
digits = 0
spaces = 0
special = 0

for char in content:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isdigit():
        digits += 1
    elif char == " ":
        spaces += 1
    elif char != "\n":
        special += 1

print("Uppercase letters:", uppercase)
print("Lowercase letters:", lowercase)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)
