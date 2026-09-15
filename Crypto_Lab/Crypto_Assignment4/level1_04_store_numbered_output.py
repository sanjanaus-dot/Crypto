# Store numbered lines in cryptology_no.txt

with open("cryptology.txt", "r") as infile:
    with open("cryptology_no.txt", "w") as outfile:
        line_number = 1

        for line in infile:
            outfile.write(str(line_number) + " " + line)
            line_number += 1

print("Output saved in cryptology_no.txt")
