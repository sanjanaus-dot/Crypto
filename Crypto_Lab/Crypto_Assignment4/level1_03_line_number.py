# Read file one line at a time and display line number

with open("cryptology.txt", "r") as file:
    line_number = 1

    for line in file:
        print(line_number, line.strip())
        line_number += 1
