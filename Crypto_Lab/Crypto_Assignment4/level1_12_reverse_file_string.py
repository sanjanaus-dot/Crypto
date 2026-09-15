# Read a string from a file and reverse it

with open("cryptology.txt", "r") as file:
    text = file.read()

print("Reversed string:")
print(text[::-1])
