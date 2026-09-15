# Simple simulation of the tac command
# tac displays file lines in reverse order

with open("cryptology.txt", "r") as file:
    lines = file.readlines()

for line in reversed(lines):
    print(line.strip())
