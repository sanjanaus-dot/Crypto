# Print lines containing only alphabetic characters

with open("cryptology_no.txt", "r") as file:
    for line in file:
        text = line.strip()

        if text.isalpha():
            print(text)
