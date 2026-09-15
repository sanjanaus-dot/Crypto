# Display lines containing the word "message"

with open("cryptology.txt", "r") as file:
    for line in file:
        if "message" in line.lower():
            print(line.strip())
